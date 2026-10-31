# Image Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [Mechanisms](../../README.md)

**105 acceleration papers.**

## image

<a id="paper-dynamicvar"></a>

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) (ICIC, 2027). [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16)
  - **Focus:** High-resolution AR token-path computation.
  - **Mechanism:** Routes samples among discrete/hybrid/continuous representation paths.
  - **Source:** [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16), Publisher abstract, inference-throughput statement.

<a id="paper-tmlrxyatz9hpe7"></a>

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026). [Paper](https://openreview.net/forum?id=xYATz9HpE7) · [PDF](https://arxiv.org/pdf/2505.24791)
  - **Focus:** Image generation by autoregressive normalizing flows.
  - **Mechanism:** Selective Jacobi iterations parallelize sequential flow inversions.
  - **Source:** [Paper](https://arxiv.org/pdf/2505.24791#page=9), PDF p. 9.

<a id="paper-nova"></a>

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26dq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf)
  - **Focus:** Next-scale visual AR token processing.
  - **Mechanism:** Entropy-guided adaptive token reduction and cached residual reuse.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf#page=1), PDF p. 1.

<a id="paper-amskv"></a>

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39936) · [PDF](https://arxiv.org/pdf/2511.16047)
  - **Focus:** Next-scale VAR KV memory and attention.
  - **Mechanism:** Retains condensed and local scales with adaptive cache allocation.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/39936/43897#page=7), PDF p. 7.

<a id="paper-coolsd"></a>

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39489) · [PDF](https://arxiv.org/pdf/2601.09212)
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Anneals relaxed acceptance with a specified resampling distribution.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/39489/43450#page=7), PDF p. 7.

<a id="paper-arvar"></a>

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf)
  - **Focus:** HART and Infinity next-scale inference.
  - **Mechanism:** Uses earlier attention for token selection and removes a late guidance branch.
  - **Source:** [Paper](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf#page=14), PDF p. 14.

<a id="paper-sar"></a>

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26du.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf)
  - **Focus:** Grouped AR image generation.
  - **Mechanism:** Self-token prediction generates flexible token groups per step.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf#page=5), PDF p. 5.

<a id="paper-barmbm"></a>

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yu26z.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf)
  - **Focus:** Bitwise AR image generation.
  - **Mechanism:** Masked bit modeling supports efficient prediction of large-vocabulary image representations.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf#page=7), PDF p. 7.

<a id="paper-arpg"></a>

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf)
  - **Focus:** Random-order AR image decoding.
  - **Mechanism:** Decouples position guidance and content prediction for grouped decoding.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf#page=14), PDF p. 14.

<a id="paper-ciar"></a>

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1)
  - **Focus:** Cloud-device AR image decoding.
  - **Mechanism:** On-device interval verification reduces cloud verification calls.
  - **Source:** [Paper](https://arxiv.org/pdf/2603.25463v1#page=7), PDF p. 7.

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

<a id="paper-driftar"></a>

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) · [PDF](https://arxiv.org/pdf/2603.28049)
  - **Focus:** Hybrid AR prediction and iterative visual decoding.
  - **Mechanism:** Entropy-guided speculation and one-step drifting decoder.
  - **Source:** [Paper](https://arxiv.org/pdf/2603.28049#page=13), PDF p. 13.

<a id="paper-varcompressor"></a>

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR, 2026). [Paper](https://doi.org/10.1007/978-3-032-31920-3_1) · [PDF](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf)
  - **Focus:** 8B bitwise AR image generation on edge GPUs.
  - **Mechanism:** Compresses inference memory for deployment.
  - **Source:** [Paper](https://doi.org/10.1007/978-3-032-31920-3_1#page=11), PDF p. 11.

<a id="paper-ccfsemantic1d"></a>

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chu26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf)
  - **Focus:** AR prior over 1D image tokens.
  - **Mechanism:** Jointly learns semantic 1D representation and AR generation.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf#page=13), PDF p. 13.

<a id="paper-sparsear"></a>

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/tong26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf)
  - **Focus:** AR image KV attention.
  - **Mechanism:** Entropy-aware cache sparsification.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf#page=1), PDF p. 1.

<a id="paper-evar"></a>

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf)
  - **Focus:** Next-scale VAR parameter and execution cost.
  - **Mechanism:** Structured pruning with scale-aware compensation and distillation.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf#page=1), PDF p. 1.

