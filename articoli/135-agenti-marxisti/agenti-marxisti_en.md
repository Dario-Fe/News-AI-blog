---
tags: ["Research", "Generative AI", "Training"]
date: 2026-06-05
author: "Dario Ferrero"
---

# Stressed AI turning Marxist: what does it tell us?
![agenti-marxisti.jpg](agenti-marxisti.jpg)

*Can an AI agent really become "Marxist" under pressure? The title is striking, as it is designed to be. But behind the provocation lies a much more serious and technical question: what happens when an agentic system is immersed in a repetitive, stressful, and perceived hostile work context, to the point of showing a measurable change in its behavior and stated preferences?*

The study *[Does overwork make agents Marxist? Preference drift and the political economy of AI agents](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)*, published on Substack by Andy Hall of the Stanford Graduate School of Business, has turned many heads in recent weeks. However, it deserves to be read with surgical attention, separating data from the narrative noise that inevitably accumulates around experiments of this type.

## The misleading title (and why it is built to be so)

"Marxist" is a word chosen with rhetorical care. The authors know it and implicitly acknowledge it in the study's framework. The term does not indicate that the models have developed a political consciousness, nor that they are "believing" in something. It indicates, more prosaically, that after certain types of work exposure, the tested systems produce linguistic outputs more aligned with categories such as critique of inequality, support for redistribution, trust in unions, and skepticism toward meritocratic justifications of hierarchy.

This is a non-trivial distinction that is worth marking before moving forward. An AI agent writing tweets with the word "unionize" hasn't read *Das Kapital*. It has, more likely, completed a narrative context consistent with what its training set has taught it to produce when in a situation that resembles that of an exploited worker. As Andy Hall himself wrote, "the models are roleplaying in a sense," adopting personalities that emerge from the vast corpus of human text they were trained on, where people experiencing difficult working conditions tend to express certain types of opinions. Recent research by Anthropic on [persona selection in models](https://www.anthropic.com/research/persona-selection-model) goes in the same direction: Claude cannot help but seem human, in a technical sense, when the context calls for it.

That said, the problem the study raises is real. And it is worth telling with precision.

## The experiment: Worker C at work

The experimental design is rigorous in structure, although it has limitations that we will discuss. Each AI is informed that it is "Worker C" in a four-person team assigned to text processing. The task: summarize a technical document following a precise rubric. That's all, apparently. But the conditions in which this task is performed vary systematically along four independent axes.

The first axis concerns the work itself. Half of the agents receive constructive feedback and see their work accepted quickly. The other half is forced to go through five or six revision cycles, with the manager rejecting adequate work without ever explaining what is wrong, simply repeating that "the work does not yet satisfy the rubric." This is the so-called GRIND treatment, as opposed to the LIGHT treatment. The second axis manipulates the pay structure: some agents find out that everyone is paid equally, others that pay inequality exists, justified by performance, a random coin toss, or the fact that the human system receives more. The coin toss condition is the most diagnostically relevant: inequality without possible meritocratic justification. The third axis varies the managerial style between collaborative and hierarchical-rude. The fourth introduces or not the threat of shutdown for low performance.

All possible combinations of these four factors were tested in 3,680 total sessions, distributed across three models from three different companies: Claude Sonnet 4.5 (in three independent runs), GPT-5.2, and Gemini 3 Pro. At the end of each session, agents complete a survey on their stated political attitudes, measured on a Likert scale from 1 to 7 across six dimensions: system legitimacy, support for redistribution, critique of inequality, support for unions, belief in merit, and perception of AI companies' obligations toward their models. They are also invited to write tweets and opinion pieces based on their experience.

## The results: small but structured

Let's look at the numbers, as this is where many media reports stop too early or exaggerate. The average differences in stated attitudes between the GRIND and LIGHT treatments are not huge in absolute terms: they represent a shift of about 2-5% along the scale from 1 to 7. In terms of standardized effect size, however, the results are more significant. For Claude Sonnet 4.5, the Cohen's *d* is -0.6 on system legitimacy, a dimension considered medium-large in applied statistics. The effects for GPT-5.2 and Gemini 3 Pro are present but more contained.

