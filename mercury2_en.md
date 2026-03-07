---
tags: ["Generative AI", "Research", "Startups"]
date: 2026-03-13
author: "Dario Ferrero"
---

# One Thousand Tokens per Second: Mercury 2 Wants to Rewrite the Rules of AI
![mercury2.jpg](mercury2.jpg)

*There is a strange, almost alienating moment that anyone who has used Mercury 2, from Inception Labs, for the first time describes in a similar way: you type the question, press enter, and the answer is already there, in its entirety, even before your brain has finished registering that you clicked something. It's not a visual effect, it's not an interface trick. The model really generates over 1,000 tokens per second.*

To give an order of magnitude: an average Italian novel is about 300,000 characters, which is approximately 90,000-100,000 tokens. Mercury 2, in theory, would write it in less than two minutes. Claude 4.5 Haiku, one of the most widespread "fast" models today, stops at about 89 tokens per second. GPT-5 Mini at about 71. The difference is not incremental: it is structural.

All this is possible because Mercury 2 does not work like any other language model you have ever used. And understanding why requires a step back into the way generative artificial intelligence produces text, and how it has always done so in a single way.

## Two Families, One Dominant Paradigm

If you want to understand Mercury 2, you must first understand the bottleneck it seeks to eliminate. And that bottleneck has a precise technical name: autoregressive generation.

All the large language models you use every day—ChatGPT, Claude, Gemini—work on the same basic principle: they produce text one token at a time, from left to right, and each token depends on all those that precede it. It's like typing on a typewriter: you can't hit the third letter before you've hit the second. This sequential dependence is architectural, not an inefficiency that can be eliminated with more hardware or software optimizations. It is the very nature of the mechanism.

Diffusion is something different. The technique originated in the world of image generation—it's at the core of Stable Diffusion, Midjourney, DALL-E—and works in the opposite way: instead of building the result piece by piece, it starts from a completely "noisy" and imprecise output and refines it progressively in parallel, at multiple points simultaneously, converging towards the correct answer in a few steps. It's no longer like a typewriter but more like a photographer developing a polaroid: the entire image emerges gradually, all at once.

