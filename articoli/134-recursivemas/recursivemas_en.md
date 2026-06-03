---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-06-03
author: "Dario Ferrero"
---

# RecursiveMAS has abolished tokens, agents speak in their own language 
![recursivemas.jpg](recursivemas.jpg)

*A paper published on April 28, 2026, by researchers from UIUC, Stanford, NVIDIA, and MIT proposes a radical architectural shift: AI agents collaborating without exchanging text, communicating directly in latent space. The numbers are convincing. The open questions even more so. Let's discover RecursiveMAS, the framework that transforms agents into a 'recursive collective brain'*.

Imagine a team of specialists who must solve a complex case: a cardiologist, a neurologist, an anesthesiologist. Every time one of them has an intuition, however, they cannot simply pass it to their colleague; they must first translate it into a formal email, send it, wait for the other to read it, interpret it, formulate a response, write it, and send it back. And so on, with every exchange. Thinking slows down, costs increase, and something is lost in translation.

This is, with a useful approximation, the fundamental problem of language-based multi-agent systems. Every AI agent receives input in textual form, processes it, and produces textual output, which is passed to the next agent as new input. Every step requires decoding from the vocabulary (a computationally expensive operation), latency, and tokens—meaning money. If you add recursion, where the system must perform multiple rounds of collaboration to refine the answer, the problem multiplies: at each round, every agent must decode everything from scratch.

