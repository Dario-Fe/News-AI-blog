---
tags: ["Research", "Training", "Applications"]
date: 2026-08-03
author: "Dario Ferrero"
---

# DwarfStar: the dwarf star illuminating local frontier AI
![dwarfstar-antirez.jpg](dwarfstar-antirez.jpg)

*There is a scene in William Gibson's novel *Neuromancer* where the protagonist connects directly to an immense intelligence, distributed over inaccessible servers, through a connection he does not control and does not own. It was science fiction in 1984. In 2026, it is, more or less, the daily reality for anyone using ChatGPT, Claude, or Gemini: gigantic models, hosted on billion-dollar infrastructures, reachable only through an internet connection and for a monthly subscription or a cost per token. Your conversation, your data, your reasoning: everything passes through somewhere you don't see and don't manage.*

DwarfStar is, in its essence, an attempt to overturn this equation. Not a commercial alternative, not a wrapper around something else: an inference engine written from scratch, in C, obsessively optimized for a single model, distributed for free under the MIT license. And behind it is a signature that the tech community recognizes immediately: that of Salvatore Sanfilippo, alias *antirez*, the Sicilian programmer who invented Redis in 2009.

## Antirez: the programmer who does one thing, and does it well

Salvatore Sanfilippo was born in Campobello di Licata, Sicily, on March 7, 1977. He developed an interest in programming from a very young age, starting to write code at the age of five on a Texas Instruments computer given to him by his father. From then on, it's a story of fruitful diversions: he left architecture for computer science, moved into network security in the nineties, invented the *idle scan*—a stealthy network port scanning technique still implemented in nmap today—and then, almost by chance, built Redis.

Redis is an open-source in-memory data store, created by Sanfilippo and first released on February 26, 2009. Instead of just being a key-value cache, it offers rich native data structures—strings, hashes, lists, ordered sets, streams—operated atomically by the server. The philosophy governing it is the one antirez brings to every project: do less. A small and simple system you can keep in your head beats a large and complete system.

Redis is today used by practically every internet company, from Airbnb to Uber, from Snapchat to Meta, to Amazon and Twitch. Despite this, Sanfilippo has always chosen to live in Catania, far from the frenzy of Silicon Valley, prioritizing family and intellectual stimuli. In June 2020, he announced his retirement from Redis maintenance to dedicate himself to other projects, only to return in December 2024 in the role of Redis evangelist, developing the new Vector Set data type.

The respect the tech community holds for him doesn't derive only from the technical greatness of Redis. It derives from something rarer: consistency. Antirez doesn't chase trends, doesn't accumulate startups, doesn't monetize his reputation. He writes software because he likes writing software, and when something interests him, he builds it with almost artisanal care. DwarfStar is exactly that.

## The problem: frontier models live on Saturn

To understand what makes DwarfStar an extraordinary project, one must first understand the problem it addresses. The most capable language models, DeepSeek V4 Flash, but also the various GPTs and Claudes, are not small programs. They are neural networks with hundreds of billions of parameters, each of which is a floating-point number that takes up space in memory. A model like DeepSeek V4 Flash has 284 billion total parameters. If we wanted to load them all into memory in their original full-precision form, we would need about 568 gigabytes of RAM. The RAM of high-end GPU servers, the famous VRAM of NVIDIA cards, is measured in tens of gigabytes per card. Multiple network-connected machines would be needed, infrastructures costing tens of thousands of euros, electricity consumption like a small industry.

The 128 GB MacBook, which it must be said is not within everyone's reach, still seems light-years away from this reality. Yet DeepSeek V4 Flash belongs to a family of architectures that contains, hidden in its structure, the key to the solution.

## Mixture of Experts: when specialization becomes an advantage

DeepSeek V4 Flash is built on an architecture called Mixture of Experts, or MoE. The idea, now well-known, is quite intuitive: instead of having a single dense neural network that processes every token, the model is composed of dozens of specialized networks, the "experts," and for each token only some are activated, selected by a routing mechanism. DeepSeek V4 Flash has 284 billion total parameters but only 13 billion parameters active for each generated token. It's like having a thousand-volume encyclopedia, but only having to read a few books to answer a specific question.

This has a huge practical consequence: generation speed does not depend on all 284 billion parameters, but only on the 13 billion active ones. And this is where the first great intuition of DwarfStar kicks in.

The 2-bit quantizations provided for DwarfStar are not a shortcut: they behave well, work with code agents, and execute tool calls reliably. The 2-bit quantizations use a very asymmetric compression: only the routed MoE experts are quantized, gate and up to IQ2_XXS, down to Q2_K. These constitute most of the model's space: other components, shared experts, projections, routing, are left intact to ensure quality.

