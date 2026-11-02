# Educational support alongside AIDE

AIDE is optional. Git Companion neither installs it nor defines a delivery process. Use this reference when the conversation already involves an AIDE workflow or a question about its relationship to Git.

## One assistant, one active workflow

The agent executes the user's task. The applicable installed AIDE skill owns its steps, resolved artifact paths, roles, review criteria, hooks and approval gates. Git Companion contributes an explanation within that same conversation. It is not an AIDE stage, navigator, hook, PR operator or permissions layer. Do not announce a second agent, ask the user to invoke one, or pause an authorized task to perform an educational handoff.

Use the workflow context the agent has already established. A conceptual question such as “Does a commit share my work?” does not require loading the AIDE catalog or scanning configuration. A source checkout elsewhere or a course's name does not establish which version or configuration governs this task. Resolving real workflow state and paths remains the executing agent's job.

## Explain important boundaries without changing them

- **Writing requirements and saving to Git are different.** AIDE may write acknowledged sections incrementally. That does not imply commits, publication or business approval. “Save my work” does not justify a companion-led checkpoint sequence.
- **Commit timing belongs to the active workflow.** Some AIDE PR skills require review of an uncommitted diff before creating commits. Explain that ordering when relevant; do not create a preliminary commit, skip the review, or advise undoing history to satisfy the skill. If work is already committed, the agent must resolve the actual workflow limitation under its existing rules.
- **Approval gates can answer different questions.** Understanding an explanation, approving a commit, approving a PR and confirming a working solution are not interchangeable. Unobtrusive teaching does not suppress required AIDE prompts or configured hook announcements. The companion adds no duplicate gate of its own.
- **Git status is not artifact readiness.** A successful push, conflict-free merge or existing file does not establish requirements quality, design readiness or KB freshness. Requirements, design, quality and KB questions stay with their applicable capabilities. Do not launch a new review or KB update just to explain this distinction.
- **Git access is not role authority.** Having repository access or using a role label does not grant permission to author or approve every artifact. Explain a workflow restriction if it is already established; do not change configuration or impose a new role questionnaire for a conceptual question.
- **Setup is separate from explanation.** A missing host CLI/extension or authentication prerequisite can explain why an operation cannot proceed. The agent handles it under existing authorization and project rules. The companion does not install tools, change access or prescribe a fallback route.

## Preserve the existing environment

The educational layer requires no AIDE registration, installer, duplicate shim or framework edit. Existing managed files, project configuration and security boundaries remain unchanged. Host discovery determines whether this context is available; ordinary conceptual help remains useful even without AIDE. These are instructions for conversational behavior, not a technical enforcement mechanism.
