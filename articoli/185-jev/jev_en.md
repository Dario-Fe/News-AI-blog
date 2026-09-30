---
tags: ["Generative AI", "Research", "Applications"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Jev Doesn't Chat, It Decides
![jev.jpg](jev.jpg)

*Just days after its launch, a model that doesn't write a single word forces us to ask what artificial intelligence is truly for. Models have been superhuman in chat for years, so where is the automation? That is the question Diogo Almeida opens with in the [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) for Jev, published on September 15, 2026, saying he has been chasing it for four years. He leads TypeSafe, a young San Francisco startup that, according to [The Register](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) and [TS2](https://ts2.tech/en/typesafe-ai-raises-40-million-for-jev-but-its-445x-cost-claim-is-still-self-tested/), raised $40 million in a round led by DCVC.*

His track record is the first argument in his favor. Almeida is listed among the primary authors of [InstructGPT](https://arxiv.org/abs/2203.02155), OpenAI's foundational work on training with human feedback, and [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/) describes him as one of the inventors of RLHF. Precision is needed here: the idea of training a system on human preferences was formalized in a [2017 paper](https://arxiv.org/abs/1706.03741) signed by six authors, and his name is not among them. It is more prudent to say he helped bring it into chatbots, as DCVC also seems to imply in the press release reported by TS2.

The paradox is served: superhuman chatbots, yet automation remains slow and expensive. TypeSafe's answer is a model that completely abandons text generation. It doesn't converse, explain, or tell stories. Like Melville's clerk Bartleby, it would prefer not to. But it does one thing: it decides.

## The Essay and the Light Switch

To turn on a room's light, you shouldn't first have to write an essay explaining that it's dark, then hand it to someone who reads it and decides whether to flip the switch. Automation with a language model currently works much like that. The software passes an unstructured state to the model—say, a customer chat log; the model generates text one word at a time; a second piece of code parses that text and extracts the decision.

The cost is apparent in three areas. First, speed: according to an independent measurement benchmark cited by TypeSafe, flagship models respond in an interval between 3 and 329 seconds—acceptable in a human chat, but a major bottleneck inside software code. Second, price: the post notes $0.20 to $10 per million input tokens, with output roughly five times more expensive. Third, engineering friction. David Linthicum, a consultant interviewed by [InfoWorld](https://www.infoworld.com/article/4223468/typesafe-ais-new-models-work-with-machines-not-humans.html), compares using a generalist model for a simple yes/no decision to mobilizing an entire enterprise service bus for a single routing query, pointing to the endless layers of prompts, schemas, validators, retry logic, and guardrails engineers build around free-form text.

Then there is trust. A model that performs a task well in 95% of cases but doesn't specify which cases are the remaining 5%, TypeSafe argues, doesn't actually automate that task: you know it makes mistakes, but not when. [LangChain](https://www.langchain.com/blog/building-a-harness-with-jev) adds that tool calling and structured outputs have helped, but agentic loops remain slow and costly because every decision requires yet another model invocation.

## Thinking Fast, Thinking Slow

TypeSafe dubbed its new category System One Models in homage to Daniel Kahneman's *Thinking, Fast and Slow*, where System 1 is fast, intuitive thought, and System 2 is slow, deliberate reasoning. In the company's framework, traditional language models sit on the slow side; Jev aims to be the fast mirror. Unstructured state goes in; typed decisions with probability scores come out, without ever generating a sentence. The post summarizes it as a function call powered by frontier intelligence.

The metaphor comes with caveats. The post's FAQ admits that "System 1" can connote error-proneness, promising to explain later why these models can actually be more reliable. Sean Goedecke, author of a [technical blog](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/), notes that Kahneman's book is considered partially discredited due to replication issues.

The name Jev, meanwhile, comes from William Stanley Jevons, the 19th-century economist who observed that more efficient steam engines actually increased overall coal consumption. Almeida's bet is that the same holds for intelligence: every reduction in cost unlocks new use cases. The Register observes that this premise isn't guaranteed, as many people with AI access don't feel the need for it or avoid it due to moral objections.

## Anatomy of a Decision

A language model is a journalist: you hand it a fact, and it writes an article. Jev is an air traffic controller: it receives the situation and narrates nothing; it indicates the runway and with how much confidence.

According to the [documentation](https://docs.typesafe.ai/primitives/choice), you submit a state—which can be a sentence or a structured object—along with a set of questions across three primitive types. The Noul, a term coined by the company, is a yes/no query returning a single probability score. In the example on the [Noul documentation page](https://docs.typesafe.ai/primitives/noul), for a user message like "I've asked three times, can I speak to a real person?", it returns 0.99 for the request for a human operator and 0.93 for the fact that the customer had written previously. The Choice primitive selects among textually described options (up to 255), assigning a probability to each. The Score primitive evaluates on an ordered scale of 2 to 10 described levels: on the [Score documentation page](https://docs.typesafe.ai/primitives/score), a bug breaking exports strictly on Safari receives 0.7 on "defect with workaround" and 0.3 on "complete blocker", yielding a weighted average score of 1.3.

Choice and Score also return a confidence value between 0 and 1, which must be interpreted carefully. The documentation defines it as a calculation on the shape of the probability distribution: high if probability concentrates on one option, low if it is dispersed. It reflects how definitive the answer is, not whether it is correct. The Noul does not have its own confidence score.

All queries execute in parallel and isolation against the same state, meaning adding more questions barely affects latency. Consequently, the guide recommends breaking complex judgments into simpler questions and combining them in your application logic—for instance, weighting severity, customer frustration, and report quality to calculate a priority score.

What Jev doesn't do is as important as what it does. It does not generate text, does not explain its choices, and cannot return an out-of-schema value: if three responses are valid, one of those three will emerge.
![tabella1.jpg](tabella1.jpg)
[Cost comparison table](https://evals.typesafe.ai/)

## Speed and Cost: The Math

Here is why it runs fast. A language model writes its response token by token, with each token waiting for the previous one: like a clerk drafting a report line by line when all you needed was a rubber stamp. Jev, TypeSafe explains, calculates all requested probabilities in a single forward pass. In the benchmark demo on their site cited by The Register, a response arrives in 0.114 seconds compared to 8.566 seconds for GPT-5.6 Terra; the price is $0.042 per million input tokens and zero for output.

The post claims total end-to-end latency between 70 and 500 milliseconds, measured, by the company's admission, from laptops on the US West Coast. InfoWorld notes that the service is currently hosted in a single cloud region.

The headline numbers claim 193.6x faster speed and 444.6x lower cost. They must be read with the disclaimer TypeSafe itself attaches: they come from an internal benchmark on four in-house workflows, using as a baseline the average of GPT-6 Astra and Fable 5.1 responses rather than human ground truth, and the company acknowledges these represent high-end estimates compared to real-world usage. Re-evaluating the public tables, developer [Pere Pages](https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim) found that those two extreme peaks stem from comparing against the slowest and most expensive baseline models. Against GPT-5.6 Terra, which TypeSafe considers an equivalent peer, the advantage is approximately 25x in speed and 76x in cost—figures that match those reported by [DataCamp](https://www.datacamp.com/blog/system-one-models-jev).

Regarding accuracy, Jev agrees with the reference baseline in 67.8% of cases, similar to Terra (67.9%), though on invoice parsing it drops to 61.8% against Terra's 74.7%. External tests remain limited. According to Pages, Mike Taylor of [Every](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) observed Jev catch six out of seven defects where Fable 5.1 caught all seven, running roughly 25x faster at ~580x lower cost. TechCrunch reports that Vercel, replacing an OpenAI model in a command security check, achieved 5x to 18x faster responses with higher accuracy, while Bryo AI's CTO found Gemini slightly more precise for email classification, but 10x to 20x more expensive. These remain individual developer testimonials.

The most reproducible finding applies across the industry. In [TypeSafe's benchmark](https://evals.typesafe.ai/), every model improves when a complex judgment is decomposed into small, typed queries instead of a single prompt; according to Pages, Haiku 4.5 jumps from 18.1% to 53.6% accuracy. That lesson holds true even without using Jev.
![confronto1.jpg](confronto1.jpg)
[Comparison screenshot between Jev and GPT-5.6 Terra](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

## Behind the Curtain

TypeSafe has not disclosed what lies under Jev's hood. [MarkTechPost](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/) notes that neither model weights nor parameter counts have been published. TechCrunch writes that it is based on a transformer architecture but is not a language model, with external observers suspecting an open-weight base model and Almeida stating that the training data is purely synthetic. The training methodology is called RLCD (Reinforcement Learning for Calibrated Decisions): where RLHF rewards human-pleasing text and RLVR rewards programmatically verifiable outputs, RLCD aims to reward honest probabilities—such that when the model states a 70% probability, it is correct seven times out of ten.

A helpful analogy (strictly as a visual): a language model stripped of its text output head and fitted with a panel of decision buttons. Underneath lies conjecture. The most detailed analysis comes from [Archer Hume](https://archerhume.com/posts/jevs-architecture-unmasked/), who probed the API with ~10,000 requests and inferred an architecture where state is read in a single encoder pass and queries evaluate independently, with probabilities extracted directly at the output head. Goedecke suspects the technical advantage may be less mystical than it appears: one can pre-fill a standard decoder's output buffer and request only the token probabilities for specified choices. With a small open model, he measured a 2x to 3x speedup over standard structured output JSON generation.

Open-source implementations popped up within days. [Jevlike](https://github.com/vinnylarouge/jevlike) trains a small model that, given text and a list of options, returns probability distributions in a single pass. In the author's experiments, it achieves ~98% accuracy on synthetic menus and 26% on Wikispeedia player choices (with a frozen small model, vs 8% random baseline); for eight options, it runs ~100x faster than a small decoder generating 400 text tokens. The author cautions this does not match Jev's quality or replicate TypeSafe's method. [SemIf](https://github.com/TheoLeeCJ/SemIf) (formerly OpenJev) takes a different route: reading logits directly from an open model (Qwen3.5-4B) without retraining; in its benchmark, generating text responses took ~5.2x longer than direct logit extraction. For a broader overview, [awesome-jev](https://github.com/cobanov/awesome-jev) curates dozens of community projects.

## Where It Truly Fits

Its natural home is small, repetitive decision-making currently forced through text generation. In Choice documentation's example, a customer writes that shoes arrived late in the wrong size, with two credit card charges. The model assigns 0.60 to returns and 0.38 to billing; application code routes the ticket to returns with a copy to billing, and because the request is vague (confidence 0.16), triggers an automated follow-up asking what the customer prefers rather than guessing.

A second major use case is routing in agentic workflows. LangChain demonstrated a component where Jev evaluates a request and selects the cheapest model capable of executing it, alongside another that audits tool calls before execution to block risky actions. Armin Ronacher, CTO of Earendil, highlighted this to TechCrunch as a natural fit, noting it would be prohibitively expensive with standard LLMs.

Then there is gaming, where latency alters possibilities. In a Doom demo, Jev receives game state described in text (not raw pixels) and selects actions at ~10 queries per second, costing ~$7/hour according to TypeSafe's post. The post admits traditional code plays better: the point is demonstrating an AI player that obeys instructions and handles diverse state representations. In wikiracing, it selects among hundreds of links via a two-stage process exceeding the 255-option limit.

In domains where probabilities decide human outcomes—such as CV screening—that speed presents risks. Awesome-jev recommends keeping high-impact actions behind deterministic rules and human fallbacks, while Doozer AI co-founder Paul Chada reminds InfoWorld that a probability score shows how confident the model was, not *why* it decided so—a crucial distinction for auditors and regulators.
![tabella2.jpg](tabella2.jpg)
[Time comparison table](https://evals.typesafe.ai/)

## Zero Hallucinations, Real Errors

TypeSafe asserts that Jev cannot hallucinate. In a strict sense, this is true, and the company states it transparently: zero is not a benchmark metric but a structural property, because schema constraints guarantee the output always matches the expected format. If the query allows only yes/no, it will never output "maybe" or a hallucinated key. The Register considers comparing this to language models slightly disingenuous, noting it doesn't eliminate errors; Goedecke calls it semantic evasion.

Imagine asking Jev whether a candidate's experience is 3–5 years or 6–10 years. The model might return "6–10 years" with 85% probability when a careful human reader sees 3 years. Perfect schema formatting, wrong decision, high confidence. Pages, citing commentator Anthony Maio, summarizes it succinctly: the schema constrains response shape, not judgment accuracy. Similarly, if asked whether a bio mentions a PhD when the text is silent, the model might guess "yes" at 65% probability. The remedy is designing schemas with explicit escape hatches—adding "other" or "none of the above" to choice lists. For yes/no, a 0.5 Noul score doesn't mean "neutral"; it simply means yes and no are evaluated as equally probable.

The core question is whether probability scores are well-calibrated. Pages notes that TypeSafe has not published calibration curves. One independent probe exists (by a single developer, single account, single region): Hume calculated an Expected Calibration Error (ECE) of 0.031 across 1,200 MMLU questions—which is solid. However, on custom math problems, the model answered correctly 56% of the time with a declared average probability of 35%. Furthermore, reversing choice order shifted probabilities (e.g., from 0.84–0.89 to 0.93–0.96), meaning a 0.9 threshold might trigger or fail due to option ordering alone.

In Lucas Pope's *Papers, Please*, where you stamp "approved" or "denied" on passports in an endless line, the difficulty isn't stamping—it's knowing when to trust the documents. Tuning Jev's thresholds is that exact job: every stamp fits the schema, but not every stamp is right.

## Skeptics, Rivals, and Open Questions

Developers already using LLMs with structured outputs might ask what actually changes. Pages compares three approaches: a classical classifier (like BERT) is blazing fast but requires thousands of labeled examples and retraining for every new task; an LLM with JSON schema is flexible but slow and costly, with uncalibrated probabilities; Jev promises the flexibility of the latter with the speed of the former, alongside native probabilities whose calibration remains to be verified broadly.

Who benefits? InfoWorld analysts expect Jev to complement generalist models—leaving open-ended reasoning, summarization, and chat to LLMs, while offloading routing, scoring, auditing, and compliance checks to System 1 models. But the equation isn't purely technical. HyperFrame Research's Stephanie Walter points out that questions, choices, and thresholds must be defined upfront, while Broadcom's Advait Patel highlights startup risk around security, data residency, and vendor lock-in. TypeSafe acknowledges it cannot prove its pricing isn't subsidized. Ronacher predicts competitors will emerge now that the pattern is clear, while TechCrunch reports TypeSafe briefly suffered API outages due to overwhelming launch demand.

Open questions remain that only time and independent testing can resolve: Do probabilities hold calibration outside TypeSafe's four test workflows? How does it perform against human ground truth benchmarks? Will an RLCD technical paper be published? Will multi-region deployment arrive, and at what cost? And if Jevons was right, who audits the system when automated decisions reach millions per day?

Fewer words, more executable decisions: Jev isn't just another model, but a different way software interacts with AI. Linthicum envisions fast-reflex models alongside slow-thinking LLMs; Almeida dreams of ubiquitous intelligent software as commonplace as the early Web. If they are right, the future AI ecosystem will be an orchestra of small specialists directed by a model that speaks. If they are wrong, the core lesson remains invaluable: break complex judgments into simple questions, and always ask how much you can trust the answer.

---

*Data updated as of September 20, 2026. Speed, cost, and accuracy claims originate from TypeSafe or individual developers; no comprehensive independent peer-reviewed benchmarks currently exist.*
