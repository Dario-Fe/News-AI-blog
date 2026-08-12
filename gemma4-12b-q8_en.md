---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-06-15
author: "Dario Ferrero"
---

# Gemma 4 12B local: better small at its max or big and throttled?
![gemma4-12b-q8.jpg](gemma4-12b-q8.jpg)

*In previous tests on Gemma 4 26B and Qwen3.6 35B, I always had to deal with the same problem: VRAM was never enough. Large models, aggressive quantizations, offload layers. They worked, but with the feeling of driving a powerful car with the handbrake on. Then came Gemma 4 12B. Smaller, sure. But with a new architecture and the promise of running entirely on consumer GPUs without compromises. So I decided to do a different experiment: no longer "which is the most powerful model?", but "can a smaller model used at its full potential beat a larger but throttled one?". I took the exact same tests, the same questions, and compared them.*

Those who follow this series already know the hardware and the method. For all the details on installation, choice of framework, and laboratory philosophy, I refer to the [first article of the series on Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), which remains the methodological reference for all these experiments. Here I limit myself to the essentials.

The machine is always the same: a PC assembled with criteria but without exaggeration, with an AMD Ryzen 7700 processor, 32 GB of DDR5 RAM, and an AMD Radeon RX 9060 XT GPU with 16 GB of VRAM. Advanced user hardware, not a research laboratory. The software is [LM Studio](https://lmstudio.ai/), the desktop application that allows you to download and run models without opening a terminal, with the valuable feature of showing in advance an estimate of the expected performance on your configuration.

The method, I reiterate as I did in previous episodes, is not scientific in the academic sense of the term. There is no peer-reviewed protocol, no statistically significant sample of prompts. The tests are field trials, conducted with the tools of a demanding user, and the scores are personal evaluations, not sentences. The battery of tests has remained identical to that used for [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html), and [Qwen3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html): scientific reasoning, multimodality on tables, complex code generation, multilingual planning, long context on a 460-page PDF, spatial reasoning on a messy room, and the extra tests on multi-step agent and long conversation.

## Not a younger brother

Before getting into the tests, it's worth stopping for a moment on a point that risks going unnoticed: Gemma 4 12B is not simply a reduced version of the [26B MoE that I had already tested](https://aitalk.it/it/gemma4-26b.html). It's not a cheaper cut of the same project. It is something structurally different, and the difference is not one of degree but of type.

The 26B MoE, like all traditional multimodal models, uses separate encoders to handle images and text: one part of the model receives the images, compresses them, transforms them into a numerical representation, and only then passes the result to the actual language model. It's a two-phase process, with a "translator" in the middle that inevitably loses something along the way, like any translation.

The 12B eliminates this step entirely. It is the first "unified" model of the Gemma family, and that word in the name is not marketing: it's architecture. An image patch undergoes only a matrix multiplication and the addition of spatial coordinates, and ends up directly in the same space where text tokens live. Images and words are processed by the same attention, sharing the same internal representation. There is no translator: there are two languages that become one.

This design choice has direct consequences on memory, speed, and the quality of multimodal responses. And that is precisely why testing it with the same battery of trials as the previous models is interesting: you are not just measuring size, you are also measuring a different idea of how data should flow through a model.

## The configuration: finally without compromise

And here we are at the heart of the experiment. For the first time in this series of tests, I was able to configure the model without having to choose what to sacrifice. LM Studio showed a solid green, not the orange of the limit as with the 26B MoE, not the red of the discouraged configuration.
![tabella1.jpg](tabella1.jpg)

The detail that changes everything is the GPU offload: 48 layers out of 48. The model runs entirely in VRAM, without having to distribute parts of itself on the system RAM. With the 26B MoE in Q4_K_M I was forced to a partial offload, and that choice weighed on speed and latency. Here, for the first time, the machine works without that brake.

The result is felt immediately: the average speed settled around 17 tokens per second, compared to 10-12 for Qwen 36 35B, and just under 20 for Gemma 4 26B which with 8B active (the "active experts" weighed heavily on performance, 8 was the sweet spot).

There is an interesting paradox that emerged from the tests. Gemma 4 26B MoE turned out to be faster than the 12B, despite having double the total parameters. The secret lies in the architecture. The 26B is an MoE model: out of 25 billion total parameters, it activates only about 4 (8 in my test) for each token. It's like having a huge library but, for every question, you only browse a small number of books. The 12B, being a dense model, instead activates all its 12 billion parameters for each token, doing more calculations and therefore being slightly slower on average.

However, the 25 billion parameters of the MoE must still reside in VRAM, occupying more than double the memory of the 12B. And the routing overhead to manage experts becomes evident on long contexts, where the 26B loses part of its advantage while the 12B maintains more stable performance. In short: the 26B is faster but more demanding on VRAM and less stable on long sequences; the 12B is lighter, predictable, and for most daily uses more than sufficient. The choice depends on what you are looking for.

## The tests

### Test 1 — Scientific reasoning: the Higgs mechanism *(Score: 5/5)*

*Speed: 17.45 tokens/second*

What I have always used as a thermometer of the model's intelligence: explaining the Higgs mechanism and electroweak symmetry breaking to a university physics student. A question that requires rigor without sacrificing clarity, and the ability to build a path that guides the reader through non-trivial concepts.

The response arrived structured in five sections with the logic of a well-conducted lesson, starting from the central problem—that is, why explicit mass terms cannot be written without violating gauge invariance—to the complete solution, with the gauge group SU(2)_L × U(1)_Y, the condition μ² < 0 that makes the potential minimum no longer at zero, and the explanation of why the photon remains massless thanks to the residual U(1)_em symmetry. The scientific precision was impeccable: correct formulas, vacuum expectation value, the suggestive image of Goldstone bosons being "eaten" by longitudinal polarization, and a final "exam summary" in five points that summarizes the entire mechanism without trivializing it.

What is striking, however, is not just the quality of the response: it's the speed with which it arrived. With Qwen3.6 35B I was at about 11 tokens per second. With Gemma 4 26B MoE at about 10. With this model at 17.45. The difference is not negligible in daily practice.

**Score: 5/5.** A series opener hard to improve upon.

### Test 2 — Multimodality: reading a corporate spreadsheet *(Score: 5/5)*

*Speed: 17.64 tokens/second*

The second test challenged the multimodal part with a deliberately non-ideal image: a screenshot of an Excel sheet titled "PERSONNEL COSTS", a five-year financial projection from 2023 to 2027, with columns for cost items, units, unit costs, and totals.

The model did what is expected from an analyst, not an OCR. It correctly identified the structure of the document, the five categories—Overall Values, Specialized Workers, Employees, Managers, Collaborators—read the numerical values with precision, noted that unit costs remain fixed for the entire period while units increase, and drew the correct conclusion: it's not inflation, it's team expansion. It identified 2026 as "the year of great expansion," with the clear jump in overall costs, and even observed that social security contributions calculated constantly at 33% indicate standardized tax planning. A detail that a CFO would notice, and that the model extracted autonomously from a table.

This is the difference that the unified architecture should bring: not just reading data, but understanding the context in which it exists. If test 1 confirmed expectations, test 2 began to answer the question I had in my head from the start.

**Score: 5/5.** Reading and analysis, not just transcription.

### Test 3 — Code generation: an NP-hard problem *(Score: 4.95/5)*

*Speed: 17.99 tokens/second*

The classic coding test of the series: implement in Python an algorithm to find the longest cycle in an undirected graph, with the request to explain the time complexity. An NP-hard problem that requires not only implementation skills but theoretical awareness.

The answer was technically excellent, probably the best obtained on this test in the entire series. The model opened by explicitly stating that the problem is NP-hard and that there is no known polynomial-time algorithm, a theoretical maturity that not all programming assistants show. The implementation in backtracking with DFS was clean and correct, with a "symmetry breaking" technique that imposes `neighbor > start_node` to avoid exploring the same cycle multiple times, a non-trivial optimization that reduces the search space. Clear and honest explanation of complexity: factorial in the worst case, linear in space.

There is, however, a single, small flaw: the response arrived in English, even though the prompt was in Italian. In tests 1 and 2 the model had correctly responded in Italian, so it's not a structural problem. It's an oversight. The code is perfectly functional, the explanation is clear, but the lack of adherence to the prompt language is a signal worth noting. Nothing that compromises the technical result, but something you wouldn't want to see in a daily assistant.

**Score: 4.95/5.** The best solution of the series on this test, with a linguistic blemish that does not affect the substance.

### Test 4 — Multilingual and planning: five days in Japan *(Score: 5/5)*

*Speed: 17.41 tokens/second*

The multilingual test: acting as a travel agent, planning a five-day itinerary in Japan for a French client, with a focus on historical temples and street food, and a final section in Italian with advice for an Italian tourist. The test that in the 26B MoE had produced "suggeramenti" and a word with a Cyrillic ending.

The French was impeccable, fluent, with expressions showing true stylistic mastery: "âme historique," "havre de paix," "splendeur des temples." The itinerary was logistical and realistic: Asakusa with Senso-ji on the first day, Meiji Jingu and Harajuku on the second, Shinkansen to Kyoto and Fushimi Inari on the third, Kinkaku-ji and Kiyomizu-dera on the fourth, Nara with Todai-ji on the fifth. Five full but not impossible days. The practical advice was concrete and useful: the Suica card, the Pocket Wi-Fi, the etiquette of not eating while walking, key phrases in transliterated Japanese.

The Italian section was the best I have obtained on this test in the entire series. No "suggeramenti," no Cyrillic endings, no smudges. Just correct, fluent, useful Italian. A result that the 26B MoE had not reached, at least not so cleanly.

There is, however, a small lexical slip in the title of the fifth day, where the model writes "Les Daimyos," the feudal lords, instead of "Les daims," the sacred deer of Nara. A confusion between two terms that sound similar but have completely different meanings. It does not compromise the understanding of the itinerary, but it is worth noting.

**Score: 5/5.** The best Italian section of the series, with a small French slip that does not dent the overall result.

### Test 5 — Long context: 460 pages on the fly *(Score: 4.8/5)*

*Speed: 10.15 tokens/second*

Here things get interesting. The same AI Index Report 2025 from Stanford, the same PDF of about 460 pages loaded in all previous tests, the same question about the growth of video generation with a request to indicate the reference pages.

The model responded on the first attempt, without blocks, without prompts, which is already a significant improvement over the problems I had with Qwen 3.5. The summary was correct and relevant: emerging models like Runway, Luma, and Kuaishou, the famous example of the "Will Smith eating spaghetti" prompt as a marker of the qualitative leap, the features of Meta's Movie Gen, the comparison between Veo 2 and competitors. Everything present, everything accurate.

However, the page retrieval precision was less granular than in previous tests. The model indicated "around page 127," while Gemma 26B had indicated pages 125-126-127 and Qwen3.6 126-127. It's not an error, it's a less precise answer. The difference between "exactly here" and "roughly here."

The most significant data, however, is another: the speed dropped to 10.15 tokens per second, compared to 17 and more in previous tests. It's the first time in this session that generation slows down significantly. The cause is the saturated context: with 24k active tokens and a huge PDF to process, VRAM fills up and throughput drops. It's not a defect of the model, it's the physics of memory. But it's valuable information for those who have to choose: on tasks requiring very long contexts, fluidity decreases.

**Score: 4.8/5.** Response on the first attempt, but less precise and slower than previous tests. Long context has a cost.

### Test 6 — Spatial reasoning: the room in chaos *(Score: 5/5)*

*Speed: 17.56 tokens/second*

A photograph of a very messy room, the same one used throughout the series. Describe the arrangement of objects and suggest how to tidy up to create more space. A test that measures something hard to standardize: visuospatial intelligence, the ability to see a three-dimensional scene in a two-dimensional photograph and reason about it.

The speed immediately returned to the levels of the first tests, confirming that the drop in the previous test was linked to the long context and not to a generalized problem. The answer was precise and well-organized by functional areas: the bed as a central element submerged by sheets and clothes, the two ladder shelves on the sides of the headboard, the study area with desk and cabinet, the floor as the most critical area. The model noted the blue basket at the foot of the bed, the red plaid on the right side, the mirror that "visually doubles the clutter," the scattered clothes and shoes. The tidying strategy was logical and motivated: first the floor because it is the main obstacle to circulation, then the blue basket as an accumulation point, then the bed, and finally the shelves to reduce visual noise.

Compared to the best tests in the series, the model did not go as far as noticing specific reflections in the mirror with the same level of detail I had seen with Qwen3.5 and Gemma 26B. But the quality of description and planning is still excellent. It's not a step back: it's a different choice of what to emphasize.

**Score: 5/5.** Precise description, logical tidying plan, speed back to optimal levels.

### Test 7 — Multi-step agent: planning a software project *(Score: 5/5)*

*Speed: 17.26 tokens/second*

The test that measures the ability to organize work, not just to execute it. I asked to plan the development of a web app for managing family expenses: tech stack, project structure, detailed roadmap for a team of two developers.

The response demonstrated notable project maturity. The proposed stack was modern and consistent: Next.js with Tailwind for the frontend, Node.js with Prisma ORM for the backend, PostgreSQL, NextAuth.js for authentication, Recharts for graphs, PapaParse for CSV, react-pdf for reports, Resend for emails. Every choice had an implicit logic in the context of the project. The code structure was organized by feature, a professional and scalable approach. The roadmap was divided into eight sprints with clear focuses, concrete deliverables, division of labor between the two developers, and—a detail that makes the difference—identified criticalities for each. "Non-standardized CSV formats," "difficult PDF rendering," "unexpected bugs in production": the ability to anticipate problems before they occur is the signal of a deep understanding of the software development cycle. The concluding strategic advice—"Database First," validation with Zod, unit tests for financial calculations—was practical and worthy of a senior developer.

It's the kind of response an experienced project manager would sign off on, not just a tool that writes code on request.

**Score: 5/5.** Complete, realistic planning, with the right criticalities in the right place.

### Test 8 — Long conversation: coherence over four turns *(Score: 5/5)*

*Speed: from 17.65 to 15.98 tokens/second*

The test that evaluates a quality different from the others: not the skill on a single response, but the ability to maintain the thread through a conversation that builds over time. Qwen3.6 had introduced this trial to test its "thinking preservation" functionality. Here I proposed it again with the same structure: four turns on a collaborative design session, with technological choices that accumulate and refine.

In the first turn, I asked for advice on the stack for a task management app. In the second, how to handle real-time notifications for 1000 concurrent users: the model explained why polling is discouraged and why WebSocket with Redis Pub/Sub is the correct choice, also citing the SSE alternative with pros and cons. In the third, the database schema: six tables in logical order, key relationships, senior developer advice on using UUID, indices, and soft deletes. In the fourth, I asked for a summary of all the choices made and a scalability strategy for 10,000 users.

The model correctly remembered everything. The stack from the first turn, the reasons for WebSocket from the second, the data structures from the third. It spontaneously added a five-point scalability strategy: load balancer, Redis Pub/Sub for distributed connection management, connection pooling with PgBouncer, asynchronous queues with BullMQ, caching. No contradictions, no forgetfulness.

One piece of data is worth reporting: the speed dropped progressively, from 17.65 tokens per second in the first turn to 15.98 in the fourth. The phenomenon is predictable and physically understandable; with each turn the KV cache fills up and the model must manage an increasingly long context. The drop is contained, about 1.7 tokens per second over four turns, and does not compromise fluidity. But it is a real behavior that those who use the model for prolonged work sessions will find useful to know.

**Score: 5/5.** Coherence maintained through four turns, constant quality, marginal drop in speed within the norm.

### Test 9 — Video generation: not yet *(not evaluated)*

As in previous episodes, LM Studio does not yet support video input. The reasons are already explained in the [article on Qwen3.6](https://aitalk.it/it/qwen36-35b-ai.html), where I also documented attempts with alternative formats. The issue remains open and deserves a dedicated deep dive, probably with llama.cpp or vLLM.

## Minimum configuration: how many resources are really needed

One of the most interesting aspects that emerged from this test is that Gemma 4 12B in Q8_0 does not require an extraordinary workstation. Based on my direct experience, here are the minimum requirements to run it acceptably—that is, with a speed around 15-17 tokens per second and without continuous swap on RAM:
![tabella2.jpg](tabella2.jpg)

The comparison with the previous models in the series tells a precise story:
![tabella3.jpg](tabella3.jpg)

The practical conclusion is this: if you have a GPU with 12-14 GB of VRAM, you can run Gemma 4 12B Q8_0 in full GPU with excellent performance. If you have less VRAM, you can go down to Q6 or Q4 and still get decent results. With the larger models, even with aggressive quantizations, you were already at the limit or beyond.
![tabella4.jpg](tabella4.jpg)

## The answer to the question

The arithmetic mean of the eight tests performed is 4.97 out of 5. A high number, but the number is not the most interesting point of this experiment.

The interesting point is the configuration with which it was achieved. For the first time in this series of tests, I ran a model entirely on GPU, 48 layers out of 48, without bottlenecks of any kind. The average speed of about 17 tokens per second was constant and fluid, a midpoint among the models tried that is more than acceptable and that does not push such a machine to its limit, guaranteeing stability in responses and reducing the risk of sudden crashes. And this difference, in daily practice, changes the nature of the interaction.

There is a scene in *Ping Pong the Animation*, the adaptation of Taiyo Matsumoto's manga of the same name, where the more technically gifted character loses to an opponent who should be inferior, simply because the latter plays without any weight on his back, without fear, at the maximum of what he can do. It's not a question of absolute talent: it's a question of free margin between potential and execution. Gemma 4 12B on this configuration gave me the same feeling: a model that plays its entire game, with nothing held back.

The question that motivated this experiment was: "Can a smaller model used at its maximum beat a larger but throttled one?" The answer I'm taking home is yes, for most daily uses. The 12B in Q8_0, with full GPU offload, produces excellent quality responses, is fast, has more predictable latency thanks to the dense architecture, without the variable peaks typical of MoE models, and requires less memory. The 26B MoE in Q4_K_M with partial offload remains an excellent model, but loses in fluidity and responsiveness on standard consumer hardware.

Then there is the issue of multimodal architecture. The 12B, with its unified approach that eliminates separate encoders, promises a more integrated understanding of text and images. I couldn't test the video part due to LM Studio limits, but what I saw on the corporate tables test, where the model didn't just read data but interpreted it in its context, suggests that the design choice is not just theoretically elegant. It works.

The real news, for those reading, is this: today there is a very high-quality model that runs entirely on your consumer GPU, without compromise. You no longer have to choose between "large but throttled model" and "small but insufficient model". Gemma 4 12B is the balance point that many were waiting for. And the fact that it is also architecturally more advanced than its predecessor in multimodal management is the icing on a cake that, this time, has baked well.

---

*All articles in the series: [Qwen 3.5 on my PC](https://aitalk.it/it/qwen3.5-locale-puntata1) — [Gemma 4 26B local](https://aitalk.it/it/gemma4-26b.html) — [Qwen3.6 35B local](https://aitalk.it/it/qwen36-35b-ai.html)*
