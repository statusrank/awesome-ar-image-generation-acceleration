# Image Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [By mechanism](../../README.md) · [Background](../../background/README.md) · [Pending](../../pending/README.md)

**105 core papers.** A study with verified image and video applications appears in both task lists. Counts must not be added to obtain unique papers.

## image

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) (ICIC, 2027). [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) · [Details](../../paper-notes.md#dynamicvar)
  - **Accelerates:** High-resolution AR token-path computation.
  - **Approach:** Routes samples among discrete/hybrid/continuous representation paths.
  - Online 2026, proceedings imprint 2027.
  - **Original-source evidence:** Publisher abstract explicitly reports inference throughput against AR and diffusion generators.
  - **Source location:** Publisher abstract, inference-throughput statement · [Original source](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16).
  - **Measured scope:** Abstract-supported throughput, hardware/timing boundary not checked. Reading extent: official abstract / selected original-source text.

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026). [Paper](https://openreview.net/forum?id=xYATz9HpE7) · [PDF](https://arxiv.org/pdf/2505.24791) · [Details](../../paper-notes.md#tmlrxyatz9hpe7)
  - **Accelerates:** Image generation by autoregressive normalizing flows.
  - **Approach:** Selective Jacobi iterations parallelize sequential flow inversions.
  - **Original-source evidence:** Source evaluates image-model inference speed.
  - **Source location:** PDF p. 9; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2505.24791#page=9).
  - **Measured scope:** AR normalizing-flow inference, not token-level speculative decoding. Reading extent: selected primary PDF passages.

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26dq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) · [Details](../../paper-notes.md#nova)
  - **Accelerates:** Next-scale visual AR token processing.
  - **Approach:** Entropy-guided adaptive token reduction and cached residual reuse.
  - **Original-source evidence:** Source evaluates runtime of the token-reduction method.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf#page=1).
  - **Measured scope:** VAR inference runtime. Reading extent: selected primary PDF passages.

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39936) · [PDF](https://arxiv.org/pdf/2511.16047) · [Details](../../paper-notes.md#amskv)
  - **Accelerates:** Next-scale VAR KV memory and attention.
  - **Approach:** Retains condensed and local scales with adaptive cache allocation.
  - **Original-source evidence:** Original experiments compare cache budget and generation quality against full-cache VAR.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://ojs.aaai.org/index.php/AAAI/article/download/39936/43897#page=7).
  - **Measured scope:** KV storage and attention, not automatically end-to-end latency. Reading extent: selected primary PDF passages.

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39489) · [PDF](https://arxiv.org/pdf/2601.09212) · [Details](../../paper-notes.md#coolsd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Anneals relaxed acceptance with a specified resampling distribution.
  - **Original-source evidence:** Source reports speed-quality experiments on visual AR generators.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://ojs.aaai.org/index.php/AAAI/article/download/39489/43450#page=7).
  - **Measured scope:** Speculative generation latency, no new preservation certification. Reading extent: selected primary PDF passages.

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) · [Details](../../paper-notes.md#arvar)
  - **Accelerates:** HART and Infinity next-scale inference.
  - **Approach:** Uses earlier attention for token selection and removes a late guidance branch.
  - **Original-source evidence:** Original source reports inference speed comparisons and component ablations.
  - **Source location:** PDF p. 14; abstract/selected method and performance passages · [Original source](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf#page=14).
  - **Measured scope:** Reported image inference latency. Reading extent: selected primary PDF passages.

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26du.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) · [Details](../../paper-notes.md#sar)
  - **Accelerates:** Grouped AR image generation.
  - **Approach:** Self-token prediction generates flexible token groups per step.
  - **Original-source evidence:** Source reports inference efficiency and grouped-input comparisons.
  - **Source location:** PDF p. 5; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf#page=5).
  - **Measured scope:** Grouped generation runtime. Reading extent: selected primary PDF passages.

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yu26z.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) · [Details](../../paper-notes.md#barmbm)
  - **Accelerates:** Bitwise AR image generation.
  - **Approach:** Masked bit modeling supports efficient prediction of large-vocabulary image representations.
  - **Original-source evidence:** Source compares generation FID with image throughput.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf#page=7).
  - **Measured scope:** New-generator throughput. Reading extent: selected primary PDF passages.

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) · [Details](../../paper-notes.md#arpg)
  - **Accelerates:** Random-order AR image decoding.
  - **Approach:** Decouples position guidance and content prediction for grouped decoding.
  - **Original-source evidence:** Original source reports image throughput and GPU-memory comparisons for ARPG.
  - **Source location:** PDF p. 14; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf#page=14).
  - **Measured scope:** Generator throughput and memory. Reading extent: selected primary PDF passages.

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1) · [Details](../../paper-notes.md#ciar)
  - **Accelerates:** Cloud-device AR image decoding.
  - **Approach:** On-device interval verification reduces cloud verification calls.
  - **Original-source evidence:** Official source reports decoding speed and cloud-request reductions.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2603.25463v1#page=7).
  - **Measured scope:** Cloud-device runtime and communication requests. Reading extent: selected primary PDF passages.

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_32) · [PDF](https://arxiv.org/pdf/2411.11925) · [Details](../../paper-notes.md#cspd)
  - **Accelerates:** MAR continuous conditional sampling.
  - **Approach:** Uses continuous speculative proposals and approximate trajectory alignment.
  - **Original-source evidence:** Source reports wall-time comparisons with default MAR.
  - **Source location:** PDF p. 2; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2411.11925#page=2).
  - **Measured scope:** MAR inference time, trajectory/endpoint guarantees not rechecked here. Reading extent: selected primary PDF passages.

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/wang26gi.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) · [Details](../../paper-notes.md#csd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Uses content-dependent acceptance relaxation and resampling.
  - **Original-source evidence:** Source evaluates inference acceleration on Lumina-mGPT and image metrics.
  - **Source location:** PDF p. 9; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v306/wang26gi.html#page=9).
  - **Measured scope:** Visual AR generation runtime. Reading extent: selected primary PDF passages.

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) · [PDF](https://arxiv.org/pdf/2603.28049) · [Details](../../paper-notes.md#driftar)
  - **Accelerates:** Hybrid AR prediction and iterative visual decoding.
  - **Approach:** Entropy-guided speculation and one-step drifting decoder.
  - **Original-source evidence:** Source studies joint acceleration of the sequential AR stage and iterative decoder.
  - **Source location:** PDF p. 13; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2603.28049#page=13).
  - **Measured scope:** AR stage plus visual decoder. Reading extent: selected primary PDF passages.

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR, 2026). [Paper](https://doi.org/10.1007/978-3-032-31920-3_1) · [PDF](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) · [Details](../../paper-notes.md#varcompressor)
  - **Accelerates:** 8B bitwise AR image generation on edge GPUs.
  - **Approach:** Compresses inference memory for deployment.
  - **Original-source evidence:** Source reports edge-GPU memory/latency trade-offs.
  - **Source location:** PDF p. 11; abstract/selected method and performance passages · [Original source](https://doi.org/10.1007/978-3-032-31920-3_1#page=11).
  - **Measured scope:** Memory reduction and runtime must be reported separately. Reading extent: selected primary PDF passages.

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chu26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) · [Details](../../paper-notes.md#ccfsemantic1d)
  - **Accelerates:** AR prior over 1D image tokens.
  - **Approach:** Jointly learns semantic 1D representation and AR generation.
  - **Original-source evidence:** Appendix reports sampling throughput and FLOPs on H100.
  - **Source location:** PDF p. 13; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf#page=13).
  - **Measured scope:** New-generator image throughput. Reading extent: selected primary PDF passages.

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/tong26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) · [Details](../../paper-notes.md#sparsear)
  - **Accelerates:** AR image KV attention.
  - **Approach:** Entropy-aware cache sparsification.
  - **Original-source evidence:** Source evaluates AR image generation and editing; retain generation results separately.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf#page=1).
  - **Measured scope:** KV memory and attention runtime. Reading extent: selected primary PDF passages.

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) · [Details](../../paper-notes.md#evar)
  - **Accelerates:** Next-scale VAR parameter and execution cost.
  - **Approach:** Structured pruning with scale-aware compensation and distillation.
  - **Original-source evidence:** Source reports single-image iOS latency for pruned versus original VAR.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf#page=1).
  - **Measured scope:** Measured edge inference latency. Reading extent: selected primary PDF passages.

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#farmer)
  - **Accelerates:** Pixel-level autoregressive normalizing-flow sampling.
  - **Approach:** Self-supervised dimension reduction reduces sequential sampling burden.
  - **Original-source evidence:** Source reports an inference-speed intervention and sampling comparisons.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf#page=8).
  - **Measured scope:** Pixel-space AR/flow hybrid, not latent-token SD. Reading extent: selected primary PDF passages.

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26go.html) · [PDF](https://arxiv.org/pdf/2512.16483) · [Details](../../paper-notes.md#fastervar)
  - **Accelerates:** Late-scale VAR execution.
  - **Approach:** Adaptive stage selection and reduced computation at costly scales.
  - **Original-source evidence:** Source reports runtime evaluations of the acceleration method.
  - **Source location:** PDF p. 18; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2512.16483#page=18).
  - **Measured scope:** Next-scale inference runtime. Reading extent: selected primary PDF passages.

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#fasthybrid)
  - **Accelerates:** Hybrid AR image generator with diffusion decoder.
  - **Approach:** Lookahead and guided decoding reduce hybrid generation computation.
  - **Original-source evidence:** Source evaluates accelerated hybrid AR inference.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** AR plus conditional diffusion decoding. Reading extent: selected primary PDF passages.

- [**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) · [Details](../../paper-notes.md#ccfpredictionrefinement)
  - **Accelerates:** Causal AR image prediction unit.
  - **Approach:** Predicts overlapping tensors to refine previous discrete outputs.
  - **Original-source evidence:** Source contains quality/latency comparisons for TensorAR.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf#page=6).
  - **Measured scope:** New-generator inference latency. Reading extent: selected primary PDF passages.

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) · [Details](../../paper-notes.md#gtr)
  - **Accelerates:** MAR stages and inner sampling budget.
  - **Approach:** Separates structure generation and detail reconstruction with frequency-weighted selection.
  - **Original-source evidence:** Source compares MAR generation speed and quality under the two-stage strategy.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf#page=1).
  - **Measured scope:** MAR sampling runtime. Reading extent: selected primary PDF passages.

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39686) · [PDF](https://arxiv.org/pdf/2504.09261) · [Details](../../paper-notes.md#hack)
  - **Accelerates:** VAR historical KV storage.
  - **Approach:** Head-dependent cache compression.
  - **Original-source evidence:** Source evaluates inference cache requirements and generation behavior.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2504.09261#page=1).
  - **Measured scope:** KV memory and attention. Reading extent: selected primary PDF passages.

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1) · [Details](../../paper-notes.md#core2reviewcandidate)
  - **Accelerates:** LlamaGen guidance computation.
  - **Approach:** Weak-model training supports guidance and later replacement of expensive computation.
  - **Original-source evidence:** Primary source explicitly includes LlamaGen experiments alongside diffusion models.
  - **Source location:** PDF p. 16; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2503.09662v1#page=16).
  - **Measured scope:** Retain AR application, do not transfer diffusion-only speedups. Reading extent: selected primary PDF passages.

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#lactokgen)
  - **Accelerates:** High-resolution AR prior plus image reconstruction.
  - **Approach:** Compact discrete tokens with latent-consistency decoding.
  - **Original-source evidence:** Source reports per-image time on A800 with vLLM, including AR baselines.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Image generation time. Reading extent: selected primary PDF passages.

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#lazyvar)
  - **Accelerates:** VAR token processing and scale schedule.
  - **Approach:** Scale-dependent token pruning plus grouped scale decoding.
  - **Original-source evidence:** Source reports generation acceleration and ablations.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf#page=8).
  - **Measured scope:** VAR inference runtime. Reading extent: selected primary PDF passages.

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026). [Paper](https://2026.acmmm.org/site/technical-programme.html) · [PDF](https://arxiv.org/pdf/2511.15499v1) · [Details](../../paper-notes.md#ear)
  - **Accelerates:** AR image generation order and parallel groups.
  - **Approach:** Spiral expansion with length-adaptive parallel decoding.
  - Accepted
  - **Original-source evidence:** Source reports image generation quality-efficiency comparisons.
  - **Source location:** PDF p. 11; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2511.15499v1#page=11).
  - **Measured scope:** New-generator sampling throughput. Reading extent: selected primary PDF passages.

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026). [Paper](https://doi.org/10.1007/978-3-032-37035-8_33) · [PDF](https://arxiv.org/pdf/2512.04857v1) · [Details](../../paper-notes.md#linear)
  - **Accelerates:** Causal visual AR KV storage.
  - **Approach:** Progressively evicts historical lines outside retained dependency regions.
  - **Original-source evidence:** Source reports GPU-memory and throughput measurements on image generators.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2512.04857v1#page=1).
  - **Measured scope:** KV memory and throughput. Reading extent: selected primary PDF passages.

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) · [Details](../../paper-notes.md#lisa)
  - **Accelerates:** Visual AR speculative verification.
  - **Approach:** Locality-informed verifier modifies acceptance behavior.
  - **Original-source evidence:** Original source evaluates generation speed under a fixed drafter.
  - **Source location:** PDF p. 13; abstract/selected method and performance passages · [Original source](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf#page=13).
  - **Measured scope:** Speculative image inference. Reading extent: selected primary PDF passages.

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2507.01957v2) · [Details](../../paper-notes.md#lpd)
  - **Accelerates:** AR position grouping and inference schedule.
  - **Approach:** Position query tokens and locality-aware parallel generation order.
  - **Original-source evidence:** Source reports image generation latency against parallel AR baselines.
  - **Source location:** PDF p. 24; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2507.01957v2#page=24).
  - **Measured scope:** New-generator latency. Reading extent: selected primary PDF passages.

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) · [Details](../../paper-notes.md#madformer)
  - **Accelerates:** AR/diffusion hybrid block computation.
  - **Approach:** Allocates AR conditioning layers and iterative diffusion layers.
  - **Original-source evidence:** Controlled source experiments compare image quality under inference-compute budgets.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf#page=7).
  - **Measured scope:** Inference compute, not automatically measured end-to-end speedup. Reading extent: selected primary PDF passages.

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_34) · [PDF](https://arxiv.org/pdf/2506.12035) · [Details](../../paper-notes.md#marche)
  - **Accelerates:** MAR attention and feed-forward recomputation.
  - **Approach:** Cache-aware attention and selective KV refresh.
  - **Original-source evidence:** Source reports acceleration against original MAR.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2506.12035#page=1).
  - **Measured scope:** MAR inference runtime. Reading extent: selected primary PDF passages.

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#markovvar)
  - **Accelerates:** VAR historical context and memory.
  - **Approach:** Compressed history state and limited scale context.
  - **Original-source evidence:** Source reports peak-memory reductions against full-context VAR.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf#page=7).
  - **Measured scope:** Inference memory, not memory-to-speed equivalence. Reading extent: selected primary PDF passages.

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#marval)
  - **Accelerates:** MAR iterative conditional sampling.
  - **Approach:** Distills a faster sampler while retaining a masked AR generation organization.
  - **Original-source evidence:** Source explicitly evaluates inference acceleration from MAR distillation.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf#page=7).
  - **Measured scope:** Learned MAR sampling process. Reading extent: selected primary PDF passages.

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37611) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) · [Details](../../paper-notes.md#moss)
  - **Accelerates:** High-resolution next-scale transformer execution.
  - **Approach:** Mixes scale work and dispatches late refinement selectively.
  - **Original-source evidence:** Original source reports transformer-backbone speedup.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573#page=7).
  - **Measured scope:** Backbone runtime, not automatically complete-image latency. Reading extent: selected primary PDF passages.

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#mulosd)
  - **Accelerates:** High-resolution AR image speculative generation.
  - **Approach:** Low-resolution proposals with upsampling and spatially local verification.
  - **Original-source evidence:** Source reports image-generation acceleration.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** Speculative generation runtime. Reading extent: selected primary PDF passages.

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) · [Details](../../paper-notes.md#mvar)
  - **Accelerates:** VAR spatial and scale context.
  - **Approach:** Restricts conditioning to adjacent scales and local neighborhoods.
  - **Original-source evidence:** Source evaluates reduced model complexity and inference resource requirements.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf#page=6).
  - **Measured scope:** Conditional computation and memory. Reading extent: selected primary PDF passages.

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) · [Details](../../paper-notes.md#omnimamba)
  - **Accelerates:** Autoregressive image-token prediction with a Mamba-2 state-space backbone.
  - **Approach:** Train a unified next-token image/text generator with Mamba-2 and modality-specific vocabularies and adapters.
  - **Original-source evidence:** Section 4.5 separates text output from image output. Table 4 reports 5.68 images/s and 2.81 s for OmniMamba, 0.81 images/s and 19.66 s for Show-o, and 1.02 images/s and 15.64 s for JanusFlow. The image experiment uses one RTX 4090, FP16, batch 16 and 256-resolution output.
  - **Source location:** Official ECCV PDF pp. 3, 12–13, Section 4.5 and Table 4. Table 4 visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf).
  - **Measured scope:** Reported batched image-generation timing for different trained generators. The 119.2x headline and 63% memory result concern image-conditioned text output, not image generation. Inclusion of encoding and image decoding in Table 4 timing is not explicitly established. Reading extent: selected primary PDF passages.

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#pjd)
  - **Accelerates:** AR image Jacobi candidate refinement.
  - **Approach:** Spatial parallel drafts with adaptive attention masks.
  - **Original-source evidence:** Source reports image-generation runtime acceleration.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** Jacobi decoding runtime. Reading extent: selected primary PDF passages.

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26gy.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) · [Details](../../paper-notes.md#prismmoe)
  - **Accelerates:** Dense visual AR predictor computation.
  - **Approach:** Dense-to-MoE conversion with sparse expert activation.
  - **Original-source evidence:** Source Table 3 reports wall-clock latency with a fused MoE backend.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf#page=7).
  - **Measured scope:** Source-defined end-to-end inference latency. Reading extent: selected primary PDF passages.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811) · [Details](../../paper-notes.md#tmlrwkctcxo1a9)
  - **Accelerates:** Multiscale AR serial sampling schedule.
  - **Approach:** Progressive checkerboards permit parallel positions within scales.
  - **Original-source evidence:** Original source reports single-image A100 inference time against other AR models.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2602.03811#page=6).
  - **Measured scope:** New-generator inference time. Reading extent: selected primary PDF passages.

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) · [PDF](https://arxiv.org/pdf/2511.16546) · [Details](../../paper-notes.md#variant)
  - **Accelerates:** VAR inference depth and memory.
  - **Approach:** Progressive supernet training permits scale-dependent subnet execution.
  - **Original-source evidence:** Source evaluates reduced inference resource requirements.
  - **Source location:** PDF p. 5; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2511.16546#page=5).
  - **Measured scope:** Learned depth adaptation. Reading extent: selected primary PDF passages.

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) · [Details](../../paper-notes.md#ptq4arvg)
  - **Accelerates:** AR visual predictor arithmetic.
  - **Approach:** Post-training weight/activation quantization and calibration.
  - **Original-source evidence:** Source evaluates reduced numerical precision for visual-generation inference.
  - **Source location:** PDF p. 9; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf#page=9).
  - **Measured scope:** Quantized inference resources. Reading extent: selected primary PDF passages.

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#radar)
  - **Accelerates:** VAR sparse attention plus decoded images.
  - **Approach:** Cost-constrained sparse prediction and decoder adaptation.
  - **Original-source evidence:** Original source compares image metrics and generation latency.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** Accelerated predictor plus adapted decoder. Reading extent: selected primary PDF passages.

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) · [Details](../../paper-notes.md#scan)
  - **Accelerates:** AR coarse image prediction and selected refinement.
  - **Approach:** Coarse generation followed by calibrated local refinement.
  - **Original-source evidence:** Original source compares image generation time with LlamaGen; refinement itself adds work.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://ojs.aaai.org/index.php/AAAI/article/view/37400#page=6).
  - **Measured scope:** Whole design comparison, not a speedup caused by refinement alone. Reading extent: selected primary PDF passages.

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) · [Details](../../paper-notes.md#shiftsum)
  - **Accelerates:** VAR quantized matrix computation.
  - **Approach:** Shift-and-sum value quantization with calibration resampling.
  - **Original-source evidence:** Appendix throughput table compares 8-bit variants and full precision on CPU.
  - **Source location:** PDF p. 17; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf#page=17).
  - **Measured scope:** CPU throughput, not a GPU speedup claim. Reading extent: selected primary PDF passages.

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://doi.org/10.1109/TPAMI.2026.3700227) · [PDF](https://arxiv.org/pdf/2512.07503v1) · [Details](../../paper-notes.md#sjdplus)
  - **Accelerates:** AR text-to-image Jacobi candidate reuse.
  - **Approach:** Retains high-confidence unaccepted draft states.
  - **Original-source evidence:** Source reports image inference-latency reductions.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2512.07503v1#page=1).
  - **Measured scope:** Speculative runtime. Reading extent: selected primary PDF passages.

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#sjdpac)
  - **Accelerates:** AR image Jacobi candidate generation.
  - **Approach:** Proactive drafting and adaptive continuation.
  - **Original-source evidence:** Source reports inference throughput for the revised SJD procedure.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Speculative runtime. Reading extent: selected primary PDF passages.

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26fd.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) · [Details](../../paper-notes.md#sjdsv)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Semantic subsequence verification changes the tested/committed positions.
  - **Original-source evidence:** Source reports generation acceleration.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf#page=7).
  - **Measured scope:** Runtime relevance does not certify the full-prefix preservation theorem. Reading extent: selected primary PDF passages.

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#sparvar)
  - **Accelerates:** Next-scale VAR attention.
  - **Approach:** Predicts sparse attention patterns from earlier scales.
  - **Original-source evidence:** Source reports inference latency and image/task metrics.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf#page=7).
  - **Measured scope:** Sparse attention and generation runtime. Reading extent: selected primary PDF passages.

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026). [Paper](https://doi.org/10.1145/3805622.3810814) · [PDF](https://arxiv.org/pdf/2603.01757) · [Details](../../paper-notes.md#stepvar)
  - **Accelerates:** High-resolution VAR token evaluation.
  - **Approach:** Structural and texture criteria select retained tokens.
  - **Original-source evidence:** Source evaluates inference speed of pruning.
  - **Source location:** PDF p. 10; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2603.01757#page=10).
  - **Measured scope:** VAR inference runtime. Reading extent: selected primary PDF passages.

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2602.22948) · [Details](../../paper-notes.md#toprovar)
  - **Accelerates:** VAR tokens, layers and scale computation.
  - **Approach:** Entropy-guided sparse execution.
  - **Original-source evidence:** Source reports acceleration on Infinity model configurations.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2602.22948#page=7).
  - **Measured scope:** VAR inference runtime. Reading extent: selected primary PDF passages.

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) · [Details](../../paper-notes.md#proceedings215)
  - **Accelerates:** AR generation with aligned compact visual tokens.
  - **Approach:** Causal decoder constrains tokenizer dependencies.
  - **Original-source evidence:** Original source reports faster AR sampling as well as quality.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf#page=7).
  - **Measured scope:** Efficient generator design. Reading extent: selected primary PDF passages.

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#ccfunicompress)
  - **Accelerates:** Unified-model AR image output sequences.
  - **Approach:** Token compression/decompression shortens visual generation.
  - **Original-source evidence:** Original Table 3 separately reports generation inference minutes and understanding inference minutes.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Generation timing only, not visual-understanding timing. Reading extent: selected primary PDF passages.

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/peng26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) · [Details](../../paper-notes.md#uniar)
  - **Accelerates:** Unified AR image-generation token decoding.
  - **Approach:** Channel-bitwise prediction reduces serial autoregressive steps.
  - **Original-source evidence:** Appendix Table 9 reports generation inference time, separate from training costs.
  - **Source location:** PDF p. 15; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v306/peng26k.html#page=15).
  - **Measured scope:** Image-generation latency in a unified model. Reading extent: selected primary PDF passages.

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**](https://doi.org/10.1109/hpca68181.2026.11408607) (HPCA, 2026). [Paper](https://doi.org/10.1109/hpca68181.2026.11408607) · [Details](../../paper-notes.md#varturbo)
  - **Accelerates:** VAR execution and dedicated accelerator.
  - **Approach:** Parallel decoding, token aggregation and bypass with hardware support.
  - **Original-source evidence:** Official HPCA main-track abstract reports software work reduction and accelerator measurements.
  - **Source location:** Official HPCA 2026 main-conference abstract, software/hardware co-design and result paragraphs · [Original source](https://2026.hpca-conf.org/details/hpca-2026-main-conference/53/VAR-Turbo-Unlocking-the-Potential-of-Visual-Autoregressive-Models-through-Dual-Redun).
  - **Measured scope:** Hardware co-design, not a like-for-like GPU software speedup. Reading extent: official abstract / selected original-source text.

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#ccfvibetoken)
  - **Accelerates:** Resolution-flexible AR image prior.
  - **Approach:** Resolution-agnostic 1D tokenization bounds AR sequence burden.
  - **Original-source evidence:** Source reports generation inference FLOPs across resolutions.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** Reported AR inference FLOPs, not an invented latency speedup. Reading extent: selected primary PDF passages.

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/jiang26ah.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) · [Details](../../paper-notes.md#viar)
  - **Accelerates:** Next-scale visual AR stack.
  - **Approach:** Implicit equilibrium layer with variable inference iterations.
  - **Original-source evidence:** Source reports GPU-memory savings and per-scale inference compute control.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf#page=6).
  - **Measured scope:** Memory and compute, not training-memory-only evidence. Reading extent: selected primary PDF passages.

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#vvs)
  - **Accelerates:** AR visual speculative verification.
  - **Approach:** Skips verification for selected provisional positions.
  - **Original-source evidence:** Source evaluates image generation speed.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** Skipped verification does not automatically preserve the original sampler. Reading extent: selected primary PDF passages.

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/liu26ck.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) · [Details](../../paper-notes.md#xyzflow)
  - **Accelerates:** MAR conditional-head sampling and AR teachers.
  - **Approach:** Shortcut flow modeling with multidimensional prediction.
  - **Original-source evidence:** Source explicitly evaluates autoregressive teachers and Next Shortcut Prediction.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v306/liu26ck.html#page=6).
  - **Measured scope:** Conditional-head budget, separate from generic flow-only experiments. Reading extent: selected primary PDF passages.

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD) · [Details](../../paper-notes.md#sjd)
  - **Accelerates:** AR text-to-image next-token execution.
  - **Approach:** Jacobi candidate reuse with stochastic verification.
  - **Original-source evidence:** Source reports visual AR inference-speed experiments.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf#page=8).
  - **Measured scope:** Speculative runtime. Reading extent: selected primary PDF passages.

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#xar)
  - **Accelerates:** AR image prediction units and conditional sampling.
  - **Approach:** Next-X prediction over flexible entities.
  - **Original-source evidence:** Source reports image inference efficiency and controlled generation configurations.
  - **Source location:** PDF p. 2; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=2).
  - **Measured scope:** New-generator inference. Reading extent: selected primary PDF passages.

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://arxiv.org/pdf/2411.17787) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2411.17787) · [Details](../../paper-notes.md#code)
  - **Accelerates:** Next-scale VAR computation and memory.
  - **Approach:** Large model predicts coarse scales and a smaller model refines later scales.
  - **Original-source evidence:** Source compares VAR generation time and memory with collaborative decoding.
  - **Source location:** PDF p. 2; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2411.17787#page=2).
  - **Measured scope:** Generation time and GPU memory. Reading extent: selected primary PDF passages.

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/shao25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) · [Details](../../paper-notes.md#energyar)
  - **Accelerates:** Continuous AR per-position conditional sampling.
  - **Approach:** Models continuous conditionals with score maximization instead of iterative diffusion.
  - **Original-source evidence:** Source explicitly contrasts conditional sampling efficiency with per-token diffusion.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf#page=7).
  - **Measured scope:** Conditional-head computational work. Reading extent: selected primary PDF passages.

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#dcar)
  - **Accelerates:** Hybrid masked AR text-to-image generator.
  - **Approach:** Deep-compression hybrid tokenizer reduces spatial sequence burden.
  - **Original-source evidence:** Original source explicitly reports throughput and latency against prior generators.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf#page=1).
  - **Measured scope:** New-generator throughput and latency. Reading extent: selected primary PDF passages.

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#ccfdtp)
  - **Accelerates:** Continuous MAR token prediction.
  - **Approach:** Adds denoising refinement of unmasked predictions.
  - **Original-source evidence:** Source Fig. 4 compares inference time against image quality.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf#page=8).
  - **Measured scope:** Efficient MAR generator variant. Reading extent: selected primary PDF passages.

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2412.17153v3) · [Details](../../paper-notes.md#dd1)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Distills AR sampling into a few-step flow generator.
  - **Original-source evidence:** Original source compares steady-state wall time and quality against AR teachers.
  - **Source location:** PDF p. 10; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2412.17153v3#page=10).
  - **Measured scope:** Learned replacement of AR latent sampler. Reading extent: selected primary PDF passages.

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) · [Details](../../paper-notes.md#dd2)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Conditional score distillation trains a one-step replacement.
  - **Original-source evidence:** Source reports inference speed and image quality relative to AR teachers.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf#page=1).
  - **Measured scope:** Learned replacement, not unchanged-reference execution. Reading extent: selected primary PDF passages.

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/you25d.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) · [Details](../../paper-notes.md#emigm)
  - **Accelerates:** Continuous masked image generation including MAR.
  - **Approach:** Revises masking, sampling schedule and conditional token modeling.
  - **Original-source evidence:** Source includes MAR in its formulation and reports sampling-time/quality comparisons.
  - **Source location:** PDF p. 29; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf#page=29).
  - **Measured scope:** Continuous MAR-related variant, not every discrete masked model. Reading extent: selected primary PDF passages.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.23367) · [Details](../../paper-notes.md#fastvar)
  - **Accelerates:** High-resolution next-scale token processing.
  - **Approach:** Cached token pruning forwards selected tokens and recovers omitted states.
  - **Original-source evidence:** Original source reports runtime and resolution-scaling experiments.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2503.23367#page=1).
  - **Measured scope:** VAR inference runtime. Reading extent: selected primary PDF passages.

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) · [Details](../../paper-notes.md#flexvar)
  - **Accelerates:** Next-scale generator schedule.
  - **Approach:** Ground-truth scale prediction supports variable inference-stage budgets.
  - **Original-source evidence:** Source discusses faster inference with fewer stages and reports flexible-step generation.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf#page=6).
  - **Measured scope:** New-generator stage/quality trade-off. Reading extent: selected primary PDF passages.

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) · [PDF](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) · [Details](../../paper-notes.md#freqexit)
  - **Accelerates:** VAR transformer depth at inference.
  - **Approach:** Trains frequency-aware early-exit behavior.
  - **Original-source evidence:** Source evaluates dynamic inference and computational savings.
  - **Source location:** PDF p. 25; abstract/selected method and performance passages · [Original source](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf#page=25).
  - **Measured scope:** Depth-adaptive inference. Reading extent: selected primary PDF passages.

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html) · [PDF](https://arxiv.org/pdf/2507.20454) · [Details](../../paper-notes.md#sparsevar)
  - **Accelerates:** Late-scale VAR spatial computation.
  - **Approach:** Frequency-guided token omission and recovery.
  - **Original-source evidence:** Source reports accelerated high-resolution VAR inference.
  - **Source location:** PDF p. 5; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2507.20454#page=5).
  - **Measured scope:** VAR runtime. Reading extent: selected primary PDF passages.

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#gsd)
  - **Accelerates:** AR image speculative decoding.
  - **Approach:** Groups spatially related token candidates for verification.
  - **Original-source evidence:** Source explicitly reports accelerated visual AR inference.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf#page=8).
  - **Measured scope:** Sampling runtime. Reading extent: selected primary PDF passages.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) · [Details](../../paper-notes.md#hart)
  - **Accelerates:** High-resolution AR image generator.
  - **Approach:** Discrete AR structure with a small residual diffusion module.
  - **Original-source evidence:** Original source reports throughput and MACs for the hybrid design.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf#page=1).
  - **Measured scope:** New-generator throughput and arithmetic work. Reading extent: selected primary PDF passages.

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) · [Details](../../paper-notes.md#hawk)
  - **Accelerates:** AR text-to-image speculative proposals.
  - **Approach:** Spatial-context drafting improves candidate prediction.
  - **Original-source evidence:** Source reports visual AR inference speed and drafting ablations.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf#page=1).
  - **Measured scope:** Speculative image generation runtime. Reading extent: selected primary PDF passages.

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://arxiv.org/pdf/2505.20288v1) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/zheng25i.html) · [PDF](https://arxiv.org/pdf/2505.20288v1) · [Details](../../paper-notes.md#himar)
  - **Accelerates:** Hierarchical continuous masked AR image generation.
  - **Approach:** Low-resolution pivots condition later high-resolution groups.
  - **Original-source evidence:** Source contains a speed/accuracy experiment and generation-step comparisons.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2505.20288v1#page=8).
  - **Measured scope:** New-generator sampling speed. Reading extent: selected primary PDF passages.

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://arxiv.org/pdf/2506.04421v1) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) · [PDF](https://arxiv.org/pdf/2506.04421v1) · [Details](../../paper-notes.md#hmar)
  - **Accelerates:** Hierarchical next-scale masked AR execution.
  - **Approach:** Hierarchical ordering and IO-aware block-sparse attention kernels.
  - **Original-source evidence:** Source reports inference time and inference-memory reductions against VAR.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2506.04421v1#page=1).
  - **Measured scope:** New-generator inference time and memory. Reading extent: selected primary PDF passages.

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) · [Code](https://github.com/FoundationVision/Infinity) · [Details](../../paper-notes.md#infinity)
  - **Accelerates:** High-resolution next-scale AR generation.
  - **Approach:** Bitwise prediction avoids a very large categorical classifier.
  - **Original-source evidence:** Original source reports high-resolution image generation time.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf#page=6).
  - **Measured scope:** New-generator inference, not a controlled execution-only comparison. Reading extent: selected primary PDF passages.

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) · [Details](../../paper-notes.md#lantern)
  - **Accelerates:** Visual AR speculative acceptance.
  - **Approach:** Latent-neighborhood relaxed acceptance.
  - **Original-source evidence:** Source reports sampling-speed and image-quality experiments.
  - **Source location:** PDF p. 22; abstract/selected method and performance passages · [Original source](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf#page=22).
  - **Measured scope:** Relaxed speculative runtime, not unqualified distribution equality. Reading extent: selected primary PDF passages.

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [Code](https://github.com/feihongyan1/LazyMAR) · [Details](../../paper-notes.md#lazymar)
  - **Accelerates:** MAR repeated feature computation and guidance.
  - **Approach:** Caches stable token features and branch differences.
  - **Original-source evidence:** Source reports MAR inference-time comparisons and refresh behavior.
  - **Source location:** PDF p. 5; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf#page=5).
  - **Measured scope:** MAR feature/head inference. Reading extent: selected primary PDF passages.

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) · [Details](../../paper-notes.md#scalekv)
  - **Accelerates:** Next-scale VAR KV cache.
  - **Approach:** Layer-dependent retention of scales and cache entries.
  - **Original-source evidence:** Source reports KV-memory and inference efficiency comparisons.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf#page=6).
  - **Measured scope:** KV memory and attention. Reading extent: selected primary PDF passages.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) · [Details](../../paper-notes.md#nfig)
  - **Accelerates:** Next-scale AR frequency stages.
  - **Approach:** Generates low-frequency structure before higher-frequency detail.
  - **Original-source evidence:** Source explicitly compares inference speed against VAR-d20.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf#page=7).
  - **Measured scope:** New-generator inference speed. Reading extent: selected primary PDF passages.

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34249) · [PDF](https://arxiv.org/pdf/2412.12441) · [Details](../../paper-notes.md#numericalpruning)
  - **Accelerates:** Decoder-only AR transformer parameters.
  - **Approach:** Numerical-score structured pruning.
  - **Original-source evidence:** Source explicitly evaluates both language and AR image generation; retain image results only.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://ojs.aaai.org/index.php/AAAI/article/download/34249/36404#page=7).
  - **Measured scope:** Image-model compression and inference work. Reading extent: selected primary PDF passages.

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) · [Details](../../paper-notes.md#recap)
  - **Accelerates:** MAR context-feature recomputation.
  - **Approach:** Alternates full evaluations with low-cost cached-context steps.
  - **Original-source evidence:** Source explicitly tests MAR in addition to MaskGIT and MAGE.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf#page=1).
  - **Measured scope:** Full/local evaluation timing, not interchangeable. Reading extent: selected primary PDF passages.

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) · [Code](https://github.com/ziqipang/RandAR) · [Details](../../paper-notes.md#randar)
  - **Accelerates:** Random-order AR image inference.
  - **Approach:** Position instruction tokens enable parallel decoding.
  - **Original-source evidence:** Source evaluates image sampling efficiency of parallel inference.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf#page=7).
  - **Measured scope:** New-generator inference. Reading extent: selected primary PDF passages.

- [**Randomized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#rar)
  - **Accelerates:** AR image generator execution at a quality target.
  - **Approach:** Randomized-order training yields an AR generator evaluated with KV-cached serving.
  - **Original-source evidence:** Source Table 5 compares sampling throughput using optimized inference.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=7).
  - **Measured scope:** Efficient generator comparison, not a plug-in acceleration of fixed weights. Reading extent: selected primary PDF passages.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../../paper-notes.md#spectralar)
  - **Accelerates:** AR spectral image-token generation.
  - **Approach:** Orders tokens by increasing spectral detail.
  - **Original-source evidence:** Original performance table reports measured own-method wall time with rescaled comparator times.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=6).
  - **Measured scope:** Own timing measured, comparator scaling is not a controlled speed comparison. Reading extent: selected primary PDF passages.

- [**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) · [Details](../../paper-notes.md#sjd2)
  - **Accelerates:** AR text-to-image Jacobi refinement.
  - **Approach:** Fine-tunes noisy embeddings for next-clean-token prediction.
  - **Original-source evidence:** Source reports accelerated image inference after low-cost fine-tuning.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf#page=8).
  - **Measured scope:** Jacobi inference, preparation separate. Reading extent: selected primary PDF passages.

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) · [Details](../../paper-notes.md#entropydecoding)
  - **Accelerates:** Visual AR sampling and speculation.
  - **Approach:** Entropy controls temperature and relaxed acceptance.
  - **Original-source evidence:** Source reports reduced inference cost for speculative visual generation.
  - **Source location:** PDF p. 9; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf#page=9).
  - **Measured scope:** AR inference cost. Reading extent: selected primary PDF passages.

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/he25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) · [Details](../../paper-notes.md#zipar)
  - **Accelerates:** Causal visual AR decoding.
  - **Approach:** Spatially parallel decoding with local context windows.
  - **Original-source evidence:** Source reports model-forward and generation-runtime experiments.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf#page=7).
  - **Measured scope:** Forward counts and runtime are distinct. Reading extent: selected primary PDF passages.

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024). [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [Code](https://github.com/FoundationVision/VAR) · [Details](../../paper-notes.md#var)
  - **Accelerates:** AR image generation sequence organization.
  - **Approach:** Next-scale prediction replaces raster next-token progression.
  - **Original-source evidence:** Source compares inference speed against AR baselines.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf#page=7).
  - **Measured scope:** Efficient generator design. Reading extent: selected primary PDF passages.

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) · [Details](../../paper-notes.md#efficientvqgan)
  - **Accelerates:** High-resolution AR image attention and local code generation.
  - **Approach:** Local tokenization with blockwise parallel generation.
  - **Original-source evidence:** Source compares generated-image throughput for high-resolution synthesis.
  - **Source location:** PDF p. 6; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html#page=6).
  - **Measured scope:** AR image sampling throughput. Reading extent: selected primary PDF passages.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) · [Details](../../paper-notes.md#mqvae)
  - **Accelerates:** AR image sequence redundancy.
  - **Approach:** Masks less-important regions and predicts selected/content positions with Stackformer.
  - **Original-source evidence:** Source reports faster generation and compares sampling efficiency.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf#page=8).
  - **Measured scope:** AR sampling speed. Reading extent: selected primary PDF passages.

- [**Reject Decoding via Language-Vision Models for Text-to-Image Synthesis**](https://ojs.aaai.org/index.php/AAAI/article/view/25379) (AAAI, 2023). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25379) · [Details](../../paper-notes.md#rejectdecoding)
  - **Accelerates:** Multi-path AR text-to-image search.
  - **Approach:** Tiny visual-language scorer terminates poor partial paths early.
  - **Original-source evidence:** Original abstract reports lower synthesis time for search; baseline is multi-path reranking.
  - **Source location:** Official AAAI abstract, multi-path search and time-consumption statements · [Original source](https://ojs.aaai.org/index.php/AAAI/article/view/25379).
  - **Measured scope:** Search acceleration, separate from fixed single-trajectory sampling. Reading extent: official abstract / selected original-source text.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) · [Details](../../paper-notes.md#dqvae)
  - **Accelerates:** AR image code length and decoding.
  - **Approach:** Dynamic quantization plus coarse-to-fine position/content prediction.
  - **Original-source evidence:** Original Fig. 6 compares generation speed against ViT-VQGAN on RTX-3090.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf#page=8).
  - **Measured scope:** Measured AR sampling speed. Reading extent: selected primary PDF passages.

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022). [Paper](https://iclr.cc/virtual/2022/poster/6228) · [PDF](https://arxiv.org/pdf/2110.02037) · [Details](../../paper-notes.md#ardm2022)
  - **Accelerates:** Order-agnostic AR image model evaluations.
  - **Approach:** Parallel generation under a selected network-evaluation budget.
  - **Original-source evidence:** Original Table 2 compares sequential and parallel CIFAR-10 sampling budgets.
  - **Source location:** PDF p. 7 · [Original source](https://arxiv.org/pdf/2110.02037#page=7).
  - **Measured scope:** Model-evaluation counts only, not measured wall-clock acceleration. Reading extent: selected primary PDF passages.

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022). [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) · [Details](../../paper-notes.md#rqtransformer)
  - **Accelerates:** AR image spatial sequence and depth code prediction.
  - **Approach:** Residual quantization compresses spatial maps and predicts code stacks.
  - **Original-source evidence:** Original Fig. 4 compares sampling speed by map shape and batch size.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html#page=7).
  - **Measured scope:** Measured AR sampling speed. Reading extent: selected primary PDF passages.

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021). [Paper](https://proceedings.mlr.press/v139/song21a.html) · [PDF](https://proceedings.mlr.press/v139/song21a/song21a.pdf) · [Details](../../paper-notes.md#songjacobi)
  - **Accelerates:** Deep AR image-model feedforward sampling.
  - **Approach:** Parallel nonlinear fixed-point solving.
  - **Original-source evidence:** Source includes AR image-model experiments, not only general solver theory.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v139/song21a/song21a.pdf#page=7).
  - **Measured scope:** Historical 2021 methodological visual acceleration. Reading extent: selected primary PDF passages.

## image super-resolution

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018). [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) · [Details](../../paper-notes.md#blockwise)
  - **Accelerates:** AR image super-resolution decoding.
  - **Approach:** Predicts blocks provisionally and commits the prefix validated by a scoring model.
  - **Original-source evidence:** Source evaluates image super-resolution iteration counts and wall-clock decoding speed.
  - **Source location:** PDF p. 7; abstract/selected method and performance passages · [Original source](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html#page=7).
  - **Measured scope:** Historical 2018 image super-resolution, separate from 2022–2026 additions. Reading extent: selected primary PDF passages.

## image; video

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720) · [Details](../../paper-notes.md#tmlroufnxesoco)
  - **Accelerates:** Image and video block-AR conditional diffusion.
  - **Approach:** Block-causal denoising with reusable past context.
  - **Original-source evidence:** Source Fig. 5 compares sampling time for different AR lengths.
  - **Source location:** PDF p. 10; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2412.07720#page=10).
  - **Measured scope:** Image/video sampling-time boundaries remain distinct. Reading extent: selected primary PDF passages.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2) · [Details](../../paper-notes.md#scd)
  - **Accelerates:** AR image stochastic speculative execution.
  - **Approach:** Couples proposal/verification randomness.
  - **Original-source evidence:** Source reports image and video inference gains; the two task results remain separate.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2510.24211v2#page=1).
  - **Measured scope:** No new independent exactness certification. Reading extent: selected primary PDF passages.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696) · [Details](../../paper-notes.md#nar)
  - **Accelerates:** Image and video AR position decoding.
  - **Approach:** Neighbor expansion with dimension-oriented parallel prediction heads.
  - **Original-source evidence:** Source reports image and UCF101 generation throughput.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2503.10696#page=8).
  - **Measured scope:** Image and video results remain separate. Reading extent: selected primary PDF passages.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) · [Details](../../paper-notes.md#par)
  - **Accelerates:** Image and video AR sequential decoding.
  - **Approach:** Generates spatially distant groups concurrently.
  - **Original-source evidence:** Source evaluates ImageNet and UCF101 speed and quality.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf#page=1).
  - **Measured scope:** Image/video throughput, separately. Reading extent: selected primary PDF passages.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) · [Details](../../paper-notes.md#parallelmultiscale2017)
  - **Accelerates:** Pixel AR sampling dependency depth.
  - **Approach:** Parallel multiscale density factorization.
  - **Original-source evidence:** Original source explicitly analyzes faster parallel image sampling.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf#page=8).
  - **Measured scope:** Table 4 separates ImageNet image sampling and robot-video frame sampling with different batch settings. Reading extent: selected primary PDF passages.
