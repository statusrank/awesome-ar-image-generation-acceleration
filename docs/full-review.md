# Complete inventory review, 31 October 2026

[Home](../README.md) · [Original 186 decisions](../data/full_review_186.csv) · [All decisions](../data/scope_decisions.csv) · [Per-paper findings](../papers/paper-notes.md)

## What changed

All 186 original records received a paper-specific decision. There are 103 core papers, 68 background records and 15 pending records in that cohort. Formal-publication follow-up adds 46 records, of which 38 are core and eight remain pending. The current catalog has 232 records: 141 core, 68 background and 23 pending.

Admission depends on the generated output and the source-reported inference intervention. A formal venue or the word “autoregressive” in a title does not suffice. Efficient new generators qualify when the original source connects the design to an inference-cost result or a model-evaluation budget. Their results remain distinct from accelerating a fixed model.

Each record includes an operation-level description, reading extent and source location. The findings are selected-passage checks rather than full proof reviews. Core evidence comes from selected PDF passages for 138 records. DynamicVAR, VAR-Turbo and Reject Decoding retain abstract/selected-text limits without an inspected full performance table. No theorem is certified from an abstract.

## Consequential decisions

| Paper | Finding that controls the decision |
|---|---|
| TiTok | The inspected speed experiment uses MaskGIT-ViT. That result is not evidence of AR inference acceleration. Background. |
| CAT | The throughput improvement identified in the source concerns training. Background. |
| DPAR | Inspected cost evidence concerns training FLOPs. AR inference savings remain pending. |
| FlexTok, CaTok, ImageFolder and STAT | A shorter representation or reconstruction result alone does not establish the required inference-cost comparison. Pending. |
| UniCompress | Generation-inference timing is separated from visual-understanding timing. Core basis uses the former. |
| CoRe² | The AR evidence is the LlamaGen quality/time trade-off. Full-capacity operation is not described as faster, and SD3.5 results are not transferred to AR. |
| SpectralAR | Own measured times and source-rescaled comparator times retain different status. |
| StructMAR | The recovered original Table 5 compares 3.85s with a 3.56s Plain MAR baseline. Its headline speedup is against diffusion-based MIGC. Reclassified as background rather than an AR accelerator. |
| Quant VideoGen | KV-memory reduction is reported with latency overhead. Core memory-efficiency work, not a measured latency improvement. |
| Avatar Forcing | Motion-generation latency assumes pre-extracted audio features and a specified denoising budget. It is not complete audiovisual-system latency. |
| Deep Forcing and Context Forcing | Bounded context-memory designs are recorded as such. Long-video throughput does not by itself establish a standalone speedup from the memory component. |
| ARDM and VibeToken | Model-evaluation budgets or inference FLOPs remain distinct from measured wall-clock time. |
| Reject Decoding | Multi-path search acceleration uses its search-budget baseline. It is not a single-reference-sampler speculative-decoding guarantee. |

The paper-level notes give the original passages supporting these decisions. No speedup values were pooled across studies.

## Publication checks and remaining work

Workshop-only work is excluded. TMLR is included by author permission. Findings records do not automatically inherit main-track eligibility. Formal publication identity and the reading version are separate fields. A source with an old under-review header can still have a verified later publication.

The [coverage note](coverage.md) describes proceedings and journal searches. The [15 earlier unadmitted candidates](../data/unresolved_search_candidates.csv) remain outside the 232-record catalog. The original 69-entry review is historical and is superseded for admission decisions.

Bibliographic identity fields of the original 186 are preserved. The companion manuscript and bibliography are protected from changes in this task. Potential Survey issues are recorded locally for author review, not implemented.

The later [complete-directory follow-up](directory-review-20261031.md) records five additional core admissions and three pending papers. It explicitly separates directory enumeration from unfinished individual screening.