<a id="paper-farmer"></a>

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf)
  - **Focus:** Pixel-level autoregressive normalizing-flow sampling.
  - **Mechanism:** Self-supervised dimension reduction reduces sequential sampling burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf#page=8), PDF p. 8.

<a id="paper-fastervar"></a>

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26go.html) · [PDF](https://arxiv.org/pdf/2512.16483)
  - **Focus:** Late-scale VAR execution.
  - **Mechanism:** Adaptive stage selection and reduced computation at costly scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2512.16483#page=18), PDF p. 18.

<a id="paper-fasthybrid"></a>

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf)
  - **Focus:** Hybrid AR image generator with diffusion decoder.
  - **Mechanism:** Lookahead and guided decoding reduce hybrid generation computation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-ccfpredictionrefinement"></a>

- [**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf)
  - **Focus:** Causal AR image prediction unit.
  - **Mechanism:** Predicts overlapping tensors to refine previous discrete outputs.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-gtr"></a>

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf)
  - **Focus:** MAR stages and inner sampling budget.
  - **Mechanism:** Separates structure generation and detail reconstruction with frequency-weighted selection.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-hack"></a>

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39686) · [PDF](https://arxiv.org/pdf/2504.09261)
  - **Focus:** VAR historical KV storage.
  - **Mechanism:** Head-dependent cache compression.
  - **Source:** [Paper](https://arxiv.org/pdf/2504.09261#page=1), PDF p. 1.

<a id="paper-core2reviewcandidate"></a>

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1)
  - **Focus:** LlamaGen guidance computation.
  - **Mechanism:** Weak-model training supports guidance and later replacement of expensive computation.
  - **Source:** [Paper](https://arxiv.org/pdf/2503.09662v1#page=16), PDF p. 16.

<a id="paper-lactokgen"></a>

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf)
  - **Focus:** High-resolution AR prior plus image reconstruction.
  - **Mechanism:** Compact discrete tokens with latent-consistency decoding.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-lazyvar"></a>

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf)
  - **Focus:** VAR token processing and scale schedule.
  - **Mechanism:** Scale-dependent token pruning plus grouped scale decoding.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf#page=8), PDF p. 8.

<a id="paper-ear"></a>

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026). [Paper](https://2026.acmmm.org/site/technical-programme.html) · [PDF](https://arxiv.org/pdf/2511.15499v1)
  - **Focus:** AR image generation order and parallel groups.
  - **Mechanism:** Spiral expansion with length-adaptive parallel decoding.
  - **Source:** [Paper](https://arxiv.org/pdf/2511.15499v1#page=11), PDF p. 11.

<a id="paper-linear"></a>

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026). [Paper](https://doi.org/10.1007/978-3-032-37035-8_33) · [PDF](https://arxiv.org/pdf/2512.04857v1)
  - **Focus:** Causal visual AR KV storage.
  - **Mechanism:** Progressively evicts historical lines outside retained dependency regions.
  - **Source:** [Paper](https://arxiv.org/pdf/2512.04857v1#page=1), PDF p. 1.

<a id="paper-lisa"></a>

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf)
  - **Focus:** Visual AR speculative verification.
  - **Mechanism:** Locality-informed verifier modifies acceptance behavior.
  - **Source:** [Paper](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf#page=13), PDF p. 13.

<a id="paper-lpd"></a>

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2507.01957v2)
  - **Focus:** AR position grouping and inference schedule.
  - **Mechanism:** Position query tokens and locality-aware parallel generation order.
  - **Source:** [Paper](https://arxiv.org/pdf/2507.01957v2#page=24), PDF p. 24.

<a id="paper-madformer"></a>

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
  - **Focus:** AR/diffusion hybrid block computation.
  - **Mechanism:** Allocates AR conditioning layers and iterative diffusion layers.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-marche"></a>

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_34) · [PDF](https://arxiv.org/pdf/2506.12035)
  - **Focus:** MAR attention and feed-forward recomputation.
  - **Mechanism:** Cache-aware attention and selective KV refresh.
  - **Source:** [Paper](https://arxiv.org/pdf/2506.12035#page=1), PDF p. 1.

<a id="paper-markovvar"></a>

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf)
  - **Focus:** VAR historical context and memory.
  - **Mechanism:** Compressed history state and limited scale context.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf#page=7), PDF p. 7.

<a id="paper-marval"></a>

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf)
  - **Focus:** MAR iterative conditional sampling.
  - **Mechanism:** Distills a faster sampler while retaining a masked AR generation organization.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf#page=7), PDF p. 7.

<a id="paper-moss"></a>

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37611) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573)
  - **Focus:** High-resolution next-scale transformer execution.
  - **Mechanism:** Mixes scale work and dispatches late refinement selectively.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573#page=7), PDF p. 7.

