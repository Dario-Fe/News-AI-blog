---
tags: ["Applications", "Generative AI", "Research"]
date: 2026-07-03
author: "Dario Ferrero"
---

# Headroom: the token compressor that doesn't use AI to compress AI
![headroom.jpg](headroom.jpg)

*There is a silent paradox at the heart of many modern artificial intelligence systems. Engineers build sophisticated agents capable of reasoning, planning, and coordinating complex sequences of actions. Then they look at the monthly API bill and realize that the biggest expense is not reasoning, not creativity, not even accuracy. It is traffic. The sheer, banal volume of text that components exchange with each other.*

Tejas Chopra, a Netflix engineer, found himself in exactly that situation. His AI agent was burning two hundred dollars a day not for doing extraordinary things, but simply for carrying context: tool outputs, system logs, debug files. Instrumental data, often redundant, which occupied precious context windows and were billed token by token. His response is [Headroom](https://github.com/headroomlabs-ai/headroom), an open-source project that in a few months has collected over 45,000 stars on GitHub and proposes a solution as simple in premise as it is interesting in details: compress what goes into the LLM before it actually gets there.

The premise is that modern AI agents suffer from a structural problem. At each step of their work cycle, they read files, query databases, execute shell commands, and receive responses from external APIs. All this material flows into the context that is sent to the model, and the model pays for every token. A thousand-line system log, even if it contains only one critical line, costs like a thousand lines. A JSON array of five hundred search results, even if twenty would be enough to answer the question, weighs like five hundred results.

The solution market has responded predictably: hosted services that compress text by sending it in turn to another LLM, which produces a summarized version to send to the main model. The elegance of this solution is inversely proportional to its economic effectiveness, because it introduces an additional cost in an attempt to reduce one. Headroom makes a radically different choice.

## The trick: algorithms, not models

The design decision that distinguishes Headroom from most competitors is so counter-intuitive that it deserves to be highlighted: to compress the context of LLMs, Headroom does not use any LLM. It uses deterministic algorithms. Classic software that reads the structure of data and reduces it following precise rules, without ambiguity, without variance, without the cost of additional inference.

This approach has important consequences in three dimensions: speed, predictability, and cost. Compressing a 500-element JSON array requires about 940 milliseconds on CPU; the same operation with a language model would require seconds, with a non-negligible cost. Algorithmic compression always produces the same output for the same input, making it testable, auditable, and predictable in production. And it doesn't add a dependency on an external provider at the very moment you are trying to reduce the API budget.

The heart of the architecture is the **ContentRouter**, which analyzes the incoming content and sorts it to the appropriate compressor. It is not a coarse classification: the router recognizes structured JSON, string arrays, numerical arrays, system logs, source code, prose text, images. Each corresponds to a different strategy.

The **SmartCrusher** handles JSON, which represents the most frequent category in agent outputs. Its logic is not simply "keep the first N elements": it uses the Kneedle algorithm to find the point on the bigram coverage curve where adding further elements stops bringing new information. Then it divides the budget así obtained: thirty percent from the first elements of the array (to capture the schema), fifteen percent from the last (recency bias), fifty-five percent from elements that importance scoring identifies as anomalies. Errors, exceptions, statistical outliers are always preserved, even if they exceed the overall budget. It is a design choice that reveals a clear understanding of the context of use: in an agent that does debugging, losing the only line with "FATAL" would be catastrophic.

The **CodeCompressor** is technically the most sophisticated, and also the most conservative in its actual behavior. It uses tree-sitter to build the Abstract Syntax Tree of the source code and could theoretically reduce it by eliminating implementation details not necessary for structural understanding. In practice, in the default configuration, source code almost always passes through without modifications. The reasons are honestly documented: short messages are skipped, code in the last four conversations is always protected, and if the user used words like "analyze", "explain", or "fix" in the most recent message, all code in the session is considered untouchable. It is a conservative approach that reflects a clear priority: better to waste a few tokens than risk breaking the model's reasoning.

**Kompress-base** is the only component that introduces a machine learning model, but it is a local model that runs on the user's hardware and does not require external calls. Trained on agentic traces, it handles prose text (documentation, unstructured logs) and produces reductions in the range of forty-five percent. It is available on HuggingFace as [kompress-v2-base](https://huggingface.co/chopratejas/kompress-v2-base).

## Six compressors, one goal

The galaxy of components that makes up Headroom converges on a single fundamental guarantee: compression is always reversible. This is the heart of the CCR system, an acronym for Compress-Cache-Retrieve, which solves the thorniest problem of aggressive compression: what happens if the model needs the original data?

Headroom's response is pragmatic and well-conceived. When content is compressed, the original is kept in a local cache (with a configurable TTL, one hour by default). The compressed content includes a marker that the model can see, like "1000 elements compressed to 20. Retrieve with hash=abc123". Simultaneously, Headroom injects into the available tools schema a tool called `headroom_retrieve`, which the model can invoke autonomously if it considers the twenty elements received insufficient.

The architecture is elegant because it shifts the decision to those who have the most information to make it. The model, which knows its own reasoning and needs, independently decides whether the compressed data is enough or if it's worth retrieving the original. Retrieval is local, with latency in the millisecond range. The model can also perform semantic searches within the cache using BM25, receiving a relevant subset instead of the entire payload.

In practice, this feature is more of a safety net than a frequently activated mechanism: if the compression works well, the model rarely needs to retrieve the original. But knowing that the safety net exists is enough to use Headroom in contexts where information loss would be unacceptable.

The other components complete the picture. The **CacheAligner** stabilizes message prefixes to maximize cache hits on provider KV caches, particularly Anthropic and OpenAI, with additional savings that add to content compression. **IntelligentContext** manages the conversational window over very long sessions, eliminating low-relevance messages (also cached via CCR). The **headroom learn** function analyzes failed sessions and writes corrections into agent configuration files like `CLAUDE.md` or `AGENTS.md`, transforming past errors into future instructions.

Integration with existing stacks occurs in three distinct ways. As a Python or TypeScript library, with a single `compress(messages)` call before sending to the provider. As a local proxy (`headroom proxy --port 8787`), which intercepts requests directed to the API without modifying the application code. As an MCP server, compatible with Claude Code, Cursor, Codex, and any MCP client. There is also `headroom wrap`, a command that directly wraps command-line agents. Declared support covers LangChain, LiteLLM, Vercel AI SDK, Agno, and Strands.
![tabella1.jpg](tabella1.jpg)
[Headroom process diagram from github.com](https://github.com/headroomlabs-ai/headroom)

## The numbers: real or marketing?

The numbers Headroom presents deserve careful reading, because they mix convincing results with some points that require contextualization.

Workload-based benchmarks are the most significant. A code search with a hundred results goes from 17,765 to 1,408 tokens, a ninety-two percent saving. An SRE debug session from 65,694 to 5,118 tokens, same order of magnitude. GitHub issue triage from 54,174 to 14,761, seventy-three percent. These are plausible scenarios for an agent that uses tools intensively, and internal numbers from the compression pipeline show millisecond latencies for most operations.

Accuracy benchmarks are reassuring but require a methodological note. On GSM8K (elementary math) and SQuAD v2 (extractive question answering), the results with and without Headroom are practically identical or slightly better with compression, because removing noise sometimes helps the model focus. But these are standard benchmarks, measured on generic content. There are no equivalent tests, at least in public documentation, on domains where terminological precision is critical: legal texts, medical technical sheets, financial contracts. The documentation of limits is honest on this point: Headroom is optimal for sessions with many tool calls, not for short or conversational texts, where the median compression detected across 50,000 real sessions is just 4.8%.

It is worth dwelling on this last datum, because it scales back some expectations. The 4.8% median means that half of real sessions benefit very little from Headroom, because they are short conversations, single questions, exchanges without context accumulation. The tool's value emerges in heavy workloads, those with accumulation of tool outputs, logs, files: there compression rises to forty-eighty percent. It is a tool for specific use cases, not a universal magic wand, and the documentation says so explicitly in the limitations section.

Aggregated telemetry data is presented with methodological transparency: 50,000 proxy sessions, 250 unique instances between March and April 2026, 1.4 billion tokens saved, about 4,000 dollars of total saving on the monitored fleet. These numbers allow some calculations: 4,000 dollars across 250 instances in two months means about 8 dollars per month per instance. It is a real saving, but modest for most users, which returns to the previous point about workload heterogeneity.

The additional latency introduced by the proxy is 52 milliseconds median, negligible compared to the 2-10 seconds typical of an LLM inference. The P99 is 4 seconds, which could be problematic for applications particularly sensitive to latency. In real-time or high-frequency streaming scenarios, overhead must be evaluated on a case-by-case basis.

## Who wins, who loses, what remains open

Headroom is a young project, born in public three months ago and grown rapidly. The speed of development, 157 releases in as many days, reflects a very aggressive iteration cycle. The Apache 2.0 license is more permissive than MIT in commercial contexts, allowing use in proprietary products with fewer constraints. The codebase is written predominantly in Python (79%) with a critical layer in Rust (17%) for low-latency operations.

The project's point of concentration is its primary author, Tejas Chopra. There are more than thirty contributors, and the Discord community is active, but the architectural vision and key decisions still pass through a single person. It is not unusual for a project in its phase, but it is a factor to consider for those evaluating long-term production adoption. A security whitepaper does not yet exist, nor do compliance certifications (GDPR, SOC2, HIPAA). Security documentation exists—the SECURITY.md in the repository describes vulnerability management—but it doesn't cover aspects like the local cache isolation model or the management of credentials and PII that may pass through compressed logs.

For those building AI agents with intensive tool use, Headroom represents a concrete and well-documented option with a clear and measurable value proposition. The choice to not use an LLM for compression is not just a technical distinction: it is a guarantee of deterministic behavior, absence of drift, and predictable compression costs. The CCR system elegantly solves the problem of lossy compression with a retrieve-on-demand architecture that preserves information integrity.

For those who use LLMs primarily for conversation, writing, or textual analysis without tool-based context accumulation, the impact will be marginal and the adoption overhead is probably not worth the investment. The tool is explicit about this in its own documented limits, which is a sign of project maturity that is not a given.

The most interesting open question is not technical: it is whether the problem Headroom solves will become less relevant as providers evolve. OpenAI and Anthropic are working on increasingly large context windows and native compression and caching mechanisms. If the cost per token drops significantly, or if providers offer compression-as-a-service at competitive prices, Headroom's niche shrinks. For now, in this moment of still high prices and still limited contexts, the project responds to a real need with solid tools.

The [repository](https://github.com/headroomlabs-ai/headroom) is public, documentation is well-structured, and benchmarks are reproducible with `python -m headroom.evals suite --tier 1`. For those who want to evaluate it on their specific workload, the quickest starting point is `headroom perf`, a command that analyzes existing sessions and estimates potential savings before touching any production configuration.
