# Choose the amount of help

Use these options when asked about the companion, not as a recurring reminder. Its default is relevant, concise context; no expertise level or special phrase is required.

## In this conversation

Ask for a short answer, examples, advanced internals or no extra explanation. “Stop adding Git explanations in this chat” pauses unsolicited teaching while the task continues. A later direct question still gets answered and does not automatically resume ongoing teaching. Ask to resume when useful. This is a conversational preference, not unloading context or changing settings.

## Persistent choices

The host's controls affect skill invocation; a separate project instruction cue may still tell the agent to read the file. For a project-wide on-demand or off choice, remove only the Git Companion cue from the applicable instruction file, preserving other content. For personal settings, leave shared files alone and explicitly tell the agent not to follow the companion cue unless you ask. That preference is guidance, not a technical block on reading a file. Start a fresh conversation after changes; already-read context cannot be removed by claiming “disabled.”

These instructions are optional configuration choices, not permission for the companion to edit settings. Check the active host and organization policy. Shared skill-file changes affect others when distributed. Preserve such choices during updates; do not use the installer to restore automatic invocation over a customized skill.

### Copilot in VS Code

In the installed SKILL.md frontmatter, `disable-model-invocation: true` makes invocation manual-only; adding `user-invocable: false` disables both automatic loading and the slash command. Preserve other fields. For the associated project cue, see `.github/copilot-instructions.md`. [Official controls](https://code.visualstudio.com/docs/agent-customization/agent-skills#use-skills-as-slash-commands).

### Claude Code

For a personal/local choice in supported versions, the `/skills` menu can set the skill to user-only or off. The corresponding `skillOverrides` values for `git-companion` are `user-invocable-only` and `off`; the menu saves to local settings. The separate cue is in `CLAUDE.md`. Plugin controls differ; these bundles are ordinary project skills. [Official skill visibility controls](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings).

### Codex

For a personal off choice, add an entry to `~/.codex/config.toml`, using the actual installed SKILL.md path:

```toml
[[skills.config]]
path = "/actual/project/.agents/skills/git-companion/SKILL.md"
enabled = false
```

Restart Codex. For manual-only use, the installed skill can instead have `agents/openai.yaml` containing `policy: { allow_implicit_invocation: false }`, preserving any existing metadata. The separate project cue is in `AGENTS.md`. The canonical package does not add this host-specific policy. [Official Codex controls](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills).

## Updates and verification

Keep local customizations separately reviewable. The installer refuses different same-name skill files; it does not silently upgrade or re-enable them. A host's discovery/visibility evidence can show configuration was recognized. A plausible answer or “I disabled myself” is not proof. These controls are documented from official sources; this release did not run live-host checks.
