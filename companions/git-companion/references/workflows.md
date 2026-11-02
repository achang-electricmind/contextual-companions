# Git concepts in the context of work

Use only the explanation relevant to the conversation. This filename is retained for compatibility with existing links; this reference supplies educational context, not execution procedures. The agent and applicable project workflow own inspection, actions and approvals.

## Follow the conversation

Interpret short questions using prior turns. “Will they see it?” after a local commit concerns publication; after an email it concerns email delivery. “Is it approved?” can concern a PR, a stakeholder decision or a formal AIDE gate. If the existing context settles the meaning, do not ask again. If it does not, clarify the artifact or intended outcome without assuming Git.

The same principle works in a crash course, a general bootcamp, an AIDE workspace and an ordinary project. Use the actual artifact when known: a requirement, test checklist, source file, design note or README. Do not import course roles, six-repository layouts, enterprise policies, AIDE configuration or branch names into another project. A non-Git document or design tool has its own sharing/version model; the companion need not contribute.

## Explain the distinction that matters now

| Moment in the task | Useful explanation | Avoid implying |
| --- | --- | --- |
| “I saved it; can my teammate see it?” | Saving updates a file; a Git commit records selected changes; publishing sends commits to the relevant remote. Explain only the missing distinction. | That closing an editor guarantees a save, or a commit alone proves anyone received it. |
| “Why is this version different?” | A branch is a line of work; different branches or repositories can contain different versions. | That a branch is a duplicate folder, an approval stage, or that switching is the required next action. |
| “What are staged changes?” | Staging selects saved contents, including files or hunks, for an ordinary commit; the selection can differ from current editor contents. Some commands stage automatically, so a separate staging command is not always needed. | That every changed file belongs in the same commit, that without staging Git must commit everything or nothing, that staging bypasses the index or guarantees recovery, or that another task's selection can be replaced. |
| “The tutor has newer work.” | Fetching updates information about remote history; integrating changes affects the working version. Unsaved editor text is outside Git's index. Saved local edits may block or conflict with an update when incoming changes touch the same files or lines; the result depends on the operation, configuration and repository state. | That checking for updates discards local edits, that Git always protects local edits, that any edit to the same file forces a refusal, or that a particular merge/rebase strategy has been selected. |
| “No conflicts—are we approved?” | Git's ability to combine text, recorded PR reviews and substantive project approval are different facts. Overlapping edits may conflict; identical overlapping changes can combine cleanly. A clean textual merge can still produce unintended wording or meaning. | That a clean merge preserves intended meaning, resolves contradictory requirements or completes an AIDE review. |
| “Where did my work go?” | A changed view or branch does not itself prove deletion; saved, committed and unsaved work have different recovery possibilities. | That recovery is guaranteed, that data was lost, or that reset/restore is the answer. |
| “Why another confirmation?” | Explain the purpose of the current workflow gate if known; approval to commit and confirmation that a solution works can concern different decisions. | That understanding a concept grants permission, or that this companion requires another approval. |
| A check or publish step fails | Translate the actual outcome and its effect on the user's goal, including partial results. | That an attempted operation succeeded, that all repositories changed together, or that installation/access changes are authorized. |

These are examples of meaning, not activation phrases or a required response format. A question may need only one sentence. A conceptual question needs no closing commit/pull recipe, command catalog or suggested action prompt. For example, uncertainty about preserving a draft calls for explaining the difference between learning about remote changes and integrating them; it does not select “commit first, then pull.” If the user asks what to tell an agent, focus on outcome, scope and constraints already missing from the conversation, without restarting settled approvals. An explicit request for a deeper lesson can receive examples, diagrams or command explanations. Never execute an illustrative command merely because it appears in an explanation.

## Evidence and its limits

Use only the distinction needed to answer the actual claim. These are interpretation aids, not a prescribed inspection sequence or a requirement to run commands. When the person supplies the facts, answer from them; add verification commands only when asked.

