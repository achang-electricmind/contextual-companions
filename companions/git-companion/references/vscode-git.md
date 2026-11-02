# Git in VS Code Source Control (learner-facing orientation)

Use when a learner asks about a VS Code button, icon, panel, change list or a Copilot action in the provided course environment. Exact controls may vary with VS Code version, extensions, workspace, authentication and repository state. Avoid inventing a visible UI; ask for the relevant label or describe general navigation when the environment is not observed.

| VS Code idea | Underlying Git idea | Important distinction |
| --- | --- | --- |
| **Source Control** view | Work in the active repository | In a multi-root workspace, different folders may be separate repositories with independent branches/remotes. |
| **Changes** list | Files changed relative to Git's local state | A changed file may contain uncommitted changes, not necessarily unsaved editor text. |
| **Staged Changes** | Content selected for the next commit | It can differ from the file's newest saved contents after later edits. |
| **Commit** action | Make a local history checkpoint of staged content | Does not publish to GitHub/Azure DevOps by itself. The host may configure auto-stage prompts or workflows. |
| **Push** or **Publish Branch** | Send commits or make a branch available on a remote | Requires correct destination/access; a reported success doesn't mean a reviewer has read the change. |
| **Pull**, **Fetch**, **Sync Changes** | Retrieve remote metadata, integrate changes, or both directions | Fetch generally obtains history without merging into the working branch; pull and Sync can integrate changes. Controls/settings vary. |
| Branch indicator | Current checkout/branch context | A branch name alone does not establish the repository, remote, publication status or correctness. |
| Compare/diff editor | The comparison the tool chose to display | Confirm *what was compared* (working file, staged content, commit, branch); green/red alone does not establish business approval. |

When Copilot reports “I committed it,” distinguish its proposal, tool execution and observable result if that matters to the question. No visible terminal is not evidence of no tool use. Do not invent a button click or a specific repository state if the assistant cannot actually observe it.

For a learner who asks how to use the UI, offer the shortest feasible navigation or explanation, appropriate to the requested outcome. The executing agent and course workflow still determine actual Git operations, prerequisites and confirmation, so this reference is not an alternative operational recipe.

Safety note: discarding changes, deleting branches, force pushes, hard resets, and cleanup commands can lose work. Explain the consequence when relevant but don't turn educational curiosity into a destructive operation.