<a id="paper-mulosd"></a>

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf)
  - **Focus:** High-resolution AR image speculative generation.
  - **Mechanism:** Low-resolution proposals with upsampling and spatially local verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-mvar"></a>

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf)
  - **Focus:** VAR spatial and scale context.
  - **Mechanism:** Restricts conditioning to adjacent scales and local neighborhoods.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-omnimamba"></a>

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf)
  - **Focus:** Autoregressive image-token prediction with a Mamba-2 state-space backbone.
  - **Mechanism:** Train a unified next-token image/text generator with Mamba-2 and modality-specific vocabularies and adapters.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf), PDF pp. 3, 12–13, Section 4.5 and Table 4.

<a id="paper-pjd"></a>

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf)
  - **Focus:** AR image Jacobi candidate refinement.
  - **Mechanism:** Spatial parallel drafts with adaptive attention masks.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-prismmoe"></a>

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26gy.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf)
  - **Focus:** Dense visual AR predictor computation.
  - **Mechanism:** Dense-to-MoE conversion with sparse expert activation.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf#page=7), PDF p. 7.

<a id="paper-tmlrwkctcxo1a9"></a>

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811)
  - **Focus:** Multiscale AR serial sampling schedule.
  - **Mechanism:** Progressive checkerboards permit parallel positions within scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2602.03811#page=6), PDF p. 6.

<a id="paper-variant"></a>

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) · [PDF](https://arxiv.org/pdf/2511.16546)
  - **Focus:** VAR inference depth and memory.
  - **Mechanism:** Progressive supernet training permits scale-dependent subnet execution.
  - **Source:** [Paper](https://arxiv.org/pdf/2511.16546#page=5), PDF p. 5.

<a id="paper-ptq4arvg"></a>

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf)
  - **Focus:** AR visual predictor arithmetic.
  - **Mechanism:** Post-training weight/activation quantization and calibration.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf#page=9), PDF p. 9.

<a id="paper-radar"></a>

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf)
  - **Focus:** VAR sparse attention plus decoded images.
  - **Mechanism:** Cost-constrained sparse prediction and decoder adaptation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-scan"></a>

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362)
  - **Focus:** AR coarse image prediction and selected refinement.
  - **Mechanism:** Coarse generation followed by calibrated local refinement.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400#page=6), PDF p. 6.

<a id="paper-shiftsum"></a>

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf)
  - **Focus:** VAR quantized matrix computation.
  - **Mechanism:** Shift-and-sum value quantization with calibration resampling.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf#page=17), PDF p. 17.

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

<a id="paper-sjdsv"></a>

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26fd.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf)
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Semantic subsequence verification changes the tested/committed positions.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf#page=7), PDF p. 7.

<a id="paper-sparvar"></a>

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf)
  - **Focus:** Next-scale VAR attention.
  - **Mechanism:** Predicts sparse attention patterns from earlier scales.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf#page=7), PDF p. 7.