[RecursiveMAS](https://arxiv.org/abs/2604.25917), the framework presented on April 28, 2026, by a team of twelve researchers distributed among UIUC, Stanford, NVIDIA, and MIT, starts from a seemingly simple question: what if agents stopped talking to each other in text?

## Recursion as a system principle

To understand the scope of the proposal, a step back is necessary. In recent years, recursion—the idea of "looping" the same processing on internal model states to deepen reasoning—has established itself as one of the new scaling axes for large language models. Instead of training increasingly larger models, one can take a reasonably sized model and have it iterate multiple times on the same problem, progressively refining its internal representations. This approach, called *recursive language model* (RLM) in literature, has shown promising results in research over the last two years.

The conceptual leap of RecursiveMAS consists in extending this principle from the inside of a single model to the entire multi-agent system. No longer recursion within an agent, but recursion of the system as a unit. The entire collaboration between agents becomes a unique recursive loop, in which information flows continuously, in the form of latent states, not text, from one agent to another, and the circle closes: the last agent passes its internal state to the first, which can then restart processing with the information accumulated in the previous round.

The result is what the paper describes as a *recursive collective brain*: each agent acts as a layer of a recursive model, and the entire system iteratively converges toward an answer without ever, except in the last round, producing intermediate text.

## RecursiveLink: the lightweight interpreter

The most delicate technical problem is that of translation between worlds. In a heterogeneous multi-agent system, where each agent is a different model with a different architecture and hidden size, how do you transfer a latent state from one model to another without converting it to text?

The answer proposed by RecursiveMAS is the [RecursiveLink](https://recursivemas.github.io/) module: a lightweight component with two residual layers that acts as an interpreter between the latent spaces of different models. In its internal variant (*inner link*), it operates within each individual agent during generation: instead of projecting the hidden state onto the vocabulary to produce a token, it transforms it and reinjects it as input for the next step, keeping the reasoning entirely in the continuous space. In the external variant (*outer link*), it adds an additional linear layer to project the latent state of one agent into the dimensional space of the next, allowing transfer even between models with incompatible internal geometries.

The choice of the residual connection is not aesthetic: maintaining the original component of the latent state means that the module doesn't have to learn the entire projection from scratch, but only the *difference*, the gap between the source and destination space. This makes training more stable and efficient.

The most surprising thing, however, is the size of the trained component. While the base parameters of all agents remain completely frozen, RecursiveLink introduces only about 13 million trainable parameters to the entire system, equal to 0.31% of the total parameters. To give an idea of the proportion: it's like optimizing a symphony orchestra by acting exclusively on the amplification system between the music stands, without touching any instrument.
![grafico1.jpg](grafico1.jpg)
[Image taken from arxiv.org](https://arxiv.org/html/2604.25917v1)

## Inner loop, outer loop: training an entire system

The other structural innovation of the framework concerns the training method. Optimizing a recursive multi-agent system coherently is not trivial: if models are trained separately, each learns to behave well in isolation but not necessarily to collaborate. If, instead, you try to optimize them all together from the beginning, complexity explodes and gradients tend to vanish through the recursive rounds.

RecursiveMAS proposes a two-phase algorithm called *inner-outer loop learning*. In the first phase, the inner loop trains each agent's *inner link* in parallel and independently, using the cosine similarity between the produced latent thoughts and the distribution of correct tokens in the embedding layer as an objective. This is a warm-start: each agent is taught to think in latent space without yet worrying about how it will interact with others.

In the second phase, the outer loop optimizes the entire system as a unit. The framework is deployed for *n* recursive rounds, and only at the end of the last round is a textual response produced on which to calculate the loss. The gradient is then backpropagated through the entire recursive chain, assigning a shared credit signal to each outer link based on its contribution to the final prediction. Each link thus learns not only from its local error but from the overall quality of the entire system on every single example.

The main theorem of the paper (Theorem 4.1) formally demonstrates why this approach works better than the text-based one: gradients passing through the residual RecursiveLinks remain stable through the rounds, while in the case of text—where the projection onto the vocabulary introduces a discontinuity—they tend to collapse toward zero as recursive depth increases. A vanishing gradient means a system that stops learning.

## The numbers: nine benchmarks, four patterns

RecursiveMAS was tested on nine benchmarks covering mathematics (MATH500, AIME 2025, AIME 2026), science and medicine (GPQA-Diamond, MedQA), code generation (LiveCodeBench, MBPP+), and web search (HotpotQA, Bamboogle). The models involved include Qwen3/3.5, LLaMA-3, Gemma3, and Mistral, in configurations ranging from less than 1.5 billion to about 10 billion parameters per agent.

The results compared to all baselines—single agent with LoRA, single agent with full fine-tuning, Mixture-of-Agents, TextGrad, LoopLM, Recursive-TextMAS—show an average improvement of 8.3 percentage points in accuracy. The most striking gain is recorded on dense mathematical reasoning benchmarks: on AIME 2025, the *scaled* version of RecursiveMAS reaches 86.7% against 73.3% of the best comparable baseline. Importantly, the advantage grows with recursive depth: at *r* = 1 (a single round), the average improvement is 3.4 points; at *r* = 3, it rises to 7.2. Text-based systems, by comparison, tend to worsen or stabilize with deeper recursion, a sign that they accumulate errors at each round instead of refining themselves.

On the efficiency front, the data is even clearer. Compared to an equivalent recursive multi-agent system based on text, RecursiveMAS offers a speedup from 1.2× at *r* = 1 to 2.4× at *r* = 3, with a reduction in consumed tokens ranging from 34.6% to 75.6%. The estimated training cost is $4.27 compared to $9.67 for full fine-tuning, and with less GPU memory: 15.29 GB peak versus the 41.40 required by full SFT.

The framework was tested on four distinct collaboration patterns: *Sequential* (Planner, Critic, Solver in sequence), *Mixture* (specialists in parallel aggregated by a Summarizer), *Distillation* (a larger expert agent instructing a smaller apprentice agent), and *Deliberation* (an internal Reflector coupled with a Tool-Caller accessing Python and search APIs). In all four contexts, RecursiveMAS outperforms the strongest single agent in the corresponding configuration.

## When agents stop talking

So much for the numbers. But there is a question that numbers do not solve, and it concerns something more uncomfortable: if agents no longer speak to each other in natural language, how does a human being understand what is happening?

In traditional multi-agent systems, every textual exchange between agents is, in principle, readable. An engineer can open the log, scroll through the conversation between the Planner and the Solver, understand where the reasoning took a wrong turn, and intervene. The textual trace is a form of implicit transparency: the system thinks out loud, and that voice is understandable.

In RecursiveMAS, intermediate rounds do not produce text. The latent thoughts—high-dimensional vector representations passing between models through RecursiveLinks—do not have a natural translation into human language. The paper includes analyses of semantic distributions in the latent space through the rounds, showing that semantic coherence is maintained and that relevant concepts crystallize progressively, but this is a technical reassurance, not an accessible window into the system's cognition.

The true contribution of RecursiveMAS, as observed in an analysis on Towards AI, is the extension of the COCONUT style—continuous thought in latent space—across agents via the RecursiveLink adapter. But COCONUT, presented by Meta in 2024, had already raised this concern in the context of a single model: when a system reasons without emitting intermediate text, standard mechanisms of interpretability, attention analysis, layer probing, and vector steering become much harder to apply to the entire computational flow.

The mechanistic interpretability research community, which has made remarkable progress in recent years in understanding how individual transformers process information, faces a new frontier: systems where the units of analysis are no longer the layers of a single model, but the latent passages between heterogeneous models. The RecursiveMAS paper does not explicitly address this point, a gap worth noting.

This is not alarmism. Most practical applications of these systems—code generation, question answering, mathematical reasoning—do not require real-time transparency into intermediate rounds. The point is more subtle: in high-risk deployment scenarios, or when a system produces an unexpected result and one needs to understand why, the lack of an intermediate textual trace makes debugging structurally more difficult. The cost of speed is, in part, paid in understandability.
![grafico2.jpg](grafico2.jpg)
[Image taken from arxiv.org](https://arxiv.org/html/2604.25917v1)

## Limits, gaps, and intellectual honesty

The paper does not dedicate an explicit section to its limits, an editorial choice common in academic research but worth compensating for with external analysis.

The first point is the nature of the benchmarks. All nine tests used are standardized datasets built around problems with a verifiable and unique answer: equations, multiple choice in medicine, mathematical competition problems, code generation evaluated with automatic tests. These are the benchmarks by which the community measures progress, and they make sense as a comparative baseline. But they say nothing about how RecursiveMAS would behave in open-ended tasks, long document drafting, ambiguous text analysis, or multi-step planning with human feedback, where response quality is not binary and the process matters as much as the result.

The second point concerns external tools. The *Deliberation* pattern includes the use of Python and search APIs, and it is encouraging that the framework holds up in this context. But integration with external tools has remained intentionally simple: two types of tools in a controlled configuration. Real agentic systems in production handle dozens of heterogeneous tools with variable latencies, network errors, and unstructured outputs. How does RecursiveLink behave when the latent chain is interrupted by an API call that takes three seconds? This question remains unanswered.

The third limit is scalability. The tests presented involve a maximum of four agents. Multi-agent architectures in production can easily reach dozens of specialized agents. The theoretical complexity of the system scales linearly with the number of agents *N*, but the practical management of RecursiveLinks between increasingly diverse model families, with different hidden sizes, different tokenizers, and different specializations, is a non-trivial engineering problem on which the paper is silent.

Finally, there is the issue of reproducibility. At the time of publication, the [official GitHub repository](https://github.com/RecursiveMAS/RecursiveMAS) includes the code for inference and the demo, but marks the release of the complete training pipeline and training data as still in progress. Independently verifying the reported results—an essential practice in the scientific community—therefore requires waiting for these assets to be released.

## A turning point, not a destination

RecursiveMAS is the first demonstration that recursion can work as an architectural principle at the system level, shifting the conversation from "how do we optimize each individual agent?" to "how do we evolve the system as a unified entity?". The numbers—+8.3% average accuracy, up to 2.4 times faster, three-quarters of tokens saved, halved training cost—are obtained under controlled conditions and should be read with that caution, but they cannot be ignored.

The most difficult questions remain open: how much does it scale with dozens of agents? How does it behave on real and ambiguous tasks? How is understandability maintained when intermediate rounds become invisible? Those who build AI systems for critical environments have every interest in not dismissing these as implementation details.

One thing seems clear: the future of AI agents will not be a linear chain of prompts and responses. It will be a loop. The question is who will decide how that loop is designed, and with what guarantees of transparency about what happens inside it.
