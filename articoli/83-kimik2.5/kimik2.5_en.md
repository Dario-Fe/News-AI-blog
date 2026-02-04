---
tags: ["Generative AI", "Research", "Ethics & Society"]
date: 2026-02-04
author: "Dario Ferrero"
---

# Kimi K2.5 and China's Long March in AI: When the Embargo Becomes a Springboard
![kimik2.5.jpg](kimik2.5.jpg)

*There's a moment in every high-level chess game when you realize the player under pressure isn't trying to defend: they're building a counter-move. Something similar is happening in the great geopolitical game of artificial intelligence, and the release of Kimi K2.5 by Moonshot AI is not just another press release to be skimmed distractedly. It's another chapter in a story worth following closely, as in the previous analysis of [Qwen3-TTS](https://aitalk.it/it/qwen3-tts.html) and synthetic voice generation, because it narrates and confirms how the hardware restrictions imposed by the United States on China are producing the exact opposite of the intended effect: instead of slowing down Chinese innovation, they are accelerating it along unexpected trajectories.*

We had already talked about it when analyzing [DeepSeek and its MHC architecture](https://aitalk.it/it/deepseek-mhc.html), and before that with [Kimi K2 Thinking](https://aitalk.it/it/kimi-k2-thinking.html). Today we return to the topic not to chase the hype of the latest model release, but because each release adds a piece to a mosaic that is reshaping the global balance of AI. And Kimi K2.5, with its one trillion parameters organized in a deeply optimized Mixture of Experts architecture, represents a qualitative leap that deserves more than a distracted scroll on Hacker News.

## Yet Another Release That Matters

Let's start with the numbers, because in AI, numbers tell stories. [Kimi K2.5](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart) is a monster with a total of one trillion parameters, but thanks to its MoE architecture, it only activates thirty-two billion for each generated token. It's like having a huge library where, instead of browsing all the volumes every time, you automatically select the eight most relevant shelves out of the three hundred and eighty available, plus one shared shelf that is always consulted. This approach, technically defined as "sparsity," is not new, but Moonshot has brought it to an impressive level of refinement.

The architecture rests on sixty-one layers, one of which is dense, with an attention mechanism called MLA (Multi-Head Latent Attention) that drastically reduces memory requirements during inference. The hidden dimension of the attention is 7168, while each MoE expert works with 2048 hidden dimensions. The vocabulary has 160,000 tokens, and the context extends up to 256,000 tokens, a window that allows for processing very long documents or articulated conversations without losing the thread.

But the real leap from K2 is elsewhere. Moonshot has natively integrated multimodal capabilities through MoonViT, a 400-million-parameter vision encoder that allows the model to "see" images and videos not as painstakingly grafted-on add-ons, but as an organic part of its understanding of the world. It was trained on about fifteen trillion mixed tokens, visual and textual, through continual pretraining on the Kimi-K2-Base foundation. The result: K2.5 not only reads code, it generates it by looking at UI mockups or analyzing workflows from videos.

Salvatore Sanfilippo, one of the most respected developers in the international tech community and the creator of Redis, analyzed K2.5, emphasizing this very aspect: "It is a natively multimodal model, trained specifically to solve user interface-related programming problems by acting as an agent that 'sees' the layout." We're not talking about a demo trick, but a design capability that changes how one can interact with AI in daily work.

And there's another element that Sanfilippo highlights as crucial: native four-bit quantization. K2.5 was trained from the start with Quantization-Aware Training techniques that allow it to run with about 600-700 GB of RAM. This means a cluster of Mac Studios or consumer servers with relatively accessible GPUs can run a frontier model through distributed inference. You don't need a megacorporation's datacenter. It's concrete technological democratization, not rhetoric.

## MoE, Vision, and Agent Swarm

But the real novelty of K2.5 lies in a feature that sounds like science fiction but is already operational: the agent swarm. Instead of having a single AI agent work on complex tasks, K2.5 can dynamically instantiate swarms of specialized sub-agents that collaborate in parallel. It's like moving from a solitary craftsman to a Renaissance workshop where each master focuses on their part of the work.

The mechanism is based on a technique called Parallel-Agent Reinforcement Learning (PARL): the model autonomously breaks down a complex task into sub-goals, generates specialized agents for each, and coordinates their execution. In benchmarks like BrowseComp and WideSearch, K2.5 in swarm mode significantly outperforms not only its single-agent version but also competitors like GPT-5.2 and Claude 4.5 Opus. On BrowseComp with swarm active, it achieves 78.4% compared to 60.6% in standard mode. On WideSearch, it goes from 72.7% to 79%.

The configuration involves a main agent that can perform up to fifteen steps, while each sub-agent can go up to one hundred steps. It's computational orchestration that is more reminiscent of an orchestra conductor than a soloist, and the results speak for themselves: on tasks requiring deep web research, multi-page navigation, or analysis of complex datasets, the swarm approach unlocks previously inaccessible levels of performance.

This paradigm shift from single-agent scaling to swarm-like execution is perhaps Moonshot's most original contribution. While OpenAI and Anthropic continue to scale up ever larger and more expensive models, the Chinese are exploring distributed coordination methods that could render the monolithic approach obsolete. It's the difference between building ever-taller skyscrapers and designing efficient horizontal cities.
![orchestrator.jpg](orchestrator.jpg)
[Image from kimi.com](https://www.kimi.com/blog/kimi-k2-5.html)

## Benchmarks: Performance in the Field

Let's get to the numbers that really matter: how does K2.5 perform when faced with real problems? The benchmarks released by Moonshot cover an impressive spectrum: mathematical reasoning, coding, multimodal vision, long contexts, agentive search. And here, an uncomfortable but necessary premise must be made.

As Sanfilippo points out again, "they make the benchmarks themselves" and what is needed is "an aseptic and detached entity that can screen the results independently." American producers are "completely self-referential," tending to compare new models only with their own previous versions while ignoring competitors. The Chinese, on the contrary, still include data from American models in their tests "to prove they can rival them on a global scale." Moonshot is no exception: it publishes direct comparisons with GPT-5.2, Claude 4.5 Opus, Gemini 3 Pro, DeepSeek V3.2.

Let's start with reasoning. On HLE-Full (Humanity's Last Exam), one of the toughest benchmarks measuring advanced problem-solving capabilities, K2.5 scores 30.1% without tools and 50.2% with tools enabled. GPT-5.2 reaches 34.5% and 45.5%, Claude 4.5 Opus 30.8% and 43.2%. When you add the ability to use external tools, K2.5 surpasses both. On AIME 2025, the American mathematics olympiad, K2.5 achieves 96.1% averaged over thirty-two runs, against GPT-5.2's 100% but above Claude's 92.8%.

On the coding front, the results are even more interesting. SWE-Bench Verified, which tests the ability to solve real bugs from GitHub repositories, sees K2.5 at 76.8%, GPT-5.2 at 80%, Claude at 80.9%. A minimal gap. But on SWE-Bench Multilingual, K2.5 rises to 73% against GPT's 72% and Claude's 77.5%. And on Terminal Bench 2.0, which measures autonomous shell use, K2.5 reaches 50.8%, trailing GPT-5.2 (54%) but clearly beating DeepSeek V3.2 (46.4%).

The visual part is where K2.5 really shines. On MMMU-Pro, a university multimodal benchmark, it gets 78.5% against GPT's 79.5% and Claude's 74%. On MathVision, which requires solving math problems from images, K2.5 reaches 84.2%, beating GPT (83%) and Claude (77.1%). On WorldVQA, a benchmark created by Moonshot itself to test real-world visual knowledge, K2.5 scores 46.3% against GPT-5.2's meager 28%. And on video understanding, VideoMMMU sees K2.5 at 86.6%, VideoMME at 87.4%, LongVideoBench at 79.8%.

Sanfilippo, while acknowledging the risk of data leakage (datasets ending up in the training), considers "Kimi's benchmarks historically reliable" and suggests the most pragmatic solution: "Download it and subject it to ten problems invented on the spot. Only by personally verifying if the model solves new problems is it possible to understand if it's as strong as they say." The open-weights nature of K2.5 makes this empirical verification possible, unlike closed American models.
![benchmark1.jpg](benchmark1.jpg)
[Image from platform.moonshot.ai](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart)

## Open Source vs. Closed: A Geopolitical Game

And here we come to the crucial point, the one that transforms this release from a tech news item into a geopolitical event. Moonshot has released the full weights of K2.5 on Hugging Face under a Modified MIT license, which is extremely permissive. You can download the model, modify it, use it commercially. The only constraint: if you exceed twenty million dollars a month in revenue or one hundred million active users, you must explicitly cite Moonshot AI. That's it.

Compare this with the American strategy. OpenAI has closed GPT-4, GPT-5 is even more locked down. Anthropic only releases Claude APIs, zero access to the weights. Google keeps Gemini under lock and key. The approach is what some call "stratified openness": releasing minor open-source versions (Meta's Llama, Google's Gemma) but keeping the frontier models strictly proprietary. The goal is to control the ecosystem, maintain a competitive advantage, and monetize through high-margin APIs.

China is playing a different game. DeepSeek has released the weights of V3, Qwen does the same, Moonshot with K2.5 confirms the trend. Sanfilippo is explicit: "Chinese models are currently the only guarantee for a future democratization of artificial intelligence. While American companies tend to close their strongest models to dominate the market, the Chinese continue to release them."

The question is: why? It's not philanthropy. It's strategy. Releasing open-weights models creates reverse technological dependence: developers in Africa, South America, Eastern Europe start building on Chinese infrastructure. When that developer becomes the CTO of a grown startup in three years, what stack do you think they will rely on? And when European, Latin American, Asian governments have to choose national AI infrastructures, will they really think that relying completely on closed American APIs is a good strategic idea?

Sanfilippo touches this nerve: "Possession of the Kimi 2.5 weights is a protection against possible arbitrary political decisions, such as a block on access to American AI by the United States. European rulers should pay close attention to these developments as a strategic challenge." This isn't paranoia: we've seen what happened with Huawei, with TikTok, with semiconductor supply chains. Why should AI be any different?

Then there's a more subtle issue. Sanfilippo defends the concept of open-weights against open-source purists: "Having the weights and the inference code is sufficient for user freedom, it allows for continued training or the creation of independent inference systems." You don't need complete datasets and training pipelines (which nobody ever really releases, not even Meta with Llama). You need to be able to run, modify, and extend the model. And K2.5 fully allows this.

The community is responding. The Kimi team's Reddit AMA saw hundreds of questions about fine-tuning, local deployment, hardware optimizations. Together.ai has already integrated K2.5 into its platform. Developers are testing different quantizations, creating adapters for specific frameworks, publishing independent benchmarks. It's a self-sustaining ecosystem, exactly like what happened with Linux versus Windows in the nineties.

## Hardware Denied, Software Empowered

And here we arrive at the most delicious paradox of this story. The US export restrictions on advanced chips were supposed to paralyze Chinese AI. Instead, they have made it more resilient and innovative. It's like denying premium fuel to a Formula One team: they don't stop racing, they design more efficient engines.

Since 2022, the United States has progressively blocked the export to China of high-end NVIDIA GPUs: first the A100, then the H100, and recently even the H200. Chinese companies can only access "downgraded" versions like the H800 and H20, with reduced memory bandwidth and interconnect, or they must rely on still-immature domestic Huawei Ascend hardware.

The response? Software architectures that squeeze every last drop of performance from inferior hardware. DeepSeek has shown that a competitive model can be trained primarily using H800s. Moonshot with K2.5 takes this philosophy further: an extremely optimized MoE that activates only 3.2% of the total parameters for each token, native INT4 quantization that reduces memory requirements by four times, and prefill and decoding techniques that, according to the [official documentation](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart), achieve a 4.5x speedup compared to naive implementations.

Sanfilippo frames the issue perfectly: the MoE architecture of K2.5 is "deeply sparse" precisely because "for each token emitted, only 32 billion are activated, involving 8 experts out of a total of 380." This means more efficient training on less powerful H800/H20 clusters, and inference that is accessible even to those without NASA-level datacenters.

There's another aspect that deserves attention: Sanfilippo mentions the "hypothesis that DeepSeek is currently engaged in a massive Chinese government plan for training on Huawei GPUs," a possible "AI Manhattan Project" that would explain the slowdown in their public releases. If confirmed, it would mean that China is aiming for complete hardware independence within a few years. And when that happens, US export restrictions will become irrelevant.

The historical comparison that comes to mind is with the Japanese automotive industry in the 1970s. When the oil embargo hit, Toyota and Honda didn't give up: they designed more efficient engines and conquered the global market. Moonshot, DeepSeek, and Alibaba are doing the same with AI. The chip embargo is creating the Toyotas and Hondas of artificial intelligence.
![benchmark2.jpg](benchmark2.jpg)
[Image from kimi.com](https://www.kimi.com/blog/kimi-k2-5.html)

## Parallel Economies and Emerging Markets

Let's talk about money, because in the end, it's always about money. Moonshot AI is valued at $3.6 billion according to the latest estimates, with backing from Alibaba and other Chinese investors. It seems like a lot, until you compare it with OpenAI (valued at over $150 billion), Anthropic (around $30 billion), or Google and Microsoft, which have market capitalizations in the two-trillion-dollar range.

Sanfilippo notes the "strong discrepancy between form (financial valuation) and substance (technical capability)." Moonshot produces a model that competes with GPT-5 and Claude 4.5, but is worth a tenth of Anthropic and a fortieth of OpenAI. Why? Different financial markets, different VC ecosystems, but also less aggressive monetization.

Look at the API prices. According to third-party sources, K2.5 costs $0.60 per million input tokens and $2.50 for output. GPT-5.2 in thinking mode runs at $1.75 for input and $14 for output per million tokens. Claude Opus 4.5 is at $5 for input and $25 for output. K2.5 is therefore three times cheaper than GPT-5.2 and about eight times cheaper than Claude Opus 4.5 on input, with even more marked differences on output.

For a startup in Vietnam, Nigeria, or Argentina that wants to integrate AI into its products, the choice is obvious. K2.5 not only costs less, but being open-weights, you can also host it locally if you have the hardware, completely eliminating API costs and dependence on external providers. This is creating parallel economies in AI, ecosystems that are growing outside the Silicon Valley-centric circuit.

The impact on emerging markets is already visible. Indian companies are building customer service chatbots on Qwen and DeepSeek. African startups are using K2 for local educational applications. In South America, developers are fine-tuning Chinese models for specific tasks in Portuguese and Spanish. These aren't glamorous markets that end up on TechCrunch, but they are volumes that are growing exponentially.

And there's a perverse network effect (from the American perspective): the more developers learn to work with Chinese models, the more tools, frameworks, and integrations are born around these models, and the more expensive it becomes to switch to American alternatives. It's lock-in in reverse. Microsoft and Google built empires on this principle. now they find themselves on the wrong side of the barricade.

The numbers speak for themselves: according to data from Andreessen Horowitz and OpenRouter, Chinese open-source models have gone from 1.2% of global usage at the end of 2024 to almost 30% by December 2025. Nikkei reports that in November 2025, Chinese AI models accounted for about 15% of the global market share, a vertical growth from 1% the previous year. A RAND Corporation study highlights that as of August 2025, Chinese providers had captured over 10% of users in thirty countries and over 20% in eleven countries, mainly in Asia, Africa, and South America. Alibaba's Qwen has surpassed seven hundred million downloads on Hugging Face, becoming the most used open-source AI system in the world. Not enough to dethrone OpenAI or Google in Western markets, but enough to make any global monopoly impossible.

## Open Questions About the Future

Let's close with questions, because in the AI of 2026, certainties are a rare commodity and questions are more useful than pre-packaged answers. First issue: alignment. Chinese open-weights models follow different safety guidelines than American ones, inevitably reflecting the cultural and political values of the context in which they are born. When K2.5 is fine-tuned by a Nigerian or Argentine startup, who guarantees that the original alignments will persist? Who decides which guardrails are necessary and which are censorship?

Second issue: the roadmap. Moonshot is already talking about K3, DeepSeek is working on V4, Alibaba continues to iterate on Qwen. The release speed is impressive, but is it sustainable? Training these models requires monstrous energy and huge datacenters. China has low-cost energy (coal, nuclear, expanding renewables), rapidly being built datacenters, and a pool of computer science PhDs larger than Europe and the US combined. But can it maintain this pace while facing an economic slowdown and growing geopolitical tensions?

Third issue: regulation. Europe has approved the AI Act, which classifies models above certain parameter and capability thresholds as "high-risk," requiring stringent compliance. K2.5 far exceeds those thresholds. Will Moonshot have to certify the model for the European market? And if it does, does that mean that open-weights will have different versions for different jurisdictions, undermining the very concept of "open"?

Fourth issue: national security. If Western governments begin to perceive Chinese models as vectors of strategic influence, we could see restrictions on the use of K2.5, DeepSeek, and Qwen in sensitive sectors. Some US government agencies already prohibit Chinese software on official devices. Extending this ban to AI models would be technically complex but politically plausible. And at that point, the bifurcation of the global AI ecosystem becomes permanent.

Fifth issue: the Huawei factor. If China truly succeeds in developing Ascend GPUs that are competitive with NVIDIA, the dynamics change completely. No longer software optimization to circumvent hardware limitations, but independent end-to-end capability. Sanfilippo speculates that DeepSeek is already working on massive training with Huawei chips, a government-led "Manhattan Project." If true, in twelve to eighteen months we could see Chinese models trained entirely on domestic hardware, immunized from any future embargo.

Finally: the question of truth. How do we verify the real performance of these models? Sanfilippo suggests independent empirical testing, but who has the resources to do it systematically? What is really needed is a CERN for AI, a neutral international body that tests models under controlled conditions and publishes verifiable results. Until it exists, we navigate between self-referential claims and potentially leaked benchmarks.

## A Checkmate Worth the Game

Let's return to the initial image, that of the chess game. The United States moved with the technology embargo, thinking it would put China in check. China responded with a series of unexpected counter-moves: more efficient software architectures, strategic open-weights releases, developer ecosystems growing outside Silicon Valley's control. Kimi K2.5 is one of these counter-moves, and it won't be the last.

The ridiculous market valuation compared to its technical capabilities, according to Sanfilippo, tells a deeper story: "Moonshot AI is worth $3.6 billion, a very low figure compared to the off-the-charts valuations of OpenAI or Anthropic, despite the model's quality being comparable." The Western financial market has not yet processed that AI will not be an American monopoly, that alternative trajectories exist, that software can (and has) compensated for hardware limitations.

The release of K2.5 doesn't end the game, it opens new phases. Global developers now have access to advanced multimodal capabilities, agent swarms, vision-based coding, without depending on American APIs or enterprise budgets. Governments have strategic options that don't involve technological submission to Washington. Researchers can study, modify, and extend a frontier model without asking for permission or signing impossible NDAs.

The open questions are many, the certainties few. But one thing is clear: the geography of artificial intelligence is being redrawn, and to think that this redrawing can be stopped with export controls is as naive as thinking an oil embargo would have stopped Toyota in the seventies. Technological history rewards those who innovate under constraints, not those who protect their established positions.

Moonshot AI, as the name suggests, is shooting for the moon. Whether it will actually get there is too soon to say. But in the meantime, while we watch, they are building better and better rockets with materials that shouldn't be enough. And that, in itself, is already something worth following.
