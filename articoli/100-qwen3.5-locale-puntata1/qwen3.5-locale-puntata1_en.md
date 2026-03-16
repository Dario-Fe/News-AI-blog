---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-16
author: "Dario Ferrero"
---

## AI at Home: LM Studio and Qwen 3.5 on My PC - Episode 1
![qwen3.5-locale-puntata1.jpg](qwen3.5-locale-puntata1.jpg)

*There is a precise moment when a technology stops being a promise and becomes a tool. It's not when the press release comes out, it's not when the benchmarks go viral on social media, but when an ordinary person, with an ordinary PC, sits down, downloads something, and decides to really understand what is happening. This article is that moment, at least for me.*

Over the past two weeks, only one name has dominated conversations in the open-weight artificial intelligence ecosystem: Qwen 3.5. On March 2, 2026, the Alibaba team released the small series of the model, variants from 0.8 to 9 billion parameters, all under the Apache 2.0 license, all executable on consumer hardware, and the community's reaction was immediate and lively. But before getting into the details of the model and my personal experiment, it is useful to understand why this moment has arrived right now.

## The Wind Changes Direction

In an article published a few weeks ago on this portal, [I analyzed the reasons why 2026 is shaping up to be the year of Small Language Models](https://aitalk.it/it/slm-2026.html): the convergence of pressures on energy costs, increasingly stringent privacy demands, and a qualitative leap in architectural efficiency that has redrawn the boundary between "possible on cloud" and "possible locally." It's not an ideological trend; it's a pragmatic response to real constraints.

The data, however, still tells a story of two speeds. As emerges from the [analysis of the DigitalOcean Currents report also published here](https://aitalk.it/it/agenti-al-lavoro.html), 64% of companies today integrate models through third-party provider APIs, and only 21% use open-weight models in production. The cloud is not dead: it is still dominant. But what seemed like an insurmountable asymmetry between huge proprietary models and "fallback" local models is narrowing with a speed that surprises even the most attentive observers.

On benchmarks like [GPQA Diamond](https://huggingface.co/datasets/Idavidrein/gpqa), the reference test for advanced university-level reasoning—198 questions in physics, chemistry, and biology—Qwen3.5-9B scores 81.7, surpassing OpenAI's GPT-OSS-120B which stops at 71.5, as reported on the [model's official page on HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B). We are talking about a model with thirteen times fewer parameters. It is not an incremental optimization: it is a paradigm shift in what "small" means in 2026.

Reactions in the sector have been significant and, as often happens in this field, not unanimous. Some leading observers welcomed the release with enthusiasm, highlighting the density of capabilities relative to size. Others, Anthropic first and foremost, maintained a more cautious tone, noting that models optimized to perform on benchmarks do not always transfer those capabilities to the real world with the same fidelity. A tension that runs through the entire debate on open-weight AI and that no number on a table definitively resolves. The truth, as always, lies in the use.

And that is exactly why I decided to get my hands dirty.

## An Honest Experiment, without Scientific Pretensions

Before proceeding, it is necessary to be clear about what this article is and what it is not. What follows is a personal experiment, conducted by an enthusiast who wants to understand what can be achieved with ordinary means at this precise historical moment. There is no peer-reviewed testing protocol, there is no statistically significant sample of prompts, there is no reproducible method that would stand up to the scrutiny of an academic conference. The tests were verified by cross-referencing the results with frontier models like Claude and DeepSeek, but this does not turn them into scientific benchmarks: they remain field tests, conducted with the tools of an advanced user, not a researcher.

The value, if there is any, lies exactly in this: understanding how far you can get with good but non-doctoral knowledge, with private hardware, and the will to understand before buying. Those who want certified numbers will find the official benchmarks on the [model's HuggingFace page](https://huggingface.co/Qwen/Qwen3.5-9B). Those who want to know how it runs on a 2025 PC purchased at a reasonable price, keep reading.

## The Laboratory: An Intermediate-Level PC

The machine on which I conducted the tests is neither a professional rendering workstation nor a competitive gaming rig. It is a PC assembled with judgment but without exaggeration: AMD Ryzen 7700 processor, 32 GB of DDR5 RAM, and above all an AMD Radeon RX 9060 XT GPU with 16 GB of VRAM. A configuration that many advanced users, gamers, content creators, developers working from home, might recognize as their own. Mid-to-high-end hardware in the consumer segment, but far from the A100 imagined when talking about local inference on language models.

This choice is not accidental. The mid-range of the configuration is precisely the point. If a model runs well here, it runs well on a huge slice of already existing PCs. If it struggles here, that slice narrows considerably.

## Choosing the Framework: LM Studio versus Ollama

To run a language model locally, you need two things: the model itself (a file of a few gigabytes) and a framework that acts as an interpreter between the hardware and the model, managing memory, tokenization, and inference. Without this intermediate layer, downloading a model's weights is like having the files for a movie without a video player.

The two paths that dominate this space in 2026 can be represented by [LM Studio](https://lmstudio.ai/) and [Ollama](https://ollama.com/), and the difference between them reflects a classic tension in software: accessibility versus control.

[Ollama](https://ollama.com/) is the tool for developers. It is installed with a single line in the terminal, exposes an OpenAI-compatible REST API on `localhost:11434` by default, and integrates seamlessly into scripts, pipelines, and applications. It is open source, has a large community, and its minimalist philosophy—one command to download, one command to run—makes it the preferred backend for dozens of third-party applications. In terms of raw performance, it tends to be faster, handles concurrent requests better, and consumes fewer resources thanks to the absence of graphical overhead. The flip side: it requires familiarity with the terminal, advanced configuration goes through Modelfiles, and its native graphical interface arrived late and remains minimal. There is also a question of transparency worth noting: Ollama is open source and the community trusts its conduct, while LM Studio is closed source—a detail that those particularly concerned with privacy should keep in mind.

[LM Studio](https://lmstudio.ai/) plays in a different field. It is a desktop application with a polished graphical interface, available for Windows, macOS, and Linux. It allows searching, downloading, and loading models without opening a terminal, also exposes an OpenAI-compatible API for those who want to integrate it into other tools, and automatically manages GPU acceleration on NVIDIA, Apple Silicon, and AMD hardware. But the detail that truly changes the experience for those coming to local AI without a developer background is this: at the time of selecting a model, LM Studio shows a real-time estimate of the expected performance on your hardware configuration, with color indicators that immediately communicate if the model will run smoothly, with limitations, or if the hardware is insufficient. For an individual experimenting, this eliminated friction is worth any potential performance gap compared to Ollama.

The choice for this experiment fell on LM Studio for pragmatic reasons: the ability to see in advance if Qwen 3.5 9B Q8_0 would run at full speed on my GPU, without manual calculations or technical documentation to consult, allowed me to optimize the choice immediately. For those who instead intend to integrate a model into an application, automate workflows, or work in a server environment, Ollama remains the solid choice.
![lmstudio.jpg](lmstudio.jpg)
*Screenshot of my PC at LM Studio startup. In the top right menu, the software options with the bottom button to select and download the desired model. Next to it, the chat history. In the bottom center, the dialog box for prompts, where the selected model can be seen.*

## Installing LM Studio: Five Minutes and You're Off

The installation does not require special technical skills. From the [official site](https://lmstudio.ai/), you download the installer for your operating system—an executable for Windows, a DMG for macOS, an AppImage for Linux—and proceed as with any other desktop application. No external dependencies to install, no virtual environments to configure, no terminals to open. The package weighs about 500 MB; the first screens guide you through the configuration of the automatically detected hardware acceleration, and in a few minutes, you are facing the main screen.

From there, the model search section allows you to browse the catalog, which draws primarily from HuggingFace, filtering by size, quantization type, and declared hardware compatibility. Selecting a model brings up performance estimates on your machine: this is where you immediately understand what you can expect before downloading even a single gigabyte.

## Why Qwen 3.5 9B, and Why Q8_0

With the framework installed, the choice of the model is the second critical junction. I chose Qwen 3.5 9B in Q8_0 quantization—the file occupies just over 10 GB on disk—for reasons worth explaining, as they reflect a logic useful for anyone approaching this choice.

The 9-billion-parameter size has become the de facto standard for field tests in this period: it is the most common size among all major competitors releasing open-weight models, represents the point of balance between capacity and hardware requirements, and allows for meaningful comparisons between different families. The 27B and 35B variants are certainly more capable, but they require more expensive hardware, which for an individual represents a non-trivial jump. For even a small company, however, evaluating a 9B model has double value: understanding what you get immediately with minimal investment, and projecting what you could get with an hardware step up, given the pace at which performance grows and requirements drop.

The choice of Q8_0 quantization, the highest among the three options available in LM Studio for this model, was made possible specifically by the 16 GB of VRAM: the green indicator confirmed that the model would run entirely on the GPU without having to offload layers to system RAM, ensuring maximum inference speed and response quality not degraded by the numerical approximations of more aggressive quantizations.

On a technical level, Qwen 3.5 is not simply a shrunk-down previous model. As described in the [official documentation on HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B), the architecture adopts a hybrid approach that combines Gated Delta Networks—a form of linear attention—with sparse Mixture-of-Experts, aiming to address the "memory wall" that typically limits small models while ensuring high throughput with reduced latency. The native context window is 262,144 tokens, extendable up to about one million through YaRN. And unlike previous generations that added vision capabilities as separate modules, Qwen 3.5 was trained from the start on multimodal tokens—text, images, and video integrated through a process called early fusion.

The model supports two operating modes: *thinking* and *non-thinking*. In the first, before producing the answer, the model explicitly generates a chain of internal reasoning, dedicating 20 to 40 seconds of processing before writing the actual answer. In the second, it responds immediately. In all the tests that follow, I used the thinking mode, as some prompts were deliberately complex. I also did the same tests by disabling thinking: the answers become immediate, the depth drops slightly on more articulate questions, but for daily use, writing assistance, routine coding, text analysis, informative questions, the combination of precision and speed is more than satisfactory. In both modes, the output traveled at about 30 tokens per second on this hardware configuration.
![grafico1.jpg](grafico1.jpg)
[Image taken from huggingface.co](https://huggingface.co/Qwen/Qwen3.5-9B)

## The Tests: Six Field Trials

The six tests that follow were designed to cover the main areas of language model evaluation: advanced scientific reasoning, multimodal understanding, complex code generation, multilingual capability with planning, handling of very long contexts, and visual-spatial reasoning. For each test, Qwen 3.5 9B's results were verified by cross-referencing the responses with frontier models like Claude and DeepSeek, not as a scientific validation, but as a practical validity check.

The grades accompanying each test are the result of a personal evaluation after online research, cross-referenced with the responses to the same prompts and the evaluations of the answers provided by Qwen 3.5 9B, submitted to Claude and DeepSeek. It is the judgment of a demanding user, not the sentence of a benchmark.

### Test 1 — Scientific Reasoning: The Higgs Mechanism

The first test was a high-level benchmark classic: explain the Higgs mechanism and electroweak symmetry breaking to a university physics student. A question that requires mathematical rigor without sacrificing clarity, and the ability to build a narrative path that guides the reader through non-trivial concepts.

The response arrived structured in five sections that progressed with the logic of a well-conducted lesson: from framing the problem of mass in gauge bosons, to introducing the Higgs field with its "Mexican hat" potential as a mental image, to explaining the mechanism by which the W and Z bosons "drink" Goldstone bosons acquiring mass while the photon remains massless thanks to residual symmetry. Each formula was accompanied by a physical interpretation; each technical step had a sentence revealing its deep physical sense. Cross-checks with frontier models, and personal online research, found the response correct, well-structured, and with the right metaphors. Not trivial for a model running on a consumer PC.

**Grade: 5/5.** The rigor was there, the clarity too. The ability to choose appropriate metaphors instead of merely reproducing notions is what was most surprising.

### Test 2 — Multimodality: Reading Visual Chaos

For the second test, I downloaded a small, low-quality image online showing a spreadsheet with a store's electronics inventory: nine columns with item codes, product names, purchase dates, categories, quantities, costs, and selling prices. The image was deliberately poor, slightly blurry, and I uploaded the file directly into LM Studio asking the model to describe what it saw.

The model read all the columns and numerical values, but the interesting part came later: it independently noticed that the "Total" column was the product of quantity times unit price, identified some monitors with zero sales interpreting them as potential unsold goods, distinguished low-cost items like mice from premium products like processors, and recognized that the purchase dates spanned from October 2017 to December 2018. It did not just transcribe: it interpreted the data like an analyst would.

Some minor numerical details were reported inaccurately, which is understandable given the image quality. But the ability to move from reading to contextual understanding is exactly what distinguishes decorative multimodality from functional multimodality.

**Grade: 4.8/5.** The reading was correct, the added business intelligence analysis was an unexpected bonus. A few points lost for some minor numerical inaccuracies.

### Test 3 — Code Generation: An NP-hard Problem

The third test was on coding, the area where benchmarks suggest Qwen 3.5 9B is slightly less brilliant than others. I asked to implement in Python an algorithm to find the longest cycle in an undirected graph, an NP-hard problem that requires not only implementation capability but theoretical awareness.

The first response stopped halfway due to a technical problem handling long output, a behavior to be reported honestly. When prompted to complete, the model produced a full solution with backtracking and pruning—the correct approach for this type of problem—with type hints, well-separated methods, and relevant comments. But the detail that struck most came even before the code: the model explicitly stated that the problem is NP-hard, that no known polynomial-time algorithm exists, and that for large graphs, an approximate approach should be considered. This awareness of theoretical limits even before writing code is a sign of something deeper than simple syntax generation.

**Grade: 5/5.** The initial hiccup should be noted, but the final solution and demonstrated theoretical maturity exceeded expectations for a 9-billion-parameter model.

---

*This episode ends here. In the second part: the multilingual planning test, the challenge with a 460-page PDF, and the visual-spatial reasoning on a room in chaos. Plus the conclusions on what it truly means to have a local assistant in 2026.*
