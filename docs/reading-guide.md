# Reading Guide

[Home](../README.md) · [Paper catalog](../papers/README.md)

## Generation before acceleration

Read [LlamaGen](https://arxiv.org/abs/2406.06525) for discrete next-token generation, [VAR](https://arxiv.org/abs/2404.02905) for next-scale prediction and [MAR](https://arxiv.org/abs/2406.11838) for continuous latent generation conditioned on a visible set. These examples explain different arrangements of generation stages. An iterative conditional head supplies values within a stage in generators that use such a head.

An image decoder reconstructs pixels from the completed representation in latent-space generators. Its cost belongs in a complete-image comparison.

## Choose a mechanism

The [sampling and decoding collection](../papers/sampling-and-decoding.md) separates candidate construction from verification. Read these together to distinguish provisional values from values committed to later conditioning. Scheduling methods change which positions are processed and which completed values are available.

The [conditional-computation collection](../papers/conditional-computation.md) follows the computation that is reduced. Feature reuse substitutes stored values for recomputation. Spatial selection requires a way to supply information at omitted positions. Cache policies and guidance simplifications act on different stored or predicted objects.

The [efficient-generator collection](../papers/efficient-generators.md) includes designs that learn a different predictor or representation. Its distillation section separates a conditional-head replacement from an image-decoder replacement or a learned replacement for the complete generation process.

## Read the results in context

For any reported speedup, identify the baseline and the timed computation. Check whether the measurement includes image reconstruction. Image-quality scores and similarity to paired reference images answer different questions. A sampling-preservation claim needs an identified reference procedure and the conditions of its mathematical argument.

See [evaluation](evaluation.md) for a compact comparison guide. The catalog itself does not certify every source's proof or implementation.
