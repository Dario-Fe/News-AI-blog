---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-04-13
author: "Dario Ferrero"
---

# TurboQuant: One bit to redefine the limits of artificial intelligence
![turboquant.jpg](turboquant.jpg)

*At the end of April 2025, four researchers from Google Research and New York University published a paper on arXiv with a sober title: *[TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://arxiv.org/abs/2504.19874)*. For months, almost no one talked about it outside of academic circles. Then, in March 2026, Google published a [post on the official blog](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) announcing TurboQuant as a breakthrough in the efficiency of language models, with acceptance at [ICLR 2026](https://iclr.cc/), and within forty-eight hours the paper appeared on every tech feed. Announcements of compressions over five times higher without loss of quality, enthusiastic headlines everywhere. A one-year delay, a wave of hype.*

It's worth stopping, because this dynamic—the dormant paper that explodes thanks to the communication push of a large laboratory—tells something about how information works in the artificial intelligence ecosystem. It's even more worth understanding what TurboQuant really does, without overestimating or dismissing the contribution.

When a large language model generates text, it doesn't process every word from scratch every time. Instead, it keeps in memory a structure called **KV cache**, an archive of key-value pairs, which works like a high-speed digital cheat sheet. As the conversation progresses, the model accumulates the mathematical vectors that encode the meaning of everything it has already read, to consult them instantly during the *attention* mechanism, with which the Transformer decides what to pay attention to at any moment.

The problem is that this cache grows inexorably with context. With windows of 128,000 or 250,000 tokens, now standard in modern models, it can occupy dozens of gigabytes of high-speed memory. Those who use models locally know the paradoxical situation: enough RAM to load the model weights, but not enough as soon as you try to use it with a long context. Like having a large archive with corridors too narrow to carry the files inside.

The obvious answer is to compress those vectors, and that's where quantization comes in.

## Quantizing without losing the thread

Quantization is one of those concepts that seem obscure until you find the right analogy. Imagine a ruler with very fine graduations, capable of measuring to the tenth of a millimeter. You want to store thousands of measurements but have little space, so you switch to a coarser ruler with notches every half centimeter: you lose a bit of precision, but occupy much less space. In practice, KV vectors are normally saved at 16 bits per component, about 65,000 distinct values. Bringing them to 4 bits reduces to only 16 possible values, with a memory saving of four times, but with an approximation that can degrade model performance.

The degradation is not trivial. As programmer and technical analyst Salvatore Sanfilippo observes in his in-depth analysis, KV cache quantization not only affects the ability to retrieve precise textual details but also compromises the quality of semantic synthesis in the Transformer's subsequent layers, where tokens become increasingly abstract representations. Benchmarks on the *needle in a haystack*, the classic test in which a specific piece of information is hidden in a very long text, capture only part of this deterioration.

The territory has already seen many explorers. Techniques like [KIVI](https://arxiv.org/abs/2402.02750) have proposed different approaches to KV cache compression. In the more general field, *product quantization* (PQ) is the historical standard: it divides each vector into subvectors, builds a dictionary for each, and replaces each subvector with the index of the nearest centroid. It works well but requires an offline training phase, unusable in scenarios like the KV cache, where vectors arrive in real-time.

TurboQuant starts from a more ambitious goal: to be *data-oblivious*, that is, to work without knowing anything about the distribution of input data, and to do so with solid theoretical guarantees.
![grafico1.jpg](grafico1.jpg)
[Image taken from arxiv.org](https://arxiv.org/abs/2504.19874)

## The rotation trick and the residual bit

The technical heart of TurboQuant is explained in two acts.

**First act: random rotation.** KV vectors have a persistent structural problem: their components are not uniformly distributed. Some dimensions contain almost all relevant information, while many others are close to zero. Applying standard quantization means wasting precious bits on irrelevant dimensions and accumulating errors on the few that really matter. It's like calibrating a precision scale to weigh pebbles, thus losing all the finesse needed to weigh gold dust.

TurboQuant solves this by applying a **random rotation** to the vector before quantizing it: multiplying it by a rotation matrix changes the coordinates without altering the vector's length, just as rotating an object in space doesn't change its dimensions. The result is that after rotation, the components follow a statistical distribution known in advance, a Beta distribution that in high dimensions converges to a Gaussian, transforming a data-dependent problem into a universal one. The original distribution no longer matters: optimal quantization tables can be precalculated for each desired bit level and applied always, without case-by-case calibrations. Note the important technical distinction: multiplying by any random Gaussian matrix would also change the vector's length, introducing uncontrollable distortions. Rotation keeps the L2 norm invariant, and this property is fundamental.

**Second act: the residue bit.** Quantizers optimized to minimize mean squared error (MSE) do not guarantee accurate estimates of *inner products* between vectors, and inner products are exactly what the *attention* mechanism calculates continuously. Having a good reconstruction of the vector does not automatically imply good estimates of inner products.

TurboQuant addresses this with a second stage: after quantizing the vector to b−1 bits, it calculates the residue—the difference between the original and quantized vectors—and processes it with the **QJL** (*Quantized Johnson-Lindenstrauss*) technique, which projects it onto a random Gaussian matrix and keeps only the sign of each component, occupying exactly 1 bit. This bit acts as an error corrector: it guarantees that the inner product estimate is *unbiased*, meaning the error is not systematically oriented in one direction. The magnitude of the residual error is estimated analytically without saving it, because the distribution is known from the quantizer's construction. The system uses a total of b bits: b−1 for main compression, 1 for correction.

## How solid is the theoretical claim?

The paper states that TurboQuant is *near-optimal*, close to the theoretical lower limit of distortion for any possible quantizer. It's the kind of statement that should be read with care.

The authors demonstrate, using Shannon's coding theorem and Yao's minimax principle, that for any randomized quantizer there exist inputs for which MSE distortion is at least 1/4^b. TurboQuant reaches a distortion at most √(3π/2) ≈ 2.7 times higher than this lower bound, and at 1 bit, the gap drops to about 1.45. The results are formally proven.

The claim holds, with two clarifications. First: "near-optimal" means within a constant factor from the theoretical limit, not touching the limit. The constant 2.7 is small and in practice negligible, but technically the gap exists. Second: the lower bound is derived for the worst case on arbitrary inputs. In production, real KV vector distributions may behave differently.

A fundamental distinction, often ignored in media coverage, is that between optimization for MSE and optimization for inner product distortion. They are two different objectives requiring different solutions, and TurboQuant addresses both with its two-stage approach. It's not a detail: it means the method is specifically designed for the internal functioning of Transformers, not just for compressing vectors in a generic sense.
![grafico2.jpg](grafico2.jpg)
[Image taken from research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## The RabbitQ question: who did what first

The paper raised a debate during the review phase, and it would be dishonest not to address it.

The crux: random rotation as a preprocessing technique was not invented by TurboQuant. A previous method called [RabbitQ](https://arxiv.org/abs/2405.12154) had already used a similar transformation, and its authors protested publicly during peer review, claiming their contribution had been ignored. Their notes were acknowledged, but the characterization of RabbitQ in the final paper continued to be considered inadequate, with researchers claiming properties of asymptotic excellence for their method as well.

There is also a previous work by the same authors of TurboQuant, [PolarQuant](https://arxiv.org/abs/2502.02617), which used a transformation into polar coordinates to achieve a similar effect, but with significantly higher computational cost, making it unusable in online scenarios. TurboQuant is a more practical evolution of it.

As Sanfilippo observes, the rotation trick was already present elsewhere, and not explicitly recognizing it is the most problematic part of the whole affair. Google's public communication smoothed over these precedents, amplifying the impression of a more radical novelty than the paper itself claims.

## Benchmarks and the real value of the contribution

The claim of "absolute qualitative neutrality at 3.5 bits" is supported by the data, but with contexts that deserve attention. The main tests are conducted on Llama-2-7B, a model with 7 billion parameters that is considered small by current standards. On larger models, aggressive quantization tends to behave differently. Sanfilippo emphasizes a critical point: when benchmarks show that even less sophisticated methods obtain similar scores, it can mean the task is too simple to discriminate real differences.

On LongBench, the comparison is more revealing. KIWI at 5 bits obtains scores comparable to TurboQuant at 3.5 bits on several tasks. This does not diminish the result—using fewer bits for the same quality is a real advantage—but it re-scales the scope of the "revolution." The effective saving, in the most honest evaluation, is on the order of one bit compared to the state of the art: being able to quantize at 4 bits with the same performance as a 5-bit quantization with other methods, i.e., reducing KV cache occupancy by 20% compared to competitors. A solid advantage, not a discontinuity.

On the vector search front, the results are more clearly differentiating: eliminating the offline training phase of the codebook is a concrete operational advantage for those building retrieval systems on dynamic data.
![grafico3.jpg](grafico3.jpg)
[Image taken from research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## Open questions

After reading the paper, the blog post, the criticisms from RabbitQ researchers, and Sanfilippo's analysis, some fundamental questions remain without a satisfactory answer.

The first and most important: do the results on Llama-2-7B transfer to models with 70 or 400 billion parameters, to the mixture-of-experts architectures dominant today? Theory says yes, but it must be empirically verified. More recent architectures, with grouped query attention or multi-query configurations, where KV vector sizes are reduced, might respond differently to random rotation.

The second concerns direct comparison with RabbitQ under the same conditions. Controversies during peer review suggest that the comparison presented in the paper was not completely fair: RabbitQ tested on CPU, TurboQuant on H100. A comparison on identical hardware, with the same benchmarks, remains to be done independently.

The third concerns integration into real pipelines. In production, the KV cache coexists with token eviction strategies, sparse attention, and memory paging systems like PagedAttention. A bit gained from quantization can easily be canceled out by sub-optimal integration in these composite systems.

Finally, the broader question: is KV cache compression really the main bottleneck in long-context inference, or are there other factors—bandwidth, access latency, attention parallelization—that weigh more? Saving one bit is a real contribution, but its practical impact depends on where the system's real constraint lies.

TurboQuant is a solid piece of research, with robust theoretical foundations and an original technical contribution in the second QJL stage. It is not the end of the story for vector compression, and it wasn't right to present it as such. But it is a genuine step forward, the kind worth understanding, not just sharing.
