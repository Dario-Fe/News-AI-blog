---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-01
author: "Dario Ferrero"
---

# More Agents, Less Intelligence? Stanford Questions Multi-Agent Architecture
![agenti-multipli-stanford.jpg](agenti-multipli-stanford.jpg)

*There's a cult scene in "Primer," Shane Carruth's low-budget sci-fi film, where two engineers build a time machine in their home garage, convinced that the more components they add, the better it will work. Then they discover, in the most painful way possible, that complexity is not synonymous with power: it's just complexity. The artificial intelligence industry is currently going through a similar philosophical crisis, albeit decidedly less temporal, regarding multi-agent systems. And a paper, published by two Stanford researchers in April 2026, has the merit of putting its finger exactly on the wound.*

The title of the paper: [*Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*](https://arxiv.org/abs/2604.02460), is one of those that leave no room for interpretation. A single agent, under the right conditions, beats a multi-agent system. Not always, not everywhere, not for trivial reasons. But it beats it.

## What is an agent, and why do we suddenly need more and more of them

Before understanding why the paper is relevant, it's worth stopping for a moment on what we mean when we say "agent" in the context of large language models. An agent, in this context, is simply an instance of a language model that is given a task: it receives an input text, a question, a problem, an instruction, "reasons" on it, and produces an answer. That's it. The model thinks, answers, end of story.

A multi-agent system, on the other hand, is a pipeline in which several of these agents work together, each seeing only a part of the problem or a portion of the available information, and communicating through generated text. Typically, there is a planner that decomposes the problem into sub-problems, a set of specialized workers that each tackle their own part, and an aggregator that synthesizes the partial answers into a final answer.

The intuitive idea is powerful: divide and conquer. It seems almost obvious that distributing a complex task among specialized agents should produce better results than what a single mind can do. It's the exact same logic that leads us to think that an orchestra sounds better than a soloist, that a team of surgeons operates better than one alone, that a creative collective produces more than an isolated individual. And in many contexts, it's true. The problem is that with language models, the comparison is almost always done incorrectly.

## The trick of the hidden bill

When a multi-agent system seems to beat a single agent, there is almost always a very simple reason behind it: it used more computational resources. It's not a better architecture. It's just that it "thought" more, in the literal sense of the term: it generated more intermediate reasoning tokens.

Modern language models, especially "reasoning" ones like DeepSeek, Gemini, or Qwen, produce a flow of internal thought before responding, the so-called *thinking tokens*. These tokens do not appear in the final answer, but they are the means by which the model reasons step-by-step before producing the output. They are computationally expensive, and the number of tokens a model uses internally is directly proportional to the quality of the answers on complex tasks.

Now, the problem is that in a multi-agent system, each agent has its own budget of reasoning tokens. If you have five agents and each thinks for a thousand tokens, the system has consumed five thousand reasoning tokens in total. If you then compare this system with a single agent that you only gave a thousand to, you are making an unequal comparison. It's like comparing an athlete who trains five hours a day with one who trains for an hour, and then being surprised that the former runs faster.

This is exactly the point that Dat Tran and Douwe Kiela of Stanford decided to address with methodological rigor. Their approach is simple: impose an equal total budget of thinking tokens for all systems, and then measure who performs better. Not prompt tokens, not output tokens, just intermediate reasoning tokens. Then see what happens.

## The testing ground: chain questions and multi-step answers

The researchers chose two specific benchmarks for their experiments. The first is [FRAMES](https://arxiv.org/abs/2409.12941), a dataset designed to test the ability to retrieve and synthesize information from multiple sources. The second is [MuSiQue](https://arxiv.org/abs/2108.00573), filtered to include only four-hop questions, i.e., those that require concatenating four distinct reasoning steps to arrive at the correct answer. Such as: "In which country is the birthplace of the director of the film that won award X in the year in which the author of book Y was born?" This isn't a real example, but it gives an idea of the complexity: each answer is tied to the previous one, and missing one link means losing the whole chain.

The model families used are three: Qwen3-30B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash, and Gemini 2.5 Pro. The thinking token budgets tested range from 100 to 10,000, across six levels. And the multi-agent architectures compared are five, all described in detail in the paper: Sequential (a planner that divides the problem into steps, agents that execute in series, a final aggregator), Parallel for Subtasks (same logic but workers operate in parallel), Parallel Roles (one solver, one fact extractor, one skeptic, and a second solver operating in parallel), Debate (two agents confront each other and then criticize each other), and finally Ensemble (multiple agents respond independently and a judge chooses the best answer).

The most interesting architecture from a theoretical point of view is Sequential, because it is the cleanest comparison with the single agent: both tackle the problem serially, both use the same total budget, the only difference being that in the multi-agent system the intermediate reasoning is externalized in explicit messages between agents, while in the single agent it remains latent within a continuous chain of thought.

## The mathematics that tells us why the single agent should win

Before looking at the numbers, the researchers build a theoretical argument that deserves to be understood, because it has implications that go far beyond this specific paper.

The argument is based on the "Data Processing Inequality," a classic result in information theory. In very simple words, it says this: whatever transformation you apply to information, you cannot increase the amount of information it contains about the answer you are looking for. You can only preserve it or lose it.

In the context of multi-agent systems, this translates into a direct observation: the messages an agent passes to the next agent are a function of the original context. That function cannot create information out of thin air. Therefore, the original context, seen in its entirety by a single agent, always contains at least as much useful information as any message extracted from it. Every time information is "summarized" and passed from one agent to another, something is inevitably lost. Communication is always a funnel.

The practical corollary is immediate: if a single agent can see all the available context and has the same computational budget as a multi-agent system, there is no theoretical reason why the multi-agent system should perform better. It could do the same. Not better.

But there is an exception, and that is where the paper becomes really interesting.
![tabella1.jpg](tabella1.jpg)
[Image taken from arxiv.org](https://arxiv.org/abs/2604.02460)

## When the context is degraded: the only case where multi-agents recover

The theoretical guarantee of the single agent holds only if the single agent uses the context perfectly. And modern language models do not. There are well-documented phenomena in the literature, from attention dilution to the so-called "lost in the middle"—the fact that models tend to remember information better at the beginning and end of a long context rather than in the middle—which show that the ability to efficiently use a very long context is not a given.

The researchers formalize this as "context degradation" and model it experimentally through four modes: deleting parts of the relevant text, masking key information, replacing it with incorrect text, and inserting misleading distractors. As the level of degradation increases, the theoretical guarantee of the single agent weakens, because the single agent no longer operates on the intact context but on a noisy version of it. In this case, a well-designed multi-agent system can partially compensate for that noise through task structuring: different agents seeing different parts, verifying each other, filtering noise through multiple steps.

The crucial point is "partially." Even under severe degradation conditions, multi-agent systems do not become clearly dominant: they become *comparable* to the single agent. The advantage of the single agent reduces, but it does not continuously invert.

## The numbers, which are the uncomfortable part

Table 1 of the paper, covering 192 combinations of model, dataset, budget, and architecture, is one of those you look at somewhat slowly. Not because the results are ambiguous, but because the complexity is real and deserves respect.

The main result is that, at equal thinking token budgets, the single agent (SAS) is the strongest architecture or statistically indistinguishable from the best architecture in practically all cases above the minimum budget of 100 tokens. With 100 tokens, the model produces no useful reasoning, either as a single agent or as a multi-agent, so that level says nothing interesting.

Looking at intermediate and high budgets, the pattern is stable. At 1,000 thinking tokens, for example, the average across all models and datasets is 0.418 for SAS versus 0.379 for Sequential, 0.369 for Parallel, and 0.333 for Ensemble. At 2,000 tokens, 0.421 for SAS versus 0.389 for Sequential. At 5,000 tokens, 0.427 for SAS versus 0.386 for Sequential. The distance tends not to amplify or disappear as the budget increases, but remains consistent.

There are exceptions: with Gemini 2.5 Pro at low budgets, the Sequential and Debate systems have competitive numbers, sometimes slightly higher. But these cases are partly explained by a specific technical artifact of Gemini that deserves separate mention.

## The Gemini problem and opaque token accounting

One of the most interesting diagnostic sections of the paper concerns Gemini 2.5, and reveals something quite uncomfortable about how the APIs of these models work in practice.

When a thinking token budget is set for Gemini via API, the number of thinking tokens actually "visible," i.e., emerging in the response text, tends to be much lower than the requested budget in the case of the single agent. The researchers show that Gemini seems to "think internally" in an opaque way, producing less visible reasoning text than the budget would allow, while in a multi-agent system with multiple API calls, the total amount of visible thinking is higher, simply because there are more calls extracting reasoning text.

This means that, for Gemini, comparisons at equal nominal budget are not entirely reliable: the single agent might actually be using *less* actual compute than requested, while the multi-agent system uses more through multiple calls. It's an irregularity in how Gemini handles thinking tokens internally, not an architectural advantage of the multi-agent system.

To compensate for this, the researchers developed the SAS-Lm "Longer Thinking" variant, which adds a structured instruction to the single agent's prompt: before responding, identify ambiguities, propose interpretations, evaluate them, then respond. This small change pushes Gemini to produce more visible reasoning text, bringing the actual compute closer to the nominal one. The result is that SAS-L improves significantly on Gemini 2.5 Flash and Pro, while having negligible or neutral effects on Qwen3 and DeepSeek, where the opaque accounting problem does not exist. For Gemini 2.5 Flash on MuSiQue, SAS-L is the strongest architecture in every budget range. A significant datum.

## The fragility of benchmarks: the paraphrasing test

There is another analysis in the paper that deserves attention, because it touches on a methodological issue that plagues the entire literature on language models: how much do the results depend on the exact wording of the questions?

The researchers conducted an ablation study with paraphrases: they rewrote the benchmark questions with different terms but equivalent meaning, and then measured how much the results changed. The answer is: quite a bit. The accuracy of the models changes significantly when the questions are paraphrased, which suggests that part of the results depends on the fact that the models "recognize" the benchmark questions, having seen similar or identical formulations during training, and answer them partially by memory rather than by pure reasoning. This phenomenon, known as *benchmark contamination* or memorization, is a cross-cutting problem in all language model evaluation, and the paper honestly points it out as a limitation.

The good news is that contamination seems to be distributed relatively uniformly between SAS and MAS: it's not that multi-agent systems benefit systematically more than the single agent, or vice versa. But it's a warning not to take absolute accuracy numbers as definitive truth.
![grafico1.jpg](grafico1.jpg)
[Image taken from arxiv.org](https://arxiv.org/abs/2604.02460)

## The honest limit: FRAMES and MuSiQue are not the real world

The paper is also rigorous in its admissions. The two chosen benchmarks, FRAMES and MuSiQue, are excellent for isolating chain-of-reasoning capabilities on structured data. But they are not representative of all the tasks in which multi-agent systems are actually used. They are relatively "clean": the questions have well-defined correct answers, the context is provided explicitly, there are no external tools, there is no uncertainty about sources, there is no real-world ambiguity.

A multi-agent system for corporate document analysis that includes web search, database extraction, source verification, and report generation operates in a much more chaotic environment than the one tested in the paper. The researchers explicitly recognize this limit in the dedicated section and invite not to generalize the results beyond the domain of multi-hop reasoning on intact context. It's a warning to keep in mind, and one we'll come back to.

Similarly, the evaluation metric used, LLM-as-a-judge—i.e., using another language model to judge the correctness of answers—has its own limits. The judge can be influenced by the format of the answers, by verbosity, by the "confidence" with which an architecture presents its conclusions. Multi-agent systems, which aggregate responses from multiple agents, often produce more elaborate and structured answers, which a judge might evaluate positively even when the factual content is similar. The researchers tried to minimize this effect by using a fixed rubric, but the risk of a systematic judge bias cannot be completely eliminated.

## When orchestration is true architecture

All that said, we come to the question that really matters for those who must decide how to build real systems: when does it make sense to use a multi-agent system and when is it instead compute masked as complexity?

The paper's answer, integrated with the broader context, leads to a distinction between two very different scenarios.

The first scenario where orchestration makes genuine sense is one where the task requires operationally distinct and non-interchangeable phases: searching in external sources, structured data retrieval, factual verification, planning, tool execution, quality control. In these cases, separation into agents is not an architectural choice to improve reasoning; it is an operational necessity. The agent searching the web cannot do the same thing as the agent generating executable code. It's not about dividing a reasoning problem, but about orchestrating different capabilities that cannot coexist in a single prompt.

The second scenario where orchestration becomes relevant is exactly the one the paper identifies theoretically and verifies experimentally: when the context available to the single agent is degraded, fragmented, noisy, or too long to be used efficiently. In these cases, distributing the work among agents who each see a smaller, more manageable portion of the context can compensate for the loss of reasoning quality that the single agent experiences when faced with a deteriorated context. It's not a magic solution, and the paper shows that even in these cases the multi-agent advantage is often modest, but it's a real and theoretically grounded direction.

There is also a third scenario, not directly tested in the paper but consistent with its theoretical framework: tasks in which the number of steps required cannot be determined in advance, and where orchestration serves to manage operational complexity that changes dynamically during execution. A system that must monitor an ongoing process, adapt to unforeseen intermediate results, and coordinate actions across multiple systems cannot be reduced to a single prompt with a fixed budget. Here orchestration is not a performance choice but a structural necessity.

## When it's just disguised compute

The situations in which multi-agentness is not useful, or of little use, are perhaps the most important for those who must decide what to build and what not to build.

The most common pseudo-architecture pattern is the system that performs better than the single agent simply because it uses more total compute, without there being any real structural advantage. If your multi-agent system produces better results only because it has five times more reasoning tokens distributed among agents, you don't have a smarter architecture: you have a richer single agent hiding behind a more complex interface. The paper's data shows this clearly: when the total budget is controlled and equal, the advantage reduces or disappears.

A specific version of this problem is the Ensemble: multiple agents responding independently to the same question, and then a judge choosing the best answer. The intuition is that of the "wisdom of the crowd," the law of large numbers applied to artificial intelligence. But the paper shows that Ensemble is almost always the worst architecture among those multi-agent systems tested, with averages systematically lower than the single agent and often lower than other multi-agent architectures. The reason is that sampling more responses from the same model doesn't produce true diversity if the model is already capable enough: it produces variance, not quality. You are buying statistical margin, not better reasoning.

The same applies to the Debate architecture, two agents criticizing each other, which produces results on average similar to Sequential but not superior to the single agent. The idea that debate among agents leads to better reasoning is seductive, but it only works when the agents have genuinely different information or perspectives. If two instances of the same model tackle the same problem with the same context, the criticism tends to be superficial or quickly converge on the same answer, without the interaction adding real value.

The easiest signal to recognize to understand if you are in the "disguised compute" territory is simple: remove the extra tokens and the advantage disappears. If your multi-agent system only works well when you have it perform more attempts, more internal discussions, more verification iterations compared to a single agent with an equivalent budget, you don't have a better architecture. You have a single agent with a decorative wrapper around it.

## The final question: what changes, in practice?

For those building real systems, the practical implications of this paper are concrete and immediate. The first is that the costs of a multi-agent system are not only monetary. There are observability costs—a system with five communicating agents is much harder to inspect and debug than a single agent—and maintenance costs, because every interface between agents is a potential point of failure. If performance is equivalent, the single agent is almost always preferable for operational simplicity.

The second implication is that the choice of architecture should be guided by the structure of the task, not by expectations or marketing. A complex reasoning task on a well-defined context doesn't need orchestration. A workflow that includes retrieval from external sources, code execution, and cross-verification probably does.

The third, and perhaps most important, is that every time different architectures are compared, you must look at the total compute consumed, not just the result. A multi-agent system that beats a single agent using five times more resources is not more efficient: it's more expensive. The right question isn't "who wins?" but "who wins with equal resources?".

The Stanford paper doesn't say that multi-agent systems are useless. It says something more precise and useful: they are not universally better, their presumed advantage is often a computational artifact, and for tasks where reasoning is the main bottleneck, a single agent with a good budget is hard to beat. Understanding when this rule applies and when operational complexity truly requires orchestration is the distinction that separates a well-designed AI architecture from one that is merely, to use a word that still carries an aura of myth in the industry, "agentic."