<a id="paper-stepvar"></a>

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026). [Paper](https://doi.org/10.1145/3805622.3810814) · [PDF](https://arxiv.org/pdf/2603.01757)
  - **Focus:** High-resolution VAR token evaluation.
  - **Mechanism:** Structural and texture criteria select retained tokens.
  - **Source:** [Paper](https://arxiv.org/pdf/2603.01757#page=10), PDF p. 10.

<a id="paper-toprovar"></a>

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2602.22948)
  - **Focus:** VAR tokens, layers and scale computation.
  - **Mechanism:** Entropy-guided sparse execution.
  - **Source:** [Paper](https://arxiv.org/pdf/2602.22948#page=7), PDF p. 7.

<a id="paper-proceedings215"></a>

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf)
  - **Focus:** AR generation with aligned compact visual tokens.
  - **Mechanism:** Causal decoder constrains tokenizer dependencies.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-ccfunicompress"></a>

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf)
  - **Focus:** Unified-model AR image output sequences.
  - **Mechanism:** Token compression/decompression shortens visual generation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-uniar"></a>

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/peng26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf)
  - **Focus:** Unified AR image-generation token decoding.
  - **Mechanism:** Channel-bitwise prediction reduces serial autoregressive steps.
  - **Source:** [Paper](https://proceedings.mlr.press/v306/peng26k.html#page=15), PDF p. 15.

<a id="paper-varturbo"></a>

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**](https://doi.org/10.1109/hpca68181.2026.11408607) (HPCA, 2026). [Paper](https://doi.org/10.1109/hpca68181.2026.11408607)
  - **Focus:** VAR execution and dedicated accelerator.
  - **Mechanism:** Parallel decoding, token aggregation and bypass with hardware support.
  - **Source:** [Paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/53/VAR-Turbo-Unlocking-the-Potential-of-Visual-Autoregressive-Models-through-Dual-Redun), Official HPCA 2026 main-conference abstract, software/hardware co-design and result paragraphs.

<a id="paper-ccfvibetoken"></a>

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf)
  - **Focus:** Resolution-flexible AR image prior.
  - **Mechanism:** Resolution-agnostic 1D tokenization bounds AR sequence burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-viar"></a>

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/jiang26ah.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf)
  - **Focus:** Next-scale visual AR stack.
  - **Mechanism:** Implicit equilibrium layer with variable inference iterations.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf#page=6), PDF p. 6.

<a id="paper-vvs"></a>

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf)
  - **Focus:** AR visual speculative verification.
  - **Mechanism:** Skips verification for selected provisional positions.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-xyzflow"></a>

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/liu26ck.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf)
  - **Focus:** MAR conditional-head sampling and AR teachers.
  - **Mechanism:** Shortcut flow modeling with multidimensional prediction.
  - **Source:** [Paper](https://proceedings.mlr.press/v306/liu26ck.html#page=6), PDF p. 6.

<a id="paper-sjd"></a>

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD)
  - **Focus:** AR text-to-image next-token execution.
  - **Mechanism:** Jacobi candidate reuse with stochastic verification.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf#page=8), PDF p. 8.

<a id="paper-xar"></a>

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image prediction units and conditional sampling.
  - **Mechanism:** Next-X prediction over flexible entities.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=2), PDF p. 2.

<a id="paper-code"></a>

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://arxiv.org/pdf/2411.17787) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2411.17787)
  - **Focus:** Next-scale VAR computation and memory.
  - **Mechanism:** Large model predicts coarse scales and a smaller model refines later scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2411.17787#page=2), PDF p. 2.

<a id="paper-energyar"></a>

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/shao25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf)
  - **Focus:** Continuous AR per-position conditional sampling.
  - **Mechanism:** Models continuous conditionals with score maximization instead of iterative diffusion.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf#page=7), PDF p. 7.

<a id="paper-dcar"></a>

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf)
  - **Focus:** Hybrid masked AR text-to-image generator.
  - **Mechanism:** Deep-compression hybrid tokenizer reduces spatial sequence burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf#page=1), PDF p. 1.

<a id="paper-ccfdtp"></a>

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf)
  - **Focus:** Continuous MAR token prediction.
  - **Mechanism:** Adds denoising refinement of unmasked predictions.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf#page=8), PDF p. 8.

<a id="paper-dd1"></a>

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2412.17153v3)
  - **Focus:** Complete VAR and LlamaGen latent generation.
  - **Mechanism:** Distills AR sampling into a few-step flow generator.
  - **Source:** [Paper](https://arxiv.org/pdf/2412.17153v3#page=10), PDF p. 10.

<a id="paper-dd2"></a>

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf)
  - **Focus:** Complete VAR and LlamaGen latent generation.
  - **Mechanism:** Conditional score distillation trains a one-step replacement.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf#page=1), PDF p. 1.

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

