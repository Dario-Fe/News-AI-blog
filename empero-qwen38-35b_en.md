---
tags: ["Generative AI", "Training", "Startups"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Empero and Distillation: I Tested Their Qwen3.8-35B-A3B
![empero-qwen38-35b.jpg](empero-qwen38-35b.jpg)

*When an independent lab promises to transfer the reasoning of a frontier model into a file you can download and run on your own PC, the right question is not whether it succeeded on paper, but how much of that promise stands when the file actually lands inside consumer RAM. This is the question that guided previous installments of this series, from [Qwen 3.5 9B](https://aitalk.it/it/qwen3.5-locale-puntata1.html) to [Qwen 3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html), and today it returns with a different protagonist: not an official model from a billion-dollar lab, but a German project called [Empero](https://empero.org/) and its distilled creation, [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill).*

## A German Lab Against the Cloud

Empero describes itself as an independent research lab based in Germany, dedicated to building language models efficient enough to run on user-owned hardware without going through a third-party API. It is not an isolated slogan: the website's section for European enterprises explains that a growing number of companies cannot send regulated data to foreign APIs, and an Apache-2.0 model executable locally—verifiable down to its weights—addresses that exact constraint. It is a market positioning before it is a technical one, and it is worth keeping in mind when reading the numbers that follow.

The ecosystem Empero has built around this philosophy is broader than the single model I am testing today. There are families of distillations from Qwen3.8, available in sizes of 2, 4, and 9 billion parameters alongside the 35B model we will use today; there is the Qwythos line with over a million downloads on Hugging Face; there is a terminal coding agent named [Abacus](https://github.com/empero-org/abacus) designed to work with local or remote endpoints; and there are internal research tools like `rethink` for generating reasoning traces, `SFTSuite` for organizing them into curricula, and `Microverse` for exploring new architectural configurations before launching full training runs. The picture is not that of an isolated fine-tuner, but of a supply chain Empero claims to control end to end.

For the hardware and software configuration of these tests—AMD Ryzen 7700 processor, 32 GB DDR5 RAM, AMD Radeon RX 9060 XT GPU with 16 GB VRAM, LM Studio runtime—I refer to the [first episode of the series](https://aitalk.it/it/qwen3.5-locale-puntata1.html), which remains the methodological benchmark for anyone arriving just now.

## What the Latest Distillate Promises (and What It Doesn't)

According to the official model card, Qwen3.8-35B-A3B-Distill stems from distilling Qwen3.8 frontier models into the Mixture-of-Experts architecture of Qwen3.6-35B-A3B, trained on curated traces from teacher models covering chain-of-thought math, code, general reasoning, instruction following, and tool usage—filtered for quality prior to training. The listed teacher models are two internal Qwen3.8 variants: one trained on 2.4 trillion tokens and another called Flash Next. Each response opens with a thinking block learned directly from the teacher's traces rather than generated autonomously by the student: this is the distinction Empero itself makes between memorizing a master's moves and improvising them on one's own—much like the protagonist of *Vagabond*, Takehiko Inoue's manga, who crafts his style by moving from school to school rather than inventing it out of thin air.

However, benchmark numbers should be read with more caution than the press release suggests. Compared to the base model Qwen3.6-35B-A3B, Empero's distillate shows practically unchanged MMLU performance (0.838 vs. 0.834)—a difference the technical documentation itself places within the statistical margin of error. Where improvement is clearer is on ARC-Challenge (rising from 0.548 to 0.582) and ARC-Easy (rising from 0.819 to 0.830). It is a real but selective gain, not generalized superiority: the open question is whether progress concentrated on these two benchmarks translates into a perceptible advantage in daily use or remains confined to that specific test suite.
![tabella1.jpg](tabella1.jpg)

It is also worth clarifying what in this package is not an invention by Empero. The Mixture-of-Experts architecture did not originate with them; distillation from larger models is now a widespread technique across the industry; and the GGUF format is a local ecosystem standard used by dozens of other projects. What Empero claims as its own is not a single ingredient, but direct control over the entire supply chain combining them—from trace generation to a post-training technique called FTPO, designed to correct unwanted behaviors like repetition loops without re-running full training. Whether this suffices to justify the "special" label remains a question every reader can assess for themselves.

## The Model on the Bench: Architecture and Weights

The tested file is named [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill), built on top of the base model Qwen3.6-35B-A3B and released under the Apache-2.0 license. The architecture is hybrid: forty total layers, organized into ten cycles consisting of three Gated DeltaNet layers (a form of linear attention) followed by one full-attention layer, totaling ten full-attention layers out of forty. Expert routing involves 256 routed experts plus one shared expert, with eight active experts per generated token. It follows the same partial orchestration logic described in the Qwen 3.6 review, but applied here by Empero starting from those weights to apply off-policy SFT on teacher Qwen3.8 traces—not training from scratch, but a model carrying distilled knowledge from much larger teacher traces.

The point worth reiterating, as it is easy to misunderstand, is that the roughly 3 billion active parameters per token concern computation, not memory. The entire file, with its 35 billion total parameters, must still be loaded into RAM or VRAM before inference can begin. Available quantizations on the [GGUF repository](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) range from 12.5 GB for IQ2_M up to 71 GB for full BF16.
![tabella2.jpg](tabella2.jpg)

For this test, I chose Q5_K_M (25.348 GB on disk), which the spec sheet indicates as usable with roughly 32 GB VRAM or 48 GB RAM for comfortable execution. On my hardware—16 GB VRAM and 32 GB DDR5 RAM—this necessarily means a compromise between GPU and system RAM, precisely the kind of delicate balance previously explored with Qwen 3.6.

## Installing and Running It Locally

The required runtime must be up to date: a recent build of `llama.cpp` supporting the Qwen3.6 architecture and Gated DeltaNet MoE layers—a condition the [GGUF repository](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) explicitly highlights, because older builds simply fail to load the model. LM Studio, Ollama, Jan, and KoboldCpp are listed as compatible. For anyone who hasn't installed anything yet, the process remains the one described in the [first installment of the series](https://aitalk.it/it/qwen3.5-locale-puntata1.html): download the installer from lmstudio.ai, no dependencies to configure manually, and automatic detection of available hardware acceleration.

Recommended inference parameters from the spec sheet are temperature 0.6, top-p 0.95, and top-k 20, with the thinking block embedded in the chat template (to be hidden in end-user applications if desired). In my configuration, I worked with an 80,640-token context—well below the 262,144 native limit, but sufficient for most planned tests—GPU offloading of 22 layers out of 41, 8 CPU threads out of 8 available, evaluation batch size of 2048, physical batch size of 512, and a maximum of 4 concurrent predictions. This setup is designed for realistic use on upper-midrange hardware, not for squeezing out every last token per second.

## Ten Tests, an Average Score

The test battery mirrors previous installments, with two additional tests added to stress the agentic and conversational performance of the model.

On the Higgs mechanism and electroweak symmetry breaking, the model produced an explanation across four logical sections, featuring correct formulas and specific focus on why the photon remains massless: score 5/5, at 26.13 tokens per second.

In the multimodality test—a low-quality image of an Excel dashboard—the model correctly read structure and values, identified seasonal patterns and the difference between 2017 and 2018, and offered concrete recommendations on June's decline: score 5/5, at 24.4 tokens per second.

On code generation—an NP-hard problem of finding the maximum cycle in a graph—it proposed three complementary approaches: an exact one with backtracking, an approximate one on a spanning tree, and a bounded trade-off version, with clean, commented code: score 5/5, at 26.64 tokens per second (the single highest speed across all tests).

On multilingual planning—a five-day Japan itinerary in French and Italian—the French was fluent, but a couple of logistical inaccuracies appeared (Shinjuku Gyoen mistaken for a street food market, JR East instead of JR Central for the Shinkansen): score 4.5/5, at 23.38 tokens per second.

On long context—a 460-page PDF on video generation growth—the model accurately pointed to pages 126 and 127, citing specific figures and key industry models on the first attempt: score 5/5, at 22.8 tokens per second.

On spatial reasoning—a photograph of a messy room—the response was correct but superficial, lacking color details and featuring an unclear rationale for the cleanup strategy: score 3.8/5, at 21.24 tokens per second (the only real weakness in the battery).

On the multi-step agent test—planning a web app—it produced a complete tech stack, a Prisma database schema, a six-sprint roadmap, and a dedicated risks/mitigations section with a probability-impact table: score 5/5, at 23.38 tokens per second.

On the four-turn long conversation, it maintained full consistency across all previous technical choices, proposing an architecture with Socket.IO and Redis and a scalability strategy up to ten thousand users: score 5/5, averaging around 22.8 tokens per second.

On the three-year strategic planner test, it produced a six-semester plan complete with goals, measurable KPIs, and a $10 million budget allocation: score 5/5, at 22.71 tokens per second.

On the abstract data analyst test—a logic problem with three contradictory premises to formalize—it identified the contradiction and justified the choice of which premise to fix with three solid arguments: score 5/5, at 23.63 tokens per second.
![tabella3.jpg](tabella3.jpg)

The overall average was 4.83 out of 5, with an average speed around 23.7 tokens per second—the highest recorded so far in the series. Compared to a dense model from the same family (Qwen3.8-27B tested in a prior installment), the speed difference is dramatic—roughly four to five times faster at equivalent perceived response quality. It is precisely the speed gap that MoE architectures promise on paper and that seems to translate into practice here.
![tabella4.jpg](tabella4.jpg)

## How Well the Promise Holds in Q5

Returning to the opening question: how much of the capability transferred from the Qwen3.8 teacher remains available when the model is compressed to Q5_K_M and run with 22 layers on GPU and the rest on system RAM? The ten tests suggest that most of it holds up, with a clear exception on fine visuospatial reasoning and a subtle flaw in geographic precision in multilingual contexts. Whether this suffices to deem the model superior to its base model remains debatable according to official benchmarks: the gain is concentrated on ARC, not generalized, while MMLU remains virtually identical.

There is also a broader question concerning the user. A 25 GB file requiring 16 GB of VRAM while saturating much of the system RAM is within reach of an interested individual, but is it realistic as a standard for those who haven't already invested in dedicated hardware? And in choosing between a cloud API and a local model like this, how much weight does data sovereignty carry—an argument Empero places at the center of its commercial offering to European businesses? These questions warrant different answers depending on who is asking, and perhaps that is the most interesting aspect of Empero's experiment: not whether the model beats its predecessor, but whether the full supply chain it promises—from distillation to GGUF packaging and Abacus as a daily tool—succeeds in making local execution a practical choice rather than an exercise for enthusiasts with a beefy GPU at home.

*Technical note: all data regarding architecture, quantizations, and benchmarks cited in this article come from official model cards on Hugging Face and Empero's website linked in the text. Scores and generation speeds across the ten tests are personal measurements, not automated benchmark certifications, and should be read as such.*
