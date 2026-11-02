"""Shared validation, packaging and safe adapter helpers for CCS 1.0.

The code depends only on the Python standard library. For full JSON Schema checks,
install the optional `jsonschema` package; the own strict structural validation is
always performed.
"""
from __future__ import annotations

from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, unquote
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import io
import json
import re
import stat

ROOT = Path(__file__).resolve().parent.parent
COMPANIONS = ROOT / 'companions'
HOSTS = ('copilot', 'claude', 'codex')
MANIFEST_KEYS = {'ccs_version', 'id', 'version', 'kind', 'domain', 'activation', 'adaptation', 'authority', 'evaluation'}
START = '<!-- BEGIN CCS:{id} -->'
END = '<!-- END CCS:{id} -->'


class Invalid(ValueError):
    pass


def read_text(path: Path) -> str:
    if not path.is_file() or path.is_symlink():
        raise Invalid(f'missing, non-file or symlink: {path}')
    data = path.read_bytes()
    if b'\0' in data:
        raise Invalid(f'NUL in text file: {path}')
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError as error:
        raise Invalid(f'non-UTF8 file: {path}') from error


def source_dir(companion: str) -> Path:
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', companion) or len(companion) > 64:
        raise Invalid(f'invalid companion ID: {companion}')
    directory = COMPANIONS / companion
    if not directory.is_dir() or directory.is_symlink():
        raise Invalid(f'no such companion: {companion}')
    return directory


def manifest(companion: str) -> dict:
    folder = source_dir(companion)
    raw = json.loads(read_text(folder / 'companion.json'))
    if not isinstance(raw, dict) or raw.keys() != MANIFEST_KEYS:
        raise Invalid('manifest has missing or unknown keys')
    if raw['ccs_version'] not in {'1.0.0', '1.0.1'} or raw['id'] != companion or raw['kind'] != 'contextual-educational-companion':
        raise Invalid('manifest identity, kind, or CCS version incorrect')
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', raw['version']):
        raise Invalid('invalid semver')
    for section, required in {
        'domain': ('purpose', 'includes', 'excludes'),
        'activation': ('direct', 'implicit', 'followups', 'negative'),
        'adaptation': ('dimensions', 'signals', 'no_profiling'),
        'authority': ('execution_owner', 'workflow_owner', 'extra_gates', 'companion_tool_calls', 'required_frameworks'),
        'evaluation': ('cases', 'discovery_requires_live_test'),
    }.items():
        value = raw[section]
        if not isinstance(value, dict) or set(value) != set(required):
            raise Invalid(f'manifest.{section} keys invalid')
    for section, keys in {
        'domain': ('includes', 'excludes'),
        'activation': ('direct', 'implicit', 'followups', 'negative'),
        'adaptation': ('dimensions', 'signals'),
    }.items():
        for key in keys:
            val = raw[section][key]
            if not isinstance(val, list) or not val or any(not isinstance(v, str) or not v.strip() for v in val) or len(set(val)) != len(val):
                raise Invalid(f'empty, duplicated, or malformed manifest {section}.{key}')
    if not isinstance(raw['domain']['purpose'], str) or not raw['domain']['purpose'].strip():
        raise Invalid('manifest.domain.purpose must be nonempty')
    if raw['adaptation']['no_profiling'] is not True:
        raise Invalid('profiling must be disabled')
    authority = raw['authority']
    if authority != {
        'execution_owner': 'host-agent',
        'workflow_owner': 'existing-project-workflow',
        'extra_gates': False,
        'companion_tool_calls': False,
        'required_frameworks': [],
    }:
        raise Invalid('CCS authority boundaries are non-negotiable')
    evaluation = raw['evaluation']
    if evaluation['cases'] != f'tests/cases/{companion}.json' or evaluation['discovery_requires_live_test'] is not True:
        raise Invalid('missing standard evaluation contract')
    if not (ROOT / evaluation['cases']).is_file():
        raise Invalid('missing test cases file')
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        pass
    else:
        schema = json.loads(read_text(ROOT / 'standard/companion.schema.json'))
        errors = sorted(Draft202012Validator(schema).iter_errors(raw), key=lambda error: str(error.path))
        if errors:
            raise Invalid(f'JSON schema validation failed: {errors[0].message}')
    return raw