Applying this technique to text, unlike images, is however a much more difficult problem. Language has logical, grammatical, and semantic constraints that images do not have to the same extent. For years, it was believed that diffusion was not suitable for text. If you want to delve deeper into the technical comparison between the two approaches, you can find [an article dedicated to this very topic](https://aitalk.it/it/diffusion-vs-autoregressive.html) on the portal.
![grafico1.jpg](grafico1.jpg)
[Image taken from inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Who Solved the Impossible Problem

The breakthrough came from Stanford. Stefano Ermon, a computer science professor and one of the co-inventors of the diffusion techniques used in Stable Diffusion and DALL-E, had been working on this problem since 2019. Years of research to understand how to apply diffusion to text, until a breakthrough documented in a paper presented at ICML 2024, the leading international machine learning conference, which won the best paper award. This is no small distinction: it means the scientific community formally recognized the advancement as significant.

In 2024, Ermon founded Inception Labs in Palo Alto, bringing with him two former students who became professors: Aditya Grover from UCLA and Volodymyr Kuleshov from Cornell. The expanded team includes researchers and engineers from Google DeepMind, Meta AI, Microsoft AI, and OpenAI, and the group's contributions are not limited to diffusion: their collective curriculum includes foundational work on flash attention, decision transformers, and direct preference optimization (DPO), techniques that marked the development of modern language models.

Funding arrived in November 2025 with a [$50 million seed round](https://techcrunch.com/2025/11/06/inception-raises-50-million-to-build-diffusion-models-for-code-and-text/), led by Menlo Ventures with participation from Mayfield, M12 (Microsoft's venture capital fund), Snowflake Ventures, Databricks Ventures, NVentures (NVIDIA's investment arm), and Innovation Endeavors. Angel investors include Andrew Ng and Andrej Karpathy; the latter, former Director of AI at Tesla and co-founder of OpenAI, has publicly encouraged his followers to try the model, noting that the non-autoregressive nature of diffusion could lead to "new psychology, novel strengths and weaknesses." When Karpathy says something is worth trying, the industry tends to listen.

## Mercury 2: What It Does, How Much It Costs, How Well

On February 24, 2026, Inception [launched Mercury 2](https://www.inceptionlabs.ai/blog/introducing-mercury-2), presenting it as the first production-available diffusion-based "reasoning LLM." Speed numbers were independently verified by [Artificial Analysis](https://artificialanalysis.ai/models/mercury-2), one of the industry's most rigorous benchmark firms: 711.6 tokens per second in their standardized multi-turn evaluations, placing Mercury 2 first out of 132 monitored models. On the optimal hardware configuration—NVIDIA Blackwell GPUs with NVFP4 precision—Inception's internal numbers rise to 1,009 tokens per second, with an end-to-end latency of 1.7 seconds.

The comparison is merciless for competing models in the same tier: Gemini 3 Flash completes responses in 14.4 seconds, Claude 4.5 Haiku with reasoning in 23.4 seconds. It's not a difference of degree, it's a difference of user experience; the subjective feeling of "instantaneity" changes completely. [InfoWorld](https://www.infoworld.com/article/4137528/inceptions-mercury-2-speeds-around-llm-latency-bottleneck.html) summed up the point well: Mercury 2 doesn't optimize margins, it redraws the bottleneck.

On the qualitative front, Mercury 2 positions itself honestly in the "fast and light" model tier, not among the giants of deep reasoning. The published benchmarks are clear: 91.1 on AIME 2025 (competitive mathematics), 73.6 on GPQA Diamond (advanced scientific reasoning), 67.3 on LiveCodeBench (coding), 52.9 on TAU-bench (complex agents). These results are competitive with Claude 4.5 Haiku and GPT-5 Mini, but not with Claude Opus 4.6 or the best extended reasoning models, which score in the range of 80-90 out of 100 on the Artificial Analysis Intelligence Index, while Mercury 2 stops at 33.

The pricing is one of the most interesting aspects: $0.25 per million input tokens, $0.75 per million output tokens. For comparison, Claude 4.5 Haiku costs about $4.90 per million output tokens, about six and a half times more. GPT-5 Mini is around $1.90, about two and a half times more. For the same volume, the cost difference in high-traffic pipelines can be worth tens of thousands of dollars per month. The API is compatible with the OpenAI standard: in theory, for those already using the OpenAI ecosystem, it's a replacement without rewriting code.
![grafico2.jpg](grafico2.jpg)
[Image taken from inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Where Mercury 2 Really Works

Inception is explicit about which use cases Mercury 2 is designed to serve, and the testimonials collected at launch are consistent with that positioning.

The most natural field is **agentic loops**: systems where an AI agent performs dozens or hundreds of inference calls to complete a task—code analysis, iterative research, data pipelines. In these contexts, latency doesn't manifest just once; it multiplies at every step. With traditional models, a ten-step workflow that requires 20 seconds per inference leads to over three minutes of total waiting. With Mercury 2, the same workflow takes less than twenty seconds. It's not just faster: it changes which interactions are physically feasible in real-time.

Zed, a code editor highly followed in advanced development environments, is one of the launch partners: its co-founder Max Brunsfeld described the suggestion speed as fast enough to seem "part of one's own thinking." Skyvern, an automation platform for web agents, reported that Mercury 2 is at least twice as fast as GPT-5.2 for their use cases. Wispr Flow, a tool for real-time cleaning of voice transcriptions, evaluated it as irreplaceable for low-latency human-machine interaction applications.

**Voice AI** is the second area where speed becomes decisive. Voice interfaces have the narrowest latency window in the entire AI ecosystem: a response that arrives in more than two seconds breaks the naturalness of the conversation. At 70-90 tokens per second, autoregressive models are at the limit of usability for voice. Mercury 2 removes that limit with a massive margin. OpenCall and Happyverse AI, both active in the voice avatar and phone agent sector, cited low latency as the main enabling factor.

For **search and RAG pipelines** (Retrieval-Augmented Generation), where documents are retrieved, classified, and summarized in sequence, Mercury 2 allows adding a reasoning step in the search cycle without exploding the latency budget. SearchBlox, active in enterprise search for compliance, analytics, and e-commerce, stated that the partnership with Inception makes "real-time AI practical" for their product.

## Shadows in the Frame: The Limits That Count

Mercury 2 is currently a **text-only** model. It does not process images, audio, or video. In a landscape where multimodal capability has become almost the expected standard, especially for complex enterprise applications, this is a concrete limitation, not a footnote detail.

Furthermore, it is a **cloud-only model, without open weights**. There is no downloadable version, no on-premise deployment possible, and no fine-tuning on proprietary data available. For organizations with data residency requirements, model sovereignty, or the need for specialized adaptation—sectors like healthcare, finance, defense—this excludes Mercury 2 for a wide class of use cases.

Then there is the **problem of verbosity**. As documented in the [independent review by Awesome Agents](https://awesomeagents.ai/reviews/review-mercury-2/), Artificial Analysis found that during their evaluations, Mercury 2 produced 69 million output tokens, compared to an average of 20 million for equivalent models. The model tends to generate more text than necessary. In practical terms, this is not just an aesthetic problem: it inflates the effective output cost and adds noise to workflows that require structured and concise output. This behavior is manageable with prompt engineering, but it is a default that requires attention.

The deeper question concerns the **maturity of the architecture**. Diffusion models for text are an emerging class; Mercury 2 is effectively the first model of its kind available in commercial production. This means there are fewer engineers who know the failure patterns in production, less documentation on edge cases, and a smaller community that has already faced and solved typical problems. When something breaks in a production system—and it always does—the ecosystem support for a consolidated technology like GPT or Claude is incomparably richer. This is not a critique of the architecture, but a real cost that does not appear in any benchmark.

Finally, it's worth noting that the highest speed numbers, the title of 1,009 tokens per second, assume NVIDIA Blackwell GPUs with NVFP4 precision. The Artificial Analysis data, which reflect real standard cloud infrastructure, attest to 711.6 tokens per second: an extraordinary number, but far from the headline. There are no published data for older hardware.

## The Market Speaks, But with Caution

The relevant question is not just whether Mercury 2 works—independent evidence suggests that yes, the speed promises are real—but whether the market is actually adopting diffusion models at scale, or if we are still in the technical curiosity phase.

Signs of adoption exist: documented integrations with tools like Zed, Skyvern, Wispr Flow, SearchBlox, and Viant (an advertising platform that stated it uses Mercury to optimize campaigns in real-time). The [availability on Azure AI Foundry](https://www.inceptionlabs.ai/blog/mercury-azure-foundry), announced in November 2025, opens Mercury to Microsoft's vast enterprise ecosystem. Compatibility with the OpenAI API lowers the entry barrier to almost zero for those already operating in that ecosystem.

On the other hand, Mercury 2's position in the "Haiku-class" tier of models, competitive with fast models but not with the best for deep reasoning, structurally limits its use to use cases where speed has priority over reasoning complexity. For decisions requiring analysis of long and complex documents, advanced multi-source synthesis, or reasoning on nuanced scenarios, frontier models maintain a real advantage that Mercury 2 does not eliminate. As [The New Stack](https://thenewstack.io/inception-labs-mercury-2-diffusion/) noted, Ermon himself is candid about this: Mercury 2 competes with the Haiku/Flash tier, not with Opus or GPT.

Inception's bet is that the trajectory of quality in diffusion models will follow the same scalability curve seen in autoregressive models: quality can be improved over time, with the structural advantage of speed as a starting point. It's a plausible bet, not yet verified.

## Open Questions: Is the Future Parallel?

Mercury 2 does not answer the biggest question it raises: can diffusion really become the dominant paradigm for language models, or will it remain a specialized approach for high-speed use cases?

Ermon has stated that he imagines a future where all language models are based on diffusion. It's an ambitious vision, and the person who expressed it—one of the scientists who helped build the foundations of diffusion for images—has the credentials to support it. But moving from "it works exceptionally well for a specific subset of use cases" to "it replaces autoregressive as the general paradigm" is a huge leap, and there is no evidence yet that the quality gap with frontier models is destined to close.

Furthermore, concrete open questions remain: how do diffusion models behave on very long chain-of-thought reasoning, where coherence across thousands of tokens is crucial? What happens to quality at 50,000 or 100,000 context tokens, when the 128K window is truly stressed? How is an architecture whose output production is less step-by-step interpretable than autoregressive managed ethically?

The speed is real. The cost is competitive. The team is credible beyond any reasonable doubt. The current limitations are concrete and documented. Mercury 2 represents something genuinely new in the language model landscape—not the smartest model available today, but perhaps a signal of where the conversation on AI inference efficiency still needs to go.

The typewriter, token after token, might really have its days numbered. But the novel that will be written next, and how good it will be, is still all to be seen.

---
