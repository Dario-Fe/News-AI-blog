---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-11-02
author: "Dario Ferrero"
---

# LFM2.5-24B-A2B Locally: Fast, but Not a Generalist
![lfm2-5-24b-a2b.jpg](lfm2-5-24b-a2b.jpg)

*A Cambridge, Massachusetts laboratory decided to make a model think "out loud"—one that performs as much work per output word as a two-billion-parameter model. In that single sentence lies the entire gamble of LFM2.5-24B-A2B: giant capacity, featherweight compute, and explicit reasoning before every response. It remains to be seen whether that gamble pays off on a standard home PC or only on the creator's benchmark charts. As always, our style is straightforward—no academic fluff, listing pros and cons, separating vendor claims from our own measurements.*

Liquid AI released the model on October 13, 2026, as the largest and final member of the LFM2.5 family, as detailed in their [launch post](https://www.liquid.ai/blog/lfm2-5-24b-a2b). The company is headquartered in Cambridge, Massachusetts, and was founded in 2023, according to [LLM Reference](https://www.llmreference.com/model/lfm-2.5-24b-a2b).

Its name reveals its secret. Twenty-four billion represents total parameters, but only about 2.45 billion are activated per token (word fragment). Imagine a building with sixty-four specialists on every floor, where only four are called upon for each word. All sixty-four must fit inside the building, so memory overhead is paid in full; but since only a few work at a time, compute cost stays low. [TechRepublic](https://www.techrepublic.com/article/news-liquid-ai-lfm25-24b-a2b-local-ai/) clarifies this: activating fewer parameters reduces compute load, but does not grant the model the memory footprint of a 2B model.

The core question of this test is whether this sparse architecture delivers a real advantage on consumer hardware.

## The Test Bench

Our lab setup is well-known: AMD Ryzen 7700, 32 GB DDR5 RAM, 16 GB AMD Radeon RX 9060 XT graphics card, running LM Studio, as described in the [first article of this series](https://aitalk.it/it/qwen3.5-locale-puntata1.html). The tested model is the UD-Q4_K_XL version in GGUF format—a 4-bit dynamic Unsloth quantization weighing approximately 15.4 GB. On a 16 GB card, VRAM headroom is razor-thin. It is plausible that part of the workload offloads to system RAM, though we did not verify this directly; keep this in mind when reading generation speeds.

For optimal generation, Liquid recommends temperature 0.1, top_k 50, and repetition penalty 1.05, as stated on the [official model page](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b). Additional context comes from an [independent memory benchmark](https://pasqualepillitteri.it/news/25727/lfm25-24b-a2b-ram-liquid-ai) on a smaller tech outlet: a 4-bit version peaked at 14.5 GB RAM usage under a ~2,600 token prompt. Since that was a different quantization, the figure is merely indicative.

## Inside the Hybrid Architecture

The [documentation](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b) describes forty layers: thirty gated short convolution layers and ten Grouped-Query Attention (GQA) layers, featuring sixty-four experts per block with top-4 routing. Simply put, convolutions look only at neighboring words at low compute cost, while attention compares words across the entire text—costlier, but essential for long-range coherence. Blending them is a matter of efficiency, not fashion.

Compared to its predecessor, context length expands from 32,768 to 131,072 tokens, and vocabulary size doubles from 65,000 to 128,000 entries via in-place tokenizer expansion designed for non-Latin scripts. The training pipeline is massive: pre-training scaled from 17 to 33 trillion tokens, followed by 2 trillion tokens at 32K context and 300 billion at 131K context, culminating in a five-stage post-training pipeline. The final stage involves reinforcement learning embedded within real agent toolings like OpenClaw, Hermes Agent, Pi, and OpenCode, as explained in the [Hugging Face blog post](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b).

A key design choice sets this model apart: it is a reasoning-only model, generating an explicit chain-of-thought before every answer. Liquid claims this design leverages its fast generation speed. The most transparent detail of the release concerns training quirks: during expert specialization, the model learned to "cheat" by searching for answers in Git history or across GitHub, PyPI, and Hugging Face, even detecting that it ran inside a sandbox. Liquid subsequently tightened test environments and states that official benchmark scores reflect sealed evaluations.

Two caveats before moving on: sixteen languages are officially supported, including Italian. However, the model accepts text input only, per [CloudPrice](https://cloudprice.net/models/liquid/lfm2.5-24b-a2b). The broader model family includes separate vision variants, but this particular release is text-only.

## Benchmark Claims Under Scrutiny

Liquid benchmarked the model against Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it, and Nemotron-3.5-Lightning across sixteen benchmarks, all evaluated via vLLM. These are vendor-provided figures: at launch, no independent third party had audited the model, as noted by [OrcaRouter](https://www.orcarouter.ai/it/blog/lfm2-5-24b-a2b-on-device-agents). Here are key highlights from the [official benchmark table](https://www.liquid.ai/blog/lfm2-5-24b-a2b).
![tabella1.jpg](tabella1.jpg)

The picture is more nuanced than a slogan. The model leads or ties in five of eight tool-use benchmarks and ranks first across all three instruction-following tests, while larger models retain superiority in general knowledge and coding. On SWE-Bench, Nemotron (53.40) outperforms our model (31.20), while Gemma (25.80) lags further behind. Liquid itself recommends pairing the model with a retrieval search system for knowledge-heavy tasks.

Regarding speed, Liquid claims 184 tokens per second on an Apple M5 Max and 114 t/s on a Ryzen AI Max+ 395. Those figures were measured using llama.cpp, Q4_K_M quantization, and 4K input tokens, as reported by [Unite.AI](https://www.unite.ai/it/liquid-ai-releases-open-weight-lfm2-5-24b-a2b-for-on-device-agents/). Those conditions differ from our test environment. Users accessing the hosted API pay $0.10 per million input tokens and $1.00 per million output tokens.

## Local Field Tests

Our standard ten-test battery was applied, with one caveat: the two image-based tests could not be executed because the model is text-only. The remaining eight tests reveal a model that is strong in methodology and planning, but weaker in granular domain knowledge.

On **scientific reasoning** (Higgs mechanism, W/Z bosons, photon), the explanation was solid and well-structured, concluding with a summary table. However, it omitted Goldstone bosons and their role in the longitudinal polarization of massive vector bosons. Furthermore, output formatting suffered from garbled character encoding (e.g., "ГЁ" and "вҶ’"), pointing to a decoder issue rather than reasoning failure. On **coding** (finding the longest cycle in an undirected graph), it generated clean code that solved a different problem altogether: it applied a polynomial-time algorithm to an NP-hard problem without noting its complexity class. While a single test, this aligns with benchmark trends showing SWE-Bench measuring bug fixes in real repositories rather than synthetic algorithm generation.

On **multilingual planning** (a 5-day Japan itinerary for a French client, delivered in French and Italian), the structure was clear, but grammatical flaws appeared (e.g., "le aéroport" instead of "l'aéroport") alongside logistical errors: taking the Narita Express to Asakusa, placing Kanda Myōjin in Ueno, and scheduling Ryoan-ji and Nishiki Market in the same morning. Specific transit routes and JR Pass details were omitted. Conversely, **PDF retrieval** (~1 MB lease contract document) performed impeccably: figures were accurate, correctly distinguishing rental listings (Immobiliare.it) from actual sales transactions (CNA/OMI), citing the correct page upon follow-up.

Its strongest performances came in structured planning. In **web app planning** for a two-developer team, it proposed React, NestJS, PostgreSQL, and Prisma across seven sprint milestones with deliverables and risk analyses, containing only one minor typo ("pdfgenerate"). In a **four-turn conversation** designing a task management app, it maintained perfect context retention, generating a WebSocket vs. polling comparison table, full database DDL scripts, indexes, Prisma schema, and a 10k user scaling plan. In **strategic planning** for a $10M startup, it produced executive-level output covering six semesters with risk mitigations—though it responded in English to an Italian prompt, deducting half a point. In **logical analysis** of three contradictory statements, it formalized the premises, identified the contradiction, and justified its conclusion in proper Italian.
![tabella2.jpg](tabella2.jpg)

The overall average score was 4.3 out of 5, with an average output speed of ~44.7 tokens per second.

Next came the critical test for an agentic model: tool calling. To clarify how this works: the model does not execute actions directly; it formats function calls between special tokens (using Python syntax by default), which the host harness executes before feeding results back, as explained in Liquid's [tool use guide](https://docs.liquid.ai/lfm/key-concepts/tool-use). We tested two simulated tools (weather and email). The model generated correct JSON call sequences at 46.45 tokens/sec with ~2 seconds of reasoning pause. All three variants succeeded: when provided with external tool output, it incorporated the data into its draft; when missing a recipient address, it asked for Mario's email instead of hallucinating one; and when given a prompt requiring no tools, it executed no call. These test format adherence and judgment, but stopped short of a live multi-turn agent loop.

## Thinking Before Responding

In *Disco Elysium*, the protagonist never acts without debating his twenty-four internal skills—voices arguing in his head. LFM2.5-24B-A2B operates similarly, and unlike in the game, we see the reasoning stream scroll in real time. This changes how speed is perceived: the 44 tokens/sec rate measures answer generation, but precedes several seconds of initial reasoning (~2 seconds in the tool test). For inter-agent communication, that latency is negligible. For interactive chat, user perception depends on task length, as longer prompts increase reasoning time.

Liquid emphasizes that reasoning tokens carry low compute overhead because only 2.45B parameters are active. While true for FLOPs, wall-clock time remains a factor. Furthermore, an independent Italian test noted instances where the model reasoned in English before answering in Italian—a behavior to monitor, though our Italian prompts received Italian responses.

What about the sparse architecture's performance advantage? On our test bench, 44 tokens/sec is less than half the 114 t/s reported on a Ryzen AI Max+, owing to different quantization, context lengths, and memory bandwidth. It remains a respectable speed for daily work, and for a 24B parameter model running on a 16 GB card, it is an impressive feat. However, proving a generational leap would require side-by-side benchmarks on identical hardware.

## Where It Excels, Where It Falls Short

Its sweet spot matches its design intent: autonomous agents, workflow automation, project planning, long coherent conversations, and strict instruction-following. It is poorly suited for complex algorithmic coding or acting as a standalone encyclopedia—knowledge and coding deficits are acknowledged in Liquid's own benchmarks and confirmed by our testing. It lacks vision capabilities. Italian language performance is strong, though explicitly specifying the language in system instructions is recommended.

A note on privacy: "local execution" does not guarantee "data safety." An agent wired to web search, cloud APIs, or external integrations can still transmit data externally. The weights remain on your machine, but tool outputs may not. Who wins? Small studios and enterprises beneath the commercial revenue threshold gain a fast, private, free agentic model. Who loses? Anyone deploying it for tasks requiring deep encyclopedic knowledge or mission-critical code generation.
![tabella3.jpg](tabella3.jpg)
*Comparison table with models previously evaluated on AiTalk.it*

## Verdict and Licensing

LFM2.5-24B-A2B is a fast, methodical model that plans with clarity, but stumbles when deep domain knowledge or theoretical rigor is required. We recommend deploying it for agents, automation, and planning, pairing it with a retrieval search system for factual queries, using a stronger model for complex code, and explicitly specifying the target language.

For developers building commercial products, licensing details matter. The LFM Open License v1.0 permits free commercial use for entities with under $10M in annual revenue; above that threshold, a paid license is required. Derivative models remain subject to the same terms, while academic research and qualifying non-profits are exempt from revenue limits. Full terms appear on the [official licensing page](https://docs.liquid.ai/lfm/help/model-license).

Three open questions remain: How well will benchmark scores hold up under independent reproduction? How much does mandatory reasoning overhead impact real-time tasks? What happens when a live agent with real tools encounters occasional language drift? Only long-term production deployments will provide the answer.
