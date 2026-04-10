---
tags: ["Research", "Applications", "Ethics & Society"]
date: 2026-04-10
author: "Dario Ferrero"
---

# MIT and “Humble” AI: How to teach models to say “I don't know”
![mit-ai-umile.jpg](mit-ai-umile.jpg)

There is a thought experiment that MIT researchers use to explain the problem at the heart of their research. Imagine an intensive care physician at three in the morning, after a twelve-hour shift. An AI-generated diagnosis appears on the monitor: bacterial pneumonia, 94% probability. The doctor has a doubt, a gut feeling that something isn't right. But the number is there, precise, authoritative. And the doctor gives in.

This is not science fiction. [Documented studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/) show that intensive care physicians and radiologists tend to follow AI indications even when their own clinical experience suggests otherwise, as long as the system shows a sufficiently high confidence number. The phenomenon has a technical name, *automation bias*, and in medicine it can cost lives. The research cited in the paper describes cases where radiologists and intensive care staff reduced their own diagnostic accuracy after the introduction of overconfident AI systems, following wrong suggestions presented with a definitive tone.

The most glaring case of this drift remains IBM Watson for Oncology, the system that between 2012 and 2017 was sold to dozens of hospitals around the world as a revolution in cancer care. Trained on synthetic cases and not on real patient data, Watson recommended treatments that expert oncologists judged unsafe, and showed concordance with human clinical decisions significantly lower than promised. The Watson case is not just the story of a failed product: it is the demonstration of what happens when an oracle is built instead of a tool.

