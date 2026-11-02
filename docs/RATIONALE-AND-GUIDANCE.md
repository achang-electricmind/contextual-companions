# Purpose and rationale

**Reusable companions supply the surrounding knowledge people need to participate effectively in whatever they’re doing.**

People encounter unfamiliar concepts while pursuing another goal: sharing a requirement, discussing a design, reviewing a change or joining a team. A companion provides focused domain understanding in that existing activity, using the assistant conversation and context already available. Participation includes understanding and judgment as well as task completion.

The reusable unit is domain guidance. Its purpose, knowledge, relevance signals and explanation principles remain stable across everyday work, onboarding, collaboration, independent learning and formal training. A course-specific fork, proficiency survey or calibration step would undermine this portability. Domain relevance still matters: a Git companion should not teach Git during an unrelated email or business review.

## Context changes; core knowledge remains reusable

The companion answers the immediate question, connects to the person's actual artifact when established, and explains only what helps their understanding or next decision. It adapts to demonstrated comprehension and expressed preferences. Git knowledge and AI-tool fluency are independent; job titles and audience labels do not establish either.

An optional context adapter can describe the activity, relevant materials, terminology, local conventions and assistance boundaries. The host consumes it through existing conversation or instruction mechanisms. No new parser or runtime is needed, and an adapter is unnecessary when the existing context is sufficient. Missing optional context should lead to a bounded explanation, or a focused question when essential, rather than setup demands. See [context adapters](CONTEXT-ADAPTERS.md).

Host adapters solve a different problem: packaging and discovery in a supported assistant. Neither kind of adapter owns a second workflow or replaces canonical domain teaching. Several companions may be available, but only relevant contributions belong in the host's answer; their explanations should not accumulate into competing lessons.

## Training is one application

As training expands, differences in prerequisite knowledge can pull participants and facilitators away from the intended exercise. Preparing the working context and supplying relevant companions could help participants focus on the main learning goal. The same Git explanation can support a requirements workshop, developer onboarding or ordinary collaboration without changing Git Companion.

A workshop's explicit learner-practice boundaries belong to the host's surrounding instructions. Completing the exercise for someone may remove the intended practice; companions should support those existing boundaries without inventing teaching checkpoints. Outside that activity, they should not carry its goals or restrictions into unrelated work. Ordinary project use needs no learning objective.

## Authority and evidence

The companion owns explanations. The host owns tools and task execution; applicable AIDE/project workflows own their stages, artifacts and approvals. Context supplies facts and applicable guidance under normal host rules, not new permissions. Preserve depth/pause/off preferences when context changes; never require tools solely for teaching or inspect sensitive material for an analogy.

Editor save, staged contents, local history, remote publication, review request and substantive approval are different. An agent's narrative, an observed action and a verified effect are different too. Preserve those distinctions without appending a verification recipe to every conceptual answer.

Useful outcomes to examine are informed participation, relevant timing, fewer mistaken assumptions and less avoidable facilitator or teammate intervention. For training, also examine time spent practicing the intended skill and later independent application. These are intended benefits, not measured results of this release. Artifact tests validate distribution; static review checks the written contract; neither proves model behavior or educational effectiveness.