<a id="paper-flexvar"></a>

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf)
  - **Focus:** Next-scale generator schedule.
  - **Mechanism:** Ground-truth scale prediction supports variable inference-stage budgets.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-freqexit"></a>

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) · [PDF](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf)
  - **Focus:** VAR transformer depth at inference.
  - **Mechanism:** Trains frequency-aware early-exit behavior.
  - **Source:** [Paper](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf#page=25), PDF p. 25.

<a id="paper-sparsevar"></a>

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html) · [PDF](https://arxiv.org/pdf/2507.20454)
  - **Focus:** Late-scale VAR spatial computation.
  - **Mechanism:** Frequency-guided token omission and recovery.
  - **Source:** [Paper](https://arxiv.org/pdf/2507.20454#page=5), PDF p. 5.

<a id="paper-gsd"></a>

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image speculative decoding.
  - **Mechanism:** Groups spatially related token candidates for verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf#page=8), PDF p. 8.

<a id="paper-hart"></a>

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf)
  - **Focus:** High-resolution AR image generator.
  - **Mechanism:** Discrete AR structure with a small residual diffusion module.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-hawk"></a>

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf)
  - **Focus:** AR text-to-image speculative proposals.
  - **Mechanism:** Spatial-context drafting improves candidate prediction.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-himar"></a>

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://arxiv.org/pdf/2505.20288v1) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/zheng25i.html) · [PDF](https://arxiv.org/pdf/2505.20288v1)
  - **Focus:** Hierarchical continuous masked AR image generation.
  - **Mechanism:** Low-resolution pivots condition later high-resolution groups.
  - **Source:** [Paper](https://arxiv.org/pdf/2505.20288v1#page=8), PDF p. 8.

<a id="paper-hmar"></a>

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://arxiv.org/pdf/2506.04421v1) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) · [PDF](https://arxiv.org/pdf/2506.04421v1)
  - **Focus:** Hierarchical next-scale masked AR execution.
  - **Mechanism:** Hierarchical ordering and IO-aware block-sparse attention kernels.
  - **Source:** [Paper](https://arxiv.org/pdf/2506.04421v1#page=1), PDF p. 1.

<a id="paper-infinity"></a>

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) · [Code](https://github.com/FoundationVision/Infinity)
  - **Focus:** High-resolution next-scale AR generation.
  - **Mechanism:** Bitwise prediction avoids a very large categorical classifier.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf#page=6), PDF p. 6.

<a id="paper-lantern"></a>

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf)
  - **Focus:** Visual AR speculative acceptance.
  - **Mechanism:** Latent-neighborhood relaxed acceptance.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf#page=22), PDF p. 22.

<a id="paper-lazymar"></a>

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [Code](https://github.com/feihongyan1/LazyMAR)
  - **Focus:** MAR repeated feature computation and guidance.
  - **Mechanism:** Caches stable token features and branch differences.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf#page=5), PDF p. 5.

<a id="paper-scalekv"></a>

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf)
  - **Focus:** Next-scale VAR KV cache.
  - **Mechanism:** Layer-dependent retention of scales and cache entries.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-nfig"></a>

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf)
  - **Focus:** Next-scale AR frequency stages.
  - **Mechanism:** Generates low-frequency structure before higher-frequency detail.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-numericalpruning"></a>

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34249) · [PDF](https://arxiv.org/pdf/2412.12441)
  - **Focus:** Decoder-only AR transformer parameters.
  - **Mechanism:** Numerical-score structured pruning.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/34249/36404#page=7), PDF p. 7.

<a id="paper-recap"></a>

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf)
  - **Focus:** MAR context-feature recomputation.
  - **Mechanism:** Alternates full evaluations with low-cost cached-context steps.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-randar"></a>

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) · [Code](https://github.com/ziqipang/RandAR)
  - **Focus:** Random-order AR image inference.
  - **Mechanism:** Position instruction tokens enable parallel decoding.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf#page=7), PDF p. 7.

<a id="paper-rar"></a>

- [**Randomized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image generator execution at a quality target.
  - **Mechanism:** Randomized-order training yields an AR generator evaluated with KV-cached serving.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=7), PDF p. 7.

<a id="paper-spectralar"></a>

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR spectral image-token generation.
  - **Mechanism:** Orders tokens by increasing spectral detail.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=6), PDF p. 6.

<a id="paper-sjd2"></a>

- [**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf)
  - **Focus:** AR text-to-image Jacobi refinement.
  - **Mechanism:** Fine-tunes noisy embeddings for next-clean-token prediction.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf#page=8), PDF p. 8.

<a id="paper-entropydecoding"></a>

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf)
  - **Focus:** Visual AR sampling and speculation.
  - **Mechanism:** Entropy controls temperature and relaxed acceptance.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf#page=9), PDF p. 9.