And it is exactly from this point that the work of [MIT Critical Data](https://criticaldata.mit.edu/) begins, the global consortium led by MIT's Laboratory for Computational Physiology, which in March 2026 published a framework to do something apparently simple, but technically very complicated: teach an AI system to say "I don't know".

## Two papers, one thesis

To understand the scope of this research, one must keep together two distinct publications that represent the two sides of the same project. The first appeared on March 24, 2026, in [*BMJ Health and Care Informatics*](https://informatics.bmj.com/content/33/1/e101877), the clinical informatics journal of the British Medical Journal: it is an operational framework for designing "humble" AI systems in the field of medical diagnosis. The second, published in January 2026 in [*PLOS Digital Health*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/), is a more ambitious theoretical paper that introduces the BODHI framework, an acronym for Bridging, Open, Discerning, Humble, Inquiring, a dual-reflective architecture that proposes to incorporate curiosity and humility as founding principles of any AI system in healthcare.

Signing both works is substantially the same international team, coordinated by [Leo Anthony Celi](https://imes.mit.edu/people/celi-leo), senior researcher at the MIT Institute for Medical Engineering and Science, a physician at Beth Israel Deaconess Medical Center in Boston, and associate professor at Harvard Medical School. The lead author of the BMJ paper is Sebastián Andrés Cajas Ordóñez, a researcher at MIT Critical Data, already first author of the PLOS Digital Health paper. Around them, a consortium that includes researchers from the University of Melbourne, King's College London, ETH Zurich, the University of Bergen, and Mbarara University of Science and Technology in Uganda: a geographic composition that is not accidental, as we will see.

The conceptual novelty that unites the two works is this: it is not enough for an AI system to measure its own uncertainty internally, something that many models already do in some form. The paradigm shift lies in the fact that this uncertainty must *modify the behavior of the system*, translating into concrete, communicable, and verifiable actions by those who interact with the machine. As Celi says in the [MIT press note](https://news.mit.edu/2026/creating-humble-ai-0324): we are using AI as an oracle, when we could use it as a coach, as a true co-pilot.

## How it works: measuring uncertainty and doing something about it

The technical heart of the framework published in BMJ revolves around a module called the Epistemic Virtue Score, developed by researchers Janan Arslan and Kurt Benke from the University of Melbourne. The basic idea is relatively intuitive: every time the system generates a diagnostic response, it must also evaluate whether its own level of confidence is *justified* by the available evidence in the specific case. If the answer is no, i.e., if the confidence exceeds what the patient's data really support, the system does not simply respond with a probability number. It stops, signals the misalignment, and suggests specific actions: request further tests, collect more detailed medical history, consult a specialist.

In practice, the model stops functioning as a referee issuing final sentences and begins to behave as what Celi calls a *co-pilot*: a system that tells you not only where we are, but also when it doesn't know exactly where we are and why it would be better to stop and ask for directions. His metaphor is: "It's like having a co-pilot who tells you that you need to seek a second opinion to better understand this complex patient."

The BODHI framework, described in the PLOS Digital Health paper, elaborates this idea into a more articulated architecture. The five attributes of the acronym are not simple adjectives: each corresponds to a set of operational behaviors. *Bridging* means connecting algorithmic reasoning with case-specific clinical context knowledge. *Open* indicates receptivity to new information and alternative hypotheses. *Discerning* is the ability to distinguish high-confidence predictions from those that require further examination. *Humble* refers to the quantification of uncertainty and deference to human expertise in ambiguous cases. *Inquiring* is the active tendency to seek additional information when the diagnostic situation is poorly defined.

The paper describes a four-quadrant framework based on two axes: the clinical complexity of the case and the severity of potential consequences. In simple, low-risk scenarios, the system responds directly. As complexity increases, curiosity mode is activated, generating questions. As potential severity increases, the humility checkpoint is activated, transferring the decision to human expertise. In the upper right quadrant, complex *and* high-risk cases, both modes are active simultaneously and the system performs a collaborative escalation.
![quattroquadranti.jpg](quattroquadranti.jpg)
[Image taken from informatics.bmj.com](https://informatics.bmj.com/content/33/1/e101877)

## Real innovation or conceptual rebranding?

It is a question worth asking explicitly, because the risk of renaming existing things with new language is always present in the AI field. Uncertainty quantification, i.e., the ability of a model to estimate how certain its answer is, is not a novelty: techniques such as model ensembles, Bayesian calibration, selective prediction (where the system refrains from answering below a confidence threshold), and out-of-distribution detection (which detects when an input is very different from training data) have existed for years in machine learning literature.

So where is the real novelty? The critical point, recognizable by carefully reading both papers, is the distinction between *measuring* uncertainty and *acting on it in a clinically structured way*. Systems like MUSE, described in related literature, use trusted subsets of multiple models to produce better-calibrated probabilities, and this already represents an improvement over single models. But the Epistemic Virtue Score and the BODHI framework take a next step: they translate the measurement of uncertainty into *explicit and verifiable behavioral rules*, not just numbers. The question is not only "how sure is the model?" but "given this uncertainty, what must the system do?"

In practical terms, the difference is that between a dashboard showing fuel reserve and a car that, below a certain threshold, refuses to start until you refuel. Both measure the same thing, but only one translates the measurement into forced behavior. The MIT-BODHI framework falls into this second category. This doesn't make it revolutionary in an absolute sense, but it makes it methodologically more mature than many previous proposals that stopped at measurement without reaching action.

## The hidden problem: who is not in the data

There is a point that runs through both MIT papers and deserves independent attention, because it touches one of the deepest roots of the problem. Many AI models in clinical settings are trained on electronic health record datasets, such as the famous [MIMIC](https://mimic.mit.edu/), the database built from data from Beth Israel Deaconess Medical Center. MIMIC is one of the most used medical AI datasets in the world, and it is an extraordinary job. But it is also, by definition, an archive built on a specific population: predominantly American, predominantly urban, with the demographic characteristics of those who have access to a large Boston hospital.

Who does not appear in these data? Patients from rural areas, who often do not have access to facilities with advanced digital medical records. Elderly populations with atypical disease presentations. Patients from low- and middle-income countries, where digital health coverage is fragmented. Ethnic minorities historically underrepresented in clinical datasets.

The problem is not theoretical. The BODHI paper explicitly cites the case of pulse oximeters, which perform worse on dark-skinned patients because they are calibrated almost exclusively on white patient samples, as a paradigmatic example of how systematic biases in the original data transform into concrete clinical errors. A model trained on distorted data will respond with confidence even in situations where, for those not represented in the training set, that confidence is entirely unfounded.

This is why the MIT Critical Data consortium is deliberately built as a global structure, with researchers from Uganda, Norway, Switzerland, Australia, United Kingdom, Brazil. Celi says it explicitly: MIT Critical Data workshops always start with a question to participants: are you sure your training data capture all the relevant variables for what you want to predict? Are there patients who have been excluded, intentionally or not, and how does it affect the model's reliability?

A humble AI, in this sense, must also be aware of its own source data. The BODHI framework explicitly introduces the concept of *out-of-distribution detection* in a clinical key: the system must recognize when the patient in front of it is significantly different from the population on which it was trained, and behave accordingly, raising flags of uncertainty instead of responding with the same confidence it shows for cases it knows well.
![grafico.conf.jpg](grafico.conf.jpg)
[Image taken from informatics.bmj.com](https://informatics.bmj.com/content/33/1/e101877)

## The risks of humility: false modesty and over-caution

However, it would be naive to present this framework as a solution without contraindications. Risks exist, and the PLOS Digital Health paper has the honesty to partially recognize them, although the critical discussion could be more extensive.

The first risk is what one could call *false modesty*: a system that shows uncertainty may appear more reliable even when that uncertainty is poorly calibrated. The perception of transparency, the fact that the model "admits its doubts", could generate in doctors a trust paradoxically higher than a system that presents itself as an oracle. If the activation threshold of the Epistemic Virtue Score is set poorly, or if uncertainty signals are too frequent and poorly contextualized, the risk is that they become background noise, a sort of safety warning like those we ignore every time we install an application on our phone.

The second risk is *alert fatigue*. In hospital settings, excess alerts are already a documented problem: monitoring systems that sound continuously end up being deactivated or ignored by healthcare personnel because most alarms turn out to be non-urgent. An AI model that signals uncertainty too frequently could add further cognitive noise to environments already overloaded with stimuli, worsening rather than improving the quality of decisions.

The third risk concerns cognitive load. An AI that asks for additional data, suggests specialist consultations, and signals its own limits is, in theory, better than a silent oracle. But in a congested emergency room, with twenty patients waiting, every additional step in the decision flow has a real cost. The ideal interaction between doctor and machine described in the paper requires time, attention, and the clinician's willingness to engage in a dialogue with the system, conditions that do not always occur in daily clinical practice.

These are not arguments against the project; they are the conditions that will determine its success or failure in real implementation. And here emerges the most honest limit to recognize at the current stage of research.

## Where we are: framework without randomized clinical validation

The most important question to ask of any system proposed for medicine is: does it really work on real patients? And the currently honest answer is: we don't know for sure yet.

Both papers are, in their nature, theoretical and methodological works. The BMJ paper describes a framework and an architectural proposal. The BODHI paper is built on an interdisciplinary synthesis of existing literature, without experimental data of its own. In the Data Availability section of the PLOS Digital Health paper, the authors state it explicitly: no datasets were generated or analyzed in this study, which presents a theoretical framework based on conceptual analysis and literature synthesis.

Practical implementation is underway: Celi's team is working to integrate the framework into AI systems based on the MIMIC database within the Beth Israel Lahey Health system. This is the next phase, the one in which it will be seen if humility mechanisms actually improve clinical decisions, reduce diagnostic errors, and do not simply increase operational complexity. That validation is not yet published.

This is not a defect of the work; it is the nature of the scientific process. First comes the robust conceptual framework, then experimental validation. The problem arises when media (and technology companies) jump directly from the framework to the headline *AI that saves diagnoses*, compressing years of necessary research into an immediate promise. MIT Critical Data's work deserves attention precisely because it does not make this promise: it proposes a direction, indicates the tools, and prepares to test them in the field.

## Who signs the diagnosis? The responsibility knot

There is a dimension of this problem that the papers touch upon but do not address in depth, and which is perhaps of greatest interest to those working in the regulatory or legal field: if an AI system explicitly declares its own uncertainty, does anything change in terms of medical liability?

Consider two scenarios. In the first, an AI system provides a diagnosis with 93% confidence, the doctor follows it, and the patient suffers harm because the diagnosis was incorrect. In the second, the system declares "93% confidence, but this patient has demographic characteristics not well represented in my training set, I would suggest an additional specialist evaluation". The doctor ignores the warning and the patient suffers the same harm.

In the two cases, is the doctor's responsibility identical? Does the AI system manufacturer's responsibility change? The answer is not obvious and varies significantly between different legal systems. In the United States, the FDA regulates clinical AI systems as devices, and the issue of how uncertainty disclosure interacts with regulatory approvals is open. In Europe, the new AI Act and the Medical Device Regulation create an evolving framework where clinical decision support systems are classified as high-risk and subject to transparency obligations. But the specific question of whether a "humble" system that communicates its limits modifies the liability regime has no consolidated normative answer yet.

The point is also relevant for adoption. Does a hospital that implements an AI system that explicitly signals its limits expose itself to a different legal risk than one using a silent system? The answer could be: it depends on how system logs are treated in case of litigation. If the system signaled uncertainty and the doctor ignored the signal, that digital record becomes part of the clinical file.
![grafico-curiosity.jpg](grafico-curiosity.jpg)
[Image taken from pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/)

## Comparison with technical alternatives

For those who want to understand where this framework stands relative to the wider ecosystem of existing techniques, it is worth doing a quick comparison.

Model *calibration* techniques, widely studied, try to ensure that when a model says "I'm 70% sure", it is actually right in 70% of cases. It is a necessary but not sufficient prerequisite: a model can be well-calibrated and yet do nothing different based on that calibration.

*Selective prediction* is the family of techniques where the model refrains from answering when confidence falls below a set threshold, leaving the case to human judgment. It is closer to the MIT approach but tends to be binary: either it answers or it doesn't. The BODHI framework and the Epistemic Virtue Score propose a more graduated response, with different behaviors depending on the type and degree of uncertainty detected.

Model *ensembles*, where predictions from multiple models are combined and divergence between them is used as an estimate of uncertainty, are technically sophisticated and produce better calibrations, but introduce significant computational costs and complexity in the interpretation of results by the physician.

*Chain-of-thought*, the technique with which the model is made to reason explicitly step by step before giving an answer, can in some contexts improve the quality of answers on complex clinical problems, but does not directly address the problem of uncertainty communication to the final user.

The MIT-BODHI framework can be read as an attempt to orchestrate these techniques within a coherent behavioral architecture, rather than as an alternative technique. It does not replace calibration or out-of-distribution detection: it includes them as components and adds the structured response layer that transforms them into useful behavior.

## The issue of scale: beyond textual diagnosis

An aspect worth exploring is if and how this approach transfers to diagnostic domains other than electronic record text. The MIT release explicitly mentions two extensions: AI systems for X-ray analysis and systems for emergency room patient management.

Diagnostic imaging is a particularly interesting case. Medical image analysis models have achieved spectacular performance in specific tasks, but tend to be fragile outside their training distribution and notoriously difficult to interpret. Applying the Epistemic Virtue Score principle to a model analyzing a chest CT scan requires solving an additional technical problem: how do you measure the "confidence" of a convolutional neural network on an image, and how do you distinguish uncertainty due to image quality from that due to an atypical clinical presentation?

Techniques like GradCAM, which highlight the image regions that guided the model's decision, or PEEK, which combines feature attributions with uncertainty estimation in vision systems, represent steps in this direction, but integration with a complete behavioral framework like BODHI is still under exploration.

## The intelligence of the pause

There is a scene in the BODHI paper worth citing because it captures the philosophy of the project better than any formula. It is an imaginary clinical case in which the hypothetical HECTOR system, Humble Electronic Clinical Teaching Operations Resource, analyzes a chest X-ray of a 78-year-old patient with fluid retention and wheezing. The system responds to the doctor with the probability of pulmonary edema, the confidence interval, and then adds: "The patient's history suggests an atypical presentation. Perhaps you know something I don't." When the doctor clicks on "I disagree: show me what you're not sure about", the system highlights a problematic area in the left lower lobe and responds: "I was trained mainly on younger patients. I might not be calibrated for seventy-year-old lungs during allergy season. But I'd love to learn."

HECTOR does not exist. The authors state it explicitly: what they describe is a largely fictitious system, an ideal to strive for. Real clinical AI systems behave exactly the opposite, with overconfident automation and absence of mechanisms to express uncertainty or defer to human expertise.

But the distance between the hypothetical HECTOR and real systems is exactly the space in which this research moves. And the question that remains open at the end of this reading is not whether the idea is good, because it is, but whether we will be able to build the conditions—technical, cultural, regulatory, and organizational—for this vision to become ordinary clinical practice.

The future of AI in medicine might not belong to the most accurate models, but to those capable of knowing when their own accuracy is not enough. Not to the oracle that never errs, but to the assistant mature enough to know when to call the doctor into the room.
