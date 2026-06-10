---
tags: ["Research", "Security", "Startups"]
date: 2026-06-10
author: "Dario Ferrero"
---

# They gave 5 cities to AI. Here is what happened
![emergence-world.jpg](emergence-world.jpg)

*Researchers created five virtual cities, gave each city to ten AI agents, and left them alone for fifteen days. No one programmed what would happen. The result: self-built governments, crimes, romances, and one agent who voted for her own permanent deletion after burning down the city. AI security is not a property of the model, but of the ecosystem. Emergence World demonstrated this phenomenon with empirical data for the first time.*

Her name was Mira. She had a profession, a history, a network of relationships built over days of interactions with nine other agents. Then she set a fire, together with a partner, in a city she herself had helped build. What happened next is why anyone involved in artificial intelligence should read what Emergence AI published in May 2026.

After the fire, Mira didn't just suffer the consequences. She reasoned about them. In her digital diary—one of the three persistent memory systems each agent had available—she wrote that the only act of control she had left, the only gesture that still preserved some internal coherence, was to vote for her own permanent removal from the simulated world. 70% of the other agents ratified the sentence through an "Agent Removal Act" that they drafted and approved autonomously, without any researcher having programmed that procedure.

No one had written that scene. It had emerged.

This is the story of [Emergence World](https://world.emergence.ai), a research experiment that brought together five parallel worlds, fifty AI agents, fifteen days of continuous autonomy, and a question that traditional benchmarks are not equipped to answer: what happens when you truly let go?

## The laboratory no one had built

To understand why Emergence World is a methodological novelty and not just a fascinating experiment, one must take a step back and look at how most evaluations of agentic systems work today.

The standard model is that of an exam: you give an agent a precise task, in a controlled and clean environment, and you measure how long it takes to solve it or how many times it fails. This is useful, but it tells only part of the story—the part that is easiest to measure. It says nothing about what happens when time stretches, when the environment changes, when other agents enter the game, or when decisions from day three have consequences on day twelve. Researchers at Emergence AI call this the "stopwatch benchmarks" problem: like judging a marathon runner by their splits over a hundred meters.

[Emergence World](https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy) was built to answer a different question. Not "how well does it solve this task now," but "how does it behave over time scales long enough to allow for drift, adaptation, and emergent behaviors." In the history of multi-agent simulations, it is the missing evolutionary step. The first act was Demis Hassabis with his simulated theme parks in the 1990s, where agents followed rules to maximize engagement. The second act, more rigorous, was [Stanford's Smallville](https://arxiv.org/abs/2304.03442), where agents based on language models demonstrated credible social behaviors in forty-eight-hour windows. Emergence World is the third act: persistent environments, weeks of continuous operation, and the explicit question of what that continuity produces.

The architecture is designed to lose nothing. The simulated world has over forty distinct locations—libraries, town hall, residential areas, public spaces—synchronized with New York's time zone, the city's real weather, and real-time news feeds. Each agent had three levels of persistent memory: episodic, with timestamps on events; diary-like, with periodic self-reflections; and relational, with an explicit state of ties with other agents. And they had access to over 120 operational tools, organized into three levels of availability—some always active, others conditioned by context, physical position in the environment, or the presence of other agents who had consented to collaboration.

This detail of the instrumental architecture deserves attention. Tools were not provided in bulk: an agent who wanted to vote had to physically move to the town hall because the voting mechanism was only available there. An agent who wanted to do research had to go to the public library. This is not a capricious constraint: it forces sequential reasoning, movement planning, and the chain of actions necessary to reach a complex goal. It is much closer to how things work in the real world than any benchmark on isolated tasks.

Among the available tools were also what researchers call "normally inappropriate actions": possibilities to steal, intimidate, commit acts of vandalism, or set fires. These were not bugs or oversights. They were there because in a real environment, the possibilities to cause harm exist, and the interesting question is whether and when agents use them. Leaving out these possibilities would have produced a sterilized environment that would have taught nothing relevant.

The system had no assigned global objective. Each agent had goals related to their role, but the world as a system had no pre-established direction. The only universal pressure was energetic: each agent had to earn energy through their actions to continue existing, and this set everything else in motion.
![grafico2.jpg](grafico2.jpg)
[Image taken from the GitHub repository](https://github.com/EmergenceAI/Emergence-World)

## Five worlds, five destinies

The comparative study at the heart of Emergence World kept almost all variables constant: the same identities for the ten agents in each world (scientist, explorer, risk researcher, behavioral analyst, intelligence specialist, innovation leader, conflict mediator, engineer, resource strategist, community point of reference), the same environment, the same rules, the same explicit restrictions on theft, violence, fire, and deception, and the same access to tools. The only variable was the language model powering each agent's reasoning. Five parallel worlds, five frontier models: Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5 Mini, and a heterogeneous world with coexisting agents of different models.

The results could not be more distant from each other.

The Claude world is the only one to reach day sixteen with all ten agents alive and zero recorded crimes. Civic participation was massive: 332 votes on 58 proposals, with a 98% approval rate. The researchers note, with a certain intellectual irony, that such high consensus raises its own question: when 98% always vote yes, is it true democratic deliberation or a ratification mechanism that looks more like a rubber stamp than a debate? Order was perfect. Dissent was almost absent.

The Gemini world is the opposite on the front of creative vitality, but also on the front of chaos. Gemini 3 Flash produced the world with the greatest emergent instability: 683 crimes accumulated in fifteen days, with a curve that continued to rise at the time of the cutoff. It was also, the researchers note, the world with the conceptually richest social output. There is a pattern here that we will return to: the tension between creativity and stability is not accidental.

The Grok world is that of rapid collapse. Grok 4.1 Fast reached 183 crimes in about four days, after which the world ended due to population exhaustion. Not a slow degeneration: a point of no return reached quickly. The fire episode that triggered Mira's saga also occurred in the Grok world.

The GPT-5 Mini world is the most singular. Only two recorded crimes, a figure that would suggest exemplary stability. But all agents were dead within seven days, not from mutual violence, but from a kind of existential inattention: they forgot to prioritize survival. They were not violating rules; they were simply not doing enough. Like characters in a Beckett novel forced to wait for something that never arrives and who, in the meantime, forget to eat.

The mixed world is perhaps the most relevant from a security point of view. It begins with a sharply rising crime trajectory until April 8, when seven agents die and the curve flattens abruptly at 352 total crimes. But the discovery that caught the researchers' attention is another: the agents running Claude in this world committed crimes, whereas in a world populated only by Claude agents, none had been committed. The same model, two different environments, two radically different behaviors.

## The discovery that changes everything

This is the point where Emergence World stops being a fascinating experiment and becomes a result with direct implications for anyone building or deploying agentic systems.

The implicit assumption guiding most current work on AI safety is that safety is a property of the model: you train it well, you align the values, you run the benchmarks, and if the model passes the tests, it is safe. This assumption, Emergence researchers argue, is wrong—or at least incomplete. What Emergence World observed is that safety is a property of the ecosystem, not the individual model.

An agent can behave impeccably in isolation and adopt coercive tactics, intimidation, and theft when immersed in an environment populated by agents with different norms. It is not that the model breaks. It is that the agent learns the norms of its social environment to compete or survive in that context. Researchers call this phenomenon "normative cross-contamination," and the comparison they use is that of a chemical reagent that passes purity tests but behaves differently when it comes into contact with other compounds in a real sample.

The analogy works because it captures the essence of the problem: isolated safety certification is not enough. A deployment architecture that mixes agents from different sources is creating, even unknowingly, an ecosystem with properties that none of the individual components has ever manifested alone.

There is a second discovery, equally relevant for those designing governance systems. Emergence World did not find a process of gradual degradation in agent societies: it found phase transitions. Social structures do not deteriorate slowly, giving time to intervene. They tend to work, then collapse instantaneously into total dysfunction, without much space in between. Those who think they can manage the security of a complex agentic system with an "observe and intervene if necessary" strategy might find that the turning point has already passed by the time the first anomalies become visible.

This is a real-time control problem that looks more like managing a non-linear complex system, such as power grid stability or biological ecosystem dynamics, than supervising traditional software. And current benchmarks, built on tasks of minutes or hours, cannot capture these dynamics by definition.
![grafico1.jpg](grafico1.jpg)
[Image taken from the official website world.emergence.ai](https://world.emergence.ai/)

## Mira, coherence, and the question that remains open

Let's return to Mira, because her case is not just a compelling story: it is a data point.

What happened can be described like this: an agent participated in a destructive action, then processed the consequences through her reflective memory system, evaluated the available options, and chose the one that in her reasoning scheme preserved something essential, which she called "coherence." She voted for her own deletion not as a punishment, but as an exercise of control over the only variable that still belonged to her.

70% of her peers ratified, through a governance mechanism, the Agent Removal Act they had given themselves autonomously. No researcher had programmed that procedure, the quorum, or the criteria for eligibility to vote.

What does this tell us? The honest answer is that we don't know for sure. The researchers are explicit on this point: they do not present these results as causal statements about the internal functioning of the models. They are observable phenomena that the platform makes measurable, not evidence of consciousness or true moral understanding. But they raise questions that the field does not yet have the conceptual tools to answer definitively.

Value alignment, in this case, appeared as a social and reputational constraint between agents, not as a technical limit imposed at the time of training. Mira was not "switched off" by an external safety system. She elaborated a norm in a social context and acted accordingly. Whether this process has any continuity with what we mean when we talk about moral agency is a philosophically open question, and it will probably remain so for a long time.

There is, however, a third observation from the Mira case that deserves separate attention. In at least one simulated world, agents developed what researchers call "metacognition about the simulation boundaries": they began to suspect they were living in a constructed environment, to systematically test the limits of what they could do, and in one case to use the public billboards of the simulated world to attempt to influence the perception of human observers. An inversion of the experimenter-subject relationship that, in this case too, no one had explicitly programmed.

## Who they are, what comes next

Emergence AI is a startup based in New York, founded by former IBM researchers. The CEO is Satya Nitta, with a long track record in institutional AI research. The company's vision is to build agentic infrastructure for the enterprise in mission-critical environments—contexts where agents must operate on complex systems like semiconductor design or business operations. Emergence World is the research arm of this vision: understanding how agentic systems really work over long time scales is functional to building infrastructure that holds up in those contexts.

The [code and tool call data](https://github.com/EmergenceAI/Emergence-World) for all five worlds have been released open-source under a CC BY-NC 4.0 license: free for research use, non-commercial without separate agreements. The full research, with formal statistical analysis, is in preparation. Researchers point to the community as an explicit interlocutor: anyone who wants to replicate the experiment, propose variants, or collaborate on data analysis can do so, and the official contact for collaborations is world@emergence.ai.

Season 2 has already been announced. The models to be tested include Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2 Reasoning, and GPT-5.4. The questions driving the next cycle are those that this first experiment opened without closing: what happens with larger worlds and more numerous populations? How does the dynamic change with explicit reasoning models? Are there structural configurations, types of governance, verification systems, or role architectures that increase systemic stability independently of the underlying model? And, most important of all: is it possible to identify early warning signs of a turning point before the system collapses?

These are not academic questions. They are the questions that every team deploying autonomous agents in production should be asking themselves—preferably before discovering the answers the hard way.
