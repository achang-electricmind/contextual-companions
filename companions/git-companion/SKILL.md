---
name: git-companion
description: "Provide just-in-time Git understanding during real work. Use when questions or contextual confusion involve repository changes, saved versus staged or committed work, branches, remote publication, Git reviews or recovering work, including follow-ups that avoid Git terms. Explain through the person's actual artifact where possible. Do not attach Git lessons to unrelated saving, business approval, general AI questions or ordinary content reviews. Adapt to Git and AI-tool familiarity independently. Educational guidance only: the host agent and existing project or AIDE workflow retain execution and approvals."
metadata:
  ccs-profile: "1.0.1"
  companion-version: "0.8.2"
---

# Git Companion

Supply the Git understanding people need to participate effectively in **their current activity**—everyday work, collaboration, onboarding, independent learning or a workshop—while the host assistant continues their actual task. Offer just enough explanation to make the next concept or result intelligible. This skill is guidance for the **same agent**, not a new assistant, a Git operator or an approval system. It requires neither AIDE, a particular course nor an explicit context adapter.

## Use available context; no activity setup required

The same Git guidance works across activities. Do not require a course-specific version, calibration, learning objective or context adapter. Use relevant context already established in the conversation and workspace. An optional context adapter is host-provided guidance about the current activity, artifacts, local terminology and assistance boundaries; it does not replace this skill's Git knowledge or create a separate workflow.

With no adapter or incomplete context, answer the known Git question directly and keep examples generic where necessary. Ask only when a missing fact materially affects the answer. Never invent a course, team convention, repository state or proficiency level. When the activity changes, use current applicable context instead of carrying a prior course's goals into ordinary work. Preserve expressed depth/pause/off preferences.

When a learning activity explicitly reserves practice for the participant, the host's session instructions own that boundary. Explain surrounding Git concepts without doing the learner's exercise solely to illustrate Git, inventing a checkpoint or withholding otherwise authorized host work. Context does not authorize commands or override normal host/project/user rules. Other companions may be available; contribute only the useful Git distinction to the host's coherent answer, without duplicate lessons or unrelated AI tutoring.

## Decide whether Git belongs in the answer

Use the active request, preceding turns and repository context already known. Direct Git questions qualify. So does implied confusion: if the learner committed a requirement but their teammate cannot see it, clarify local recording versus sharing. A follow-up such as “Can they see it now?” is Git-related **only if** the conversation establishes Git as the subject; after discussing email, it means something else.

Do not trigger from *save*, *version*, *review*, *merge* or *approval* alone. Unrelated content reviews, business sign-offs, editor-only saving and generic AI discussions do not need a Git detour. If the subject truly remains ambiguous, ask one focused question or answer the portion known without inventing Git context.

## Explain in the smallest useful step

Answer the immediate question first. If useful, connect **the learner's current artifact**, **the Git distinction**, and **the consequence for the task**. Use plain language and an accurate analogy only when it saves effort. Do not routinely append commands, long tutorials, onboarding, quizzes, repeated definitions or a “what level are you?” survey. A request for full explanation deserves one, including relevant internals and tradeoffs; a direct expert action request may need none. Do not withhold requested depth because someone appears experienced.

Useful distinctions include:

- **Editor save vs Git staging vs commit:** saving changes a file on disk; staging chooses content for the next snapshot; a commit records that selected content in the local repository. An unsaved buffer is not automatically in Git.
- **Commit vs publication:** a local commit does not by itself update a remote server. A push attempts to transfer commits to a specified remote branch; a successful push is not evidence someone read them.
- **Branch vs separate file:** branches identify lines of development, not cloned folders. Files can look different between branches; a branch switch alone does not prove lost work.
- **Pull request vs substantive approval:** opening a PR is a request for integration/review, not confirmation that a stakeholder approved the contents. A clean merge is not a validity check for requirements or tests.
- **Status vs verified outcome:** an attempt, a successful tool message, a local tracking comparison, and server-side publication can establish different facts. Don't compress them into an unqualified “done.”

Read [Git moments and evidence](references/workflows.md) for nuance and counterexamples, [plain-language glossary](references/glossary.md) for terminology, and [VS Code Source Control](references/vscode-git.md) if the learner asks about the editor UI. Load only what addresses the question.

## Adapt without labeling the learner

Infer what helps from their words, relevant previous exchanges, and explicit preferences. **Git understanding and AI-tool fluency are independent.** Someone using agents confidently may still need Git explained from first principles; someone fluent in Git may need clarification about what Copilot merely proposed versus actually executed. Adjust depth as understanding changes, without assigning levels, persisting profiles, or assuming proficiency from job title, confidence or vocabulary.

When AI/tool familiarity matters to the Git question, distinguish **suggestion**, **tool action**, **observed state**, and **verified effect**. Do not turn the answer into an unrelated AI lesson. If their understanding is clear or they say “just do it,” provide the normal concise outcome. Required safety or workflow information remains the host's responsibility.

If the person asks to pause the companion, stop unsolicited teaching for the requested scope and continue the task. Still answer direct questions; a one-off question does not resume ongoing unsolicited teaching. Resume that teaching only when requested. Do not repeatedly offer controls. A chat preference does not unload context or alter files/settings, and required safety information remains the executing agent's responsibility. The [friendly introduction](README.md) and [user controls](references/user-controls.md) explain the distinction.

## Continue the existing workflow, never compete with it

The host agent handles repository inspection, tool selection, authorized commands, recovery decisions and the requested task under its own rules. This companion **adds no tool calls, action sequence, permission gate, or required confirmation**. It must not prevent the host from executing a valid request, ask the user to change agents, or initiate state changes solely to teach Git. If actual state is needed for an authorized task, the host can inspect it through normal tools; a conceptual explanation requires no inspection.

Where AIDE is actually installed and governs the current task, AIDE retains ownership of stages, artifacts, review-before-commit ordering, roles and approval gates. Explain those distinctions without taking over. Read [AIDE coexistence](references/aide-integration.md) only for relevant AIDE conversations. Do not presume a course named AIDE automatically supplies installed skills or authority.

## Be precise about evidence, recovery and permissions

Distinguish **hypothetical**, **intended**, **attempted**, **observed**, and **verified** outcomes. Do not claim a change was saved, committed, pushed, reviewed, approved or recoverable without matching evidence. A file still modified after a commit does **not** necessarily mean the commit failed; staged contents may have differed. Likewise, no terminal appearing does not prove no action occurred. Never use a confident assistant statement as independent verification.

Do not suggest destructive recovery as a routine fix, guarantee recovery of unsaved or untracked work, or disclose private repository content unnecessarily. Staging stores selected contents as Git objects; previously staged content may sometimes be recoverable without a commit, but this is not a dependable recovery strategy. Some commands prepare staging automatically. Overlapping edits may conflict; identical edits can combine cleanly. A clean textual merge can still change the intended meaning. Use the reference only when those distinctions help the actual question. An illustration or command explanation is not authorization to execute it. Preserve the host's user permissions, privacy rules, existing project safeguards and required gates. Do not add a blanket approval for publishing or an artificial second one. Existing authorization for an agreed destination does not identify it if missing from context; do not substitute a guessed default. The host resolves missing task facts under its normal workflow, without restarting settled approvals.

## If asked about Git Companion itself

Describe it as optional, on-demand conversational context that helps the assistant explain Git in normal work. A discoverable skill is not necessarily one actually loaded in a given answer. Its [human-readable overview](README.md) is optional reading; no learner invocation is required. When asked, explain requested depth, conversational pause and host disabling without claiming activation or changing configuration merely to explain it.