| Available observation | What it supports; what remains unestablished |
| --- | --- |
| A file is still modified after a commit | Current saved contents differ from recorded or selected contents. If A was staged and the file was then saved as B without staging again, a successful ordinary commit records A; B remains a working-tree modification. Excluded edits also remain. A dirty working tree does not prove commit failure. |
| A commit hash exists | A particular commit exists; the intended contents, target repository and relationship to the requested task still matter. A timestamp or attribution trailer alone does not prove which actor performed it. |
| A real change summary such as `requirements.md \| 2 +-` | It identifies a file and change counts; it does not prove the exact committed wording. A requested change, such as a new deadline, remains unverified until the changed lines or committed file contents are available. |
| Local tracking information agrees, or shows no ahead/behind | It describes the local comparison with a locally recorded remote reference, which can be stale. It does not prove the server currently has the latest work. A successful push record for the destination or a current remote observation is different evidence. |
| No terminal appeared | No visible terminal was observed. An agent may have used another tool or interface; absence of that window proves neither success nor failure. Rely on whatever tool-call, repository, commit-content or remote evidence is available, and state what remains uncertain when it is missing. |
| The assistant says “done” or repeats its confidence | A claim was made. Actual tool results and relevant state can support it; narrative output is not independent confirmation. |

For example: stage a requirement with a five-day deadline, save a seven-day edit without staging again, then make an ordinary commit. That commit records five days while the working file still says seven days and remains modified. Both observations can be true. Likewise, a successful push can establish publication to a particular destination without proving a reviewer accessed it or approved its meaning. Staging writes selected content into Git objects. Previously staged content may sometimes be recoverable from those objects, even without a commit; this is not a dependable recovery strategy. A commit records a snapshot in history, but neither state alone guarantees recovery. Publication likewise does not guarantee receipt.

## Analogies with useful limits

A repository resembles a project folder with history, but a shared-drive analogy does not imply automatic synchronization. A branch resembles a parallel draft, but it can affect a whole collection of files and is not a separate copied folder. A commit resembles a checkpoint, but it records selected saved contents rather than every open editor buffer. A PR resembles a structured review request, but opening one is not approval or evidence that the application works.

## Courses and multiple repositories

When the task has established a workspace map, explain why related artifacts may live in separate repositories and why each can have a different state. A workspace window is a view over folders, not necessarily one Git repository. Matching branch names do not prove compatible contents. A missing folder may not have been provided or accessible; it does not prove the learner deleted it. A documentation reviewer may be able to contribute without access to application source.

Use these distinctions only when they help the person's question. Let the executing agent determine actual paths, access and required actions. Do not turn an explanation into a cloning, checkout or setup sequence. Running the application and collaborating on its documentation can have different prerequisites.

## Return to the task

After the executing agent establishes an outcome, explain its consequence if useful: “The checkpoint is local; it has not been published in this operation.” Attribute only what the evidence supports—there could already be other published versions. Do not append a tutorial when a concise result suffices. Offer optional depth naturally when the user remains confused; no quiz or routine follow-up is required.


## AI fluency and Git knowledge can differ

Adapt the explanation to the actual question, without labeling the person. Someone familiar with AI workflows may need a concrete Git explanation: “A commit records these selected changes locally; it does not publish them.” Someone experienced with Git but new to agents may instead need the evidence distinction: “That was a proposed command, not a completed tool action.” Someone new to both may benefit from a plain-language link between the artifact, the assistant's intended help and what has actually happened. Someone experienced with both may want only the requested result.

The educational contribution can support four practical habits: decide what to delegate, describe the intended outcome, examine evidence instead of trusting confident prose, and retain responsibility for the result. These are not extra workflow stages or approval gates. Do not turn a Git question into a lesson about models, tokens, prompt engineering, automation or tool connections unless the person asks or that detail resolves the immediate confusion. For curiosity about how a skill works, explain that it is context for the assistant, not executable enforcement or proof that it was loaded.


## Respect the person's control

Give more detail when it is requested, including internals, tradeoffs and command explanations relevant to the question. A request for a detailed explanation does not authorize running the example commands. A request to stop unsolicited teaching should be honored without another offer, lesson or reminder. Answer later direct questions normally; do not treat a one-off question as permission to resume ongoing unsolicited teaching. Actual host disabling is separate from a conversational preference; the [friendly README](../README.md) explains the options.
