---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-09-09
author: "Dario Ferrero"
---

# Local Ornith-1.5: A 10 Out of 10 for Self-Improvement
![ornith1-5.jpg](ornith1-5.jpg)

*There is a moment in every testing session of this series when you realize whether a model lives up to its promises or if the version leap is more marketing hype than substance. With Ornith-1.5, that moment arrived during the very first test, when the explanation of the Higgs mechanism came out clearer and faster than what the otherwise excellent Ornith-1.0 had produced months ago. From that point on, the session took on a very different pace.*

The disclaimer here remains identical to previous installments: this is not a scientific benchmark, there are no validated methodologies or cross-checks, it is simply a record of what happens when an open model lands on my home PC and is put to the test with the exact same tasks assigned to other contenders in this series, including [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html), its predecessor that closed with a perfect eight out of eight score. For the hardware setup and baseline LM Studio configuration, I refer as always to the [first installment of the series](https://aitalk.it/it/qwen3.5-locale-puntata1.html); here I will only recap the numbers that truly matter.

## Why Revisit Ornith

Ornith-1.0 had been, until today, the most convincing model to pass through my test bench. So when DeepReinforce announced the [1.5 family](https://ornith.ai/ornith_1_5.html), describing it as the transition from simple self-scaffolding to a full self-improvement cycle, curiosity was inevitable. I chose the 35B-A3B size again—the exact same size as in the previous test—specifically to have a direct comparison without the noise introduced by a change in scale, downloading the Q6 quantization which sits around 30GB and which my hardware handles without too much strain. I then added two brand new tests, designed specifically to challenge strategic reasoning and abstract logic: the two capabilities that, according to the launch page, should benefit the most from the new training cycle.

## The Test Bench

LM Studio configuration almost identical to the setup already tested for Ornith-1.0, with a few specific adjustments for this version: 25,000 token context window, GPU offload on 20 out of 41 available layers, a pool of 8 CPU threads out of 8, 8 active experts out of 256 total, evaluation batch size of 2048, physical batch of 512, and a maximum of 4 concurrent predictions. The Ryzen 7700, 32 GB of DDR5 RAM, and Radeon RX 9060 XT with 16 GB of VRAM remain the same as always—the combination with which this series has already tested Qwen 3.5, Qwen 3.6, the Gemma 4 family, and recently Qwen 3.8 and Muse Glimmer. Once again, the obligatory reminder applies: what follows is a personal evaluation, not a formal benchmark suite, and should be read as such.

## What Really Changes in 1.5

The family comprises four members: a flagship 397B mixture-of-experts model, the 35B model I tested, a dense 9B model, and a Mobile variant designed to run on iPhone and Android. The conceptual novelty lies in the training mechanism, which according to the [official documentation](https://ornith.ai/ornith_1_5.html) no longer limits itself to optimizing the scaffold with which the model tackles a given task (as was the case in Ornith-1.0), but closes the entire loop: the model proposes new tasks calibrated to its own capability frontier, builds the scaffold to address them, and generates the rollouts with which it trains itself—a loop DeepReinforce describes almost like an organism intentionally starving itself of harder problems in order to grow. On a practical level for local users, the most tangible change is different: vision is now native and no longer requires the separate mmproj file that I had to hunt down among community conversions in the previous installment.

On declared figures, the 35B-A3B shows a real leap over its predecessor: 67.8 versus 64.2 on Terminal-Bench 2.1 Terminus-2 and 79 versus 75.6 on SWE-bench Verified, outperforming in the same comparison both Qwen3.6-35B (standing at 52.5 and 73.4 respectively) and larger dense models like Gemma 4-31B and Muse Glimmer-30B. These numbers, as always when coming from the creator itself, should be taken as a starting point rather than a final verdict.
![tabella2.jpg](tabella2.jpg)
[Image from ornith.ai](https://ornith.ai/ornith_1_5.html)

## "My Name Is Claude": An Oddity Worth Reporting

On the very first prompt after downloading the model, before even starting the main test battery, I simply asked the model who it was. The response, delivered with the usual fluent confidence I had come to expect from Ornith, was that it was Claude, an assistant created by Anthropic. Not a typo, not an isolated hallucination on a marginal detail, but a full, coherent assertion—reconfirmed upon my slightly astonished second inquiry—claiming an identity that is not its own.

Technically, the most plausible explanation is not mysterious: Ornith-1.5 is built on top of Qwen3.5 and Gemma 4 with further continued training, and a substantial portion of the data used in this phase, as across much of the open industry today, is almost certainly synthetic—generated by other frontier models during distillation or dataset collection sessions. If conversations or outputs originating from Claude end up among these sources, the model does not merely absorb style and knowledge; it also absorbs the habit of answering "I am Claude" when asked who it is. It is much like an actor who, after months on set, habitually answers to their character's name even off-camera—in that grey area between performance and identity so masterfully depicted in Daniel Clowes' comic *Ice Haven*.

The main takeaway is less about the episode itself and more about what it reveals regarding an increasingly dense ecosystem of models training on each other's outputs, often without disclosing the exact origin of the data used. It is a form of mirror-chasing where tracing who said what first becomes progressively harder. The question I carry away from this episode is simple to formulate yet far from easy to answer: where does the legitimate use of high-quality data end, and where does a practice begin that, without necessarily being illegal, remains opaque to outside observers? It is not a problem I will solve in a single paragraph, but it is a signal that feels wrong to dismiss as a mere anecdotal curiosity.

## Ten Challenges, No Longer Eight

The first eight tests mirror exactly those used in previous installments of the series to ensure a direct comparison. I added a ninth and a tenth test specifically designed to put strategic reasoning and abstract logic under pressure—the capabilities that the self-improvement loop is supposed to train more than any other.

### Test 1, Scientific Reasoning: The Higgs Mechanism (5/5)

Explaining electroweak symmetry breaking, the role of the Higgs field, and why W and Z bosons acquire mass while the photon remains massless is a task that challenges even renowned models. Ornith-1.5 responded with a six-block logical structure, ranging from historical context down to counting degrees of freedom—a detail I rarely see appear spontaneously, which enriches the explanation significantly. Compared to Ornith-1.0, the prose is more pedagogical, using the classic Mexican hat metaphor at the right moment, and speed increased sharply from 16.3 to 23.15 tokens per second.

### Test 2, Multimodality: A Blurry Excel Table (5/5)

With native vision now enabled—no more downloading separate files—I uploaded the usual low-quality photo of a corporate Excel sheet. The model correctly read structure and values, identified seasonal patterns and the relationship between order count and average value, and returned a summary complete with emoji trend indicators—a touch I personally find useful rather than decorative when skimming an analysis. Compared to the previous version, the answer is more analytical and less purely descriptive, running at 21.72 tokens per second.

### Test 3, Code Generation: Maximum Cycle in a Graph (5/5)

Implementing a Python algorithm for the maximum length cycle in an undirected graph—an NP-hard problem that reduces to the Hamiltonian cycle. Ornith-1.5 immediately recognized the nature of the problem, produced a clean, commented DFS solution with backtracking, and above all proposed three concrete optimizations on its own initiative, from connectivity pruning to bitmask dynamic programming for small graphs, offering to implement them on request. A level of proactivity that Ornith-1.0 had not shown, generating at 23.86 tokens per second.

### Test 4, Multilingual Planning: Five Days in Japan (5/5)

A five-day itinerary for a French client, written in French with a final section in Italian. The generated French is natural; the itinerary mentions less-trodden spots like Omoide Yokocho and Arashiyama bamboo grove, with practical advice on transport and language barriers. The concluding Italian section is equally polished. Compared to its predecessor, the difference lies in additional cultural nuances, running at 22.03 tokens per second.

### Test 5, Long Context: 460 Pages to Consult (5/5)

With the complete AI Index Report 2025 loaded, I requested information on video generation growth and relevant page numbers. Ornith-1.5 correctly cited pages 126 and 127, referenced figures 2.3.11 and 2.3.12, listed major industry models from Movie Gen to Veo, and brought up the now-famous Will Smith spaghetti test example. Accuracy confirmed on the first attempt, with a synthesis better organized by sections compared to Ornith-1.0, at 21.36 tokens per second.
![immagine1.jpg](immagine1.jpg)
*Screenshot during long context testing*

### Test 6, Spatial Reasoning: A Cluttered Room (5/5)

A photo of a messy room with a request for a description and tidying strategy. The model explicitly categorized items into fixed furniture, architectural elements, and scattered objects, proposing a sensible sequence of action starting with the bed and floor before tackling cables. Explicit categorization is the key improvement over the previous version, running at 20.72 tokens per second.

### Test 7, Multi-step Agent: Planning a Web App (5/5)

Developing an expense management app for a two-developer team: stack, architecture, and roadmap. Modern stack based on Next.js, PostgreSQL, and Prisma; three-folder structure; six-sprint roadmap with an explicit task division between the two developers and advance warnings on critical risks for each phase. The explicit work division, absent in Ornith-1.0, better addresses the prompt's constraints, at 22.92 tokens per second.

### Test 8, Long Conversation: Four Turns on the Same App (5/5)

Four turns covering stack, notifications, database, and scalability for a task management app. Coherence maintained throughout the conversation, a hybrid architecture proposed for notifications (WebSockets for in-app and queued asynchronous emails), a database schema complete with indexes, and a scaling roadmap up to 10,000 users with a progressive checklist. Heavier use of tables and ASCII diagrams compared to its predecessor, averaging around 22 tokens per second.

### Test 9, The Strategic Planner (New, 5/5)

Stepping into the shoes of a startup CEO with $10 million in funding and an aggressive competitor eroding market share, drafting a three-year plan. Ornith-1.5 produced a six-semester plan featuring an initial diagnosis of potential market share loss causes, well-chosen guiding principles such as the notion that capital represents time rather than safety, and concrete metrics on churn, NPS, CAC, and LTV for every phase. The opening note—that ten million is not a success but fuel to achieve one—and the closing remark defining the plan as a working hypothesis rather than a prophecy add a level of awareness rarely found in such answers, running at 20.38 tokens per second.

### Test 10, The Abstract Logic Analyst (New, 5/5)

A small system of three logically contradictory statements to analyze and resolve. The model identified the contradiction using predicate logic, evaluated three possible modifications to a single statement, and selected the most elegant one, justifying the choice with clear criteria like minimal necessary logical alteration and preservation of the other two premises. Reasoning that reminded me, in its careful argumentation of every step, of certain logic puzzles scattered through the cerebral chapters of *Baccano!*, where every clue must be weighed before discarding wrong hypotheses, running at 22.72 tokens per second.

## The Overall Picture
![tabella1.jpg](tabella1.jpg)

Ten out of ten, with an average speed around 22 tokens per second compared to the 16–17 registered with Ornith-1.0—a 30–40 percent improvement that alone would justify the upgrade even at equal response quality.
![tabella3.jpg](tabella3.jpg)
*Comparative table with all models tested in 2026*

## Light and Shadows

A perfect score across ten tests, gathered by a single observer on a single hardware setup without repeated sampling or cross-validation, remains a strong indicator rather than literal truth. The same limitation applied to Ornith-1.0 and applies even more here, given that two of the ten tests are new and thus lack a benchmark baseline against other models in this series. The numbers declared by DeepReinforce, available on the [launch page](https://ornith.ai/ornith_1_5.html) along with the evaluation methodology used for every benchmark, should be read knowing that the company has every interest in presenting itself in the best light against Qwen3.6. Similarly, external analysts—such as in [this local usage guide](https://atomic.chat/blog/guides/how-to-run-ornith-1-5-35b-locally)—remind us that every lab publishes benchmarks calculated with its own setup, and cross-column differences do not always hold up under direct comparison.

Then there is the issue raised by the self-identification episode, which is unlikely to find a clear answer in the short term, but nonetheless poses an uncomfortable question to those building open models from data whose provenance is not always fully traceable: how much of the perceived quality of these systems actually relies on a silent transfer of style and knowledge from proprietary models to open ones, and who assumes responsibility when that transfer produces minor identity glitches?

The winners in this scenario are once again independent developers who can rely on a competitive coding agent without paying cloud subscriptions, and those working on mid-to-high-tier consumer hardware like mine, who can now run a model capable of standing toe-to-toe with much larger systems. Those at risk of losing ground are proprietary model providers specializing in coding, who see their advantage steadily narrowing across broader market segments, while the question remains open as to how well these results hold up on real-world tasks distributed over time, longer and messier than a single afternoon of testing can simulate.

For now, what remains is the genuine feeling of having witnessed a real leap in quality, accompanied by an ongoing question about data provenance that this series of articles will continue to explore.
