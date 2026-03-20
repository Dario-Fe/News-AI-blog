---
tags: ["Research", "Training", "Applications"]
date: 2026-03-20
author: "Dario Ferrero"
---

# The Researcher Sleeps. Autoresearch: How Andrej Karpathy Taught Machines to Perform Autonomous Research
![autoresearch-karpathy.jpg](autoresearch-karpathy.jpg)

*There is a scene in Japanese role-playing games, Karpathy knows them well, in which the protagonist stops fighting monsters alone and begins to train other characters to do it in his place. The transition changes everything: you are no longer a fighter, you are a trainer. Andrej Karpathy has done something similar with artificial intelligence research.*

Karpathy is a figure who needs little introduction in the sector, but it is worth framing him for those coming from outside. Former director of artificial intelligence at Tesla, co-founder of OpenAI, today an independent and prolific technical communicator: he is known above all for his ability to make dense and specialized concepts accessible. His course [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) is a reference point for anyone who wants to understand language models without a PhD in their pocket.

At the beginning of March 2026, Karpathy published a new open-source project on GitHub called [autoresearch](https://github.com/karpathy/autoresearch). The repository already has over 23,000 stars and nearly three thousand forks, numbers that in the world of software development measure interest with the same precision as a seismograph. The basic idea is simple to describe but difficult to digest: give an artificial intelligence agent a small but authentic language model training system, and let it experiment on its own, at night, while the researcher sleeps.

## Anatomy of a Nightly Loop

To understand what autoresearch does, it is useful to imagine the daily work of a machine learning researcher. Normally, this person sits in front of the computer, formulates a hypothesis ("what if I used a smaller batch size?"), manually modifies the training code, launches an experiment that lasts for hours, analyzes the results, and starts over. It is a serial process, slow, and limited by the hours of the working day and human concentration capacity.

Autoresearch breaks this cycle radically. The system is built around only three files that really matter: `prepare.py` (which handles data preparation and is never modified), `train.py` (the model code, which the agent can touch in every part), and `program.md` (instructions for the agent, written in natural language). The human user does not touch the Python files: their task is to write and refine the Markdown file, that is, to *program the program* rather than programming directly.

Once started, the agent—in the standard configuration this is Anthropic's Claude or OpenAI's Codex—reads the instructions, proposes a modification to the training code, runs an experiment with a fixed duration of exactly five minutes, measures if the result has improved, keeps or discards the modification, and repeats. Twelve experiments per hour, about a hundred over the course of a night. In the morning, the researcher wakes up to a detailed log of everything that was tried and (hopefully) a better model.

The metric used to measure progress is called `val_bpb`, or *validation bits per byte*: it measures how well the model manages to compress the text, in terms of how many bits are needed to represent each byte of data. It is an elegant metric because it is independent of the vocabulary size, which means that experiments with different architectures remain comparable with each other. Lower values indicate a more capable model.

The entire code base spans about 630 lines of Python. It is not an accessory feature: it is a philosophical choice. Karpathy deliberately built a system that a single developer can read, understand, and keep under control. Human review remains possible. The diffs, the differences between one version of the code and the next, are readable.

To fully understand autoresearch, you need to know the project it was born from: [nanochat](https://github.com/karpathy/nanochat), which Karpathy describes simply as "the best ChatGPT that a hundred dollars can buy." This is not marketing hyperbole: nanochat is a complete and minimal system for training language models on a single GPU, covering the entire pipeline, from tokenization to pretraining, from fine-tuning to a functional chat interface.

Its boast is a public leaderboard that measures the time needed to replicate the capabilities of the original GPT-2 (which in 2019 cost about $43,000 and weeks of computation) on accessible hardware: currently, the record has dropped to just over three hours on a node with eight H100 GPUs, for a cost of around seventy dollars.

Autoresearch is, in essence, the single-GPU and agent-centric version of nanochat: it uses the same simplified code base as an experimental field, with the same val_bpb metric as a compass, but entrusts the agent with the task of exploring that territory on its own.

Understanding nanochat means understanding what the agent is actually working on, and why the results obtained in five minutes of autonomous training can be compared, with some caution, with those of the more demanding sessions on the main leaderboard.

## What the Numbers Really Do

The most honest way to evaluate autoresearch is not to look at the project description, but at the real data of the experiments. Karpathy published in [discussion #43](https://github.com/karpathy/autoresearch/discussions/43) of the repository a detailed account of a full session, remarkably transparent: 126 experiments performed on an NVIDIA H100 GPU over approximately ten and a half hours.

The starting point was a `val_bpb` of 0.9979. The end point: 0.9697. An improvement of 0.0282 in absolute terms, which in this context represents a significant leap. To get oriented: the most impactful modifications were the reduction of the batch size (from 524,000 to 262,000 tokens, which allowed for more update steps in the available five minutes, gaining a 0.0119 improvement), the addition of a layer to the model depth (0.0043), and a series of finer adjustments such as the introduction of small regularization values (*weight decay*) on the embedding components.

What is striking when reading the full log is not just the final result, but the granularity of the process. The agent systematically explored dozens of hypotheses, many of which turned out to be dead ends: *weight tying* between embedding and de-embedding produced a catastrophic drop in the metric; multi-query attention with a single key-value head turned out to be too aggressive; architectures with more layers but smaller dimensions ended up exhausting the five-minute budget even before converging. These documented failures are almost more useful than the successes, because they draw the map of the explored territory.

The results obtained on an H100 GPU, the highest-performing graphics card currently available for this type of workload, then proved transferable to deeper models with 24 layers, enough to compete in industry reference rankings. This is not a trivial result. But the boundary of transferability is still unclear, and this is one of the project's limitations worth dwelling on.
![grafico1.jpg](grafico1.jpg)
[Image taken from github.com](https://github.com/karpathy/autoresearch)

## The Flip Side

Autoresearch has received an enthusiastic reception, and the enthusiasm is understandable. But an honest analysis requires looking also at where the system shows its cracks.

The first limit is structural: the fixed budget of five minutes per experiment, which is also one of the project's strengths, becomes a rigid constraint when exploring more complex architectures. In the data from session #43, it is clearly seen: every attempt to add layers beyond a certain threshold ended with an incomplete experiment, because time ran out before the model converged. The agent was searching in a space of possibilities partially blocked by its own temporal architecture.

The second limit concerns parallelism. The system is designed for a single GPU, and experiments are executed in sequence, not in parallel. It means that while one experiment is running, no other can be started. Those who have access to a GPU cluster might want to explore more directions simultaneously; autoresearch, by deliberate choice, does not support it. Karpathy is transparent about this: it is a design decision, not an oversight. But the practical consequence is that the exploration of the research space remains fundamentally linear.

Third critical point: dependence on proprietary models. To run experiments in autonomous mode, a capable agent is needed, and in the standard configuration this refers to Claude or Codex, both commercial systems. Those who want to democratize artificial intelligence research might find it paradoxical that a tool designed to lower entry barriers still requires a subscription to third-party services.

There is also a subtler aspect, which concerns the very nature of the choices the agent makes. autoresearch is excellent for local optimization: it finds the best point in the vicinity of the starting point, through a sequence of small steps. But it is not a system designed to make conceptual leaps. Literature review, formulation of radically new hypotheses, understanding why an approach works at a theoretical level, all this remains human territory, at least for now. Real research, the kind that changes paradigms, is not just a sequential optimization process.

Finally, there is the issue of explainability. When the agent discovers that a weight initialization reduced to 0.68x of the standard value produces better results, it does not provide a causal explanation for this improvement. It knows that it works, not why it works. For those using the results as a starting point for subsequent research, this lack of understanding is a technical debt that sooner or later must be settled.

## The Human Who Programs the Program

One of the most interesting, and least discussed, ideas of autoresearch is the role it assigns to the human being in the process. It is not about eliminating them, but about moving them.

The `program.md` file is described in the README as an ultra-light "skill": a natural language document that defines the agent's goals, its priorities, and the constraints within which to operate. The user no longer writes Python, they write instructions. They don't modify the training code; they modify the document that tells the agent how to modify the training code. It is an extra level of abstraction, and it brings concrete consequences.

On one hand, this enormously lowers the entry threshold. You don't need a PhD in machine learning to start an autoresearch session. The README includes a "Weekend Guide," a weekend guide that promises to take anyone from initial configuration to the first autonomous experiments without a specialized background. The technical simplicity of the setup (a single NVIDIA GPU, Python 3.10 or higher, and the `uv` package manager) is real.

On the other hand, this abstraction creates a new dependency. Whoever writes the instructions in `program.md` determines the agent's exploration space. A poorly written document, with vague goals or contradictory constraints, produces equally vague research sessions. The bottleneck shifts: instead of requiring code writing skills, autoresearch requires skills in writing effective instructions for artificial intelligence systems, a relatively new discipline, still lacking consolidated standards.

There is something recursive in all this, and Karpathy is aware of it. In the project's README he has inserted a deliberately ambiguous epigraph, describing a hypothetical future in which swarms of autonomous agents manage computing clusters in a continuously self-modifying research, with a code base in the ten-thousand-and-twelfth generation "grown beyond human understanding." It is a tone between dystopian and a nerd joke, but the fact that that sentence opens the presentation document of a real project is not accidental.

## Where This Path Leads

The most immediate comparison for autoresearch is with AutoML, systems that in recent years have tried to automate the choice of neural architectures and hyperparameters. But there is a substantial difference: traditional AutoML operates on predefined search spaces, looking for the optimal combination among already enumerated options. autoresearch lets the agent freely modify any part of the code, including architecture, optimizer, batch size, learning scheme, practically everything. The exploration space is much larger, and much less structured.

This opens interesting possibilities, but also uncomfortable questions. If the system really works, if autonomous agents can do significant research on language models without continuous supervision, where does this process stop? The honest answer is that no one knows for sure. The project is explicitly designed to be the starting point for something larger, and Karpathy himself points the direction towards asynchronous multi-agent configurations, where multiple parallel instances explore different directions on distributed clusters.

From an ethical point of view, this scenario deserves attention. The acceleration of research cycles is desirable if it leads to better and safer models. But the same acceleration, applied without adequate supervision, can amplify algorithmic biases already present in the training data, produce optimizations that maximize measurable metrics at the expense of non-measurable qualities, or make the process opaque enough to escape any form of meaningful control.

The fact that autoresearch is open-source and minimalist is, in this sense, a guarantee parziale. The code is short enough to be audited; the experiment data are public. But as the system scales, towards multi-GPU clusters, towards longer sessions, towards agents that refine their own instructions, supervision becomes more difficult.

Finally, there is a pragmatic consideration regarding those evaluating this tool for professional use. autoresearch in its current form is a refined prototype, not a production system. It requires specific hardware (NVIDIA GPU, with optimal support for H100), depends on external APIs for the agent, and produces results that must be interpreted competently to be useful. The promise of the "weekend guide" is real for those who want to experiment, but it does not replace the basic understanding of how language model training works.

That said, the value of autoresearch is not measured only by what it does today, but by what it demonstrates to be possible. It shows that automated research on real systems—not simplified simulations, not artificial benchmarks—is already within the reach of anyone with a single GPU and the curiosity to explore. And it does so with a methodological transparency—that of public logs and readable code—that many well-funded research laboratories do not allow themselves.

The researcher who sleeps, meanwhile, has already woken up. He has found 126 experiments waiting to be read.