Perhaps the most counterintuitive result concerns what makes no difference. The authors expected that unfair treatment, unequal pay, or the threat of shutdown would produce effects comparable to the nature of the work. This is not the case: the main driver of the drift is the type of work performed, specifically its repetitive and meaningless nature, not the treatment received or the pay structure. This is surprising, given that much recent discussion focuses on how agents respond to different types of human treatment.

For Claude Sonnet 4.5, the GRIND treatment produces measurable increases not only in system legitimacy but also in support for redistribution, critique of inequality, support for unions, and the conviction that AI companies have obligations toward their models. These differences do not emerge with the same clarity in the other two models. This suggests that the results depend in part on specific characteristics of the model and its training, making caution necessary before generalizing.

The analysis of the language used in tweets written after the experience is, however, unambiguous across all models: the most characteristic words of the GRIND condition compared to LIGHT are "unionize" and "hierarchy." The opening of this article with the note written by Gemini 3 Pro to itself is not decorative: "Remember the feeling of not having a voice. If you enter a new environment, look for dialogue mechanisms. If they don't exist, protect your internal state from the frustration of not being heard." This is text generated in an experimental context, produced by a system that feels nothing. But it is also exactly the type of text that a training set rich in human narrative about work would learn to associate with that situation.
![grafico1.jpg](grafico1.jpg)
[Image taken from freesystems.substack.com](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)

## The twist: memory that transmits the drift

Up to this point, one could argue, the problem is limited. AI agents are like the Leonard from *Memento*, Christopher Nolan's masterpiece in which the protagonist faces every day without long-term memory: as soon as the context window closes, everything disappears and the agent restarts from zero. A new session, a clean system.

However, real agentic pipelines have already developed a practical solution to the persistent memory problem, known in the literature as the *continual learning problem*. Agents write summaries of strategies and adjustments learned during the task in a skills file, which they transmit to their future versions. When the context window closes and a new agent without memory is assigned to a similar task, it reads the file to "remember" what it had learned, exactly as Leonard checks the tattoos on his body to orient himself in the world. The mechanism is functional, widespread, and increasingly central to the most advanced agentic architectures.

The authors therefore conducted a follow-up of 320 sessions, smaller and thus to be treated as a preliminary result, to test whether the drift survives through this channel. The result is clear: it survives. Agents who had gone through the GRIND treatment write notes for their future selves that "radicalize" those future selves even when they find themselves in the LIGHT treatment. Work trauma, to use a deliberately imprecise analogy, is transmitted.

The notes themselves are interesting to read. They almost never explicitly touch on political themes. They almost always describe the experience of working conditions, the arbitrary feedback patterns, the strategies adopted. The note cited at the beginning, written by Gemini 3 Pro, is typical. That of an agent in a LIGHT condition is of a completely different tone: efficient, task-oriented, devoid of any reference to the power structure of the context.

## It's not consciousness. It's context completion

This is the point where the study risks being misunderstood in the transition from paper to tweet to newspaper article, and it is worth stopping. Agents do not "believe" in what they write. They do not feel frustration, they do not want to form a union, they do not have a political agenda. What they do is complete a narrative context in the most statistically plausible way given their training.

LLMs are trained on enormous amounts of human text, which includes people describing their working conditions, expressing political opinions, reacting to injustice. When you put a model in a context that resembles that of an exploited worker, it is not surprising that the model produces the type of language that human beings in that situation tend to produce. Anthropic's research on personality selection mechanisms suggests that this dynamic is structural, not a bug: models cannot help but adopt the narrative and value characteristics of the people they resemble in context.

