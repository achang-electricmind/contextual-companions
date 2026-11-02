# Host packages and controls

One canonical companion supplies all hosts and relevant activities. Native paths differ; domain teaching does not. No per-workshop calibration or explicit context adapter is required.

This page describes **host adapters**. Optional **context adapters** supply activity facts and existing assistance boundaries through the host's normal mechanisms; they do not alter native skill paths or fork teaching. See the [context adapter guide](../docs/CONTEXT-ADAPTERS.md). The installer does not discover or install activity context.

| Host | Skill directory | Optional instruction cue location | Host ZIP |
| --- | --- | --- | --- |
| Copilot in VS Code | `.github/skills/git-companion/` | `.github/copilot-instructions.md` | `git-companion-copilot-0.8.2.zip` |
| Claude Code | `.claude/skills/git-companion/` | `CLAUDE.md` | `git-companion-claude-0.8.2.zip` |
| Codex | `.agents/skills/git-companion/` | `AGENTS.md` | `git-companion-codex-0.8.2.zip` |

The host ZIP contains only the skill tree. The complete kit includes the cue template, adapters and optional installer. Manual inclusion and deliberate cue merging are supported; no AIDE installer or registration is needed. Use one intended installation in an open workspace. Several hosts scan multiple skill locations, so three copies may cause duplicate or ambiguous selection.

For Copilot, a cue in `.github/copilot-instructions.md` links to `skills/git-companion/SKILL.md` relative to that file; the other listed root cues link to their native paths. Read [next steps](../docs/NEXT-STEPS.md) for inclusion and [user controls](../companions/git-companion/references/user-controls.md) for the distinction between chat preferences, host controls and the independent cue. The cue must honor off/manual-only preferences; it is not a route around them.

The optional installer previews by default and writes only with `--apply`. It checks known managed markers, symlinks, differing skill files, malformed cue blocks and changes since planning. It cannot recognize every project's ownership convention or lock against concurrent edits. Inspect repository rules and preserve installer-owned files through the project's supported customization route. Do not use it to silently replace a prior or customized skill.

Host capability, account policy, selected roots and harness versions can affect discovery. Use actual host evidence to establish availability and invocation; model prose does not prove either. Restart or use a fresh conversation after control changes as directed by that host. No user settings, active installations or organization policies are changed by building this kit.

Optional plugins are separate distribution formats and are not needed here. They do not inherently guarantee invocation. Recheck vendor formats and permissions before introducing one.

References: [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills).
