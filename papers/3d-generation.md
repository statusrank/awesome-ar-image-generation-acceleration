# AR 3D-generation acceleration

[Home](../README.md) · [All categories](../papers/README.md) · [By year](../papers/by-year.md)

Acceleration of autoregressive 3D geometry and layout generation.

**8 papers.** Titles link to recorded PDFs or the official paper page.

## Papers

- [**FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) · [Details](paper-notes.md#flashmesh3d)
  - **Accelerates:** AR mesh token decoding.
  - **Approach:** Trained face/point/coordinate proposal blocks with structured correction and backbone verification.

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) · [Details](paper-notes.md#nalalayout)
  - **Accelerates:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Approach:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.

- [**PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) · [Details](paper-notes.md#pointnsp3d)
  - **Accelerates:** AR point-cloud sampling.
  - **Approach:** Next-scale level-of-detail prediction replaces next-point progression.

- [**Repurposing 3D Generative Model for Autoregressive Layout Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) · [Details](paper-notes.md#lavigen3d)
  - **Accelerates:** Autoregressive 3D layout generation.
  - **Approach:** Repurposes a 3D diffusion model and uses dual-guidance self-rollout distillation.

- [**ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) · [Details](paper-notes.md#scalemogenmotion)
  - **Accelerates:** Seven scale-wise AR stages for motion synthesis.
  - **Approach:** Section 3.2 conditions each skeletal-temporal scale on text and a prefix formed from completed coarser token maps. Section 4.7 specifies seven sequential scale stages. No Flow Matching head is part of the inspected next-scale bitwise-token prediction mechanism.

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Details](paper-notes.md#supervoxelgpt)
  - **Accelerates:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Approach:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.

- [**XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26dn.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) · [Details](paper-notes.md#xspecmesh3d)
  - **Accelerates:** AR mesh next-token decoding.
  - **Approach:** Multi-head proposals with backbone verification/resampling and head distillation.

- [**3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes**](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) (BMVC, 2025). [Paper](https://bmvc2025.bmva.org/proceedings/1064/) · [PDF](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) · [Details](paper-notes.md#wag3d)
  - **Accelerates:** Autoregressive shape token sampling.
  - **Approach:** Wavelet hierarchy supports next-scale generation.