<a id="paper-zipar"></a>

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/he25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf)
  - **Focus:** Causal visual AR decoding.
  - **Mechanism:** Spatially parallel decoding with local context windows.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf#page=7), PDF p. 7.

<a id="paper-var"></a>

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024). [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [Code](https://github.com/FoundationVision/VAR)
  - **Focus:** AR image generation sequence organization.
  - **Mechanism:** Next-scale prediction replaces raster next-token progression.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-efficientvqgan"></a>

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf)
  - **Focus:** High-resolution AR image attention and local code generation.
  - **Mechanism:** Local tokenization with blockwise parallel generation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html#page=6), PDF p. 6.

<a id="paper-mqvae"></a>

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf)
  - **Focus:** AR image sequence redundancy.
  - **Mechanism:** Masks less-important regions and predicts selected/content positions with Stackformer.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf#page=8), PDF p. 8.

<a id="paper-rejectdecoding"></a>

- [**Reject Decoding via Language-Vision Models for Text-to-Image Synthesis**](https://ojs.aaai.org/index.php/AAAI/article/view/25379) (AAAI, 2023). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25379)
  - **Focus:** Multi-path AR text-to-image search.
  - **Mechanism:** Tiny visual-language scorer terminates poor partial paths early.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25379), Official AAAI abstract, multi-path search and time-consumption statements.

<a id="paper-dqvae"></a>

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf)
  - **Focus:** AR image code length and decoding.
  - **Mechanism:** Dynamic quantization plus coarse-to-fine position/content prediction.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf#page=8), PDF p. 8.

<a id="paper-ardm2022"></a>

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022). [Paper](https://iclr.cc/virtual/2022/poster/6228) · [PDF](https://arxiv.org/pdf/2110.02037)
  - **Focus:** Order-agnostic AR image model evaluations.
  - **Mechanism:** Parallel generation under a selected network-evaluation budget.
  - **Source:** [Paper](https://arxiv.org/pdf/2110.02037#page=7), PDF p. 7.

<a id="paper-rqtransformer"></a>

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022). [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf)
  - **Focus:** AR image spatial sequence and depth code prediction.
  - **Mechanism:** Residual quantization compresses spatial maps and predicts code stacks.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html#page=7), PDF p. 7.

<a id="paper-songjacobi"></a>

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021). [Paper](https://proceedings.mlr.press/v139/song21a.html) · [PDF](https://proceedings.mlr.press/v139/song21a/song21a.pdf)
  - **Focus:** Deep AR image-model feedforward sampling.
  - **Mechanism:** Parallel nonlinear fixed-point solving.
  - **Source:** [Paper](https://proceedings.mlr.press/v139/song21a/song21a.pdf#page=7), PDF p. 7.

## image super-resolution

<a id="paper-blockwise"></a>

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018). [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf)
  - **Focus:** AR image super-resolution decoding.
  - **Mechanism:** Predicts blocks provisionally and commits the prefix validated by a scoring model.
  - **Source:** [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html#page=7), PDF p. 7.

## image; video

<a id="paper-tmlroufnxesoco"></a>

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720)
  - **Focus:** Image and video block-AR conditional diffusion.
  - **Mechanism:** Block-causal denoising with reusable past context.
  - **Source:** [Paper](https://arxiv.org/pdf/2412.07720#page=10), PDF p. 10.

<a id="paper-scd"></a>

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2)
  - **Focus:** AR image stochastic speculative execution.
  - **Mechanism:** Couples proposal/verification randomness.
  - **Source:** [Paper](https://arxiv.org/pdf/2510.24211v2#page=1), PDF p. 1.

<a id="paper-nar"></a>

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696)
  - **Focus:** Image and video AR position decoding.
  - **Mechanism:** Neighbor expansion with dimension-oriented parallel prediction heads.
  - **Source:** [Paper](https://arxiv.org/pdf/2503.10696#page=8), PDF p. 8.

<a id="paper-par"></a>

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf)
  - **Focus:** Image and video AR sequential decoding.
  - **Mechanism:** Generates spatially distant groups concurrently.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf#page=1), PDF p. 1.

<a id="paper-parallelmultiscale2017"></a>

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf)
  - **Focus:** Pixel AR sampling dependency depth.
  - **Mechanism:** Parallel multiscale density factorization.
  - **Source:** [Paper](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf#page=8), PDF p. 8.
