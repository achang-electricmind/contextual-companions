# Validation status

The proposal has a portable Git Companion implementation, offline artifact checks and behavioral evaluation specifications. Validation distinguishes package integrity from actual assistant behavior and learner outcomes.

## Artifact verification

Verified on **2026-11-01**:

- `sh scripts/verify --changed`: exit **0**, **27 offline tests passed**.
- The same command in a freshly extracted complete kit: exit **0**, **27 tests passed**.
- Rebuilding from the extracted kit reproduced all four archives byte for byte.

These checks cover manifest and skill metadata, reviewed source inventory, packaged links, native host paths, archive integrity, repeatable builds and installation in disposable directories. They also verify that optional activity context stays separate from canonical teaching and that local-only archives are excluded without traversal or content reads. The Git ignore rule for the local archive was checked in an isolated temporary repository.

Each native host package contains only the reusable skill tree. The complete kit contains the reviewed proposal sources, maintainer resources and matching host packages. No active installation or personal setting was changed by these checks.

## Static review

The [traceability table](../standard/EVALUATION.md) connects the core proposition to the standard, canonical Git instructions and review cases. Source review covers independent usefulness without calibration, stable domain teaching across activities, optional context adaptation, host authority, user preferences and explicit practice boundaries.

## Behavioral and outcome evidence

The **42 conversation scenarios** specify expected and forbidden behavior. Their format and coverage are checked offline; they have not been executed as a live model evaluation for this proposal.

Live-host invocation, model compliance, multi-companion coordination, effective participation and learning outcomes remain unverified. A discoverable file does not prove invocation, a plausible answer does not prove understanding, and task completion alone does not establish learning. Use the [evaluation playbook](../standard/EVALUATION.md) to assess these outcomes in the intended environment.
