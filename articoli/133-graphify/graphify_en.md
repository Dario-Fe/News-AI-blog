---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-06-01
author: "Dario Ferrero"
---

# Graphify and the Memory LLMs Don't Have
![graphify.jpg](graphify.jpg)

*What if your AI assistant could stop re-reading the entire project every time to answer a single question? Graphify, an open-source tool published on GitHub with over 50,000 stars, promises exactly that: to transform a folder of code, documents, PDFs, images, and videos into a knowledge graph queryable by AI agents, drastically reducing the number of tokens consumed for every query.*

Anyone working daily with AI agents on medium-sized projects knows a specific frustration well: every time an assistant like Claude Code, Cursor, or Gemini CLI has to answer a question about the project, it traverses the entire codebase as if it had never read anything. It re-reads files, re-analyzes structures, and starts from scratch. It's a bit like Detective Lunge from Naoki Urasawa's *Monster*, who, to remember something, must reconstruct the entire deductive chain from the first clue every time, unable to maintain an intermediate state between sessions.

In April, on these same pages, we analyzed in detail [Andrej Karpathy's proposal for an evolutionary knowledge base for LLMs](https://aitalk.it/it/llm-knowledge-base.html): building a structured wiki in Markdown that the model could compile and query, avoiding reloading the entire corpus into the context every time. The proposal garnered over 16 million views on X, triggering a heated technical debate on which memory architecture was truly viable for professional use.

Graphify starts from exactly that intuition, explicitly citing Karpathy's approach in the README as a starting point, only to push it further: instead of a flat wiki in Markdown, it builds a knowledge graph where every entity, every function, and every concept extracted from your files becomes a node, and the relations between entities become navigable edges. The difference is not aesthetic; it's structural.

## What Is a Graph (And Why It Changes Everything Here)

A graph, in its simplest form, is a collection of points connected by lines. The points are called nodes, and the lines are called edges. It's the same structure that Google Maps uses to represent city streets, or that social networks employ to model relationships between users. This isn't a metaphor: it's a data structure with mathematical properties that make it particularly suited for representing complex relationships.

Why is a graph more useful than a Markdown document for a software project? The answer lies in the nature of relationships. In text, even well-structured text, the connections between concepts are implicit: you have to read, understand the context, and infer the links. In a graph, relationships are explicit, typed, and traversable. You can ask "what is the shortest path between the authentication module and the database?" and get an answer by navigating the edges, not by analyzing text.

For an AI agent that has to answer about a project, this difference is substantial. Instead of loading dozens of files into the context hoping the model finds the relevant connections, the agent navigates the graph, retrieves only the pertinent nodes and their direct neighbors, and builds the answer with a fraction of the tokens. It's the difference between asking someone to read an entire encyclopedia to answer a question or giving them a semantic index to navigate directly to the right entry.

## Three Passes to Understand Everything

Graphify's internal pipeline, documented in detail in the [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) file of the repository, is divided into three phases designed to maximize local processing and minimize external API calls.

The first pass concerns the source code and is entirely local: no APIs, no tokens consumed. Tree-sitter, the AST parser also used by editors like Neovim and Helix for real-time syntax highlighting, analyzes code files and extracts classes, functions, imports, call graphs, and inline comments. The result is deterministic: the same file always produces the same output. SQL files receive special treatment, with tables, views, foreign keys, and JOIN relationships extracted with the same deterministic logic. At the time of release, Graphify declares support for 29 programming languages.

The second pass covers audio and video files, also local. Faster-whisper, an optimized implementation of OpenAI's Whisper model that runs entirely locally, transcribes multimedia content. There is a refined technical detail: the transcription is "guided" by the most connected nodes of the graph built in the first pass, the so-called "god nodes," the concepts that appear most frequently in the relationships extracted from the code. This causes the transcription model to pay closer attention to project-specific domain terms. Transcripts are cached: subsequent runs skip already processed files.

The third pass, the one that consumes API tokens, handles documents, PDFs, and images. Here, the user-configured language model comes into play: Claude, Gemini, OpenAI, or alternatively a local instance of Ollama, or AWS Bedrock via the IAM credential chain. Files are processed in parallel by multiple sub-agents, each returning a structured JSON fragment with nodes, edges, and group relationships. The fragments are then merged into a single coherent graph.

Community clustering occurs with the Leiden algorithm, a method published in 2019 in *Nature Scientific Reports* that groups nodes by connection density without requiring separate vector embeddings. Semantic relationships extracted by the language model, for example `semantically_similar_to` between two related concepts, are already in the graph as edges and directly influence the shape of the detected communities. There is no separate vector database: the graph structure is the similarity signal.

Every relationship is marked with one of three confidence tags: `EXTRACTED` for relationships found directly in the source code, `INFERRED` for model inferences with a score from 0.55 to 0.95 according to a documented discrete scale, and `AMBIGUOUS` for uncertain cases flagged in the final report for manual review. You always know whether the graph is telling you something certain or hypothetical.
![graphify-query1.jpg](graphify-query1.jpg)
*Screenshot of my test on data (MTV paradox request) in opencode*

## The Entire Project in 7 Megabytes

I installed Graphify via OpenCode and ran it on the entire AiTalk project: code, articles, images, audio files, the entire base of work accumulated over time. The source material weighed about 970 MB. The generated output, the `graphify-out/` folder with its three main files, occupied just over 7 MB.

Three files: `graph.html`, the interactive visualization navigable in any browser; `GRAPH_REPORT.md`, the textual report with key concepts, most significant connections, and suggested questions; and `graph.json`, the complete graph in NetworkX node-link format, directly queryable.

From that moment, any question asked of OpenCode about the project's technical structure, code logic, article content, and thematic connections between them received excellent answers. Not generic, but contextualized: the agent knew which components depend on which, which topic is covered in multiple articles with different angles, where there were non-explicit connections between apparently distant content. The model navigated the graph instead of re-reading source files every time. Where before a complex query required loading dozens of files into the context, now the agent starts from the report and navigates the JSON to find only what is needed.
![grafo-aitalkjpg.jpg](grafo-aitalkjpg.jpg)
*Screenshot of the html page with the dynamic and navigable representation of the AiTalk.it project graph*

## Honest Numbers: 71x, But It Depends

The repository publishes an explicit benchmark in the [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) file, and it is worth reading carefully because the numbers are presented with an honesty unusual for a project in the promotional phase.

On a mixed corpus of 52 files composed of Karpathy's repositories, five academic papers, and four images, Graphify claims a 71.5x reduction in tokens for each query compared to directly reading the raw files. On a smaller corpus, four files between source code and papers, the reduction drops to 5.4x. On six files, about 1x: no significant advantage in terms of tokens, if anything structural clarity.

The pattern is clear and explicitly explained: compression scales with corpus size. Six files already fit into a single context window. At 52 files, savings compound quickly. Each `worked/` folder in the repository contains original input files and actual output, so anyone can replicate the benchmark independently.

It should be clarified, however, what these numbers do not include: the cost of initial extraction, the moment Graphify consumes API tokens to analyze documents, PDFs, and images. This cost is amortized over subsequent queries thanks to the SHA256 cache that skips unmodified files, but it is a real cost that in a large corpus can be significant, especially with premium models. The benchmark measures savings in a steady state, not the setup cost. The documentation says so clearly.

## Integrate or Get Lost

One of the most carefully designed aspects of the project is compatibility with the developer tool ecosystem. Currently, Graphify supports direct installation on Claude Code, OpenCode, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, and other less widespread tools.

The integration mechanism is simple. Once the graph is built, the command `graphify claude install` (or the corresponding one for the chosen platform) writes a configuration file that instructs the assistant to read `GRAPH_REPORT.md` before answering. On platforms that support hooks, such as Claude Code, Codex, and Gemini CLI, a hook activates automatically before every file read: the assistant navigates the graph instead of scanning the directory.

For teams, the recommended workflow is to commit the `graphify-out/` folder to the Git repository. Every member who pulls finds the graph already updated. The `graphify hook install` command adds a post-commit hook that automatically reconstructs the AST part after each commit, at zero cost in terms of APIs, with a Git merge driver that handles conflicts on `graph.json` by merging the two graphs instead of leaving unresolvable markers.

The package is called `graphifyy` on PyPI (double y), requires Python 3.10+, and installs with `uv tool install graphifyy`, `pipx install graphifyy`, or `pip install graphifyy`. The CLI command remains `graphify`.
![graphify-query2.jpg](graphify-query2.jpg)
*Screenshot of my test on the code (site generation method request) in opencode*

## Privacy: What Stays at Home

Privacy management follows an explicit logic. Source code is processed entirely locally via tree-sitter, without any calls to external services. Audio and video files are transcribed locally with faster-whisper. Not a single byte of code or multimedia content leaves the user's machine.

The situation changes for documents, PDFs, and images: these are sent to the configured language model via its API. If Claude is used, files are sent to Anthropic. If Ollama is used, they stay local. For contexts with sensitive data, Graphify offers two options: a local Ollama instance or AWS Bedrock via IAM, without explicit API keys. The project states it has no telemetry, usage tracking, or data analysis.

An aspect to consider for teams on proprietary code: even if the code remains local, architectural documents, specification PDFs, and mockup images are processed by the configured external model. In the presence of contractual confidentiality obligations, this distinction should be evaluated carefully before adoption.

## Limits Without Discounts

It would be dishonest to stick only to praise. There are aspects that deserve critical evaluation.

The first concerns the quality of inferred relationships. Relationships labeled `INFERRED` depend on the quality of the model used. A smaller model or one configured with a reduced token budget may produce speculative relationships with optimistic confidence scores. The scale from 0.55 to 0.95 is calibrated to the developer's test corpora, not necessarily the type of project the tool is applied to.

The second limit concerns updates. The SHA256 cache skips unmodified files, but what happens when you move a function from one module to another or refactor a class significantly? The graph may have orphaned nodes or relationships pointing to entities that no longer exist. The `--update` command handles modified files, but for deep refactoring, a complete reconstruction is likely necessary, with the associated token cost.

The third critical aspect is scale. As with Karpathy's wiki approach, the graph also has a breaking point. For very large corpora, the documentation suggests using direct queries on `graph.json` or exposing the graph as an MCP server with `python -m graphify.serve`, which offers structured tools like `query_graph`, `get_node`, `get_neighbors`, and `shortest_path`. The solution is refined but adds a layer of configuration that not all workflows can easily absorb.

Finally, it should be noted that the project is essentially maintained by a single developer, Safi Shamsi. The repository shows intense activity, with 97 releases at the time of writing and the last stable version v0.7.16 released on May 12, 2026, but the long-term sustainability of a project with this visibility and this dependence on a single maintainer is a variable not to be ignored for those planning an adoption in critical environments.

## The Future of Memory

Graphify solves a concrete problem. But the most interesting question it raises doesn't concern token savings: it concerns the nature of memory in AI agents.

Today, an agent has no persistent memory. Every session is a clean slate, every project rediscovered from scratch. Graphify and similar projects are attempts to build an external layer of structured memory that survives sessions, that accumulates over time, that represents not just raw data but the relationships between them.

Many open questions remain. How do you maintain the coherence of a graph in a rapidly evolving project? Who is responsible for the quality of inferred relationships when an agent makes decisions based on them? And the most subtle: if the agent navigates a graph instead of reasoning on files, the quality of initial extraction becomes the real bottleneck, not controllable with a temperature parameter but with the quality of the ingest pipeline.

From the Graphify Labs site, a more ambitious vision emerges: Penpax, the commercial product announced in a trial version soon, promises to apply the same logic to a person's entire daily work—meetings, emails, files, and code—updating in the background, without cloud, completely on-device. A digital "second brain" built on serious technical foundations instead of motivational metaphors.

Graphify in its open-source form is already a significant starting point. It's not the ultimate solution to the problem of LLM memory, but it's a precise indicator of the direction being sought: not inside the model, not in the context, but in a structured and persistent representation that lives outside of both.

---

*Graphify is available on [GitHub](https://github.com/safishamsi/graphify) under the MIT license. The PyPI package is called [graphifyy](https://pypi.org/project/graphifyy/) (double y). The project site is [graphifylabs.ai](https://graphifylabs.ai). Technical documentation on the extraction pipeline is in [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md).*
