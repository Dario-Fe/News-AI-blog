---
tags: ["Business", "Ethics & Society", "Security"]
date: 2026-01-09
author: "Dario Ferrero"
---

# 'Artificial Intelligence and Software Engineering: What Companies Must Do'. A Conversation with Enrico Papalini
![papalini-interview.jpg](papalini-interview.jpg)

*Enrico Papalini has a resume that would make many a LinkedIn consultant pale: over twenty years spent building and orchestrating software systems where failure is not an option. As Head of Engineering Excellence and Innovation at Borsa Italiana, part of the Euronext group, he has guided the adoption of artificial intelligence in a context where the word "crash" has implications that go far beyond a runtime bug. Before that, he navigated the industry from various angles: from Microsoft to Intesa Sanpaolo, from tech startups to financial giants, always in the role of someone who has to make things work when everyone else can afford for them not to.*

His [LinkedIn profile](https://www.linkedin.com/in/enricopapalini/) tells the story of a professional trajectory where innovation has always had to marry reliability. He is not an academic theorizing from the outside, nor a founder who can afford the luxury of "move fast and break things." He is someone who has had to answer questions like: "Can we use this technology in a system that processes millions of transactions a day?" The right answer is never an enthusiastic yes or a conservative no, but a "it depends, and let me explain how."

Now Papalini has synthesized this experience into a book that is generating discussion: [*Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*](https://amzn.to/3Z12Ng9), also published in an [English version](https://www.amazon.com/dp/B0G7LPJBTH) titled *Non-Deterministic Software Engineering: How to Build Reliable Software with AI Assistants Without Losing Quality, Security, or Control*. The subtitle is already a manifesto: how to build reliable software with AI assistants without losing quality, security, or control.

## The Broken Silent Pact

While the tech publishing market continues to churn out manuals on "how to use ChatGPT to code faster," Papalini has chosen a completely different angle. His book is based on research conducted by DX on over 180 companies, integrates DORA (DevOps Research and Assessment) metrics adapted for AI-assisted development, and analyzes case studies of those who have already been burned or have found a balance: OpenAI, Shopify, Google. To write it, he engaged in dialogue with some of the heaviest hitters in contemporary software engineering: Martin Fowler, the theorist of design patterns and refactoring; Kent Beck, the inventor of Extreme Programming; Addy Osmani, an engineering manager at Google Cloud.

I ask him to tell me what prompted him to write this particular book, right now, when everyone seems focused on the miraculous speed promised by AI assistants.

"Everyone talks about speed, but the real revolution is something else," Papalini replies. "It's a change in the nature of the tools we use. For forty years, we took one thing for granted: you write some code, and it does exactly what you wrote. Always. It is on this certainty that we have built everything—how we test, how we debug, how we work in teams. Generative AI breaks this silent pact. Not because it's faulty, but because it has a probabilistic nature. You ask it the same thing twice, it gives you different answers. Sometimes brilliant, sometimes wrong with disarming confidence."

The metaphor he uses to frame the problem is illuminating: "Companies that think they can replace programmers with AI and smugly look at how many more lines of code they can produce are missing the point: they are introducing a random variable into the heart of their systems. It's a bit like a civil engineer building a bridge with materials that *might* hold the expected weight. It works great when a few cars pass over it, but when the first truck comes along, it collapses."

He wrote the book, he says, "because it seemed to me that there was a lack of guidance for those who have to navigate this change without crashing, but also without giving up the benefits, which are real."

## From Determinism to Tolerance

The conceptual heart of the book is encapsulated in its English title: *Non-Deterministic Software Engineering*. It is a deliberate oxymoron. Software engineering, by definition, has always been the art of building deterministic systems: input A always produces output B. Papalini is proposing that we welcome into our processes tools that, by their nature, do not respect this fundamental rule.

I ask him how the paradigm of quality control changes when we move from a world where code did exactly what was written, to a world where we welcome probabilistic systems into our IDEs.

"Everything changes, and at the same time, nothing changes. I know, it sounds like a paradox," he begins. "Everything changes because 'it works' no longer means 'it's correct.' AI-generated code compiles, passes the tests you've written, and looks professional. But it could hide vulnerabilities, handle edge cases poorly, or be written in a way that no one will understand in six months. Nothing changes because the fundamentals of software engineering remain the same: testing, reviews, design thinking. In fact, they become more important than ever."

The key, according to Papalini, lies in adopting an approach that has so far been foreign to software developers: "The real novelty is that we have to learn to think in terms of 'tolerances.' Martin Fowler often uses this analogy: his wife is a structural engineer, and she never designs to the exact limit. She always calculates a safety margin. We developers have never had to do that because our 'materials' were perfectly predictable. Now they are not. And those who don't build these margins will, sooner or later, see their 'bridge' collapse."

It's a radical change in mindset for an entire profession that has built its identity on the absolute certainty of execution. Like telling a Swiss watchmaker that from now on, they will have to accept that their watches may have a variable margin of error.

## The Illusion of Speed

One of the most counterintuitive passages in the book concerns productivity data. Papalini cites a study by METR (an independent organization that evaluates the capabilities of AI systems) which shows that developers can feel 20% faster with artificial intelligence, while real tests on measurable tasks indicate that in some cases, they are 19% slower.

I ask him how this perceptual discrepancy is possible, and above all, how companies can measure true productivity without falling for the marketing of the tools.

"You know what struck me most about that study? It wasn't the data showing that with AI they were 19% slower. It was that the developers *believed* they were faster. And they continued to believe it even after seeing the results," Papalini recounts. "Why does this happen? Because AI reduces *perceived* effort. You feel more fluid, less stuck. It's like having a colleague who is always available to help, who doesn't judge you, and doesn't make you wait. Psychologically, it's powerful. But 'I feel productive' and 'I am producing value' are two very different things."

The solution he proposes is not philosophical but methodological: "To avoid falling for the hype, a company should establish a baseline *before* adopting the tools. Without a 'before,' you can never prove an 'after.' When the CEO asks what AI has brought, you need numbers, not feelings. But the numbers must be the right ones: stop measuring lines of code or how many AI suggestions are accepted. Measure what matters: features released, bugs in production, time to resolve incidents. And one fundamental thing: measure how motivated your developers remain."

It's a call for engineering discipline in a time of collective euphoria. Like in the early days of Agile methodologies, when everyone measured "velocity" in story points without asking if they were actually delivering value.

## Monday Morning, Three Moves

The Italian subtitle of the book asks a direct question: "What must companies do." Not "what could they do" or "what would be nice to do," but "what they must do." It's an imperative, and it implies urgency.

I ask Papalini to be even more direct: if he had to point out the first three concrete actions a CTO or CEO should take on Monday morning to avoid being overwhelmed, what would they be?

"The first is to conduct an audit of what is *already* happening," he replies without hesitation. "I guarantee you: your developers are already using ChatGPT, Copilot, Claude, whether you know it or not. Not out of malice, but simply because these tools work. Before writing policies, understand the real situation."

This phenomenon of Shadow AI, the unauthorized use of intelligent tools, is one of the recurring themes in the book. It's not a problem of indiscipline but of necessity: when official tools are slow to be approved or too limited, people find alternatives.

"The second is to draw a clear line between exploration and production," Papalini continues. "Rapid prototyping, experiments, proofs of concept—all legitimate. But it must be *clear* that this code does not go into production without a conscious rewrite. The classic disaster is the Friday prototype that becomes the Monday critical system because 'it works anyway'."

It's the pattern that anyone who has worked in a startup recognizes immediately: the demo becomes the product, the workaround becomes the architecture, the temporary becomes permanent. With AI, this process accelerates dangerously because generating a convincing prototype is a matter of minutes.

"The third is to invest in review capability, not in generation capability," he concludes. "The bottleneck is no longer writing code, but understanding, validating, and maintaining it. If your developers can generate ten times more code but the review capacity remains the same, you're just accumulating technical debt faster."

## The "It Works" Trap

Andrej Karpathy, one of the pioneers of modern AI and former Director of AI at Tesla, popularized the term "vibe coding": programming by following the intuition of the moment, letting the AI suggest directions that "feel right." It is a fascinating and profoundly dangerous approach.

Papalini dedicates several pages of the book to what he calls the "It Works Trap." I ask him to tell me about the long-term risks for a corporate codebase written primarily by following the vibe of the moment without rigorous human validation.

"Let me tell you a story," he begins. "Martin Fowler had used AI to generate a visualization in SVG vector format, nothing complex. It worked perfectly. Then he wanted to make a trivial change: move a label a few pixels. He opened the file and found what he called 'crazy stuff'—code that worked, yes, but was structured in a completely alien way, impossible to touch without breaking everything. The only option? Throw it away and regenerate it from scratch."

The anecdote perfectly captures the problem: "This is the real cost and risk of vibe coding on a corporate scale. You create systems that *work* but that *no one understands*. And corporate software has to live for years, sometimes decades. It has to be modified, extended, debugged at three in the morning when something explodes."

The solution he proposes is simple in its formulation but requires discipline in its execution: "The rule we must follow is simple: never commit code that you can't explain to a colleague. If it's generated with AI and I don't understand how it works, it's not ready for production."

It's like the digital equivalent of the mountaineers' rule: don't climb anything you don't know how to get down from.

## The Price of Unreliability

In the book, Papalini introduces the concept of the "unreliability tax." It is a hidden but measurable cost of using generative systems in code production. I ask him to quantify, in concrete terms of security and maintenance, how much it really costs a company to clean up AI-generated code that seems correct but hides vulnerabilities.

"The numbers are sobering," he begins. "Research shows that a significant percentage of AI-generated code contains vulnerabilities, some sources say almost half. And the insidious thing is that they are 'plausible' vulnerabilities: the code looks professional, it uses recognizable patterns. It's just that it's missing input validation at that critical point, or it uses a deprecated cryptographic function."

These are not obvious errors that any linter would flag. They are errors of judgment, seemingly reasonable choices that in specific contexts become security holes: "The direct cost is the remediation time. But the real cost is what you don't see right away: the vulnerability that goes unnoticed for months, until someone finds it. At that point, you're not paying for development hours, you're paying for incident response, potential data breaches, reputational damage."

Papalini also identifies a more subtle cost: "There is also a subtler tax: the loss of trust in the system. When the team starts to distrust its own code, everything slows down. Every change becomes a risk. And the same goes for customers: there's a risk they will switch to a more reliable competitor."

His recommendation is pragmatic: "The sensible investment is in prevention: automatic security scanning, targeted training, mandatory human review for anything that touches authentication or sensitive data. It costs less than cleaning up disasters afterward and losing customers."

## The Sovereignty Question

One of the densest chapters of the book addresses the theme of data sovereignty and security in the age of AI assistants. Companies face a triple challenge: protecting intellectual property from vendor lock-in, preventing Shadow AI, and mitigating what Papalini calls the "Security Debt" of probabilistic code.

I pose a complex question to him: between the speed of cloud models and the complexity of on-premise open source, what strategic architecture does he recommend to ensure privacy and security without the protection of assets becoming an unsustainable cost?

"It's a real challenge, I live it every day in the financial sector. And the honest answer is: it depends on your risk profile," Papalini begins. "For most companies, a hybrid approach works: cloud models for non-sensitive code, with clear rules about what can go out and what cannot. The main providers now offer enterprise options with serious contractual guarantees. Those with stricter requirements can look to on-premise with open-source models. Llama, Mistral, DeepSeek have remarkable capabilities. The price is operational complexity."

But he identifies an often-underestimated threat: "But you know what the most underestimated threat is? Shadow AI: developers using unauthorized tools because the official ones are slow to be approved or too limited. The solution is not to prohibit, but to offer legitimate alternatives that are good enough to not create an incentive to bypass the rules."

It is an approach reminiscent of harm reduction in health policies: instead of criminalizing inevitable behaviors, make safer alternatives available.

## Apprenticeship in the Age of Machines

One of the most provocative sections of the book concerns the future of training and skills. An emerging distinction is being drawn between traditional computer science graduates and the new figure of the AI Engineer, someone who knows how to orchestrate intelligent systems but may have never written a parser from scratch.

I ask Papalini if AI that allows anyone to generate code means the end of the "pure" programmer, or if we are simply raising the bar for the necessary architectural skills.

"The programmer is not destined to disappear, but their role is changing a lot," he replies. "Think about what happened when high-level languages arrived. Assembly programmers didn't disappear, they became niche specialists. The bulk of the work moved up a level."

The current transition, according to Papalini, follows a similar pattern: "Something similar is happening now. A different figure is emerging, let's call it an 'orchestrator': someone who knows how to break down complex problems, specify requirements with precision, critically evaluate what the AI produces, and make architectural decisions."

But here comes the paradox: "The paradox? It requires *more* experience, not less. A junior can use AI to generate code that seems to work. But only a senior recognizes when that code is a ticking time bomb, because they have seen enough disasters to recognize the signs."

The systemic risk he identifies is that of skill atrophy: "We must also be careful not to think that everyone is born an orchestrator: if we delegate all the 'grunt work' to AI, how do we train the next generation of seniors? The data tells us that the employment of younger developers is already declining. But even those who enter the market risk never developing those deep skills that are built only by banging your head against problems."

## Trio Programming

To solve this dilemma, Papalini proposes a model in the book that he calls "trio programming," an evolution of pair programming that includes AI as a third actor.

"In the book, I propose 'trio programming' as a solution to the training problem," he explains. "The junior works with the AI to implement the features. The AI accelerates, suggests, generates code. So far, nothing new. The senior orchestrator doesn't write code; they are there to ask questions. 'Explain to me what this method does.' 'Why did the AI choose this data structure?' 'What happens if the input is null?' 'How would you handle a network error here?'"

The mechanism is pedagogically brilliant: "By answering these questions, the junior learns. The senior, for their part, transfers that tacit knowledge that is in no manual—the intuition about what can go wrong, the sensitivity for code that 'smells,' the experience of someone who has seen systems collapse."

It's like the apprenticeship in Renaissance workshops: the master does not paint in the apprentice's place, but points out where the perspective is wrong, why that mix of colors will not hold, where the composition loses balance.

## The Value of Judgment

I return to the theme of monetization and value. Papalini has written several articles on Medium exploring how companies are trying to extract profit from generative AI. I ask him: beyond software, how does he see the impact of generative AI in marketing and the creation of digital products? Is it just a matter of speed, or is the very value of the product changing?

"Yes, the value is changing, but in a counterintuitive way," he replies. "When everyone can generate content, images, code, *production* becomes a commodity. It's abundant, so it's worth less. What gains value is everything else: understanding what is worth building, distinguishing the mediocre from the excellent, having a vision."

In software, he says, he sees it manifest every day: "If anyone can generate a working app in a weekend, what distinguishes your product? It's no longer the implementation, it's the insight into the problem, the user experience, the ability to evolve over time."

And the same goes for marketing: "AI can churn out infinite variations of copy, images, videos. But 'infinite' doesn't mean 'effective.' You need someone who knows what to test, how to read the results, when to stop."

The synthesis is elegant: "We are entering an era of cognitive abundance. The bottleneck is no longer producing, it's choosing, curating, judging."

It's like the transition from scarcity to overabundance in the music industry. When anyone can record and distribute an album, the value shifts from the technical ability to produce to the artistic ability to create something worthy of attention.

## Autonomous Agents and the Near Future

We are moving from simple coding assistants (the various Copilots) to autonomous agentic systems, theoretically capable of taking initiative, coordinating complex tasks, and even debugging their own code. I ask him for his vision on the evolution of AI agents in software engineering over the next five years. Will we see systems that self-repair and self-deploy?

"In the next 12-18 months, we will see the orchestration of agents become common practice in the most advanced companies," Papalini predicts. "Not twenty agents in parallel, that's demo stuff. Two or three workstreams managed together: one agent updating tests, one migrating dependencies, one adding a minor feature. All while the developer focuses on the work that requires judgment."

But he warns: "The keyword is 'verifiable.' Human attention remains the bottleneck. It doesn't matter how fast the agent is if it then takes a week to understand what it has done."

On the long term, he is cautious: "Five years from now? I'm cautious. Agents that 'self-repair' already exist—automatic rollbacks, self-healing infrastructure. But agents that self-deploy completely autonomously? For critical systems, I doubt it. And I'm not even sure we should want that."

His most solid prediction concerns the human role: "My safest prediction: the engineer's role shifts towards specification and validation, less towards implementation. But this change will require *more* competence from workers, not less."

## Skill Atrophy

There is a theme that runs through the entire book: the risk that the massive adoption of AI will not amplify human capabilities but atrophy them. It is the ethical and social question that lies beneath the surface of every technical consideration.

I ask him directly: how can we ensure that the massive adoption of AI in companies does not devalue human professionalism, but becomes a real amplifier of talent capabilities?

"This is the question I care about most," Papalini replies. "The concrete risk I call 'skill atrophy.' An engineer interviewed by MIT Technology Review said that after months of intensive AI use, when he tried to program without it, he felt lost; things that were once instinct had become laborious. This is exactly the alarm bell we should be listening to."

The solution is not rejection but intentionality: "The solution is not to reject AI; that would be like rejecting electricity. But we must be intentional about how we integrate it, especially in training paths. That's why in the book I propose models like 'trio programming' to cultivate the abilities of talent and not make the mistake of sawing off the bottom rung of the ladder from which we climbed, the learning process that brought us to where we are."

## Beyond Software

At the end of the conversation, I ask him if a CEO of a company that does not produce software can find value in his book. It's a legitimate question: the title explicitly talks about software engineering.

"Absolutely, and let me explain why," he replies with conviction. "Software was the first domain to be massively invested in by generative AI, so it's the laboratory where certain phenomena have manifested earlier and in a more measurable way. But the patterns I describe in the book are universal; they concern the relationship between human beings and probabilistic systems, and this now touches every sector."

The generalization is convincing: "Let's take the central concept: the shift from determinism to non-determinism. When you ask an AI to write code, you don't know exactly what you'll get. But the same is true when you ask it to write a marketing campaign, analyze a balance sheet, draft a contract, or respond to a customer. The output looks professional, it's formulated with confidence, but it could be subtly wrong in ways that only an expert recognizes."

Papalini translates every concept from the book outside the domain of code: "The '70% problem' works identically in every context. The AI quickly gets you to a draft that seems almost finished—a report, a presentation, a market analysis. But that 'almost' hides the 30% where nuances, context, and judgment are needed. The junior in marketing who accepts AI-generated copy without understanding why certain words work and others don't is making exactly the same mistake as the programmer who commits code they can't explain."

The theme of training becomes even more urgent: "The 'competence trap' is perhaps the most urgent theme for any CEO. If your junior analysts delegate the construction of financial models to AI, they will never learn how to do them. If your young lawyers use AI for first drafts without ever writing one from scratch, they will never develop the intuition for contractual risks. You are saving time today and destroying competence tomorrow."

Even trio programming becomes generalized: "'Trio programming' that I propose becomes 'trio working': a junior, a senior, and the AI working together. The junior uses the AI to accelerate, the senior asks the questions that force understanding. It works for training an analyst, a consultant, an account manager—any role where expertise is built by doing."

And the problem of governance cuts across every business function: "And then there's Shadow AI, employees who use ChatGPT secretly because the official tools are too slow or limited. It happens everywhere: in the legal office, in customer service, in human resources. It's not a technological problem, it's a governance problem that every CEO must address."

The conclusion is pragmatic: "The book uses software as a context, but what it tells is the story of how to integrate powerful but unreliable tools into professional work without losing quality, skills, and control. This is the challenge of every organization today, whether it produces code, contracts, advertising campaigns, or financial analyses."

And he adds a final note that sounds like a manifesto: "A CEO who reads it will not find instructions for configuring Copilot; they will find a framework for thinking about the adoption of AI that they can apply to any function of their company. And frankly, in this moment of unbridled hype and inflated expectations, a little engineering clarity can do anyone who has to make decisions a lot of good."

## Many Answers That Open Many Questions

We conclude this long conversation. Papalini has to get back to dealing with systems that move capital; I have to turn this conversation into something readable. But the feeling that remains is that of having spoken with someone who is watching the same movie we are all watching, just a few minutes ahead.

The book [*Intelligenza Artificiale e Ingegneria del Software*](https://amzn.to/3Z12Ng9) is not a technical manual, despite its title. It is more like those mountaineering essays written after a particularly risky expedition: a map of things that can go wrong, written by someone who came back to tell the tale. With the only difference that we are all climbing this mountain, whether we like it or not, and someone who has already made a couple of attempts can be useful.

The real question is not whether we will use artificial intelligence to write code, do marketing, analyze data, or make decisions. We are already using it. The question is whether we will manage to do so without losing along the way the skills that allowed us to get here. And on this question, for now, the answer is still open.
