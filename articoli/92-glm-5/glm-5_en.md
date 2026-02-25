---
tags: ["Generative AI", "Training", "Business"]
date: 2026-02-25
author: "Dario Ferrero"
---

# GLM-5: The model trained on Chinese chips
![glm-5.jpg](glm-5.jpg)

*A 744-billion parameter model, trained entirely on domestic Huawei chips, that reaches the performance of the best proprietary American models in some of the most relevant tests. All without a single NVIDIA processor. The race for Chinese technological autonomy is no longer a future promise: it has already happened, and GLM-5 is the most eloquent proof of it to date.*

Anyone who has been following this portal for a while knows that we are observing something bigger than a series of model releases. With [Kimi K2.5](https://aitalk.it/it/kimik2.5.html), [DeepSeek MHC](https://aitalk.it/it/deepseek-mhc.html), and [Kimi K2 Thinking](https://aitalk.it/it/kimi-k2-thinking.html), we have described the pieces of a mosaic that now, with the arrival of [GLM-5](https://z.ai/blog/glm-5), shows its overall shape with greater clarity. These are not isolated exceptional models. This is a systematic, coordinated movement that in just a few months has brought Chinese open-source artificial intelligence from chasing to parity, and in some cases to surpassing, the most prestigious American labs.

GLM-5 was presented on February 11, 2026, by [Z.ai](https://z.ai/blog/glm-5), the international name used since 2025 by Zhipu AI, a company founded in 2019 as a spin-off of Tsinghua University in Beijing. The launch could not have been more symbolic: the eve of the Lunar New Year, in what some analysts are already calling the "Spring Festival offensive" of Chinese AI. A coincidence? Hard to believe.

## Inside the engine: engineering at scale

To understand what GLM-5 represents from a technical point of view, it is useful to start with an analogy. Imagine a large recording studio. Old models were like standard-sized orchestras where all musicians play at the same time. "Mixture of Experts" (MoE) models, like GLM-5, instead work like a huge orchestra where, for each piece, only the most suitable musicians are called onto the stage. The final result is richer, yet the cost to execute it is much lower than what one would expect from the overall size of the ensemble.

In concrete terms: GLM-5 has 744 billion total parameters (the equivalent of the "knowledge" stored in the neural network), but for processing each single request, it only activates 40 billion. Compared to its predecessor GLM-4.5, which stopped at 355 billion total parameters with 32 billion active, this is a considerable jump, both in terms of capacity and efficiency in managing the computational load.

This is accompanied by another relevant technical choice: the integration of the sparse attention mechanism developed by DeepSeek, known as DeepSeek Sparse Attention. Without going into mathematical details, this technique allows the model to handle very long texts, up to 200,000 text "tokens", equivalent to about 150,000 words, without computational costs exploding proportionally to the length. It is the same logic that allowed DeepSeek to slash the operating costs of its models: don't waste resources on every single word of the context, but focus on the most relevant ones.

Training data grew from 23 to 28.5 trillion tokens, on which the model was "trained" before receiving further refinements through reinforcement learning—a technique that, to put it simply, rewards the model when it produces better answers and corrects it when it makes mistakes, similar to how an athlete is trained with a demanding coach. To manage this process on such a large scale, the Zhipu team developed a training infrastructure called [Slime](https://github.com/THUDM/slime), which optimizes the calculation flow asynchronously, reducing downtime between one training cycle and the next.

A practical note for those thinking about autonomous installation: the model in its original version at maximum precision requires about 1,490 gigabytes of memory, more than a terabyte and a half. These are numbers for a data center, not a home workstation. However, there is a reduced precision version (FP8) that halves this requirement, making the model accessible to more common, though still significant, infrastructures.

## Where it wins, where it struggles: the numbers without filters

Performance analysis is where press release rhetoric meets test reality. And here GLM-5 holds some surprises, in both directions.

On the front of agentic capabilities—the model's ability to perform complex tasks autonomously, not just answer single questions—GLM-5 achieves results that until a few months ago seemed the exclusive prerogative of paid proprietary models. According to measurements by [Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-everything-you-need-to-know), which uses a composite index called GDPval-AA to measure practical utility in real work tasks, GLM-5 obtains an ELO score of 1412, positioning it in third place overall in the world rankings, immediately after Anthropic's Claude Opus 4.6 and OpenAI's GPT-5.2. It is first among all open-source models, with a significant margin over competitors in the same category such as Kimi K2.5 and DeepSeek V3.2.

Even more significant is the jump forward compared to its direct predecessor: GLM-4.7 obtained a score of 42 on the Artificial Analysis intelligence index; GLM-5 reaches 50, the first open-source model to reach and exceed that threshold in version 4.0 of the index. This is not an arbitrary number: it marks the moment when the distance between open models and high-end proprietary models has shrunk to something truly measurable.

In programming, GLM-5 reaches 77.8% in the SWE-bench Verified benchmark, which measures the ability to solve real problems on existing code repositories—a test much closer to a developer's daily work than theoretical tests. Claude Opus 4.5 stops at 80.9%, GPT-5.2 at 80.0%: the distance exists, but it's on the order of a few percentage points, not an abyss.

Perhaps the most surprising result concerns hallucinations, that phenomenon where language models "invent" information with the same confidence as they report true facts, one of the most difficult problems in generative AI. GLM-5 reduces its hallucination rate by 56% compared to GLM-4.7, reaching the lowest level among all models tested by Artificial Analysis. The mechanism used is simply honest: when the model doesn't know something, it refrains from answering instead of inventing. A choice that slightly penalizes the completeness of answers but radically improves the reliability of those provided.

However, there are concrete limits not to be underestimated. GLM-5 is, currently, an exclusively text-based model: it does not analyze images or produce multimedia content, while competitors like Kimi K2.5 already support visual input. The inference speed, about 17-19 tokens per second, is significantly lower than that of models trained on latest-generation NVIDIA hardware, which reach 25 tokens and more. And the maximum context window of 200,000 tokens, while large, remains below the million reached by Claude Opus 4.6. Not negligible defects, but elements to be weighed in relation to cost and availability.
![bench.jpg](bench.jpg)
[Image taken from z.ai](https://z.ai/blog/glm-5)

## The Huawei move: much more than a technical detail

This is where technical analysis gives way to something bigger. GLM-5 was trained entirely on Huawei Ascend chips, without a single NVIDIA processor. But to understand the weight of this statement, we need to take a step back of a few months.

On January 14, 2026, Zhipu AI had already announced a result that made news under the radar: GLM-Image, its generative image model, had become the first high-end multimodal model in the world to complete its entire training cycle on Chinese hardware, specifically on Huawei Ascend Atlas 800T A2 servers. It was already a milestone. With GLM-5, Zhipu replicated and expanded that experience on a much larger scale, extending it to its flagship language model.

The geopolitical context is essential. The US Department of Commerce added Zhipu AI to its list of entities acting against US national security interests, citing alleged links to Chinese military structures. The practical consequence was the blocking of access to NVIDIA H100 and A100 processors, the graphics cards that have become the de facto standard for training the most advanced language models. Zhipu's response was not to seek shortcuts or alternative Western hardware: it was to accelerate collaboration with Huawei and demonstrate that the same work can be done with Chinese tools.

Huawei's Ascend 910B and 910C processors individually offer about 60-80% of the computing power of an NVIDIA H100. A non-negligible gap, which Zhipu closed through two parallel strategies: deep software optimization through Huawei's MindSpore framework, and horizontal scalability—more machines working in parallel to compensate for each one's lower individual power. Huawei's CloudMatrix 384 system, which aggregates nearly 400 Ascend chips into a single logical unit, reaches 300 petaflops of total computing power—an impressive number, obtained with an approach that requires more hardware but proves the feasibility of the "domestic" alternative.

It is worth being precise on one point: GLM-5 is not the first large Chinese language model trained on non-NVIDIA chips. But it is the first of this generation—the generation of models with hundreds of billions of parameters that compete with the best American labs—to do so on such a scale, on entirely Chinese hardware, and to obtain results that stand up to comparison with the world's top models. The distinction is technical, but the strategic scope is enormous.

It is significant to note that Zhipu did not limit itself to Ascend. Official documentation on [GitHub](https://github.com/zai-org/GLM-5/blob/main/example/ascend.md) lists support for Moore Threads, Cambricon, Kunlun Chip, MetaX, Enflame, and Hygon—practically the entire ecosystem of alternative Chinese AI chips to NVIDIA. A signal that the direction is not simply "we use Huawei because we are forced to," but "we are building an ecosystem that does not depend on any foreign supplier."

## Open source as a strategic weapon

GLM-5 is distributed under the MIT license, the most permissive among open-source licenses, allowing commercial use, modification, and redistribution without significant restrictions. Model weights are freely downloadable from [Hugging Face](https://huggingface.co/zai-org/GLM-5) and ModelScope. The API is accessible through the [Z.ai](https://docs.z.ai/guides/llm/glm-5) platform at prices significantly lower than proprietary competitors: about 1 dollar per million input tokens and 3.2 per million output tokens, compared to 15 and more for OpenAI and Anthropic models of the same level.

There is something peculiar and deliberate in this choice of radical openness. Zhipu AI is a company listed on the Hong Kong Stock Exchange (HKEX: 2513), with a listing completed on January 8, 2026, which raised about 558 million dollars. It is not a non-profit academic project: it has investors, shareholders, and performance expectations. Yet it distributes what it considers its most advanced model for free and under a very free license.

The logic, which we have already seen with DeepSeek and Kimi, is that of the ecosystem: the more developers worldwide build on GLM-5, the more the adoption of the Z.ai platform, API services, and brand grows. It is a business model where model openness is the most effective marketing product, and at the same time, in the current geopolitical context, a tool of soft influence on the global artificial intelligence ecosystem.

However, a question must be raised that often remains in the background when talking about Chinese open-source models: the implications in terms of security and regulatory compliance. Zhipu AI operates under Chinese jurisdiction, with all the resulting obligations regarding national security and data access. The model itself, once downloaded, is independent of the company that created it, but those using the Z.ai API rely on an infrastructure subject to Chinese laws. For many Western companies, especially in regulated sectors, this is not a negligible detail. For individual developers or companies in less sensitive contexts, the MIT license guarantees a way out: download the weights, run the model independently, without external dependencies.

The issue of bias in training data, inevitable for any model trained on human text corpora, also remains an open question. Zhipu has not yet published a detailed technical report (the team announced it is "coming"), making it difficult to independently evaluate the choices made in data selection and the alignment phase. This omission is not a marginal detail: precisely on this point, American labs like Anthropic and OpenAI have built a significant part of their reputation, with extensive public documentation and explicit policies.

## The emerging picture

Looking at the articles published on this portal in recent weeks, the pattern is unmistakable. In a compressed timeframe, DeepSeek, Moonshot (with Kimi), and Zhipu (con GLM) have released models that do not just "almost" reach the best American labs: in specific benchmarks and use cases, they surpass them, often at a fraction of the cost. This is not a temporal coincidence: it is the signal of a sector that has reached a critical mass of skills, capital, and, most significantly, a development capability on domestic hardware that American sanctions have not been able to stop, but have if anything accelerated.

The markets' response to Chinese models is not news for February 2026. The most striking precedent dates back to January 27, 2025, when the announcement of DeepSeek R1 wiped out nearly 600 billion dollars in capitalization from Nvidia in a single day—the fastest collapse in the history of the American stock market. GLM-5 fits into that groove: it did not provoke a comparable shock, but it consolidates the narrative that the market has already internalized—that of a Chinese ecosystem that does not need to slow down.

For the sector as a whole, the lesson of GLM-5, like that of DeepSeek and Kimi before it, is that the race for artificial intelligence is no longer a competition between just two teams. Those designing infrastructures, evaluating suppliers, or making investment decisions in the technology sector must reckon with a genuinely multipolar ecosystem, where geopolitical variables, licensing choices, and hardware dependencies have become an integral part of technical analysis.

GLM-5 is freely available on [Hugging Face](https://huggingface.co/zai-org/GLM-5), testable via API at [Z.ai](https://chat.z.ai), and technical details can be consulted on the official [GitHub repository](https://github.com/zai-org/GLM-5). Those who want to have an informed opinion have all the material available to form one.
