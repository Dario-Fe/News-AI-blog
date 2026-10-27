---
tags: ["Applications", "Generative AI", "Research"]
date: 2026-10-30
author: "Dario Ferrero"
---

# WebGPU: In-Browser AI Powered by Your GPU
![webgpu_ia_browser.jpg](webgpu_ia_browser.jpg)

*How a website can run a language model directly on the visitor's device—without installations and without a cloud call for every generated word. You open a page, a progress bar takes a few minutes to fill, and then a text box appears. You type, and the model responds. No software to install, no API key to paste, no distant server churning out tokens: the heavy lifting is done by the computer's graphics card sitting right in front of you, guided by a web page. On your next visit, the loading bar is barely visible because the model weights remained stored on disk in a browser space reserved for that site.*

The key technology in this scenario is called WebGPU, and it helps to state immediately what it is not. It is not a model, not a file format, and not a program to install. It is an interface that browsers offer to web pages to communicate with the graphics card—for both rendering and general-purpose parallel computing—as defined by the [W3C specification](https://www.w3.org/TR/webgpu/). Downloading weights, storing them, and translating text to numbers and back fall to other pieces of the tech stack. This article lays them all out in sequence, with currently available benchmarks and an honest look at the limitations.

## The GPU Enters the Browser

To understand why a graphics card is essential for artificial intelligence, a kitchen analogy is useful. The CPU is a highly experienced head chef, preparing one dish at a time with flawless technique. The GPU is a kitchen staffed by thousands of assistants—each capable of performing only one simple task, but all working simultaneously at the exact same instant. A language model spends its time multiplying tables of numbers, a task that breaks down into millions of independent calculations: it's the dream shift for the kitchen line, not the executive chef.

For years, however, browsers could talk to GPUs primarily to draw graphics. With WebGL, anyone wishing to use it for general computing had to disguise numbers as pixels and calculations as graphical effects. WebGPU changes this paradigm by adding compute shaders alongside graphics: small programs written in a language called WGSL that the GPU executes for arbitrary calculations, far beyond coloring triangles.
![tabella1.jpg](tabella1.jpg)

Between the web page and the silicon lies a network of conduits not unlike the one in Terry Gilliam's *Brazil*, where every request travels through offices and pipes before producing an outcome. The site speaks WebGPU, and the browser translates it into Metal on Apple, Vulkan on Linux and Android, or DirectX on Windows. Different engines handle this: [Dawn](https://dawn.googlesource.com/dawn) in Chromium-based browsers, [wgpu](https://github.com/gfx-rs/wgpu) in Firefox, and WebKit's native implementation in Safari, as described in a [recent preprint discussed later](https://arxiv.org/html/2605.20706v1).

The milestone that makes this discussion relevant today is cross-browser support. As [web.dev](https://web.dev/blog/webgpu-supported-major-browsers) notes, Chrome and Edge have supported WebGPU since version 113 on Windows, macOS, and ChromeOS, while Android requires Chrome 121 and at least Android 12. Firefox introduced support on Windows with version 141 and on ARM Macs with version 145; Safari shipped it in version 26 across all Apple platforms. [Khronos notes](https://www.khronos.org/developers/linkto/webgl-and-webgpu-sigg26) place Firefox on Windows in July 2025 and Safari in September 2025, adding that Chromium expanded Linux support to 12th-gen Intel GPUs and newer in January 2026. Firefox on Linux and Android remains in development according to web.dev, meaning developers must still provide fallbacks for unsupported environments.

## From Download to Tokens

In-browser AI follows a precise execution sequence. The page verifies that WebGPU is available and that the GPU is suitable. It then downloads the model from a server or CDN, caches it in browser storage, and loads it into VRAM. When the user types, the text is split into tokens (word fragments), computations run on the GPU via WebGPU, and the generated tokens are reconstructed into sentences. A detail that often gets overlooked: WebGPU itself downloads nothing and saves nothing—it handles purely computation. Everything else relies on standard browser network and storage APIs.

JavaScript libraries stitch these components together. [WebLLM](https://arxiv.org/abs/2412.15803), born from the MLC project, offers an API compatible with OpenAI's format, leveraging WebGPU for the GPU and WebAssembly for CPU tasks. [Transformers.js](https://huggingface.co/docs/transformers.js/index) relies on ONNX Runtime, while [wllama](https://github.com/ngxson/wllama) brings [llama.cpp](https://github.com/ggml-org/llama.cpp) models—originally built for CPU execution—into the browser with a dedicated WebGPU backend. The cited web.dev post confirms that both ONNX Runtime and Transformers.js utilize WebGPU for local inference.

Under the hood, two distinct computational phases take place, and the difference matters. In the prefill phase, the model reads the entire prompt at once, dominated by matrix-matrix multiplications. In the decode phase, it generates one token at a time, where work shifts to matrix-vector multiplications. Benchmark measurements on an Apple M3 with a 1-billion-parameter model quantized to 4 bits show that matrix multiplications account for 92.6% of prefill time and 89.9% of decode time. Furthermore, decode speed is bottlenecked primarily by memory bandwidth (reading weights from VRAM), which is why weight quantization helps—less data needs to be moved across the bus.

Herein lies the gap between access and performance. As the preprint highlights, WebGPU provides functional portability but not performance portability: the same code runs everywhere, but not at the same speed everywhere. Optimal performance demands quantized weights, hand-tuned compute shaders for each GPU architecture, and careful VRAM management. There is also a one-time startup latency for compiling GPU shaders, which authors estimate at one to five seconds.

## Where Model Weights Live

After downloading, model weights don't disappear into thin air. [Chrome's guide on caching models](https://developer.chrome.com/docs/ai/cache-models) notes their size: a 1.35 GB file, such as a compressed version of Gemma 2B, is considered tiny for a language model. To retain them on device, three browser storage options exist: Cache API, Origin Private File System (OPFS), and IndexedDB. The Chrome team generally recommends Cache API and considers IndexedDB the worst choice for large files.

This is not a file you can browse with a standard file explorer. The Origin Private File System is, per Chrome's guide, private to the origin and invisible to the user. This does not mean the file format is exotic: wllama, for instance, stores standard GGUF files from llama.cpp inside that storage space. They simply aren't visible in the OS file manager.

Closing the browser tab frees system RAM and VRAM, but the cached files remain on disk. Closing the browser changes nothing: on the next visit, the site reloads the model instantly from local storage. Eviction happens only via browser settings or automatically if space runs low and the site has not requested persistent storage permission.

Each origin receives its own isolated storage. The [webllm.io FAQ](https://webllm.io/docs/faq/)—an independent developer kit built on MLC's engine—clarifies that models are sandboxed per origin, making them inaccessible to other sites and clearable via browser settings, with initial downloads ranging between 1.5 and 4.5 GB depending on hardware capabilities. Consequently—as an inference, not a benchmark—downloading the same model across two different domains will consume double the disk space. The browser resembles Howl's Moving Castle in Miyazaki's film: a moving structure with many doors, each opening onto a different location and each requiring its own key.

## Who Pays for Computation?

This brings us to the economic equation. When inference runs on the end user's device, the provider serves the model as a static asset, leaving electricity, heat, and compute time to the visitor. While a logical deduction rather than an empirical measurement, the premise is sound: every local session is one less server instance billed to a cloud GPU provider. The preprint authors note that local execution can improve latency and energy efficiency, citing third-party studies, though it leaves an open question: does the net energy balance across millions of laptops actually improve compared to centralized data centers?

Servers don't disappear entirely, however. They host the web page, accounts, updates, and model files—and those files are heavy. Bandwidth costs for delivering multi-gigabyte models to new visitors shift expense from cloud inference to content delivery. Tellingly, webllm.io documentation outlines a hybrid architecture, falling back to cloud APIs when WebGPU is missing or local hardware is insufficient. The same documentation notes that local execution requires Cross-Origin Isolation headers (COOP and COEP) because it uses SharedArrayBuffer—a requirement site operators must configure that can impact external embedded resources.

Who wins and who loses in this shift? These are scenarios, not guarantees. Winners include lightweight service providers cutting cloud bills, users with powerful GPUs benefiting from instant responses and local data privacy, and GPU manufacturers for whom VRAM becomes a compelling selling point. Losers include users on legacy hardware bound to cloud fallbacks or sluggish performance, and cloud GPU providers relying on lightweight inference workloads.

## Limitations: What the Numbers Say

The most comprehensive empirical data currently available comes from the preprint [*Llamas on the Web*](https://arxiv.org/html/2605.20706v1), published on arXiv in May 2026 by researchers from UC Santa Cruz and Microsoft Research. Two caveats apply: it is a preprint awaiting peer review, and the authors themselves developed llama.cpp's WebGPU backend, meaning they are evaluating their own code. The dataset is substantial: sixteen devices across eight hardware vendors, ten models, and approximately twenty-five hours of automated benchmarks.

The primary finding provides a sobering reality check for those expecting miracles. Compared to native llama.cpp backends, WebGPU falls significantly behind on dedicated hardware: native CUDA and Vulkan outperform WebGPU by up to 10x in prefill and 2.5x in decode, leveraging tensor cores and vendor-specific matrix instructions. On Apple silicon, native Metal leads WebGPU by over 2x in prefill and 50% in decode. However, the story isn't one-sided: on Mac, WebGPU outperforms Vulkan translated via MoltenVK by up to 59% in prefill and 45% in decode; on an AMD GPU, native Vulkan lags behind WebGPU by 3x in prefill despite beating native HIP in decode. On Intel GPUs, WebGPU edges out SYCL by 23% in prefill—though only with browser safety checks disabled, an artificial condition in real web browsing.

Those safety checks come at a cost. WebGPU compilers inject bounds checks to prevent out-of-bounds memory access and division-by-zero errors. Disabling them in benchmarks reveals an average performance penalty of 14% for prefill on quantized models and 23% for full precision—reaching up to 42% on an RTX 5080—while decode impact ranges from 1% to 5%. That is the price of the web sandbox: a web page must never breach browser memory boundaries.

Then there is WebLLM. Its [paper](https://arxiv.org/abs/2412.15803) claims up to 80% of native performance, while the [MLC blog](https://blog.mlc.ai/2024/06/13/webllm-a-high-performance-in-browser-llm-inference-engine) cites up to 85% relative to Metal on a MacBook Pro M3 Max when both engines are compiled via the same toolchain. These do not contradict the UC Santa Cruz preprint: they evaluate against different baselines and should be compared with care.

Among in-browser runtimes, the preprint's comparisons favor the authors' backend over alternatives. Their implementation generates text 45% to 69% faster during decode across four GPUs from different vendors, while using 29% to 33% less memory. However, it trails during prefill (21% to 51% slower) because fast matrix instructions, known as subgroup matrix operations, are not yet enabled in stable browser builds. For WebLLM and Transformers.js, the authors also report VRAM consumption spikes approaching 10 GB in certain configurations, attributing them to potential memory leaks. Note that these measurements reflect specific software versions tested at the time.

Mobile devices present tighter constraints. On iPhones, a Safari tab receives less than 500 MB of usable memory, and lower-end mobile GPUs across iOS and Android could run only the four smallest test models, yielding 4 to 17 tokens per second in decode. On flagship mobile GPUs, small models exceed 3,000 tokens/sec in prefill and 100 in decode, while the largest tested model (a ~3 GB Gemma 4 variant) drops to 65 and 30 tokens/sec.

Browser choice also introduces massive variance. On an M3 Mac, the same model generates ~1 token/sec in Firefox compared to ~52 tokens/sec in Chrome; the authors excluded Firefox from main benchmarks as a result. While a single datapoint rather than a universal rule, it demonstrates that "WebGPU support" does not equal "Chrome-equivalent performance."

Finally, WGSL language limitations play a role. WGSL currently lacks native support for bf16, int8, int16, and int4 types that modern GPUs execute natively, forcing emulation. This creates a counterintuitive effect documented in the preprint: in WebGPU, weight quantization serves primarily to fit models into VRAM rather than accelerate computation; dropping from 4-bit to 2-bit quantization on mid-range hardware actually reduces decode speed by 17%.

## Privacy with Conditions

Privacy is WebGPU's most highlighted advantage—real, but conditional. It helps to separate three claims that marketing copy often blends together. First, that computation occurs locally: WebGPU enables this completely. Second, that the web application sends no prompts, responses, or telemetry externally: this depends entirely on the site operator, not the underlying API. webllm.io documentation, for example, guarantees zero data transmission in purely local mode, but the same product includes cloud fallback modes, making privacy dependent on configuration. If user input gets forwarded to external search, moderation, or logging endpoints, local privacy guarantees vanish.

Third, that the model itself remains secure from extraction: here, the answer is no. Chrome's guide warns that weights stored in Cache API or OPFS can be easily extracted using standard DevTools, and encryption doesn't help because the decryption key must inevitably be delivered to the client. Anyone needing to protect proprietary weights must keep the model on the server.

## Browser vs. Native?

Where does the advantage lie? It depends on your goals, as summarized in the table below.
![tabella2.jpg](tabella2.jpg)

The two paths are converging: llama.cpp's WebGPU backend entered the main codebase through over a hundred community contributions, bringing GGUF models directly to the browser. Web standards are advancing too: Khronos updates highlight subgroup extensions arriving in Chrome 144 and 145—distinct from the matrix instructions expected later. Chrome's built-in AI APIs (Prompt, Summarizer, Translator) offer another approach, detailed in [official documentation](https://developer.chrome.com/docs/ai/built-in): browser-provided models exposed directly to sites, rather than sites shipping their own weights. How this coexists with WebGPU remains an open question.

## Your PC as Your Server

The primary conclusion is modest: for maximum speed, massive models, and uncompromised control, WebGPU cannot replace native llama.cpp or LM Studio. Benchmark data show native backends leading prefill by up to 10x, while mobile devices handle only tiny models. The second conclusion is far more intriguing: for the first time, major browsers can communicate directly with GPUs, making a new distribution model viable—a web URL, a one-time model download, and computation executed entirely on the visitor's machine.

Challenges remain: browser/driver fragmentation, sandbox overhead, subgroup matrix availability in stable builds, and the net energy footprint of millions of client GPUs versus centralized data centers. In short: WebGPU doesn't turn the browser into an AI server—it turns the browser into a secure sandbox where your own computer becomes the server for your AI.

---

*Technical note: Performance data originate from an unreviewed preprint reflecting May 2026 software versions. Browser and runtime implementations evolve rapidly; verify figures before relying on them for production decisions.*
