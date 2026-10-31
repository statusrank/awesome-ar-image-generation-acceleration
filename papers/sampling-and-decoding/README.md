# Sampling and Decoding

[Home](../../README.md) · [Collections](../../papers/README.md)

Parallel evaluation, speculative decoding and generation scheduling.

**31 papers.**

## Contents

- [Parallel and Speculative Candidate Generation](#parallel-and-speculative-candidate-generation)
- [Verification and Commitment](#verification-and-commitment)
- [Generation Scheduling and Context Organization](#generation-scheduling-and-context-organization)
- [Other parallel sampling](#other-parallel-sampling)

## Parallel and Speculative Candidate Generation

<a id="paper-tmlrxyatz9hpe7"></a>

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026). [Paper](https://openreview.net/forum?id=xYATz9HpE7) · [PDF](https://arxiv.org/pdf/2505.24791)
  - **Focus:** Image generation by autoregressive normalizing flows.
  - **Mechanism:** Selective Jacobi iterations parallelize sequential flow inversions.
  - **Source:** [Paper](https://arxiv.org/pdf/2505.24791#page=9), PDF p. 9.

<a id="paper-ciar"></a>

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1)
  - **Focus:** Cloud-device AR image decoding.
  - **Mechanism:** On-device interval verification reduces cloud verification calls.
  - **Source:** [Paper](https://arxiv.org/pdf/2603.25463v1#page=7), PDF p. 7.

<a id="paper-fasthybrid"></a>

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf)
  - **Focus:** Hybrid AR image generator with diffusion decoder.
  - **Mechanism:** Lookahead and guided decoding reduce hybrid generation computation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-lisa"></a>

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf)
  - **Focus:** Visual AR speculative verification.
  - **Mechanism:** Locality-informed verifier modifies acceptance behavior.
  - **Source:** [Paper](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf#page=13), PDF p. 13.

<a id="paper-mulosd"></a>

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf)
  - **Focus:** High-resolution AR image speculative generation.
  - **Mechanism:** Low-resolution proposals with upsampling and spatially local verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-sjdplus"></a>

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://doi.org/10.1109/TPAMI.2026.3700227) · [PDF](https://arxiv.org/pdf/2512.07503v1)
  - **Focus:** AR text-to-image Jacobi candidate reuse.
  - **Mechanism:** Retains high-confidence unaccepted draft states.
  - **Source:** [Paper](https://arxiv.org/pdf/2512.07503v1#page=1), PDF p. 1.

<a id="paper-sjdpac"></a>

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf)
  - **Focus:** AR image Jacobi candidate generation.
  - **Mechanism:** Proactive drafting and adaptive continuation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-scd"></a>

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2)
  - **Focus:** AR image stochastic speculative execution.
  - **Mechanism:** Couples proposal/verification randomness.
  - **Source:** [Paper](https://arxiv.org/pdf/2510.24211v2#page=1), PDF p. 1.

<a id="paper-supervoxelgpt"></a>

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf)
  - **Focus:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Mechanism:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf), PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency.

<a id="paper-sjd"></a>

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD)
  - **Focus:** AR text-to-image next-token execution.
  - **Mechanism:** Jacobi candidate reuse with stochastic verification.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf#page=8), PDF p. 8.

<a id="paper-hawk"></a>

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf)
  - **Focus:** AR text-to-image speculative proposals.
  - **Mechanism:** Spatial-context drafting improves candidate prediction.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf#page=1), PDF p. 1.

## Verification and Commitment

<a id="paper-coolsd"></a>

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39489) · [PDF](https://arxiv.org/pdf/2601.09212)
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Anneals relaxed acceptance with a specified resampling distribution.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/39489/43450#page=7), PDF p. 7.

<a id="paper-cspd"></a>

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_32) · [PDF](https://arxiv.org/pdf/2411.11925)
  - **Focus:** MAR continuous conditional sampling.
  - **Mechanism:** Uses continuous speculative proposals and approximate trajectory alignment.
  - **Source:** [Paper](https://arxiv.org/pdf/2411.11925#page=2), PDF p. 2.

<a id="paper-csd"></a>

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/wang26gi.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf)
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Uses content-dependent acceptance relaxation and resampling.
  - **Source:** [Paper](https://proceedings.mlr.press/v306/wang26gi.html#page=9), PDF p. 9.

<a id="paper-lisa"></a>

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf)
  - **Focus:** Visual AR speculative verification.
  - **Mechanism:** Locality-informed verifier modifies acceptance behavior.
  - **Source:** [Paper](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf#page=13), PDF p. 13.

<a id="paper-mulosd"></a>

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf)
  - **Focus:** High-resolution AR image speculative generation.
  - **Mechanism:** Low-resolution proposals with upsampling and spatially local verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-sjdsv"></a>

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26fd.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf)
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Semantic subsequence verification changes the tested/committed positions.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf#page=7), PDF p. 7.

