# Designing Efficient Autoregressive Generators

[Home](../../README.md) · [Categories](../README.md)

Generator design changes inference computation and its distribution across generation stages.

**83 papers.**

## 5.1 Efficient AR Predictors

- [**Autoregressive Image Generation with Linear Complexity: A Spatial-Aware Decay Perspective**](https://arxiv.org/pdf/2507.01652v2) (arXiv preprint, 2026).
  Uses recurrent linear attention with spatially aware decay for autoregressive image generation.

- [**Decoupled Scale-Wise Autoregressive Modeling for Visual Generation**](https://arxiv.org/pdf/2411.10433) (Findings of CVPR, 2026).
  Decouples bidirectional within-scale spatial attention from cross-scale conditioning through a linear-complexity Mamba module.

- [**Dynamic Mixture-of-Experts for Visual Autoregressive Model**](https://arxiv.org/pdf/2510.08629) (ICLR DeLTa Workshop, 2026).
  Uses token-dependent expert routing with scale-dependent thresholds to reduce active feed-forward computation in VAR.

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026).
  Structured pruning with scale-aware compensation and distillation.

- [**LINA: Linear Autoregressive Image Generative Models with Continuous Tokens**](https://arxiv.org/pdf/2601.22630) (arXiv preprint, 2026).
  Combines linear attention with local convolutions and bidirectional KV gating for continuous-token prediction. Reported savings concern attention FLOPs.

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026).
  Uses a state-space autoregressive predictor with measured image-generation timing. headline long-sequence gains concern text output.

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026).
  Dense-to-MoE conversion with sparse expert activation.

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026).
  Progressive supernet training permits scale-dependent subnet execution.

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026).
  Implicit equilibrium layer with variable inference iterations.

- [**ActVAR: Activating Mixtures of Weights and Tokens for Efficient Visual Autoregressive Generation**](https://arxiv.org/pdf/2511.12893) (arXiv preprint, 2025).
  Uses token-specific expert routing and gated token selection, with feature reconstruction for skipped tokens. Reported savings concern FLOPs.

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025).
  Trains frequency-aware early-exit behavior.

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025).
  Numerical-score structured pruning.

- [**Scalable Autoregressive Image Generation with Mamba**](https://arxiv.org/pdf/2408.12245v5) (arXiv preprint, 2025).
  Uses a Mamba-based image predictor with linear sequence processing and recurrent generation.

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024).
  Next-scale prediction replaces raster next-token progression.

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023).
  Combines global and local prediction with block-wise autoregressive generation to reduce sequential sampling work.

- [**Axial Attention in Multidimensional Transformers**](https://arxiv.org/pdf/1912.12180) (arXiv preprint, 2019).
  Factorizes attention across image axes and supports semi-parallel autoregressive sampling.

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018).
  Predicts blocks provisionally and commits the prefix validated by a scoring model.

## 5.2 Efficient Generation Structures and Conditioning

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026).
  Caches completed blocks under block-causal attention and samples within each block by diffusion. image and video timings are reported separately.

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026).
  Self-token prediction generates flexible token groups per step.

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026).
  Decouples position guidance and content prediction for grouped decoding.

- [**FlashAR: Efficient Post-Training Acceleration for Autoregressive Image Generation**](https://arxiv.org/pdf/2605.09430) (arXiv preprint, 2026).
  Adapts a pretrained raster-order generator for parallel horizontal and vertical prediction using an intermediate vertical branch and learned fusion.

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026).
  Spiral expansion with length-adaptive parallel decoding.

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026).
  Position query tokens and locality-aware parallel generation order.

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026).
  Allocates AR conditioning layers and iterative diffusion layers.

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Compressed history state and limited scale context.

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026).
  Restricts conditioning to adjacent scales and local neighborhoods.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026).
  Combines cross-scale conditioning with progressive checkerboard groups to reduce sequential sampling rounds.

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Next-X prediction over flexible entities.

- [**DetailFlow: 1D Coarse-to-Fine Autoregressive Image Generation via Next-Detail Prediction**](https://arxiv.org/pdf/2505.21473) (arXiv preprint, 2025).
  Organizes tokens from coarse semantic structure to finer details and uses parallel self-correction during autoregressive generation.

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025).
  Ground-truth scale prediction supports variable inference-stage budgets.

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25i/zheng25i.pdf) (ICML, 2025).
  Low-resolution pivots condition later high-resolution groups.

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  Hierarchical ordering and IO-aware block-sparse attention kernels.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Neighbor expansion with dimension-oriented parallel prediction heads.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  Generates spatially distant groups concurrently.

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025).
  Position instruction tokens enable parallel decoding.

