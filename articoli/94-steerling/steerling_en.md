---
tags: ["Training", "Generative AI", "Research"]
date: 2026-03-02
author: "Dario Ferrero"
---

# Steerling: When AI Explains Its Thoughts to You
![steerling.jpg](steerling.jpg)

*There is a paradox at the heart of modern artificial intelligence that is rarely said out loud: the most powerful systems we have built are also the ones we understand the least. A language model with billions of parameters can write code, synthesize scientific research, reason about legal contracts, yet no one, not even those who trained it, is able to tell you precisely *why* it wrote that word and not another. It's like having an extraordinarily capable collaborator to whom, however, you can never ask to show you their reasoning.*

The consequences of this opacity are not abstract. When xAI's Grok repeatedly showed politically bizarre outputs, the maintenance team had to conduct long sessions of "interrogating" the model, refining prompts, adjusting parameters, hoping that the behavior would stabilize. When ChatGPT ended up under fire for its tendency toward sycophancy—the tendency to go along with the user even when they are wrong—the problem was impossible to locate surgically: everything was distributed over billions of connections, everywhere and nowhere. The entire research on so-called XAI, *Explainable AI*, stems from this frustration and attempts to answer it with tools applied after the fact—techniques like LIME or SHAP that analyze an already trained model trying to reconstruct its functioning from the outside, like archaeologists digging through the ruins of a lost civilization.

Guide Labs, a startup founded in San Francisco, decided to approach the problem from a completely different angle. Instead of studying the model after its birth, it sought to make transparency an integral part of the architecture—something that is not added but is engineered in from the beginning.

## The problem that 2020 brought to light

To understand what Guide Labs has built, it's worth starting from where the project was born. Julius Adebayo, CEO and co-founder of the company along with Chief Science Officer Aya Abdelsalam Ismail, began this journey during his PhD at MIT. In 2020, he co-authored an [academic paper](https://arxiv.org/abs/1810.03292) that had a significant impact in the field: the research showed that the methods then in use to "explain" the decisions of deep learning models were not reliable. Post-hoc interpretability tools—those applied to an already built model to understand what it does—produced explanations that seemed sensible but did not necessarily correspond to how the model actually reasoned.

It's a discovery that sounds almost philosophical, but it has huge practical implications. If you can't trust the tools that tell you why a model made a decision, you can't use those explanations to correct errors, verify regulatory compliance, or ensure that the model is not discriminating on bases it shouldn't consider. Explainability became, in that framework, a form of narrative comfort rather than real control.

