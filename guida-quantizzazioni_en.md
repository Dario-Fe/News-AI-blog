---
tags: ["Generative AI", "Training", "Research"]
date: 2026-10-07
author: "Dario Ferrero"
---

# A Guide to Quantization Formats for Local LLMs
![guida-quantizzazioni.jpg](guida-quantizzazioni.jpg)

*In Borges' parable of the empire and its map, the cartographers end up drawing a map as large as the territory itself, only to discover that it is useless. A 16-bit language model is that map: perfectly faithful, 1:1 scale, but far too unwieldy to fit on your desk. Quantization is the art of shrinking the scale without losing the roads that matter, and in 2026, the tools to do so are so numerous that they require a glossary before you even begin choosing. Following the [guide to inference engines](https://aitalk.it/it/guida-motori-inferenza-locale), this piece brings order to the formats: what they are, what they cost in terms of quality, and which hardware they suit best.*

A premise, as always: this is an analysis of papers, documentation, and repositories, not a benchmark. The numbers come from the linked sources and have not been independently reproduced; where a source has a commercial interest, we state it explicitly.

## Containers versus methods

The first misunderstanding is lexical. A container defines how numbers are written to disk, while a quantization method defines how they are reduced. Among containers, we can include safetensors, GGUF, and old pickle files (.bin, .pt); among methods, GPTQ, AWQ, NF4, and llama.cpp's K-quants and I-quants; and then the hybrid cases: EXL2 and EXL3 are both a method and a file structure, tied to a single library. Pickle files can execute arbitrary code upon loading: beware of files from unknown sources. GGUF, by contrast, according to [Hugging Face documentation](https://huggingface.co/docs/hub/en/gguf), encapsulates standard tensors and metadata, and was created by Georgi Gerganov, the creator of llama.cpp.