- [**Switti: Designing Scale-Wise Transformers for Text-to-Image Synthesis**](https://arxiv.org/pdf/2412.01819v4) (arXiv preprint, 2025).
  Conditions each scale on the preceding token map and omits selected unconditional guidance evaluations during refinement.

- [**Token-Shuffle: Towards High-Resolution Image Generation with Autoregressive Models**](https://arxiv.org/pdf/2504.17789) (arXiv preprint, 2025).
  Merges neighboring token embeddings along the channel dimension to shorten the Transformer sequence, then restores spatial positions with token-unshuffle.

- [**Customize Your Visual Autoregressive Recipe with Set Autoregressive Modeling**](https://arxiv.org/pdf/2410.10511) (arXiv preprint, 2024).
  Predicts sets of image tokens conditioned on completed sets, allowing flexible group sizes and fewer sequential generation stages.

- [**E-CAR: Efficient Continuous Autoregressive Image Generation via Multistage Modeling**](https://arxiv.org/pdf/2412.14170v2) (arXiv preprint, 2024).
  Distributes a continuous flow trajectory across increasing resolutions, limiting high-resolution denoising work.

- [**Locally Hierarchical Auto-Regressive Modeling for Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2022/file/67d60c2694f4fecd18fa04d1fa8c0a5c-Paper-Conference.pdf) (NeurIPS, 2022).
  Models local code pyramids and samples fine-code groups in parallel after their coarse code is generated.

- [**PixelPyramids: Exact Inference Models from Lossless Image Pyramids**](https://openaccess.thecvf.com/content/ICCV2021/papers/Mahajan_PixelPyramids_Exact_Inference_Models_From_Lossless_Image_Pyramids_ICCV_2021_paper.pdf) (ICCV, 2021).
  Uses lossless image pyramids and local conditional dependencies to parallelize block-autoregressive pixel generation.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017).
  Uses a learned multiscale pixel-group factorization for parallel image sampling, changing the original PixelCNN dependencies.

## 5.3 Efficient Visual Representations and Reconstruction

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/content/pdf/10.1007/978-981-92-3378-6_16.pdf) (ICIC, 2026).
  Routes generation through discrete, hybrid or continuous representation paths to reduce inference cost relative to a fixed-path configuration.

- [**Autoregressive Image Generation with Frequency Progression**](https://arxiv.org/pdf/2503.05305) (TMLR, 2026).
  Generates continuous frequency groups progressively and allocates fewer inner diffusion updates to lower-frequency stages.

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026).
  Masked bit modeling supports efficient prediction of large-vocabulary image representations.

- [**BitDance: Scaling Autoregressive Generative Models with Binary Tokens**](https://arxiv.org/pdf/2602.14041) (NeurIPS, 2026, to appear).
  Combines binary visual tokens with a diffusion head and next-patch prediction to generate multiple image tokens in parallel.

- [**CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization**](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.pdf) (CVPR, 2026).
  Reconstructs images from compact autoregressive codes with a one-step MeanFlow decoder.

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026).
  Jointly trains a one-dimensional semantic tokenizer and its autoregressive generator, with sampling FLOPs and H100 throughput comparisons.

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026).
  Self-supervised dimension reduction reduces sequential sampling burden.

- [**G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation**](https://arxiv.org/pdf/2611.13004) (arXiv preprint, 2026).
  Combines spatially compressed groups of discrete codes with a semi-autoregressive head for efficient prediction within each group.

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026).
  Compact discrete tokens with latent-consistency decoding.

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026).
  Trains a tokenizer with a causal decoder for efficient autoregressive prediction. throughput comparisons concern separately trained generators.

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Shortens the main autoregressive visual sequence and expands it with a smaller autoregressive decompressor before image decoding.

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026).
  Channel-bitwise prediction reduces serial autoregressive steps.

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026).
  Uses short resolution-agnostic codes to reduce autoregressive prediction FLOPs. image reconstruction remains a separate cost.

- [**"Principal Components" Enable A New Language of Images**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_Principal_Components_Enable_A_New_Language_of_Images_ICCV_2025_paper.pdf) (ICCV, 2025).
  Learns an ordered compact semantic representation that supports autoregressive image generation with fewer token predictions.

- [**D2C: Unlocking the Potential of Continuous Autoregressive Image Generation with Discrete Tokens**](https://arxiv.org/pdf/2503.17155) (arXiv preprint, 2025).
  Uses a compact discrete autoregressive prior to condition a continuous generator, reducing the work of continuous image generation.

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025).
  Deep-compression hybrid tokenizer reduces spatial sequence burden.

