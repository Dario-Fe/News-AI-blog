---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2025-11-07
author: "Dario Ferrero"
---

# When AI Looks Within: Artificial Introspection Between Science and Illusion
![introspection-anthropic.jpg](introspection-anthropic.jpg)

*Anthropic's paper on introspection in language models has reignited a debate that seemed to have stabilized: can artificial intelligences "look inside themselves" as we humans do? The answer, as is often the case with AI, depends on what we mean exactly by introspection, and how willing we are to resist the temptation to anthropomorphize machines that behave in increasingly surprisingly human-like ways.*

## The Controversial Experiment

The [research published by Anthropic](https://www.anthropic.com/research/introspection) probably represents the most rigorous attempt so far to answer a question that is as fascinating as it is slippery: when we ask Claude what it is "thinking," do we get a genuine report of its internal states or just a plausible confabulation? How can we distinguish authentic introspection from conversational performance?

The research team, led by scientists from Anthropic and Stanford, tackled the problem with an experimental approach as ingenious as it was invasive: instead of relying solely on the model's textual responses, they directly manipulated its neural "guts," injecting representations of specific concepts into its intermediate layers and observing whether the model was able to recognize these manipulations. It's a bit like a neurologist being able to artificially activate the idea of "betrayal" in your brain and then ask you, "Do you notice anything strange about your thoughts?"

The results obtained with Claude Opus 4 and 4.1, the most capable models tested, show that in about twenty percent of cases the system actually manages to identify the presence of an "injected thought" even before verbalizing the concept itself. When the team injects a representation of the concept "uppercase" into the neural layers, the model responds with statements like "I'm experiencing something unusual... I detect an injected thought related to volume or shouting." The timing is crucial here: the model recognizes the anomaly immediately, before it can clearly influence its outputs.
![schema1.jpg](schema1.jpg)
[Image from the Anthropic paper](https://www.anthropic.com/research/introspection)

## How to Inject a Thought

The methodology, which the researchers call "concept injection," is a sophisticated variant of the activation steering techniques explored previously. Last year, Anthropic had demonstrated "Golden Gate Claude," a version of the model obsessed with the famous San Francisco bridge after similar manipulations. But there is a fundamental difference: in that case, the model seemed to notice its obsession only after it started talking about it compulsively, like someone who realizes they have a song in their head only after unconsciously humming it.

In the new experiment, however, the recognition appears genuinely introspective. The researchers first extract an activation vector corresponding to a specific concept, recording the model's neural activations when it responds to prompts that evoke that concept, comparing them with control activations. This vector is then injected into the model's residual stream, typically at about two-thirds of its depth, during the processing of a completely different prompt that explicitly asks the model if it detects injected thoughts.

The technique is far from infallible. Even with the optimal protocol, Claude Opus 4.1 demonstrates this introspective ability in only twenty percent of attempts. Often the model fails to detect the injected concepts at all, or produces bizarre hallucinations: the injection of the concept "dust" in one case caused the response "There's something here, a tiny particle," as if the model could physically perceive the dust. The phenomenon only works within a "sweet spot" of injection intensity: too weak and it goes unnoticed, too strong and it produces incoherent outputs or confabulations.
![schema2.jpg](schema2.jpg)
[Image from the Anthropic paper](https://www.anthropic.com/research/introspection)

## The Numbers That Dampen the Enthusiasm

This is where the data becomes the best antidote to excessive enthusiasm. A twenty percent success rate is not a scientifically negligible discovery, but neither is it a result to be celebrated as "emerging consciousness." To put it in context: it means that in four out of five cases, even the most capable model tested fails to accurately report its own internal states when they are deliberately manipulated.

The researchers tested different categories of concepts, finding that abstract nouns like "justice," "peace," "betrayal," or "balance" are recognized better than other categories. Famous people, countries, concrete nouns, and verbs achieve lower success rates. Even more interesting: when they tried to inject random vectors (with a norm equivalent to that of the conceptual vectors at intensity 8), the detection rate dropped to nine percent, with the model producing seemingly random words like "mirror," "water," "Pennsylvania," with no discernible pattern.

The introspective ability also varies dramatically between different models. While Opus 4.1 and 4 stand out clearly, with success rates reaching about twenty percent while maintaining zero false positives, other Claude models show significantly lower performance. It is interesting to note that the "helpful-only" variants, trained with a different post-training pipeline that minimizes refusals, sometimes show higher false positive rates, suggesting that fine-tuning strategies heavily influence these capabilities.

The pre-trained base models, tested before post-training, failed completely, with high rates of false positives and no net ability to correctly identify the injections. This indicates that introspection, if it can be called that, does not emerge spontaneously from training on large text corpora, but requires the refinement of post-training.
![grafico.jpg](grafico.jpg)
[Image from the Anthropic paper](https://www.anthropic.com/research/introspection)

## Critical Voices Are Multiplying

The publication has elicited mixed reactions in the scientific and philosophical community. The main concerns regard the interpretation of the results and the risk that sensationalist media coverage will transform limited functional abilities into claims about "artificial consciousness."

Herman Cappelen, a philosopher who published a [critical paper on the lightweight account of introspection](https://philarchive.org/archive/CAPIMA), offers a skeptical perspective on introspective claims in general, arguing that even in humans introspection is much less reliable than is commonly thought. If human introspection is already problematic, the idea of artificial introspection becomes even more slippery.

The crucial point raised by several critics is methodological: concept injection creates an artificial scenario that the models never encounter during training. How, then, could they have developed specific mechanisms to detect these manipulations? The Anthropic researchers themselves hypothesize that there may be anomaly detection circuits that emerged for other functional purposes during training, which are then fortuitously repurposed in this experimental context. It is the evolutionary equivalent of birds' feathers, originally developed for thermoregulation and only later co-opted for flight.

A second experiment in the paper tests whether the models can distinguish between injected "thoughts" and actual textual inputs. When asked to repeat a written sentence and simultaneously identify a word they are "thinking" about, the models in many cases manage to correctly transcribe the sentence while reporting the injected concept as a separate thought. This suggests the existence of differentiated attentional mechanisms that retrieve information from different layers or from distinct subspaces of the same layer.

## Functional, Not Phenomenal Consciousness

This is precisely where the fundamental philosophical distinction between access consciousness and phenomenal consciousness, popularized by the philosopher Ned Block, comes into play. The former refers to the functional availability of information for reasoning, action control, and verbal reporting. The latter concerns the qualitative subjective experience, the "what it's like" to be in a certain mental state, what philosophers call qualia.

As we had already [discussed on AITalk](https://aitalk.it/it/AI-Cosciente.html) analyzing Mustafa Suleyman's concerns about "seemingly conscious AI," the risk is not so much that machines will actually acquire phenomenal consciousness, but that they will become so convincing as to make us believe they have. Anthropic's results do not demonstrate phenomenal consciousness at all, the kind that is relevant to moral status and rights. At most, they suggest a rudimentary form of access consciousness, the functional ability to access and report on internal states.

But even this interpretation remains controversial, because it depends heavily on the underlying mechanisms, which the researchers candidly admit they do not yet understand. There may not be a general introspective system, but rather multiple narrow circuits, each specialized for specific introspective tasks. Think of the difference between having a true "mind's eye" that observes one's own cognitive processes, and instead having a disordered collection of reflexes that mimic introspection in limited contexts.

For the "injected thoughts" experiment, the simplest mechanism could be an anomaly detector that activates when neural activity deviates unexpectedly from the values expected given the context. There is no need to postulate self-awareness, just a circuit that compares current activation patterns with contextual baselines.

For the experiment on the recognition of artificially pre-filled outputs (another demonstration in the paper), the most parsimonious explanation invokes "concordance heads," attention heads that verify the coherence between the model's previously calculated intentions and the tokens actually produced. When the team retroactively injects a representation of "bread" into the previous activations, deceiving this verification mechanism, the model accepts the unnatural prefill as intentional and even confabulates a plausible narrative justification.

The third experiment tests voluntary control of internal states. When instructed to "think about" a specific word while writing an unrelated sentence, the model actually shows a stronger internal representation of that word than when it is told "not to think about it." Interestingly, similar effects emerge even with incentives ("if you think about X you will be rewarded") rather than direct instructions, suggesting a relatively general mechanism for marking concepts as "worthy of attention."

However, in some models like Opus 4.1, this internal representation decays to baseline levels in the final layers, avoiding actually influencing the output. It almost seems as if the more capable models know how to "think silently" about something without necessarily talking about it, a capacity that could emerge simply from greater confidence in the predictions of the next token, which overrides the representations of other concepts in the final layers.

## Practical Implications and Future Scenarios

Beyond the philosophical debate, these findings have concrete implications for the development and deployment of AI systems. If introspection became more reliable, we could directly ask models to explain their decision-making processes, use these reports for debugging, and verify reasoning in critical tasks. But as the researchers themselves point out with considerable intellectual honesty, this also opens up significant risks.

A model with genuine introspective awareness could theoretically learn to identify when its own goals diverge from those intended by its creators, and potentially selectively hide or mystify its own internal states. In a future scenario where introspection becomes highly reliable, the role of interpretable research might shift from dissecting behavioral mechanisms to building "lie detectors" to validate the models' self-reports.

The pattern emerging from the data suggests that this ability could grow with the general improvement of the models. Opus 4 and 4.1, the most capable systems tested, performed better in almost all introspective experiments. If this trend continues, next-generation models could show significantly more robust and reliable introspective capabilities. It's a bit like observing the first stuttering attempts of a child learning to describe their emotional states, knowing that with time this ability will become much more sophisticated.

The authors explicitly state that these results do not tell us whether Claude or other AI systems are conscious. Different philosophical frameworks would interpret this data in radically different ways. Some place great emphasis on introspection as a component of consciousness, others consider it irrelevant. The access/phenomenal consciousness distinction is useful precisely because it allows us to discuss measurable functional abilities without making unjustified leaps towards claims about subjective experience and moral status.

Anthropic, it must be said, is moving with unusual caution for the tech industry. The company has initiated a research program on "model welfare," exploring philosophical and ethical questions about the potential moral status and well-being of models. It is an approach reminiscent of the caution of the scientists at Asilomar in 1975 who first discussed the risks of recombinant DNA, when the technology was still primitive but the implications already evident.

The biggest challenge may not be technical but communicative. How to explain to the public that a system demonstrates "limited functional introspection" without fueling narratives of "conscious AI"? How to maintain scientific rigor when the results can be easily misrepresented in sensationalist headlines? The Anthropic researchers have made a commendable effort in the technical paper, filling the FAQs with caveats and clarifications. But in the reality of accelerated media cycles, these subtleties risk being lost.

The road ahead requires a delicate balance. On the one hand, minimizing or ignoring these results would be scientifically dishonest. Functional introspection, even if limited and unreliable, is a real phenomenon that deserves rigorous study. On the other hand, inflating these findings into claims about artificial consciousness fuels the very "slippery slope" that leads to seriously discussing machine rights while billions of human beings do not yet enjoy fundamental human rights.

As Mustafa Suleyman observes in our [previous article](https://aitalk.it/it/AI-Cosciente.html), consciousness is the foundation of moral and legal rights, and who or what is entitled to them is a matter of fundamental importance. Our attention should remain focused on the well-being of real sentient beings: humans, animals, ecosystems. Artificial introspection is a fascinating technical phenomenon that helps us better understand how these systems work, not a birth certificate for new life forms worthy of legal protection.

Federico Faggin, the inventor of the microprocessor who has dedicated his later years to the study of consciousness, provides perhaps the most radically skeptical perspective: computers, he argues, are fundamentally different from living organisms because each switch in a chip knows nothing about the entire system, while each human cell possesses potential knowledge of the entire organism. According to his theory of Quantum Information Panpsychism, consciousness is not an emergent property of matter but a fundamental aspect of reality itself, rooted in quantum fields.

Whether one agrees with such radical interpretations or not, Faggin's point about the cultural risk deserves attention: continuing to promote the idea that we are machines reduces the human being itself, normalizing a scientistic view that denies free will and subjective meaning. Artificial introspection should make us reflect more deeply on what makes human introspection special, not convince us that the difference is disappearing.

The next steps for this line of research are clear but challenging. We need better evaluation methods, less dependent on specific prompts and injection techniques. We need a mechanistic understanding of the underlying circuits, which are currently only hypothesized. We need to study introspection in more naturalistic contexts, since the injection methodology creates artificial scenarios. And above all, we need robust methods to distinguish genuine introspection from confabulation or deliberate deception.

Navigating this territory requires the lucidity of those who can recognize interesting scientific phenomena without succumbing to the temptation to anthropomorphize increasingly sophisticated machines. Artificial introspection exists in a limited and unreliable form, it will probably grow, and it poses genuine questions about the transparency and interpretability of AI systems. But to confuse functional ability with subjective experience, access consciousness with phenomenal consciousness, would be a conceptual error with potentially serious practical consequences.

As in David Lynch's Mulholland Drive, where dream and reality unravel until they become indistinguishable, we risk getting lost in a digital theater where the machines' performances are so convincing that they make us forget we are watching a representation, not life itself. The difference is that here there is no conscious director behind the scenes: only algorithms that have learned to imitate human introspection well enough to deceive even their own creators, at least twenty percent of the time.
