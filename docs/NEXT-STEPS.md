# Include Git Companion in an existing workspace

Choose the host the activity actually uses—an ordinary project, team collaboration, onboarding, independent learning or a course. The skill is ordinary repository content; no AIDE installation or participant setup exercise is required.

1. Inspect the target repository's existing instructions, managed-file markers and same-name skills. Choose one host bundle; do not install all three into one workspace without checking duplicate discovery.
2. Extract that host ZIP so its native skill directory sits at the intended project root. The ZIP includes skill files only; it does not replace AGENTS.md, CLAUDE.md or Copilot instructions. An unopened ZIP is not active context.
3. Merge the short cue from `companions/git-companion/adapter/cue.md` into a project-approved instruction location, resolving `{{skill_path}}` for that host. The [host guide](../standard/PORTABILITY.md) lists paths. Preserve unrelated instructions and existing manual-only/off choices. For installer-owned files, use their supported customization route rather than inserting a cue into managed content.
4. Alternatively, a maintainer may preview the optional installer from this complete kit: `python3 tools/install.py --host copilot --target /path/to/repository`. Only `--apply` writes. It refuses differing skill files and recognized managed instruction files; it does not silently migrate an older installation or decide an unmarked file's ownership.
5. Review the resulting diff under the project's normal process, then distribute the prepared workspace. Open the intended root in the chosen host and use a fresh chat. Access, extensions and organization policy remain prerequisites controlled by the host.

No course calibration or context adapter is required. Use the conversation and existing project context first. If shared activity context would help, follow the [context adapter guide](CONTEXT-ADAPTERS.md) to supply it separately through the host. Keep it outside the reusable skill; the installer does not copy or activate it. A facilitator may name the session's main learning goal and explicit practice boundaries in that surrounding context without changing the companion.

Availability is separate from use. Inspect the host's customization/discovery evidence and actual references or traces for a relevant conversation. Neither finding the folder nor a reassuring assistant answer proves activation. No live-host checks were run for this release; do them in the actual environment when authorized.

The [friendly README](../companions/git-companion/README.md) covers depth, pause and the optional host-specific controls. Persistent choices should not reset during maintenance. For a concrete problem, use the [maintenance guide](MAINTAINER.md), not an onboarding questionnaire or repeated feedback prompts.
