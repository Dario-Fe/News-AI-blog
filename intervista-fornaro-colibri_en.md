---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Vincenzo Fornaro and Colibrì: "I'm Not Interested in Genius, I'm Interested in Curiosity"
![intervista-fornaro-colibri.jpg](intervista-fornaro-colibri.jpg)

*I have already written about Colibrì, telling how it is possible to run a 744-billion-parameter Mixture-of-Experts model on a computer with barely 25 GB of RAM, treating the disk as an intelligent memory tier rather than a simple storage bin ([you can read the full technical analysis here](https://aitalk.it/it/colibri.html)). What was missing was the voice of the person who wrote that engine, one C file at a time, alone, without a lab or a cluster behind him. I chatted with Vincenzo Fornaro to hear the story behind the code, and the conversation turned out to be longer and more inspiring than I had anticipated.*

## From a Warehouse in Brescello to an Idea Chased at Night

Very little can be found about Vincenzo online. His [GitHub](https://github.com/JustVugg/colibri) profile is limited to a single line: "Founder of Colibrì, a tiny engine, immense model." Yet in three weeks, the project passed twenty-five thousand stars and ended up at the center of the debate on democratizing artificial intelligence. I asked him who he is, even before asking him how he did it.

"I think it's hard to find information about me online because I've never been a particularly outgoing person, and above all, I've never had much interest in showcasing myself. I've always preferred to put my projects first.

For me, programming has always been an outlet for imagination. For years, especially at night, it was simply me, a computer, and an idea to think about. I didn't necessarily program because someone asked me to or because I had a product in mind to sell. Often I programmed because I needed to understand if an idea in my head could become real.

I've always felt that the project is more important than the person who creates it. But over time I also understood something else: when a project starts being useful to many people, the person who started it has the responsibility to give it direction and build around it the conditions for it to grow.

I was born in Taranto, but today I live in Brescello, in Emilia-Romagna, the town of Don Camillo and Peppone. My life wasn't particularly easy: I was orphaned when I was nine, and for much of my life, economic resources were limited.

I studied computer science in Bari, but at a certain point, I could no longer continue my studies for financial reasons. So I started working in a warehouse as a stock keeper.

Life often takes paths you didn't plan. That was the job, but my mind kept being elsewhere. I never stopped programming. I kept studying, experimenting, and imagining applications and systems.

I was greatly influenced by the stories of people who managed to build something starting from far from perfect conditions. I wasn't interested in copying their path. I was interested in understanding how an idea could transform into something capable of changing the way people use technology.

From a technical point of view, I've always had a special predilection for C and C++. I've studied them since university, and I continue to consider them extraordinary tools when a problem requires control, predictability, and speed. I like having as few layers as possible between what I think and what the computer executes.

Colibrì was born exactly like that.

I wanted to understand if it was possible to take a relatively common computer, even a slow one without a particularly powerful GPU, and manage to run a huge model.

There wasn't a company behind it, there wasn't a team, and there wasn't initially a business plan. There was a technical problem that curious me enough to make me work night and day.

When I managed to solve it, for a while, the project remained on my computer. Then I almost casually decided to publish it on GitHub.

From that moment, something happened that I hadn't foreseen.

People started trying it, discussing it, contributing, and using it. Colibrì began to be much bigger than the experiment from which it was born.

And that's precisely where the perspective changed for me too.

Colibrì wasn't born because I wanted to build a startup. But when thousands of people start telling you, directly or indirectly, that the problem you decided to address interests them too, you have to start asking yourself how big the solution can become.

Today that is the question that interests me."

## Opening a Model, Not Just Using It

The project's GitHub page reads almost like a manifesto: "Frontier models should not be sealed inside datacenters. Colibrì exists so that anyone curious enough can open one up." I ask him what "opening" a model really means to him, not simply accessing it via an API, and whether the AI democracy he envisions is a matter of access or something deeper.

"For me, access to AI should be as simple as possible. You should be able to turn on a computer, open a program, and start experimenting.

It shouldn't be a possibility reserved only for those who own hardware worth tens of thousands of euros or those who can use large infrastructures.

But I believe that access is only the first level.

The thing that interests me even more is the possibility of knowing the technology you are using.

When I talk about an 'open' model, therefore, I don't simply mean being able to get an answer. I mean being able to run it, observe it, measure it, make experiments, and try to understand what happens when you change something.

There is a huge difference between using intelligence and being able to study it.

This doesn't mean the cloud is wrong. The cloud is and will continue to be extremely important. There are problems for which concentrating huge amounts of compute in a datacenter is the best solution.

I simply think it shouldn't be the only possible model.

There should also be another possibility: bringing more and more inference capacity close to the person, researcher, company, or device that needs it.

The democratization of AI, in my opinion, should therefore be both a democratization of access and a democratization of understanding.

I wouldn't want a person's first question to be: 'Do I have enough GPUs to try this?'

I would want it to be: 'What can I discover if I try doing it?'

AI is becoming one of the most powerful knowledge tools we have built. The more people can experiment with it directly, the higher the probability that someone will find a use, an optimization, or even a paradigm we haven't thought of today.

For me, the main requirement should increasingly become curiosity, not the size of the infrastructure you own."

## A Post on Hacker News, Not a Manifesto

There is a detail that struck me from the beginning: the post with which Fornaro presented Colibrì on Hacker News wasn't titled "I created the ultimate inference engine," but simply "Getting GLM-5.2 running on my slow computer." An almost modest attitude for a result that is far from modest. I ask him when he realized that his personal experiment was becoming something else, and which reaction from the community made him think that things were really changing.

"The title was simply 'Getting GLM-5.2 running on my slow computer' because that was exactly the story.

I didn't want to say I had built the ultimate inference engine. I had solved a problem I found interesting and wanted to explain how.

Colibrì wasn't born with the goal of becoming a startup. It was born out of curiosity.

Then two things happened.

The first was seeing people actually use what I had built.

I particularly remember a guy who wrote to thank me because, thanks to Colibrì, he had managed to access a model that would otherwise have required a much more expensive machine.

That struck me much more than the number of stars.

Because for the first time, I wasn't just looking at a technical solution. I was looking at a real problem eliminated for someone.

The second thing was the community.

People I didn't know started opening issues, making pull requests, testing hardware, finding bugs, and proposing optimizations.

At that point, I understood that something important was happening: Colibrì wasn't growing because I was trying to convince someone it was useful. People were arriving spontaneously because they recognized the problem.

For those who build technology, this is a very strong signal.

Since then, I've started looking at Colibrì differently.

It remains an open-source project and I want it to continue being one, but I think the technology and the problem we are addressing can have much larger implications than the repository where it all started.

The interesting transition, now, is understanding how to transform that spontaneous interest into an increasingly solid, generalizable, and usable technology.

And to do that, inevitably, Colibrì will have to grow beyond the dimension of a single person."
![colibri-dashboard.jpg](colibri-dashboard.jpg)
[The Colibrì web dashboard, image taken from the official repository](https://github.com/JustVugg/colibri)

## One File, Thirteen Hundred Lines, No Compromises

The core of Colibrì is a single C file of about thirteen hundred lines, with no dependencies, no GPU required, and no runtime Python. At a time when vLLM, TensorRT-LLM, and SGLang are projects born in labs with large teams and complex codebases, Fornaro's choice sounds almost like an act of resistance, much like those homemade record productions with four instruments that manage to sound denser than an entire orchestra. I ask him if behind this extreme simplicity lies a purely architectural choice or a more philosophical conviction.

"It was initially an architectural choice, but it also became a conviction.

When you try to make a huge model work on a relatively small machine, every additional layer has a cost.

You need to know exactly where memory is located, when it is moved, what is calculated, and why something is slow.

C allows me to have extremely direct control over these things.

But that doesn't mean I consider complexity inherently bad.

Complexity is an investment.

You must introduce it when the value it produces is greater than the cost it adds.

In the beginning, Colibrì could afford to be extremely small. Today, GPU backends, servers, interfaces, new architectures, and other components are arriving. Inevitably, the project will grow.

The challenge is to grow without losing readability.

I would like the core of the system to remain something that a good developer can open, read, and understand.

This also has a very concrete advantage for an open-source project: it enormously reduces the barrier for those who want to contribute.

Simplicity, in this sense, is not just elegance.

It is development speed, debugging capability, ease of experimentation, and the ability to bring new people into the project."

## Disk as Memory, Not Storage

The underlying mechanism of Colibrì has a minimalist elegance: the dense part of the model stays resident in RAM, while experts are pulled from disk only when needed—a bit like the JIT compiler of certain languages that doesn't translate everything in advance, but only what execution actually requires, moment by moment. I ask Fornaro what, for someone approaching Colibrì for the first time, is the most counterintuitive concept to digest.

"Probably the most counterintuitive concept is this: a gigantic model doesn't necessarily use all its parameters at the same time.

When a person hears '744 billion parameters,' they imagine that to generate each token, the computer must use all those parameters.

In a Mixture-of-Experts model, it doesn't work like that.

It's more like a huge organization with many specialized departments. They all exist, but for each token, the model activates only a portion of the experts.

So the question stops being:

'How do I fit the whole model in RAM?'

and becomes:

'How do I make the right part of the model available at the exact moment it's needed?'

Colibrì tries to answer this second question.

Storage becomes another level of the memory hierarchy. Experts can remain on disk and be brought close to the compute when needed.

It's like having a huge warehouse and a relatively small workbench. You don't put the whole warehouse on the table. You must organize the system so that what is needed reaches the table fast enough.

Then caching, prefetching, usage patterns, and other optimizations come into play.

The general principle, however, remains simple:

you don't necessarily have to have everything at the same time.

You must manage to have the right thing at the right moment.

And that is a principle I believe can have much broader applications as models continue to grow."
![tiers.jpg](tiers.jpg)
[A memory hierarchy instead of a single memory requirement, image taken from the official repository](https://github.com/JustVugg/colibri)

## 0.05 Tokens per Second, Honestly

Here comes the most discussed point online. On a laptop with 25 GB of RAM, early benchmarks spoke of one token every ten to twenty seconds, and an analysis by Wavect wrote that the project "runs, but at 0.05-0.1 tokens per second from cold cache," calling it "a serious proof of architecture, not yet a drop-in production server." Tom's Hardware points to 20-30 tokens per second as the threshold for truly fluid interaction, while on a machine with six RTX 5090 GPUs, it reaches 6 tokens per second. I ask him how he positions himself regarding these observations, whether Colibrì is today a fascinating engineering exercise or an already usable product.

"Wavect's analysis is honest.

Calling the early versions of Colibrì 'a serious proof of architecture, not yet a drop-in production server' is a description I consider correct.

Speed is a real problem, and I don't want to hide it.

On a laptop today, running a model of that size through Colibrì doesn't mean having the same experience you would have using a model served by a large datacenter.

But in my opinion, the interesting point is understanding the trajectory.

Before, the problem was binary: that model either fit into your infrastructure or it didn't.

Colibrì tries to turn it into a continuous problem: how slowly can we start, how much can we improve caching, storage, prefetching, speculation, accelerated backends, and how much of the bottleneck can we progressively eliminate?

Engineering often starts by turning a zero into a number.

Once something works, you can measure it.

And once you can measure it, you can seriously start optimizing it.

I wouldn't promise 20 or 30 tokens per second today for a model with hundreds of billions of parameters on any laptop. There are physical limits that software cannot simply erase.

But I think there is a huge space between 'impossible' and 'as fast as a datacenter.'

And that is precisely the space I'm interested in exploring.

In the short term, I see Colibrì as a very interesting platform for developers, researchers, enthusiasts, and use cases where local access to huge models has a particular value.

In the long term, however, the goal is to keep reducing the distance between local inference and centralized infrastructure.

If we manage to do that well enough, it won't just be a technical experiment anymore.

It will become a new infrastructure option."

## Correctness Before Benchmarks

Colibrì still has open frontiers: it is not a production server; for now, it works with the architecture of GLM-5.2 and not with generic MoE models; validating the quality of int4 quantization is a work in progress; the NVMe disk remains the toughest opponent to beat. I ask him how he tackles these challenges and whether there are compromises he is willing to accept today to gain speed, or lines he considers uncrossable.

"A small correction to the premise: Colibrì already supports several MoE model families today, and each new architecture added allows us to understand something that can become useful to the others as well.

Quantization has also matured a lot.

We found and fixed real quality issues, and the community was fundamental in this.

The main opponent, however, remains the amount of data you have to move.

And that's why a rule I continuously try to apply is: measure before believing.

It's extremely easy to invent an optimization that looks brilliant on paper.

It's much harder to prove that it truly improves the system on real hardware and real workloads.

I have a small laboratory of experiments where many ideas go to die.

And that's exactly what should happen.

As for compromises, I'm willing to accept many.

I can accept a slower cold start if performance improves during use.

I can accept greater complexity in the data format if it means reading much less from storage.

I can accept different strategies depending on the hardware.

What I don't want to sacrifice is correctness.

An impressive benchmark obtained by silently degrading the quality of the model doesn't interest me.

If Colibrì is to become an infrastructure on which other people build something, trust in the results must come before the best number in a table."

## Software, Hardware, Models: Three Paths Converging

The project already has CUDA and Metal backends, a working web interface, and native support for GLM-5.2 speculative decoding. I ask him what is missing to reach a speed that can truly compete with a cloud API in daily use—say ten to twenty tokens per second on hardware an average person could buy—and whether it is a matter of code, hardware, or future models better suited to this approach.

"It's all three things: software, hardware, and models.

But probably the most interesting element is how these three parts can begin to be designed together.

Software can do a great deal.

We can improve data formats, reduce reads, predict which experts will be needed, overlap transfer and compute, improve caching, and better utilize available CPUs, GPUs, and storage.

But software cannot eliminate a physical limit.

Hardware will therefore continue to be important.

Consumer SSDs are becoming faster and faster, memory capacity is growing, and computer architectures are changing too.

For Colibrì, this is particularly interesting because we consider storage not simply as the place from which to load the model at the start, but as an active part of the inference architecture.

Then there are the models.

Current ones were designed for infrastructures where huge amounts of memory and bandwidth exist.

They weren't optimized with a consumer machine in mind that must continuously decide which parts of the model to bring close to compute.

However, I see no reason why this should remain a constant.

Models with greater locality, smaller experts, more predictable routing, or structures explicitly designed for memory hierarchies could radically change the problem.

In a sense, it could be that Colibrì arrived before the ideal model for this type of inference.

This is also one of the things I find most interesting from a future perspective.

I don't want Colibrì to simply be 'a program that runs GLM on a laptop.'

I'm interested in understanding if some of the ideas we are exploring can become a different way of thinking about the inference of very large models.

If that happens, the potential market won't be limited to the single enthusiast with a slow computer.

It could concern workstations, edge computing, companies that want to keep data locally, research, dedicated appliances, and probably use cases we haven't imagined today."

## Owning a Model: Beyond Savings

Some see in Colibrì the proof that local AI can become real even for those who cannot afford a datacenter, while others object that the democratization of AI is already a reality—all it takes is a browser and twenty dollars a month for ChatGPT. I ask him how he responds to this objection, and what owning a model really means beyond mere economic savings—whether it is a matter of privacy, freedom, or something more radical like the ability to do science on AI, not just use it.

"The objection is absolutely legitimate.

If the question is 'Can I use a very powerful artificial intelligence?', the cloud has already enormously democratized access.

And that's an extraordinary thing.

I don't view Colibrì as a war against the cloud.

I think cloud and local AI solve different problems and will coexist in the future.

There will be tasks for which it makes sense to use the most powerful model available in a datacenter.

And there will be others where latency, privacy, cost predictability, network independence, infrastructure control, or the ability to study the exact system you are using will be important.

I think about the history of computing.

The personal computer didn't make mainframes useless.

It simply opened another dimension of computing.

The fact that a computer was yours meant you could program it, modify it, break it, experiment.

With AI, I think something similar can happen.

A remote service is extraordinarily convenient when you want to get an answer.

A local model becomes interesting when you also want to ask questions about the system itself.

Why did it answer like this?

How does behavior change if I modify this component?

How much can I compress it?

Can I reproduce the same result in five years?

Can I use data that I don't want to send outside my infrastructure?

Can I build a product that continues to work without depending entirely on an external provider?

So I don't see the future as 'cloud versus local.'

I see it as a continuum.

And I think today one part of that continuum is still much less developed than the other.

That's where Colibrì tries to work."

## 2036 and the Legacy of an Idea

We close with a long view. Imagine 2036: models have become even larger, or perhaps smaller and smarter; consumer hardware is transformed. I ask him if Colibrì, or something born from it, will still be relevant; what he dreams will happen in the next ten years for those who want to keep artificial intelligence in their own hands; and more personally, after twenty-five thousand stars and headlines on Tom's Hardware and Hacker News, what he wants people to remember about him.

"In 2036, I hope many of the things that Colibrì makes difficult today will have become normal.

That doesn't mean I hope Colibrì disappears.

It means I hope it evolves.

Important technology projects rarely stay identical to their first version. They change along with the problem they are trying to solve.

If running huge models on relatively common hardware is normal ten years from now, that will be a victory.

At that point, Colibrì will probably be facing another frontier.

What I'd like to remain constant is the underlying idea: reducing the distance between a curious person and a technology that today seems too big, expensive, or complex to explore directly.

In 2036, I'd like a person to be able to look at an advanced model and think:

'I want to understand how it works.'

And be able to do it.

As for what I personally want to build, today I feel a different responsibility than at the beginning.

Colibrì was born as an individual experiment, but I don't think it necessarily has to remain one.

If we want to seriously address this problem, we will need people much better than me in many different areas, we will need an increasingly strong community, and probably we will also need to build a structure capable of sustaining the project in the long term.

This doesn't change why I started.

It simply makes it more ambitious.

And if in ten years someone, faced with a problem everyone considers impossible, thinks:

'Let's try.'

and maybe uses something that was also born from the work done today on Colibrì, for me that will already be a huge result.

I'm not particularly interested in people remembering the idea of Vincenzo Fornaro as a 'genius.'

I'd be much more interested if another idea remained:

that a person with few resources, but enough curiosity, can still start something important enough to attract other people and become much bigger than themselves.

That's exactly what is happening to Colibrì."

---

*The [Colibrì repository](https://github.com/JustVugg/colibri) remains available on GitHub for those who want to try it, contribute, or simply read those thirteen hundred lines of C that sparked the conversation.*
