# Git vocabulary in everyday work

Use only the term the person needs. Adapt examples to their task, not their job title. Definitions explain concepts; they do not prescribe operations or grant approval.

| Term | Plain-language meaning | Useful distinction |
| --- | --- | --- |
| Repository | A project collection with a history of changes | One workspace window can show several repositories. |
| Working copy | The checked-out files the person works with | Unsaved editor text is not on disk and is outside Git's index. |
| Branch | A named line of work in the project's history | Not a business-approval stage or a separate copied folder. |
| Stage | Select saved contents for an ordinary commit | Some commands stage automatically. Selected contents can differ from later edits; staging is not a dependable recovery checkpoint. |
| Commit | A recorded checkpoint of selected changes | Does not by itself send those changes to colleagues or guarantee recovery. |
| Remote | Another repository location used for collaboration | Its audience and access cannot be inferred from its name. |
| Push | Send commits to a remote repository | Sending is not evidence of review, approval or successful deployment. |
| Fetch | Update local information about remote history | Does not itself integrate that history into working files. |
| Pull | Fetch and integrate changes into the current line of work | Integration can change files or encounter conflicts; saved local edits may block it or conflict when incoming changes touch the same files or lines. |
| Pull request / merge request | A proposal to integrate changes, often with discussion and review | Creating it does not establish formal business or AIDE approval. |
| Merge | Combine lines of history | Overlap does not always mean conflict; a clean textual merge can still produce unintended meaning. |
| Conflict | A case Git cannot resolve automatically during integration | Git cannot decide which business meaning is correct. |

A document save, Git checkpoint, publication, review decision and verified business outcome are separate events. Explain the distinction relevant now, not the entire list every time.
