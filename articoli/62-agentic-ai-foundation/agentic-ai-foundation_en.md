---
tags: ["Business", "Ethics & Society", "Generative AI"]
date: 2025-12-17
author: "Dario Ferrero"
---

# The Agent Cartel: When Open Source Becomes a Preemptive Monopoly
![agentic-ai-foundation.jpg](agentic-ai-foundation.jpg)

*On December 9, 2025, the Linux Foundation announced the formation of the [Agentic AI Foundation](https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/), an initiative that brings together OpenAI, Anthropic, and Block under the aegis of what is supposed to be neutral governance. The three giants have donated their most strategic projects: Anthropic's Model Context Protocol, Block's Goose framework, and OpenAI's AGENTS.md. The initiative is accompanied by platinum sponsors like AWS, Google, Microsoft, Bloomberg, and Cloudflare. A coalition so broad it seems almost suspicious.*

The official press release talks about "transparency," "collaboration," and "public interest." These are all reassuring terms that hide an uncomfortable question: why now? And more importantly, why this rush to define standards for a technology that regulators are still trying to understand?

## The Genealogy of the Autonomous Agent

To understand what's at stake, we need to take a step back. AI agents are not a theoretical novelty: as early as 2023, experimental projects like Auto-GPT showed that language models could be orchestrated to perform complex tasks autonomously. But there's a chasm between a GitHub experiment and an enterprise product, made of reliability, security, and above all, interoperability.

