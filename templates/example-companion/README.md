# Example Companion template

Replace the placeholders in this folder, rename the directory, and keep `SKILL.md` frontmatter `name` and `companion.json` `id` identical to the directory name. Define a reusable domain contribution that helps people participate across relevant activities, without calibration or a context adapter. Define the domain and cases first; don't leave this example unmodified in a learner workspace. Replace this maintainer README with a participant-facing overview before packaging; keep authoring templates and their external references in the maintainer kit.

`adapter/cue.md` is a short host-neutral cue template with a `{{skill_path}}` placeholder. Host-specific packaging resolves that path. `companion.json` is a maintainer contract; the agent uses `SKILL.md`.

To complete the evaluation contract, create `tests/cases/<new-id>.json` using `BEHAVIOR-CASES-template.json` as a starting point; author at least 12 real scenarios covering direct, implicit, contextual follow-up, negative, execution, expert, evidence, and security. Move the completed case pack out of the companion into that tests path and remove the authoring-only `BEHAVIOR-CASES-template.json` from the copied companion directory. Then set `evaluation.cases` to `tests/cases/<new-id>.json` (do not keep the example ID). The default build script validates the named companion with `--companion <new-id>`.

Keep activity-specific context outside the companion. The maintainer kit provides `docs/CONTEXT-ADAPTERS.md` and `templates/context-adapter.md`; do not link to these external resources from a packaged participant README. Add cases for no-adapter help, reuse across activities, missing/stale context, preferences, domain relevance and host-owned assistance boundaries. These are scenario specifications until actually evaluated.

Add each reviewed source resource to `distribution-files.json` before building; unexpected files are rejected. Preserve user depth/pause preferences and keep host-control documentation separate from default shared behavior.
