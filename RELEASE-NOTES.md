# Initial proposal: contents and packages

**Reusable companions supply the surrounding knowledge people need to participate effectively in whatever they’re doing.** This proposal defines the approach and provides Git Companion as a concrete implementation for relevant everyday work, collaboration, onboarding, independent learning and training.

## Included

- A proposed Contextual Companion Specification defining reusable domain guidance, relevance, adaptation, user preferences and authority boundaries.
- Git Companion: contextual explanations of saving, staging, committing, sharing, branches, reviews and recovery inside the existing assistant conversation.
- Optional context adapter guidance and a template for supplying activity facts, references and existing assistance boundaries without course-specific calibration.
- Host packages for Copilot in VS Code, Claude Code and Codex, with one canonical teaching source.
- Authoring templates, an optional preview-first installer, deterministic packaging tools and offline checks.
- Behavioral scenario specifications and an evaluation method for assessing relevance, correctness, participation and workflow continuity.

## Status and evidence

This is a proposal for evaluation. The [validation record](docs/VALIDATION.md) reports executed artifact checks and static review. The 42 behavioral scenarios are specifications, not successful interaction results. Live-host activation, model compliance, multi-companion coordination, effective participation and learning outcomes remain to be evaluated.

The installer includes the companion and its host cue. An optional context adapter is supplied through the host's normal context mechanisms. Follow the [inclusion guide](docs/NEXT-STEPS.md) to try the companion in an appropriate workspace.

## Packages

Package identifiers: **CCS 1.0.1 / Git Companion 0.8.2**.

- [Copilot package](releases/git-companion-copilot-0.8.2.zip)
- [Claude Code package](releases/git-companion-claude-0.8.2.zip)
- [Codex package](releases/git-companion-codex-0.8.2.zip)

Complete maintainer kit: `releases/contextual-companion-kit-1.0.1-git-companion-0.8.2.zip`. Checksums: `releases/SHA256SUMS.txt`.
