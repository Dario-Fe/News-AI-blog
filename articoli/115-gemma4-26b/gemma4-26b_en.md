---
tags: [" Generative AI", "Applications", "Training"]
date: 2026-04-20
author: "Dario Ferrero"
---

# Gemma 4 locally: 26 billion on my PC
![gemma4-26b.jpg](gemma4-26b.jpg)

*There is a particular satisfaction in running something that it would be recommended not to download. Not the satisfaction of the hacker who forks a system, that's different stuff, but that quieter and more artisanal one of those who tighten the screws a bit beyond the recommended torque and discover that the structure holds anyway. It's the kind of satisfaction I found this week, while Gemma 4 26B ran on my consumer PC with a fluidity I didn't expect.*

This article is the second in a series I [started a few weeks ago with Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html). If you have read that piece, you can skip the next paragraph. If instead you are here for the first time, I will quickly give you the coordinates of the project.

## The laboratory, already known

The idea is simple: take newly released open models, run them locally on consumer hardware, and understand what you really get, outside of press releases and marketing benchmarks. The tool is [LM Studio](https://lmstudio.ai/), a desktop application that allows downloading and launching models without opening a terminal, with the very useful feature of showing in advance an estimate of expected performance on your hardware configuration. A color-coded discriminant—green-orange-red—that saves hours of fruitless attempts. The machine is a PC assembled with criteria but without excess: AMD Ryzen 7700 processor, 32 GB of DDR5 RAM, and an AMD Radeon RX 9060 XT GPU with 16 GB of VRAM. High-end user hardware, not a research lab.

The method, I reiterate here as I did at the beginning of the piece on Qwen, is not scientific in the academic sense of the term. There is no peer-reviewed protocol, there is no statistically significant sample of prompts, there is no reproducibility certified by a conference. The tests were verified by cross-referencing results with frontier models like Claude and DeepSeek, but this does not turn them into benchmarks: they remain field tests, conducted with the tools of a demanding user. The grades accompanying each test are personal evaluations, not verdicts.

## Gemma 4: family, architecture, philosophy

Google DeepMind released Gemma 4 on April 2, 2026, under Apache 2.0 license. This is not a secondary detail: it is the first time in the history of the Gemma family that a model has been released under this license, which eliminates any ambiguity about commercial use and puts Gemma 4 on the same permissive level as Qwen 3.5, with which it shares the open-weight ecosystem.

The family consists of four variants: E2B and E4B, designed for deployment on mobile and edge devices with a 128,000 token context window, and the two larger variants, the 26B MoE and the 31B Dense, with a 256,000 token context window. The 31B Dense is the flagship model in terms of raw quality, and at launch it conquered the third global position on the Arena AI text leaderboard, not among open models, but among all models in absolute. The 26B MoE settled in sixth place.

On the 26B MoE it is worth spending two lines of architecture, I promise to be brief. The key concept to keep in mind for reading the rest of this article is only one: the 26B model activates during inference only about 3.8 billion of its total parameters, which makes it significantly faster than the total number would suggest, bringing it closer in terms of speed to a 4 billion parameter model. The price to pay is that all 26 billion parameters must still stay in memory. Fast as a small model, heavy as a large one: a bill paid in VRAM.

Benchmark numbers are impressive, particularly compared to the previous generation. The leap from Gemma 3 is hard to ignore: on AIME 2026 it goes from 20.8% to 89.2%, on LiveCodeBench from 29.1% to 80.0%, on GPQA Science from 42.4% to 84.3%. It's not an incremental optimization. Something structural has changed in the way these models reason.
![grafico1.jpg](grafico1.jpg)
[Image taken from deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

## The choice beyond the limit

Coming to my specific experiment, I chose to test the **Gemma 4 26B A4B Instruct Q4_K_M**, the version with the most aggressive quantization available for the 26 billion variant. The choice was deliberately at the limit: LM Studio flagged this configuration as slightly outside the recommended capabilities for my hardware, indicating it with that orange color that usually suggests lowering expectations or downsizing the choice. I ignored the advice, not out of stubbornness, but because testing the limit was exactly the point.

The Q4_K_M quantization reduces the numerical precision of model weights from 16 bits to about 4 bits, with a technique that seeks to distribute information loss less uniformly and more intelligently compared to flat quantizations, better preserving the weights that the model considers most important. The practical result is a file that occupies about 16 GB on disk and can rely entirely on the 16 GB of VRAM of my GPU, a balance at the limit: Q4_K_M on the 26B MoE model uses approximately 16 GB, just within the limits of a consumer GPU like mine. The quality loss compared to the full version in bfloat16 is real, but how real? This is one of the subtexts of the entire experiment.

I deliberately chose the same six tests used with Qwen 3.5, not because the two models are comparable in a strict sense (one is a dense 9B, the other a 26B MoE), but to maintain a minimum methodological consistency that would allow at least qualitative observations. It is not a head-to-head comparison. It is more like measuring temperature with the same thermometer in two different cities: the numbers are comparable, the cities are not.

## Six trials, six verdicts

### Scientific reasoning: the Higgs mechanism — 5/5

The first test is the one I use as a general thermometer of the model's intelligence: explaining the electroweak symmetry breaking mechanism in the Standard Model, the role of the Higgs field, and why W and Z bosons acquire mass while the photon remains without. Explicit request: precise language but accessible to a physics university student.

The answer surprised me, not so much for the correctness of contents, as for the expository quality. The model organized the explanation in four logical sections with the structure that a good university professor would use, starting from gauge invariance, passing through the "Mexican hat" potential with the condition on the mass term sign, to the concrete physical consequences. Formulas were reported correctly: gauge group SU(2)_L × U(1)_Y, vacuum expectation value, boson masses. But the real strength was the ability to accompany each formula with a comprehensible mental image. When the model wrote that the angular degrees of freedom are "eaten" by the gauge bosons, it was translating an abstract mathematical concept into something that a second-year physicist recognizes immediately. It's the difference between a dictionary and a professor.

A technical detail is worth noting: despite the complexity of reasoning and length of answer, the model reasoned for only 2.2 seconds and generated the text at about 24 tokens per second. For a model that theoretically weighs 26 billion parameters, it is a surprising speed, made possible precisely by the MoE architecture that keeps most weights inactive during generation. **Grade: 5/5.**

### Multimodality: reading a blurry spreadsheet — 5/5

The second test was designed to put visual capabilities to the test with a deliberately difficult input: a small and not sharp photo of a spreadsheet for monthly family budget, with the request to describe the content, main data, and emerging trends.

The model took about ten seconds to analyze the image, a significantly longer time compared to the previous test, understandable for a visual task, before starting generation at about 23 tokens per second. The answer was remarkably complete: it correctly identified the structure of the document, an Excel template with sections for income, savings, and expenses, each with Budget, Actual, and Difference columns. It read key numerical values with millimeter precision: monthly net savings with predicted budget of 1,350 dollars, actual of 2,624 dollars, positive difference of 1,274 dollars. It even noticed the presence of a horizontal bar chart on the right side of the sheet.

But the part that confirmed it wasn't just simple transcription was the analysis: the model autonomously observed that despite the increase in income, actual total expenses had remained close to the predicted budget, and drew a logical conclusion about saving efficiency. From a blurry image to a cash flow analysis. **Grade: 5/5.**
![grafico3.jpg](grafico3.jpg)
Image taken from my PC during tests on LM Studio

### Code: an NP-hard problem with self-correction — 4.5/5

The third test was the most technical: implementing in Python an algorithm to find the maximum length cycle in an undirected graph, handling graphs with multiple cycles and explaining time complexity.

The positive aspects were notable. The model declared without hesitation that the problem is NP-hard, that no polynomial algorithm exists to solve it on generic graphs, and chose backtracking with depth-first search as the correct approach, what anyone who has studied algorithms seriously would use. The representation via adjacency list with dictionary was efficient, the simple path exploration logic correct, the explanation of time complexity clear and honest.

However, the first version of the code contained three syntax errors: a keyword written as `not be in` instead of `not in`, a wrong variable name in a method call, and another variable written incorrectly in the loop condition check. Three errors that, alone, would have prevented execution without manual intervention.

Here however comes the most interesting part of the evaluation. When I asked the model, in a generic way and without indicating what the errors were, to check the code for any syntax problems, it identified and corrected all three on the first attempt. In other words, it already knew how the correct code should be written: it simply hadn't written it with enough attention the first time. This behavior mirrors realistic use of these tools: a programmer rarely blindly trusts the first version generated. The ability to diagnose its own errors upon generic prompting is almost as valuable as perfect initial writing. Almost. **Grade: 4.5/5.**

### Multilingual and planning: Japan in French — 4.8/5

The fourth test evaluated multilingual capabilities and complex planning: acting as a travel agent, planning a five-day itinerary in Japan for a French client who doesn't speak English, with a focus on historical temples and street food, plus a final section in Italian with tips for an Italian tourist.

The French was impeccable, fluent, and error-free, with a professional but not cold tone. Itinerary planning was logistically realistic: first day in Asakusa with Senso-ji and an izakaya in the evening, second between Meiji-jingu shrine and Shibuya, third by shinkansen to Kyoto with Kiyomizu-dera and Gion, fourth to the Golden Pavilion and Arashiyama bamboo forest, fifth to Fushimi Inari. Each day balanced between historical site and gastronomic experience, as requested. Knowledge of Japan was surprisingly detailed: citations of places like Sannenzaka and Ninenzaka, specific foods like Age-manju, practical advice on the Suica card and the Japan Transit application, the mention of Depachika, the basement floors of Japanese department stores, an insider detail not found in generic travel guides.

However, the final section in Italian presented two errors that cannot be ignored. The first was "suggeramenti" instead of "suggerimenti," a term that simply doesn't exist in Italian. The second was stranger: the word "comprare" (to buy) appeared written with a Cyrillic ending, "compraть", as if the model had momentarily lost the thread of the language. Two errors in one hundred and fifty words of Italian, on a language that is not among the rarest in the world. For a model that declares support for over 140 languages, one would expect greater robustness even in secondary languages of an answer. **Grade: 4.8/5.**
![grafico2.jpg](grafico2.jpg)
[Image taken from deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

### Long context: 460 pages of AI at the first attempt — 5/5

The fifth test is the one I consider most significant for real model use: I uploaded Stanford's [AI Index Report 2025](https://aiindex.stanford.edu/report/), a PDF of about 460 pages and over 20 million characters, the same document used in the Qwen 3.5 test. I asked the model, in a generic way, to tell me about the growth of video generation and to indicate the pages where to find the data.

The answer arrived after 4.4 seconds of processing, at 22 tokens per second. The model correctly identified pages 125, 126, and 127, not a vague reference to the "central chapter", but precise and verifiable references. It then provided a structured summary of the contents: Stability AI's Stable Video Diffusion, OpenAI's Sora presented in February 2024 and made public in December, Meta's Movie Gen with editing and audio integration capabilities, Google's Veo and Veo 2. It even cited the famous example of the prompt "Will Smith eating spaghetti," that test that became a meme in the AI community to document progress in video generation.

The comparison with the experience on Qwen 3.5 is illuminating: the 9 billion model had required four attempts and explicit prompting to answer in chat to obtain a similar result. Gemma 4 answered at the first attempt, without hesitation. The 256,000 token context window proved to be not just a technical specification but a truly usable capability on consumer hardware. **Grade: 5/5.**

### Spatial reasoning: the room in chaos — 4.9/5

The last test was the one I love most because it measures something hard to standardize: visuospatial intelligence. I uploaded a photo of a very messy room, the same one used with Qwen 3.5, and asked to describe the arrangement of objects and suggest how to tidy up to create more space. The model took 7.5 seconds to process, the second longest time of the entire test.

The answer opened with a sentence I didn't understand: "No citations were found in user files for this request." A phrase out of context, as if the model had activated a document search mechanism that had nothing to do with the visual task. Beyond that initial oddity, however, the rest of the answer was excellent.

The description was precise: double bed on the right with partially covered white sheets, two tall and narrow bookshelves positioned correctly in relation to the window and desk, gray desk on the left, two windows with vertical striped curtains. But the truly impressive part was the description of objects on the ground: scattered clothes, footwear including a pair of flip-flops, bags, laundry baskets, and the detail that one of the baskets was blue with patterns. This level of fine observation is remarkable.

The only small inaccuracy concerned the mirror: the model placed it on a wardrobe or a chest of drawers, while in the photo it was mounted on the entrance door. An understandable error in a two-dimensional image where the distinction between door and wardrobe can be ambiguous.

The tidying plan was logical and well-motivated: first clothes and fabrics on the floor because they are the main obstacle to walking, then baskets and bags towards a dedicated area, finally the desk and bookshelves to reduce the sense of visual crowding. The priority assigned to "clearing the walkable surface" was correct and practical. **Grade: 4.9/5.**
![tabella-confronto.jpg](tabella-confronto.jpg)

*Just for fun, given the impossibility of comparison due to the size and different characteristics, I propose a table where you can make your own evaluations and choices depending on the hardware available. Despite different sizes, the results are very similar, with preferences for one or the other depending on the task. I must add, however, that in subsequent uses Qwen 3.5 9b showed situations of freezing and no response, which Gemma 4 26b did not show.*

## What remains in hand

The arithmetic average of the six tests is 4.87 out of 5. A number that must be contextually honest.

We are talking about a model with 26 billion total parameters, quantized to its most compressed version, run on consumer hardware slightly underpowered compared to recommended specifications, locally, without cloud, without APIs, without costs per token. The fact that it runs fluidly at speeds that make interaction reactive is in itself a remarkable result. The fact that it answers with this quality makes it something more interesting.

The comparison with Qwen 3.5 9B, the subject of the previous test, is not direct due to size difference, but some qualitative observations emerge clearly. Gemma 4 handles long context with superior reliability, answers at the first attempt without need for prompting, and shows more robust expository coherence in complex tasks. It pays something, however, on the front of syntax perfection in code at first generation, and shows some fragility in secondary languages within the same answer. It is not a surprising trade-off for a model of this size.

The question that remains open, and which is not within the scope of this experiment, is how much Q4_K_M quantization actually cost in terms of quality compared to the full version. The results are high enough to make it difficult to estimate how much margin was left on the table. Perhaps a lot, perhaps surprisingly little. It would be an interesting experiment for those with access to hardware with more VRAM.

What I can say with certainty, as an enthusiast who wants to understand what is possible with normal means in 2026, is that the border between "possible only on cloud" and "possible locally" has shifted again. Not by a little. Gemma 4 26B MoE, even in its most compressed version, on hardware that many advanced users already own, produces answers that until a few months ago would have required an API call to a frontier model. This is the datum I find most significant, more than any single grade.

One thing is certain: what in January I indicated as the trend of the year, the race for [Local Small Language Models](https://aitalk.it/it/slm-2026.html), is not just confirming itself, it is burning stages. And we are only in April.
