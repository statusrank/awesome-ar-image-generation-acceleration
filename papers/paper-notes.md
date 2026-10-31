# Paper-level source notes

[Home](../README.md) · [Core](core.md) · [Background](background.md) · [Pending](pending.md)

Each note states the reading extent. Selected PDF passages are not a full-proof review or an independent reproduction. PDF page numbers count the downloaded PDF pages, including a cover where present. The reading version can be an author manuscript corresponding to a verified formal publication.

<a name="adanat"></a>

## adanat

**AdaNAT: Exploring Adaptive Policy for Token-Based Image Generation**. ECCV, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | MaskGIT-style non-autoregressive image synthesis |
| Intervention | Learns sample-dependent unmasking policies |
| Original-source basis | The abstract explicitly identifies NATs as its object. No AR-generator application established here |
| Cost boundary | Non-AR masked generation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02478.pdf#page=1) · [Formal publication record](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2478_ECCV_2024_paper.php)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="amskv"></a>

## amskv

**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**. AAAI, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale VAR KV memory and attention |
| Intervention | Retains condensed and local scales with adaptive cache allocation |
| Original-source basis | Original experiments compare cache budget and generation quality against full-cache VAR |
| Cost boundary | KV storage and attention, not automatically end-to-end latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/download/39936/43897#page=7) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/39936)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="arpg"></a>

## arpg

**Autoregressive Image Generation with Randomized Parallel Decoding**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Random-order AR image decoding |
| Intervention | Decouples position guidance and content prediction for grouped decoding |
| Original-source basis | Original source reports image throughput and GPU-memory comparisons for ARPG |
| Cost boundary | Generator throughput and memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 14; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf#page=14) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="arvar"></a>

## arvar

**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | HART and Infinity next-scale inference |
| Intervention | Uses earlier attention for token selection and removes a late guidance branch |
| Original-source basis | Original source reports inference speed comparisons and component ablations |
| Cost boundary | Reported image inference latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 14; abstract/selected method and performance passages |

