---
tags: ["Ethics & Society", "Generative AI", "Business"]
date: 2026-07-08
author: "Dario Ferrero"
---

# GLM-5.2: the Chinese open-weight closing the gap, at least in coding
![glm5.2.jpg](glm5.2.jpg)

*When Z.ai, the laboratory everyone in China still knows as Zhipu AI, released [GLM-5](https://aitalk.it/it/glm-5.html) last February, the message was already clear: the GLM series wasn't just aiming to be competitive, it was aiming to be relevant for those who build software. That 744-billion-parameter model with a Mixture-of-Experts architecture had put performance on the table that didn't look out of place next to the big proprietary ones, with the far-from-secondary difference of open weights under the MIT license. Just over four months later, on June 13, 2026, Z.ai raised the stakes again: GLM-5.2 arrived first on the GLM Coding Plan tiers, the subscription plans dedicated to developers, and then, on June 16, on public API and on [Hugging Face](https://huggingface.co/zai-org/GLM-5.2) with freely downloadable weights.*

The jump from 5.1 to 5.2 might seem like an incremental update, the kind of release companies use to stay visible between cycles. It isn't. GLM-5.2 brings with it a one-million-token context that, for the first time in the series, Z.ai declares "solid," a carefully chosen word, in contrast to the industry trend of advertising huge windows that in practice degrade already beyond one hundred thousand positions. And it brings with it a series of results on long-horizon coding benchmarks that deserve to be read carefully, without hype but without downplaying.

## Architecture: 753 billion with a sparse brain

GLM-5.2 is an MoE model with 753 billion total parameters and about 40 billion active per token. This means that at each inference, the model "turns on" only a specialized fraction of its neural network, somewhat like an orchestra in which only the musicians needed for that piece play together, not all one hundred and thirty. This allows for the expressive capacity of an enormous model with much lower computational costs compared to an equivalent dense architecture.

The main architectural novelty compared to GLM-5.1 is a technique that Z.ai calls IndexShare in its documentation, described in the paper as [IndexCache](https://arxiv.org/abs/2603.12201). In sparse attention architectures, which allow the model to selectively "look" at portions of the context instead of everything, the component that decides where to look is called an indexer. In GLM-5.2, every four sparse attention layers share the same indexer instead of calculating a separate one. The result is a 2.9x reduction in calculations per token at a one-million-token context: a computational saving that makes that huge window truly usable, not just advertiseable.

The other improvement is on the MTP layer, the speculative decoding mechanism that allows generating multiple tokens in advance and then verifying them. Combining IndexShare with a shared KV-cache system and training with end-to-end TV loss, Z.ai has increased the acceptance rate of speculative tokens by 20%. In practice: faster responses for the same quality, a relevant detail for those using the model in agentic pipelines where latency multiplies by hundreds of calls.

The one-million-token context isn't just a figure for press releases. Z.ai conducted months of specialized training on coding-agent scenarios: large-scale implementations, automated research, performance optimization, complex debugging. The declared goal was for the model not to just accept more tokens in input, but to maintain quality and coherence throughout the trajectory, which is something else entirely. The technical documentation explicitly speaks of "engineering judgments formed earlier" that the model must know how to "carry forward into subsequent execution": understanding architectures, remembering API constraints, respecting code conventions established twenty screens earlier.

## Benchmarks: where it wins, where it follows

The most honest way to read GLM-5.2's numbers is to separate them by category, because the model is not uniformly strong on everything, and it is precisely this selectivity that makes it interesting as a trend signal more than an object of hype.

On standard coding, GLM-5.2 is the strongest open-weight model available. On [Terminal-Bench 2.1](https://terminal-bench.com) it scores 81.0 against GLM-5.1's 63.5, a jump of nearly 18 points that isn't explained by marginal adjustments. On SWE-bench Pro it scores 62.1 against the predecessor's 58.4, overtaking Qwen3.7-Max (60.6), MiniMax M3 (59), and DeepSeek-V4-Pro (55.4). Claude Opus 4.8 remains ahead with 69.2, GPT-5.5 stops at 58.6.

Where GLM-5.2 does the most surprising thing is on long-horizon benchmarks, those that measure the ability to complete complex engineering projects, not single functions. On [FrontierSWE](https://www.frontierswe.com), which measures the ability to carry forward technical projects lasting hours or dozens of hours, GLM-5.2 scores 74.4 against the previous version's 30.5: more than doubled. It is only one percentage point away from Claude Opus 4.8 (75.1) and surpasses GPT-5.5 (72.6) by nearly two points. On [PostTrainBench](https://posttrainbench.com), where each agent is assigned an H100 GPU to improve smaller models via post-training, GLM-5.2 scores 34.3 beating both GPT-5.5 (28.4) and Claude Opus 4.7, second only to Opus 4.8 (37.2). On [SWE-Marathon](https://swe-marathon.vercel.app), the most brutal testing ground, with tasks like building compilers and developing production-grade services, the model rises to 13.0 from the previous 1.0, but here the gap from Claude Opus 4.8 (26.0) is still clear.

On general reasoning the picture is more mixed. On HLE (Humanity's Last Exam) GLM-5.2 scores 40.5, in line with GPT-5.5 (41.4) but distant from Claude Opus 4.8 (49.8) and Gemini 3.1 Pro (45). On AIME 2026 it scores 99.2, third overall in the table. The overall profile is that of a model precisely optimized for engineering workloads, not a generalist all-rounder.

An important detail concerns the control of "effort level": GLM-5.2 exposes two presets, High and Max, which allow balancing performance and latency. With the Max setting, the model consumes more tokens, and the Artificial Analysis data is enlightening: in the Intelligence Index evaluation, it generated 140 million tokens against an average of 110 million. More verbose than necessary, therefore, and this translates into higher costs per session. It's not a hidden flaw; it's a characteristic to be known before building production pipelines.
![bench.jpg](bench.jpg)
[Image from the github.com repository](https://github.com/zai-org/GLM-5)

## Field test: twenty minutes of the Giro d'Italia

It's worth recounting a direct test, with all its limitations declared at the outset. I used the free version of the chatbot on [chat.z.ai](https://chat.z.ai), which doesn't expose the model's maximum performance, uses a reduced context and doesn't have access to effort levels, with a deliberately sparse request: build a web app that, taking historical data from the Giro d'Italia, would visualize with a simple graphic animation the gaps between riders chosen by the user in an edition specified by the user.

In about twenty minutes, the model produced a complete project: Next.js 16 with App Router, TypeScript, Tailwind CSS, animated SVG components for the cyclists, architecture with route handlers, a dataset of 37 historical editions, proportional animation of the gaps, speed controls and gap amplification. An articulated technical specification on multiple levels, with coherent architectural choices and working code. The level of organization and structural reasoning was genuinely impressive.

The limit manifested on the data: many riders' times and some historical rankings contained errors, requiring requests for correction. It's no surprise; these are specific factual pieces of information on which models hallucinate regularly, and the free version certainly doesn't offer the model's maximum performance. However, tests conducted by well-known enthusiasts with paid plans and full access return significantly superior coding results, confirming that the free tier is an entry point, not a faithful representation of the model's capabilities.
![immagine1.jpg](immagine1.jpg)
*Screenshot of the application developed with GLM 5.2*

## The price that changes the conversation

The detail that makes GLM-5.2 a serious conversation for development teams isn't any of the benchmarks mentioned above. It's the price. The standalone API, active since June 16, costs 1.40 dollars per million input tokens and 4.40 in output, with input cache at 0.26 dollars, about a fifth of the normal cost for repeated context. For comparison: GPT-5.5 costs 5 dollars per million in input and 30 in output; Claude Opus 4.8 5 dollars in input and 25 in output. The average cost of GLM-5.2 is about one-sixth that of GPT-5.5.

For a team doing agentic coding with intensive pipelines, hundreds of thousands of tokens per session, multiple sessions a day, the difference is not marginal. It's the difference between a service that laboriously balances the books and one that makes them work with a margin.

There is also the GLM Coding Plan, the flat subscription model designed for those using the model directly within tools like Claude Code, Cline, OpenCode, Roo Code and a dozen other compatible development environments. The base tier starts at about 10-18 dollars per month, with quotas in prompts per hourly cycle rather than per token, a more predictable pricing model for individual developers. The Max tier goes up towards 80 dollars per month with much higher volumes. During peak hours (14:00-18:00 Beijing time), quota consumption is multiplied; off-peak, at least until the end of September 2026, the current promotion zero's out the multiplier.

For those who want to eliminate the cost item entirely: the weights are available under the MIT license, no field-of-use constraints, no monthly active user thresholds, no separate commercial agreements. The full model in FP8 occupies about 800 GB on disk and runs in production on 8 H200 GPUs with sufficient headroom for the one-million-token context. An INT4 quantized version drops to about 200 GB and works on 4 H200s with a regression of about 1-3% on coding benchmarks, an acceptable loss for many corporate scenarios, especially considering the disappearance of the cost per token. The model is also available on [OpenRouter](https://openrouter.ai/z-ai/glm-5.2) with slightly lower prices and access to more than thirteen providers competing on inference costs.

## Who wins, who loses, what remains open

The launch of GLM-5.2 doesn't have a single protagonist and doesn't produce a single effect. It's worth looking at it from multiple angles.

For development teams using coding assistants or agentic pipelines, the most concrete message is that there is now an open-weight model with performance in the territory of the top proprietary ones on engineering tasks, at a cost that significantly changes the economic calculation. It's not certain that it's the right choice for every context; verbosity, effective costs with Max effort and run-to-run variance remain factors to be evaluated on a case-by-case basis, but it's the first time the conversation can take place on grounds of real technical equality, not just ideological.

For the open-weight market as a whole, GLM-5.2 consolidates a trend that had already shown clear signals with GLM-5.1 and with Moonshot AI's Kimi K2.7: Chinese open-architecture models are no longer chasing Western proprietary ones with a six-month delay on generic benchmarks. On specific verticals, coding, agentic tasks, long contexts, they are building their own advantages, and they do so with cost structures that the OpenAI-Anthropic duopoly cannot easily replicate.

However, there are shadows that it's incorrect to ignore. Z.ai has been on the U.S. Bureau of Industry and Security Entity List since January 15, 2025: MIT weights are legally usable by private companies, but American federal clients and most defense primes effectively treat models of Chinese origin as inaccessible, regardless of the license. For European enterprises in regulated sectors, the absence of an AI Act GPAI Code of Practice signed by Zhipu, and the lack of an Annex XI technical sheet, offloads the burden of transparency compliance onto the downstream deployers. These are not absolute vetos, but they are costs and risks that must be taken into account along with those per token.

The question that remains open is the most interesting one: is GLM-5.2 the signal that the competitive advantage of high-end proprietary models is eroding specifically on coding, or is it a vertical excellence that leaves significant differences intact on everything else? The honest answer, at the moment, is that on tasks outside coding and agentic capability, the benchmarks show a strong but not exceptional model. The positioning is declared and coherent: Z.ai is not trying to make the world's best general model, it's trying to be the reference for those who build software. Whether it's succeeding, adoption in the coming months will measure, in the production logs of the teams that will use GLM-5.2 as the backbone of their pipelines, not in the comparison tables that every laboratory prepares to look good.