[The Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), launched by Anthropic in November 2024, is the first serious attempt to standardize how AI agents communicate with external systems. As David Soria Parra, co-creator of MCP, explained to [TechCrunch](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/): "The main goal is to have enough adoption in the world for it to become the de facto standard." Adoption has been rapid: according to [GitHub data](https://github.blog/open-source/maintainers/mcp-joins-the-linux-foundation-what-this-means-for-developers-building-the-next-era-of-ai-tools-and-agents/), thousands of MCP servers were created in just a few months, with SDKs available for all major programming languages and [over 97 million monthly downloads](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) combined for the Python and TypeScript libraries.

[Block's Goose](https://block.github.io/goose/), released in early 2025, adopts a local-first philosophy that appeals to privacy paranoids. As an agent framework that combines language models with extensible tools and MCP-based integrations, Goose allows developers to maintain control over what is sent where. An approach that Manik Surtani, Head of Open Source at Block, summarized at the [AAIF launch](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation): "The technology that will define the next decade can either remain closed and proprietary for the benefit of a few, or be driven by open standards for all."

[OpenAI's AGENTS.md](https://agents.md/), launched in August 2025, is perhaps the simplest but also the most insidious project. It's a Markdown file that agents can read to understand how to operate in a repository: code conventions, build steps, testing requirements. [According to OpenAI](https://openai.com/index/agentic-ai-foundation/), over 60,000 open source projects have already adopted it, including tools like Cursor, Devin, GitHub Copilot, and VS Code. An impressive number for a standard born just four months ago.

## Who Writes the Protocol, Writes the Law

And this is where the official narrative begins to crack. Why does this coordinated convergence towards common standards happen at a very specific moment: when regulators have not yet legally defined what autonomous AI agents are.

The [EU AI Act](https://artificialintelligenceact.eu/), which came into force in August 2024, was designed before agents became mainstream. As a [report by The Future Society](https://thefuturesociety.org/aiagentsintheeu/) from June 2025 notes, "although the AI Act was not originally designed with AI agents in mind, we find that the world's most comprehensive regulatory framework for governing AI does in fact apply to agents. But gaps remain." The central problem is that the Act categorizes AI systems based on static risk, whereas agents operate dynamically, adapting and making autonomous decisions that can vary the level of risk depending on the context.

An [article on the European Law Blog](https://www.europeanlawblog.eu/pub/dq249o3c/release/1) describes what it calls "Agentic Tool Sovereignty": the impossibility for states and providers to maintain legal control over how AI systems autonomously invoke and use cross-border tools. Imagine a recruiting system in Paris that in five seconds invokes a US psychometric API, a UK verification service, a Singaporean skills platform, and a Swiss salary tool. Three months later, four regulators issue fines. Who is responsible? The deployer had no visibility into the data flows, the audit trails were insufficient, the agent had no geographic routing controls.

In September 2025, MEP Sergey Lagodinsky formally asked the Commission to clarify "how AI agents will be regulated." As of this writing, no public response has been issued. This regulatory vacuum is the perfect playground for those who want to write the rules before the referees arrive.
![annuncio.jpg](annuncio.jpg)
[Image from the Agentic AI Foundation website](https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/)

## Anatomy of a Strategic Alliance

The three founding projects of AAIF are not chosen at random: they represent the critical layers of the agent infrastructure. MCP defines how agents talk to the outside world. AGENTS.md standardizes how agents understand work contexts. Goose demonstrates how these pieces assemble into a working framework. Together, they cover the entire technology stack.

The donation to the Linux Foundation sounds noble, but it raises questions about real governance. The Linux Foundation has a controversial history with corporate influence. As reported by [The New Stack](https://thenewstack.io/linux-foundation-critics/) back in 2021, the foundation removed the ability for community members to be elected to the board from its bylaws, leaving control exclusively to corporate sponsors. Matthew Garrett, a Linux kernel contributor, [denounced](https://techrights.org/o/2016/01/21/linux-foundation-coup/) this change as an abandonment of community representation.

Jim Zemlin, Executive Director of the Linux Foundation, [stated](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) that "an early indicator of success, beyond the adoption of these standards, would be the development and implementation of shared standards used by vendor agents worldwide." But who decides which standards should be implemented? The platinum members who pay hundreds of thousands of dollars a year, or the community that develops the tools?

Nick Cooper of OpenAI told [TechCrunch](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/) that "I don't want it to be a stagnant thing. I don't want these protocols to be part of this foundation and just sit there for two years. They should evolve and continuously accept further input." Nice words, but the history of open source software teaches that whoever controls the maintainers and finances the development determines the project's direction.

## What's at Stake

The economic implications are enormous. Analysts predict that the market for autonomous AI agents will reach tens of billions of dollars in the coming years, with applications ranging from email management to complex web browsing. Whoever controls the standards controls the tolls: what company will want to invest in a proprietary agent system when the ecosystem consolidates around MCP, AGENTS.md, and the like?

Microsoft and GitHub [announced](https://www.tekedia.com/microsoft-and-github-join-forces-with-anthropic-to-expand-ai-ecosystem-via-model-context-protocol/) in May 2025 that they were joining the MCP steering committee, bringing with them access to the Windows file system, windowing capabilities, and the Windows Subsystem for Linux through MCP servers. GitHub is developing a registry service for MCP. When tech giants align their infrastructures around a protocol, it becomes the de facto standard, regardless of how "open" it is on paper.

As a [critical analysis on Implicator](https://www.implicator.ai/the-agentic-ai-foundation-is-a-trade-bloc-disguised-as-open-governance/) notes, AAIF looks more like a trade bloc disguised as open governance. Paid memberships create a hierarchy where those who pay more have more say. The platinum members include exactly the companies that have the most to gain from the consolidation of the agent market under standards they themselves helped create.

## The Inversion of the Standardization Process

There's a detail that escapes the official narrative, but that anyone who lived through the Nineties immediately recognizes: the process is inverted. When the Internet was born, standards came first. The Requests for Comments (RFCs) were rigorous, publicly discussed documents that defined protocols like TCP/IP, HTTP, SMTP before a market existed. Downstream, companies implemented those standards. It was a bottom-up process where engineers and academics defined the architecture and the market followed.

With AAIF, we are witnessing the opposite: first, companies build proprietary protocols (MCP was born inside Anthropic, AGENTS.md inside OpenAI, Goose inside Block), then they see they have traction, and finally, they coalesce into an "open" foundation to crystallize their first-mover advantage. They are not creating neutral standards from scratch; they are legitimizing protocols already deployed on millions of systems. It is post-facto standardization, where adoption precedes governance.

But there is a second, even more disturbing aspect: geography. All the founders of AAIF are American. The Linux Foundation is based in San Francisco. The platinum sponsors are all Western, with a predominance of the USA. Yet China is investing massively in agentic AI: according to a [2025 McKinsey report](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), Chinese companies account for 15% of global AI investments and are developing their own frameworks for autonomous agents. Alibaba, Baidu, Tencent all have internal projects on agents. Why are none of them in AAIF?

One possible interpretation is that AAIF is not really a global initiative, but a Western bloc attempting to establish standards before Chinese players can propose alternatives. It is the same dynamic seen with 5G, where the USA and Europe pushed to exclude Huawei from critical networks. The difference is that here we are not talking about physical infrastructure but software protocols, which are much harder to control once they are open source. If tomorrow Alibaba were to release an agent protocol incompatible with MCP but technically superior, with the Chinese ecosystem massively adopting it, AAIF would risk becoming irrelevant outside the West.

It is yet another manifestation of technological balkanization: one world, two Internets, two sets of AI standards. And as always happens in these scenarios, the one who pays the price is the global interoperability that these very standards claim to want to preserve.


## The Regulatory Vacuum as an Opportunity

And here we come to the crucial point: is it possible that behind the rhetoric of open interoperability, AAIF represents a preemptive strike on standards before regulators can establish the rules? This is my hypothesis, but consider the timing. The EU AI Act is being implemented with clear gaps regarding agents. The US still does not have comprehensive federal regulation on AI. In this regulatory vacuum, tech giants are de facto writing the regulations before the referees arrive.

A [report from the Center for European Policy Studies](https://babl.ai/new-report-urges-eu-to-clarify-governance-of-ai-agents-under-ai-act/) warns that AI agents could "completely escape regulation or lead to fragmented enforcement across the EU." The [privacy implications are profound](https://www.mhc.ie/latest/insights/rise-of-the-helpful-machines): the GDPR does not explicitly mention agents, but their ability to autonomously collect and process vast amounts of personal data raises questions about who the data controller is when a system acts autonomously.

The security risks are equally concerning. Agents introduce new attack surfaces: prompt injection via external data, leakage of personal information, model tampering, data poisoning through compromised feedback loops. [HiddenLayer](https://hiddenlayer.com/innovation-hub/governing-agentic-ai/), an AI security company, notes that these systems "test the boundaries of existing regulation" and that "compliance is not a checkbox, it's a competitive advantage in the era of autonomous AI."

But if the technical standards have already been defined by vendors through AAIF, regulators will have few options: adapt to the existing standards or risk stifling innovation by requiring changes incompatible with the already established ecosystem. It's the same dynamic that made the GDPR so difficult to apply to social platforms: when technical architectures are already deployed, changing them becomes prohibitive.

## Towards an Agent-Centric Future

Not everything is bleak. Open standards have historically accelerated innovation by allowing smaller players to compete without having to reinvent the infrastructure. MCP could indeed reduce ecosystem fragmentation, AGENTS.md could make agent behavior more predictable, and Goose could show that local-first is possible. The Linux Foundation, despite criticism, has a long history of stewarding critical projects like Kubernetes and Node.js.

But a critical eye is needed. As Neal Stephenson observed in "Snow Crash," when private protocols govern shared spaces, whoever controls the protocols de facto controls those spaces. AAIF could genuinely be an initiative for the common good, or it could be the tech equivalent of dividing up territory before the law arrives.

The questions to ask are simple: who has real decision-making power in AAIF? How are conflicts between member corporations with competing interests resolved? What mechanisms are in place to ensure that the standards serve end-users and not just the commercial interests of the founders? And above all: will regulators be involved in the standard-setting process, or will they find themselves having to ratify decisions already made?

Jim Zemlin of the Linux Foundation [argues](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/) that "dominion emerges from merit and not from vendor control," citing Kubernetes as an example. But Kubernetes emerged when the field was open. AAIF is trying to define standards when the founders are already the main players in the market.

Time will tell if AAIF will become the neutral infrastructure it promises to be, or if it will turn out to be a well-packaged cartel where open source becomes a tool for preemptive monopoly. For now, as tech companies write the protocols and regulators are still studying the problem, one thing is certain: whoever defines the language then defines the law. And right now, the language is being defined by OpenAI, Anthropic, and Block, with the imprimatur of the Linux Foundation and the funding of tech giants. Ask yourselves: is this really in the public interest, or is it a strategic alliance disguised as benevolence?
