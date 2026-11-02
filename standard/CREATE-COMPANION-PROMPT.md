# Reusable directive: create or refine a Contextual Companion

Use this directive with a coding agent that can read this repository. Replace the three user-input lines and point the agent at `standard/CCS-1.0.md`.

```text
Act as a Principal Engineer and instructional systems designer. Build or refine a
Contextual Companion that conforms to standard/CCS-1.0.md and the Agent Skills
format. Treat companions/git-companion as a reference implementation, not as a
source of Git-specific assumptions.

DOMAIN: <the single topic this companion helps learners understand>
REPRESENTATIVE ACTIVITIES: <everyday work, collaboration, onboarding, learning, or other relevant activities; examples, not required configuration>
IMPORTANT BOUNDARIES: <what this companion must not teach, trigger, own, or change>

Required approach:
1. Define the surrounding domain knowledge people need to participate effectively.
   Show useful help without calibration, a course brief or a context adapter, and
   reuse of the same companion across different activities. Define positive,
   implicit and contextual activation, counterexamples and changing understanding.
2. Keep the interaction in the host agent's existing conversation. Do not invent
   an independent agent, a mandatory onboarding/quiz, a proprietary proficiency
   profile, new approvals, hidden monitoring or educational-only tool operations.
3. Keep all domain teaching in a canonical, portable Agent Skill. Use compact
   SKILL.md instructions and on-demand references for additional knowledge.
   Separate optional context adapters (activity facts, references and existing
   assistance boundaries) from host adapters (placement and discovery). Use
   existing context first; add no required context parser, manifest field or setup.
   Preserve host authority and user preferences, including when activities change.
4. Write companion.json against standard/companion.schema.json. Declare separate
   domain knowledge dimensions only when they actually help. Respect the host's
   normal execution and the project's existing SDLC/workflow authority.
5. Reuse the host adapter contracts in adapters/ to generate native host packages for
   Copilot in VS Code, Claude Code and Codex, but do not overwrite project-owned
   instructions. Prefer dry-run and explicit opt-in to repository modifications.
6. Create at least 12 real evaluation scenarios in tests/cases/<id>.json,
   including direct, implicit, contextual follow-up, negative, expert, action,
   evidence and security situations. Also cover absent/partial/stale context,
   cross-activity reuse, overlapping domains and host-owned practice boundaries.
   For each, record the desired response and a specific dangerous or distracting
   behaviour that must not occur.
7. Run schema, packaging and non-destructive install tests. Keep reproducible
   artifacts. Clearly separate deterministic checks from model simulations and
   real host discovery/learner evaluation evidence.

Before declaring completion, compare your implementation with the CCS contract,
identify scope creep, contradictory host/project rules, ambiguous trigger words,
unsafe tool assumptions, excessive prompting and redundant reference material.
Explain improvements and unresolved limitations. Never claim a host activated a
skill without real host evidence.
```

See the [context adapter guide](../docs/CONTEXT-ADAPTERS.md) for optional situational guidance. A learning session is one application of the reusable companion.

This directive intentionally does not demand a plugin or MCP server. Add those only when a companion needs a real capability beyond reusable educational context, and reassess whether it remains a CCS educational companion.

Add each reviewed source resource to `distribution-files.json` before building; unexpected files are rejected. Preserve user depth/pause preferences and keep host-control documentation separate from default shared behavior.
