# Contextual Companions

**Reusable companions supply the surrounding knowledge people need to participate effectively in whatever they’re doing.**

A companion contributes focused domain understanding inside the assistant conversation someone already uses. It can help a person understand an artifact, contribute to a discussion, make a decision or carry out a task. The same companion can support everyday work, team collaboration, onboarding, independent learning, workshops and courses wherever its domain is relevant.

No workshop-specific version, learner calibration or session brief is required. The companion uses available conversation and workspace context, adjusts to demonstrated understanding and preferences, and stays quiet when its domain adds nothing useful. It does not infer ability from a job title or audience label.

## Reusable knowledge, optional context

| Layer | Responsibility | Example |
| --- | --- | --- |
| Companion | Stable domain knowledge, relevance signals, explanation guidance and boundaries | Explain the difference between a local commit and sharing work |
| Optional context adapter | Activity purpose, artifacts, references, local terminology and assistance boundaries | A requirements workshop or a team's collaboration conventions |
| Host adapter | Native skill placement and a short discovery cue | Packaging for Copilot, Claude Code or Codex |

A context adapter helps a team or facilitator supply relevant context consistently. It is ordinary guidance the host can read, not a new runtime or a required configuration step. Existing conversation or project context may already be enough. It does not duplicate the companion's teaching, assign proficiency, grant permissions or override user preferences. See the [context adapter guide](docs/CONTEXT-ADAPTERS.md) and [optional template](templates/context-adapter.md).

For training, a facilitator can prepare the working context and include companions for likely prerequisite gaps so participants can focus on the session's main learning goal. Explicit boundaries about what participants must practice belong to the host's session instructions. Companions explain surrounding concepts without taking over the exercise or adding checkpoints. The same companions remain useful after the course.

## Git Companion: the first implementation

Git Companion helps people understand Git while writing requirements, editing documentation, developing software or collaborating. Someone asking “I saved my changes—can my teammate see them?” should get an explanation connected to their work, without needing Git terminology first.

It explains saving, staging, commits, branches, sharing, reviews and recovery when those distinctions matter. Git knowledge and AI-tool fluency are independent. Explanations are brief by default; anyone can ask for examples, advanced detail or a pause. The [friendly introduction](companions/git-companion/README.md) describes the controls and why examining an assistant's context is useful.

The host assistant and applicable project or AIDE workflows retain operations and approvals. There is no companion-owned command loop, mandatory quiz, profile or additional approval process. Git Companion requires neither AIDE nor a particular course. It can be included in our crash courses and Electric Wealth AIDE workspaces, as well as ordinary projects.

## Use or author a companion

Choose one package for the assistant used in the workspace:

- [Copilot package](releases/git-companion-copilot-0.8.2.zip)
- [Claude Code package](releases/git-companion-claude-0.8.2.zip)
- [Codex package](releases/git-companion-codex-0.8.2.zip)

Each host ZIP contains only the reusable skill tree. The complete maintainer kit includes the standard, authoring templates, optional context adapter resources, installer, references and checks. The context adapter template is not automatically installed into participant workspaces. Package details and checksums are listed in the [proposal contents](RELEASE-NOTES.md).

Follow [workspace inclusion](docs/NEXT-STEPS.md) and preserve existing instructions. For another domain, use the [CCS standard](standard/CCS-1.0.md), [authoring directive](standard/CREATE-COMPANION-PROMPT.md) and [companion template](templates/example-companion/README.md). Improve guidance from concrete observations using the [maintenance guide](docs/MAINTAINER.md).

## Proposal status

This is an initial proposal with a packaged Git Companion implementation. Offline artifact checks pass; live-host behavior and participation or learning outcomes remain unverified. The [validation record](docs/VALIDATION.md) states the evidence and its limits. Installation alone does not prove that a host invoked the companion.
