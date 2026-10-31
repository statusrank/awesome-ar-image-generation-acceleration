# Evaluation Notes

[Home](../README.md) · [Evaluation papers](../papers/evaluation.md)

| Question | Information needed |
|---|---|
| Is image generation faster? | A specified reference and timing boundary, including the treatment of image decoding |
| Can the system process more images? | Throughput at a stated batch size and workload |
| Does it require less memory? | Peak allocation at an identified device or system boundary |
| How do the generated images perform? | The dataset, task and image-quality metric |
| How close are paired outputs? | The pairing procedure and reference-similarity metric |
| Is a sampling distribution preserved? | The reference sampling law, probability space and mathematical assumptions |

The model checkpoint and image resolution affect runtime. Precision and batching also affect execution. Compare configurations within a study before attempting comparisons across studies.

A high acceptance rate does not identify the distribution of an entire committed continuation. The verification and correction rules determine that transition. FID or a task score cannot replace a sampling-law argument.

Training or calibration needed before inference is a separate cost. Replacing a generator may require an image-level comparison when its latent representation differs from the reference.
