# Contextual Companion Specification (CCS) 1.0.1

Status: **proposed project standard**, 2026-11-01. This is an authoring and distribution profile **on top of** the public [Agent Skills specification](https://agentskills.io/specification). It is not an alternative to Agent Skills or an official vendor standard.

## 1. Purpose and applicability

**Reusable companions supply the surrounding knowledge people need to participate effectively in whatever they’re doing.**

CCS defines a **contextual educational companion** as reusable, narrowly scoped domain guidance that contributes relevant understanding within a person's existing conversation with an assistant. Its purpose and core knowledge remain stable across activities; available context shapes examples and depth. The first reference implementation is **Git Companion**.

A companion can support everyday work, team collaboration, onboarding, independent learning, a workshop or a course wherever its domain is relevant. It MUST NOT require a workshop-specific version, learner calibration, session brief or context adapter before providing useful domain help. It **does not** own the user's task, execute commands in a separate loop, authorize operations, or introduce a second workflow. The *host agent* may perform authorized work under its own instructions. A companion contributes understanding, not new permissions or required actions.

Effective participation may mean understanding an artifact, contributing to a discussion, making an informed decision or completing a task. Training is one application. In a learning activity, task completion alone does not establish learning; explicit practice boundaries remain part of the host's surrounding instructions. Broad reuse does not imply relevance to every request or support in every host.

CCS is best suited to explaining things at the point of need: Git, testing, deployments, API design, observability, AI usage, or another domain with recurring novice/expert differences. A task-executing or autonomous agent is a different type of capability and SHOULD NOT claim CCS conformance.

**Normative language:** MUST, MUST NOT, SHOULD, SHOULD NOT, MAY indicate requirements, recommendations, and options for this proposed standard.

## 2. Canonical authoring structure

```text
companions/<id>/
  SKILL.md                 # MUST: standards-compliant Agent Skill
  companion.json           # MUST: CCS metadata, not agent instructions
  README.md                # SHOULD: human-friendly purpose and boundaries
  references/              # SHOULD: detailed, on-demand knowledge
    ...
adapters/
  copilot.json             # Host-specific path and instruction-file mapping
  claude.json
  codex.json
companions/<id>/adapter/
  cue.md                   # Short host-neutral cue with {{skill_path}} placeholder
tests/cases/
  <id>.json                # MUST: activation and interaction test cases
```

`<id>` MUST match `SKILL.md` frontmatter `name` and the destination skill-directory name. **SKILL.md is the canonical agent-facing source.** `companion.json` is a packaging/testing contract, NOT an alternative instruction channel. Adapters MUST NOT fork or overwrite canonical pedagogy.

A distribution may copy only the `SKILL.md`, README and `references/` to a host-native directory, with the companion manifest included for traceability. Installation MUST NOT assume the host reads the manifest or README.

### Agent Skills requirements

The canonical `SKILL.md` MUST conform to the [open Agent Skills specification](https://agentskills.io/specification): YAML frontmatter with `name` (1–64 lowercase alphanumeric/hyphens, no consecutive hyphens, matches directory) and `description` (nonempty, <=1024 characters), followed by Markdown instructions. Optional standard fields MAY be used; `metadata` values MUST be strings. `description` MUST communicate **positive** and **negative** activation conditions; avoid only mentioning technology names.

The main skill SHOULD be short enough to load without overwhelming the user's task. Longer explanations belong in one-hop `references/` files. It SHOULD NOT depend on proprietary tool names or hardcoded paths to access the skill's core behaviour.

### Companion manifest

`companion.json` MUST validate against [`companion.schema.json`](companion.schema.json). Its identity, version, activation domain, behavioural adaptations, execution boundaries and evaluation file are maintainer-facing facts. `ccs_version` tracks the profile version separately from the companion's `version`. All user-visible teaching remains authored in `SKILL.md`.

## 3. Behaviour contract

**C1: Single conversation.** The companion MUST help the existing assistant within the current conversation, not demand that learners select another agent or invoke a skill explicitly. It MAY be invoked explicitly for diagnostics.

**C2: Domain boundary.** The companion MUST be narrowly scoped and MUST NOT hijack unrelated tasks. It SHOULD use prior turns to interpret ambiguous follow-ups. Generic words such as *save*, *review*, or *approve* are not automatically Git signals.

**C3: Point-of-need instruction.** The assistant SHOULD answer the user's immediate question first and connect the explanation to the current artifact or activity if already known. Depth SHOULD be proportional to uncertainty and the user's request; no mandatory mini-lessons, quizzes, onboarding screens, telemetry, or repeated prompts.

**C4: Adaptive, not classificatory.** The assistant MUST respond to demonstrated comprehension and expressed preferences, not inferred role, job title, confidence, or demographic traits. It MUST NOT assign proficiency scores or persistent labels. Dimensions MAY be independent (e.g. Git knowledge and AI/tool fluency); evidence from one must not automatically determine another.

**C5: No second workflow.** The companion MUST NOT impose an operational action sequence, tool invocation, authorization gate, or special confirmation of its own. The host agent retains execution; installed AIDE or comparable workflows retain their stage ownership, approvals and artifacts. The companion MUST NOT accidentally prevent authorized tasks from proceeding.

**C6: Evidence discipline.** It MUST distinguish hypothetical, proposed, attempted and verified outcomes. It MUST NOT claim a file is saved, a commit exists, a push succeeded, or review passed without adequate observed evidence. Unknown state remains unknown until the host performs applicable work.

**C7: Safety and privacy.** The companion MUST NOT teach by running potentially destructive operations or inspecting additional sensitive data just for an analogy. It MUST preserve existing security, privacy, tool, project, and user constraints. Educational wording is neither authorization nor policy enforcement.

**C8: Quiet competence.** Experienced participants may receive no extra explanation. The companion MUST respect requests to be concise, skip education, or go deeper. A pause applies for the requested scope; direct questions still receive answers without automatically resuming unsolicited teaching. Required warnings associated with the underlying task remain the host's responsibility.

**C9: Activation humility.** Being installed, discoverable, or named by the agent does not prove the host loaded its complete instructions. Neither CCS nor Agent Skills guarantees invocation from ordinary conversational relevance.

**C10: Independent value and contextual adaptation.** A companion MUST use relevant context already available and remain useful without an explicit context adapter. Missing optional context MUST NOT become an onboarding or setup gate. Ask a focused question only when missing information materially affects the answer; otherwise explain within known facts. Context MUST NOT broaden the domain, assign proficiency from an audience label, reset user preferences or introduce companion-owned operations.

## 4. Activation design

An author MUST document at least five paths:

1. **Explicit direct:** “What does staging mean?”
2. **Implicit need:** “I saved my file but my teammate cannot see it.” (only if repository context establishes Git relevance)
3. **Contextual follow-up:** “So can they see it now?” after an established push/commit topic
4. **Negative control:** “Review this business proposal” outside Git
5. **Task-execution coexistence:** “Commit the changes” when host has authorization, without the skill creating an artificial gate

The manifest's activation examples are testing aids, not trigger regexes. A keyword match MUST NOT override conversational context. Avoid invisible background monitoring or hidden user profiling.

## 5. Instruction architecture and authority

```text
User request / conversation + available activity context
             |
      Host agent (existing tools, task permissions, project rules)
             |
       Native skill discovery (on demand, not guaranteed)
             |
      CCS companion: educational context only
             |
       Existing workflow continues (AIDE if installed/active)
```

The **skill** owns reusable domain explanations and relevance guidance. An optional **context adapter** supplies situational facts, references, goals and assistance boundaries to the host. A **host adapter** owns skill path and short persistent routing cue. A **plugin** MAY later own install/distribution metadata but MUST NOT silently introduce tools, actions, hooks, MCP connections or extra approvals. **External task workflow** owns execution, inspections, branch/review policy and durable decisions.

Host instruction conflicts MUST be resolved by the host's normal precedence; a CCS adapter is additive and MUST NOT claim higher authority than users or managed project policies.

### Optional context adapter contract

A context adapter is ordinary host-readable guidance for an activity, team, project or learning session. It MAY supply the current purpose, relevant artifacts, local terminology/conventions, applicable companion domains and explicit assistance boundaries. It SHOULD reference maintained source material rather than duplicate it. There is no required filename, parser, manifest field or separate agent; putting a file in a workspace does not itself load it.

The context adapter MUST remain separate from canonical companion teaching and host packaging. It MUST NOT fork the companion for each audience, require personal profiles, imply domain relevance from installation alone, grant permissions, invent approvals, bypass a pause/off preference or own a second workflow. A goal describes the activity; it does not authorize actions. Referenced documents provide context under the host's normal trust and instruction rules, not unrestricted authority.

The host can consume context from the existing conversation, project instructions or a deliberately linked document through its supported mechanisms. An explicit adapter is OPTIONAL when sufficient context already exists. Without one, the companion follows the normal conversation and known facts. When activities change, use current applicable context; do not carry a previous course's goals or constraints into unrelated work. Resolve uncertain or conflicting applicability under normal host rules rather than guessing.

For a workshop, explicit learner-practice boundaries belong to the host's session instructions. Companions support those boundaries through their explanations; they MUST NOT invent teaching checkpoints or suppress an otherwise authorized action on their own. For multiple companions, each MUST stay within its domain; the host integrates relevant contributions into one proportionate answer, without repeated lessons or a requirement to activate the entire bundle.

See the [context adapter guide](../docs/CONTEXT-ADAPTERS.md) and [optional template](../templates/context-adapter.md). These are maintainer resources, excluded from native companion packages. The existing `adapters/*.json` files and `adapter/cue.md` implement **host** integration, not activity calibration.

## 6. Host adapter contract

Every host adapter MUST declare (a) a native skill destination, (b) the host instruction file or equivalent cue, (c) whether the cue is automatic in that host, (d) a non-destructive installation plan, (e) how to verify discovery and invocation, and (f) host/version caveats. Host adapters MUST be minimal, contain no duplicated glossary/procedures, and not rewrite existing project instructions without deliberate merge.

For this version, host adapters are:

| Host | Skill location | Lightweight always-on cue |
| --- | --- | --- |
| GitHub Copilot in VS Code | `.github/skills/<id>/` | append a section to `.github/copilot-instructions.md` |
| Claude Code | `.claude/skills/<id>/` | append a section to `CLAUDE.md` |
| Codex | `.agents/skills/<id>/` | append a section to `AGENTS.md` |

Supported paths, enterprise configuration, and recognition vary with host and version. A published skill is not proof of runtime activation. Avoid installing **three copies with the same name** in a single VS Code workspace, because several harnesses scan more than one skill location. Prefer **one target-host bundle per workspace**; if sharing a repository across hosts, test discovery and deduplication deliberately.

**Plugin packaging is OPTIONAL** and host-specific. A plugin is not the companion itself and does not automatically make its skill persistently loaded. Add one only after checking current plugin manifests, installation scope, distribution policies and live activation; do not bundle privileged MCP or hooks for an education-only companion.

## 7. Conformance, tests and release

A release MUST pass all automated artifact checks: metadata/schema validation, native paths, relative links, duplicate/unexpected files, archive reproducibility, no symlinks/path traversal, and non-destructive cue merging. A release MUST supply behaviour scenarios for direct/implicit/contextual/negative/task-execution cases and for a learner's changing demonstrated understanding.

Real-model evaluations SHOULD compare a *baseline host* without companion versus *same host with companion*, holding prompts, tool permissions, model, task state and prior turns constant. Score relevance, factual truth, helpfulness, unwanted teaching, authorized task continuity and workflow compliance. Run live harness-discovery checks separately: **tests of instructions are not tests of invocation**. Tests and simulations MUST be labeled by evidence type; manual response reviews are not deterministically proven behaviour.

Behaviour specifications MUST also cover useful help without an adapter, the same companion in different activities, partial or stale activity context, irrelevant domains staying quiet, preserved preferences and host-owned practice/authority boundaries. Include overlapping companion domains when proposing a bundle. Evaluate effective participation in the actual activity; measure learning separately when learning is an intended outcome. Scenario coverage is not evidence that these behaviours occurred.

**Release gates:** no known permission/workflow regression; no unsupported success claims in reviewed cases; negative controls stay quiet; source/host artifacts validate; live host verification completed or explicitly reported as pending. Preserve change history and increment the companion version for behaviour or packaging changes.

## 8. Extending to another companion

1. Copy [`templates/example-companion/`](../templates/example-companion/) into `companions/<new-id>/`.
2. Name its domain, useful outcomes, exclusions, implicit need signals and follow-up interpretation. Don't use *all technical questions* as a trigger.
3. Author a portable `SKILL.md` and put longer domain references under `references/`.
4. Identify which adaptations are meaningful. It need not assume every learner is a novice or every domain relates to AI fluency.
   Keep the companion useful without a course brief. Put optional activity-specific facts in a context adapter, leaving canonical teaching unchanged across activities.
5. Declare the host's and framework's authority boundaries. If your design needs to execute its own commands or enforce approvals, it is not a CCS educational companion as defined here.
6. Reuse host adapter *patterns*, replacing the reference to the new skill; generate and merge one host bundle.
7. Build a task-specific behavioural case pack and validate the release. Evaluate real learner conversations only when authorized and report the evidence type accurately.

## 9. External specifications and compatibility references

- [Agent Skills format and progressive disclosure](https://agentskills.io/specification)
- [VS Code Agent Skills and native skill locations](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [VS Code project-level instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Codex Skills and repo guidance](https://developers.openai.com/codex/skills)
- [Agent Plugins packaging](https://developers.openai.com/plugins/build/plugins)

These are upstream product references; this CCS document is a project proposal and may need revisiting when hosts change.