In concrete terms: the parts of the model that are used often and carry more "signal" are preserved at the original precision. Experts that are rarely activated and contribute less to the quality of the final result are compressed aggressively. The result is a GGUF file of about 81 gigabytes that maintains quality surprisingly close to the original model. But how is it determined which part of the model carries more signal? Through an empirical process called *imatrix calibration*: the model is run on real datasets covering coding, mathematics, reasoning, and tool calling, and how the various parts of the network activate is measured. This importance map then guides the compression decisions.

It's the difference between cutting a tree with a chainsaw and pruning it with care. The difference is a living plant instead of a dead one.

## When RAM is not enough: the disk as an extension of memory

Even with 81 gigabytes of compressed weights, the problem is not entirely solved. A MacBook with 64 or 96 GB of RAM must find a way to manage a model that doesn't fit completely. And the context, the memory of the ongoing conversation, takes up additional space as the conversation grows.

DwarfStar introduces an SSD streaming mode only for Metal: in this mode, unrouted weights remain resident, while routed MoE experts are kept in an in-memory cache and loaded from the GGUF file when a cache miss occurs. Streaming is not as fast as loading the entire model into RAM, but it's useful because routed experts dominate the model's size and modern Mac SSDs are fast enough to make cache misses tolerable.

The mechanism is elegant in its conceptual simplicity: DwarfStar keeps the most frequently called experts' weights in RAM—the "hot" ones—and loads the others from the disk only when the router decides to activate them. Modern NVMe SSDs, those mounted on MacBooks and Mac Studios, reach sequential read speeds in the range of 7-10 GB/s. Fast enough not to make loading the main bottleneck, at least for tasks that don't require minimum latency.

This means that, in practice, a 64 GB MacBook can execute a model with 284 billion parameters. Not at the same speed as a Mac Studio with 512 GB of unified RAM, certainly, but at a speed sufficient for real work.

## Context, sessions, and memory that survives reboot

Modern language models talk about "context windows" as if they were obviously unlimited. They are not. Every token in the conversation takes up space in the KV cache, the data structure the model uses to remember what has been said, and the KV cache grows linearly with the length of the context. DeepSeek V4 Flash has a context window of 1 million tokens, and the KV cache is incredibly compressed, allowing inference on long contexts on local computers and the persistence of the KV cache on disk.

DwarfStar exploits this feature with a persistent session system on disk. When a conversation is interrupted, the server is restarted, a session is changed, one wants to resume work the next day, the system does not have to re-process all previous tokens from scratch. The saved session contains the exact state of the KV cache, the token checkpoint, even the probability distribution of the last generated token. Resumption is almost instantaneous.

This solves one of the most frustrating problems of local AI agents: the fact that every new API call must re-send the entire context, paying the computational cost of the *prefill* every time. With DwarfStar, expensive prefills are saved and reused. A code agent using a system prompt 25,000 tokens long, as Claude Code does, pays that cost only once.

## Two machines are worth more than one

The most recent point in DwarfStar's evolution concerns the distribution of inference over multiple machines. The distributed branch is now in the main code: distributed inference moves from theory to executable code. The GGUF file resides on each machine, but each node loads only its portion of layers through the --layers flag with inclusive ranges, without keeping the weights that don't belong to it in RAM. Coordinator/worker architecture: one machine acts as coordinator (tokenization, sampling, and the initial prompt), the others are workers that process their own portion and forward activations via TCP.

The approach is that of *layer split*: machine A loads and processes the first N layers of the transformer, passes the activations to machine B which processes the remaining layers, and the result returns to the coordinator for sampling. Data transfer between machines is minimal because only intermediate activations are transferred—relatively small vectors—and not the model weights.

With DwarfStar, a 512 GB M3 Ultra Mac Studio can execute DeepSeek V4 PRO at 150 tokens/s of prefill and about 10-13 tokens/s of decoding—not exceptional but at a level usable for certain use cases. Two connected Mac Studios could distribute the larger model, DeepSeek V4 PRO at full precision, and enjoy a faster prefill thanks to micro-batching. Those with two 128 GB M5 Max MacBooks can now split the load of a single model instead of using them separately.

Antirez is also exploring more experimental approaches: the ensemble of models, where two instances of the same (or different) models run on separate machines and combine their logits—the probability distribution on subsequent tokens—to produce an output better than what each would produce alone. It is a technique studied in literature but rarely implemented in a practical way.

## The numbers: what to expect in practice

