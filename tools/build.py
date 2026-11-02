#!/usr/bin/env python3
"""Create deterministic native host bundles and a complete CCS maintainer kit."""
import argparse
from pathlib import Path, PurePosixPath
import sys
import json
import os
import re
from urllib.parse import urlsplit, unquote
from ccs import ROOT, HOSTS, Invalid, validate, runtime_files, make_zip


PROTECTED = {'standard', 'companions', 'adapters', 'templates', 'docs', 'examples', 'tests', 'tools', 'scripts'}


def source_files() -> dict[str, bytes]:
    manifest_path = ROOT / 'distribution-files.json'
    if manifest_path.is_symlink():
        raise Invalid('source manifest must not be a symlink')
    names = json.loads(manifest_path.read_text())
    if not isinstance(names, list) or any(not isinstance(n, str) for n in names) or len(names) != len(set(names)):
        raise Invalid('source manifest must contain unique relative paths')
    expected = set(names)
    if 'distribution-files.json' not in expected:
        raise Invalid('source manifest must include itself')
    for name in expected:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or str(path) != name or '\\' in name:
            raise Invalid('invalid source manifest path')
        if any(re.search(r'(?i)^(?:\.env.*|.*credentials?.*|.*secrets?.*|.*tokens?.*)$', part) for part in path.parts):
            raise Invalid('restricted source path')
    actual = set()
    ignored_roots = {'dist', 'releases', '.git', '.harness', 'graft', '.local-history'}
    ignored_root_files = {'CCS-1.0.md', 'CREATE-COMPANION-PROMPT.md'}
    for directory, dirs, files in os.walk(ROOT, followlinks=False):
        folder = Path(directory)
        is_root = folder == ROOT
        dirs[:] = [d for d in dirs if d not in {'__pycache__', '.DS_Store'} and not (is_root and (d in ignored_roots or d in ignored_root_files))]
        for name in [*dirs, *files]:
            if name == '.DS_Store' or (is_root and (name in ignored_roots or name in ignored_root_files)):
                continue
            path = folder / name
            relative = path.relative_to(ROOT).as_posix()
            if path.is_symlink():
                raise Invalid(f'cannot distribute symlink: {relative}')
            if name in files:
                actual.add(relative)
    if actual != expected:
        raise Invalid('source files differ from the reviewed distribution-files.json allowlist')
    # Validate the complete inventory before opening any payload file.
    return {name: (ROOT / name).read_bytes() for name in sorted(expected)}


def check_links(payload: dict[str, bytes]):
    for name, data in payload.items():
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'\]\(([^)]+)\)', data.decode('utf-8')):
            parsed = urlsplit(link.strip('<>'))
            if parsed.path == '{{skill_path}}' and name.endswith('/adapter/cue.md'):
                continue  # Resolved and validated by the host adapter, not a file link.
            if parsed.scheme in {'https', 'http', 'mailto'} or not parsed.path:
                continue
            if parsed.scheme or parsed.path.startswith('/'):
                raise Invalid(f'nonportable link in {name}')
            resolved = ((ROOT / name).parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                raise Invalid(f'escaping link in {name}')
            target = resolved.relative_to(ROOT.resolve()).as_posix()
            if target not in payload and not any(n.startswith(target.rstrip('/') + '/') for n in payload):
                raise Invalid(f'link absent from distribution: {name} -> {link}')


def output_name(companion: str, host: str, version: str) -> str:
    return f'{companion}-{host}-{version}.zip'


def build(output: Path, companion: str = 'git-companion') -> dict[str, bytes]:
    kit_payload = source_files()
    info = validate(companion)
    version = info['version']
    packages = {}
    for host in HOSTS:
        packages[output_name(companion, host, version)] = make_zip(runtime_files(companion, host))
    for name, data in packages.items():
        kit_payload[f'releases/{name}'] = data
    check_links(kit_payload)
    kit_name = f'contextual-companion-kit-{info["ccs_version"]}-{companion}-{version}.zip'
    packages[kit_name] = make_zip(kit_payload)
    return packages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path, help='new or empty directory for generated ZIPs')
    parser.add_argument('--companion', default='git-companion')
    args = parser.parse_args()
    output = args.output.absolute()
    if output.is_symlink():
        raise Invalid('output must not be a symlink')
    output = output.resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise Invalid('output must be absent or empty, no existing files were changed')
    if output == ROOT or output in ROOT.parents:
        raise Invalid('output cannot be the project root or an ancestor')
    if any(output.is_relative_to(ROOT / path) for path in PROTECTED):
        raise Invalid('output cannot be placed inside source-owned directories')
    packages = build(output, args.companion)
    output.mkdir(parents=True, exist_ok=True)
    for filename, payload in packages.items():
        with (output / filename).open('xb') as file:
            file.write(payload)
        print(f'BUILT {filename}: {len(payload):,} bytes')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f'Packaging refused: {exc}', file=sys.stderr)
        sys.exit(1)
