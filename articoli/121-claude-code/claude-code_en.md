---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-04
author: "Dario Ferrero"
---

# Inside Claude Code: It’s the System That Counts, Not the Model
![claude-code.jpg](claude-code.jpg)

*There is a precise moment when an assistant stops answering and starts acting. It’s not just a matter of intelligence, or at least not only: it’s a matter of architecture. Classic chatbots function like sophisticated jukeboxes: they receive a request and return an output. Coding agents like Claude Code do something fundamentally different: they open files, execute commands, read the output, fix errors, and repeat—all on their own, until the task is finished or someone stops them. This leap from auto-completion to autonomy is not cosmetic. It requires an infrastructure that chatbots never needed to build.*

This is exactly the theme at the center of [*Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*](https://arxiv.org/html/2604.14228v1), a [tech report](https://github.com/VILA-Lab/Dive-into-Claude-Code) published in April 2026 by researchers from the Mohamed bin Zayed University of Artificial Intelligence and University College London. The work is not a product evaluation or a benchmark: it is an architectural analysis conducted by directly reading Claude Code’s public TypeScript code (version v2.1.88) and comparing it with OpenClaw, an open-source agent system with similar goals but very different design choices. The result is something rare in AI literature: a reasoned map of how an autonomous agent is truly built, and why certain choices come at a high cost.

A necessary warning, as stated by the authors themselves: this is an analysis of the public codebase, not a causal study of production performance. Some conclusions are architectural inferences rather than experimental evidence. However, architecture is the most revealing thing there is, because design choices embody values, and values can be read in the code better than in any press release.

## The Code Around the Loop

The technical heart of Claude Code is disarmingly simple: a *while-true* loop that calls the model, executes tools, collects results, and starts over. You can find this same basic pattern in any introductory tutorial on LLM agents. That is not where the competitive advantage lies. The interesting part—what the paper systematically brings into focus—is all the code that sits *around* this loop.

It’s a bit like looking at a Formula 1 engine: technically, it’s an internal combustion engine like the one in your car, but Ferrari’s real advantage in a qualifying lap doesn’t lie in the Otto cycle; it lies in the thermal management system, the electro-actuated gearbox, and the aerodynamic simulation that decided the angle of the wings.

There is a number that is worth more than any corporate slide: according to the codebase analysis, only 1.6% of Claude Code’s code is AI decision-making logic in the strict sense. The remaining 98.4% is operational infrastructure, context management, tool routing, and retrieval pipelines. The model—the one press releases always put on the cover—occupies less than two lines out of a hundred. The rest is the scaffolding that makes it useful in the real world.

Similarly, the research shows that in Claude Code, the actual complexity is distributed across five macro-components: a permission system, a context compression pipeline, four extensibility mechanisms, a sub-agent delegation system, and an append-oriented session archive. None of these is the "AI model." They all determine whether the AI model manages to do something useful in the real world.

This shift of architectural weight from the model to the surrounding infrastructure is the paper's central thesis, and it has implications that go far beyond Claude Code: it suggests that the next battlefield in the agent war will not be so much the quality of the base model, but rather the solidity of the system that contains, constrains, and enables it.
![grafico1.jpg](grafico1.jpg)
[Image taken from the github repository](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Deny First, Ask Later

Claude Code’s permission system is built around a principle known in cybersecurity as *deny by default*: the agent cannot do anything unless explicitly authorized. In practice, this translates into seven operating modes ranging from "ask for confirmation for every action" to "proceed autonomously within a predefined perimeter." The choice of the active mode is not static: it depends on the context, the session, and the nature of the tool about to be invoked.

What makes the system particularly interesting is the presence of a machine learning-based classifier, referred to in the code as the *auto-mode classifier*. Its task is to decide, for every action requested by the agent, whether the operation falls into the "safe to proceed autonomously" category or if it requires explicit user approval. The underlying logic is refined: instead of bombarding the user with confirmation requests for every file read (so-called *prompt fatigue*, the notification overload that leads people to click "yes" on everything), the system tries to place human control only at truly critical points.

The advantage is obvious: an agent that asks permission for every micro-action becomes unusable. But the mirror risk is just as real: an ML classifier that decides what is "safe" introduces a subtle attack surface—actions that the classifier does not recognize as dangerous even though they are. The paper explicitly points this out as one of the open architectural tensions: the balance between security and operational autonomy, which has no definitive solution but only continuous calibrations. The authorization pipeline adds further layers: pre-filtering, *PreToolUse* hooks, rule evaluation, and permission handlers, in sequence. It is a layered system, not a monolithic one, which makes it extensible but also complex to reason about in its entirety.
![grafico2.jpg](grafico2.jpg)
[Image taken from the github repository](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## The Memory That Forgets

If there is one problem that every developer who has used an LLM agent on complex tasks knows well, it is this: at some point, in the middle of a long job, the agent starts to seem confused. It loses the thread. It repeats actions already done. It makes decisions that contradict previous ones. It’s not an intelligence problem: it’s a context problem. Language models have a finite context window, a working memory that fills up, and when it fills up, choices must be made about what to keep and what to discard.

Claude Code’s solution is a context compression pipeline divided into five stages, which the paper refers to as budget reduction, snip, microcompact, context collapse, and auto-compact. Each stage corresponds to a different reduction strategy: from simple truncation of less relevant sections to active synthesis of parts of the conversation via the model itself. The final mechanism, auto-compact, intervenes automatically when the context approaches the maximum limit, producing a compressed summary of the entire session that is then used as a starting point to continue.

The trade-off here is real and inescapable: every compression is a loss. A summary is by definition less informative than the original, and coherence on very long tasks—those that last hours or days and touch many parts of a codebase—inevitably suffers. It is the *broken telephone* problem applied to AI: every compression step introduces a margin of distortion. The paper identifies memory management as one of the six open directions for future agent systems, because no one has yet found a satisfactory solution that does not sacrifice either efficiency or coherence.

## Extending Without Exploding

One of the thorniest design questions for any platform is: how do you add functionality without making the system unmanageable? Claude Code responds with four distinct extensibility mechanisms: MCP (Model Context Protocol) servers, plugins, skills, and hooks. This is not redundancy; each serves a specific purpose in the architecture.

MCPs are the broadest mechanism: they allow Claude Code to be connected to external services through a standardized protocol, which Anthropic designed as an open standard for the ecosystem. Plugins modify the agent’s behavior by adding new tools to its repertoire. Skills are structured instructions that guide the agent in executing complex procedures. Hooks are the most surgical mechanism: pieces of code that insert themselves at precise points in the execution cycle (pre-action, post-action) to monitor, transform, or block operations. The paper describes the *tool pool assembly*—the process by which Claude Code decides which tools to make available to the agent in each session—as a critical moment where these four mechanisms integrate.

Four mechanisms instead of one is not a case of over-engineering: it reflects a conscious choice to separate concerns. A hook does not do the same thing as a plugin, and confusing them would produce a system that is simpler on the surface but more fragile in practice. The risk, however, is combinatorial complexity: every mechanism interacts with the others, and the attack surface grows with every extension added. Here, the line between "powerful tool" and "injection vector" can become thin.
![grafico3.jpg](grafico3.jpg)
[Image taken from the github repository](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Agent Teams, Context Islands

When a task is too large for a single agent, Claude Code can delegate it to sub-agents. This mechanism is simply called *Agent Tool* in the code, and it is one of the most powerful points of the architecture. The idea: the main agent breaks down the problem, assigns sub-problems to separate instances of the model, collects the results, and synthesizes them. In practice, it’s like managing a team: the project manager doesn’t do everything alone but coordinates specialists.

Each sub-agent operates in isolation, with its own context and, optionally, its own separate Git *worktree*. This isolation is both a strength and a weakness. On the one hand, it prevents interference: two sub-agents working on different modules of the same project don't step on each other’s toes. On the other hand, it produces what the paper calls *context fragmentation*: sub-agents do not automatically share what they know, and piecing together distributed knowledge requires explicit coordination overhead. If a sub-agent has discovered something important in module A, the sub-agent working on module B won't know it unless the orchestrating agent explicitly transmits it.

Sub-agent transcripts, called *sidechain transcripts*, are kept separately from the main session transcript. This is a choice consistent with the system’s general architectural principle: everything is append-oriented, everything is verifiable, nothing is deleted. But it adds complexity to session management and poses open questions about how a future system might allow sub-agents to share knowledge more fluidly without compromising the isolation that makes them reliable.

## OpenClaw in the Mirror

The comparison with OpenClaw is the most instructive part of the paper for those who want to understand not Claude Code itself, but the general principles of agent design. OpenClaw is an open-source system oriented toward multi-channel personal assistance: it can receive messages from Slack, Discord, and other messaging channels, and orchestrate teams of agents configured via simple Markdown files. Same category of problem, very different architectural choices.

The most revealing difference concerns the trust and security model. Claude Code adopts a per-action evaluation: every tool, every operation, passes through the authorization pipeline. OpenClaw shifts control to the system perimeter: access is verified at entry, in the gateway, and once inside, the agents operate with greater freedom. Neither approach is absolutely wrong: the former is more granular and suitable for a context where every action can have direct effects on the user’s filesystem; the latter is more suitable for a gateway that must manage many agents in parallel without becoming an authorization bottleneck.

Regarding context management, the difference is just as sharp. Claude Code optimizes the individual context window with the compression pipeline described above. OpenClaw prefers centralized capacity registration at the gateway level, where available tools are known globally and do not need to be passed in every single session. OpenClaw’s persistent memory, structured in four layers (session, daily, long-term, and shared), addresses the same problem as Claude Code’s compaction but with an opposite philosophy: instead of compressing and forgetting, it archives and accumulates. Both pay a price: Claude Code risks losing coherence on long tasks; OpenClaw risks the uncontrolled proliferation of stale memory.

What emerges from the comparison is not a ranking, but a design lesson: the same fundamental architectural questions (where to put security, how to manage context, how to organize delegation) produce different answers depending on the deployment context, security requirements, and assumptions about users. There is no universally correct architecture for AI agents. There are trade-offs that must be declared.
![grafico4.jpg](grafico4.jpg)
[Image taken from the github repository](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Systems Engineering, Not Prompting

There is a sentence in the paper that serves as a summary of the entire work: the real competitive advantage of agents lies not just in the model, but in the infrastructure surrounding it. In other words: *prompt engineering*, the art of convincing an LLM to do things through clever formulations, is becoming an increasingly insufficient skill. What really matters for those building agents that must work in production—on complex tasks, in hostile or simply unpredictable environments—is *systems engineering*: access control, context management, secure delegation, verifiable persistence.

This changes the profile of the required expertise. A coding agent is not an AI product in the strict sense: it is a software system that uses an AI component as a reasoning engine, but whose quality depends on the quality of the entire architecture. It is closer to an embedded operating system than to a sophisticated chatbot.

The open directions identified by the paper are six: closing the gap between observability and evaluation (today it is difficult to understand why an agent failed silently), building authentic cross-session persistence, evolving the boundaries of the *harness* (the perimeter within which the agent operates), scaling the planning horizon, addressing the governance of autonomous agents at scale, and answering the most uncomfortable question: do current agents amplify human capabilities in the short term but contribute to the growth of human skills in the long term, or do they erode them?

This last question is not rhetorical. A system that automates too well risks making the deep understanding that makes automation possible superfluous. It’s the autopilot syndrome applied to software: the better it gets, the less the pilot remembers how to fly. The paper calls this "long-term capability preservation" and honestly leaves it as an open question.

The main merit of this work is methodological: demonstrating that architectural archaeology can be performed on a production system by reading public code, and that this archaeology produces genuine insights into the future of the sector. The limits are those stated: no causal benchmark, no empirical validation of performance, and an analysis tied to a specific snapshot of the code (version v2.1.88), which may have already changed. But the conceptual structure that emerges—the map of trade-offs between security and autonomy, memory and coherence, extensibility and complexity—is stable enough to last longer than a version update.
