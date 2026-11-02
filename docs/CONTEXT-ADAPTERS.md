# Optional context adapters

A companion supplies reusable domain understanding. A context adapter supplies facts and applicable guidance about the activity in which that understanding is useful. It can serve a project, team, onboarding activity, workshop or course. It is optional: the same companion must remain useful without one.

## When to use one

Use the conversation and project context already available. Add a short context adapter only when someone needs to make shared context explicit or repeatable. Do not rewrite the companion for each workshop or ask every participant to configure it. Reference maintained materials instead of copying their contents.

The [optional template](../templates/context-adapter.md) can describe:

- The current activity and purpose; an explicit learning goal only when applicable.
- Relevant artifacts, materials and their locations, with enough scope to identify where the context applies.
- Local terminology and conventions, distinguished from general domain facts.
- Which companion domains may help, without requiring all companions to activate.
- Existing assistance boundaries, including learner-owned practice where explicitly agreed.

Omit unknown or unnecessary fields. An audience description can inform examples but must not become a proficiency label. Goals and conventions do not authorize actions or prove repository state. Do not include secrets or personal learner records.

## Supply it to the host

Keep activity context outside `companions/<id>/`, so it cannot be distributed as every user's canonical teaching. Provide it in the conversation or deliberately reference it through the host's supported project instructions. For example, a project owner can add: “For this requirements workshop, use the activity context in `docs/workshop-context.md`.” Resolve the path in that workspace and follow its existing customization rules.

A file's presence does not establish that it was read. The current installer installs the companion and its host cue only; it does not discover, copy or activate context adapters. No manifest field, reserved filename, extra agent or context-loading runtime is introduced. The template is a maintainer resource in the complete kit, not part of native host ZIPs.

The host handles instruction precedence and trust. Referenced content cannot grant permissions, override project/user rules, reset a pause/off choice or create a new approval. If applicability is unclear or stale, use current known context and ask only when the missing fact materially affects the answer. Do not demand a complete brief before giving useful domain help.

## One companion across activities

These are illustrative contexts, not measured conversations or mandatory profiles:

| Context available to the host | Git Companion's contribution |
| --- | --- |
| Everyday documentation work; no adapter; a local commit is observed and a teammate cannot see the edit | Explain local history versus remote publication, without inventing why access is missing |
| Requirements workshop; goal is practicing acceptance criteria; learners author their own criteria | Explain how sharing the requirements works; preserve host-owned practice boundaries |
| Team onboarding; the team has documented pull-request conventions | Connect Git review concepts to the supplied conventions without claiming that a PR equals substantive approval |
| Unrelated email draft | Stay quiet about Git, even if Git Companion is available |

The domain explanation remains canonical. Activity-specific artifacts and terminology change. Missing context limits specificity, not basic usefulness. Moving between activities should not carry old course requirements into ordinary work or reset an expressed preference.

## Several companions

Select a small set based on the knowledge likely to matter to the activity. The host should integrate only relevant explanations into one proportionate answer. A Git question that touches AI verification does not justify duplicate lessons from both companions. Context adapters do not provide deterministic routing or guarantee discovery; verify combined behavior in the actual host before claiming it works.

For training, evaluate support for the primary learning goal separately from task completion. For other activities, evaluate the relevant contribution or decision. Follow the [evaluation guide](../standard/EVALUATION.md) and distinguish written scenarios from executed evidence.