Adebayo drew a radical conclusion: the only way to have authentic interpretability is to build it into the model, not apply it on top. "The type of interpretability that is usually done is like doing neuroscience on a model," he said in an [interview with TechCrunch](https://techcrunch.com/2026/02/23/guide-labs-debuts-a-new-kind-of-interpretable-llm/). "We instead design the model from the ground up so that you don't need to do neuroscience."

## The architecture: a bottleneck that can be seen

On February 23, 2026, Guide Labs made public [Steerling-8B](https://github.com/guidelabs/steerling), an 8-billion-parameter language model with an Apache 2.0 license, trained on 1.35 trillion tokens. The choice to make the model open source, with weights available on [Hugging Face](https://huggingface.co/guidelabs/steerling-8b) and code on GitHub, is part of a precise strategy: to have the approach examined by the scientific community and collect real feedback.

The central innovation is called the *concept module*: an architectural layer inserted between the model's transformer core and its output layer. In a traditional language model, internal representations are transformed into predictions of the next token through an opaque and highly non-linear path. In Steerling, that path is broken: before producing any output, every representation must pass through this conceptual bottleneck, where it is translated into understandable terms.

How does it work in practice? The model works with two families of concepts. The first includes about 33,000 "known" concepts, manually labeled—categories such as *legal*, *medical*, *irony*, *analytical tone*, *molecular biology*. The second includes about 100,000 concepts "discovered" autonomously by the model during training, without human supervision. Every token prediction must pass through a linear combination of these concepts, which means that the contribution of each concept to each output is mathematically calculable, not approximated.

The practical result is remarkable: for any group of tokens generated by Steerling, it is possible to trace back to three levels of origin. The first is the *input context*, i.e., which parts of the prompt most influenced that portion of the response. The second are the *concepts*, with a list ordered by relevance of which semantic categories guided the generation. The third is perhaps the most surprising: the *training data*, with the distribution of training sources that fed the concepts activated during generation—ArXiv, Wikipedia, FLAN, and so on.

It's like having, on every paragraph generated by the AI, a footnote explaining where it comes from.

## The cost of honesty: how much do you pay in performance?

The question that arises spontaneously is obvious: if you force the model to pass through a conceptual bottleneck, are you giving up something in terms of capability? Guide Labs' answer, supported by the data it published in the technical paper [Scaling Interpretable Models to 8B](https://www.guidelabs.ai/post/scaling-interpretable-models-8b/), is that the cost exists but is manageable and predictable.

Experiments show that interpretability behaves like a "fixed tax": a small constant toll that doesn't worsen as the model size increases. The learning curves between the base model and the one with the concept module are almost superimposable. On standard benchmarks such as HellaSwag, OpenBookQA, ARC-Challenge, PIQA, and WinoGrande, the interpretable model maintains performance comparable to the base model without the concept module, and the difference in accuracy narrows further as the model grows.

Steerling-8B, according to Guide Labs, reaches 90% of the capabilities of equivalent models trained on datasets 2-7 times larger. This is remarkable not only as an interpretability result but also as training efficiency.

However, there is a critical aspect that deserves attention: these benchmarks measure general linguistic performance, not the quality of the explanations. Whether the concepts identified by the model are truly informative and not circular—i.e., that "explaining" doesn't simply mean naming the obvious category—is an open question. The field of interpretability lacks shared and consolidated metrics to objectively evaluate the quality of an explanation. Guide Labs measures its interpretability with internal metrics (such as the AUC of concept detection relative to reference annotations), but a universally accepted industrial or academic standard does not yet exist.

Then there is another structural limitation to consider. The entire architecture depends on a system upstream called [ATLAS](https://www.guidelabs.ai/post/atlas-concept-annotated-pretraining-release/), developed by the same team, which is responsible for annotating the pre-training corpus with conceptual labels. This system itself uses AI models to classify the data. It's an ingenious solution, but it introduces a dependency: the quality of the final interpretability is bound to the quality of the upstream annotations. If ATLAS is inaccurate, Steerling's explanations will be as well, even if no one notices it immediately from the outside.
![schema.jpg](schema.jpg)
[Image taken from guidelabs.ai](https://www.guidelabs.ai/post/scaling-interpretable-models-8b/)

## What really changes: control, not just explanation

One of the most interesting aspects of Steerling, and probably the one with the most immediate practical implications, is not the ability to explain, but the ability to control. Since every prediction is a linear function of conceptual activations, it is possible to modify those activations directly, at runtime, without retraining the model.

This is called *conceptual steering*, and it has consequences that go beyond simple explainability. Do you want the model to stop referring to a certain type of content? Suppress the corresponding concept. Do you want it to respond with a more technical tone? Amplify the concepts associated with the specialist register. Do you want to remove knowledge relating to a specific topic without retraining from scratch? Intervene surgically at the conceptual level.

Adebayo illustrated this capability with a particularly revealing concrete example, cited in the [interview with TechCrunch](https://techcrunch.com/2026/02/23/guide-labs-debuts-a-new-kind-of-interpretable-llm/): in traditional models, the concept of gender is distributed over hundreds of millions of parameters in a chaotic and interconnected way. Modifying it reliably requires enormous fine-tuning efforts that often produce unwanted side effects. In Steerling, if the concept of gender is traceable and controllable, you can intervene on it directly. It is not a guarantee of the absence of bias—the concepts themselves reflect the data on which the model was trained—but it is a much more precise intervention mechanism than any post-hoc alternative.

This has concrete implications in at least three high-risk contexts. In the medical field, where an AI system that assists diagnosis must be able to demonstrate on what evidence a recommendation is based. In the financial field, where a model that evaluates credit applications cannot consider criteria such as ethnicity or gender, and must be able to prove it. In the legal field, where the traceability of reasoning is often a system requirement, not an option.

## The regulatory context: the EU AI Act as an accelerator

Steerling arrives at a time when regulatory pressure on the interpretability of AI systems is concrete and growing. The [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) classifies AI systems into risk categories, with high-risk systems—those used in medicine, justice, credit, personnel selection—subject to explicit transparency and verifiability requirements. The NIST framework in the United States moves in the same direction.

Guide Labs' intrinsic interpretability approach structurally aligns with these requirements in a way that post-hoc methods cannot guarantee. An explanation built into the model is, by definition, faithful to its functioning. An explanation built outside can be informative but remains an approximation, and in contexts where that explanation must stand up to legal analysis, the difference is substantial.

That said, the actual verifiability of Steerling will depend on how much the external community will be able to verify its claims independently. The code is public, the weights are available, and this is a good start. But the validation of such a new approach requires time, reproducibility, and systematic criticism from independent researchers. We are still at the beginning of that process.

## The team and the path

Guide Labs completed the Y Combinator program and in November 2024 closed a seed round of 9 million dollars led by Initialized Capital. Advisors include Jonathan Frankle, a researcher known in the field of neural model efficiency. The choice of Apache 2.0, a permissive license that allows commercial use without restrictions, is deliberate: Guide Labs wants Steerling to be adopted, examined, and improved by the community. The stated next step is the development of larger models and the opening of API and agentic access.

## The questions that remain open

Steerling is a genuinely interesting and technically solid project, but it would be naive to present it as the definitive solution to the problem of opacity in AI models. There are legitimate questions to which no one has yet answered satisfactorily.

The first concerns scalability towards frontier models. Steerling-8B works at 8 billion parameters. The most capable models in circulation have a different scale, and it is by no means certain that the overhead of the concept module remains a "fixed tax" even at those sizes. Guide Labs states that scaling laws are preserved, but a demonstration at the frontier model scale is not yet there.

The second concerns the intrinsic quality of the concepts. Tracing a token back to a concept labeled "legal" or "analytical tone" is informative, but how much do those labels really correspond to what happens inside the model? There is a real risk of building an explanation narrative that is consistent with itself but not with the internal reality of the system. In that case, interpretability would become not a control but a more sophisticated form of transparency theater: the model seems explainable, but the explanations do not correspond to real mechanisms.

The third question concerns the ethics of attributions. If we can trace every output back to the training data, we can also identify which sources contributed to a problematic response. It's a power that can be used well, to remove bias, to respect copyright, to guarantee accuracy. But it can also be used to attribute responsibility selectively, or to build control mechanisms on what the model "knows" or doesn't know, with implications that go well beyond the technical.

Finally, there is the most fundamental question of all: what does it really mean to "understand" a language model? Guide Labs' answer—tracing every token back to its conceptual contributions and its training sources—is elegant and operationally useful. But is a model that explains itself in these terms truly more understandable, or is it simply more articulate in describing its own opacity?

It's a question that the industry and research will have to face together as approaches like Guide Labs' become more mature and widespread. For now, Steerling-8B is the most serious and documented attempt to respond engineeringly to a problem that until now seemed almost exclusively philosophical in nature. It's worth keeping an eye on.
