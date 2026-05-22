---
tags: ["Research", "Ethics & Society", "Training"]
date: 2026-05-15
author: "Dario Ferrero"
---

# Talkie: When an LLM Knows Nothing After 1930
![talkie-vintage-llm.jpg](talkie-vintage-llm.jpg)

*There is a thought experiment that Demis Hassabis, founder of DeepMind, has launched on several occasions as an intellectual provocation: if you trained a language model on the entire scientific corpus available up to 1911, would it manage to independently rediscover General Relativity, which Einstein would formulate four years later? The question is not rhetorical. It is one of the most difficult that can be asked about artificial intelligence, because it touches on the problem of true generalization, the kind that goes beyond the retrieval of memorized patterns and approaches something we might call, with great caution, reasoning.*

It is from this tension that Talkie was born, a project presented in April 2026 by Nick Levine, David Duvenaud, and Alec Radford, the latter known for contributing to the development of GPT-2 at OpenAI. The idea is simple to state and complicated to execute: train a thirteen-billion-parameter language model using exclusively texts published before December 31, 1930, then study its behavior like studying a sample in a laboratory, in a controlled environment isolated from any contemporary contamination.

The result is called [talkie-1930-13b](https://huggingface.co/talkie-lm/talkie-1930-13b-it), and it is publicly available on Hugging Face. But before talking about what it does, it's worth understanding why it exists.

## Not Nostalgia, but Methodology

The greatest risk with a project like this is reading it as a curiosity, a cultural toy, the digital equivalent of a gramophone. That would be an error in perspective. Talkie is not a model that competes with Claude, ChatGPT, or Gemini on any practical task. It is a research tool that answers structural questions about the functioning of modern language models, questions that cannot even be properly formulated with general-purpose models.

The central problem is called contamination, and it is one of the most persistent ghosts in the evaluation of artificial intelligence systems. When measuring a model's ability on a benchmark, such as MMLU, HumanEval, or ARC, it is implicitly assumed that the model has not already "seen" the questions or similar answers during pre-training. But this assumption is increasingly fragile: modern corpora include enormous amounts of text from the web, and the web includes forums, solutions, explanations, and even direct copies of the benchmarks themselves. A model that correctly answers a math question might do so because it reasons, or because it has memorized the answer from some corner of Reddit. Distinguishing them is almost impossible when the training corpus is the entire web.

A model trained only on texts from 1930 does not have this problem by design. It cannot have seen Python, because Python did not exist. It cannot have memorized solutions from Stack Overflow, because Stack Overflow did not exist. If it manages to write correct code after seeing a few examples in context, it does so through pure generalization, not retrieval. It is an experimental environment that modern models, by the way they are built, can never offer.

The idea of a "vintage LM" is not completely new: the team itself cites previous projects such as Ranke-4B, Mr. Chatterbox, and Machina Mirabilis as part of a nascent ecosystem. Talkie, however, is the largest in this category and the first to systematically document the methodological challenges that this type of training entails.

## Building an Archive of the Past: 260 Billion Tokens

The first practical question is where to find so much pre-1931 text in digital format. The answer is that most of the work had already been done by others. The Talkie team built their corpus by leaning on the [Institutional Data Initiative](https://huggingface.co/datasets/institutional/institutional-books-1.0), the [Internet Archive](https://archive.org), and the [Common Pile](https://huggingface.co/common-pile) project, aggregating books, newspapers, periodicals, scientific journals, patents, and legal acts in English for a total of 260 billion tokens.

The choice of the cutoff at December 31, 1930, is not arbitrary, nor is it only symbolic. It has a precise legal basis: according to US copyright law, works published before 1926 are in the public domain, and the window extends progressively to 1930 for works of that specific year. The temporal cutoff therefore also resolves the problem of licensing, making the corpus legally distributable without the complications that plague modern datasets.

The choice to limit it to English for this version is pragmatic: the team explicitly states that validating the data pipeline requires deep familiarity with the source documents, and the researchers are native English speakers. Multilingual expansion is indicated as a future priority, both to increase the size of the corpus and to diversify the cultural perspectives represented.

Two hundred and sixty billion tokens seem like a lot, but they must be contextualized: modern general-purpose models are trained on corpora in the order of trillions of tokens, often with multiple passes over the most important data. The team estimates, however, that they can grow their corpus to over a trillion tokens of historical text, an estimate that, if confirmed, would bring the model's capabilities into the range of GPT-3.5, described in the introductory post as "similar in capability to the original ChatGPT."
![identity.jpg](identity.jpg)
[Image taken from the GitHub repository](https://github.com/talkie-lm/talkie)

## The Invisible Enemy: OCR and Systematic Noise

If the corpus is the foundation, its quality is the deepest crack in the building. In 1930, native digital text did not exist: everything that ended up in the Talkie dataset was transcribed from physical sources through optical character recognition, a process that introduces a type of noise radically different from any error present in modern corpora.

Classic OCR systems, those used historically to digitize archives, work well on simple layouts and clean scans. On period newspapers with irregular columns, deteriorated typefaces, and yellowed pages, their accuracy collapses. The Talkie team quantified this problem precisely: training a model on pre-1931 texts transcribed with conventional OCR produces, for equal computational resources, only 30% of the learning efficiency of a model trained on the same transcriptions done by humans. Cleaning with regular expressions recovers some ground, bringing the figure to 70%, but a significant gap remains.

The alternative solution, using modern systems based on large vision models, creates a paradoxical problem: these more accurate systems tend to hallucinate modern facts in the transcribed text, contaminating exactly the corpus one wants to keep pure. The team is developing a specific "vintage" OCR system for this purpose, a model trained to transcribe historical texts without introducing contemporary knowledge.

It is a problem that recalls the situation of the film restorer who must clean a film from the twenties without introducing recognizable digital artifacts: every modern tool leaves traces of itself in the material it touches.

## When the Past Lets the Future Filter Through: The Problem of Temporal Leakage

Even with an apparently circumscribed corpus, the temporal boundary is more porous than it seems. The team identifies several ways through which content later than 1930 can infiltrate the dataset: incorrect date metadata on digitized documents, modern editorial introductions added to reprints of classics, footnotes written by post-war curators, anachronistic insertions in otherwise historical texts.

To address this problem, Talkie uses an anachronism classifier based on document-level n-grams, a tool that identifies statistically improbable word sequences in a pre-1931 corpus and filters suspect documents. The system is not infallible, however: an earlier version of the seven-billion-parameter model clearly showed knowledge of the Roosevelt presidency and the New Deal, both subsequent to the cutoff. The current 13-billion version retains some traces of knowledge relating to World War II, the UN, and the division of Germany—details that could not have come from 1930 texts.

These residues of the future in the model are not just a technical defect: they are a demonstration of how difficult it is, in practice, to build a truly watertight temporal boundary. The team documents them with methodological honesty, citing them as a starting point for future research rather than hiding them, and is developing more advanced classifiers for future versions of the model.
![grafico1.jpg](grafico1.jpg)
[Image taken from the official site talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Instructing a Model Without Using the Present

Once the base model is trained, the next step is to make it useful as an interlocutor, which requires a post-training process—that is, an alignment that transforms the model from a text predictor into a conversationalist capable of following instructions. The problem is that all standard datasets for this process—collections of human-assistant dialogues, annotated preferences, instruction-following benchmarks—are intrinsically modern. Using them would mean contaminating the model with expectations, communication styles, and knowledge from the 21st century.

The team built a post-training pipeline from scratch. The first phase uses historical texts with regular structure as raw material: Victorian etiquette manuals, period cookbooks, dictionaries, encyclopedias, fairy tale collections, epistolary guides. Instruction-response pairs that reflect the communicative conventions of the time are extracted from these texts, and the model is fine-tuned on them. It is like teaching someone good manners using Monsignor Della Casa's etiquette instead of a contemporary corporate communication course.

The second phase is more sophisticated and introduces an interesting conceptual tension. The team uses online Direct Preference Optimization, a technique for preference training, generating synthetic prompts on various types of tasks and using Claude Sonnet 4.6 as a judge to evaluate the quality of Talkie's responses. The average instruction-following score went from 2.0 to 3.4 on a five-point scale during this process. A third phase then uses synthetic conversations generated between Claude Opus 4.6 and Talkie to smooth out residual conversational rough edges.

The problem is that this approach inevitably introduces subtle contamination: a modern model evaluating the responses of a vintage model transfers, even unintentionally, contemporary expectations of what constitutes a good response. An earlier version of the model, after reinforcement learning with AI feedback, had developed the habit of responding in bulleted lists—a style entirely alien to the prose of the 19th and early 20th centuries, but characteristic of modern assistant models. The team explicitly recognizes this limitation and points to the future goal of using their own vintage models as judges, eliminating dependence on contemporary systems.

## What It Knows, What It Doesn't: Comparison with the Modern Twin

To contextualize Talkie's capabilities rigorously, the team trained a "modern twin," an architecturally identical model but trained on FineWeb, one of the main corpora of modern web text. The comparison at equal computational resources shows that Talkie underperforms its contemporary equivalent in standard knowledge evaluations—an expected result openly declared.

What is more interesting is what happens when anachronistic questions are filtered from the benchmarks—those that presuppose knowledge of events, technologies, or concepts posterior to 1930. By eliminating these questions, the performance gap is reduced by approximately half. The vintage model and the modern model show comparable performance on fundamental linguistic understanding and numerical reasoning tasks—capabilities that depend less on the specific content of the corpus and more on the structure of language itself.

The most fascinating test from a theoretical point of view concerns programming. The team administered to Talkie a version of HumanEval, the standard benchmark for evaluating Python code-writing ability, providing the model with a few examples in context but no prior knowledge of Python or modern programming. The results are significantly lower than any model trained on web data, where code is abundant. However, with increasing scales, the model shows constant improvements even on this task—a signal that something resembling generalization is emerging. The problems correctly solved are simple, often single-line, but include cases such as implementing the decoding function of a rotation cipher when only the encoding function is provided, suggesting a rudimentary understanding of the concept of an inverse function.
![grafico2.jpg](grafico2.jpg)
[Image taken from the official site talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Historical Bias and Cultural Responsibility

A model trained exclusively on texts from 1930 necessarily reflects the culture, values, lexicon, and prejudices of that era. This is not a marginal detail: it is a structural feature that the team explicitly recognizes with the note that Talkie "may produce offensive output for users"—a sober formulation to indicate that the corpus includes texts produced in an era of active colonialism, institutionalized racism, systematic exclusion of women from public life, and widespread anti-Semitism in mainstream culture.

This aspect is both an evident application limit and, paradoxically, one of the elements of greatest scientific interest. Studying how these biases manifest in the model's behavior, how they propagate from the corpus to the output, and how they interact with post-training could offer valuable insights into the same dynamic in modern models, where biases are more difficult to isolate because they are drowned in a vast and heterogeneous corpus.

The issue also poses broader questions that the team explicitly raises: how much of what we observe in current language models is a property of human language in general, and how much is instead a specific property of the web as a corpus? Modern models are all, to varying degrees, children of the same digital parent. Building models trained on radically different corpora—such as historical texts, pure scientific texts, or non-English literature—could reveal how much of what we call "emergent behavior" is actually emergent and how much is instead a faithful reflection of the source.

## Where Talkie Stands Relative to Current Research

It is important to place this project honestly within the research landscape. At the time of publication, in April 2026, Talkie's work has not yet passed a formal peer review: it is presented as an introductory post with documented methodology, quantitative data, and public access to the model and code on [GitHub](https://github.com/talkie-lm/talkie), but without the external validation that a paper published in a conference such as NeurIPS or ICML would entail. The reported data, such as the 30% OCR efficiency or the improvement in the DPO score from 2.0 to 3.4, are presented as internal results and should be confirmed by independent replications.

The project receives computational and financial support from Anthropic and Coefficient Giving, and the acknowledgments include prominent names in the field such as John Schulman and Andrej Karpathy—signals of credibility within the research ecosystem. But the road from a public demo to a consolidated methodological contribution is still long.

What can be said with certainty is that the research question is legitimate and important. Benchmark contamination is a documented and growing problem, as evidenced by a [recent paper](https://arxiv.org/abs/2602.12413) cited by the authors themselves. The idea of using models with sharp temporal cutoffs as tools for evaluating generalization is original and methodologically coherent. The project opens a direction; it does not close it.

## A New Research Line, Not an Alternative

Talkie's scaling plan is ambitious: by summer 2026 the team expects to release a model in the range of GPT-3 in capability, and estimates that a corpus of over a trillion historical tokens is sufficient to build something comparable to GPT-3.5. These goals should be read in the context in which they are declared: not as product announcements, but as research horizons that determine the scale of future experiments.

The most interesting ambition, however, is not the numerical one. It is the possibility of building a completely autonomous post-training pipeline, in which vintage models are used as judges of themselves, eliminating dependence on Claude or other modern systems in the evaluation of preferences. If realized, this would allow for a genuinely "period" model not only in the pre-training data but in the entire alignment process—an unprecedented experiment on how the source of training values influences the final behavior of the system.

There is a useful parallelism with certain experiments in computational linguistics in the nineties, when researchers such as Frederick Jelinek at IBM built statistical models of language on strictly controlled corpora—not because they wanted production systems, but because controlled environments reveal mechanisms that large and noisy corpora hide. Talkie fits into this tradition: it uses limitation as an analytical lens.

The answer to Hassabis' question—whether a model stuck in 1911 could rediscover General Relativity—remains open. But Talkie suggests that the way to approach a credible answer is not to speculate, but to build the experiment. Train the model, give it Maxwell's physics and the anomalies in Mercury's orbit, and see what emerges. It's not science fiction: it's the scientific method applied to artificial intelligence, with all the patience and rigor it requires.

---

*The Talkie source code is available on [GitHub](https://github.com/talkie-lm/talkie). The base model and post-trained version are publicly accessible on [Hugging Face](https://huggingface.co/talkie-lm). A conversational demo is available at [talkie-lm.com/chat](https://talkie-lm.com/chat).*
