---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-09-11
author: "Dario Ferrero"
---

# Guide to Inference Engines and Clients for Local LLMs
![guida-motori-inferenza-locale.jpg](guida-motori-inferenza-locale.jpg)

*There is a precise moment when a technology stops being a promise and becomes a tool. It is not when the press release comes out, nor when benchmarks go viral on social media, but when a regular person with a regular PC sits down, downloads something, and decides to truly understand what is going on. In 2026, that moment arrived forcefully for local inference, and with it came a problem that almost no one clearly explained before people found themselves confused in front of the command prompt: it is no longer the model that is missing, but clarity on *how* to run it.*

The reason for all this is simple yet understated. As highlighted in the [DigitalOcean Currents report](https://www.digitalocean.com/currents/february-2026), 64% of companies today integrate models via third-party provider APIs, while only 15% focus primarily on training models from scratch: in short, most of the work is now integration rather than construction. The cloud is not dead; it remains dominant. But what once seemed like an insurmountable asymmetry between huge proprietary models and "second-rate" local models is shrinking at a speed that surprises even the keenest observers. Qwen3.5-9B, with roughly thirteen times fewer parameters than some cloud giants, scores 81.7 on the GPQA Diamond benchmark—the benchmark test for advanced university-level reasoning—compared to 80.1 for OpenAI's GPT-OSS-120B, as reported on the [official model page on Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B). The gap is minimal, not a vast abyss, but the point stands: a vastly smaller model holds its own against a much larger one, representing a paradigm shift in what "small" means in 2026.

Yet with the democratization of hardware came a new labyrinth: if you download an open-weight model and put it on your PC, what do you use to run it? The answer depends on a distinction that almost no one explains beforehand and that organizes virtually the entire ecosystem: the difference between the inference **engine** and the **client** that wraps that engine.

Before proceeding, it is necessary to be clear about what this article is and what it is not. What follows is an analysis of features and technical specifications built on official documentation, repositories, changelogs, and cross-verification among authoritative sources. It is not a scientific benchmark, there is no peer-reviewed testing protocol, and there is no statistically significant sample. I have tested only two products in this overview on real hardware, and I cite them as illustrations, not as a structural framework. Those looking for certified numbers will find benchmarks on each product's official pages. Those wanting to understand what these tools promise to do, and with what hardware, read on.

The truth, as often happens in this field, does not lie in a table. It lies in understanding what each tool actually does, and what it asks you to surrender in return.

## The Engine and the Car

To run a language model locally, you need two things: the model itself—a file of several gigabytes—and something that acts as an interpreter between your hardware and the model, managing memory, tokenization, and inference. Without this intermediate layer, downloading model weights is like having a movie file without a video player. And this is where the division splitting almost the entire ecosystem opens up.

On one side are the **inference engines**, also called runtimes. These are low-level libraries and servers, often headless, that directly manage model loading, request scheduling, CPU and GPU utilization, quantizations, and various weight formats. They almost never feature a graphical user interface, communicate via APIs, and their success is measured in throughput and latency. Their target audience is developers, MLOps engineers, and anyone serving a model to dozens of users. They are the bare engine of a car—what you see when someone pops the hood to show you what is inside.

On the other side are the **clients**, runners, or end-user products. Ready-to-use applications that take one or more engines and wrap them in something usable: a model browser, a chat interface, a pre-configured API server, sometimes web search plugins, RAG on your documents, or even agents. They don't ask you to configure anything, but in exchange, you don't always know what is happening under the hood. The car metaphor is precise here: the client gives you air conditioning, navigation, and parking sensors. You give up manually adjusting the brake bias, but you still arrive at your destination.

The underlying question running through this article is not "how much control am I giving up," but "with what hardware can I run what is promised." This shifts the focus from software to hardware, which is where the real difference between the two worlds resides. An engine optimized for data center H100s and a client designed to run on a home MacBook speak different languages; knowing which tool fits which need is half the battle.

My real-world experience touches only two points on this map, and I cite them as illustrations rather than a backbone: LM Studio and Unsloth Studio on a Radeon RX 9060 XT with 16 GB of VRAM—the same configuration many advanced users, gamers, content creators, or work-from-home developers would recognize as their own. Upper-mid-range consumer hardware, but far from the A100s envisioned when discussing local inference. The rest comes from careful reading of documentation, not field testing.
![schema1.jpg](schema1.jpg)

## The Engines

### llama.cpp

[llama.cpp](https://github.ggml-org/llama.cpp) is the reason almost everything runs. This C/C++ library is the silent engine behind most client applications known to the general public: Ollama, LM Studio, Jan, GPT4All, and KoboldCPP all rely, to varying degrees, on its core. Its strength lies in extreme portability: it runs on CPUs, NVIDIA GPUs via CUDA, AMD via HIP, Intel cards via Vulkan and SYCL, and Apple Silicon's Metal—all within the same package. It is no coincidence that the GGUF format—quantized, self-contained, architecture-agnostic weights—has become the de facto standard for local models: llama.cpp is its reference implementation.

The flip side of its ubiquity is its developer-centric setup: fine-grained control with little focus on multi-user serving. If you want to run a model on your laptop to experiment with GGUF quantizations, it is probably the absolute best choice. If you need to serve that model to an entire team via stable APIs, it is the engine, but not the complete product.

### vLLM

If llama.cpp is the DIY engine, [vLLM](https://vllm.ai/) is the production race engine. Created by researchers at UC Berkeley, it has become the de facto standard for high-throughput serving, and its breakthrough is called PagedAttention: instead of treating KV cache memory as a single wasted block, it treats it like an operating system's paged virtual memory, complete with copy-on-write and prefix sharing across similar requests. In the project's original paper, previous systems utilized only 20–40% of available KV cache memory; with PagedAttention, utilization rises to roughly 96%, enabling 2–4x higher throughput compared to naive batching at equivalent latency.

However, vLLM thrives on NVIDIA GPU territory. CUDA is its native home, and while AMD support via HIP is growing, it remains a data-center-oriented tool less suited for laptops and CPUs. Setup is more complex, and its philosophy is clear: team and enterprise serving, backend APIs for applications, and concurrent workloads. If your goal is to have dozens of users talk to the same model, vLLM is likely the first thing you should study.

### SGLang

[SGLang](https://github.com/sgl-project/sglang) does something different and more specialized: it is optimized for models that do not merely answer, but think in graphs—multi-step agents, tool use, advanced RAG, and "deep research" workflows where the model calls external tools and chains generations together. Its strength lies in co-designing the programming frontend alongside the runtime to handle non-trivial decoding patterns efficiently.

It is less of a general commodity than vLLM or llama.cpp, and its documentation still carries an early-adopter feel. But if your objective is local multi-step agents or prototyping agentic workflows, SGLang is one of the most promising tools in 2026, offering swift support for cutting-edge models like gpt-oss.

### TGI

[Text Generation Inference](https://huggingface.co/docs/text-generation-inference) by Hugging Face is a veteran in transition. For years, it was the reference inference server for hosting Hugging Face models in production, offering optimized Rust and Python kernels, maturity, solid documentation, and direct integration with the HF Hub. However, on December 11, 2025, Hugging Face placed TGI into maintenance mode: no new models, features, or performance optimizations, with Hugging Face explicitly directing users planning new deployments toward vLLM and SGLang. The repository now accepts only bug fixes and documentation improvements.

It is not dead and continues to function, but for a new project, it is a choice to make with full awareness: you can still use it, but it is no longer the future Hugging Face is building. It is the classic case where yesterday's best tool becomes legacy software to maintain—much like COBOL mainframes that no one wants to modify, yet no one can shut down.

### TensorRT-LLM

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) is NVIDIA's stack for optimized inference on its modern GPUs, from the H100 and L40S to the A100 and newer series. Its strength is peak performance on NVIDIA hardware, with direct integration into Triton Inference Server to scale from a single GPU to full clusters via Kubernetes. It is the tool for those who already own the infrastructure and want to extract every ounce of performance.

The tradeoff is lock-in: TensorRT-LLM lives and dies with NVIDIA, carries a steep learning curve, and is irrelevant for the average consumer. If you work in a data center with NVIDIA GPUs and your workload is latency- and throughput-critical, it is top tier. Otherwise, it belongs to a world far removed from your desktop.

### MLX

[MLX](https://mlx.ai/) is Apple's framework for machine learning on Apple Silicon, and its strength lies in unified memory usage. On a Mac equipped with an M1, M2, M3, or later chip, CPU and GPU share the same RAM pool, and MLX leverages this to perform zero-copy inference that no llama.cpp port can match in efficiency. It is the reason a MacBook can run models that equivalent PCs struggle to execute.

Its limitation is obvious: MLX lives and dies with macOS and Apple Silicon, offering less cross-platform utility. But if you own a MacBook or Mac mini, it is likely the most natural engine for local inference, with an increasing number of runners and apps relying on it as a native Apple ecosystem backend.

## The Cars

### Ollama

[Ollama](https://ollama.com/) is the tool for those seeking simplicity. It installs with a single command, exposes an OpenAI-compatible REST API on `localhost:11434` by default, and integrates seamlessly into scripts, pipelines, and applications. It is open source, boasts a large community, and its minimalist philosophy—one command to download, one to run—makes it the preferred backend for dozens of third-party applications. In terms of raw performance, it is generally faster, handles concurrent requests better, and consumes fewer resources due to the absence of graphical overhead.

The flip side is the required terminal familiarity, advanced configuration that routes through Modelfiles, and a native GUI that arrived late and remains minimal. There is also a transparency factor worth noting: being open source, Ollama's code can be inspected by anyone—something that is not always true for competitors with proprietary GUIs. For local LLM app development, command-line personal use, API integrations, or rapid prototyping, Ollama remains a cornerstone.

### LM Studio

[LM Studio](https://lmstudio.ai/) operates on a different field. It is a desktop application featuring a refined graphical interface available for Windows, macOS, and Linux. Its strength lies in eliminating the friction that deters most people from local AI. It allows users to search, download, and load models without touching a terminal, exposes an OpenAI-compatible API, and automatically handles GPU acceleration across NVIDIA, Apple Silicon, and AMD.

However, the detail that truly transforms the experience for users without a development background is this: upon selecting a model, LM Studio displays a real-time performance estimate tailored to your specific hardware configuration, complete with color-coded indicators—green, yellow, red—that immediately communicate whether the model will run smoothly, with constraints, or if your hardware is insufficient. For a hobbyist experimenting at home, this eliminated friction is well worth any potential performance gap compared to Ollama.

This is not theoretical; I have seen it work. On my setup with a 16 GB Radeon RX 9060 XT, it was LM Studio's green indicator that confirmed Qwen 3.5 9B in Q8_0 would run entirely on the GPU without spilling layers into system RAM. I picked the model in advance without manual calculations or reading technical docs—meaning I didn't discover I had picked the wrong model after downloading ten gigabytes.

LM Studio is closed source—a free binary, but not transparent—and certain web-related features are not enabled by default. Nevertheless, for local chat with a GUI, experimenting with GGUF models, and local API serving, it is likely the best starting point for those who prefer not to worry about what happens under the hood.

### Jan

[Jan](https://jan.ai/) is the open-source alternative focusing on privacy and self-hosting without sacrificing usability. It features a clean desktop GUI, supports multiple backends including llama.cpp, exposes a local API on a dedicated port, and presents itself as a genuinely open alternative to ChatGPT. Its strength is balance: open source in a way LM Studio is not, with a user experience that Ollama lacks.

Its limitation is a less curated model ecosystem and a smaller user base, translating to less community support and documentation. For those wanting open source and a GUI without excessive complications, Jan deserves a spot on your radar.

### Unsloth Studio

[Unsloth Studio](https://unsloth.ai/) is the product that comes closest to what a local "agentic" assistant should be. *A useful clarification: currently there are two entry points to the same ecosystem—Unsloth Studio, the browser-based interface labeled as beta at the time of writing, and Unsloth Desktop, the newer native app for Windows, macOS, and Linux. The core features are identical; only the container differs.* It is not just a runner: it is an environment integrating native web search, deep research, RAG on local documents, code execution, personal knowledge bases, and guided QLoRA fine-tuning without opening a terminal. The underlying engine is llama.cpp for GGUFs, coupled with training components that make it a hybrid tool between inference and training.

Its target audience is precise: creators, researchers, and writers who want the model to fetch sources, read pages, and generate cited drafts. Integrated web search and deep research—which drafts a plan, finds credible references, and generates a cited report—set it apart from most competitors. The tradeoff is that it remains in rapid evolution, less mature as a "pure" runner compared to Ollama or LM Studio, and certain features may exhibit instability consistent with its beta label. But if your goal is writing backed by sources, it is arguably the most promising tool in the group.

Here, too, direct experience carries weight. Testing Unsloth Studio on my RX 9060 XT, having the model search web pages while I worked and using deep research to compile cited reports demonstrated what it means to have an agentic environment ready out of the box without assembling six different components. It is not merely a runner; it is a workshop.

### LocalAI

[LocalAI](https://localai.io/) performs an elegant task: it acts as a uniform abstraction layer over multiple backends. If you have llama.cpp, vLLM, and MLX, and want a consistent OpenAI-compatible API that speaks to all of them without remembering which command launches which engine, LocalAI is the solution. It supports multiple models simultaneously, following a philosophy of "one installation, many engines," without requiring a massive initial download because each backend activates only when a model requests it.

Its limitation is that it is more infrastructure-focused than desktop-friendly: it is not a tool for casual chatting, but for building a unified backend in heterogeneous environments. For self-hosted servers and applications utilizing multiple engines, it is a solid choice.

### Open WebUI

[Open WebUI](https://openwebui.com/) is what many people seek without realizing it: a "self-hosted ChatGPT" for their team. It connects to Ollama, vLLM, or other engines via API, adding everything missing from a shared platform: multi-user chat, integrated RAG, web search via SearXNG or providers like Brave, user management, workspaces, and agents. The interface is modern and highly flexible.

The cost is deployment: it requires Docker and basic server configuration, meaning it is not "click and run." But if you want a shared team platform with RAG and web search, Open WebUI is arguably the best outcome of 2026 on this front.

### GPT4All

[GPT4All](https://gpt4all.io/) was for years the first point of contact for many with the concept of a local LLM on their own computer: a simple interface, zero configuration, and one-click model downloads. However, to be clear, active development has stalled: no commits to the repository since May 2025, and no new releases since February 2025. The app still functions and opens without issues, but it no longer receives updates, new models, or security fixes. It should be viewed as a historical milestone rather than a recommended choice for 2026: those seeking equivalent simplicity today will find more active alternatives in Jan or Ollama.

### KoboldCPP

[KoboldCPP](https://koboldcpp.com/) originates from the KoboldAI ecosystem and caters to a specific audience: writers of long-form fiction, roleplay, or assisted storytelling. Built on top of a llama.cpp engine, it constructs a suite of generation options, presets, and editing tools tailored for creative prose—features like narrative memory management or World Info that other clients do not offer. It is a single, lightweight executable designed for users coming from text-based gaming rather than software development.

Its limitation lies in its specialization: outside creative writing, KoboldCPP is less convenient than LM Studio or Ollama for general use, and its interface—while functional—feels like a tool built by enthusiasts for enthusiasts rather than a polished product.

### Text Generation WebUI

[Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) is the Swiss Army knife of local experimentation. A locally installable web interface offering multi-backend support and an extension system that allows adding virtually anything—from RAG and TTS to advanced sampling configurations that other clients deliberately hide for simplicity. It is the tool for those who want full control over every parameter.

The tradeoff is the learning curve: the interface displays everything, which also means showing too much for someone who just wants to chat. It is not designed for casual users, but for those treating local inference as a permanent laboratory.
![tabella1.jpg](tabella1.jpg)

## What to Choose, Based on What You Actually Want

The right choice depends on what you are trying to accomplish, and no universal ranking can replace your specific context. However, certain scenarios almost always lead to the same answers.

You just want to chat locally on your PC without configuring anything. Here, LM Studio wins for UX, or Jan if you prefer something fully open source, with Ollama as an alternative if you are comfortable with a CLI. If you tested LM Studio on your setup and saw the green indicator light up, there is no need to reinvent the wheel.

You need to serve a model to multiple enterprise users with a stable API. This is the domain of engines: vLLM for throughput and continuous batching, TGI if you are starting from an existing Hugging Face ecosystem (keeping in mind its maintenance status), or SGLang if your users build agents or complex RAG. Open WebUI can serve as the human-facing frontend above all of these.

You want to write technical articles and have the model find sources, read pages, and generate cited drafts. Unsloth Studio is the most direct answer, with native web search and deep research. Alternatively, Open WebUI or Text Generation WebUI can work, albeit requiring a longer setup.

You have an NVIDIA GPU and want maximum production performance. TensorRT-LLM or vLLM, depending on whether you already have an NVIDIA-native infrastructure or prefer an open stack.

You want a uniform API across multiple backends. LocalAI does exactly this and is the natural choice for heterogeneous environments.

You are primarily interested in creative writing or storytelling. KoboldCPP is built specifically for that, packed with generation options tailored for long-form narrative.

You want to experiment with RAG, plugins, and advanced configurations without limits. Text Generation WebUI and Open WebUI give you maximum flexibility at the expense of a steeper learning curve and a less streamlined UX.

In truth, developers often use LM Studio for exploration, llama.cpp when building, or Ollama for prototyping and vLLM when moving to production. A tool does not have a fixed identity; it has a job to do.

## Where Things Are Heading

Three signals, in particular, reveal a great deal about where this space is going. The first is format convergence: GGUF has become the de facto standard for local models, and the fact that nearly all clients support it means a model downloaded today will run tomorrow on different hardware without friction. It is the same logic that made USB-C the universal connector, though unlike physical hardware, no software format is entirely immune to future disruption.

The second is the growth of local "agentic" environments. Unsloth Studio, SGLang, Open WebUI, and others are shifting the center of gravity from "running a model" to "making the model do work," integrating web search, tool use, RAG, and agents that interact with your documents. It is the difference between an engine that responds and an assistant that acts—the same distance separating a jukebox from an improvising musician.

The third is the tighter integration between local inference, web search, tool use, and RAG over personal documents. These are no longer separate domains: they are layers accumulating around the model, with the client acting as the unifying glue. The trend points toward orchestrating multi-step local agents—similar to cloud "operators," but running locally on your machine, where data never leaves.

Many open questions remain. How sustainable is today's hardware over time against models growing faster than efficiency gains can keep up? Who is accountable for the quality of what an agent extracts and infers when the bottleneck is no longer the model, but the ingestion pipeline? And the most subtle: if we trust a client whose inner workings we cannot inspect, are we gaining real control, or merely the illusion of maintaining it?

The answer, as always, lies in usage—and in knowing what is under the hood when it matters.
