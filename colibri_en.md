---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-07-20
author: "Dario Ferrero"
---

# Colibrì: the mini engine that runs a 744B model on consumer hardware
![colibri.jpg](colibri.jpg)

*Every week, the local open-source artificial intelligence community seems to look for its favorite conversation topic, and the one that just passed seems to have elected a GitHub repository with a curious name and an almost absurd promise: running GLM-5.2, a 744-billion-parameter Mixture-of-Experts model, on a computer with just 25 GB of RAM. The project is called [Colibrì](https://github.com/JustVugg/colibri) and is the work of a single developer, JustVugg, who in the acknowledgments section of his README admits with disarming honesty that he wrote and tested everything on a twelve-core laptop. No lab, no cluster, no hardware sponsorship. Just a technical obsession carried to its conclusion.*

It must be said immediately, with the same honesty that the author reserves for his own work: Colibrì is not designed for a mass audience, it is not a product and does not aspire to become one. It is an experiment, in the most classic sense of the term, of someone who wants to discover where the physical limit of a consumer machine really lies when asked to support a model that, under normal conditions, would require hundreds of gigabytes of dedicated memory. And it is precisely this experimental framework, more than the performance itself, that makes it interesting to recount.

## What's inside the engine

The heart of Colibrì lies in a single C file of about 2,400 lines, `glm.c`, accompanied by some minimal headers. Zero external dependencies, zero linear algebra libraries like BLAS, zero Python runtime during the actual inference (Python comes into play only in the model's offline conversion phase, a task it performs once and then leaves the scene). it's a setup that recalls the philosophy of certain historic computer science projects, where the choice to write less code, but write it well, becomes a statement of intent in itself.

There is something, in this minimalist stubbornness, that brings to mind certain musical productions of the British IDM scene of the nineties: few instruments, rigid rules, yet surprisingly complex results that emerge from a system deliberately poor in elements. Colibrì works more or less like this: a tiny engine that orchestrates a colossal model, no frills, no superfluous levels of abstraction, with the declared goal of running exactly one architecture, GLM-5.2, and doing so with verifiable fidelity compared to the original implementation in `transformers`.

## GLM-5.2, the monstrous model

To understand why this feat makes technical sense, one must first understand what "744 billion parameters" really means. GLM-5.2 is a Mixture-of-Experts model, an architecture where the network doesn't process every token with its entire capacity but sorts it among thousands of specialized sub-networks, called experts, activating only a small part of them for each generated token. In the case of GLM-5.2, the routable experts are 21,504, distributed over 75 MoE layers of 256 experts each plus an additional head for speculative decoding, for a grand total of 19,456 experts according to the count the project itself uses in its dashboard. Of all these, only about 40 billion parameters are actually activated for each individual token, and of these just 11 GB really change from one token to another—the ones routed by the router.

It is a crucial distinction, because it means that the problem is no longer "how do I keep 744 billion parameters in memory," but "how do I get just the 11 GB that are really needed this instant to the processor in a timely manner." It is the same principle, applied with extreme radicalism, that governs other MoE inference engines born in these weeks, and it's worth keeping in mind when we later compare Colibrì with a conceptual cousin born near Redis.
![immagine1.jpg](immagine1.jpg)
[The Colibrì web dashboard, image from the GitHub repository](https://github.com/JustVugg/colibri)

## The three-level memory hierarchy

The technical idea that supports the whole project is, after all, simple to explain with an analogy. Imagine an endless library where the part of the catalog you consult every day is on your desk, the one you need every now and then is on a shelf in another room, and the one you rarely open is in an external warehouse from which it must be requested specially. Colibrì treats VRAM, RAM, and disk exactly like three levels of this same library, managed as a single memory hierarchy.

The dense part of the model—attention, shared experts, embeddings, about 17 billion parameters—always remains resident in RAM in int4 format, occupying about 9.9 GB. The over 21,000 routed experts, instead, live on disk in an int4 container weighing a total of about 370 GB, and are dynamically loaded only when the model's router decides to activate them, thanks to an LRU cache for each layer, an optional "hot store" for the most used experts, and the operating system's page cache that acts as a free intermediate level. It is at this point that the bottleneck shifts, in an almost philosophical way, from calculation to reading: it's no longer the CPU that decides how fast you are, it's the disk.

## Minimum hardware, realistic expectations

Colibrì runs on Linux, WSL2, macOS and, since its most recent evolution, also on native Windows 11 thanks to a specifically written compatibility layer. A processor with AVX2 support, at least 16 GB of RAM, and about 370 GB free on a local NVMe drive are required, never on a network share. It's not a trivial requirement, but it's still orders of magnitude more affordable than the GPU cluster that would be needed to load the same model in its entirety at full precision.

The most important distinction, however, does not concern the minimum hardware but the difference between "it works" and "it is practicable." Colibrì works even on the most modest configuration tested by the author—twelve cores and 25 GB of RAM behind a WSL2 virtual machine with a disk that reads at about 1 GB per second. But at that speed, the model produces responses at a rate between 0.05 and 0.1 tokens per second from cold cache, a value that makes the experience more like a telegram than a conversation. It is a project designed to be pushed further, not to be used as is on the starting configuration.

## The honest performance numbers

The project README dedicates an entire section, titled without irony "honest numbers," precisely to clarify this distance between theory and practice. On the development machine, a cold start costs about 11 GB of disk reads for each generated token, which means that speed depends almost entirely on the throughput of the disk itself: with a physical limit of about 1 GB per second on that configuration, the result is precisely the aforementioned 0.05-0.1 tokens per second.

Things change significantly as the community has started testing Colibrì on more capable hardware, and here the data collected in the repository issues becomes the project's true lab. On a Ryzen AI Max with 128 GB of RAM, speed rises to about 0.37-0.40 tokens per second once the cache has warmed up. On a Mac with an M5 Max chip and 128 GB of unified memory, one reaches about 1 token per second with the base configuration, and over 2 tokens per second by enabling the experimental Metal backend. The most extreme datapoint comes from a rack of six RTX 5090 cards connected together, where keeping the entire expert pool resident between VRAM and RAM reaches 6 tokens per second in decoding on a single request—a figure that starts to approach truly conversational use, although obtained with a hardware investment that is no longer consumer.

An interesting technical detail concerns the native speculative decoding of GLM-5.2, the so-called MTP, in which a small additional head of the model tries to guess the next tokens in advance, which the main engine then verifies in a single pass. It works only if that head is quantized at 8-bit instead of 4: with the wrong precision, the acceptance of the proposed tokens collapses to zero, while with the correct one it rises between 39 and 59 percent, bringing up to 2.8 tokens generated for each model pass. It's the kind of apparently tiny detail that, on such a stretched-to-the-limit system, makes the difference between a usable project and one that stalls without apparent reason.

## The cache that learns

One of the most fascinating aspects of Colibrì, from a purely conceptual point of view, is that the engine observes itself while working and learns from its own usage patterns. Each chat session updates a file that records which experts were actually activated, and at the next restart, the engine uses that history to decide which experts to keep pre-loaded in the available RAM. The more you use it, the more the machine becomes, in a very literal sense, accustomed to your conversations.

Added to this is a predictive prefetch mechanism, still experimental, that exploits an interesting regularity discovered in the router's behavior: the state of a layer after attention allows correctly anticipating 71.6 percent of the experts that will be activated by the next layer, a value measured by the project's contributors themselves. A dedicated I/O thread can therefore start reading the next layer's experts from the disk while the current one is still calculating, overlapping reading time and calculation time instead of summing them in sequence.
![immagine2.jpg](immagine2.jpg)
[The Colibrì brain page, image from the GitHub repository](https://github.com/JustVugg/colibri)

## A place of its own in the local landscape

Colibrì is not born in a vacuum. In the same weeks, another project has catalyzed the attention of the local inference community with a surprisingly similar philosophy: DwarfStar (codenamed DS4), the engine written by Salvatore Sanfilippo, alias antirez, the creator of Redis, of which I spoke [on Codemotion](https://www.codemotion.com/magazine/it/intelligenza-artificiale/dwarfstar-la-stella-nana-che-illumina-lai-di-frontiera-locale/). DwarfStar is also a C engine written from scratch, manically optimized for a single model, and there too the strategy to bypass consumer memory limits passes through a combination of aggressive quantization and expert streaming from disk on Mac with Metal architecture.

The differences, however, are just as instructive as the similarities. DwarfStar focuses on DeepSeek V4 Flash, a more compact MoE model with 284 billion total and 13 billion active parameters, and compresses it down to a GGUF file of about 81 GB thanks to an asymmetric quantization empirically calibrated on the weights that really matter. Colibrì, on the contrary, chooses the opposite and more radical path: it does not compress the model to fit in the available RAM, it leaves it huge—about 370 GB on disk—and instead builds an entire caching and streaming system to manage its immensity without compromising its declared precision. Where DwarfStar says "I make the model smaller because RAM is what it is," Colibrì says "I leave the model large as it is and reinvent the way memory touches it." They are two different answers to the same question, and compared they tell better than any benchmark how alive the ferment around the local inference of frontier models is right now.

There is then a scale difference worth highlighting: DwarfStar works on a 284-billion-parameter model designed for high-end Apple hardware, with benchmarks reaching 25-36 tokens per second in generation on Mac Studio. Colibrì tackles a model nearly three times larger—744 billion parameters—and does so in the most hostile condition possible: a generic PC with limited RAM and any disk, consequently obtaining much more modest numbers. It's not a peer comparison, and it's right to say it clearly, but it is precisely the distance between the two approaches that makes evident how much maneuver space between "model compression" and "intelligent memory streaming" is still to be explored.

## Why it matters, beyond the demo

Beyond the immediate technical fascination, Colibrì touches on a theme that in recent months has returned to the center of the artificial intelligence debate: technological sovereignty, i.e., the concrete possibility of executing capable models without depending on a third-party cloud infrastructure. A model that runs entirely on your own hardware, however slowly, does not send a single byte of conversation to an external server, and this for certain contexts—research, development of proprietary tools, experimentation on sensitive data—has a value that goes beyond simple technical curiosity.

Colibrì also suggests something broader about the future of MoE models on consumer hardware: that the path to democratizing access to frontier models does not necessarily, or only, pass through making them smaller. It also passes through radically rethinking how memory is managed, treating RAM, VRAM, and disk as a single fluid resource instead of as watertight compartments. It's an intuition that, if it were to mature beyond the experimental stage, could influence how the next inference runtimes are designed, well beyond the scope of a single personal project.

## The still-open nodes

It would be dishonest towards readers and towards the very spirit of the project to close without listing the criticalities that Colibrì still carries with it. Speed in cold cache conditions remains very low, at the limit of unusable for any task requiring quick responses. Dependence on storage performance is total: those without a truly fast NVMe will see numbers hardly distinguishable from a timeout. Then there is the still-open question of accuracy: a first quality benchmark conducted by the community measured a score of 62.5 percent on a standard test battery, significantly lower than the 85-95 percent published for the original full-precision version of the model, although the author himself calls for caution, pointing out that the evaluation method used structurally penalizes a model designed to reason step by step, and that a direct and controlled comparison between the two precisions is still needed to truly isolate the cost of quantization from measurement noise.

Finally, a more prosaic observation must be added: usability for a non-technical audience is, at present, almost nil. Configuring Colibrì means downloading hundreds of gigabytes, converting weights, reading environment variables and interpreting diagnostic logs. It is a tool for those who already know what they are doing, not a ready-to-use application, and independent benchmarks on more varied hardware are needed before we can say with certainty how representative the published numbers are outside the artisanal lab in which the project was born.

## Conclusions

Colibrì does not demonstrate that huge models have become comfortable to use on any computer, and it would be misleading to tell it that way. Rather, it demonstrates that the boundaries of local inference can be pushed much further than most insiders would have bet until a few weeks ago, treating memory scarcity not as an insurmountable obstacle but as a design constraint to be bypassed with engineering creativity. It is an important project to recount precisely because, together with parallel experiments like DwarfStar, it shows where the open-source AI ecosystem is really going right now: not towards a single definitive solution, but towards a plurality of strategies—those who compress the model, those who reinvent memory—that confront each other openly on the same ground.

Colibrì is not the future of local AI for everyone, but it is a clear sign of how runtimes are becoming more creative in overcoming the physical limits of hardware.
