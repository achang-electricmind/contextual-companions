# Maintain the value of Git Companion

The companion succeeds when useful domain understanding helps someone participate effectively in their current activity: understand, contribute, decide or act. Task completion is one outcome; learning needs separate evidence. More instruction text, more activation or longer answers are not success measures. Treat the [main introduction](../README.md) as the team's introduction and the [runtime SKILL.md](../companions/git-companion/SKILL.md) as the behavioral source of truth.

## Improve from a concrete observation

1. Record the relevant question, preceding context, expected help and observed response. Remove private content. Record whether the skill/cue was actually read; an assistant's claim alone is insufficient.
2. Identify the smallest gap: relevance, factual accuracy, explanation depth, user preference, workflow interference or host discovery. A discovery problem need not be a trigger-text problem.
3. Change the smallest useful part. Core decision guidance belongs in SKILL.md; detailed explanations in references; discoverability in the description/cue. Avoid phrase lists as activation rules, repeated warnings, mandatory formats or another workflow.
4. Add or refine a representative case in `tests/cases/git-companion.json`, including an unrelated counterexample or user-control case where useful. Cases are specifications until actually run. Factual errors count even when they miss a rubric's exact wording; a zero-failure score from a narrow rubric is not a safety sign-off.
5. Run `sh scripts/verify --changed`. For packaging changes, check a freshly extracted kit and compare the nested host archives with their standalone counterparts. Do not call a model or change live repositories just to satisfy offline verification.
6. If behavioral or host checks are separately authorized, record the actual model/mode, context, raw response, discovery evidence and limitations. Distinguish observations from inferred benefits. Preserve original evidence; correct interpretations in a separate record.

## Keep one canonical teaching source

`companions/git-companion/` is shared by all three host bundles. Host adapters own placement, not different pedagogy. Keep the README welcome, depth/pause/off guidance and instruction cue aligned. Preserve local disabled/manual-only choices during an upgrade; a differing installed skill is a customization to review, not something to overwrite automatically.

`distribution-files.json` is the explicit source allowlist. Add reviewed resources deliberately; unlisted payload files are rejected before their content is read. Root `.git` and `.harness` administrative metadata, and local-only `.local-history/` notes, are excluded without traversal or content reads. `.local-history/` is also excluded by `.gitignore`; keep internal drafting records out of the published reading path. Generated output belongs in an empty external directory, `dist/`, or `releases/`; do not put build outputs beneath source-owned directories. Review all packaged links. No secrets, environment files, private records or unreviewed logs belong in the list.

The optional installer is a maintainer utility, not part of the assistant's runtime. It previews by default, preserves different skill files, rejects known managed instruction markers and stale plans, and merges only a bounded cue. Marker recognition is not a universal detector of ownership. Inspect the project's rules even when no marker is present. Do not edit an installer-owned instruction file; use a permitted customization location manually. The installer does not provide a filesystem transaction or lock against simultaneous changes; avoid concurrent writers and inspect the resulting diff.

## Preserve reuse when adding context

Keep domain teaching in the canonical skill. Use existing activity context first; place optional context adapters in the activity workspace, outside the companion. A new workshop should not need a new companion version unless it reveals a general gap in domain guidance. Host adapters own packaging/discovery; context adapters supply situational facts and existing assistance boundaries. See the [context adapter guide](CONTEXT-ADAPTERS.md).

Review both no-adapter help and the same companion in different activities. Check stale context, preferences, domain overlap and explicit host-owned practice boundaries. Do not treat an audience label as ability or make a brief mandatory. Scenario specifications and static review do not establish model compliance.

## Build and distribute

```sh
sh scripts/verify --changed
python3 tools/build.py --output dist/release
```

The output directory must be absent or empty. The build produces three host ZIPs and one complete kit; host ZIPs contain no root instruction files and cannot overwrite project guidance during extraction. The complete kit includes the exact host ZIP bytes. Keep versioned releases and their source hashes; update companion metadata, release links and test version expectations together. Refer to [next steps](NEXT-STEPS.md) for inclusion and the [validation record](VALIDATION.md) for the evidence accompanying the package.

The proposed CCS profile and template are optional authoring resources for maintainers. Participants do not need to understand them, and they do not enforce model behavior.
