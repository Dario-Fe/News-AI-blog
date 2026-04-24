---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-04-24
author: "Dario Ferrero"
---

# Learning memory: Karpathy challenges RAG with an evolutionary knowledge base
![llm-knowledge-base.jpg](llm-knowledge-base.jpg)

*There is a moment that anyone who has worked intensely with a language model knows well: the reset. You are building something complex, perhaps an elaborate software architecture or research weaving together dozens of sources, and the model has understood everything, keeps the thread, responds with surgical precision. Then the session ends, or you reach the context limit, and the AI forgets everything. It starts from zero. You have to explain again who you are, what you are doing, what decisions you made together. It’s like Christopher Nolan's film "Memento," where the protagonist must tattoo information on his body because short-term memory doesn't work: brutal, redundant, and deeply frustrating.*

Andrej Karpathy, former director of AI at Tesla and co-founder of OpenAI, now engaged in an independent project, described this problem in exactly these terms, and on April 2, 2026, he [published on X](https://x.com/karpathy/status/2039805659525644595) a proposal to solve it. The post went viral with over 16 million views, and the [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) for in-depth study exceeded 5,000 stars in a few days. He wasn't announcing a new model or a benchmark. He was describing a change in the way he himself uses language models, a change that triggered a heated technical debate and, as often happens, some oversimplification.

## What RAG is, and why it became the dominant method

Before understanding what Karpathy proposes, it is worth explaining what RAG does, because in the last three years it has become the standard approach to giving language models access to external knowledge, and because it carries some structural problems that not everyone names explicitly.

Retrieval-Augmented Generation literally means generation augmented by retrieval. In a standard RAG system, documents are cut into arbitrary fragments called "chunks," converted into mathematical vectors called embeddings, and stored in a specialized database. When the user asks a question, the system performs a "similarity search" to find the most relevant fragments and inserts them into the model's context.

The mechanism works, and works well in many scenarios. But it carries some characteristics that in certain contexts become problems. The first is the fundamentally stateless nature of the system: every query starts from scratch, searching among sources again, without anything accumulating over time. There is no memory of past elaborations, no accumulation of knowledge. The second problem concerns retrieval quality: cutting a document into pieces and searching by vector similarity works well when the answer lies in one or two contiguous fragments, but becomes imprecise when a question requires synthesizing ideas distributed across dozens of different sources. The third, often underestimated, is infrastructural complexity: vector databases, embedding pipelines, indexing systems—all this has a cost in terms of latency, maintenance, and opacity. Vectors are not readable by any human, making it hard to understand why the system retrieved certain fragments instead of others.

## How the memory machine works

Karpathy's proposal starts from a different question: instead of searching every time, what would happen if the AI built structured knowledge in advance, and then consulted it directly?

Karpathy published on GitHub Gist the description of a three-folder system that allows a model to compile and maintain a knowledge base without vector databases. The architecture is deliberately simple. The first folder, `raw/`, contains raw material: PDFs, notes, web articles, GitHub repositories, datasets. The second, `wiki/`, hosts articles compiled by the model, one per concept or topic. The third is an `index.md` file, an overall map of all articles, sized to fit within the model's context window.

Karpathy uses the Obsidian Web Clipper to convert web content into Markdown files, ensuring that images are also saved locally so the model can reference them through its vision capabilities.

The central step, what differentiates the approach from a simple archive, is compilation. Instead of indexing files, the model "compiles" them: it reads raw data and writes a structured wiki, generating summaries, identifying key concepts, producing encyclopedic-style articles, and, fundamentally, creating backlinks between related ideas.

The system is not static: Karpathy describes periodic "linting" cycles, where the model scans the wiki for inconsistencies, missing data, or new possible connections. The system behaves like a living knowledge base that self-heals. Queries performed on the system are archived in the wiki itself, so every exploration accumulates: answers, graphs, analyses are inserted into the knowledge base, which grows cumulatively.

At what scale does all this work? Karpathy specified that he currently operates with about 100 articles and 400,000 words of source material, and that at this size the model's ability to navigate through summaries and index files is more than sufficient. An analysis conducted by MindStudio found that this approach can reduce token consumption by up to 95% compared to fully loading documents into the context, an advantage that shrinks compared to optimized RAG pipelines.

Karpathy's post fits into a precise sequence of his thinking on human-AI interaction: after the "vibe coding" of February 2025, where the user accepts generated code without reviewing it line by line, and the agentic engineering of January 2026, where [humans orchestrate agents](https://aitalk.it/it/autoresearch-karpathy.html) instead of writing code directly, LLM Knowledge Bases represent the third phase: AI manages knowledge, not just code. The human becomes a curator, not a writer.
![postx.jpg](postx.jpg)
[Screenshot taken from Andrej Karpathy's X profile](https://x.com/karpathy/status/2039805659525644595)

## The advantage of readability

One of the most concrete aspects of the proposal, and often the one that most easily convinces those coming from enterprise RAG experiences, concerns transparency. By treating Markdown files as the source of truth, Karpathy avoids the "black box" problem of embedding vectors. Every statement by the model can be traced back to a specific `.md` file that a human can read, modify, or delete.

This feature has non-trivial practical implications. In a RAG system, when the model returns an incorrect or partial answer, tracing the origin of the problem requires understanding which fragments were retrieved, how they were segmented, and why similarity search favored certain vectors over others. In a well-structured Markdown wiki, the error is visible: there is a poorly written article, a missing backlink, outdated information. It is an editorial problem, not a linear algebra problem.

The architecture is deliberately built on Markdown as an open and tool-independent standard. If Obsidian were to disappear or change license conditions, the knowledge base would remain a directory of plain text files that any editor can open. It is a form of sovereignty over one's own data that enterprise solutions tend not to offer.

Lex Fridman confirmed using a similar system, adding a dynamic visualization layer: it generates HTML with JavaScript to sort and filter data, and builds temporary mini-knowledge bases focused on a specific theme to be loaded in voice mode during his 10-15 kilometer runs. This "ephemeral wiki" foreshadows an interesting direction: you don't chat with an AI, you spawn a team of agents to build a personalized research environment for a specific task, which then dissolves.

There is also a long-term implication that Karpathy mentions only in passing but is worth naming. As the wiki is repeatedly linted (automated review) and refined, it becomes an increasingly clean representation of the domain: de-duplicated (information appears only once), cross-linked, written in a coherent style. At that point, the knowledge base becomes a candidate for training data: instead of continuously prompting a large general model with the wiki, a team could fine-tune a smaller model on that curated corpus, encoding the knowledge base into the model's weights and transforming a personal or departmental archive into private specialized intelligence.

## Where RAG holds its ground

The "RAG is dead" narrative that circulated on social media in the days following Karpathy's post is exactly the kind of simplification that causes damage. RAG is not dead, and there are precise contexts where it remains the right approach, often the only practicable one.

The first limit of Karpathy's proposal is made explicit by Karpathy himself: scale. When the number of articles grows beyond a few hundred, or sources exceed millions of words, the index itself becomes too large to fit in the context window, and retrieval becomes necessary again. The approach is explicitly positioned for personal and small team use, not for corporate-level document archives. A company with millions of documents, heterogeneous legacy systems, stringent compliance requirements, and hundreds of simultaneous users needs something more robust than a directory of Markdown files.

The second limit concerns data freshness. RAG is particularly suitable when sources change frequently and you cannot afford to "recompile" knowledge every time. A customer support assistant that must respond using updated documentation for a constantly evolving product, or a financial analysis system that must incorporate real-time market news, needs dynamic retrieval, not a wiki that is updated periodically.

The third problem, perhaps the most insidious, is what is called "memory drift" in the comments to the GitHub Gist. As the knowledge base grows, how do you handle semantic drift—the phenomenon where the meaning of a term, concept, or statement gradually shifts over time with each rewrite or synthesis, moving away from the original intention without anyone explicitly noticing—and how do you prevent contradictory information from accumulating?

Every time the model rewrites or synthesizes an article, there is a risk: if the synthesis is imprecise, or if two contradictory sources are integrated inconsistently, the error enters the base and propagates. In RAG, a wrong document remains isolated in the corpus and can be corrected or removed. In an AI-compiled wiki, the error may have been reformulated and distributed across multiple linked articles, making correction much more complicated.

Some proposals in the community suggest integrating the system with SQLite, BM25, and TREESEARCH to better manage corpus growth, and several commentators emphasize that humans must remain in the loop to manage the knowledge context prepared by AI and prevent drift and inconsistencies.

Then there is the issue of source provenance. A well-formatted wiki is transparent in structure but not necessarily in the origin of statements. Without a rigorous internal citation system that traces every claim to the original source document, you get readability without verifiability, a distinction that makes a substantial difference in regulated, medical, or legal contexts.

## Hybrid or showdown?

As an analyst wrote in a comment to the Gist, the LLM Wiki is essentially a manual and traceable implementation of Graph RAG: every claim links back to sources, relationships are explicit, and the structure is human-readable. It is a point that clarifies a lot: the two approaches are not philosophical opposites; they are engineering solutions optimized for different contexts, and the boundary between them is more permeable than the online debate suggests.

Some teams are already trying to bridge the gap with multi-agent architectures: a "Swarm Knowledge Base" design scales Karpathy's workflow to a system of 10 agents orchestrated by a control layer, adding supervisor models to protect the shared wiki from compounding hallucinations. A model focused on evaluation, used as a "quality gate," assesses and validates draft pages before they enter the active knowledge base.

The most plausible future is not the victory of one of the two paradigms over the other. It is a layered architecture where a structured and compiled wiki manages stable domain knowledge, updated with periodic human-supervised cycles, while dynamic retrieval intervenes for live sources, fresh data, and corpora that change too quickly to be compiled. Structured memory as a foundation, retrieval as a window to the outside world, human review as quality control that no automatic system can yet completely replace.

In the Gist, Karpathy notes that his token usage has shifted from code generation to structured knowledge management, an apparently marginal note that actually signals a change in priority in the real use of advanced models. Knowledge management is becoming the center of gravity of work with language models, not code generation.

The real question is not whether Karpathy "beats" RAG. It is which architecture maximizes reliability, updatability, and operational value in the specific context in which it operates. For an independent researcher, a small team building internal technical documentation, or a knowledge worker who wants their AI assistant to stop having amnesia every session, Karpathy's proposal is concrete, implementable today, and solves a real problem. For a company with millions of documents, data changing every hour, and stringent governance requirements, RAG in its evolved form, perhaps enriched by elements of Karpathy's proposal, remains the only viable option.

For teams considering whether to adopt this approach or invest in a full RAG pipeline, the honest answer is: start with this, and move to RAG only when the context window becomes a real bottleneck, not a hypothetical problem. You will probably be surprised by how far structured Markdown takes you. It is not the end of RAG. It is the beginning of a more sophisticated conversation on how AI systems manage memory over time, a conversation that until two weeks ago almost no one was having in the right way.
