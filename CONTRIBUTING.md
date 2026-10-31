# Contributing

Please suggest a paper through an issue or pull request. Include its full title, publication source and a stable paper URL. Explain which computation the method changes and where it belongs in the catalog.

For code links, provide the author repository or an author-controlled paper page that identifies it. Do not infer an official repository from its name. An independent implementation can be proposed with an explicit label.

## Scope

Include papers that accelerate autoregressive image or visual generation. Efficient generator or tokenizer design is not sufficient by itself. The original source must connect the design to generation inference cost. Identify the output task and the AR computation that is accelerated. See the [paper-level inclusion criteria](docs/inclusion-criteria.md). Related masked-generation background remains separate. A paper published only in a workshop is excluded. If a subsequent main-conference or journal version exists, provide that version.

New main-collection entries require a confirmed formal publication in a CCF-listed venue, or TMLR under the author's explicit exception. The existing LlamaGen preprint remains labeled foundational background. A former under-review manuscript must be checked for a later formal publication. Workshop-only papers are excluded. Findings and other distinct tracks keep their exact names and are not automatically assigned the main conference's CCF grade.

Confirm relevance independently of venue. Tokenizer reconstruction, training throughput and visual understanding do not establish generation inference acceleration. Distinguish measurements of actual inference time from component-cost or memory results. Video and 3D generation require separate task labels. The scope-review CSV records mechanism relevance, which is not itself final core admission. A metadata-only candidate stays pending.

## Editing the catalog

1. Edit `data/papers.json`. Keep one stable ID for each distinct paper.
2. Preserve exact method and component names from the source. Explain any proposed reclassification.
3. Run `python scripts/render.py` and `python scripts/validate.py`.
4. Include the generated changes and a short changelog entry in the pull request.

Report incorrect metadata separately from disagreements about a paper's guarantee. A correction to a theoretical claim requires the relevant source location and assumptions.

Original contributions to the documentation and catalog are submitted under CC BY 4.0. Changes to maintenance scripts use MIT. These terms do not relicense the linked works.


## Source support for core admission

Provide the concrete AR-generation object, the intervention and the exact source passage or table. State which cost was reduced and what baseline was used. Training-only improvements and token compression without an inference comparison do not suffice. Label the reading extent and unresolved source details. See the [current review](docs/full-review.md). Do not silently promote a pending record or rewrite a historical cohort decision file by hand.
