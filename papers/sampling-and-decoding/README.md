# Sampling and Decoding

[Home](../../README.md) · [All categories](../../papers/README.md) · [By year](../../papers/by-year.md)

Parallel evaluation, speculative decoding and generation scheduling.

**31 papers.** Titles link to recorded PDFs or the official paper page.

## Contents

- [Parallel and Speculative Candidate Generation](#parallel-and-speculative-candidate-generation)
- [Verification and Commitment](#verification-and-commitment)
- [Generation Scheduling and Context Organization](#generation-scheduling-and-context-organization)
- [Other verified parallel sampling](#other-verified-parallel-sampling)

## Parallel and Speculative Candidate Generation

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026). [Paper](https://openreview.net/forum?id=xYATz9HpE7) · [PDF](https://arxiv.org/pdf/2505.24791) · [Details](../paper-notes.md#tmlrxyatz9hpe7)
  - **Accelerates:** Image generation by autoregressive normalizing flows.
  - **Approach:** Selective Jacobi iterations parallelize sequential flow inversions.

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1) · [Details](../paper-notes.md#ciar)
  - **Accelerates:** Cloud-device AR image decoding.
  - **Approach:** On-device interval verification reduces cloud verification calls.

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#fasthybrid)
  - **Accelerates:** Hybrid AR image generator with diffusion decoder.
  - **Approach:** Lookahead and guided decoding reduce hybrid generation computation.

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) · [Details](../paper-notes.md#lisa)
  - **Accelerates:** Visual AR speculative verification.
  - **Approach:** Locality-informed verifier modifies acceptance behavior.

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#mulosd)
  - **Accelerates:** High-resolution AR image speculative generation.
  - **Approach:** Low-resolution proposals with upsampling and spatially local verification.

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://doi.org/10.1109/TPAMI.2026.3700227) · [PDF](https://arxiv.org/pdf/2512.07503v1) · [Details](../paper-notes.md#sjdplus)
  - **Accelerates:** AR text-to-image Jacobi candidate reuse.
  - **Approach:** Retains high-confidence unaccepted draft states.

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#sjdpac)
  - **Accelerates:** AR image Jacobi candidate generation.
  - **Approach:** Proactive drafting and adaptive continuation.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2) · [Details](../paper-notes.md#scd)
  - **Accelerates:** AR image stochastic speculative execution.
  - **Approach:** Couples proposal/verification randomness.

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Details](../paper-notes.md#supervoxelgpt)
  - **Accelerates:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Approach:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD) · [Details](../paper-notes.md#sjd)
  - **Accelerates:** AR text-to-image next-token execution.
  - **Approach:** Jacobi candidate reuse with stochastic verification.

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) · [Details](../paper-notes.md#hawk)
  - **Accelerates:** AR text-to-image speculative proposals.
  - **Approach:** Spatial-context drafting improves candidate prediction.

## Verification and Commitment

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39489) · [PDF](https://arxiv.org/pdf/2601.09212) · [Details](../paper-notes.md#coolsd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Anneals relaxed acceptance with a specified resampling distribution.

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_32) · [PDF](https://arxiv.org/pdf/2411.11925) · [Details](../paper-notes.md#cspd)
  - **Accelerates:** MAR continuous conditional sampling.
  - **Approach:** Uses continuous speculative proposals and approximate trajectory alignment.

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/wang26gi.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) · [Details](../paper-notes.md#csd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Uses content-dependent acceptance relaxation and resampling.

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) · [Details](../paper-notes.md#lisa)
  - **Accelerates:** Visual AR speculative verification.
  - **Approach:** Locality-informed verifier modifies acceptance behavior.

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#mulosd)
  - **Accelerates:** High-resolution AR image speculative generation.
  - **Approach:** Low-resolution proposals with upsampling and spatially local verification.

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26fd.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) · [Details](../paper-notes.md#sjdsv)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Semantic subsequence verification changes the tested/committed positions.

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#vvs)
  - **Accelerates:** AR visual speculative verification.
  - **Approach:** Skips verification for selected provisional positions.

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD) · [Details](../paper-notes.md#sjd)
  - **Accelerates:** AR text-to-image next-token execution.
  - **Approach:** Jacobi candidate reuse with stochastic verification.

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#gsd)
  - **Accelerates:** AR image speculative decoding.
  - **Approach:** Groups spatially related token candidates for verification.

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) · [Details](../paper-notes.md#hawk)
  - **Accelerates:** AR text-to-image speculative proposals.
  - **Approach:** Spatial-context drafting improves candidate prediction.

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) · [Details](../paper-notes.md#lantern)
  - **Accelerates:** Visual AR speculative acceptance.
  - **Approach:** Latent-neighborhood relaxed acceptance.

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) · [Details](../paper-notes.md#entropydecoding)
  - **Accelerates:** Visual AR sampling and speculation.
  - **Approach:** Entropy controls temperature and relaxed acceptance.

## Generation Scheduling and Context Organization

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) · [Details](../paper-notes.md#gtr)
  - **Accelerates:** MAR stages and inner sampling budget.
  - **Approach:** Separates structure generation and detail reconstruction with frequency-weighted selection.

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) · [Details](../paper-notes.md#hiarvideo)
  - **Accelerates:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Approach:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37611) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) · [Details](../paper-notes.md#moss)
  - **Accelerates:** High-resolution next-scale transformer execution.
  - **Approach:** Mixes scale work and dispatches late refinement selectively.

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#pjd)
  - **Accelerates:** AR image Jacobi candidate refinement.
  - **Approach:** Spatial parallel drafts with adaptive attention masks.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811) · [Details](../paper-notes.md#tmlrwkctcxo1a9)
  - **Accelerates:** Multiscale AR serial sampling schedule.
  - **Approach:** Progressive checkerboards permit parallel positions within scales.

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) · [Details](../paper-notes.md#mpadmri)
  - **Accelerates:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Approach:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/you25d.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) · [Details](../paper-notes.md#emigm)
  - **Accelerates:** Continuous masked image generation including MAR.
  - **Approach:** Revises masking, sampling schedule and conditional token modeling.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.23367) · [Details](../paper-notes.md#fastvar)
  - **Accelerates:** High-resolution next-scale token processing.
  - **Approach:** Cached token pruning forwards selected tokens and recovers omitted states.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) · [Details](../paper-notes.md#nfig)
  - **Accelerates:** Next-scale AR frequency stages.
  - **Approach:** Generates low-frequency structure before higher-frequency detail.

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/he25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) · [Details](../paper-notes.md#zipar)
  - **Accelerates:** Causal visual AR decoding.
  - **Approach:** Spatially parallel decoding with local context windows.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) · [Details](../paper-notes.md#parallelmultiscale2017)
  - **Accelerates:** Pixel AR sampling dependency depth.
  - **Approach:** Parallel multiscale density factorization.

## Other verified parallel sampling

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022). [Paper](https://iclr.cc/virtual/2022/poster/6228) · [PDF](https://arxiv.org/pdf/2110.02037) · [Details](../paper-notes.md#ardm2022)
  - **Accelerates:** Order-agnostic AR image model evaluations.
  - **Approach:** Parallel generation under a selected network-evaluation budget.