[Reading source](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf#page=14) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/3564)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="autonat"></a>

## autonat

**Revisiting Non-Autoregressive Transformers for Efficient Image Synthesis**. CVPR, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Non-autoregressive image synthesis |
| Intervention | Optimizes NAT training and generation strategies |
| Original-source basis | The source explicitly studies NATs, not an accelerated AR reference generator |
| Cost boundary | Non-AR masked generation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Revisiting_Non-Autoregressive_Transformers_for_Efficient_Image_Synthesis_CVPR_2024_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Revisiting_Non-Autoregressive_Transformers_for_Efficient_Image_Synthesis_CVPR_2024_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="barmbm"></a>

## bar_mbm

**Autoregressive Image Generation with Masked Bit Modeling**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Bitwise AR image generation |
| Intervention | Masked bit modeling supports efficient prediction of large-vocabulary image representations |
| Original-source basis | Source compares generation FID with image throughput |
| Cost boundary | New-generator throughput |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/yu26z.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="blockwise"></a>

## blockwise

**Blockwise Parallel Decoding for Deep Autoregressive Models**. NeurIPS, 2018.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image super-resolution |
| Study type | execution optimization |
| Specific object | AR image super-resolution decoding |
| Intervention | Predicts blocks provisionally and commits the prefix validated by a scoring model |
| Original-source basis | Source evaluates image super-resolution iteration counts and wall-clock decoding speed |
| Cost boundary | Historical 2018 image super-resolution, separate from 2022–2026 additions |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html#page=7) · [Formal publication record](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="catok"></a>

## catok

**CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image tokens and MeanFlow image reconstruction |
| Intervention | Causal 1D tokens with one-step or multi-step image decoding |
| Original-source basis | The inspected tables report tokens, reconstruction steps and quality. A measured AR inference-cost comparison was not located |
| Cost boundary | Operation counts only in inspected passages |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |
| Unresolved item | The inspected tables report tokens, reconstruction steps and quality. A measured AR inference-cost comparison was not located |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="clip"></a>

## clip

**Learning Transferable Visual Models From Natural Language Supervision**. ICML, 2021.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Image-text representation and evaluation support |
| Intervention | Contrastive image-text pretraining |
| Original-source basis | Not an AR visual-generation accelerator |
| Cost boundary | Evaluation/background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v139/radford21a.html#page=1) · [Formal publication record](https://proceedings.mlr.press/v139/radford21a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="code"></a>

## code

**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale VAR computation and memory |
| Intervention | Large model predicts coarse scales and a smaller model refines later scales |
| Original-source basis | Source compares VAR generation time and memory with collaborative decoding |
| Cost boundary | Generation time and GPU memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 2; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2411.17787#page=2) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="coolsd"></a>

## cool_sd

**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**. AAAI, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image speculative verification |
| Intervention | Anneals relaxed acceptance with a specified resampling distribution |
| Original-source basis | Source reports speed-quality experiments on visual AR generators |
| Cost boundary | Speculative generation latency, no new preservation certification |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/download/39489/43450#page=7) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/39489)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="csd"></a>

## csd

**CSD: Content-aware Speculative Decoding for Efficient Image Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image speculative verification |
| Intervention | Uses content-dependent acceptance relaxation and resampling |
| Original-source basis | Source evaluates inference acceleration on Lumina-mGPT and image metrics |
| Cost boundary | Visual AR generation runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v306/wang26gi.html#page=9) · [Formal publication record](https://proceedings.mlr.press/v306/wang26gi.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="cspd"></a>

## cspd

**Continuous Speculative Decoding for Autoregressive Image Generation**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR continuous conditional sampling |
| Intervention | Uses continuous speculative proposals and approximate trajectory alignment |
| Original-source basis | Source reports wall-time comparisons with default MAR |
| Cost boundary | MAR inference time, trajectory/endpoint guarantees not rechecked here |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 2; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2411.11925#page=2) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/5776)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dcar"></a>

## dc_ar

**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Hybrid masked AR text-to-image generator |
| Intervention | Deep-compression hybrid tokenizer reduces spatial sequence burden |
| Original-source basis | Original source explicitly reports throughput and latency against prior generators |
| Cost boundary | New-generator throughput and latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dd1"></a>

## dd1

**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | learned replacement of an AR process |
| Specific object | Complete VAR and LlamaGen latent generation |
| Intervention | Distills AR sampling into a few-step flow generator |
| Original-source basis | Original source compares steady-state wall time and quality against AR teachers |
| Cost boundary | Learned replacement of AR latent sampler |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 10; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2412.17153v3#page=10) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dd2"></a>

## dd2

**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | learned replacement of an AR process |
| Specific object | Complete VAR and LlamaGen latent generation |
| Intervention | Conditional score distillation trains a one-step replacement |
| Original-source basis | Source reports inference speed and image quality relative to AR teachers |
| Cost boundary | Learned replacement, not unchanged-reference execution |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="depthvar"></a>

## depthvar

**Depth Adaptive Efficient Visual Autoregressive Modeling**. CVPR Findings, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | VAR token-wise computational depth |
| Intervention | Schedules how many transformer blocks each token receives |
| Original-source basis | Acceleration evidence is present, but the confirmed publication is CVPR Findings. Main-track CCF equivalence is not established |
| Cost boundary | Venue-track eligibility unresolved |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |
| Unresolved item | Acceleration evidence is present, but the confirmed publication is CVPR Findings. Main-track CCF equivalence is not established |

[Reading source](https://arxiv.org/pdf/2604.17286#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026F/html/Li_Depth_Adaptive_Efficient_Visual_Autoregressive_Modeling_CVPRF_2026_paper.html)

Venue check: publication confirmed; requested CCF venue/track eligibility unresolved

<a name="diagonalsparsity"></a>

## diagonal_sparsity

**Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation**. IISWC, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image attention and KV accesses |
| Intervention | Studies diagonal attention sparsity |
| Original-source basis | Mechanism is relevant. The confirmed IISWC venue is not established under the requested CCF list |
| Cost boundary | Venue eligibility unresolved |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |
| Unresolved item | Mechanism is relevant. The confirmed IISWC venue is not established under the requested CCF list |

[Reading source](https://iiswc.org/iiswc2026/program.html#page=1) · [Formal publication record](https://iiswc.org/iiswc2026/program.html)

Venue check: publication confirmed; requested CCF venue/track eligibility unresolved

<a name="dimo"></a>

## dimo

**Di[M]O: Distilling Masked Diffusion Models into One-step Generator**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked diffusion image generator distillation |
| Intervention | Distills MaskGIT/Meissonic-style teachers into one-step students |
| Original-source basis | Inspected teacher experiments concern masked diffusion generators, not an identified AR teacher |
| Cost boundary | Related non-AR distillation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_DiMO_Distilling_Masked_Diffusion_Models_into_One-step_Generator_ICCV_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_DiMO_Distilling_Masked_Diffusion_Models_into_One-step_Generator_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dpar"></a>

## dpar

**DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image token sequence |
| Intervention | Entropy-guided dynamic patchification |
| Original-source basis | The inspected efficiency result is training FLOPs. The paper calls generation-speed improvements a future direction |
| Cost boundary | AR inference cost not established by training FLOPs |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |
| Unresolved item | The inspected efficiency result is training FLOPs. The paper calls generation-speed improvements a future direction |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="driftar"></a>

## driftar

**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Hybrid AR prediction and iterative visual decoding |
| Intervention | Entropy-guided speculation and one-step drifting decoder |
| Original-source basis | Source studies joint acceleration of the sequential AR stage and iterative decoder |
| Cost boundary | AR stage plus visual decoder |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 13; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2603.28049#page=13) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/4877)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ear"></a>

## ear

**Learning to Expand Images for Efficient Visual Autoregressive Modeling**. ACM MM, 2026.

| Field | Paper-specific finding |
|---|---|
| Publication note | Accepted |
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image generation order and parallel groups |
| Intervention | Spiral expansion with length-adaptive parallel decoding |
| Original-source basis | Source reports image generation quality-efficiency comparisons |
| Cost boundary | New-generator sampling throughput |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 11; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2511.15499v1#page=11) · [Formal publication record](https://2026.acmmm.org/site/technical-programme.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="emigm"></a>

## emigm

**Effective and Efficient Masked Image Generation Models**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Continuous masked image generation including MAR |
| Intervention | Revises masking, sampling schedule and conditional token modeling |
| Original-source basis | Source includes MAR in its formulation and reports sampling-time/quality comparisons |
| Cost boundary | Continuous MAR-related variant, not every discrete masked model |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 29; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf#page=29) · [Formal publication record](https://proceedings.mlr.press/v267/you25d.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="emu3"></a>

## emu3

**Multimodal learning with next-token prediction for large multimodal models**. Nature, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image; video; multimodal understanding |
| Study type | not admitted to core |
| Specific object | Reference multimodal AR image/video generator |
| Intervention | Unified next-token modeling |
| Original-source basis | General multimodal model. No specific inference-acceleration contribution is established for this list |
| Cost boundary | Reference generator, Nature outside requested venue filter |
| Reading extent | official abstract / selected original-source text |
| Source location | Official Nature article abstract and architecture section |

[Reading source](https://www.nature.com/articles/s41586-025-10041-x) · [Formal publication record](https://www.nature.com/articles/s41586-025-10041-x)

Venue check: background only; no core venue admission inferred

<a name="enat"></a>

## enat

**ENAT: Rethinking Spatial-temporal Interactions in Token-based Image Synthesis**. NeurIPS, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Non-autoregressive masked image generation |
| Intervention | Separates visible-token encoding and decoding with temporal feature reuse |
| Original-source basis | Source explicitly frames the method as NAT; no direct AR application established |
| Cost boundary | Related non-AR computation reuse |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2024/file/a488aa1a0c00d76db8a922ef7815a786-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a488aa1a0c00d76db8a922ef7815a786-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="energyar"></a>

## energy_ar

**Continuous Visual Autoregressive Generation via Score Maximization**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Continuous AR per-position conditional sampling |
| Intervention | Models continuous conditionals with score maximization instead of iterative diffusion |
| Original-source basis | Source explicitly contrasts conditional sampling efficiency with per-token diffusion |
| Cost boundary | Conditional-head computational work |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v267/shao25b.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="entropydecoding"></a>

## entropy_decoding

**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Visual AR sampling and speculation |
| Intervention | Entropy controls temperature and relaxed acceptance |
| Original-source basis | Source reports reduced inference cost for speculative visual generation |
| Cost boundary | AR inference cost |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf#page=9) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="evar"></a>

## evar

**EVAR: Edge Visual Autoregressive Models via Principled Pruning**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale VAR parameter and execution cost |
| Intervention | Structured pruning with scale-aware compensation and distillation |
| Original-source basis | Source reports single-image iOS latency for pruned versus original VAR |
| Cost boundary | Measured edge inference latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf#page=1) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/3596)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="farmer"></a>

## farmer

**FARMER: Flow AutoRegressive Transformer over Pixels**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Pixel-level autoregressive normalizing-flow sampling |
| Intervention | Self-supervised dimension reduction reduces sequential sampling burden |
| Original-source basis | Source reports an inference-speed intervention and sampling comparisons |
| Cost boundary | Pixel-space AR/flow hybrid, not latent-token SD |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="fastervar"></a>

## fastervar

**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Late-scale VAR execution |
| Intervention | Adaptive stage selection and reduced computation at costly scales |
| Original-source basis | Source reports runtime evaluations of the acceleration method |
| Cost boundary | Next-scale inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 18; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2512.16483#page=18) · [Formal publication record](https://proceedings.mlr.press/v306/li26go.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="fasthybrid"></a>

## fasthybrid

**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Hybrid AR image generator with diffusion decoder |
| Intervention | Lookahead and guided decoding reduce hybrid generation computation |
| Original-source basis | Source evaluates accelerated hybrid AR inference |
| Cost boundary | AR plus conditional diffusion decoding |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="fastvar"></a>

## fastvar

**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | High-resolution next-scale token processing |
| Intervention | Cached token pruning forwards selected tokens and recovers omitted states |
| Original-source basis | Original source reports runtime and resolution-scaling experiments |
| Cost boundary | VAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2503.23367#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="fid"></a>

## fid

**GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium**. NeurIPS, 2017.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Image-distribution evaluation |
| Intervention | FID-related evaluation reference |
| Original-source basis | A quality metric source, not an accelerator |
| Cost boundary | Evaluation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://papers.nips.cc/paper_files/paper/2017/hash/8a1d694707eb0fefe65871369074926d-Abstract.html#page=1) · [Formal publication record](https://papers.nips.cc/paper_files/paper/2017/hash/8a1d694707eb0fefe65871369074926d-Abstract.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="flextok"></a>

## flextok

**FlexTok: Resampling Images into 1D Token Sequences of Flexible Length**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | GPT-style image generation with compact 1D codes |
| Intervention | Variable-length discrete codes followed by flow decoding |
| Original-source basis | The inspected source establishes AR use and code lengths. Complete inference-cost savings were not verified |
| Cost boundary | Token count is not measured generation latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |
| Unresolved item | The inspected source establishes AR use and code lengths. Complete inference-cost savings were not verified |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachmann25a/bachmann25a.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v267/bachmann25a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="flexvar"></a>

## flexvar

**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Next-scale generator schedule |
| Intervention | Ground-truth scale prediction supports variable inference-stage budgets |
| Original-source basis | Source discusses faster inference with fewer stages and reports flexible-step generation |
| Cost boundary | New-generator stage/quality trade-off |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf#page=6) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="flowar"></a>

## flowar

**FlowAR: Scale-wise Autoregressive Image Generation Meets Flow Matching**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Continuous next-scale image generator |
| Intervention | Pairs a simplified scale schedule with flow-matching conditionals |
| Original-source basis | Inspected source centers modular generation and quality. An explicit inference-cost reduction was not located |
| Cost boundary | Reference hybrid generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ren25e/ren25e.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v267/ren25e.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="freqexit"></a>

## freqexit

**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR transformer depth at inference |
| Intervention | Trains frequency-aware early-exit behavior |
| Original-source basis | Source evaluates dynamic inference and computational savings |
| Cost boundary | Depth-adaptive inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 25; abstract/selected method and performance passages |

[Reading source](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf#page=25) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="geneval"></a>

## geneval

**GenEval: An object-focused framework for evaluating text-to-image alignment**. NeurIPS Datasets and Benchmarks, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Text-to-image task evaluation |
| Intervention | Object-focused alignment benchmark |
| Original-source basis | Evaluation resource |
| Cost boundary | Evaluation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2310.11513#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a3bf71c7c63f0c3bcb7ff67c67b1e7b1-Abstract-Datasets_and_Benchmarks.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="gigatok"></a>

## gigatok

**GigaTok: Scaling Visual Tokenizers to 3 Billion Parameters for Autoregressive Image Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Visual tokenizer scaling |
| Intervention | Semantic regularization improves tokenizer scaling and downstream quality |
| Original-source basis | Inspected source concerns reconstruction/generation quality and training convergence, not a verified inference-cost result |
| Cost boundary | Tokenizer/modeling background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Xiong_GigaTok_Scaling_Visual_Tokenizers_to_3_Billion_Parameters_for_Autoregressive_ICCV_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Xiong_GigaTok_Scaling_Visual_Tokenizers_to_3_Billion_Parameters_for_Autoregressive_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="gsd"></a>

## gsd

**Grouped Speculative Decoding for Autoregressive Image Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image speculative decoding |
| Intervention | Groups spatially related token candidates for verification |
| Original-source basis | Source explicitly reports accelerated visual AR inference |
| Cost boundary | Sampling runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="gtr"></a>

## gtr

**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR stages and inner sampling budget |
| Intervention | Separates structure generation and detail reconstruction with frequency-weighted selection |
| Original-source basis | Source compares MAR generation speed and quality under the two-stage strategy |
| Cost boundary | MAR sampling runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="hack"></a>

## hack

**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**. AAAI, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR historical KV storage |
| Intervention | Head-dependent cache compression |
| Original-source basis | Source evaluates inference cache requirements and generation behavior |
| Cost boundary | KV memory and attention |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2504.09261#page=1) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/39686)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="halton"></a>

## halton

**Halton Scheduler for Masked Generative Image Transformer**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | MaskGIT unmasking scheduler |
| Intervention | Low-discrepancy spatial position schedule |
| Original-source basis | Source applies to MaskGIT rather than an identified AR reference model |
| Cost boundary | Related non-AR scheduling |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce29be756db03b0562204265256db075-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ce29be756db03b0562204265256db075-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="hawk"></a>

## hawk

**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR text-to-image speculative proposals |
| Intervention | Spatial-context drafting improves candidate prediction |
| Original-source basis | Source reports visual AR inference speed and drafting ablations |
| Cost boundary | Speculative image generation runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="himar"></a>

## himar

**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Hierarchical continuous masked AR image generation |
| Intervention | Low-resolution pivots condition later high-resolution groups |
| Original-source basis | Source contains a speed/accuracy experiment and generation-step comparisons |
| Cost boundary | New-generator sampling speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2505.20288v1#page=8) · [Formal publication record](https://proceedings.mlr.press/v267/zheng25i.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="hmar"></a>

## hmar

**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Hierarchical next-scale masked AR execution |
| Intervention | Hierarchical ordering and IO-aware block-sparse attention kernels |
| Original-source basis | Source reports inference time and inference-memory reductions against VAR |
| Cost boundary | New-generator inference time and memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2506.04421v1#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="infinity"></a>

## infinity

**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | High-resolution next-scale AR generation |
| Intervention | Bitwise prediction avoids a very large categorical classifier |
| Original-source basis | Original source reports high-resolution image generation time |
| Cost boundary | New-generator inference, not a controlled execution-only comparison |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lactokgen"></a>

## lactokgen

**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | High-resolution AR prior plus image reconstruction |
| Intervention | Compact discrete tokens with latent-consistency decoding |
| Original-source basis | Source reports per-image time on A800 with vLLM, including AR baselines |
| Cost boundary | Image generation time |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lantern"></a>

## lantern

**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Visual AR speculative acceptance |
| Intervention | Latent-neighborhood relaxed acceptance |
| Original-source basis | Source reports sampling-speed and image-quality experiments |
| Cost boundary | Relaxed speculative runtime, not unqualified distribution equality |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 22; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf#page=22) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lazymar"></a>

## lazymar

**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR repeated feature computation and guidance |
| Intervention | Caches stable token features and branch differences |
| Original-source basis | Source reports MAR inference-time comparisons and refresh behavior |
| Cost boundary | MAR feature/head inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 5; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf#page=5) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lazyvar"></a>

## lazyvar

**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR token processing and scale schedule |
| Intervention | Scale-dependent token pruning plus grouped scale decoding |
| Original-source basis | Source reports generation acceleration and ablations |
| Cost boundary | VAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="leviathan2023"></a>

## leviathan2023

**Fast Inference from Transformers via Speculative Decoding**. ICML, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | General/text stochastic speculative sampling |
| Intervention | Target acceptance and positive-residual correction |
| Original-source basis | Methodological foundation. The inspected source does not establish visual-generation experiments |
| Cost boundary | Sampling theory/background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v202/leviathan23a/leviathan23a.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v202/leviathan23a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="linear"></a>

## linear

**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Causal visual AR KV storage |
| Intervention | Progressively evicts historical lines outside retained dependency regions |
| Original-source basis | Source reports GPU-memory and throughput measurements on image generators |
| Cost boundary | KV memory and throughput |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2512.04857v1#page=1) · [Formal publication record](https://doi.org/10.1007/978-3-032-37035-8_33)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lisa"></a>

## lisa

**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Visual AR speculative verification |
| Intervention | Locality-informed verifier modifies acceptance behavior |
| Original-source basis | Original source evaluates generation speed under a fixed drafter |
| Cost boundary | Speculative image inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 13; abstract/selected method and performance passages |

[Reading source](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf#page=13) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/3385)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="llamagen"></a>

## llamagen

**Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation**. arXiv preprint arXiv:2406.06525, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference causal AR image generator |
| Intervention | Llama-style next-token prediction |
| Original-source basis | Reference model with preprint publication status in the current record |
| Cost boundary | Preprint background, not admitted to formal-publication core |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2406.06525#page=1) · [Formal publication record](https://arxiv.org/abs/2406.06525)

Venue check: background only; no core venue admission inferred

<a name="lpd"></a>

## lpd

**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR position grouping and inference schedule |
| Intervention | Position query tokens and locality-aware parallel generation order |
| Original-source basis | Source reports image generation latency against parallel AR baselines |
| Cost boundary | New-generator latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 24; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2507.01957v2#page=24) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="lpips"></a>

## lpips

**The Unreasonable Effectiveness of Deep Features as a Perceptual Metric**. CVPR, 2018.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Paired perceptual evaluation |
| Intervention | Learned perceptual distance |
| Original-source basis | Evaluation resource |
| Cost boundary | Evaluation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html#page=1) · [Formal publication record](https://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="madformer"></a>

## madformer

**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR/diffusion hybrid block computation |
| Intervention | Allocates AR conditioning layers and iterative diffusion layers |
| Original-source basis | Controlled source experiments compare image quality under inference-compute budgets |
| Cost boundary | Inference compute, not automatically measured end-to-end speedup |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="magnets"></a>

## magnets

**Masked Generative Nested Transformers with Decode Time Scaling**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | MaskGIT-style image/video masked sampling |
| Intervention | Nested model sizes and cached unmasked states |
| Original-source basis | Efficiency experiments are present, but the evaluated object is masked non-AR generation |
| Cost boundary | Related non-AR inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goyal25a/goyal25a.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v267/goyal25a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="mar"></a>

## mar

**Autoregressive Image Generation without Vector Quantization**. NeurIPS, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference continuous masked AR generator |
| Intervention | Diffusion loss models continuous token conditionals |
| Original-source basis | Retained as the reference process accelerated by MAR-specific methods |
| Cost boundary | Reference generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2024/file/66e226469f20625aaebddbe47f0ca997-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/66e226469f20625aaebddbe47f0ca997-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="marche"></a>

## marche

**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR attention and feed-forward recomputation |
| Intervention | Cache-aware attention and selective KV refresh |
| Original-source basis | Source reports acceleration against original MAR |
| Cost boundary | MAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2506.12035#page=1) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/5698)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="markovvar"></a>

## markov_var

**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | VAR historical context and memory |
| Intervention | Compressed history state and limited scale context |
| Original-source basis | Source reports peak-memory reductions against full-context VAR |
| Cost boundary | Inference memory, not memory-to-speed equivalence |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="markovgen"></a>

## markovgen

**MarkovGen: Structured Prediction for Efficient Text-to-Image Generation**. CVPR, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Muse non-AR generation |
| Intervention | Markov random field reduces Muse sampling cost |
| Original-source basis | Original application is Muse, not an identified AR generator |
| Cost boundary | Related non-AR acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2024/papers/Jayasumana_MarkovGen_Structured_Prediction_for_Efficient_Text-to-Image_Generation_CVPR_2024_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2024/html/Jayasumana_MarkovGen_Structured_Prediction_for_Efficient_Text-to-Image_Generation_CVPR_2024_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="marval"></a>

## marval

**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | learned replacement of an AR process |
| Specific object | MAR iterative conditional sampling |
| Intervention | Distills a faster sampler while retaining a masked AR generation organization |
| Original-source basis | Source explicitly evaluates inference acceleration from MAR distillation |
| Cost boundary | Learned MAR sampling process |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="maskgit"></a>

## maskgit

**MaskGIT: Masked Generative Image Transformer**. CVPR, 2022.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference masked non-autoregressive generation |
| Intervention | Parallel iterative unmasking |
| Original-source basis | Related generation background, not labeled causal AR |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2022/papers/Chang_MaskGIT_Masked_Generative_Image_Transformer_CVPR_2022_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2022/html/Chang_MaskGIT_Masked_Generative_Image_Transformer_CVPR_2022_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="moss"></a>

## moss

**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**. AAAI, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | High-resolution next-scale transformer execution |
| Intervention | Mixes scale work and dispatches late refinement selectively |
| Original-source basis | Original source reports transformer-backbone speedup |
| Cost boundary | Backbone runtime, not automatically complete-image latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573#page=7) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/37611)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="mulosd"></a>

## mulo_sd

**Multi-Scale Local Speculative Decoding for Image Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | High-resolution AR image speculative generation |
| Intervention | Low-resolution proposals with upsampling and spatially local verification |
| Original-source basis | Source reports image-generation acceleration |
| Cost boundary | Speculative generation runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="muse"></a>

## muse

**Muse: Text-To-Image Generation via Masked Generative Transformers**. ICML, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference masked text-to-image generation |
| Intervention | Parallel masked token prediction |
| Original-source basis | Related non-AR generator |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v202/chang23b/chang23b.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v202/chang23b.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="mvar"></a>

## mvar

**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | VAR spatial and scale context |
| Intervention | Restricts conditioning to adjacent scales and local neighborhoods |
| Original-source basis | Source evaluates reduced model complexity and inference resource requirements |
| Cost boundary | Conditional computation and memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf#page=6) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nar"></a>

## nar

**Neighboring Autoregressive Modeling for Efficient Visual Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image; video |
| Study type | efficient generator / representation design |
| Specific object | Image and video AR position decoding |
| Intervention | Neighbor expansion with dimension-oriented parallel prediction heads |
| Original-source basis | Source reports image and UCF101 generation throughput |
| Cost boundary | Image and video results remain separate |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2503.10696#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nextstep"></a>

## nextstep

**NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference continuous-token text-to-image AR model |
| Intervention | Causal backbone with flow-matching head |
| Original-source basis | Inspected source emphasizes generation capability. It does not establish a dedicated inference-acceleration intervention here |
| Cost boundary | Reference hybrid generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2508.10711v1#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/974ff7b5bf08dbf9400b5d599a39c77f-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nova"></a>

## nova

**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale visual AR token processing |
| Intervention | Entropy-guided adaptive token reduction and cached residual reuse |
| Original-source basis | Source evaluates runtime of the token-reduction method |
| Cost boundary | VAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v306/zhang26dq.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="numericalpruning"></a>

## numerical_pruning

**Numerical Pruning for Efficient Autoregressive Models**. AAAI, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Decoder-only AR transformer parameters |
| Intervention | Numerical-score structured pruning |
| Original-source basis | Source explicitly evaluates both language and AR image generation; retain image results only |
| Cost boundary | Image-model compression and inference work |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/download/34249/36404#page=7) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/34249)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="pagedattention"></a>

## pagedattention

**Efficient Memory Management for Large Language Model Serving with PagedAttention**. SOSP, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | LLM serving memory |
| Intervention | Paged KV storage |
| Original-source basis | No visual-generation application verified in this paper |
| Cost boundary | Systems background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://doi.org/10.1145/3600006.3613165#page=1) · [Formal publication record](https://doi.org/10.1145/3600006.3613165)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="par"></a>

## par

**Parallelized Autoregressive Visual Generation**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image; video |
| Study type | efficient generator / representation design |
| Specific object | Image and video AR sequential decoding |
| Intervention | Generates spatially distant groups concurrently |
| Original-source basis | Source evaluates ImageNet and UCF101 speed and quality |
| Cost boundary | Image/video throughput, separately |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="pjd"></a>

## pjd

**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image Jacobi candidate refinement |
| Intervention | Spatial parallel drafts with adaptive attention masks |
| Original-source basis | Source reports image-generation runtime acceleration |
| Cost boundary | Jacobi decoding runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="prismmoe"></a>

## prism_moe

**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Dense visual AR predictor computation |
| Intervention | Dense-to-MoE conversion with sparse expert activation |
| Original-source basis | Source Table 3 reports wall-clock latency with a fused MoE backend |
| Cost boundary | Source-defined end-to-end inference latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/li26gy.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ptq4arvg"></a>

## ptq4arvg

**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR visual predictor arithmetic |
| Intervention | Post-training weight/activation quantization and calibration |
| Original-source basis | Source evaluates reduced numerical precision for visual-generation inference |
| Cost boundary | Quantized inference resources |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf#page=9) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="radar"></a>

## radar

**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR sparse attention plus decoded images |
| Intervention | Cost-constrained sparse prediction and decoder adaptation |
| Original-source basis | Original source compares image metrics and generation latency |
| Cost boundary | Accelerated predictor plus adapted decoder |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="randar"></a>

## randar

**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Random-order AR image inference |
| Intervention | Position instruction tokens enable parallel decoding |
| Original-source basis | Source evaluates image sampling efficiency of parallel inference |
| Cost boundary | New-generator inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="rar"></a>

## rar

**Randomized Autoregressive Visual Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image generator execution at a quality target |
| Intervention | Randomized-order training yields an AR generator evaluated with KV-cached serving |
| Original-source basis | Source Table 5 compares sampling throughput using optimized inference |
| Cost boundary | Efficient generator comparison, not a plug-in acceleration of fixed weights |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="recap"></a>

## recap

**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR context-feature recomputation |
| Intervention | Alternates full evaluations with low-cost cached-context steps |
| Original-source basis | Source explicitly tests MAR in addition to MaskGIT and MAGE |
| Cost boundary | Full/local evaluation timing, not interchangeable |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sar"></a>

## sar

**Autoregression with Self-Token Prediction**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Grouped AR image generation |
| Intervention | Self-token prediction generates flexible token groups per step |
| Original-source basis | Source reports inference efficiency and grouped-input comparisons |
| Cost boundary | Grouped generation runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 5; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf#page=5) · [Formal publication record](https://proceedings.mlr.press/v306/chen26du.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="scalekv"></a>

## scalekv

**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale VAR KV cache |
| Intervention | Layer-dependent retention of scales and cache entries |
| Original-source basis | Source reports KV-memory and inference efficiency comparisons |
| Cost boundary | KV memory and attention |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf#page=6) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="scd"></a>

## scd

**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image; video |
| Study type | execution optimization |
| Specific object | AR image stochastic speculative execution |
| Intervention | Couples proposal/verification randomness |
| Original-source basis | Source reports image and video inference gains; the two task results remain separate |
| Cost boundary | No new independent exactness certification |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2510.24211v2#page=1) · [Formal publication record](https://proceedings.mlr.press/v306/so26a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="shiftsum"></a>

## shift_sum

**Shift-and-Sum Quantization for Visual Autoregressive Models**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR quantized matrix computation |
| Intervention | Shift-and-sum value quantization with calibration resampling |
| Original-source basis | Appendix throughput table compares 8-bit variants and full precision on CPU |
| Cost boundary | CPU throughput, not a GPU speedup claim |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 17; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf#page=17) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sjd"></a>

## sjd

**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR text-to-image next-token execution |
| Intervention | Jacobi candidate reuse with stochastic verification |
| Original-source basis | Source reports visual AR inference-speed experiments |
| Cost boundary | Speculative runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf#page=8) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sjd2"></a>

## sjd2

**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR text-to-image Jacobi refinement |
| Intervention | Fine-tunes noisy embeddings for next-clean-token prediction |
| Original-source basis | Source reports accelerated image inference after low-cost fine-tuning |
| Cost boundary | Jacobi inference, preparation separate |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf#page=8) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sjdpac"></a>

## sjd_pac

**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image Jacobi candidate generation |
| Intervention | Proactive drafting and adaptive continuation |
| Original-source basis | Source reports inference throughput for the revised SJD procedure |
| Cost boundary | Speculative runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sjdplus"></a>

## sjd_plus

**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR text-to-image Jacobi candidate reuse |
| Intervention | Retains high-confidence unaccepted draft states |
| Original-source basis | Source reports image inference-latency reductions |
| Cost boundary | Speculative runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2512.07503v1#page=1) · [Formal publication record](https://doi.org/10.1109/TPAMI.2026.3700227)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sjdsv"></a>

## sjd_sv

**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image speculative verification |
| Intervention | Semantic subsequence verification changes the tested/committed positions |
| Original-source basis | Source reports generation acceleration |
| Cost boundary | Runtime relevance does not certify the full-prefix preservation theorem |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/zhang26fd.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="songjacobi"></a>

## song_jacobi

**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**. ICML, 2021.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Deep AR image-model feedforward sampling |
| Intervention | Parallel nonlinear fixed-point solving |
| Original-source basis | Source includes AR image-model experiments, not only general solver theory |
| Cost boundary | Historical 2021 methodological visual acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v139/song21a/song21a.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v139/song21a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sparsear"></a>

## sparsear

**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image KV attention |
| Intervention | Entropy-aware cache sparsification |
| Original-source basis | Source evaluates AR image generation and editing; retain generation results separately |
| Cost boundary | KV memory and attention runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v306/tong26k.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sparsevar"></a>

## sparsevar

**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Late-scale VAR spatial computation |
| Intervention | Frequency-guided token omission and recovery |
| Original-source basis | Source reports accelerated high-resolution VAR inference |
| Cost boundary | VAR runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 5; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2507.20454#page=5) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="sparvar"></a>

## sparvar

**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Next-scale VAR attention |
| Intervention | Predicts sparse attention patterns from earlier scales |
| Original-source basis | Source reports inference latency and image/task metrics |
| Cost boundary | Sparse attention and generation runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="spectr"></a>

## spectr

**SpecTr: Fast Speculative Decoding via Optimal Transport**. NeurIPS, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | General speculative sampling |
| Intervention | Optimal-transport verification/coupling |
| Original-source basis | Methodological background. No AR visual-generation application verified here |
| Cost boundary | Sampling background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://papers.nips.cc/paper_files/paper/2023/hash/6034a661584af6c28fd97a6f23e56c0a-Abstract-Conference.html#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6034a661584af6c28fd97a6f23e56c0a-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ssim"></a>

## ssim

**Image Quality Assessment: From Error Visibility to Structural Similarity**. IEEE Transactions on Image Processing, 2004.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Image reference similarity |
| Intervention | Structural similarity metric |
| Original-source basis | Evaluation resource |
| Cost boundary | Evaluation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://ece.uwaterloo.ca/~z70wang/publications/ssim.html#page=1) · [Formal publication record](https://ece.uwaterloo.ca/~z70wang/publications/ssim.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="stepvar"></a>

## stepvar

**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**. ACM ICMR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | High-resolution VAR token evaluation |
| Intervention | Structural and texture criteria select retained tokens |
| Original-source basis | Source evaluates inference speed of pruning |
| Cost boundary | VAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 10; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2603.01757#page=10) · [Formal publication record](https://doi.org/10.1145/3805622.3810814)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="surveyefficientdiffusiontmlr2025"></a>

## survey_efficient_diffusion_tmlr2025

**Efficient Diffusion Models: A Survey**. Transactions on Machine Learning Research, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Diffusion efficiency survey |
| Intervention | Related review |
| Original-source basis | Broader diffusion scope, not a direct acceleration method |
| Cost boundary | Related survey |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2502.06805v3#page=1) · [Formal publication record](https://openreview.net/forum?id=wHECkBOwyt)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="surveyefficientdiffusiontpami2025"></a>

## survey_efficient_diffusion_tpami2025

**Efficient Diffusion Models: A Comprehensive Survey From Principles to Practices**. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Diffusion efficiency survey |
| Intervention | Related review |
| Original-source basis | Broader diffusion scope, not a direct acceleration method |
| Cost boundary | Related survey |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2410.11795v2#page=1) · [Formal publication record](https://doi.org/10.1109/tpami.2025.3569700)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="surveymitigatingemnlp2025"></a>

## survey_mitigating_emnlp2025

**Mitigating Sequential Dependencies: A Survey of Algorithms and Systems for Generation-Refinement Frameworks in Autoregressive Models**. Findings of EMNLP, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Generation-refinement survey |
| Intervention | Related review |
| Original-source basis | Exact Findings track retained; no main-track CCF equivalence assumed |
| Cost boundary | Related survey |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://aclanthology.org/2025.findings-emnlp.716.pdf#page=1) · [Formal publication record](https://aclanthology.org/2025.findings-emnlp.716/)

Venue check: background only; no core venue admission inferred

<a name="surveyvisualartmlr2025"></a>

## survey_visual_ar_tmlr2025

**Autoregressive Models in Vision: A Survey**. Transactions on Machine Learning Research, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Visual AR survey |
| Intervention | Related review |
| Original-source basis | Includes efficiency discussion, not a primary accelerator study |
| Cost boundary | Related survey |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2411.05902v2#page=1) · [Formal publication record](https://openreview.net/forum?id=1BqXkjNEGP)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="t2icompbench"></a>

## t2icompbench

**T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation**. NeurIPS Datasets and Benchmarks, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Text-to-image compositional evaluation |
| Intervention | Task benchmark |
| Original-source basis | Evaluation resource |
| Cost boundary | Evaluation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2023/file/f8ad010cdd9143dbb0e9308c093aff24-Paper-Datasets_and_Benchmarks.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f8ad010cdd9143dbb0e9308c093aff24-Abstract-Datasets_and_Benchmarks.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="titok"></a>

## titok

**An Image is Worth 32 Tokens for Reconstruction and Generation**. NeurIPS, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Compact image tokenizer used with MaskGIT |
| Intervention | Short 1D visual codes |
| Original-source basis | Fig. 4 and Table 1 explicitly measure MaskGIT-ViT generation. Do not relabel those gains as AR inference results |
| Cost boundary | Non-AR evaluated generator in inspected experiments |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e91bf7dfba0477554994c6d64833e9d8-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="toprovar"></a>

## toprovar

**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR tokens, layers and scale computation |
| Intervention | Entropy-guided sparse execution |
| Original-source basis | Source reports acceleration on Infinity model configurations |
| Cost boundary | VAR inference runtime |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2602.22948#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="uniar"></a>

## uniar

**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Unified AR image-generation token decoding |
| Intervention | Channel-bitwise prediction reduces serial autoregressive steps |
| Original-source basis | Appendix Table 9 reports generation inference time, separate from training costs |
| Cost boundary | Image-generation latency in a unified model |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 15; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v306/peng26k.html#page=15) · [Formal publication record](https://proceedings.mlr.press/v306/peng26k.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="var"></a>

## var

**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**. NeurIPS, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image generation sequence organization |
| Intervention | Next-scale prediction replaces raster next-token progression |
| Original-source basis | Source compares inference speed against AR baselines |
| Cost boundary | Efficient generator design |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a24e284b187f662681440ba15c416fb-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="varcompressor"></a>

## var_compressor

**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**. ICPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | 8B bitwise AR image generation on edge GPUs |
| Intervention | Compresses inference memory for deployment |
| Original-source basis | Source reports edge-GPU memory/latency trade-offs |
| Cost boundary | Memory reduction and runtime must be reported separately |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 11; abstract/selected method and performance passages |

[Reading source](https://doi.org/10.1007/978-3-032-31920-3_1#page=11) · [Formal publication record](https://doi.org/10.1007/978-3-032-31920-3_1)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="variant"></a>

## variant

**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | VAR inference depth and memory |
| Intervention | Progressive supernet training permits scale-dependent subnet execution |
| Original-source basis | Source evaluates reduced inference resource requirements |
| Cost boundary | Learned depth adaptation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 5; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2511.16546#page=5) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="viar"></a>

## viar

**Visual Implicit Autoregressive Modeling**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Next-scale visual AR stack |
| Intervention | Implicit equilibrium layer with variable inference iterations |
| Original-source basis | Source reports GPU-memory savings and per-scale inference compute control |
| Cost boundary | Memory and compute, not training-memory-only evidence |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf#page=6) · [Formal publication record](https://proceedings.mlr.press/v306/jiang26ah.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="vqgan"></a>

## vqgan

**Taming Transformers for High-Resolution Image Synthesis**. CVPR, 2021.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Latent AR reference generator |
| Intervention | VQ tokenization with adversarial/perceptual reconstruction |
| Original-source basis | Reference architecture, not admitted merely because it enables generation |
| Cost boundary | Foundation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2021/papers/Esser_Taming_Transformers_for_High-Resolution_Image_Synthesis_CVPR_2021_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2021/html/Esser_Taming_Transformers_for_High-Resolution_Image_Synthesis_CVPR_2021_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="vvs"></a>

## vvs

**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR visual speculative verification |
| Intervention | Skips verification for selected provisional positions |
| Original-source basis | Source evaluates image generation speed |
| Cost boundary | Skipped verification does not automatically preserve the original sampler |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="xar"></a>

## xar

**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | AR image prediction units and conditional sampling |
| Intervention | Next-X prediction over flexible entities |
| Original-source basis | Source reports image inference efficiency and controlled generation configurations |
| Cost boundary | New-generator inference |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 2; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=2) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="xyzflow"></a>

## xyzflow

**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | MAR conditional-head sampling and AR teachers |
| Intervention | Shortcut flow modeling with multidimensional prediction |
| Original-source basis | Source explicitly evaluates autoregressive teachers and Next Shortcut Prediction |
| Cost boundary | Conditional-head budget, separate from generic flow-only experiments |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v306/liu26ck.html#page=6) · [Formal publication record](https://proceedings.mlr.press/v306/liu26ck.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="zipar"></a>

## zipar

**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Causal visual AR decoding |
| Intervention | Spatially parallel decoding with local context windows |
| Original-source basis | Source reports model-forward and generation-runtime experiments |
| Cost boundary | Forward counts and runtime are distinct |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v267/he25b.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ciar"></a>

## ciar

**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Cloud-device AR image decoding |
| Intervention | On-device interval verification reduces cloud verification calls |
| Original-source basis | Official source reports decoding speed and cloud-request reductions |
| Cost boundary | Cloud-device runtime and communication requests |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2603.25463v1#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e7e506bc5a94768243083216fe51d98b-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="hart"></a>

## hart

**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | High-resolution AR image generator |
| Intervention | Discrete AR structure with a small residual diffusion module |
| Original-source basis | Original source reports throughput and MACs for the hybrid design |
| Cost boundary | New-generator throughput and arithmetic work |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfalitr"></a>

## ccf_alitr

**Adaptive Length Image Tokenization via Recurrent Allocation**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Adaptive image tokenizer |
| Intervention | Recurrent allocation changes visual representation length |
| Original-source basis | Inspected source validates tokenization and reconstruction. AR inference-cost evidence is not established here |
| Cost boundary | Tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/534ec8dfc0312d96e1c1b357304fadc2-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/534ec8dfc0312d96e1c1b357304fadc2-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfbridgetokens"></a>

## ccf_bridge_tokens

**Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Continuous/discrete AR token representation |
| Intervention | Post-training dimension-wise quantization with a lightweight predictor |
| Original-source basis | Inspected source establishes representation and generation quality. No inference-cost comparison was located |
| Cost boundary | Generator/tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Bridging_Continuous_and_Discrete_Tokens_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Bridging_Continuous_and_Discrete_Tokens_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfcat"></a>

## ccf_cat

**CAT: Content-Adaptive Image Tokenization**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Content-adaptive tokenizer |
| Intervention | Assigns fewer visual codes to simpler images |
| Original-source basis | Reported throughput gain in the abstract is explicitly training throughput |
| Cost boundary | Training-only result is not inference acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/014898b821e3ce966ae1db68cb8d9966-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/014898b821e3ce966ae1db68cb8d9966-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfdnd"></a>

## ccf_dnd

**A Spark of Vision-Language Intelligence: 2-Dimensional Autoregressive Transformer for Efficient Finegrained Image Generation**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Two-dimensional depth/sequence AR modeling |
| Intervention | Predicts multiple codes along model depth |
| Original-source basis | Source emphasizes image quality at equal backbone size and sequence length. Inference-cost savings not established |
| Cost boundary | General AR model |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 2; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf#page=2) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/674ad201bc8fa74b3c9979230aa0c63b-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dqvae"></a>

## dqvae

**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**. CVPR, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image code length and decoding |
| Intervention | Dynamic quantization plus coarse-to-fine position/content prediction |
| Original-source basis | Original Fig. 6 compares generation speed against ViT-VQGAN on RTX-3090 |
| Cost boundary | Measured AR sampling speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfdtp"></a>

## ccf_dtp

**Denoising Token Prediction in Masked Autoregressive Models**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Continuous MAR token prediction |
| Intervention | Adds denoising refinement of unmasked predictions |
| Original-source basis | Source Fig. 4 compares inference time against image quality |
| Cost boundary | Efficient MAR generator variant |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfgpstoken"></a>

## ccf_gpstoken

**GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization for Image Representation and Generation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Spatially adaptive image tokenization |
| Intervention | Gaussian-parameterized region tokens |
| Original-source basis | Inspected source focuses representation/reconstruction and generative quality. AR inference-cost savings not established |
| Cost boundary | Tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/10831838f1cdd8fcba90188e88e7a121-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/10831838f1cdd8fcba90188e88e7a121-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="imagefolder"></a>

## imagefolder

**ImageFolder: Autoregressive Image Generation with Folded Tokens**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image token prediction |
| Intervention | Folds spatially aligned product-quantized tokens for shared prediction |
| Original-source basis | Mechanism and AR use confirmed. A separate measured inference-cost comparison is still required |
| Cost boundary | Fewer steps alone are insufficient |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |
| Unresolved item | Mechanism and AR use confirmed. A separate measured inference-cost comparison is still required |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/82519a9d318f39096ea507615c61c340-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/82519a9d318f39096ea507615c61c340-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfmage"></a>

## ccf_mage

**MAGE: MAsked Generative Encoder To Unify Representation Learning and Image Synthesis**. CVPR, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked image representation and synthesis |
| Intervention | Joint masked representation learning and generation |
| Original-source basis | Related non-AR masked generator |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_MAGE_MAsked_Generative_Encoder_To_Unify_Representation_Learning_and_Image_CVPR_2023_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2023/html/Li_MAGE_MAsked_Generative_Encoder_To_Unify_Representation_Learning_and_Image_CVPR_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfmagvlt"></a>

## ccf_magvlt

**MAGVLT: Masked Generative Vision-and-Language Transformer**. CVPR, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked vision-language synthesis |
| Intervention | Joint masked multimodal token modeling |
| Original-source basis | Related masked generation, no AR acceleration experiment established |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2023/papers/Kim_MAGVLT_Masked_Generative_Vision-and-Language_Transformer_CVPR_2023_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2023/html/Kim_MAGVLT_Masked_Generative_Vision-and-Language_Transformer_CVPR_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfmask1d"></a>

## ccf_mask1d

**Democratizing Text-to-Image Masked Generative Models with Compact Text-Aware One-Dimensional Tokens**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked text-to-image generator |
| Intervention | Compact text-aware 1D tokens |
| Original-source basis | Inspected experiments concern masked generation, not an identified AR generator |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_Democratizing_Text-to-Image_Masked_Generative_Models_with_Compact_Text-Aware_One-Dimensional_Tokens_ICCV_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_Democratizing_Text-to-Image_Masked_Generative_Models_with_Compact_Text-Aware_One-Dimensional_Tokens_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfmeissonic"></a>

## ccf_meissonic

**Meissonic: Revitalizing Masked Generative Transformers for Efficient High-Resolution Text-to-Image Synthesis**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked high-resolution text-to-image generation |
| Intervention | Masked generative transformer design |
| Original-source basis | Related non-AR masked generation |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7fd4aa7246ccfe46e61b52884bf1d11-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b7fd4aa7246ccfe46e61b52884bf1d11-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="mqvae"></a>

## mqvae

**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**. CVPR, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image sequence redundancy |
| Intervention | Masks less-important regions and predicts selected/content positions with Stackformer |
| Original-source basis | Source reports faster generation and compares sampling efficiency |
| Cost boundary | AR sampling speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nfig"></a>

## nfig

**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Next-scale AR frequency stages |
| Intervention | Generates low-frequency structure before higher-frequency detail |
| Original-source basis | Source explicitly compares inference speed against VAR-d20 |
| Cost boundary | New-generator inference speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfpredictionrefinement"></a>

## ccf_prediction_refinement

**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Causal AR image prediction unit |
| Intervention | Predicts overlapping tensors to refine previous discrete outputs |
| Original-source basis | Source contains quality/latency comparisons for TensorAR |
| Cost boundary | New-generator inference latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf#page=6) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfsemantic1d"></a>

## ccf_semantic1d

**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR prior over 1D image tokens |
| Intervention | Jointly learns semantic 1D representation and AR generation |
| Original-source basis | Appendix reports sampling throughput and FLOPs on H100 |
| Cost boundary | New-generator image throughput |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 13; abstract/selected method and performance passages |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf#page=13) · [Formal publication record](https://proceedings.mlr.press/v306/chu26b.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="spectralar"></a>

## spectralar

**SpectralAR: Spectral Autoregressive Visual Generation**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR spectral image-token generation |
| Intervention | Orders tokens by increasing spectral detail |
| Original-source basis | Original performance table reports measured own-method wall time with rescaled comparator times |
| Cost boundary | Own timing measured, comparator scaling is not a controlled speed comparison |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccftcts"></a>

## ccf_tcts

**Text-Conditioned Sampling Framework for Text-to-Image Generation with Masked Generative Models**. ICCV, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked text-conditioned image sampling |
| Intervention | Revised masked-model sampling |
| Original-source basis | No direct AR-generation application established |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2023/papers/Lee_Text-Conditioned_Sampling_Framework_for_Text-to-Image_Generation_with_Masked_Generative_Models_ICCV_2023_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2023/html/Lee_Text-Conditioned_Sampling_Framework_for_Text-to-Image_Generation_with_Masked_Generative_Models_ICCV_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfunicompress"></a>

## ccf_unicompress

**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Unified-model AR image output sequences |
| Intervention | Token compression/decompression shortens visual generation |
| Original-source basis | Original Table 3 separately reports generation inference minutes and understanding inference minutes |
| Cost boundary | Generation timing only, not visual-understanding timing |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ccfvibetoken"></a>

## ccf_vibetoken

**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Resolution-flexible AR image prior |
| Intervention | Resolution-agnostic 1D tokenization bounds AR sequence burden |
| Original-source basis | Source reports generation inference FLOPs across resolutions |
| Cost boundary | Reported AR inference FLOPs, not an invented latency speedup |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="stat"></a>

## stat

**Soft Tail-Dropping for Adaptive Visual Tokenization**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Adaptive-length AR image tokens |
| Intervention | Soft tail dropping predicts how many visual tokens to retain |
| Original-source basis | Inspected Tables 1–2 compare token count and quality. AR runtime/FLOPs savings not established |
| Cost boundary | Token count only in inspected results |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |
| Unresolved item | Inspected Tables 1–2 compare token count and quality. AR runtime/FLOPs savings not established |

[Reading source](https://arxiv.org/pdf/2601.14246#page=7) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37553-7_24)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="vfmtok"></a>

## vfmtok

**Vision Foundation Models as Effective Visual Tokenizers for Autoregressive Generation**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Visual tokenizer and generation training |
| Intervention | Vision-foundation-model features regularize tokens |
| Original-source basis | Inspected efficiency statement concerns convergence/training, not verified inference cost |
| Cost boundary | Training/tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a829e299ebc1c1615ddb09e98fb6ce8-Abstract-Conference.html#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a829e299ebc1c1615ddb09e98fb6ce8-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="spectraltokenizer"></a>

## spectral_tokenizer

**Spectral Image Tokenizer**. ICCV, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Image tokenizer |
| Intervention | Spectral representation design |
| Original-source basis | Inspected source establishes tokenization and quality, not a verified AR-inference acceleration result |
| Cost boundary | Tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2025/html/Esteves_Spectral_Image_Tokenizer_ICCV_2025_paper.html#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2025/html/Esteves_Spectral_Image_Tokenizer_ICCV_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="rqtransformer"></a>

## rqtransformer

**Autoregressive Image Generation Using Residual Quantization**. CVPR, 2022.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR image spatial sequence and depth code prediction |
| Intervention | Residual quantization compresses spatial maps and predicts code stacks |
| Original-source basis | Original Fig. 4 compares sampling speed by map shape and batch size |
| Cost boundary | Measured AR sampling speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="magvitv2"></a>

## magvitv2

**Language Model Beats Diffusion: Tokenizer is Key to Visual Generation**. ICLR, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Visual tokenizer and generative-model representation |
| Intervention | Lookup-free quantization improves discrete visual tokens |
| Original-source basis | No specific AR inference-cost reduction verified in the inspected source |
| Cost boundary | Tokenizer/reference-model background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openreview.net/forum?id=gzqrANCF4g#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/036912a83bdbb1fd792baf6532f102d8-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="pixelrnn"></a>

## pixelrnn

**Pixel Recurrent Neural Networks**. ICML, 2016.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Historical pixel AR image model |
| Intervention | Recurrent pixel conditionals |
| Original-source basis | Reference architecture, not an acceleration study |
| Cost boundary | Foundation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v48/oord16.html#page=1) · [Formal publication record](https://proceedings.mlr.press/v48/oord16.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="imagegpt"></a>

## imagegpt

**Generative Pretraining From Pixels**. ICML, 2020.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Pixel-level generative pretraining |
| Intervention | AR image pretraining for representation learning |
| Original-source basis | Representation-learning objective, not visual-generation inference acceleration |
| Cost boundary | Foundation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v119/chen20s.html#page=1) · [Formal publication record](https://proceedings.mlr.press/v119/chen20s.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="efficientvqgan"></a>

## efficient_vqgan

**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**. ICCV, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | High-resolution AR image attention and local code generation |
| Intervention | Local tokenization with blockwise parallel generation |
| Original-source basis | Source compares generated-image throughput for high-resolution synthesis |
| Cost boundary | AR image sampling throughput |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="core2reviewcandidate"></a>

## core2_review_candidate

**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | LlamaGen guidance computation |
| Intervention | Weak-model training supports guidance and later replacement of expensive computation |
| Original-source basis | Primary source explicitly includes LlamaGen experiments alongside diffusion models |
| Cost boundary | Retain AR application, do not transfer diffusion-only speedups |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 16; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2503.09662v1#page=16) · [Formal publication record](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings10"></a>

## proceedings_10

**SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Continuous visual tokenizer used with diffusion/SiT |
| Intervention | Soft vector quantization |
| Original-source basis | Inspected source efficiency results do not establish AR-generator acceleration |
| Cost boundary | Diffusion/tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_SoftVQ-VAE_Efficient_1-Dimensional_Continuous_Tokenizer_CVPR_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SoftVQ-VAE_Efficient_1-Dimensional_Continuous_Tokenizer_CVPR_2025_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings43"></a>

## proceedings_43

**Progress by Pieces: Test-Time Scaling for Autoregressive Image Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image test-time search budget |
| Intervention | Adaptive sample/search allocation |
| Original-source basis | Search scaling is relevant context. Fixed quality/budget AR inference savings have not been checked here |
| Cost boundary | Search-budget background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Park_Progress_by_Pieces_Test-Time_Scaling_for_Autoregressive_Image_Generation_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Progress_by_Pieces_Test-Time_Scaling_for_Autoregressive_Image_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings111"></a>

## proceedings_111

**StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | layout-conditioned AR generator background |
| Specific object | Layout-conditioned MAR image generation, not an AR inference accelerator |
| Intervention | 2D positional embeddings, layout attention bias and policy refinement improve layout alignment |
| Original-source basis | Table 5 reports Plain MAR at 3.56 seconds and StructMAR at 3.85 seconds. The headline 4.05x result compares StructMAR with diffusion-based MIGC, not an accelerated MAR baseline |
| Cost boundary | Complete image generation comparison between different generator families. The proposed changes do not reduce the reported MAR baseline time |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8, Tables 3 and 5 and Section 4.4 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/cao26ab/cao26ab.pdf#page=8) · [Formal publication record](https://proceedings.mlr.press/v306/cao26ab.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings112"></a>

## proceedings_112

**ScalingAR: Scaling Confidence for Autoregressive Image Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR image test-time search |
| Intervention | Entropy-based trajectory pruning and guidance scheduling |
| Original-source basis | Official abstract reports visual-token consumption. It does not by itself establish wall-clock savings |
| Cost boundary | Search-token budget |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Primary publication record / abstract where available |

[Reading source](https://proceedings.mlr.press/v306/chen26fc.html) · [Formal publication record](https://proceedings.mlr.press/v306/chen26fc.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings170"></a>

## proceedings_170

**JetFormer: An autoregressive generative model of raw images and text**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Joint raw-image/text AR generator |
| Intervention | Joint normalizing-flow representation with an AR transformer |
| Original-source basis | General multimodal generation model, not a verified inference-cost reduction in inspected material |
| Cost boundary | Reference generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5a8e37f38a08c68162452dcba89ae9c-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d5a8e37f38a08c68162452dcba89ae9c-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings173"></a>

## proceedings_173

**Denoising Autoregressive Transformers for Scalable Text-to-Image Generation**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Hybrid denoising AR image generator |
| Intervention | Non-Markovian denoising trajectories |
| Original-source basis | Inspected source proposes a generation framework. An explicit AR inference-cost reduction is not established |
| Cost boundary | Reference hybrid generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd8a977883fd8d5bccf9575e873ce75-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ebd8a977883fd8d5bccf9575e873ce75-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings177"></a>

## proceedings_177

**Fluid: Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Continuous-token AR text-to-image generator |
| Intervention | Random-order continuous-token generation |
| Original-source basis | Source studies model scaling and generation quality, not an identified acceleration intervention |
| Cost boundary | Reference generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8e7248f3e659cfe70c6debcdae1b023-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f8e7248f3e659cfe70c6debcdae1b023-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings180"></a>

## proceedings_180

**WeTok: Powerful Discrete Tokenization for High-Fidelity Visual Reconstruction**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Visual tokenizer |
| Intervention | Group-wise lookup-free quantization and generative decoder |
| Original-source basis | Reconstruction/tokenizer improvements do not establish AR inference savings |
| Cost boundary | Tokenizer background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/0b2a58f2b5943b9c356f10db32073275-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0b2a58f2b5943b9c356f10db32073275-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="proceedings215"></a>

## proceedings_215

**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR generation with aligned compact visual tokens |
| Intervention | Causal decoder constrains tokenizer dependencies |
| Original-source basis | Original source reports faster AR sampling as well as quality |
| Cost boundary | Efficient generator design |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7; abstract/selected method and performance passages |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nadejmlr"></a>

## nade_jmlr

**Neural Autoregressive Distribution Estimation**. Journal of Machine Learning Research, 2016.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Autoregressive density estimation |
| Intervention | General neural density models |
| Original-source basis | Historical foundation, not a visual-generation accelerator |
| Cost boundary | Foundation |
| Reading extent | official abstract / selected original-source text |
| Source location | Official JMLR article record and abstract |

[Reading source](https://jmlr.org/papers/v17/16-272.html) · [Formal publication record](https://jmlr.org/papers/v17/16-272.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="normalizingflowsjmlr"></a>

## normalizing_flows_jmlr

**Normalizing Flows for Probabilistic Modeling and Inference**. Journal of Machine Learning Research, 2021.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | supporting reference |
| Study type | not admitted to core |
| Specific object | Normalizing-flow review |
| Intervention | Density modeling reference |
| Original-source basis | Related theoretical background, not a direct accelerator study |
| Cost boundary | Related survey |
| Reading extent | official abstract / selected original-source text |
| Source location | Official JMLR article record and abstract |

[Reading source](https://jmlr.org/papers/v22/19-1028.html) · [Formal publication record](https://jmlr.org/papers/v22/19-1028.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="tmlrwknwpz0g3g"></a>

## tmlr_wkNwPZ0g3G

**Efficient High-Resolution Image Synthesis via Autoregressive Modeling in a Diffusion-Learned Continuous Latent Space**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed high-resolution continuous-latent AR generator |
| Intervention | Not inferred from the title |
| Original-source basis | Formal TMLR identity is established. Primary mechanism/cost passages remain inaccessible |
| Cost boundary | Full-text/abstract mechanism unresolved |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Official TMLR accepted-paper record and BibTeX only |
| Unresolved item | Formal TMLR identity is established. Primary mechanism/cost passages remain inaccessible |

[Reading source](https://openreview.net/forum?id=wkNwPZ0g3G) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrcefd15ouq1"></a>

## tmlr_cEfd15ouQ1

**Autoregressive Image Generation with Frequency Progression**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Frequency-progressive continuous AR image generation |
| Intervention | Frequency-aware conditional diffusion budgets |
| Original-source basis | AR mechanism confirmed. Inspected version reports stages and quality, without a verified timing/FLOPs comparison |
| Cost boundary | Sampling stages alone are insufficient |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 2; abstract/selected method and performance passages |
| Unresolved item | AR mechanism confirmed. Inspected version reports stages and quality, without a verified timing/FLOPs comparison |

[Reading source](https://arxiv.org/pdf/2503.05305#page=2) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrwkctcxo1a9"></a>

## tmlr_wkCTCXo1a9

**Progressive Checkerboards for Autoregressive Multiscale Image Generation**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | Multiscale AR serial sampling schedule |
| Intervention | Progressive checkerboards permit parallel positions within scales |
| Original-source basis | Original source reports single-image A100 inference time against other AR models |
| Cost boundary | New-generator inference time |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2602.03811#page=6) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrxyatz9hpe7"></a>

## tmlr_xYATz9HpE7

**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | execution optimization |
| Specific object | Image generation by autoregressive normalizing flows |
| Intervention | Selective Jacobi iterations parallelize sequential flow inversions |
| Original-source basis | Source evaluates image-model inference speed |
| Cost boundary | AR normalizing-flow inference, not token-level speculative decoding |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2505.24791#page=9) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrib8pzxdpmf"></a>

## tmlr_iB8PzxdpMf

**InfoScale: Unleashing Training-free Variable-scaled Image Generation via Effective Utilization of Information**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Diffusion/SDXL variable-resolution generation |
| Intervention | Training-free variable-scale diffusion synthesis |
| Original-source basis | Primary source identifies diffusion application, not AR generation |
| Cost boundary | Outside AR core |
| Reading extent | selected original full-text passages checked in prior scope pass; no fresh full-proof check |
| Source location | Author full-text reading recorded in the preceding 69-entry scope review; diffusion/SDXL application |

[Reading source](https://openreview.net/forum?id=iB8PzxdpMf) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlroufnxesoco"></a>

## tmlr_OuFNXESoCO

**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image; video |
| Study type | efficient generator / representation design |
| Specific object | Image and video block-AR conditional diffusion |
| Intervention | Block-causal denoising with reusable past context |
| Original-source basis | Source Fig. 5 compares sampling time for different AR lengths |
| Cost boundary | Image/video sampling-time boundaries remain distinct |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 10; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2412.07720#page=10) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrnye2jun3v3"></a>

## tmlr_NYe2JuN3v3

**MaskBit: Embedding-free Image Generation via Bit Tokens**. TMLR, 2024.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Masked image generator |
| Intervention | Bit-token masked generation |
| Original-source basis | Related non-AR generator |
| Cost boundary | Non-AR background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2409.16211#page=1) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="tmlrafdcyjkhnd"></a>

## tmlr_AFDcYJKhND

**Scaling Autoregressive Models for Content-Rich Text-to-Image Generation**. TMLR, 2022.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Parti reference text-to-image AR model |
| Intervention | Scaled autoregressive image modeling |
| Original-source basis | General AR generator, not admitted simply for model capability |
| Cost boundary | Reference generator |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2206.10789#page=1) · [Formal publication record](https://jmlr.org/tmlr/papers/)

Venue check: TMLR author-approved exception, not asserted to be CCF-listed

<a name="neuripsextra77"></a>

## neurips_extra_77

**When Worse is Better: Navigating the Compression Generation Trade-off In Visual Tokenization**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Tokenizer/prior training compute |
| Intervention | Causally regularized tokenization |
| Original-source basis | The inspected compute-efficiency comparison concerns training compute scaling |
| Cost boundary | Training efficiency is not inference speed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/b6425ecad28e4960cb4a622beb338ffe-Paper-Conference.pdf#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b6425ecad28e4960cb4a622beb338ffe-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="neuripsextra94"></a>

## neurips_extra_94

**Single-pass Adaptive Image Tokenization for Minimum Program Search**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Adaptive image encoding |
| Intervention | Single-pass tokenizer predicts code length |
| Original-source basis | Tokenizer encoding efficiency does not establish downstream AR-generation inference savings |
| Cost boundary | Representation/encoding background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2507.07995#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dc35c593e61f6df62db541b976d09dcf-Abstract-Conference.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="ssdd"></a>

## ssdd

**SSDD: Single-Step Diffusion Decoder for Efficient Image Tokenization**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Single-step diffusion image decoder |
| Intervention | Distills image reconstruction |
| Original-source basis | Inspected application uses diffusion generators. No AR application established |
| Cost boundary | Diffusion-decoder background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2510.04961#page=1) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37556-8_19)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="star"></a>

## star

**Spanning Tree Autoregressive Visual Generation**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | AR traversal order and generation quality |
| Intervention | Spanning-tree order randomization |
| Original-source basis | Inspected source focuses generation/inpainting behavior, without verified inference-cost reduction |
| Cost boundary | AR modeling background |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://arxiv.org/pdf/2511.17089#page=1) · [Formal publication record](https://eccv.ecva.net/virtual/2026/poster/4249)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="dynamicvar"></a>

## dynamicvar

**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**. ICIC, 2027.

| Field | Paper-specific finding |
|---|---|
| Publication note | Online 2026, proceedings imprint 2027. |
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | High-resolution AR token-path computation |
| Intervention | Routes samples among discrete/hybrid/continuous representation paths |
| Original-source basis | Publisher abstract explicitly reports inference throughput against AR and diffusion generators |
| Cost boundary | Abstract-supported throughput, hardware/timing boundary not checked |
| Reading extent | official abstract / selected original-source text |
| Source location | Publisher abstract, inference-throughput statement |

[Reading source](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="localaricpr"></a>

## local_ar_icpr

**Local Autoregression with Finite-Support Random Variables for Image Generation**. ICPR, 2027.

| Field | Paper-specific finding |
|---|---|
| Publication note | Online 2026, proceedings imprint 2027. |
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Local image probability model |
| Intervention | Finite-support variables with controlled local dependence |
| Original-source basis | General generation method. Original abstract does not establish an inference-acceleration experiment |
| Cost boundary | Image modeling background |
| Reading extent | official abstract / selected original-source text |
| Source location | Publisher abstract, finite-support local generation model |

[Reading source](https://link.springer.com/chapter/10.1007/978-3-032-31654-7_12) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-31654-7_12)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="retrievalspecicassp"></a>

## retrieval_spec_icassp

**Breaking Codebook Redundancy for Faster Autoregressive Image Generation with Retrieval-Augmented Speculative Decoding**. ICASSP, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed retrieval-augmented AR image speculation |
| Intervention | Not inferred from the title |
| Original-source basis | Official ICASSP identity is established. Algorithm and cost-bearing result not yet retrieved |
| Cost boundary | Mechanism and inference evidence unresolved |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Official ICASSP program entry only |
| Unresolved item | Official ICASSP identity is established. Algorithm and cost-bearing result not yet retrieved |

[Reading source](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=16377) · [Formal publication record](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=16377&bare=1)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="uncertaintyquanticassp"></a>

## uncertainty_quant_icassp

**Enhancing Quantization for Visual Autoregressive Generation Via Uncertainty Identification**. ICASSP, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed visual AR quantization |
| Intervention | Not inferred whether numerical or representation quantization |
| Original-source basis | Official ICASSP identity is established. Quantization type and inference evidence remain unresolved |
| Cost boundary | Mechanism and inference evidence unresolved |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Official ICASSP program entry only |
| Unresolved item | Official ICASSP identity is established. Quantization type and inference evidence remain unresolved |

[Reading source](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=1960) · [Formal publication record](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=1960&bare=1)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="varturbo"></a>

## var_turbo

**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**. HPCA, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | software/hardware co-design |
| Specific object | VAR execution and dedicated accelerator |
| Intervention | Parallel decoding, token aggregation and bypass with hardware support |
| Original-source basis | Official HPCA main-track abstract reports software work reduction and accelerator measurements |
| Cost boundary | Hardware co-design, not a like-for-like GPU software speedup |
| Reading extent | official abstract / selected original-source text |
| Source location | Official HPCA 2026 main-conference abstract, software/hardware co-design and result paragraphs |

[Reading source](https://2026.hpca-conf.org/details/hpca-2026-main-conference/53/VAR-Turbo-Unlocking-the-Potential-of-Visual-Autoregressive-Models-through-Dual-Redun) · [Formal publication record](https://2026.hpca-conf.org/details/hpca-2026-main-conference/53/VAR-Turbo-Unlocking-the-Potential-of-Visual-Autoregressive-Models-through-Dual-Redun)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="tmxvar"></a>

## tmxvar

**TMXVAR: Twin Microscaling Floating-Point Quantization for Efficient Visual Autoregressive Model Inference on FPGA**. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed VAR FPGA numerical inference |
| Intervention | Twin microscaling floating-point quantization, title-level only |
| Original-source basis | Journal identity confirmed. Original technical result has not been retrieved |
| Cost boundary | Title is insufficient for core admission |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Publisher DOI identity and author publication record only |
| Unresolved item | Journal identity confirmed. Original technical result has not been retrieved |

[Reading source](https://doi.org/10.1109/tcad.2026.3734745) · [Formal publication record](https://doi.org/10.1109/tcad.2026.3734745)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="issccvaraccelerator"></a>

## isscc_var_accelerator

**A 28nm 47.3TFLOPs/W 894mJ/Inference Visual Autoregressive Accelerator with Differential-Amplifier Speculation and Chain-Reaction-Like Parallel Generation**. ISSCC, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed visual AR hardware inference |
| Intervention | Title-level speculation/parallel hardware |
| Original-source basis | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |
| Cost boundary | Venue and mechanism-result checks unresolved |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Official ISSCC advance-program record and DOI metadata only |
| Unresolved item | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |

[Reading source](https://doi.org/10.1109/isscc49663.2026.11409075) · [Formal publication record](https://doi.org/10.1109/isscc49663.2026.11409075)

Venue check: publication confirmed; requested CCF venue/track eligibility unresolved

<a name="varsa"></a>

## varsa

**31.4 VARSA: A Visual Autoregressive Generation Accelerator Using Performance-Scalable Multi-Precision PE-LUT and Grid-Similarity Attention Compression**. ISSCC, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Claimed visual AR hardware inference |
| Intervention | Title-level multi-precision and attention compression |
| Original-source basis | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |
| Cost boundary | Venue and mechanism-result checks unresolved |
| Reading extent | publication metadata; mechanism/result not independently established |
| Source location | Official ISSCC advance-program record and DOI metadata only |
| Unresolved item | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |

[Reading source](https://doi.org/10.1109/isscc49663.2026.11409066) · [Formal publication record](https://doi.org/10.1109/isscc49663.2026.11409066)

Venue check: publication confirmed; requested CCF venue/track eligibility unresolved

<a name="luminamgptijcv"></a>

## lumina_mgpt_ijcv

**Lumina-mGPT: Flexible Photorealistic Autoregressive Text-to-Image Generation**. IJCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Reference high-resolution AR text-to-image generator |
| Intervention | Flexible-resolution image generation |
| Original-source basis | General generator. Dedicated inference-acceleration intervention not established in inspected source |
| Cost boundary | Reference generator |
| Reading extent | official abstract / selected original-source text |
| Source location | Publisher abstract, flexible AR image generation |

[Reading source](https://doi.org/10.1007/s11263-026-02795-2) · [Formal publication record](https://doi.org/10.1007/s11263-026-02795-2)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="scalarplus"></a>

## scalar_plus

**SCALAR++: Efficient Controllable Generation via Scale-wise Visual Autoregressive Learning**. IJCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Control-conditioned VAR adapter overhead |
| Intervention | Layer-shared conditioning with lightweight modulation |
| Original-source basis | Publisher abstract claims parameter and memory savings. Inference versus training-memory boundary needs confirmation |
| Cost boundary | Memory boundary unresolved |
| Reading extent | official abstract / selected original-source text |
| Source location | Publisher abstract, layer-sharing and memory-overhead statements |
| Unresolved item | Publisher abstract claims parameter and memory savings. Inference versus training-memory boundary needs confirmation |

[Reading source](https://doi.org/10.1007/s11263-026-02984-z) · [Formal publication record](https://doi.org/10.1007/s11263-026-02984-z)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="nativetok"></a>

## nativetok

**Nativetok: Native Visual Tokenization for Improved Image Generation**. ICASSP, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Native image tokenization and training |
| Intervention | Causal meta-image modeling with hierarchical training |
| Original-source basis | Original abstract supports representation/training improvements, not an established inference-cost result |
| Cost boundary | Training/tokenizer background |
| Reading extent | official abstract / selected original-source text |
| Source location | Author abstract, native tokenization and hierarchical training |

[Reading source](https://doi.org/10.1109/icassp55912.2026.11462037) · [Formal publication record](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=11907&bare=1)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="parallelmultiscale2017"></a>

## parallel_multiscale_2017

**Parallel Multiscale Autoregressive Density Estimation**. ICML, 2017.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image; video |
| Study type | efficient generator / representation design |
| Specific object | Pixel AR sampling dependency depth |
| Intervention | Parallel multiscale density factorization |
| Original-source basis | Original source explicitly analyzes faster parallel image sampling |
| Cost boundary | Table 4 separates ImageNet image sampling and robot-video frame sampling with different batch settings |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf#page=8) · [Formal publication record](https://proceedings.mlr.press/v70/reed17a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="imagetransformer"></a>

## image_transformer

**Image Transformer**. ICML, 2018.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Image AR attention architecture |
| Intervention | Local self-attention |
| Original-source basis | Reference architecture, no separately established acceleration contribution in this review |
| Cost boundary | Foundation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.mlr.press/v80/parmar18a/parmar18a.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v80/parmar18a.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="vqvae"></a>

## vqvae

**Neural Discrete Representation Learning**. NeurIPS, 2017.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Discrete latent image representation |
| Intervention | Vector-quantized autoencoder |
| Original-source basis | Foundation for latent AR generation |
| Cost boundary | Foundation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1; abstract/selected method and performance passages |

[Reading source](https://proceedings.neurips.cc/paper/2017/hash/7a98af17e63a0ac09ce2e96d03992fbc-Abstract.html#page=1) · [Formal publication record](https://proceedings.neurips.cc/paper/2017/hash/7a98af17e63a0ac09ce2e96d03992fbc-Abstract.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="vqvae2"></a>

## vqvae2

**Generating Diverse High-Fidelity Images with VQ-VAE-2**. NeurIPS, 2019.

| Field | Paper-specific finding |
|---|---|
| Decision | background |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Hierarchical discrete image latents |
| Intervention | Multi-level VQ-VAE with AR priors |
| Original-source basis | General representation/generation reference |
| Cost boundary | Foundation |
| Reading extent | official abstract / selected original-source text |
| Source location | Official NeurIPS abstract |

[Reading source](https://proceedings.neurips.cc/paper/2019/hash/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Abstract.html) · [Formal publication record](https://proceedings.neurips.cc/paper/2019/hash/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Abstract.html)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="scan"></a>

## scan

**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**. AAAI, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / representation design |
| Specific object | AR coarse image prediction and selected refinement |
| Intervention | Coarse generation followed by calibrated local refinement |
| Original-source basis | Original source compares image generation time with LlamaGen; refinement itself adds work |
| Cost boundary | Whole design comparison, not a speedup caused by refinement alone |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6; abstract/selected method and performance passages |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/view/37400#page=6) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/37400)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="rejectdecoding"></a>

## reject_decoding

**Reject Decoding via Language-Vision Models for Text-to-Image Synthesis**. AAAI, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | multi-path search acceleration |
| Specific object | Multi-path AR text-to-image search |
| Intervention | Tiny visual-language scorer terminates poor partial paths early |
| Original-source basis | Original abstract reports lower synthesis time for search; baseline is multi-path reranking |
| Cost boundary | Search acceleration, separate from fixed single-trajectory sampling |
| Reading extent | official abstract / selected original-source text |
| Source location | Official AAAI abstract, multi-path search and time-consumption statements |

[Reading source](https://ojs.aaai.org/index.php/AAAI/article/view/25379) · [Formal publication record](https://ojs.aaai.org/index.php/AAAI/article/view/25379)

Venue check: CCF-listed venue name, checked against retained 2026 directory mirror; official-host copy unavailable

<a name="causvidvideo"></a>

## causvid_video

**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Causal video diffusion inference |
| Intervention | Distills a bidirectional many-step teacher into a KV-cached causal few-step generator |
| Original-source basis | Table 3 reports latency and FPS including the text encoder, diffusion model and VAE decoder |
| Cost boundary | New AR generator, teacher originally bidirectional |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="arcachevideo"></a>

## arcache_video

**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video diffusion recomputation |
| Intervention | History-guided cache timing with enhanced residual correction |
| Original-source basis | Original source evaluates caching on sequentially generated video segments |
| Cost boundary | AR video diffusion inference, not generic image diffusion |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="lavigen3d"></a>

## lavigen_3d

**Repurposing 3D Generative Model for Autoregressive Layout Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D layout |
| Study type | efficient generator / learned replacement |
| Specific object | Autoregressive 3D layout generation |
| Intervention | Repurposes a 3D diffusion model and uses dual-guidance self-rollout distillation |
| Original-source basis | Original performance and ablation passages compare generation time |
| Cost boundary | 3D layout generation, not static-image latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="cubecomposervideo"></a>

## cubecomposer_video

**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video view expansion |
| Study type | efficient generator / learned replacement |
| Specific object | Autoregressive cubemap video synthesis |
| Intervention | Sparse context across cube faces and temporal windows |
| Original-source basis | Source context ablation reports reduced TFLOPs and discusses lower peak memory |
| Cost boundary | Computational work for panorama generation, not measured latency reduction |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf#page=8) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="pointnsp3d"></a>

## pointnsp_3d

**PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D point cloud |
| Study type | efficient generator / learned replacement |
| Specific object | AR point-cloud sampling |
| Intervention | Next-scale level-of-detail prediction replaces next-point progression |
| Original-source basis | Table 3 reports sampling seconds separately from training GPU hours |
| Cost boundary | 3D sampling time, not training-time acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="flashmesh3d"></a>

## flashmesh_3d

**FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D mesh |
| Study type | learned speculative decoding modules |
| Specific object | AR mesh token decoding |
| Intervention | Trained face/point/coordinate proposal blocks with structured correction and backbone verification |
| Original-source basis | Table 1 reports mesh-token throughput on H20 for Meshtron and Mesh-RFT variants with learned speculation modules |
| Cost boundary | Mesh tokens per generation second, parameter counts increase with the added modules. No independent sampling-law guarantee checked |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6, Table 1 and Sections 4.1–4.2; PDF p. 8, Tables 2–5 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="novavideo"></a>

## nova_video

**Autoregressive Video Generation without Vector Quantization**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Temporal/spatial AR video generation |
| Intervention | Frame-wise temporal causality and set-wise spatial generation with continuous tokens |
| Original-source basis | Original source reports video inference latency against prior video generators |
| Cost boundary | New video generator, distinct from image accelerator NOVA |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="lumos1video"></a>

## lumos1_video

**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | LLM-based AR video generation |
| Intervention | Frame-causal masked parallel decoding with KV cache |
| Original-source basis | Table 6 compares next-token prediction and masked prediction with/without cache on H20 |
| Cost boundary | Video inference time, RoPE overhead is separately reported |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf#page=9) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59ad89d72559dd4ce557d56f36313724-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="ardragvideo"></a>

## ar_drag_video

**Real-Time Motion-Controllable Autoregressive Video Diffusion**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Motion-controlled AR video diffusion |
| Intervention | Few-step causal distillation with motion conditioning |
| Original-source basis | Original source reports latency and real-time generation comparisons |
| Cost boundary | Controlled video generation, not motion-estimation acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/71c1d6ec1f0003d8ea10bbea4291002d-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="fastcarvideo"></a>

## fastcar_video

**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video decoder MLP computation |
| Intervention | Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling |
| Original-source basis | Original experiments report decoder acceleration and energy behavior |
| Cost boundary | Edge hardware/software co-design |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf#page=8) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8488454077cb0fd9d31772274c78115d-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="flowcachevideo"></a>

## flowcache_video

**Flow Caching for Autoregressive Video Generation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video denoising and KV storage |
| Intervention | Independent chunk cache policies with bounded KV compression |
| Original-source basis | Original experiments compare caching speed and video metrics on MAGI-1 and SkyReels-V2 |
| Cost boundary | Generation speed and cache memory, no independent output-law guarantee |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf#page=9) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/85dc8f85ff978b9c606d3b2f5b0da69a-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="rollingforcingvideo"></a>

## rolling_forcing_video

**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Streaming AR video denoising |
| Intervention | Rolling-frame generation and few-step distillation with extended windows |
| Original-source basis | Experiments measure throughput and latency after stable execution speed is reached |
| Cost boundary | Steady-state latency, not first-frame latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf#page=8) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="diagonaldistillvideo"></a>

## diagonal_distill_video

**Streaming Autoregressive Video Generation via Diagonal Distillation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Streaming AR video diffusion |
| Intervention | Diagonal distillation restructures few-step frame synthesis |
| Original-source basis | Experiments separately measure H100 FPS and first-frame latency |
| Cost boundary | First-frame delay and sustained FPS are different measures |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d899eabc6c8fefd0d4064762aba407e2-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="selfforcingvideo"></a>

## self_forcing_video

**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**. NeurIPS, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Few-step streaming AR video generator |
| Intervention | Self-generated training rollouts with rolling KV-cache inference |
| Original-source basis | Original experiments report first-frame latency and throughput on H100 |
| Cost boundary | New/distilled generator, not an unchanged-model execution optimization |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="lightforcingvideo"></a>

## light_forcing_video

**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video attention |
| Intervention | Chunk-aware sparsity allocation with hierarchical sparse attention |
| Original-source basis | Original source reports standalone and combined end-to-end speedups |
| Cost boundary | Standalone and combined results must remain distinct |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/lv26i.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="sanavideo"></a>

## sana_video

**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Long-video AR attention and cache growth |
| Intervention | Linear attention with constant-memory block-causal state |
| Original-source basis | Original tables compare video latency and describe fixed-size historical state |
| Cost boundary | New-generator latency and memory, quantized deployment is a separate setting |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf#page=7) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b93c59da0d0f835907fd661d419db2-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="asdcausalvideo"></a>

## asd_causal_video

**Towards One-step Causal Video Generation via Adversarial Self-Distillation**. ICLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video conditional denoising evaluations |
| Intervention | Adversarial self-distillation with extra first-frame updates |
| Original-source basis | Table 1 compares one/two-step student settings and video quality |
| Cost boundary | Conditional update budget only, first-frame enhancement adds steps, no measured latency claimed |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf#page=8) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3ae86071c169649bff21188c536163dc-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="evatokvideo"></a>

## evatok_video

**EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video token length |
| Intervention | Adaptive video token allocation |
| Original-source basis | Table 3 reports generation tokens and quality. Inference runtime or FLOPs savings have not been established |
| Cost boundary | Token savings are not measured speedup |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |
| Unresolved item | Table 3 reports generation tokens and quality. Inference runtime or FLOPs savings have not been established |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf#page=7) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="facemesh"></a>

## face_mesh

**FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | 3D mesh |
| Study type | efficient generator / learned replacement |
| Specific object | Autoregressive mesh decoder |
| Intervention | One-face-one-token representation with latent diffusion for image-conditioned generation |
| Original-source basis | Inspected tables concern representation length and geometric fidelity |
| Cost boundary | Runtime or inference-work comparison remains unverified |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6 |
| Unresolved item | Inspected tables concern representation length and geometric fidelity |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="treemeshgpt3d"></a>

## treemeshgpt_3d

**TreeMeshGPT: Artistic Mesh Generation with Autoregressive Tree Sequencing**. CVPR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | 3D mesh |
| Study type | efficient generator / learned replacement |
| Specific object | Mesh AR sequence length |
| Intervention | Tree sequencing and compact face tokenization |
| Original-source basis | Inspected source reports compression and mesh quality. An inference-cost comparison was not located |
| Cost boundary | Token count alone is insufficient |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1 |
| Unresolved item | Inspected source reports compression and mesh quality. An inference-cost comparison was not located |

[Reading source](https://openaccess.thecvf.com/content/CVPR2025/papers/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.pdf#page=1) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2025/html/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="edgerunner3d"></a>

## edgerunner_3d

**EdgeRunner: Auto-regressive Auto-encoder for Artistic Mesh Generation**. ICLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | 3D mesh |
| Study type | efficient generator / learned replacement |
| Specific object | AR mesh sampling |
| Intervention | Compact mesh tokens with an AR autoencoder |
| Original-source basis | Source reports its own token throughput and time by face count, without an established acceleration comparison |
| Cost boundary | Own timing alone does not establish a relative acceleration result |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9 |
| Unresolved item | Source reports its own token throughput and time by face count, without an established acceleration comparison |

[Reading source](https://proceedings.iclr.cc/paper_files/paper/2025/file/58e6c003c9fb3992265005ff6aef1913-Paper-Conference.pdf#page=9) · [Formal publication record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/58e6c003c9fb3992265005ff6aef1913-Abstract-Conference.html)

Venue check: CCF-listed venue; official primary proceedings confirm the main track. CCF directory host-copy limitation retained

<a name="faststarvideo"></a>

## faststar_video

**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | InfinityStar spatiotemporal token refinement |
| Intervention | Prunes converged spatial/temporal tokens with partial residual updates |
| Original-source basis | Original source reports latency and paired/output quality for InfinityStar |
| Cost boundary | Video generation latency, separate from static-image VAR |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1 |

[Reading source](https://arxiv.org/pdf/2603.07192#page=1) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37098-3_12)

Venue check: CCF-listed venue, primary formal publication confirmed; directory host-copy limitation retained

<a name="wag3d"></a>

## wag3d

**3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes**. BMVC, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D shape |
| Study type | efficient generator / learned replacement |
| Specific object | Autoregressive shape token sampling |
| Intervention | Wavelet hierarchy supports next-scale generation |
| Original-source basis | Original Table 2 reports shape sampling time; the abstract uses a different hardware setting |
| Cost boundary | 3D shape inference, hardware-specific results remain separate |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9 |

[Reading source](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf#page=9) · [Formal publication record](https://bmvc2025.bmva.org/proceedings/1064/)

Venue check: CCF-listed venue, primary formal publication confirmed; directory host-copy limitation retained

<a name="ardm2022"></a>

## ardm_2022

**Autoregressive Diffusion Models**. ICLR, 2022.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | image |
| Study type | efficient generator / learned replacement |
| Specific object | Order-agnostic AR image model evaluations |
| Intervention | Parallel generation under a selected network-evaluation budget |
| Original-source basis | Original Table 2 compares sequential and parallel CIFAR-10 sampling budgets |
| Cost boundary | Model-evaluation counts only, not measured wall-clock acceleration |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://arxiv.org/pdf/2110.02037#page=7) · [Formal publication record](https://iclr.cc/virtual/2022/poster/6228)

Venue check: CCF-listed venue, primary formal publication confirmed; directory host-copy limitation retained

<a name="mardinivideo"></a>

## mardini_video

**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**. TMLR, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Masked-AR video planning and spatial diffusion |
| Intervention | Low-resolution planning with a lightweight high-resolution diffusion model |
| Original-source basis | Original Table 3 compares asymmetric design latency and memory on A100 |
| Cost boundary | Video latency and GPU memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://arxiv.org/pdf/2410.20280#page=8) · [Formal publication record](https://jmlr.org/tmlr/papers/bib/fuOHI59rUW.bib)

Venue check: TMLR explicit author exception

<a name="dicodevideo"></a>

## dicode_video

**DiCoDe: Diffusion-Compressed Deep Tokens for Autoregressive Video Generation with Language Models**. TMLR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR prior over diffusion-compressed video tokens |
| Intervention | Deep video tokens followed by diffusion reconstruction |
| Original-source basis | Inspected source establishes compressed tokens and training efficiency, not a comparative generation-inference cost result |
| Cost boundary | Token reduction is not complete-generation latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |
| Unresolved item | Inspected source establishes compressed tokens and training efficiency, not a comparative generation-inference cost result |

[Reading source](https://arxiv.org/pdf/2412.04446#page=8) · [Formal publication record](https://jmlr.org/tmlr/papers/bib/B7a0IAIEXZ.bib)

Venue check: TMLR explicit author exception

<a name="ca2vdmvideo"></a>

## ca2_vdm_video

**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**. ICML, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video conditional-frame recomputation |
| Intervention | Causal feature computation and cache sharing across denoising steps |
| Original-source basis | Original experiments measure video generation speed and GPU cache memory |
| Cost boundary | Generation speed and cache memory |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf#page=8) · [Formal publication record](https://proceedings.mlr.press/v267/gao25m.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="xspecmesh3d"></a>

## xspecmesh_3d

**XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D mesh |
| Study type | execution optimization |
| Specific object | AR mesh next-token decoding |
| Intervention | Multi-head proposals with backbone verification/resampling and head distillation |
| Original-source basis | Table 3 and efficiency experiments report step latency and actual sampling speedup on RTX 3090 |
| Cost boundary | Mesh decoding runtime, no new preservation theorem certified |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf#page=8) · [Formal publication record](https://proceedings.mlr.press/v306/chen26dn.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="contextforcingvideo"></a>

## context_forcing_video

**Context Forcing: Consistent Autoregressive Video Generation with Long Context**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video context-memory growth |
| Intervention | Bounded slow/fast memory retains selected historical frames |
| Original-source basis | Original method specifies bounded historical token storage; experiments report FPS for long contexts |
| Cost boundary | Context-memory budget, not a claimed standalone wall-clock speedup |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf#page=6) · [Formal publication record](https://proceedings.mlr.press/v306/chen26eu.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="aad1video"></a>

## aad1_video

**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video denoising evaluation budget |
| Intervention | Asymmetric adversarial distillation trains a one-NFE causal student |
| Original-source basis | Original experiment description compares one-NFE generation with four-NFE AR baselines |
| Cost boundary | Denoiser-evaluation count, not measured end-to-end latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf#page=6) · [Formal publication record](https://proceedings.mlr.press/v306/li26iw.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="flexforcingvideo"></a>

## flex_forcing_video

**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | AR video generation execution schedule |
| Intervention | Flexible chunks with bidirectional planning and autoregressive within-chunk inference |
| Original-source basis | Original table compares FPS and neural-function evaluations for generation variants |
| Cost boundary | Model-design runtime comparison, not unchanged reference sampling |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf#page=6) · [Formal publication record](https://proceedings.mlr.press/v306/ma26b.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="fastarvideo"></a>

## fast_ar_video

**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video self/cross-attention and KV cache |
| Intervention | Temporal cache compression and approximate-neighbor sparse attention |
| Original-source basis | Original source reports end-to-end runtime, sustained throughput and peak-memory behavior |
| Cost boundary | Source-defined end-to-end generation, attention sub-results remain separate |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/samuel26a.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="quantvideogen"></a>

## quant_videogen

**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video KV storage |
| Intervention | Semantic smoothing and progressive residual cache quantization |
| Original-source basis | Original source reports reduced KV memory with a small latency overhead |
| Cost boundary | Memory efficiency, not a measured latency reduction |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v306/xi26f.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="motioncachevideo"></a>

## motioncache_video

**Motion-Aware Caching for Efficient Autoregressive Video Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video diffusion denoising computation |
| Intervention | Motion-weighted token updates after a full-computation warmup |
| Original-source basis | Original source reports inference latency and FLOPs on AR video backbones |
| Cost boundary | Warmup and token-update overhead remain part of the method |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 7 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf#page=7) · [Formal publication record](https://proceedings.mlr.press/v306/xu26an.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="deepforcingvideo"></a>

## deep_forcing_video

**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | AR video historical KV storage |
| Intervention | Persistent sink context with importance-aware KV pruning |
| Original-source basis | Original source specifies compressed historical storage and reports long-video throughput |
| Cost boundary | KV-retention budget, not proof of faster wall-clock generation |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 1 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf#page=1) · [Formal publication record](https://proceedings.mlr.press/v306/yi26c.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="causalforcingvideo"></a>

## causal_forcing_video

**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**. ICML, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Few-step causal video diffusion generator |
| Intervention | AR-teacher ODE initialization followed by distribution-matching distillation |
| Original-source basis | Original Table 1 reports FPS and latency for the distilled AR generator |
| Cost boundary | Efficient generator design, reported reference models differ |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 8 |

[Reading source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf#page=8) · [Formal publication record](https://proceedings.mlr.press/v306/zhu26bf.html)

Venue check: Official ICML main proceedings; CCF-directory host-copy limitation retained

<a name="rewardforcing"></a>

## reward_forcing

**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient generator / learned replacement |
| Specific object | Streaming AR video attention and conditional denoising |
| Intervention | Few-step causal distillation with a smaller attention window and fixed-size EMA sink state |
| Original-source basis | Table 1 reports video generation FPS; Figure 6 relates attention-window size to inference FPS |
| Cost boundary | Complete-generator comparison between different trained models, not an unchanged-checkpoint acceleration result |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 6, Table 1; PDF p. 8, Figure 6 and Section 4.3 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.html)

Venue check: Official CVPR main proceedings; CCF-directory host-copy limitation retained

<a name="avatarforcing"></a>

## avatar_forcing

**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**. CVPR, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video avatar |
| Study type | efficient generator / learned replacement |
| Specific object | Causal avatar-motion generation latency |
| Intervention | Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator |
| Original-source basis | Equation 4 specifies autoregressive motion generation; Table 1 compares latency against a reproduced INFP baseline |
| Cost boundary | Motion-generation time assumes pre-extracted audio features and 10 neural-function evaluations. This is not complete audiovisual-system latency |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 3, Eq. 4; PDF p. 4, Figure 4; PDF p. 6, Table 1 and Sections 5.2–5.3 |

[Reading source](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf#page=6) · [Formal publication record](https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html)

Venue check: Official CVPR main proceedings; CCF-directory host-copy limitation retained

<a name="hiarvideo"></a>

## hiar_video

**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | Hierarchical denoising and pipelined execution of AR video blocks |
| Intervention | Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels |
| Original-source basis | Section 3 defines hierarchical causal denoising. Table 1 and Section 4.2 report 30 FPS and 0.30 s per-chunk latency, compared with 17 FPS and 0.69 s for other four-step distilled AR generators sharing Wan2.1-1.3B |
| Cost boundary | Streaming throughput and per-chunk latency, not complete-video latency. The approximately 1.8x headline matches the throughput ratio, not the listed latency ratio |
| Reading extent | selected primary PDF passages |
| Source location | PDF p. 9, Table 1 and Section 4.1; PDF pp. 10–11, Section 4.2 |
| Unresolved item | GPU configuration and full timing scope are not established by the selected passages. Do not equate throughput and latency ratios |

[Reading source](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13)

Venue check: Formal main proceedings, Workshop excluded

<a name="ispavideo"></a>

## ispa_video

**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | execution optimization |
| Specific object | KV-cache storage and attention computation in streaming AR video generators |
| Intervention | Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context |
| Original-source basis | Sections 3–4 describe the absorption of historical attention into projection weights. Figure 2 reports memory reduction. Figure 7 reports a 1.35x overall gain for ISPA and 1.86x when combined with W8A8, separately from the 1.89x attention-operator gain |
| Cost boundary | Peak GPU memory and the source-reported latency breakdown. Attention-only and quantized combined results remain separate |
| Reading extent | selected primary PDF passages |
| Source location | PDF pp. 2–3 and Section 3; PDF p. 11, Figure 2; PDF pp. 14–15, Figure 7 |
| Unresolved item | Figure 7 timing configuration is not fully specified in the inspected passages. Visual similarity is empirical, not equality of sampling distributions |

[Reading source](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25)

Venue check: Formal main proceedings, Workshop excluded

<a name="supervoxelgpt"></a>

## supervoxelgpt

**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | 3D geometry |
| Study type | efficient learned generator |
| Specific object | Shape-token sequence length and sequential AR transformer evaluations |
| Intervention | Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding |
| Original-source basis | Sections 3.3–4.1 explicitly apply Jacobi decoding to the AR token predictor, capped at 30 iterations. Tables 1–2 report seconds per shape. Section 4.2 decomposes total image-to-3D inference into saliency prediction, CVT, AR prediction and decoding |
| Cost boundary | Complete reported shape-generation time on one RTX 4090. Text-to-3D AR comparisons use different resolutions. The headline 10x averages heterogeneous image-to-3D baselines |
| Reading extent | selected primary PDF passages |
| Source location | PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency |
| Unresolved item | No fixed-generator ablation isolating Jacobi versus tokenization was established from the main-paper passages. Do not describe the mixed-baseline average as an AR-only speedup or infer distribution preservation |

[Reading source](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22)

Venue check: Formal main proceedings, Workshop excluded

<a name="liveavatarvideo"></a>

## live_avatar_video

**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**. ECCV, 2026.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient learned generator |
| Specific object | Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator |
| Intervention | Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations |
| Original-source basis | The method uses causal noisy-history KV caches. Table 3 separates DMD, sequence parallelism, timestep-forcing parallelism, VAE parallelism and kernel optimization. It reports 45.2 FPS and 1.21 s time to first frame for the full five-H100 configuration |
| Cost boundary | Streaming FPS and time to first frame at 720x400. GPU count changes across ablations. These values are not complete conversational latency or a same-hardware speed ratio |
| Reading extent | selected primary PDF passages |
| Source location | PDF pp. 2–3, streaming definition; PDF pp. 9–11, execution and setup; PDF p. 13, Table 3 |
| Unresolved item | Do not transfer the five-GPU system result to single-GPU deployment or infer that distillation preserves the teacher distribution |

[Reading source](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Formal publication record](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5)

Venue check: Formal main proceedings, Workshop excluded

<a name="evdmacmmm2023"></a>

## evdm_acmmm2023

**Efficiency-optimized Video Diffusion Models**. ACM MM, 2023.

| Field | Paper-specific finding |
|---|---|
| Decision | core |
| Generated output | video |
| Study type | efficient learned generator |
| Specific object | Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation |
| Intervention | Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm |
| Original-source basis | The original [MCVD paper, Section 2.1 and Figure 2](https://proceedings.neurips.cc/paper_files/paper/2022/file/944618542d80a63bbec16dfbd2bd689a-Paper-Conference.pdf#page=3) defines blockwise AR video generation. EVDM evaluates this denoiser family in multi-block prediction. Tables 2–3 report inference FLOPs reductions and Table 9 separately reports A40 latency measurements |
| Cost boundary | Denoiser FLOPs and reported model latency. The approximately 10x headline concerns arithmetic reduction. Table 9 lists 16.5 to 6.1 ms and 26.4 to 7.5 ms for two unlabeled configurations, not a 10x end-to-end video gain |
| Reading extent | selected primary PDF passages |
| Source location | EVDM PDF pp. 5–6, Tables 2–3 and experimental setup; PDF p. 8, Table 9. MCVD original Section 2.1 and Figure 2 |
| Unresolved item | Table 9 lacks explicit dataset labels for its two configurations and does not specify complete-video timing. Scope is MCVD block prediction, not every video diffusion model |

[Reading source](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) · [Formal publication record](https://dl.acm.org/doi/10.1145/3581783.3612406)

Venue check: Formal main proceedings, Workshop excluded

<a name="stablecontrolvar"></a>

## stable_control_var

**Stable Control Visual AutoRegressive Model: Precise and Efficient Image Generation via Scale Alignment**. ICASSP, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Candidate scale-alignment method for controllable VAR image generation |
| Intervention | Individual mechanism and inference savings not verified |
| Original-source basis | The complete ICASSP 2025 TOC identifies the paper at printed page 8733. Publisher-deposited DOI metadata confirms its formal title and authors. The individual IEEE page returned an access challenge and no original performance table was retrieved |
| Cost boundary | Inference cost not established |
| Reading extent | formal full-directory entry and publisher-deposited metadata only |
| Source location | ICASSP 2025 full TOC, entry beginning at p. 8733; Crossref record for 10.1109/ICASSP49660.2025.10890268 |
| Unresolved item | Retrieve the original abstract and full method/performance sections. Efficient in the title alone does not establish acceleration |

[Reading source](https://doi.org/10.1109/icassp49660.2025.10890268) · [Formal publication record](https://doi.org/10.1109/icassp49660.2025.10890268)

Venue check: Formal main proceedings, Workshop excluded

<a name="grow3d"></a>

## grow3d

**Grow3D: Hierarchical Next-Scale Octree Prediction for Fast and High-Fidelity 3D Shape Generation**. ACM Transactions on Graphics, 2026.

| Field | Paper-specific finding |
|---|---|
| Publication note | Online publication: 2026-09-14. The publisher metadata assigns volume 46(1) to the 2027 print issue. Listed under the verified online year. |
| Decision | pending |
| Generated output | 3D geometry |
| Study type | not admitted to core |
| Specific object | Next-scale octree prediction for efficient AR 3D-shape generation |
| Intervention | Multiscale sparse octree tokens with structure-aware attention |
| Original-source basis | The ACM-deposited abstract explicitly motivates faster AR shape inference and describes next-scale prediction. The DOI confirms online publication on 14 September 2026, with a 2027 print issue. The publisher page/PDF could not be accessed for experimental verification |
| Cost boundary | Author abstract reports speed benefits. No original runtime table independently inspected |
| Reading extent | publisher-deposited abstract and bibliographic metadata only |
| Source location | ACM-deposited Crossref abstract and publication dates, DOI 10.1145/3820379 |
| Unresolved item | Retrieve the full paper and identify actual inference timing, baseline and hardware. Do not report a numerical speedup from secondary summaries |

[Reading source](https://doi.org/10.1145/3820379) · [Formal publication record](https://doi.org/10.1145/3820379)

Venue check: Formal online journal publication. CCF venue-name check follows the retained catalog mirror, not an independently retrieved official-host directory

<a name="dualstreamvisualtokenizer"></a>

## dual_stream_visual_tokenizer

**A Dual Stream Visual Tokenizer for LLM Image Generation**. IJCAI, 2025.

| Field | Paper-specific finding |
|---|---|
| Decision | pending |
| Generated output | image |
| Study type | not admitted to core |
| Specific object | Compact dual-stream visual representation for LLM image generation |
| Intervention | Combine semantic codes with low-resolution structural codes and a diffusion reconstruction stage |
| Original-source basis | Sections 3–4 and Tables 2–4 evaluate token counts and reconstruction/alignment quality. The full nine-page paper was retrieved. The inspected experiments do not establish generation latency, throughput or inference FLOPs |
| Cost boundary | Token length and reconstruction measurements, with an additional diffusion decoding stage |
| Reading extent | selected primary PDF passages |
| Source location | PDF pp. 4–6, architecture and Tables 2–4 |
| Unresolved item | No original AR inference-cost result established. Shorter representation alone is insufficient for core admission |

[Reading source](https://ijcai.org/proceedings/2025/0167.pdf) · [Formal publication record](https://ijcai.org/proceedings/2025/167)

Venue check: Formal main proceedings, Workshop excluded