DwarfStar benchmarks are measurable and published in the official project documentation. On a 128 GB M3 Max MacBook Pro with 2-bit quantization:

On short prompts, prefill reaches 58.52 tokens/s and generation 26.68 tokens/s. On long prompts of about 11,700 tokens, prefill rises to 250.11 tokens/s thanks to chunked prefill, while generation drops to 21.47 tokens/s due to the growing context.

On a 512 GB M3 Ultra Mac Studio, the numbers are more generous: prefill at 84.43 tokens/s on short prompts, generation at 36.86 tokens/s, and on long prompts, prefill reaches 468.03 tokens/s with generation at 27.39 tokens/s.

The 128 GB M5 Max MacBook, according to antirez, can execute DeepSeek V4 Flash in 2-bit quantization at about 460 tokens/s of prefill and 25 tokens/s of generation, with an acceptable degradation curve as the context increases.

To give a concrete reference: reading aloud means pronouncing about 150 words per minute, corresponding to about 200 tokens. At 26 tokens per second, DwarfStar generates text at just over an eighth of that speed—slow compared to cloud services, but fast enough for real interactive use.
![tabella1.jpg](tabella1.jpg)
[Image from the GitHub repository](https://github.com/antirez/ds4)

## GLM 5.2 and the project's direction

DwarfStar was born as a deliberately narrow engine: a single family of models, supported deeply and correctly instead of supporting everything superficially.

But ambitions grow. In the last few hours, antirez published a video titled "Considerations on the implementation of GLM 5.2 in DwarfStar". It is explicitly a work in progress, the signal is clear: the project does not intend to stop at DeepSeek. The MoE architecture with compressed KV cache has become a feature shared by multiple frontier models, and DwarfStar is equipped to chase it.

It must be said honestly: the project is still in beta quality, as antirez himself declares in the README. Some features are experimental, CUDA support is more recent than Metal support, and certain behaviors might change. But the trajectory is that of a project that has already demonstrated how to do things that seemed impossible a few weeks ago.

## The frontier, open to everyone (almost)

There is a word that recurs obsessively in any discussion about DwarfStar: *democratization*. It is an overused word, often used to cover commercial products with a veil of progressive rhetoric. Here, the term has a more precise and honest sense.

DwarfStar is free. The code is MIT. The quantizations are published on Hugging Face without restrictions. There is no Pro version, there is no Enterprise plan, there is no API key to buy. Anyone with a Mac with 96 GB of RAM or a $5,000 DGX Spark, or even less with SSD streaming, can download everything and have an AI agent with almost 300 billion parameters running locally, offline, without sending a single token to a remote server.

Privacy is not a secondary argument. An agent that knows your company's code, your documents, your internal conversations should not necessarily transit through Anthropic or OpenAI servers. With DwarfStar, it doesn't.

Of course, hardware remains a real obstacle. 128 GB of unified RAM is not a fifty-euro configuration. An M3 Max MacBook Pro in the required version starts at about 4,000 euros; a 192 GB M3 Ultra Mac Studio exceeds 7,000. It is not within everyone's reach, and it is honest to say it. But it is within the reach of many professionals, studios, SMEs, researchers. And the cost of the same computational power in the cloud, on an annual basis, significantly exceeds the cost of the hardware, not to mention the value of privacy and independence.

Then there is a more subtle dimension. Every time a frontier model runs on consumer hardware, every time someone demonstrates that a data center isn't needed for serious reasoning, the inclined plane shifts slightly. Hardware improves: the M5 Max MacBook with 128 GB is already the best cost-performance balance available for local inference in 2026. Models improve and become more efficient. And there are people like Sanfilippo who work, for the taste of it, for the satisfaction of doing it well, to further narrow the gap.

Redis took years to become the most loved database in the world. DwarfStar already has 15,500 stars on GitHub just a few weeks after its launch, with active contributors, ports for CUDA and ROCm, benchmarks published on DGX Spark, MacBook, and Mac Studio. The speed of adoption says something about the urgency of the need it satisfies.

There is a character in Alan Moore's comic *From Hell*—not the Hollywood version—who observes that time is always now, that everything happens simultaneously. The past of the local AI movement and its future touch in an 81-gigabyte file that you can download now, on a computer you have on your desk. Antirez built it. The rest, as they say, is history.

---

*The official DwarfStar repository is available on [GitHub](https://github.com/antirez/ds4). Official quantizations for DeepSeek V4 Flash are published on [Hugging Face](https://huggingface.co/antirez/deepseek-v4-gguf). Salvatore Sanfilippo's blog can be reached at [antirez.com](https://antirez.com).*
