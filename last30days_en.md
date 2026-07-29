---
tags: ["Applications", "Generative AI", "Ethics & Society"]
date: 2026-07-01
author: "Dario Ferrero"
---

# Last30days: when a code agent becomes a social search engine
![last30days.jpg](last30days.jpg)

*Before writing anything about AI, I opened eleven browser tabs: Reddit, X, YouTube, Hacker News, GitHub, and a few industry newsletters. Two hours later, after three coffees, I had found three truly useful posts. The rest was noise: blog articles optimized for search engines, opinions of people paid to have them, classic galleries of the "ten AI tools that will change your life" type, written with the same depth as an assembly instruction sheet for IKEA furniture.*

The problem is not the quantity of information. It is that the systems we use to navigate it were designed to attack algorithms, not to reflect what people truly think. Google indexes editors. Reddit, X, and YouTube index people. They are fundamentally different ecosystems, each closed in its own walled garden, each with its own APIs, authentication tokens, and access logic.

[`/last30days`](https://github.com/mvanhorn/last30days-skill) is an attempt to break down those fences. It is not a search engine in the traditional sense: it is a skill for code agents that interrogates Reddit, X, YouTube, Hacker News, TikTok, GitHub, Polymarket, and others in parallel, merges the results, and delivers a structured summary in a few minutes. Written by Matthew Van Horn, it reached 41,500 stars on GitHub, ranking as the number one repository of the day in its launch week. The numbers alone don't say much, but they tell the intensity of a real need.

## Inside the machine: architecture v3

Version three of the project, the current one, is built around a simple but powerful idea: don't search for what you wrote; understand *where* to search for it first. The repository's official README describes the flow in seven steps, but the interesting part is what happens before a single API call is even made.

The engine uses a ranking fusion system called Reciprocal Rank Fusion, abbreviated RRF. Instead of entrusting relevance to a single source or a single algorithm, RRF takes results from multiple sources, each with its own ranking, and merges them into a composite ranking that reduces the weight of outliers and rewards consistency across different platforms. If a topic emerges strongly on Reddit, it receives a signal. If the same topic appears on X and is cited in a YouTube video, the signal amplifies. If, instead, it is strong only on one platform and silent on others, it is downscaled.

The other architectural element worth noting is automatic clustering: when the same story appears on Reddit, X, and YouTube with different titles, the engine doesn't show it three times. It detects it as a single cluster via entity-based overlap detection, recognizing the coincidence even when the words used across the different platforms don't match. The result is a brief that consolidates instead of duplicating.

## The brain that reads before searching

The function that the README calls "Intelligent Search" is what most clearly separates this tool from traditional searching. It was built by [Jonas Sperling](https://github.com/j-sperling) and functions as a pre-research brain, a step zero that precedes any query to external APIs.

The idea is this: when you type `/last30days OpenClaw`, the engine doesn't literally search for "OpenClaw" on all platforms. First, it resolves who and what is around that term. It understands that OpenClaw has a creator, Peter Steinberger, who on X is `@steipete`, that the main repository on GitHub is `steipete/openclaw`, and that relevant discussions are found on subreddits like `r/ClaudeCode`. Then it searches for all this in parallel, already oriented. The difference compared to the previous version, Van Horn writes in the README, is structural: "The old engine searched for keywords. The new one understands your topic first, then searches for the right people and communities."

This solves one of the most annoying problems of contextual search: ambiguity. If you search for "Paperclip," do you mean the AI startup or the small metal wire to hold papers together? The engine resolves `@dotta` and understands that you are talking about the former. If you search for "Dave Morin," you get not only his X profile but also the connections with OpenClaw and citations from the TWiST podcast. The disambiguation happens before the search, not after.

## Two judges, not one

One of the most unusual elements of `/last30days` is the presence of a second judge in the synthesis process. The first evaluates relevance: how pertinent a result is to the query, how recent it is, how much engagement it received. The second evaluates something else: humor, wit, virality.

The motivation is practical. Reddit and X produce brilliant summaries daily—perfect jokes, comments that capture the essence of a phenomenon better than any analysis. The old system buried them because they weren't "relevant" in the strict sense of the term. A comment like "My Michael Jordan is Steve Kerr" in a thread about Arizona Basketball scores low on thematic pertinence but extremely high on expressive quality.

The result is a final section called "Best Takes" that collects the most lively quotes, the most shared one-liners, the reactions that invite a return to the subject. It is not a decorative function: it is a recognition that digital culture often moves through the right joke at the right time, not through the most accurate analysis.

## Comparisons in parallel, not in series

Another function introduced in v3 deserves attention because it solves a practical problem that anyone who has tried to compare two competing tools knows well. In previous versions, a query like `/last30days "OpenClaw vs Hermes vs Paperclip"` executed three serial searches: first one, then the other, then the last. The execution time could exceed twelve minutes. v3, on the other hand, performs a single pass with entity-aware subqueries for all subjects simultaneously, bringing the time to about three minutes with the same depth of analysis.

There is also the `--competitors` mode, which works even more autonomously: given a subject, the engine discovers the main competitors on its own via web search, then starts parallel pipelines for each and merges them into a structured comparison. It's the kind of function that transforms a search tool into something resembling a junior analyst: it doesn't limit itself to answering the question you asked but builds the context in which that answer makes sense.

## Fifteen platforms, one brief

The table of supported sources in the [repository](https://github.com/mvanhorn/last30days-skill) is long: Reddit, X, YouTube, TikTok, Instagram Reels, Hacker News, Polymarket, GitHub, Digg, Threads, Pinterest, Bluesky, Perplexity, traditional web search. Some are free and work without configuration (Reddit with comments, HN, Polymarket, GitHub). Others require authentication or paid API keys.

The presence of Polymarket is particularly interesting: it doesn't collect opinions; it collects odds. The probabilities on Polymarket are determined by those who put real money on the prediction, not by those who want to seem informed. There is a significant epistemic difference between "many think X will happen" and "74% of capital bets that X will happen by December." The engine shows it as a separate signal, with probability percentages, not dollar volumes, because the magic is in the odds, not the amount.

For GitHub, there is also a so-called "person-mode": when the query concerns a specific person, the engine stops searching for who is talking about them and starts searching for what that person is actually building. The command `/last30days Peter Steinberger --github-user=steipete` returns not a press review on Steinberger but a map of his work: how many pull requests he made in the last month, in which repositories, at what approval rate, and what he released.
![tabella1.jpg](tabella1.jpg)
[The platforms where searches occur](https://github.com/mvanhorn/last30days-skill)

## Opencode: a field test

When I saw the project, the immediate question was: does it also work outside the Claude Code ecosystem? The repository's answer is affirmative: the skill is installable on Codex, Cursor, Copilot, Gemini CLI, and via the open package `npx skills add mvanhorn/last30days-skill -g` on over fifty environments compatible with the Agent Skills standard, including `opencode`.

I installed the skill on opencode and did a concrete search: user preferences on opencode about which free or low-cost language model offered the best quality-performance ratio. A niche query, with a small but active community, that a traditional search engine would have satisfied with zero useful results.

The produced report crossed providers, forums, GitHub discussions, and official documentation. It distilled that opencode supports over 75 providers and three main modes of model access. Among the free ones available immediately, without API keys: DeepSeek V4 Flash Free, a mixture-of-experts model with 284 billion parameters and one million tokens of context, distributed under the MIT license. For those wishing to spend ten dollars a month with OpenCode Go, the model with the best request/quality ratio was still DeepSeek V4 Flash, with about 158,000 estimated monthly requests, while for absolute quality, GLM-5.2 and Kimi K2.7 Code emerged, the latter particularly recommended for complex MCP agents. For those who do not want to depend on the cloud, local models via Ollama or LM Studio were documented in detail, with Qwen3.6-27B as the choice for a single 24GB GPU.

The report came out as an `.md` file upon explicit request, citing sources. It took about a minute. It wasn't perfect: some price information would require direct verification on provider sites, and the opencode community is small enough to make the sample statistically thin. But for quickly orienting oneself in a landscape that changes every week, it was exactly what was needed.

## The limits no one tells you

Honesty requires putting on the table also what doesn't work, or what works with hidden costs.

The first limit is structural: the richest sources—TikTok, Instagram, Threads, YouTube with comments—require an API key from ScrapeCreators, a paid service. The first hundred requests are free, then it enters a pay-per-use model. Anyone wanting the full version of the tool must account for a variable cost that depends on the intensity of use. The "free" model exists, but it is significantly more limited than the one described in the README use cases.

The second limit is epistemic and more subtle. The tool optimizes for engagement: a Reddit thread with 1,500 upvotes weighs more than a blog post that no one read. In principle, it makes sense. In practice, engagement is a measure of emotional reactivity as much as of informational quality. A post that simplifies, outrages, or amuses collects more upvotes than a nuanced analysis. `/last30days` doesn't solve this problem: it inherits it from the platforms it interrogates. The synthesis is as good as the conversations it finds, and online conversations have their structural biases.

The third limit concerns data latency: the tool looks for what happened *in the last few weeks*, not what happened yesterday morning. For trend analysis and context searching, it works very well. For breaking news in real time, less so.

Finally, a note on privacy. The README explicitly states that the search remains local; no data is transmitted to third-party servers outside the APIs that the user configures themselves. It is an MIT project, verifiable in the source code. But anyone using `/last30days` with an X or ScrapeCreators key is still authorizing those platforms to receive the queries: confidentiality is therefore relative; it depends on which sources are enabled.

## Who wins, who loses, who decides

From the users' point of view, `/last30days` responds to a need that existing tools systematically ignore: aggregating heterogeneous social signals without spending hours doing it manually. It is particularly useful in three contexts: before a meeting with someone whose recent work you want to understand, when you need to evaluate a new tool in a fast-moving sector, and when trying to understand if a trend is real or amplified by the usual ten influential profiles.

For the category of professional researchers and journalists, the issue is more complex. The tool accelerates collection but doesn't replace judgment. The "Best Takes" can be valuable for understanding how a community reacts, but selecting the most viral jokes is not the same as identifying the most informed voices. Optimizing for engagement and optimizing for truth are different functions, and sometimes orthogonal.

The platforms being interrogated gain nothing from this scheme: `/last30days` uses their APIs or public data without returning direct traffic. It's a dynamic already seen with traditional search engines, but amplified: here there is not even a click-through on a link. Reddit has already undertaken legal battles against those who use its data in unauthorized ways, and it's not impossible that access conditions will change in the future.

The project, with its 41,500 stars and 3,400 forks, is already large enough to attract attention. The question is not whether it works: it works, with the described limitations. The question is where this paradigm leads when it is generalized. An agent that interrogates all public conversations on a topic in parallel, merges them, synthesizes them, and delivers a response in a minute is a powerful tool. Like any powerful tool, it says much more about who uses it than about itself.