<a id="paper-vvs"></a>

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf)
  - **Focus:** AR visual speculative verification.
  - **Mechanism:** Skips verification for selected provisional positions.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-sjd"></a>

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD)
  - **Focus:** AR text-to-image next-token execution.
  - **Mechanism:** Jacobi candidate reuse with stochastic verification.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf#page=8), PDF p. 8.

<a id="paper-gsd"></a>

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image speculative decoding.
  - **Mechanism:** Groups spatially related token candidates for verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf#page=8), PDF p. 8.

<a id="paper-hawk"></a>

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf)
  - **Focus:** AR text-to-image speculative proposals.
  - **Mechanism:** Spatial-context drafting improves candidate prediction.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-lantern"></a>

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf)
  - **Focus:** Visual AR speculative acceptance.
  - **Mechanism:** Latent-neighborhood relaxed acceptance.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf#page=22), PDF p. 22.

<a id="paper-entropydecoding"></a>

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf)
  - **Focus:** Visual AR sampling and speculation.
  - **Mechanism:** Entropy controls temperature and relaxed acceptance.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf#page=9), PDF p. 9.

## Generation Scheduling and Context Organization

<a id="paper-gtr"></a>

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf)
  - **Focus:** MAR stages and inner sampling budget.
  - **Mechanism:** Separates structure generation and detail reconstruction with frequency-weighted selection.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-hiarvideo"></a>

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf)
  - **Focus:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Mechanism:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf), PDF p. 9, Table 1 and Section 4.1; PDF pp. 10–11, Section 4.2.

<a id="paper-moss"></a>

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37611) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573)
  - **Focus:** High-resolution next-scale transformer execution.
  - **Mechanism:** Mixes scale work and dispatches late refinement selectively.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573#page=7), PDF p. 7.

<a id="paper-pjd"></a>

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf)
  - **Focus:** AR image Jacobi candidate refinement.
  - **Mechanism:** Spatial parallel drafts with adaptive attention masks.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-tmlrwkctcxo1a9"></a>

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811)
  - **Focus:** Multiscale AR serial sampling schedule.
  - **Mechanism:** Progressive checkerboards permit parallel positions within scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2602.03811#page=6), PDF p. 6.

<a id="paper-mpadmri"></a>

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf)
  - **Focus:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Mechanism:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf), PDF p. 2, Figure 1; p. 9, Section 4.2; pp. 14–15, reduced-refinement discussion. Figure 1.

<a id="paper-emigm"></a>

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/you25d.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf)
  - **Focus:** Continuous masked image generation including MAR.
  - **Mechanism:** Revises masking, sampling schedule and conditional token modeling.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf#page=29), PDF p. 29.

<a id="paper-fastvar"></a>

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.23367)
  - **Focus:** High-resolution next-scale token processing.
  - **Mechanism:** Cached token pruning forwards selected tokens and recovers omitted states.
  - **Source:** [Paper](https://arxiv.org/pdf/2503.23367#page=1), PDF p. 1.

<a id="paper-nfig"></a>

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf)
  - **Focus:** Next-scale AR frequency stages.
  - **Mechanism:** Generates low-frequency structure before higher-frequency detail.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-zipar"></a>

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/he25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf)
  - **Focus:** Causal visual AR decoding.
  - **Mechanism:** Spatially parallel decoding with local context windows.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf#page=7), PDF p. 7.

<a id="paper-parallelmultiscale2017"></a>

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf)
  - **Focus:** Pixel AR sampling dependency depth.
  - **Mechanism:** Parallel multiscale density factorization.
  - **Source:** [Paper](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf#page=8), PDF p. 8.

## Other parallel sampling

<a id="paper-ardm2022"></a>

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022). [Paper](https://iclr.cc/virtual/2022/poster/6228) · [PDF](https://arxiv.org/pdf/2110.02037)
  - **Focus:** Order-agnostic AR image model evaluations.
  - **Mechanism:** Parallel generation under a selected network-evaluation budget.
  - **Source:** [Paper](https://arxiv.org/pdf/2110.02037#page=7), PDF p. 7.
