# Complete-directory follow-up, 31 October 2026

[Home](../README.md) · [Coverage](coverage.md) · [Directory entries](../data/complete_directory_entries_20261031.csv) · [Reading progress](../data/complete_directory_progress_20261031.csv) · [Source decisions](../data/directory_candidate_decisions_20261031.csv)

The local catalog now contains **232 records: 141 core, 68 background and 23 pending**. Five source-checked papers were added to the core. Three formally published candidates remain pending. Image, video and 3D results are kept separate.

## Conference directories

| Venue | Year | Extracted entries | Source and exact retrieval extent |
|---|---:|---:|---|
| ACM MM | 2022 | 829 | [Official SIGMM OpenTOC, including original abstracts. Non-research and Workshop-summary entries require exclusion.](https://sigmm.org/opentoc/MM2022-TOC) |
| ACM MM | 2023 | 1,014 | [Official SIGMM OpenTOC, including original abstracts. Non-research and Workshop-summary entries require exclusion.](https://sigmm.org/opentoc/MM2023-TOC) |
| BMVC | 2023 | 267 | [Official proceedings table, 267 entries. All 267 titles individually inspected. Twenty-four potential matches received source-level decisions.](https://bmvc2023.cvml.group/proceedings/) |
| ACM MM | 2024 | 1,151 | [All 1,151 title/author pairs in the official accepted regular-paper list. Final individual DOI matching is not complete.](https://2024.acmmm.org/accepted-list) |
| IJCAI | 2024 | 1,048 | [Official complete index. Main, survey, demo and other tracks are distinguished by individual publication pages.](https://ijcai.org/proceedings/2024/) |
| IJCAI | 2025 | 1,280 | [Official complete index. Main, survey, demo and other tracks are distinguished by individual publication pages.](https://ijcai.org/proceedings/2025/) |
| ECCV | 2026 | 2,835 | [All 78 main-conference Springer books, including all TOC pagination. All 2,835 unique chapter counts match the volume totals.](https://eccv.ecva.net/) |
| ICASSP | 2022 | 1,865 | [Full 163-page printed TOC. Four entries retain the source’s missing session-prefix text.](https://www.proceedings.com/content/065/065074webtoc.pdf) |
| ICASSP | 2023 | 2,688 | [Full 163-page printed TOC. A source N/A page number remains N/A. Wrapped Wav2vec 2.0 title repaired.](https://www.proceedings.com/content/071/071028webtoc.pdf) |
| ICASSP | 2025 | 3,301 | [Full 201-page printed TOC. Individual IEEE publication/PDF matching is not complete.](https://www.proceedings.com/content/081/081086webtoc.pdf) |

These ten directories contain **16,278 entries**. A retrieved title is not an eligible paper. Workshop titles that occur in an ACM main-volume TOC do not enter the core list.

## Journal directories

Publisher-deposited metadata covers the 19 previously enumerated journals from 2022 through 30 October 2026. Five graphics journals were added through 31 October 2026. JMLR and TMLR use their official accepted-paper indexes. All returned entries with titles were retained, rather than retaining only keyword matches.

| Journal | Returned entries with titles | Retrieval extent |
|---|---:|---|
| TPAMI | 4,201 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IJCV | 1,542 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| TIP | 2,963 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| TNNLS | 5,376 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| TMM | 4,239 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| TCSVT | 4,841 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Pattern Recognition | 4,806 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Pattern Recognition Letters | 1,567 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Neurocomputing | 8,949 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Neural Networks | 3,963 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Machine Learning | 1,076 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| ACM Computing Surveys | 1,489 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| ACM TOMM | 1,531 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IEEE TCAD | 2,457 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IEEE Transactions on Computers | 1,361 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| ACM TACO | 572 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IEEE JSSC | 2,258 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Information Fusion | 2,665 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IEEE TMC | 4,092 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| ACM TOG | 1,309 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Computer Graphics Forum | 1,396 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| IEEE TVCG | 3,322 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| The Visual Computer | 2,441 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| Computational Visual Media | 347 | Crossref cursor pages to the reported stream end. Publisher DOI registration is not claim-level verification |
| JMLR | 1,690 | Official volumes 23–27, 2022–2026 |
| TMLR | 5,000 | 5,000 entries returned by the official accepted list. No outgoing pagination found. Global completeness beyond this response is not independently established |

These 26 journal titles yield **75,453 retained metadata entries**. Computer Graphics Forum returned 1,427 distinct DOI records, of which 31 had no title and are not fabricated as paper entries. Journal records can include front matter or corrections. No CCF grade is inferred from this list. TMLR is included under the author’s explicit exception.

## Original-source findings

| Added core paper | Specific acceleration object | Source boundary |
|---|---|---|
| [HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) | Hierarchical denoising and pipelined execution of AR video blocks | Streaming throughput and per-chunk latency, not complete-video latency. The approximately 1.8x headline matches the throughput ratio, not the listed latency ratio |
| [Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) | KV-cache storage and attention computation in streaming AR video generators | Peak GPU memory and the source-reported latency breakdown. Attention-only and quantized combined results remain separate |
| [SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) | Shape-token sequence length and sequential AR transformer evaluations | Complete reported shape-generation time on one RTX 4090. Text-to-3D AR comparisons use different resolutions. The headline 10x averages heterogeneous image-to-3D baselines |
| [Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) | Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator | Streaming FPS and time to first frame at 720x400. GPU count changes across ablations. These values are not complete conversational latency or a same-hardware speed ratio |
| [Efficiency-optimized Video Diffusion Models](https://dl.acm.org/doi/10.1145/3581783.3612406) | Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation | Denoiser FLOPs and reported model latency. The approximately 10x headline concerns arithmetic reduction. Table 9 lists 16.5 to 6.1 ms and 26.4 to 7.5 ms for two unlabeled configurations, not a 10x end-to-end video gain |

The original-source notes specify the relevant PDF pages. HiAR’s throughput ratio is not equated with its latency ratio. SuperVoxelGPT’s mixed-baseline average is not described as an AR-only gain. EVDM’s arithmetic reduction is not substituted for measured complete-video latency.

Stable Control VAR remains pending because its original experiment was not retrieved. Grow3D remains pending because the ACM-deposited abstract could be checked but its performance table could not. The dual-stream visual tokenizer remains pending because its inspected experiments establish representation and reconstruction results, not AR inference-cost savings.

Propose-and-Complete is recorded outside the core: its 0.116 s network result becomes 4.013 s under the default 500-iteration post-optimization, compared with 0.171 s for ATISS. ELT’s inspected efficiency experiment uses MaskGIT rather than an AR generator. The IJCAI 2025 G3PT main paper provides geometry-quality and tokenization results without an established inference-cost comparison. These papers were not added merely because they contain relevant names.

## Remaining screening

All **91,731** returned title records have a row in the [directory export](../data/complete_directory_entries_20261031.csv). Semantic text similarity was used only to order inspection, never to assign eligibility. **1,355** individual titles have an explicit reading record. **51** records have a new original-source decision. Existing catalog decisions retain their earlier reading extent.

**90,343 entries have not been individually adjudicated.** Retrieval gaps for the requested directories have been substantially repaired, but the requested exhaustive individual screening is unfinished. No zero-result claim is made for an unread venue/year or journal. The per-entry status must be checked before describing coverage as complete.

The [source registry](../data/complete_directory_sources_20261031.csv) links every row to its actual directory source. Private downloaded papers and raw source responses stay outside this public repository. The companion Survey has not been edited or compiled.