- [**Democratizing Text-to-Image Masked Generative Models with Compact Text-Aware One-Dimensional Tokens**](https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_Democratizing_Text-to-Image_Masked_Generative_Models_with_Compact_Text-Aware_One-Dimensional_Tokens_ICCV_2025_paper.pdf) (ICCV, 2025).
  Its continuous TiTok configuration replaces MAR image latents with a shorter one-dimensional representation, with generator throughput measured on a single A100.

- [**FlexTok: Resampling Images into 1D Token Sequences of Flexible Length**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachmann25a/bachmann25a.pdf) (ICML, 2025).
  Uses variable-length code prefixes to control autoregressive prediction work, followed by a learned rectified-flow decoder.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025).
  Combines discrete autoregressive structure prediction with lightweight continuous residual sampling. residual sampling adds work relative to discrete-only generation.

- [**ImageFolder: Autoregressive Image Generation with Folded Tokens**](https://proceedings.iclr.cc/paper_files/paper/2025/file/82519a9d318f39096ea507615c61c340-Paper-Conference.pdf) (ICLR, 2025).
  Folds spatially aligned token streams and predicts paired codes from shared AR states, reducing inference FLOPs with latency close to VAR in the reported configuration.

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025).
  Bitwise prediction avoids a very large categorical classifier.

- [**MergeVQ: A Unified Framework for Visual Generation and Representation with Disentangled Token Merging and Quantization**](https://arxiv.org/pdf/2504.00999) (CVPR, 2025).
  Merges redundant visual latents and removes duplicate tokens from the MergeAR KV cache, retaining their positional information.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025).
  Organizes multiscale autoregressive generation from low to high frequencies. reported runtime comparisons also vary model capacity.

- [**Spectral Image Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Esteves_Spectral_Image_Tokenizer_ICCV_2025_paper.pdf) (ICCV, 2025).
  Uses spectral image codes for autoregressive generation at multiple resolutions. Reported throughput benefits depend on the requested resolution.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Uses compact spectral tokens with sequential or grouped prediction. grouped configurations trade generation time against image quality.

- [**Vision Foundation Models as Effective Visual Tokenizers for Autoregressive Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/5a829e299ebc1c1615ddb09e98fb6ce8-Paper-Conference.pdf) (NeurIPS, 2025).
  Uses region-adaptive quantization of foundation-model features to reduce AR token count and supports generation without classifier-free guidance.

- [**When Worse is Better: Navigating the Compression Generation Trade-off In Visual Tokenization**](https://proceedings.neurips.cc/paper_files/paper/2025/file/b6425ecad28e4960cb4a622beb338ffe-Paper-Conference.pdf) (NeurIPS, 2025).
  Regularizes tokenization with an autoregressive prediction objective, enabling comparable generation quality with fewer tokens and a smaller predictor.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023).
  Omits redundant region codes, predicts retained codes and positions, and restores dense features before image decoding.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023).
  Allocates variable-length codes across image regions and predicts their positions and contents to reduce autoregressive sampling cost.

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022).
  Reduces the spatial code grid through residual quantization and predicts code stacks. reported sampling times exclude image decoding.

- [**Anytime Sampling for Autoregressive Models via Ordered Autoencoding**](https://arxiv.org/pdf/2102.11495) (ICLR, 2021).
  Orders latent dimensions by reconstruction importance so AR sampling can stop before all codes are generated.

## 5.4 Learned Sampling Acceleration

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026).
  Entropy-guided speculation and one-step drifting decoder.

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026).
  Distills a faster sampler while retaining a masked AR generation organization.

- [**ARINAR: Bi-Level Autoregressive Feature-by-Feature Generative Models**](https://arxiv.org/pdf/2503.02883) (arXiv preprint, 2025).
  Generates continuous token features through inner autoregression with Gaussian-mixture conditionals.

- [**Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Bridging_Continuous_and_Discrete_Tokens_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Combines dimension-wise quantization with a lightweight autoregressive head, avoiding a single large-vocabulary categorical prediction.

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025).
  Models continuous conditionals with score maximization instead of iterative diffusion.

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025).
  Distills AR sampling into a few-step flow generator.

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025).
  Conditional score distillation trains a one-step replacement.

- [**Fast Autoregressive Models for Continuous Latent Generation**](https://arxiv.org/pdf/2504.18391) (arXiv preprint, 2025).
  Replaces the iterative conditional sampler in masked autoregressive generation with a learned few-step shortcut sampler.

## 6 Cross-Method Evidence and Practical Trade-offs

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models through Dual Redundancy**](https://doi.org/10.1109/HPCA68181.2026.11408607) (HPCA, 2026).
  Combines software and hardware optimizations to exploit computational redundancy in visual autoregressive inference.

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) (CVPR, 2025).
  Large model predicts coarse scales and a smaller model refines later scales.


## License

[CC BY 4.0](../../LICENSE.md). Linked papers retain their original licenses.
