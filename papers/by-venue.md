# Papers by Publication Venue

[Home](../README.md) · [By year](by-year.md) · [Search coverage](../docs/coverage.md)

Venue names identify the publication record. They do not imply a cross-paper performance comparison. Proceedings imprint years can differ from conference and online-publication years.

## AAAI

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers](https://ojs.aaai.org/index.php/AAAI/article/view/39936) | Original experiments compare cache budget and generation quality against full-cache VAR |
| 2026 | [Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation](https://ojs.aaai.org/index.php/AAAI/article/view/39489) | Source reports speed-quality experiments on visual AR generators |
| 2026 | [Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling](https://ojs.aaai.org/index.php/AAAI/article/view/39686) | Source evaluates inference cache requirements and generation behavior |
| 2026 | [MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation](https://ojs.aaai.org/index.php/AAAI/article/view/37611) | Original source reports transformer-backbone speedup |
| 2026 | [SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation](https://ojs.aaai.org/index.php/AAAI/article/view/37400) | Original source compares image generation time with LlamaGen; refinement itself adds work |
| 2025 | [Numerical Pruning for Efficient Autoregressive Models](https://ojs.aaai.org/index.php/AAAI/article/view/34249) | Source explicitly evaluates both language and AR image generation; retain image results only |
| 2023 | [Reject Decoding via Language-Vision Models for Text-to-Image Synthesis](https://ojs.aaai.org/index.php/AAAI/article/view/25379) | Original abstract reports lower synthesis time for search; baseline is multi-path reranking |

## ACM ICMR

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://doi.org/10.1145/3805622.3810814) | Source evaluates inference speed of pruning |

## ACM MM

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Learning to Expand Images for Efficient Visual Autoregressive Modeling](https://2026.acmmm.org/site/technical-programme.html) | Accepted Source reports image generation quality-efficiency comparisons |
| 2023 | [Efficiency-optimized Video Diffusion Models](https://dl.acm.org/doi/10.1145/3581783.3612406) | Denoiser FLOPs and reported model latency. The approximately 10x headline concerns arithmetic reduction. Table 9 lists 16.5 to 6.1 ms and 26.4 to 7.5 ms for two unlabeled configurations, not a 10x end-to-end video gain |

## ACM Transactions on Graphics

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Grow3D: Hierarchical Next-Scale Octree Prediction for Fast and High-Fidelity 3D Shape Generation](https://doi.org/10.1145/3820379) | Online publication: 2026-09-14. The publisher metadata assigns volume 46(1) to the 2027 print issue. Listed under the verified online year. Author abstract reports speed benefits. No original runtime table independently inspected |

## arXiv preprint arXiv:2406.06525

| Year | Paper | Scope or publication note |
|---|---|---|
| 2024 | [Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation](https://arxiv.org/abs/2406.06525) | Reference model with preprint publication status in the current record |

## BMVC

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes](https://bmvc2025.bmva.org/proceedings/1064/) | Original Table 2 reports shape sampling time; the abstract uses a different hardware setting |

## Computational Visual Media

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [Text to image generation with bidirectional Multiway Transformers](https://www.sciopen.com/article/10.26599/CVM.2025.9450377) | Related non-AR generator design. Its iteration count is not an AR speedup or a measured full-image latency ratio |
| 2024 | [A causal convolutional neural network for multi-subject motion modeling and generation](https://link.springer.com/article/10.1007/s41095-022-0307-3) | First online 30 November 2023. Volume 10, issue 1, pages 45–59 belongs to the 2024 print issue. AR motion-generation background with an absolute performance statement, not an established AR acceleration result |
| 2024 | [Generating diverse clothed 3D human animations via a generative model](https://link.springer.com/article/10.1007/s41095-022-0324-2) | Simulation-surrogate timing across CPU physics and GPU neural implementations. The reported ratios are not acceleration of an AR visual generator |

## CVPR

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html) | Original source evaluates caching on sequentially generated video segments |
| 2026 | [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html) | Equation 4 specifies autoregressive motion generation; Table 1 compares latency against a reproduced INFP baseline |
| 2026 | [CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.html) | The inspected tables report tokens, reconstruction steps and quality. A measured AR inference-cost comparison was not located |
| 2026 | [CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.html) | Source context ablation reports reduced TFLOPs and discusses lower peak memory |
| 2026 | [DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.html) | The inspected efficiency result is training FLOPs. The paper calls generation-speed improvements a future direction |
| 2026 | [EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html) | Table 3 reports generation tokens and quality. Inference runtime or FLOPs savings have not been established |
| 2026 | [FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.html) | Inspected tables concern representation length and geometric fidelity |
| 2026 | [FARMER: Flow AutoRegressive Transformer over Pixels](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) | Source reports an inference-speed intervention and sampling comparisons |
| 2026 | [FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) | Source evaluates accelerated hybrid AR inference |
| 2026 | [FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html) | Table 1 reports mesh-token throughput on H20 for Meshtron and Mesh-RFT variants with learned speculation modules |
| 2026 | [LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) | Source reports per-image time on A800 with vLLM, including AR baselines |
| 2026 | [LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) | Source reports generation acceleration and ablations |
| 2026 | [Markovian Scale Prediction: A New Era of Visual Autoregressive Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) | Source reports peak-memory reductions against full-context VAR |
| 2026 | [Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) | Source explicitly evaluates inference acceleration from MAR distillation |
| 2026 | [Multi-Scale Local Speculative Decoding for Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) | Source reports image-generation acceleration |
| 2026 | [Parallel Jacobi Decoding for Fast Autoregressive Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) | Source reports image-generation runtime acceleration |
| 2026 | [PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html) | Table 3 reports sampling seconds separately from training GPU hours |
| 2026 | [Progress by Pieces: Test-Time Scaling for Autoregressive Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Progress_by_Pieces_Test-Time_Scaling_for_Autoregressive_Image_Generation_CVPR_2026_paper.html) | Search scaling is relevant context. Fixed quality/budget AR inference savings have not been checked here |
| 2026 | [Progressive Supernet Training for Efficient Visual Autoregressive Modeling](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) | Source evaluates reduced inference resource requirements |
| 2026 | [RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) | Original source compares image metrics and generation latency |
| 2026 | [Repurposing 3D Generative Model for Autoregressive Layout Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html) | Original performance and ablation passages compare generation time |
| 2026 | [Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.html) | Table 1 reports video generation FPS; Figure 6 relates attention-window size to inference FPS |
| 2026 | [SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html) | Source reports inference throughput for the revised SJD procedure |
| 2026 | [SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) | Source reports inference latency and image/task metrics |
| 2026 | [UniCompress: Token Compression for Unified Vision-Language Understanding and Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) | Original Table 3 separately reports generation inference minutes and understanding inference minutes |
| 2026 | [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) | Source reports generation inference FLOPs across resolutions |
| 2026 | [VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) | Source evaluates image generation speed |
| 2025 | [Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) | Source compares VAR generation time and memory with collaborative decoding |
| 2025 | [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html) | Table 3 reports latency and FPS including the text encoder, diffusion model and VAE decoder |
| 2025 | [HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) | Source reports inference time and inference-memory reductions against VAR |
| 2025 | [Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) | Original source reports high-resolution image generation time |
| 2025 | [Parallelized Autoregressive Visual Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) | Source evaluates ImageNet and UCF101 speed and quality |
| 2025 | [RandAR: Decoder-only Autoregressive Visual Generation in Random Orders](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html) | Source evaluates image sampling efficiency of parallel inference |
| 2025 | [SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SoftVQ-VAE_Efficient_1-Dimensional_Continuous_Tokenizer_CVPR_2025_paper.html) | Inspected source efficiency results do not establish AR-generator acceleration |
| 2025 | [TreeMeshGPT: Artistic Mesh Generation with Autoregressive Tree Sequencing](https://openaccess.thecvf.com/content/CVPR2025/html/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.html) | Inspected source reports compression and mesh quality. An inference-cost comparison was not located |
| 2024 | [MarkovGen: Structured Prediction for Efficient Text-to-Image Generation](https://openaccess.thecvf.com/content/CVPR2024/html/Jayasumana_MarkovGen_Structured_Prediction_for_Efficient_Text-to-Image_Generation_CVPR_2024_paper.html) | Original application is Muse, not an identified AR generator |
| 2024 | [Revisiting Non-Autoregressive Transformers for Efficient Image Synthesis](https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Revisiting_Non-Autoregressive_Transformers_for_Efficient_Image_Synthesis_CVPR_2024_paper.html) | The source explicitly studies NATs, not an accelerated AR reference generator |
| 2023 | [MAGE: MAsked Generative Encoder To Unify Representation Learning and Image Synthesis](https://openaccess.thecvf.com/content/CVPR2023/html/Li_MAGE_MAsked_Generative_Encoder_To_Unify_Representation_Learning_and_Image_CVPR_2023_paper.html) | Related non-AR masked generator |
| 2023 | [MAGVLT: Masked Generative Vision-and-Language Transformer](https://openaccess.thecvf.com/content/CVPR2023/html/Kim_MAGVLT_Masked_Generative_Vision-and-Language_Transformer_CVPR_2023_paper.html) | Related masked generation, no AR acceleration experiment established |
| 2023 | [Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) | Source reports faster generation and compares sampling efficiency |
| 2023 | [Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) | Original Fig. 6 compares generation speed against ViT-VQGAN on RTX-3090 |
| 2022 | [Autoregressive Image Generation Using Residual Quantization](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) | Original Fig. 4 compares sampling speed by map shape and batch size |
| 2022 | [MaskGIT: Masked Generative Image Transformer](https://openaccess.thecvf.com/content/CVPR2022/html/Chang_MaskGIT_Masked_Generative_Image_Transformer_CVPR_2022_paper.html) | Related generation background, not labeled causal AR |
| 2021 | [Taming Transformers for High-Resolution Image Synthesis](https://openaccess.thecvf.com/content/CVPR2021/html/Esser_Taming_Transformers_for_High-Resolution_Image_Synthesis_CVPR_2021_paper.html) | Reference architecture, not admitted merely because it enables generation |
| 2018 | [The Unreasonable Effectiveness of Deep Features as a Perceptual Metric](https://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html) | Evaluation resource |

## CVPR Findings

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Depth Adaptive Efficient Visual Autoregressive Modeling](https://openaccess.thecvf.com/content/CVPR2026F/html/Li_Depth_Adaptive_Efficient_Visual_Autoregressive_Modeling_CVPRF_2026_paper.html) | Acceleration evidence is present, but the confirmed publication is CVPR Findings. Main-track CCF equivalence is not established |

## ECCV

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [ActionPlan: Future-Aware Streaming Motion Synthesis via Frame-Level Action Planning](https://link.springer.com/chapter/10.1007/978-3-032-37225-3_30) | The measured 146 ms first token and 40 ms later tokens do not by themselves establish the autoregressive conditional structure. Causal TAE and temporal activation alone are insufficient to certify the complete predictor |
| 2026 | [ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) | Original source reports inference speed comparisons and component ablations |
| 2026 | [Continuous Speculative Decoding for Autoregressive Image Generation](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_32) | Source reports wall-time comparisons with default MAR |
| 2026 | [Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_29) | Table 5 reports about 2.3 to 4.0 FPS as latent dimension changes from 768 to 64. Table 7 pure AR is about 6.0 FPS, hybrid 4.0 and pure DiT 1.9. Adding the conditional head is not faster than the pure-AR ablation |
| 2026 | [Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) | Source studies joint acceleration of the sequential AR stage and iterative decoder |
| 2026 | [EVAR: Edge Visual Autoregressive Models via Principled Pruning](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) | Source reports single-image iOS latency for pruned versus original VAR |
| 2026 | [FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis](https://link.springer.com/chapter/10.1007/978-3-032-37098-3_12) | Original source reports latency and paired/output quality for InfinityStar |
| 2026 | [GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_22) | Reported 4.2 times compares 16-frame generation with eight steps over four passes against 40 steps over one pass. Chunk sizes and solver budgets change. The five-step six-frame Table 3 timing is separate |
| 2026 | [HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) | Streaming throughput and per-chunk latency, not complete-video latency. The approximately 1.8x headline matches the throughput ratio, not the listed latency ratio |
| 2026 | [InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) | Source-reported streaming FPS with parallel execution. The 2.6 s conversational TTFF includes additional components. Neither value is a single-GPU complete-video latency |
| 2026 | [InterCMDM: Block-Causal Diffusion for Autoregressive Human Interaction Generation](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_2) | Absolute source-reported streaming measurements. A demonstrated reduction against an explicit AR inference baseline has not been established |
| 2026 | [Language-Guided Transformer Tokenizer for Human Motion Generation](https://link.springer.com/chapter/10.1007/978-3-032-37041-9_17) | Read the appendix timing and identify the evaluated generator family. Token-count reduction alone is not measured latency |
| 2026 | [LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens](https://doi.org/10.1007/978-3-032-37035-8_33) | Source reports GPU-memory and throughput measurements on image generators |
| 2026 | [LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) | Original source evaluates generation speed under a fixed drafter |
| 2026 | [Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) | Streaming FPS and time to first frame at 720x400. GPU count changes across ablations. These values are not complete conversational latency or a same-hardware speed ratio |
| 2026 | [MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_34) | Source reports acceleration against original MAR |
| 2026 | [MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://link.springer.com/chapter/10.1007/978-3-032-37356-4_14) | The measured comparison adds runtime and memory relative to the fixed-window baseline. The paper supports context retention, not a demonstrated speedup in this comparison |
| 2026 | [NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) | Source-reported layout-generation runtime curves for different complete agents. The figure does not isolate token representation from backbone or optimization changes. No numeric ratio is inferred from plotted points |
| 2026 | [OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) | Efficient learned AR generator compared with a bidirectional teacher. Full-clip runtime, time to first chunk and steady streaming FPS are distinct measurements |
| 2026 | [OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) | Reported batched image-generation timing for different trained generators. The 119.2x headline and 63% memory result concern image-conditioned text output, not image generation. Inclusion of encoding and image decoding in Table 4 timing is not explicitly established |
| 2026 | [PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](https://link.springer.com/chapter/10.1007/978-3-032-37464-6_31) | Historical KV/context storage reduction and source-reported streaming throughput. The compression factor applies to the middle-history representation, not total GPU memory or complete-video runtime |
| 2026 | [ParaFlow: Parallel Sampling for Flow Matching Models](https://link.springer.com/chapter/10.1007/978-3-032-37038-9_8) | General flow-sampling background. The source abstract does not establish application to an autoregressive visual generator |
| 2026 | [Practice Makes Perfect: From Explicit Decomposition to Reinforced Latent Planning in Text-to-Motion Generation](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_27) | Retrieve the supplementary timing configuration and compare the same workload. Cross-source explicit-CoT timing is not a controlled speedup |
| 2026 | [Recurrent Autoregressive Diffusion: Global Memory Meets Local Attention](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_27) | Training-resource comparison and added-forward-computation analysis, not measured AR generation latency reduction |
| 2026 | [ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24) | Single RTX 4090, SnapMoGen: seven stages and 0.071 s/sample versus T2M-GPT 40 stages and 0.239 s. MoMask++ reports 0.051 s. The source table does not establish that the fewest stages gives the fastest method |
| 2026 | [ShotStream: Streaming Multi-shot Video Generation for Interactive Storytelling](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_12) | Single H200 Table 1: ShotStream 15.95 FPS, Self Forcing 16.36 and LongLive 16.55. Do not report the bidirectional-to-causal throughput gain as a gain over these fast AR baselines |
| 2026 | [Soft Tail-Dropping for Adaptive Visual Tokenization](https://link.springer.com/chapter/10.1007/978-3-032-37553-7_24) | Adaptive AR token count and image quality. No measured runtime or total inference-memory saving established |
| 2026 | [Spanning Tree Autoregressive Visual Generation](https://link.springer.com/chapter/10.1007/978-3-032-36839-3_15) | Inspected source focuses generation/inpainting behavior, without verified inference-cost reduction |
| 2026 | [SSDD: Single-Step Diffusion Decoder for Efficient Image Tokenization](https://link.springer.com/chapter/10.1007/978-3-032-37556-8_19) | Inspected application uses diffusion generators. No AR application established |
| 2026 | [SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) | Complete reported shape-generation time on one RTX 4090. Text-to-3D AR comparisons use different resolutions. The headline 10x averages heterogeneous image-to-3D baselines |
| 2026 | [Surprise Forcing: What to Remember, When to Skip in Long Video Generation](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) | Component-level update/compute reduction. The complete configuration is slower than LongLive in the reported FPS table. Do not describe the 15.8% component figure as a measured end-to-end speedup |
| 2026 | [SyncCache: Exploiting Asymmetric Dynamics for Fast Audio-Driven Portrait Animation](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_34) | AR/chunk-generation dependency and actual cache lifetime across chunks require verification before core admission |
| 2026 | [TinyHistory: Lightweight Video History Embeddings Via Two-Stage Context Learning](https://link.springer.com/chapter/10.1007/978-3-032-37189-8_10) | Conditioning-token budget and output consistency. Token-count ratios are not measured speedup or total GPU-memory ratios |
| 2026 | [Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) | Peak GPU memory and the source-reported latency breakdown. Attention-only and quantized combined results remain separate |
| 2026 | [Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) | Efficient learned AR generator compared with volumetric diffusion baselines. The approximately threefold FLOPs reduction is distinct from the much smaller reported runtime difference. Task is cross-contrast MRI synthesis, not general text-to-image generation |
| 2024 | [AdaNAT: Exploring Adaptive Policy for Token-Based Image Generation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2478_ECCV_2024_paper.php) | The abstract explicitly identifies NATs as its object. No AR-generator application established here |

## Findings of EMNLP

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [Mitigating Sequential Dependencies: A Survey of Algorithms and Systems for Generation-Refinement Frameworks in Autoregressive Models](https://aclanthology.org/2025.findings-emnlp.716/) | Exact Findings track retained; no main-track CCF equivalence assumed |

## HPCA

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy](https://doi.org/10.1109/hpca68181.2026.11408607) | Official HPCA main-track abstract reports software work reduction and accelerator measurements |

## ICASSP

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Breaking Codebook Redundancy for Faster Autoregressive Image Generation with Retrieval-Augmented Speculative Decoding](https://doi.org/10.1109/icassp55912.2026.11461425) | Official ICASSP identity is established. Algorithm and cost-bearing result not yet retrieved |
| 2026 | [Enhancing Quantization for Visual Autoregressive Generation Via Uncertainty Identification](https://doi.org/10.1109/icassp55912.2026.11462147) | Official ICASSP identity is established. Quantization type and inference evidence remain unresolved |
| 2026 | [Nativetok: Native Visual Tokenization for Improved Image Generation](https://doi.org/10.1109/icassp55912.2026.11462037) | Original abstract supports representation/training improvements, not an established inference-cost result |
| 2025 | [Stable Control Visual AutoRegressive Model: Precise and Efficient Image Generation via Scale Alignment](https://doi.org/10.1109/icassp49660.2025.10890268) | Inference cost not established |

## ICCV

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | Source reports image inference efficiency and controlled generation configurations |
| 2025 | [Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Bridging_Continuous_and_Discrete_Tokens_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | Inspected source establishes representation and generation quality. No inference-cost comparison was located |
| 2025 | [DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) | Original source explicitly reports throughput and latency against prior generators |
| 2025 | [Democratizing Text-to-Image Masked Generative Models with Compact Text-Aware One-Dimensional Tokens](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_Democratizing_Text-to-Image_Masked_Generative_Models_with_Compact_Text-Aware_One-Dimensional_Tokens_ICCV_2025_paper.html) | Inspected experiments concern masked generation, not an identified AR generator |
| 2025 | [Denoising Token Prediction in Masked Autoregressive Models](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) | Source Fig. 4 compares inference time against image quality |
| 2025 | [Di[M]O: Distilling Masked Diffusion Models into One-step Generator](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_DiMO_Distilling_Masked_Diffusion_Models_into_One-step_Generator_ICCV_2025_paper.pdf) | Inspected teacher experiments concern masked diffusion generators, not an identified AR teacher |
| 2025 | [FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) | Original source reports runtime and resolution-scaling experiments |
| 2025 | [Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html) | Source reports accelerated high-resolution VAR inference |
| 2025 | [GigaTok: Scaling Visual Tokenizers to 3 Billion Parameters for Autoregressive Image Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Xiong_GigaTok_Scaling_Visual_Tokenizers_to_3_Billion_Parameters_for_Autoregressive_ICCV_2025_paper.html) | Inspected source concerns reconstruction/generation quality and training convergence, not a verified inference-cost result |
| 2025 | [Grouped Speculative Decoding for Autoregressive Image Generation](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) | Source explicitly reports accelerated visual AR inference |
| 2025 | [LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) | Source reports MAR inference-time comparisons and refresh behavior |
| 2025 | [Neighboring Autoregressive Modeling for Efficient Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) | Source reports image and UCF101 generation throughput |
| 2025 | [Randomized Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | Source Table 5 compares sampling throughput using optimized inference |
| 2025 | [Spectral Image Tokenizer](https://openaccess.thecvf.com/content/ICCV2025/html/Esteves_Spectral_Image_Tokenizer_ICCV_2025_paper.html) | Inspected source establishes tokenization and quality, not a verified AR-inference acceleration result |
| 2025 | [SpectralAR: Spectral Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | Original performance table reports measured own-method wall time with rescaled comparator times |
| 2023 | [Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) | Source compares generated-image throughput for high-resolution synthesis |
| 2023 | [Text-Conditioned Sampling Framework for Text-to-Image Generation with Masked Generative Models](https://openaccess.thecvf.com/content/ICCV2023/html/Lee_Text-Conditioned_Sampling_Framework_for_Text-to-Image_Generation_with_Masked_Generative_Models_ICCV_2023_paper.html) | No direct AR-generation application established |

## ICIC

| Year | Paper | Scope or publication note |
|---|---|---|
| 2027 | [DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) | Online 2026, proceedings imprint 2027. Publisher abstract explicitly reports inference throughput against AR and diffusion generators |

## ICLR

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Autoregressive Image Generation with Randomized Parallel Decoding](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) | Original source reports image throughput and GPU-memory comparisons for ARPG |
| 2026 | [CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration](https://iclr.cc/virtual/2026/poster/10008851) | Official source reports decoding speed and cloud-request reductions |
| 2026 | [Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8488454077cb0fd9d31772274c78115d-Abstract-Conference.html) | Original experiments report decoder acceleration and energy behavior |
| 2026 | [Flow Caching for Autoregressive Video Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/85dc8f85ff978b9c606d3b2f5b0da69a-Abstract-Conference.html) | Original experiments compare caching speed and video metrics on MAGI-1 and SkyReels-V2 |
| 2026 | [From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) | Source contains quality/latency comparisons for TensorAR |
| 2026 | [Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) | Source compares MAR generation speed and quality under the two-stage strategy |
| 2026 | [Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) | Source reports image generation latency against parallel AR baselines |
| 2026 | [Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59ad89d72559dd4ce557d56f36313724-Abstract-Conference.html) | Table 6 compares next-token prediction and masked prediction with/without cache on H20 |
| 2026 | [MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) | Controlled source experiments compare image quality under inference-compute budgets |
| 2026 | [MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) | Source evaluates reduced model complexity and inference resource requirements |
| 2026 | [NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale](https://proceedings.iclr.cc/paper_files/paper/2026/hash/974ff7b5bf08dbf9400b5d599a39c77f-Abstract-Conference.html) | Inspected source emphasizes generation capability. It does not establish a dedicated inference-acceleration intervention here |
| 2026 | [PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html) | Source evaluates reduced numerical precision for visual-generation inference |
| 2026 | [Real-Time Motion-Controllable Autoregressive Video Diffusion](https://proceedings.iclr.cc/paper_files/paper/2026/hash/71c1d6ec1f0003d8ea10bbea4291002d-Abstract-Conference.html) | Original source reports latency and real-time generation comparisons |
| 2026 | [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) | Experiments measure throughput and latency after stable execution speed is reached |
| 2026 | [SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b93c59da0d0f835907fd661d419db2-Abstract-Conference.html) | Original tables compare video latency and describe fixed-size historical state |
| 2026 | [Shift-and-Sum Quantization for Visual Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html) | Appendix throughput table compares 8-bit variants and full precision on CPU |
| 2026 | [Streaming Autoregressive Video Generation via Diagonal Distillation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d899eabc6c8fefd0d4064762aba407e2-Abstract-Conference.html) | Experiments separately measure H100 FPS and first-frame latency |
| 2026 | [ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html) | Source reports acceleration on Infinity model configurations |
| 2026 | [Towards One-step Causal Video Generation via Adversarial Self-Distillation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3ae86071c169649bff21188c536163dc-Abstract-Conference.html) | Table 1 compares one/two-step student settings and video quality |
| 2026 | [Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) | Original source reports faster AR sampling as well as quality |
| 2026 | [WeTok: Powerful Discrete Tokenization for High-Fidelity Visual Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0b2a58f2b5943b9c356f10db32073275-Abstract-Conference.html) | Reconstruction/tokenizer improvements do not establish AR inference savings |
| 2025 | [A Spark of Vision-Language Intelligence: 2-Dimensional Autoregressive Transformer for Efficient Finegrained Image Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/674ad201bc8fa74b3c9979230aa0c63b-Abstract-Conference.html) | Source emphasizes image quality at equal backbone size and sequence length. Inference-cost savings not established |
| 2025 | [Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) | Source reports visual AR inference-speed experiments |
| 2025 | [Adaptive Length Image Tokenization via Recurrent Allocation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/534ec8dfc0312d96e1c1b357304fadc2-Abstract-Conference.html) | Inspected source validates tokenization and reconstruction. AR inference-cost evidence is not established here |
| 2025 | [Autoregressive Video Generation without Vector Quantization](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html) | Original source reports video inference latency against prior video generators |
| 2025 | [Denoising Autoregressive Transformers for Scalable Text-to-Image Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ebd8a977883fd8d5bccf9575e873ce75-Abstract-Conference.html) | Inspected source proposes a generation framework. An explicit AR inference-cost reduction is not established |
| 2025 | [Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) | Original source compares steady-state wall time and quality against AR teachers |
| 2025 | [EdgeRunner: Auto-regressive Auto-encoder for Artistic Mesh Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/58e6c003c9fb3992265005ff6aef1913-Abstract-Conference.html) | Source reports its own token throughput and time by face count, without an established acceleration comparison |
| 2025 | [Fluid: Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f8e7248f3e659cfe70c6debcdae1b023-Abstract-Conference.html) | Source studies model scaling and generation quality, not an identified acceleration intervention |
| 2025 | [Halton Scheduler for Masked Generative Image Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ce29be756db03b0562204265256db075-Abstract-Conference.html) | Source applies to MaskGIT rather than an identified AR reference model |
| 2025 | [HART: Efficient Visual Generation with Hybrid Autoregressive Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) | Original source reports throughput and MACs for the hybrid design |
| 2025 | [ImageFolder: Autoregressive Image Generation with Folded Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/hash/82519a9d318f39096ea507615c61c340-Abstract-Conference.html) | Mechanism and AR use confirmed. A separate measured inference-cost comparison is still required |
| 2025 | [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d5a8e37f38a08c68162452dcba89ae9c-Abstract-Conference.html) | General multimodal generation model, not a verified inference-cost reduction in inspected material |
| 2025 | [LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) | Source reports sampling-speed and image-quality experiments |
| 2025 | [Meissonic: Revitalizing Masked Generative Transformers for Efficient High-Resolution Text-to-Image Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b7fd4aa7246ccfe46e61b52884bf1d11-Abstract-Conference.html) | Related non-AR masked generation |
| 2024 | [Language Model Beats Diffusion: Tokenizer is Key to Visual Generation](https://openreview.net/forum?id=gzqrANCF4g) | No specific AR inference-cost reduction verified in the inspected source |
| 2022 | [Autoregressive Diffusion Models](https://iclr.cc/virtual/2022/poster/6228) | Original Table 2 compares sequential and parallel CIFAR-10 sampling budgets |

## ICML

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation](https://proceedings.mlr.press/v306/li26iw.html) | Original experiment description compares one-NFE generation with four-NFE AR baselines |
| 2026 | [Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis](https://proceedings.mlr.press/v306/zhang26dq.html) | Source evaluates runtime of the token-reduction method |
| 2026 | [Autoregression with Self-Token Prediction](https://proceedings.mlr.press/v306/chen26du.html) | Source reports inference efficiency and grouped-input comparisons |
| 2026 | [Autoregressive Image Generation with Masked Bit Modeling](https://proceedings.mlr.press/v306/yu26z.html) | Source compares generation FID with image throughput |
| 2026 | [Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](https://proceedings.mlr.press/v306/zhu26bf.html) | Original Table 1 reports FPS and latency for the distilled AR generator |
| 2026 | [Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://proceedings.mlr.press/v306/chen26eu.html) | Original method specifies bounded historical token storage; experiments report FPS for long contexts |
| 2026 | [CSD: Content-aware Speculative Decoding for Efficient Image Generation](https://proceedings.mlr.press/v306/wang26gi.html) | Source evaluates inference acceleration on Lumina-mGPT and image metrics |
| 2026 | [Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression](https://proceedings.mlr.press/v306/yi26c.html) | Original source specifies compressed historical storage and reports long-video throughput |
| 2026 | [End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](https://proceedings.mlr.press/v306/chu26b.html) | Appendix reports sampling throughput and FLOPs on H100 |
| 2026 | [Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing](https://proceedings.mlr.press/v306/tong26k.html) | Source evaluates AR image generation and editing; retain generation results separately |
| 2026 | [FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://proceedings.mlr.press/v306/samuel26a.html) | Original source reports end-to-end runtime, sustained throughput and peak-memory behavior |
| 2026 | [FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models](https://proceedings.mlr.press/v306/li26go.html) | Source reports runtime evaluations of the acceleration method |
| 2026 | [Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model](https://proceedings.mlr.press/v306/ma26b.html) | Original table compares FPS and neural-function evaluations for generation variants |
| 2026 | [Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://proceedings.mlr.press/v306/lv26i.html) | Original source reports standalone and combined end-to-end speedups |
| 2026 | [Motion-Aware Caching for Efficient Autoregressive Video Generation](https://proceedings.mlr.press/v306/xu26an.html) | Original source reports inference latency and FLOPs on AR video backbones |
| 2026 | [Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation](https://proceedings.mlr.press/v306/li26gy.html) | Source Table 3 reports wall-clock latency with a fused MoE backend |
| 2026 | [Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization](https://proceedings.mlr.press/v306/xi26f.html) | Original source reports reduced KV memory with a small latency overhead |
| 2026 | [ScalingAR: Scaling Confidence for Autoregressive Image Generation](https://proceedings.mlr.press/v306/chen26fc.html) | Official abstract reports visual-token consumption. It does not by itself establish wall-clock savings |
| 2026 | [SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation](https://proceedings.mlr.press/v306/zhang26fd.html) | Source reports generation acceleration |
| 2026 | [Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation](https://proceedings.mlr.press/v306/so26a.html) | Source reports wall-clock visual AR inference gains |
| 2026 | [StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](https://proceedings.mlr.press/v306/cao26ab.html) | Table 5 reports Plain MAR at 3.56 seconds and StructMAR at 3.85 seconds. The headline 4.05x result compares StructMAR with diffusion-based MIGC, not an accelerated MAR baseline |
| 2026 | [Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification](https://proceedings.mlr.press/v306/peng26k.html) | Appendix Table 9 reports generation inference time, separate from training costs |
| 2026 | [Visual Implicit Autoregressive Modeling](https://proceedings.mlr.press/v306/jiang26ah.html) | Source reports GPU-memory savings and per-scale inference compute control |
| 2026 | [XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding](https://proceedings.mlr.press/v306/chen26dn.html) | Table 3 and efficiency experiments report step latency and actual sampling speedup on RTX 3090 |
| 2026 | [XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling](https://proceedings.mlr.press/v306/liu26ck.html) | Source explicitly evaluates autoregressive teachers and Next Shortcut Prediction |
| 2025 | [Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing](https://proceedings.mlr.press/v267/gao25m.html) | Original experiments measure video generation speed and GPU cache memory |
| 2025 | [Continuous Visual Autoregressive Generation via Score Maximization](https://proceedings.mlr.press/v267/shao25b.html) | Source explicitly contrasts conditional sampling efficiency with per-token diffusion |
| 2025 | [Effective and Efficient Masked Image Generation Models](https://proceedings.mlr.press/v267/you25d.html) | Source includes MAR in its formulation and reports sampling-time/quality comparisons |
| 2025 | [FlexTok: Resampling Images into 1D Token Sequences of Flexible Length](https://proceedings.mlr.press/v267/bachmann25a.html) | The inspected source establishes AR use and code lengths. Complete inference-cost savings were not verified |
| 2025 | [FlowAR: Scale-wise Autoregressive Image Generation Meets Flow Matching](https://proceedings.mlr.press/v267/ren25e.html) | Inspected source centers modular generation and quality. An explicit inference-cost reduction was not located |
| 2025 | [Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots](https://proceedings.mlr.press/v267/zheng25i.html) | Source contains a speed/accuracy experiment and generation-step comparisons |
| 2025 | [Masked Generative Nested Transformers with Decode Time Scaling](https://proceedings.mlr.press/v267/goyal25a.html) | Efficiency experiments are present, but the evaluated object is masked non-AR generation |
| 2025 | [ZipAR: Parallel Autoregressive Image Generation through Spatial Locality](https://proceedings.mlr.press/v267/he25b.html) | Source reports model-forward and generation-runtime experiments |
| 2023 | [Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html) | Methodological foundation. The inspected source does not establish visual-generation experiments |
| 2023 | [Muse: Text-To-Image Generation via Masked Generative Transformers](https://proceedings.mlr.press/v202/chang23b.html) | Related non-AR generator |
| 2021 | [Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving](https://proceedings.mlr.press/v139/song21a.html) | Source includes AR image-model experiments, not only general solver theory |
| 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://proceedings.mlr.press/v139/radford21a.html) | Not an AR visual-generation accelerator |
| 2020 | [Generative Pretraining From Pixels](https://proceedings.mlr.press/v119/chen20s.html) | Representation-learning objective, not visual-generation inference acceleration |
| 2018 | [Image Transformer](https://proceedings.mlr.press/v80/parmar18a.html) | Reference architecture, no separately established acceleration contribution in this review |
| 2017 | [Parallel Multiscale Autoregressive Density Estimation](https://proceedings.mlr.press/v70/reed17a.html) | Original source explicitly analyzes faster parallel image sampling |
| 2016 | [Pixel Recurrent Neural Networks](https://proceedings.mlr.press/v48/oord16.html) | Reference architecture, not an acceleration study |

## ICPR

| Year | Paper | Scope or publication note |
|---|---|---|
| 2027 | [Local Autoregression with Finite-Support Random Variables for Image Generation](https://link.springer.com/chapter/10.1007/978-3-032-31654-7_12) | Online 2026, proceedings imprint 2027. General generation method. Original abstract does not establish an inference-acceleration experiment |
| 2026 | [Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs](https://doi.org/10.1007/978-3-032-31920-3_1) | Source reports edge-GPU memory/latency trade-offs |

## IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [TMXVAR: Twin Microscaling Floating-Point Quantization for Efficient Visual Autoregressive Model Inference on FPGA](https://doi.org/10.1109/tcad.2026.3734745) | Journal identity confirmed. Original technical result has not been retrieved |

## IEEE Transactions on Image Processing

| Year | Paper | Scope or publication note |
|---|---|---|
| 2004 | [Image Quality Assessment: From Error Visibility to Structural Similarity](https://ece.uwaterloo.ca/~z70wang/publications/ssim.html) | Evaluation resource |

## IEEE Transactions on Pattern Analysis and Machine Intelligence

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) | Primary source explicitly includes LlamaGen experiments alongside diffusion models |
| 2026 | [SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation](https://doi.org/10.1109/TPAMI.2026.3700227) | Source reports image inference-latency reductions |
| 2025 | [Efficient Diffusion Models: A Comprehensive Survey From Principles to Practices](https://doi.org/10.1109/tpami.2025.3569700) | Broader diffusion scope, not a direct acceleration method |

## IISWC

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation](https://iiswc.org/iiswc2026/program.html) | Mechanism is relevant. The confirmed IISWC venue is not established under the requested CCF list |

## IJCAI

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [A Dual Stream Visual Tokenizer for LLM Image Generation](https://ijcai.org/proceedings/2025/167) | Token length and reconstruction measurements, with an additional diffusion decoding stage |

## IJCV

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Lumina-mGPT: Flexible Photorealistic Autoregressive Text-to-Image Generation](https://doi.org/10.1007/s11263-026-02795-2) | General generator. Dedicated inference-acceleration intervention not established in inspected source |
| 2026 | [SCALAR++: Efficient Controllable Generation via Scale-wise Visual Autoregressive Learning](https://doi.org/10.1007/s11263-026-02984-z) | Publisher abstract claims parameter and memory savings. Inference versus training-memory boundary needs confirmation |

## ISSCC

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [31.4 VARSA: A Visual Autoregressive Generation Accelerator Using Performance-Scalable Multi-Precision PE-LUT and Grid-Similarity Attention Compression](https://doi.org/10.1109/isscc49663.2026.11409066) | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |
| 2026 | [A 28nm 47.3TFLOPs/W 894mJ/Inference Visual Autoregressive Accelerator with Differential-Amplifier Speculation and Chain-Reaction-Like Parallel Generation](https://doi.org/10.1109/isscc49663.2026.11409075) | Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established |

## Journal of Machine Learning Research

| Year | Paper | Scope or publication note |
|---|---|---|
| 2021 | [Normalizing Flows for Probabilistic Modeling and Inference](https://jmlr.org/papers/v22/19-1028.html) | Related theoretical background, not a direct accelerator study |
| 2016 | [Neural Autoregressive Distribution Estimation](https://jmlr.org/papers/v17/16-272.html) | Historical foundation, not a visual-generation accelerator |

## Nature

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Multimodal learning with next-token prediction for large multimodal models](https://www.nature.com/articles/s41586-025-10041-x) | General multimodal model. No specific inference-acceleration contribution is established for this list |

## NeurIPS

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [CAT: Content-Adaptive Image Tokenization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/014898b821e3ce966ae1db68cb8d9966-Abstract-Conference.html) | Reported throughput gain in the abstract is explicitly training throughput |
| 2025 | [Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) | Source reports inference speed and image quality relative to AR teachers |
| 2025 | [FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) | Source discusses faster inference with fewer stages and reports flexible-step generation |
| 2025 | [FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) | Source evaluates dynamic inference and computational savings |
| 2025 | [GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization for Image Representation and Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/10831838f1cdd8fcba90188e88e7a121-Abstract-Conference.html) | Inspected source focuses representation/reconstruction and generative quality. AR inference-cost savings not established |
| 2025 | [Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) | Source reports visual AR inference speed and drafting ablations |
| 2025 | [Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression](https://papers.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html) | Source reports KV-memory and inference efficiency comparisons |
| 2025 | [NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) | Source explicitly compares inference speed against VAR-d20 |
| 2025 | [Plug-and-Play Context Feature Reuse for Efficient Masked Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html) | Source explicitly tests MAR in addition to MaskGIT and MAGE |
| 2025 | [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html) | Original experiments report first-frame latency and throughput on H100 |
| 2025 | [Single-pass Adaptive Image Tokenization for Minimum Program Search](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dc35c593e61f6df62db541b976d09dcf-Abstract-Conference.html) | Tokenizer encoding efficiency does not establish downstream AR-generation inference savings |
| 2025 | [Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html) | Source reports accelerated image inference after low-cost fine-tuning |
| 2025 | [Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) | Source reports reduced inference cost for speculative visual generation |
| 2025 | [Vision Foundation Models as Effective Visual Tokenizers for Autoregressive Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a829e299ebc1c1615ddb09e98fb6ce8-Abstract-Conference.html) | Inspected efficiency statement concerns convergence/training, not verified inference cost |
| 2025 | [When Worse is Better: Navigating the Compression Generation Trade-off In Visual Tokenization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b6425ecad28e4960cb4a622beb338ffe-Abstract-Conference.html) | The inspected compute-efficiency comparison concerns training compute scaling |
| 2024 | [An Image is Worth 32 Tokens for Reconstruction and Generation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e91bf7dfba0477554994c6d64833e9d8-Abstract-Conference.html) | Fig. 4 and Table 1 explicitly measure MaskGIT-ViT generation. Do not relabel those gains as AR inference results |
| 2024 | [Autoregressive Image Generation without Vector Quantization](https://proceedings.nips.cc/paper_files/paper/2024/hash/66e226469f20625aaebddbe47f0ca997-Abstract-Conference.html) | Retained as the reference process accelerated by MAR-specific methods |
| 2024 | [ENAT: Rethinking Spatial-temporal Interactions in Token-based Image Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a488aa1a0c00d76db8a922ef7815a786-Abstract-Conference.html) | Source explicitly frames the method as NAT; no direct AR application established |
| 2024 | [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) | Source compares inference speed against AR baselines |
| 2023 | [SpecTr: Fast Speculative Decoding via Optimal Transport](https://papers.nips.cc/paper_files/paper/2023/hash/6034a661584af6c28fd97a6f23e56c0a-Abstract-Conference.html) | Methodological background. No AR visual-generation application verified here |
| 2019 | [Generating Diverse High-Fidelity Images with VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/hash/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Abstract.html) | General representation/generation reference |
| 2018 | [Blockwise Parallel Decoding for Deep Autoregressive Models](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) | Source evaluates image super-resolution iteration counts and wall-clock decoding speed |
| 2017 | [GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium](https://papers.nips.cc/paper_files/paper/2017/hash/8a1d694707eb0fefe65871369074926d-Abstract.html) | A quality metric source, not an accelerator |
| 2017 | [Neural Discrete Representation Learning](https://proceedings.neurips.cc/paper/2017/hash/7a98af17e63a0ac09ce2e96d03992fbc-Abstract.html) | Foundation for latent AR generation |

## NeurIPS Datasets and Benchmarks

| Year | Paper | Scope or publication note |
|---|---|---|
| 2023 | [GenEval: An object-focused framework for evaluating text-to-image alignment](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a3bf71c7c63f0c3bcb7ff67c67b1e7b1-Abstract-Datasets_and_Benchmarks.html) | Evaluation resource |
| 2023 | [T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation](https://proceedings.nips.cc/paper_files/paper/2023/hash/f8ad010cdd9143dbb0e9308c093aff24-Abstract-Datasets_and_Benchmarks.html) | Evaluation resource |

## SOSP

| Year | Paper | Scope or publication note |
|---|---|---|
| 2023 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | No visual-generation application verified in this paper |

## TMLR

| Year | Paper | Scope or publication note |
|---|---|---|
| 2026 | [Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding](https://openreview.net/forum?id=xYATz9HpE7) | Source evaluates image-model inference speed |
| 2026 | [ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer](https://openreview.net/forum?id=OuFNXESoCO) | Source Fig. 5 compares sampling time for different AR lengths |
| 2026 | [Autoregressive Image Generation with Frequency Progression](https://openreview.net/forum?id=cEfd15ouQ1) | AR mechanism confirmed. Inspected version reports stages and quality, without a verified timing/FLOPs comparison |
| 2026 | [DiCoDe: Diffusion-Compressed Deep Tokens for Autoregressive Video Generation with Language Models](https://openreview.net/forum?id=B7a0IAIEXZ) | Inspected source establishes compressed tokens and training efficiency, not a comparative generation-inference cost result |
| 2026 | [Efficient High-Resolution Image Synthesis via Autoregressive Modeling in a Diffusion-Learned Continuous Latent Space](https://openreview.net/forum?id=wkNwPZ0g3G) | Formal TMLR identity is established. Primary mechanism/cost passages remain inaccessible |
| 2026 | [InfoScale: Unleashing Training-free Variable-scaled Image Generation via Effective Utilization of Information](https://openreview.net/forum?id=iB8PzxdpMf) | Primary source identifies diffusion application, not AR generation |
| 2026 | [Progressive Checkerboards for Autoregressive Multiscale Image Generation](https://openreview.net/forum?id=wkCTCXo1a9) | Original source reports single-image A100 inference time against other AR models |
| 2025 | [MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale](https://openreview.net/forum?id=fuOHI59rUW) | Original Table 3 compares asymmetric design latency and memory on A100 |
| 2024 | [MaskBit: Embedding-free Image Generation via Bit Tokens](https://openreview.net/forum?id=NYe2JuN3v3) | Related non-AR generator |
| 2022 | [Scaling Autoregressive Models for Content-Rich Text-to-Image Generation](https://openreview.net/forum?id=AFDcYJKhND) | General AR generator, not admitted simply for model capability |

## Transactions on Machine Learning Research

| Year | Paper | Scope or publication note |
|---|---|---|
| 2025 | [Autoregressive Models in Vision: A Survey](https://openreview.net/forum?id=1BqXkjNEGP) | Includes efficiency discussion, not a primary accelerator study |
| 2025 | [Efficient Diffusion Models: A Survey](https://openreview.net/forum?id=wHECkBOwyt) | Broader diffusion scope, not a direct acceleration method |
