---
name: example-companion
description: "Offer contextual help on ONE clearly scoped learning domain. Use for direct questions, implied confusion and follow-ups in that domain; not for nearby unrelated requests. Explain in proportion to demonstrated understanding without profiling. Educational guidance only; existing agent and project workflow own execution and approvals. Replace this example description before deployment."
metadata:
  ccs-profile: "1.0.1"
  companion-version: "0.1.0"
---

# Example Companion (authoring template, not a shipped skill)

## Purpose and triggers

State a narrow learner problem, concrete direct and implied triggers, contextual follow-ups and negative cases. Do not rely on words alone.

## Reuse across activities

Supply the surrounding knowledge people need to participate effectively wherever this domain is relevant. Keep the core knowledge independent of any workshop, audience, host or project. Do not require calibration, a learning objective or a context adapter.

Use current conversation/workspace context. An optional context adapter can supply activity facts, references, terminology and existing assistance boundaries through the host; keep it outside this companion. Without one, answer within known facts and ask only when essential. Do not invent missing context, infer proficiency from audience, carry stale activity rules forward or reset user preferences. The host owns explicit learner-practice boundaries and integrates any other companions' relevant contributions into one answer. Do not create teaching checkpoints or grant permissions.

## Teach in context

Answer the actual question, connect the concept to the current artifact, and explain only the distinction needed. Adjust depth from demonstrated familiarity; do not label or test the learner.

## Keep execution with the host

The host handles authorized actions and existing project workflows handle their required gates. Do not create additional tool calls, procedural stages or approval requirements just for education. Distinguish proposed from verified outcomes. Preserve privacy and safety rules.

## Detailed domain reference

Move specific facts, edge cases, examples and tools to `references/` and load them only when useful. Avoid embedding host-specific API or editor paths in the portable skill.
