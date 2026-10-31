# Paper-Level Inclusion Criteria

[Home](../README.md) · [Contribution guide](../CONTRIBUTING.md) · [Scope review](scope-review.md)

The core subject is acceleration of autoregressive image or visual generation. A general AR model paper is not automatically an acceleration paper. An efficient generator design must meet the same inference-cost requirement as an execution optimization.

## Required source information

| Item | Required information |
|---|---|
| Generated output | The visual output actually evaluated. Image, video and 3D tasks remain distinguishable. |
| AR process | The model or generation procedure being accelerated. Do not substitute a text answer produced from a visual input for generated visual content. |
| Intervention | The specific inference computation or storage that changes. For a learned replacement, identify which AR component or generation process is replaced. |
| Inference evidence | The original source location supporting reduced generation inference cost. Preserve the baseline and experimental setting when reporting a result. |
| Cost scope | State whether the result concerns complete generation or a component. Memory reductions and computational-complexity results retain their own meaning. |

If a required item is unresolved, keep the record pending or supporting background. Do not promote it merely because its title contains autoregressive, visual or efficient.

## Decisions that require care

- A smaller token count can motivate a mechanism. It does not by itself establish reduced measured latency. Source-reported FLOPs or complexity reductions must be labeled accordingly.
- A lower memory requirement is an inference-efficiency result. It is not automatically a measured speedup.
- Faster training and improved tokenizer reconstruction do not establish generation inference acceleration.
- Visual understanding, caption generation and action prediction do not become visual generation because their inputs contain images.
- An AR generator may use a diffusion conditional head. Its actual generation dependencies determine relevance. Generic diffusion-only acceleration does not qualify without an explicit AR generation application.
- A distilled replacement can qualify even if the student has a different generation structure. The source must identify the replaced AR process and the inference comparison.
- Test-time search requires its own baseline and budget. Improvements over multi-candidate reranking do not imply preservation or acceleration of an unchanged single-trajectory sampler.

These are inclusion checks, not a new scientific taxonomy. Source claims, independently checked results and unresolved interpretations remain distinguishable.

## Publication requirements

Use confirmed formal publication in the requested CCF venues. TMLR is explicitly allowed by the author. Workshop-only records are excluded. Other tracks keep their actual names. An old under-review header requires checking for a later publication.

## Inventory and manuscript

Background and excluded historical records remain distinguishable from the core list. Inventory size is not the number of confirmed acceleration methods. Earlier mechanism-relevance decisions do not waive these paper-level checks.

Current work is literature research and local repository preparation. Possible issues with the associated survey are recorded separately. Changes to manuscript prose, bibliography or figures require the author's review and explicit authorization.


## Reading and cost scope

Admission records identify whether the source evidence concerns latency, computational work or memory. A shorter token sequence alone is insufficient. An explicit model-evaluation or inference-FLOPs comparison can qualify as computational work, with no wall-clock claim added. A memory-efficiency paper can qualify when its AR-generation object is explicit, even if its measured latency increases. Its note must say so.

Official abstracts can establish a provisional source-supported core record when both the AR object and the inference result are explicit. The record must expose the missing performance-table check. This does not certify the experimental settings or a mathematical guarantee. Keep source-reported findings distinct from independent verification.