The basic math is arithmetic: the table Hugging Face uses for a 7-billion parameter Llama-2 states it plainly: [13 GB originally, 4.1 GB in Q4_K_M](https://github.com/huggingface/skills/blob/main/skills/huggingface-local-models/references/quantization.md).
![tabella1.jpg](tabella1.jpg)

### The second bill: the cache

Weights are only the visible part. As we discussed [in the article on the KV cache](https://aitalk.it/it/kv-cache-approach.html), Llama-3.1-70B at 16-bit accumulates about 0.31 megabytes of cache per token: at 128,000 tokens that is roughly 40 GB, and at one million tokens it exceeds 300 GB—more than double the 140 GB required for the weights themselves. The cache is the archive where the model keeps the keys and values of what it has already read, and with every generated word it must be traversed entirely: bandwidth is the bottleneck, long before storage space is.

Solutions fall into two families. The first compresses: TurboQuant, OSCAR, and EpiCache, examined in that article, work on bits per value or on what to retain; for OSCAR on Qwen3-8B, the gap from BF16 drops to 1.42 points with an eightfold smaller cache. The second manages, which is the subject of the [piece on PagedAttention and RadixAttention](https://aitalk.it/it/pagedattention-radixattention). The [vLLM paper](https://arxiv.org/html/2309.06180v1) measured that in previous systems only 20.4 to 38.2 percent of cache memory held actual tokens; with paging, waste becomes near zero and throughput grows by two to four times. Why discuss it here? Because compressing the cache is a second lever, independent of weight quantization: ExLlamaV3, for instance, quantizes the cache from 2 to 8 bits. When a format promises a long context window on a small GPU, the credit almost always belongs to both.

## GGUF, the master key

If one format has won the local inference race, it is GGUF, for a unglamorous reason: it works everywhere. As seen when [discussing inference engines](https://aitalk.it/it/guida-motori-inferenza-locale), llama.cpp runs it on CPU, NVIDIA, AMD, Intel, and Apple, and Hugging Face lists LM Studio, Ollama, and GPT4All among the tools using it. A single file carries both weights and metadata.

The name reveals the recipe. According to the same Hugging Face table, Q4_K uses 4.5 bits per weight, Q5_K uses 5.5, and Q6_K uses 6.5625; I-quants drop to 4.25 (IQ4_XS), 2.06 (IQ2_XXS), and 1.56 (IQ1_S), relying on an importance matrix—a text sample that indicates to the quantizer which weights matter most. The letters S, M, and L indicate blends where certain layers remain at higher bit precision, which is why a Q4_K_M file is larger than the raw mathematical calculation suggests.

On this foundation came the era of dynamic quantization. [Unsloth](https://unsloth.ai/blog/dynamic-v2), familiar to readers for Unsloth Studio, assigns a different bit count to every layer, and in [benchmarks on Qwen3.5](https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks) claims that its Q4_K_XL and IQ3_XXS variants lie on the optimal Pareto frontier between size and fidelity. Due caution is required: those who measure quantizations are often those who produce them, even if they publish raw data. Furthermore, I-quants carry a runtime cost: in Unsloth's tests, inference slows down by 5 to 10 percent.

Where GGUF falls short is in multi-user serving: [vLLM documentation](https://docs.vllm.ai/en/latest/features/quantization/gguf/) labels it highly experimental and unoptimized, currently requiring an external plugin. The silver lining, invaluable at home, is that a model larger than your video memory can still run by offloading layers between GPU and CPU at the expense of speed.

## GPTQ and AWQ, workhorses

Imagine a carpenter who must trim one hundred boards to standard thicknesses: GPTQ, cutting them one by one, corrects subsequent cuts to compensate for the error just made. Metaphor aside, according to the [paper](https://arxiv.org/html/2210.17323v2), it is a one-shot method that uses second-order information to decide rounding layer by layer using a small calibration sample (128 passages of 2048 tokens). On OPT-175B, perplexity shifts from 8.34 to 8.37 with 4-bit GPTQ, whereas simple rounding pushes it to 10.54; at 3-bit, simple rounding collapses beyond 7000, while GPTQ holds at 8.68. A 175-billion parameter model compresses in about four hours on a single GPU. The claimed speedups—3.25x on A100 and 4.5x on A6000 compared to FP16—apply to single-request batch sizes and stem from moving less data across memory, not fewer compute operations, as the authors explicitly note among the limitations.

[AWQ](https://arxiv.org/abs/2306.00978), from Song Han's group at MIT and best paper at MLSys 2024, starts from an observation: not all weights are created equal, and protecting roughly 1 percent of them significantly reduces quantization error. The trick lies in how they are identified—by observing activations rather than weights—and how they are protected: not by keeping them at higher bits, but by scaling them with an equivalent transformation so the format remains uniform. Without backpropagation, the authors argue, it generalizes better without overfitting to the calibration sample, and their TinyChat exceeds Hugging Face's FP16 implementation by more than three times in speed.

Which one wins? The sources do not declare a clear winner: each paper compares its method against FP16 or simple rounding rather than against the other on the exact same engine. You will encounter them primarily in vLLM and SGLang, where serving multiple concurrent users is required.

More treacherous is the tooling landscape. A [vLLM issue](https://github.com/vllm-project/vllm/issues/30136) notes that AutoGPTQ and AutoAWQ are no longer actively maintained, and while legacy GPTQ and AWQ loaders remain for now, they will eventually be deprecated because too many pre-quantized models exist in the wild; documentation marks [AutoAWQ as deprecated](https://docs.vllm.ai/en/stable/features/quantization/auto_awq/) and points toward llm-compressor. [GPTQModel](https://github.com/ModelCloud/GPTQModel) claims to have replaced them in Transformers, Optimum, and PEFT. Practical advice: check which tool was used and when a 4-bit model was produced, because a widespread format is not necessarily actively maintained.

## EXL3, NF4, MLX: specialists

If you own a gaming NVIDIA card and want to squeeze every drop of performance in solo mode, you will run into ExLlamaV3. Its EXL3 format stems from QTIP, a technique developed at Cornell University, and according to its [README](https://github.com/turboderp-org/exllamav3), it converts using only the unquantized model and the desired target bit rate (including fractional rates): taking a few hours on an RTX 4090 for a 70B model, compared to roughly 720 A100 GPU hours ($850) that the README attributes to AQLM. The most cited figure is an anecdote: Llama-3.1-70B remains coherent at 1.6 bits per weight and, with the output layer at 3 bits and a 4096-token context cache, fits in under 16 GB VRAM. Coherent does not mean benchmarked: it is not a formal score. Limitations: CUDA 12.4+ is required and ROCm support remains a work in progress; the original file structure is preserved, which could make porting to Transformers and vLLM possible, though the README speaks of this in the future tense.

NF4, the 4-bit NormalFloat type in bitsandbytes introduced with [QLoRA](https://arxiv.org/abs/2305.14314), serves a different purpose. The paper demonstrates how to fine-tune a 65-billion parameter model on a single 48 GB GPU while preserving full 16-bit fine-tuning performance: the quantized base model remains frozen and gradients pass through it to small trainable adapter layers. It is not a format to download, but one applied on-the-fly at load time without calibration, and [Marktechpost](https://www.marktechpost.com/2026/09/18/gguf-vs-gptq-vs-awq-vs-exl2-llm-model-formats-explained-2026/) notes that it does not guarantee inference speedups. It is the workflow that tools like Unsloth Studio offer without requiring a terminal.

On the Mac, the landscape changes. According to [Hugging Face documentation](https://huggingface.co/docs/hub/en/mlx), MLX is Apple's framework for Apple Silicon, and MLX-LM converts and quantizes models with a single command, while the `mlx-community` hub publishes pre-converted weights. The constraint is ecosystem lock-in: it works there and nowhere else, and on the Mac, GGUF remains a compelling alternative.

## The cost of losing bits

In the early 2000s, William Basinski recorded his *Disintegration Loops* by looping magnetic tapes that gradually degraded with each pass: the music emerged from decay. With model weights, the loss is not poetic, but follows the same pattern: subtle at first, then steep.

In [Hugging Face's table](https://github.com/huggingface/skills/blob/main/skills/huggingface-local-models/references/quantization.md) for a 7-billion parameter Llama-2, perplexity (how surprised the model is when reading real text) increases relative to 16-bit by 0.03% with Q8_0, 0.13% with Q6_K, 0.39% with Q5_K_M, and 1.68% with Q4_K_M, while file size drops from 13 GB to 4.1 GB. Further down, the bill rises quickly: 6.07% with Q3_K_M, and 15.3% with Q2_K. This is a 2023 model, and modern architectures may react differently.

However, perplexity is a crude thermometer. In the aforementioned analysis, Unsloth demonstrates a case where an IQ2_XXS file under 11 GB outperforms an IQ3_S file on real-world benchmarks (LiveCodeBench and MMLU Pro), despite having worse perplexity and divergence scores, warning that these metrics depend heavily on the calibration text (often Wikipedia). A vendor source, to be sure, but the practical message holds: the thermometer cannot replace testing on your actual workload. A rigorous, head-to-head comparison across all formats using the same model, hardware, and task remains absent in the public literature.

## FP4, ternaries, and QAT

In *Return of the Obra Dinn*, Lucas Pope constructed a 3D world in just two colors, and it works because every pixel is chosen with care. This is the image of the frontier: below 4 bits, you do not arrive by rounding down—you arrive by design.

The first innovation is 4-bit floating point numbers, NVFP4 and MXFP4, which divide weights into small blocks with individual scaling factors. [NVIDIA](https://build.nvidia.com/playbooks/nvfp4-quantization) presents NVFP4 as a format for its Blackwell GPUs, offering roughly 3.5x memory reduction compared to 16-bit with accuracy typically within 1% of FP8, though encouraging evaluation on custom use cases (vendor data). In llama.cpp, a [generic CUDA kernel for NVFP4](https://github.com/ggml-org/llama.cpp/pull/21074) was merged in early April 2026, with a specialized Blackwell kernel planned later: full acceleration is restricted to recent hardware. In Unsloth's benchmarks, MXFP4 uses 4.25 bits per weight compared to Q4_K's 4.5, yielding worse performance across many tensor layouts.

The second path is Quantization-Aware Training (QAT)—training the model with the knowledge that it will be quantized. [Unsloth](https://unsloth.ai/blog/dynamic-v2) reports that a 5-shot MMLU score for Gemma 3 12B in Q4_0 reaches 67.07% compared to 67.15% for the 16-bit baseline: a tenth of a percentage point difference. It is a tailor-made suit rather than a altered off-the-rack coat.

The third, radical approach is ternary models. PrismML's [Ternary Bonsai 2 27B](https://www.marktechpost.com/2026/09/18/prismml-releases-ternary-bonsai-2-27b-a-5-9-gb-apache-2-0-model-retaining-98-2-of-qwen3-8-27b-performance/), released on September 18, uses weights restricted to -1, 0, or +1, occupying 5.93 GB compared to 53.80 GB in 16-bit. The company claims 98.2% of the base model's performance across twenty internal benchmarks; on long agentic tasks, however, performance drops to around 75% (Terminal-Bench 2.1: 52.8 vs 69.7), and running it requires PrismML's custom fork of llama.cpp because upstream rejects the files.

For the previous iteration, an independent developer published a [benchmark suite on GitHub](https://github.com/Astezelex/bonsai-27b-16gb-bench) using an RTX 5060 Ti 16 GB against an IQ2_XXS quantization of the same base model. On general knowledge (MMLU-Redux), it was a statistical tie (0.871 vs 0.860); on AIME26 with 60,000 reasoning tokens, the ternary model won (0.867 vs 0.633), but the gap stemmed primarily from convergence: the IQ2_XXS variant reasoned longer and hit context limits more frequently, though when it converged, it answered correctly. Hence the author's lesson: always specify the reasoning budget. Caveats: a single author, small sample sizes (30 problems on AIME26, where the accuracy gap has p=0.072), analysis orchestrated via an AI assistant as declared by the author, and no peer review. Furthermore, for multi-user serving, the author notes it is currently the wrong tool.

## Choosing based on your hardware

Start with your hardware, as outlined in the [article on engines](https://aitalk.it/it/guida-motori-inferenza-locale). If you have an AMD GPU, like the 16 GB Radeon in our test rig, GGUF is the most viable path: EXL3 requires CUDA, while llama.cpp supports HIP seamlessly. If you have an NVIDIA gaming GPU and run models locally for personal use, choose GGUF for convenience, or EXL3 if you seek maximum tokens per second and accept a narrower ecosystem. If you serve multiple concurrent users, look to GPTQ or AWQ in vLLM and SGLang, or FP8 and FP4 on recent hardware. On Mac, the choice lies between MLX and GGUF, and for fine-tuning a large model with limited VRAM, QLoRA is the standard.

How much quality should you sacrifice? A prudent rule of thumb: start at Q4_K_M and step up to Q5_K_M or Q6_K if memory permits. Go below 3 bits only with quantizations explicitly designed for low bit-rates (dynamic or ternary) and always evaluate on your specific task—whether code, reasoning, or underrepresented languages like Italian. Public sources rarely benchmark Italian performance: it remains a blind spot, and the ultimate judgment rests with you.
![tabella2.jpg](tabella2.jpg)

**Quality Rule of Thumb:**
![tabella3.jpg](tabella3.jpg)

Who wins in all of this? Users with 16 GB VRAM and 27B parameter ambitions. Who loses? Those who rely on a single benchmark number or a single format in an ecosystem where forks proliferate. Open questions remain around long-context stability, vendor benchmark reproducibility, and the integration of ternary models into mainstream inference engines. The perfect map, as Borges reminded us, serves no one: what matters is the map that fits in your backpack and gets you where you need to go.

---

*Technical Note: Data is sourced from linked papers, official documentation, and repositories, and was not independently reproduced. Hugging Face Llama-2-7B figures date from 2023; Unsloth, NVIDIA, and PrismML benchmarks are vendor-provided; the Bonsai benchmark was conducted by a single unreviewed independent author.*
