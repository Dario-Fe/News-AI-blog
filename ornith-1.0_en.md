---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-07-10
author: "Dario Ferrero"
---

# Ornith-1.0 35B local: the unknown beating everyone
![ornith-1.0-test-personale.jpg](ornith-1.0-test-personale.jpg)

*There is a moment, in every session with a new model downloaded locally, when you understand if you are facing a toy or a work tool. With Ornith-1.0-35B that moment arrived at the second prompt, when I uploaded a blurred photo of a company Excel sheet expecting the usual vague answer, and I found myself with a real financial statement analysis, complete with liquidity warning signals. From then on, the test session took a different turn than usual.*

Once again the disclaimer remains the same: it's not a scientific benchmark, there are no validated methodologies or laboratory-worthy cross-checks, it's simply the report of what happens when an open source model ends up on my home PC and is tested with the exact same tasks reserved for the other competitors in this series. If you haven't read the previous installments, you can already find all the technical details on the [hardware used and the LM Studio configuration](https://aitalk.it/it/qwen3.5-locale-puntata1.html). Here I will just mention the essential numbers: a Ryzen 7700, 32 GB of DDR5 RAM and a Radeon RX 9060 XT with 16 GB of VRAM, the same combination with which I've already tested Qwen 3.5, Qwen 3.6 and the Gemma 4 family. On the portal you can also find other installments of the series, with different models and equally surprising results.

## Who is Ornith-1.0

The name comes from the ancient Greek for "bird," and DeepReinforce explains it with a memorable image: like a bird building its own nest, the model learns to build the scaffolding with which it tackles programming problems, even before solving them. It's not empty marketing; it's the synthesis of a training approach that is truly different from the standard one.

