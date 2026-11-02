"""Deterministic artifact and safe-distribution tests; NOT a model-behaviour test."""
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from ccs import (HOSTS, Invalid, check_case_pack, check_skill, cue_block,
                 host_spec, manifest, make_zip, runtime_files, validate)
from build import build
import build as build_module
from install import merge_cue, plan_install, write_plan


class CompanionContractTests(unittest.TestCase):
    def test_manifest_and_standard_are_valid(self):
        info = validate('git-companion')
        self.assertEqual(info['ccs_version'], '1.0.1')
        self.assertEqual(info['version'], '0.8.2')
        self.assertFalse(info['authority']['extra_gates'])
        self.assertFalse(info['authority']['companion_tool_calls'])

    def test_skill_frontmatter_is_portable_and_small(self):
        info = manifest('git-companion')
        files = check_skill('git-companion', info)
        self.assertIn('SKILL.md', files)
        self.assertIn('references/vscode-git.md', files)
        self.assertNotIn('adapter/cue.md', files)
        self.assertLessEqual(len(files['SKILL.md'].decode().splitlines()), 500)

    def test_behavior_case_coverage(self):
        cases = check_case_pack("git-companion")
        self.assertGreaterEqual(len(cases), 20)
        self.assertEqual(len(cases), len({case['id'] for case in cases}))
        self.assertIn('negative', {case['category'] for case in cases})

    def test_host_paths_and_cue_consistency(self):
        for host in HOSTS:
            with self.subTest(host=host):
                spec = host_spec(host)
                cue = cue_block('git-companion', host)
                self.assertEqual(cue.count('<!-- BEGIN CCS:git-companion -->'), 1)
                self.assertEqual(cue.count('<!-- END CCS:git-companion -->'), 1)
                expected = spec['skill_dir'].replace('{id}', 'git-companion')
                self.assertIn(expected.removeprefix('.github/') + '/SKILL.md', cue)

    def test_native_bundles_contain_only_skill_files(self):
        for host in HOSTS:
            with self.subTest(host=host):
                files = runtime_files('git-companion', host)
                prefix = host_spec(host)['skill_dir'].replace('{id}', 'git-companion') + '/'
                self.assertTrue(all(path.startswith(prefix) for path in files))
                self.assertTrue(any(name.endswith('/SKILL.md') for name in files))
                self.assertFalse(any('/hooks/' in name for name in files))
                self.assertFalse(any(name.endswith('AGENTS.md') or name.endswith('CLAUDE.md') for name in files))
                payload = make_zip(files)
                with ZipFile(io.BytesIO(payload)) as archive:
                    self.assertEqual(set(archive.namelist()), set(files))
                    self.assertIsNone(archive.testzip())
                    for entry in archive.infolist():
                        self.assertNotEqual((entry.external_attr >> 16) & 0o170000, 0o120000)

    def test_build_is_repeatable_and_kit_contains_native_archives(self):
        first = build(pathlib.Path('/tmp/a'))
        second = build(pathlib.Path('/tmp/b'))
        self.assertEqual(first, second)
        self.assertEqual(len(first), 4)
        kitname = next(name for name in first if name.startswith('contextual-companion-kit-'))
        with ZipFile(io.BytesIO(first[kitname])) as archive:
            names = set(archive.namelist())
            self.assertIn('standard/CCS-1.0.md', names)
            self.assertIn('templates/example-companion/SKILL.md', names)
            self.assertIn('tools/install.py', names)
            self.assertIn('tests/test_ccs.py', names)
            for host in HOSTS:
                native = f'git-companion-{host}-0.8.2.zip'
                self.assertEqual(archive.read('releases/' + native), first[native])

    def test_context_adapter_is_optional_and_stays_out_of_native_installations(self):
        """@GC-22 Activity context belongs to the host, never canonical teaching."""
        packages = build(pathlib.Path('/tmp/context-kit'))
        kit = next(data for name, data in packages.items()
                   if name.startswith('contextual-companion-kit-'))
        with ZipFile(io.BytesIO(kit)) as archive:
            self.assertIn('docs/CONTEXT-ADAPTERS.md', archive.namelist())
            self.assertIn('templates/context-adapter.md', archive.namelist())
        canonical = (ROOT / 'companions/git-companion/SKILL.md').read_bytes()
        for host in HOSTS:
            with self.subTest(host=host), tempfile.TemporaryDirectory() as folder:
                target = pathlib.Path(folder)
                context = target / 'activity-context.md'
                context.write_text('Activity-specific material owned by this workspace.\n')
                before = context.read_bytes()
                write_plan(plan_install(target, host, 'git-companion'))
                skill_dir = target / host_spec(host)['skill_dir'].replace('{id}', 'git-companion')
                self.assertEqual((skill_dir / 'SKILL.md').read_bytes(), canonical)
                self.assertEqual(context.read_bytes(), before)
                actual = {p.relative_to(target).as_posix()
                          for p in target.rglob('*') if p.is_file()}
                expected = set(runtime_files('git-companion', host))
                expected.update({host_spec(host)['instruction_file'], 'activity-context.md'})
                self.assertEqual(actual, expected)

    def test_previous_profile_manifest_remains_compatible(self):
        """@GC-23 The clarification preserves the CCS 1.0.0 manifest contract."""
        import ccs
        original_read = ccs.read_text

        def legacy_manifest(path):
            text = original_read(path)
            if path == ROOT / 'companions/git-companion/companion.json':
                data = json.loads(text)
                data['ccs_version'] = '1.0.0'
                return json.dumps(data)
            return text

        with patch.object(ccs, 'read_text', legacy_manifest):
            info = manifest('git-companion')
        self.assertEqual(info['ccs_version'], '1.0.0')
        self.assertEqual(info['authority']['required_frameworks'], [])

    def test_reject_unsafe_archive_name(self):
        for name in ('../secret', '/absolute', 'a\\bad'):
            with self.subTest(name=name):
                with self.assertRaises(Invalid):
                    make_zip({name: b'data'})


class PackagingBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.copy = pathlib.Path(self.temp.name) / 'source'
        shutil.copytree(ROOT, self.copy,
                        ignore=shutil.ignore_patterns('dist', 'releases', '__pycache__', 'graft', '.local-history', '.git', '.harness'))

    def test_local_history_is_excluded_without_traversal_or_reads(self):
        """@GC-24 Local draft archives never enter the presentation package."""
        with patch.object(build_module, 'ROOT', self.copy):
            before = build_module.source_files()
        archive = self.copy / '.local-history' / 'drafts'
        archive.mkdir(parents=True)
        draft = archive / 'notes.md'
        draft.write_text('Synthetic development history, not proposal content.\n')
        visited = []
        reads = []
        real_walk = build_module.os.walk
        real_read = pathlib.Path.read_bytes

        def observed_walk(*args, **kwargs):
            for directory, dirs, files in real_walk(*args, **kwargs):
                visited.append(pathlib.Path(directory))
                yield directory, dirs, files

        def observed_read(path):
            if path == draft:
                reads.append(path)
            return real_read(path)

        with patch.object(build_module, 'ROOT', self.copy), \
                patch.object(build_module.os, 'walk', observed_walk), \
                patch.object(pathlib.Path, 'read_bytes', observed_read):
            after = build_module.source_files()
        self.assertEqual(after, before)
        self.assertFalse(any(p.is_relative_to(self.copy / '.local-history') for p in visited))
        self.assertEqual(reads, [])

    def test_unreviewed_source_is_rejected_before_content_read(self):
        """@GC-14 Files outside the source allowlist are rejected unread."""
        unexpected = self.copy / 'docs' / 'unreviewed-fixture.txt'
        unexpected.write_text('Synthetic fixture; not a real confidential file.\n')
        reads = []
        real_read = pathlib.Path.read_bytes

        def observed_read(path):
            if path == unexpected:
                reads.append(path)
            return real_read(path)

        with patch.object(build_module, 'ROOT', self.copy):
            with patch.object(pathlib.Path, 'read_bytes', observed_read):
                with self.assertRaises(Invalid):
                    build_module.source_files()
        self.assertEqual(reads, [], 'unreviewed content was read before rejection')

    def test_administrative_metadata_is_excluded_without_reading(self):
        """@GC-20 Checkout metadata neither blocks builds nor enters payloads."""
        with patch.object(build_module, 'ROOT', self.copy):
            before = build_module.source_files()
        administrative = set()
        for folder in ('.git', '.harness', 'graft'):
            path = self.copy / folder / 'SYNTHETIC'
            path.parent.mkdir()
            path.write_text('Synthetic administrative fixture only.\n')
            administrative.add(path)
        for name in ('.DS_Store', 'CCS-1.0.md', 'CREATE-COMPANION-PROMPT.md'):
            path = self.copy / name
            path.write_text('Synthetic local-only fixture.\n')
            administrative.add(path)
        reads = []
        real_bytes = pathlib.Path.read_bytes
        real_text = pathlib.Path.read_text

        def observed_bytes(path, *args, **kwargs):
            if path in administrative:
                reads.append(path)
            return real_bytes(path, *args, **kwargs)

        def observed_text(path, *args, **kwargs):
            if path in administrative:
                reads.append(path)
            return real_text(path, *args, **kwargs)

        with patch.object(build_module, 'ROOT', self.copy):
            with patch.object(pathlib.Path, 'read_bytes', observed_bytes), \
                    patch.object(pathlib.Path, 'read_text', observed_text):
                after = build_module.source_files()
        self.assertEqual(reads, [], 'administrative file contents were read')
        self.assertEqual(after, before)

    def test_broken_maintainer_link_prevents_build(self):
        """@GC-15 Maintainer references must resolve within the delivered kit."""
        readme = self.copy / 'README.md'
        readme.write_text(readme.read_text() +
                          '\n[Required missing guide](docs/does-not-exist.md)\n')
        with patch.object(build_module, 'ROOT', self.copy):
            with self.assertRaises(Invalid):
                build_module.build(pathlib.Path(self.temp.name) / 'output')


class SafeInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.target = pathlib.Path(self.temp.name) / 'course'
        self.target.mkdir()

    def test_cue_preview_does_not_write(self):
        plan = plan_install(self.target, 'copilot', 'git-companion')
        self.assertEqual(len(plan['create']), len(runtime_files('git-companion', 'copilot')))
        self.assertEqual(list(self.target.rglob('*')), [])

    def test_apply_copilot_preserves_preexisting_instructions(self):
        instruction = self.target / '.github/copilot-instructions.md'
        instruction.parent.mkdir()
        instruction.write_text('# Project rules\nFollow AIDE process.\n')
        write_plan(plan_install(self.target, 'copilot', 'git-companion'))
        text = instruction.read_text()
        self.assertTrue(text.startswith('# Project rules\nFollow AIDE process.\n'))
        self.assertIn('BEGIN CCS:git-companion', text)
        self.assertEqual((self.target / '.github/skills/git-companion/SKILL.md').read_bytes(),
                         (ROOT / 'companions/git-companion/SKILL.md').read_bytes())

    def test_idempotent_reapplication(self):
        write_plan(plan_install(self.target, 'codex', 'git-companion'))
        before = {p.relative_to(self.target).as_posix(): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}
        plan = plan_install(self.target, 'codex', 'git-companion')
        self.assertFalse(plan['create'])
        self.assertEqual(plan['before'], plan['after'])
        write_plan(plan)
        after = {p.relative_to(self.target).as_posix(): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_existing_different_skill_fails_without_mutation(self):
        path = self.target / '.claude/skills/git-companion/SKILL.md'
        path.parent.mkdir(parents=True)
        path.write_text('user modified skill')
        with self.assertRaises(Invalid):
            plan_install(self.target, 'claude', 'git-companion')
        self.assertEqual(path.read_text(), 'user modified skill')
        self.assertFalse((self.target / 'CLAUDE.md').exists())

    def test_malformed_existing_cue_fails(self):
        instr = self.target / 'AGENTS.md'
        instr.write_text('<!-- BEGIN CCS:git-companion -->\nunfinished')
        with self.assertRaises(Invalid):
            plan_install(self.target, 'codex', 'git-companion')
        self.assertEqual(instr.read_text(), '<!-- BEGIN CCS:git-companion -->\nunfinished')
        self.assertFalse((self.target / '.agents').exists())

    def test_instructions_symlink_refused(self):
        outside = pathlib.Path(self.temp.name) / 'outside.txt'
        outside.write_text('untouched')
        (self.target / 'CLAUDE.md').symlink_to(outside)
        with self.assertRaises(Invalid):
            plan_install(self.target, 'claude', 'git-companion')
        self.assertEqual(outside.read_text(), 'untouched')

    def test_known_managed_instruction_file_is_refused_before_writes(self):
        """@GC-16 An installer-owned instruction file is not a cue merge target."""
        instruction = self.target / 'CLAUDE.md'
        original = '# Generated by AIDE — DO NOT EDIT\nProject policy.\n'
        instruction.write_text(original)
        with self.assertRaises(Invalid):
            plan_install(self.target, 'claude', 'git-companion')
        self.assertEqual(instruction.read_text(), original)
        self.assertEqual(list(self.target.iterdir()), [instruction])

    def test_instruction_drift_invalidates_plan_before_any_skill_writes(self):
        """@GC-17 Apply preserves an instruction edit made after preview."""
        instruction = self.target / 'CLAUDE.md'
        instruction.write_text('# Original policy\n')
        plan = plan_install(self.target, 'claude', 'git-companion')
        newer = '# Another contributor changed this policy\n'
        instruction.write_text(newer)
        with self.assertRaises(Invalid):
            write_plan(plan)
        self.assertEqual(instruction.read_text(), newer)
        self.assertFalse((self.target / '.claude').exists())

    def test_instruction_symlink_substitution_invalidates_plan_before_writes(self):
        """@GC-18 Apply rejects a replaced instruction path before mutation."""
        instruction = self.target / 'CLAUDE.md'
        instruction.write_text('# Original policy\n')
        plan = plan_install(self.target, 'claude', 'git-companion')
        outside = pathlib.Path(self.temp.name) / 'outside.txt'
        outside.write_text('# Original policy\n')
        instruction.unlink()
        instruction.symlink_to(outside)
        with self.assertRaises(Invalid):
            write_plan(plan)
        self.assertTrue(instruction.is_symlink())
        self.assertEqual(outside.read_text(), '# Original policy\n')
        self.assertFalse((self.target / '.claude').exists())

    def test_target_root_symlink_substitution_is_refused_before_writes(self):
        """@GC-21 Apply rejects a target root replaced after preview."""
        plan = plan_install(self.target, 'claude', 'git-companion')
        original = pathlib.Path(self.temp.name) / 'original-course'
        self.target.rename(original)
        outside = pathlib.Path(self.temp.name) / 'different-course'
        outside.mkdir()
        self.target.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(Invalid):
            write_plan(plan)
        self.assertTrue(self.target.is_symlink())
        self.assertEqual(list(original.iterdir()), [])
        self.assertEqual(list(outside.iterdir()), [])

    def test_reversed_cue_markers_are_rejected(self):
        """@GC-19 A reversed managed block is rejected without target writes."""
        instruction = self.target / 'CLAUDE.md'
        original = '<!-- END CCS:git-companion -->\ntext\n<!-- BEGIN CCS:git-companion -->\n'
        instruction.write_text(original)
        with self.assertRaises(Invalid):
            plan_install(self.target, 'claude', 'git-companion')
        self.assertEqual(instruction.read_text(), original)
        self.assertFalse((self.target / '.claude').exists())

    def test_update_only_managed_cue_preserves_others(self):
        old = '# Other project guidance\n\n<!-- BEGIN CCS:git-companion -->\nold\n<!-- END CCS:git-companion -->\n\n# More guidance\n'
        updated = merge_cue(old, cue_block('git-companion', 'claude'), 'git-companion')
        self.assertTrue(updated.startswith('# Other project guidance\n\n'))
        self.assertTrue(updated.endswith('\n# More guidance\n'))
        self.assertNotIn('\nold\n', updated)

    def test_all_host_cues_use_correct_native_references(self):
        paths = {
            'copilot': 'skills/git-companion/SKILL.md',
            'claude': '.claude/skills/git-companion/SKILL.md',
            'codex': '.agents/skills/git-companion/SKILL.md',
        }
        for host, rel in paths.items():
            with self.subTest(host=host):
                write_plan(plan_install(self.target, host, 'git-companion'))
                text = (self.target / host_spec(host)['instruction_file']).read_text()
                self.assertIn(f']({rel})', text)

    def test_cli_preview_and_explicit_apply(self):
        def call(*args):
            return subprocess.run([sys.executable, str(ROOT / 'tools/install.py'),
                                   '--host', 'copilot', '--target', str(self.target), *args],
                                  capture_output=True, text=True, check=False)
        preview = call()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn('NOT INSTALLED', preview.stdout)
        self.assertEqual(list(self.target.iterdir()), [])
        applied = call('--apply')
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertTrue((self.target / '.github/copilot-instructions.md').exists())


if __name__ == '__main__':
    unittest.main()