def check_skill(companion: str, info: dict) -> dict[str, bytes]:
    folder = source_dir(companion)
    skill_text = read_text(folder / 'SKILL.md')
    header = re.match(r'\A---\n(.*?)\n---\n', skill_text, re.S)
    if not header:
        raise Invalid('SKILL.md requires YAML frontmatter')
    body = header.group(1)
    # This project intentionally uses a conservative portable YAML subset.
    name = re.search(r'^name: ([a-z0-9-]+)$', body, re.M)
    description = re.search(r'^description: ("[^\n]*")$', body, re.M)
    profile = re.search(r'^  ccs-profile: ("[^\n]*")$', body, re.M)
    version = re.search(r'^  companion-version: ("[^\n]*")$', body, re.M)
    if not all((name, description, profile, version)):
        raise Invalid('SKILL.md missing required portable metadata')
    try:
        desc, ccs, ver = [json.loads(match.group(1)) for match in (description, profile, version)]
    except json.JSONDecodeError as error:
        raise Invalid('invalid frontmatter quoted scalar') from error
    if name.group(1) != companion or '--' in companion or not desc.strip() or len(desc) > 1024:
        raise Invalid('Agent Skills name or description invalid')
    if ccs != info['ccs_version'] or ver != info['version']:
        raise Invalid('SKILL.md and manifest versions conflict')
    if 'Use ' not in desc and 'use ' not in desc:
        raise Invalid('description missing positive triggering language')
    if 'Do not' not in desc and 'not for' not in desc:
        raise Invalid('description missing negative triggering language')
    if len(skill_text.splitlines()) > 500:
        raise Invalid('skill exceeds recommended 500 lines')
    if '[TODO' in skill_text or 'Replace this example description' in skill_text:
        raise Invalid('unfinished template skill')
    files = {}
    for entry in folder.rglob('*'):
        if entry.is_symlink():
            raise Invalid(f'symlink in companion source: {entry}')
        if not entry.is_file():
            continue
        relative = entry.relative_to(folder).as_posix()
        if relative in ('SKILL.md', 'README.md', 'companion.json') or re.fullmatch(r'references/[a-z0-9-]+\.md', relative):
            files[relative] = entry.read_bytes()
        elif relative == 'adapter/cue.md':
            continue
        else:
            raise Invalid(f'unreviewed companion runtime file: {relative}')
    if not all(rel in files for rel in ('SKILL.md', 'README.md', 'companion.json')):
        raise Invalid('missing required runtime file')
    for rel, data in files.items():
        if rel.endswith('.md'):
            text = read_text(folder / rel)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                link = link.strip('<>')
                parsed = urlsplit(link)
                if parsed.scheme in ('http', 'https', 'mailto') or (not parsed.path and parsed.fragment):
                    continue
                if parsed.scheme or parsed.path.startswith('/'):
                    raise Invalid(f'bad local link: {rel} -> {link}')
                target = (folder / rel).parent / unquote(parsed.path)
                resolved = target.resolve()
                if not resolved.is_relative_to(folder) or not resolved.is_file() or resolved.is_symlink():
                    raise Invalid(f'broken or escaping link: {rel} -> {link}')
                if resolved.relative_to(folder.resolve()).as_posix() not in files:
                    raise Invalid(f'runtime link not packaged: {rel} -> {link}')
    cue = read_text(folder / 'adapter/cue.md')
    if cue.count('{{skill_path}}') != 1 or re.search(r'\{\{(?!skill_path\}\})', cue):
        raise Invalid('cue must have exactly one {{skill_path}} placeholder')
    if not 45 <= len(cue.split()) <= 110:
        raise Invalid('always-on cue should be 45–110 words')
    return files


def host_spec(host: str) -> dict:
    if host not in HOSTS:
        raise Invalid(f'unknown host {host}')
    spec = json.loads(read_text(ROOT / 'adapters' / f'{host}.json'))
    if spec['host'] != host or '{id}' not in spec['skill_dir']:
        raise Invalid(f'bad host adapter: {host}')
    return spec


def cue_block(companion: str, host: str) -> str:
    spec = host_spec(host)
    skillpath = spec['skill_dir'].replace('{id}', companion) + '/SKILL.md'
    if host == 'copilot':
        # Root instruction lives under `.github/`.
        skillpath = skillpath.removeprefix('.github/')
    text = read_text(source_dir(companion) / 'adapter/cue.md')
    cue = text.replace('{{skill_path}}', skillpath)
    return f'{START.format(id=companion)}\n{cue.rstrip()}\n{END.format(id=companion)}\n'


def runtime_files(companion: str, host: str) -> dict[str, bytes]:
    info = manifest(companion)
    files = check_skill(companion, info)
    skill_path = host_spec(host)['skill_dir'].replace('{id}', companion)
    return {f'{skill_path}/{rel}': data for rel, data in files.items()}


def make_zip(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with ZipFile(buffer, 'w', compression=ZIP_DEFLATED) as archive:
        for rel, data in sorted(files.items()):
            posix = PurePosixPath(rel)
            if posix.is_absolute() or '..' in posix.parts or '\\' in rel or not rel or rel.startswith('/'):
                raise Invalid(f'unsafe archive path: {rel}')
            info = ZipInfo(rel, (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, data)
    result = buffer.getvalue()
    with ZipFile(io.BytesIO(result)) as check:
        if check.testzip() or len(check.namelist()) != len(set(check.namelist())):
            raise Invalid('corrupt or duplicate archive')
        if set(check.namelist()) != set(files):
            raise Invalid('archive contents differ from allowlist')
        if any(check.read(rel) != data for rel, data in files.items()):
            raise Invalid('archive bytes differ from source')
    return result


def check_case_pack(companion: str) -> list:
    path = ROOT / 'tests' / 'cases' / f'{companion}.json'
    cases = json.loads(read_text(path))
    if not isinstance(cases, list) or len(cases) < 12:
        raise Invalid('need at least 12 behaviour cases')
    ids = set()
    categories = set()
    for case in cases:
        if not isinstance(case, dict) or set(case) != {'id', 'category', 'context', 'user', 'expected', 'forbidden'}:
            raise Invalid('case fields invalid')
        if case['id'] in ids or any(not isinstance(case[key], str) or not case[key].strip() for key in case):
            raise Invalid('duplicate case or empty field')
        ids.add(case['id'])
        categories.add(case['category'])
    if not {'direct', 'implicit', 'followup', 'negative', 'execution', 'expert', 'evidence', 'security'} <= categories:
        raise Invalid('behaviour test coverage missing a required category')
    return cases


def validate(companion: str) -> dict:
    info = manifest(companion)
    check_skill(companion, info)
    check_case_pack(companion)
    for host in HOSTS:
        host_spec(host)
        cue_block(companion, host)
        runtime_files(companion, host)
    return info