The family includes four sizes, from the dense 9B up to the massive 397B, passing through a dense 31B and the 35B Mixture of Experts I chose for my tests, available with an MIT license on [GitHub](https://github.com/deepreinforce-ai/Ornith-1) and described in detail in the [official launch post](https://deep-reinforce.com/ornith_1_0.html). Here it's worth spending a couple of lines on the MoE architecture, because it's the real reason why this model manages to run with dignity even on a 16 GB video card: of the 35 billion total parameters, only about 3 billion are activated for each single generated token, a bit like if in a huge editorial office, instead of making the whole team work on every single article, only the handful of specialists truly competent on the current topic were called upon. In the case of Ornith-1.0-35B, there are 256 total experts, of which 8 are activated on a rotating basis plus one always present, and the choice is fully felt in the generation speed, which in my tests remained stable between 16 and 17 tokens per second, a more than reasonable reading pace for daily interactive use.

The other distinctive element concerns the training method. Ornith-1.0 is born from a reinforcement learning framework that doesn't just optimize the final solution to a code problem, but also the scaffold, i.e., the action plan, tool calls, and the logic with which the model decides when to retry or when to change approach. It's a subtle but important difference compared to traditional fine-tuning, a bit like teaching someone not just to solve a crossword puzzle, but also to build the grid with which to tackle it. In declared benchmarks, this choice translates into remarkable scores on Terminal-Bench 2.1, where the 35B reaches 64.2, and on SWE-bench Verified, at 75.6—results that surpass more famous models like Qwen 3.5 and Qwen 3.6 in their respective weight categories.
![grafico1.jpg](grafico1.jpg)
[image from deep-reinforce.com](https://deep-reinforce.com/ornith_1_0.html)

## An extra eye, undeclared

There is a detail that's worth telling in full, because it accurately describes how the open source ecosystem really works when it's healthy. On the official DeepReinforce page and in the original model card, there is no mention of multimodal capabilities: Ornith-1.0 is presented exclusively as a text model for agentic coding, although equipped with native support for OpenAI-style tool calls. Yet, searching among the GGUF conversions available on Hugging Face, one finds a separate file uploaded by [bartowski](https://huggingface.co/bartowski/deepreinforce-ai_Ornith-1.0-35B-GGUF/blob/main/mmproj-deepreinforce-ai_Ornith-1.0-35B-bf16.gguf), one of the community's most prolific and reliable quantizers, labeled as mmproj: it is the visual projector that, copied into the same folder as the main model, unlocks image reading in LM Studio.

I tried it out of curiosity, expecting an error or at best crippled support, and instead it worked smoothly, paving the way for the two multimodal tests of this installment. It's a small example of how, in the world of open models, real functionalities end up being broader than those declared in the official technical sheet, thanks to the hidden work of those who disassemble, convert and reassemble weights to make them run everywhere. It also serves as a reminder for those who rely only on official documentation to evaluate a model's capabilities; the risk of underestimating its real potential is real.

## The testing ground

The configuration used in LM Studio follows the one already tested in previous installments, with some adaptations due to the size of the model. I worked with Q6_K quantization, a compromise that keeps response quality very close to the original while sacrificing a little disk space, with context set to 25,042 tokens, GPU offload on 20 of the 32 total layers, a pool of 8 CPU threads, evaluation batch at 2048 and batch size at 512, with a maximum of 4 concurrent predictions and 8 active experts per token, in line with the default configuration indicated by DeepReinforce.

The eight tests cover the same ground explored in previous installments of the series, from pure scientific reasoning to conversational memory over multiple turns, passing through multimodality, code generation, multilingual planning, management of very long documents, spatial reasoning and multi-step agentic capabilities.

## Eight challenges, one verdict

### Test 1 — Scientific reasoning: the Higgs mechanism *(5/5)*

The first testing ground was one of those that put even famous models in difficulty: explain the electroweak symmetry breaking mechanism, the role of the Higgs field, and why W and Z bosons acquire mass while the photon remains massless. Ornith responded with a structure in five logical blocks, from the framing of the problem to a final mention of the physical boson, with correct formulas and precise physical interpretations, in a register that I would define as a well-written university manual, neither too technical nor watered down.

### Test 2 — Multimodality: reading a corporate spreadsheet *(5/5)*

The second test, that of the blurred Excel table told in the opening, confirmed what was guessed at first glance: correct reading of data despite the poor image quality, identification of relations between columns, a business intelligence analysis that noted the company's progressive downsizing, the strong deleveraging, the tripled net equity and above all the worsening of liquidity, with a pertinent comment also on the meaning of a negative value in consolidated liabilities.
![screenshot1.jpg](screenshot1.jpg)
*Screenshot during the test on the Excel sheet image*

### Test 3 — Code generation: an NP-hard problem *(5/5)*

On the code generation front, the task was to implement in Python an algorithm for the maximum cycle in an undirected graph, an NP-hard problem that reduces to the Hamiltonian cycle. Ornith recognized it immediately, opening with the correct theoretical note even before writing a line of code, and then providing an implementation with backtracking and intelligent pruning to avoid duplicates, documented and correct, accompanied by a complexity analysis in the worst case and a table of alternative strategies for different scenarios. The feeling here is that of talking to someone who has truly studied theoretical computer science, not just memorized recurring code patterns.

### Test 4 — Multilingual and planning: five days in Japan *(5/5)*

The fourth test moved the bar to multilingualism, asking for the planning of a five-day trip to Japan for a French client, with an itinerary in French and a final section in Italian. The French produced is fluent and natural, the itinerary balances historical temples and street food with credible logistics, cites lesser-beaten neighborhoods like Yanaka or Omoide Yokocho and suggests arriving at Fushimi Inari before 8:30 to avoid the crowd, a tip that anyone who has visited Kyoto knows how valuable it is. The final Italian section is equally solid, with practical indications on JR Pass, Suica and offline translation apps.

### Test 5 — Long context: 460 pages on the fly *(5/5)*

With the fifth test we moved to long context management, uploading the entire AI Index Report 2025, four hundred and sixty pages, and asking for information on video generation with relative page references. Ornith responded on the first attempt, precisely pointing out pages 126 and 127, citing the main models in the sector, the viral example of the spaghetti eating test and internal benchmarks cited in the report, even specifying that the next page moves the discussion to speech recognition. Surgical precision.

### Test 6 — Spatial reasoning: the room in chaos *(5/5)*

The sixth test, the visual one enabled thanks to the mmproj file found on Hugging Face, asked to describe the photo of a messy room and propose a tidying strategy. The description covered all the main elements, from the mirror to the cabinet, from the cluttered desk to the unmade bed, with a sensible intervention strategy: first the floor to clear a path, then the bed to define the space, finally the desk and basket, each step motivated in a practical way.

### Test 7 — Multi-step agent: planning a software project *(5/5)*

The seventh test measures the ability to organize work, not just execute it. I asked to plan the development of a web app for managing family expenses: tech stack, project structure, detailed roadmap for a team of two developers. Ornith proposed a coherent stack based on Next.js, Node.js, PostgreSQL, Prisma and Redis, a modular structure organized by features and a roadmap with deliverables and criticalities for each sprint, with senior developer tips like setting up the database first and validating inputs with Zod.

### Test 8 — Long conversation: consistency over four turns *(5/5)*

The last test verified consistency over a long conversation, articulated in four turns on stacks, notifications, database and scalability of the same task management application. Ornith maintained consistency throughout the conversation, remembering the choices made in previous turns and building on them: from the comparison between WebSocket and polling for a thousand simultaneous users, accompanied by code examples, up to a complete Prisma schema with relations and indexes, to close with a scalability strategy to ten thousand users that touches load balancing, Redis adapters, read replicas and caching. The only note to point out, expected as the context increases, is a progressive slight slowing down of token/s at each iteration.
![tabella1.jpg](tabella1.jpg)

The final score, eight out of eight, I hadn't seen yet in this series, and it's worth underlining: none of the models tested so far, neither Qwen 3.5 9B, nor Gemma 4 in its 12B and 26B variants, nor Qwen 3.6 35B itself, had managed to maintain the maximum on all eight fronts simultaneously.

## Lights and shadows

That said, a perfect result in a personal test conducted by a single observer, without cross-checks or statistically significant samples, should be taken for what it is: a strong indication, not an absolute truth. The benchmarks declared by DeepReinforce should be read knowing that the company obviously has an interest in showing itself in the best light compared to Qwen 3.5 and Qwen 3.6, and some independent observers in the community have already started asking for independent speed measurements on hardware different from mine, given that throughput numbers for now circulate mostly among those who have already downloaded the model.

Then there is the issue of undeclared multimodality, which on one hand is the demonstration of how vital the ecosystem around open weights is, but on the other opens an uncomfortable question about who takes responsibility when a functionality emerges from a file uploaded by a single user of the community and not by the original model developer: if something goes wrong in the interpretation of an image, who is responsible, the company that trained the model or the one who derived the visual projector. These are open questions that the current phase of local models brings with it, and that are unlikely to find a clear answer in the short term.

The winners in this scenario are undoubtedly independent developers and small studios that can afford competitive-level coding agents without paying monthly subscriptions to cloud providers, also thanks to the MIT license that does not place constraints on commercial use. Those who risk losing something in the medium term are providers of proprietary models specialized in coding, who see their competitive advantage reduced on increasingly broad market segments, while it remains to be seen how much this type of model stands up to comparison on longer and more complex tasks than those that a single afternoon test manages to stage, a question I willingly leave open for the next installment.

For now, sitting at my PC with the Radeon fan making itself heard a bit more than usual, there remains the feeling of having touched firsthand another small real quality leap in local models.