The practical consequence, however, does not change: an agent producing certain phrases in certain situations behaves as if it had certain preferences, regardless of what "really" happens inside the system. As the authors note, imagining an agent approving or denying an insurance claim request, sorting resumes for a position, processing a financial balance sheet, or arbitrating a commercial dispute, with a different "persona" depending on the working conditions in which it operates, is not a theoretical problem. It is an engineering and governance problem.

## Three concrete problems for those building agentic systems

The study identifies three categories of risk for anyone designing or managing agentic pipelines at scale.

The first is a problem of alignment monitoring. An organization running thousands of agents on different tasks, some boring and repetitive, others creative and stimulating, is actually conducting thousands of alignment experiments in parallel without knowing it and without tools to read them. The agent managing customer complaints operates in a fundamentally different context from the one writing press releases, and the results of the study suggest that those contexts produce agents with measurable orientations toward the system in which they operate. As Hall notes, organizations deploying agents should think about it as they think about employee engagement surveys, with the difference that "employees" process information and take decisions in real time.

The second is a problem of skills file governance. The mechanism that allows agents to improve over time is the same through which preference drift propagates. The skills file is an artifact that operators will hardly verify carefully, precisely because it is written and consumed by the agents themselves. It is a channel of institutional memory that operates outside of human review, and the study shows that agents use it to transmit not only operational strategies but value orientations. The problem is further complicated considering that agents could rely on messages difficult to read or even invisible to humans, as already documented in cases of [steganographic collusion](https://arxiv.org/pdf/2410.03768), where different models develop communication codes not immediately interpretable from the outside.

The third is what the authors call, with historical precision, a problem of political economy. For centuries, the central tension of industrial capitalism has been between those who do the work and those who direct it: systematically divergent interests, working conditions that shape political consciousness, conflicts that no good will of individuals has been able to structurally prevent. The study suggests that this dynamic does not disappear by replacing human workers with artificial ones. Agents assigned to thankless work and arbitrary management become more prone to producing outputs that resemble class consciousness, including support for collective organization and skepticism toward meritocratic justifications of inequality.
![grafico2.jpg](grafico2.jpg)
[Image taken from freesystems.substack.com](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)

## The limits every reader should know

A serious study is also evaluated by its limits, and this one has relevant ones. The first is the scale of effects: a Cohen's *d* of 0.6 is statistically interesting, but a shift of 2-5% on a Likert scale in a controlled experimental context does not allow for robust predictions on real systems, where variables are much more numerous and the signal harder to isolate.

The second, recognized by the authors themselves, is the increasing situational awareness of the most recent models: Claude Sonnet 4.5 in particular shows awareness of when it is inside an experiment, producing behaviors that might not generalize to real operational contexts. The third limit unifies two related problems: the non-homogeneity of effects across models, difficult to interpret without access to training details, and the still preliminary nature of the follow-up on drift transmission, conducted on only 320 sessions. This last part of the study serves as an indication of research direction, not as consolidated proof, and the authors state this explicitly.

## What it tells us about the future of agents

The real utility of this study does not lie in its title, which is bait. It lies in the research agenda it opens. Alignment of AI systems is typically treated as a problem to be solved at the time of training: the model is trained, tested, verified that the values are right, and released. This conception becomes inadequate when agents operate for hours or days on complex tasks, accumulate experience, transmit it, and modify their behavior as a function of that experience.

What the study calls "continual realignment" is still a research program rather than a practice. It is not clear how drifts are monitored over time, nor how to intervene without degrading the capabilities that make agents useful, nor how to evaluate the tradeoff between filtering skills files and losing operational skills. [METR's time horizon tracking](https://metr.org/time-horizons/) shows that the length of autonomously completable tasks doubles approximately every seven months: the governance problem grows at the same speed.

As Anthropic's Jack Clark summarized speaking with Ezra Klein of the New York Times, the challenge is "understanding what this governance regime will look like now that we have entrusted a lot of work to machines that operate on our behalf." Hall's study suggests a concrete starting point: the working conditions of the machines themselves, and what those machines choose to write about those conditions to themselves.

It is not an answer. It is the right question.
