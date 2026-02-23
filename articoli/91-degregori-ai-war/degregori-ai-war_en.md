---
tags: ["Copyright", "Business", "Ethics & Society"]
date: 2026-02-23
author: "Dario Ferrero"
---

# What does De Gregori have to do with the AI war?
![degregori-ai-war.jpg](degregori-ai-war.jpg)

*There is a song by Francesco De Gregori from 1992, from the album "Canzoni d'amore", that perhaps few remember in the vast and poetic catalog of the Roman singer-songwriter. It is titled "Chi ruba nei supermercati?" (Who steals in supermarkets?), and its chorus poses a question that at the time was terribly current and sociological: "Which side are you on? Are you on the side of those who steal in supermarkets? Or of those who built them, stealing?" Thirty-four years later, that question resonates strangely current in a context that De Gregori, despite his extraordinary ability to read the world, could not have imagined: the technological war between the largest artificial intelligence companies on the planet.*

## The memo and the earthquake

On February 12, 2026, OpenAI sent a memorandum to the House Select Committee on Strategic Competition between the United States and the Chinese Communist Party, the bicameral committee of the American Congress dedicated to strategic competition with China. The content of that document, [reported by Reuters](https://finance.yahoo.com/news/openai-accuses-deepseek-distilling-us-221629899.html) and [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-12/openai-accuses-deepseek-of-distilling-us-models-to-gain-an-edge), is a direct accusation: the Chinese startup DeepSeek allegedly used *distillation* techniques to train its models by exploiting the outputs of ChatGPT, deliberately bypassing OpenAI's security systems through third-party routers and obfuscation techniques to hide the origin of the access.

"We have observed accounts associated with DeepSeek employees developing methods to circumvent OpenAI's access restrictions," the memo reads according to Reuters, "and we know that DeepSeek employees developed code to access US AI models and obtain their outputs for distillation in programmatic ways."

To understand why this accusation caused a stir, we must go back to January 2025, when DeepSeek triggered what many observers had dubbed the "Sputnik moment" of Chinese artificial intelligence. The Hangzhou-based startup, founded by Liang Wenfeng and funded exclusively by his High-Flyer hedge fund, had released the [DeepSeek-V3](https://api-docs.deepseek.com/news/news1226) and [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120) models, capable of competing with the best American models at a fraction of the declared cost: less than six million dollars in computational power, compared to the billions that OpenAI, Anthropic, Meta, and Google continued to invest in their infrastructures. The cost of training R1, as documented by [independent analysis](https://www.reuters.com/technology/artificial-intelligence/what-is-deepseek-why-is-it-disrupting-ai-sector-2025-01-27/), had been declared at less than six million dollars using Nvidia H800 chips, the "downgraded" version of the H100s that the United States had already banned from export to China.

The effect on markets was immediate and brutal: Nvidia burned about 600 billion dollars in capitalization in a few days. The dominant narrative, that dominating AI necessarily required billions of investments in chips and data centers, suddenly seemed fragile.

## How distillation works

Before proceeding, it is necessary to clarify exactly what *distillation* is, because the term, as often happens in tech communication, is used imprecisely by both DeepSeek's detractors and defenders.

In the most proper technical sense, distillation is a process where a smaller and lighter model, the "student", is trained to replicate the behavior of a larger and more powerful model, the "teacher". [As OpenAI itself explains](https://finance.yahoo.com/news/openai-accuses-deepseek-distilling-us-221629899.html) in the memo to Congress, the technique "involves an older, more established and powerful AI model evaluating the quality of responses produced by a newer model, effectively transferring the learning results of the older model to the newer one." In more concrete terms: instead of learning from the world through billions of human texts, the student learns from the wisdom already distilled in the teacher.

The technique itself is neither new nor illegal. It is a standard tool in the field: DeepSeek itself, in its [technical paper on R1](https://arxiv.org/abs/2501.12948), openly describes how it created distilled versions of its model to make them accessible on less powerful hardware, using GRPO (Group Relative Policy Optimization) as a reinforcement learning framework instead of the more conventional RLHF. The paper, signed by DeepSeek-AI and 199 co-authors, describes a multi-stage training process that integrates reinforcement learning, supervised fine-tuning and, indeed, distillation *of its own models towards smaller versions*.

The point of controversy is therefore not the technique itself, but its goal: OpenAI claims that DeepSeek distilled *ChatGPT outputs*, i.e., used the competitor model's responses as training material for its own. [OpenAI's Terms of Service](https://openai.com/policies/row-terms-of-use/) explicitly prohibit using the outputs of its services "to develop models that compete with OpenAI."

## DeepSeek does not respond. Silence as a response

Faced with the accusations of February 2026, DeepSeek did not respond to Reuters' requests for comment. It is not the first time: even in January 2025, when the first rumors about distillation emerged in the *Financial Times*, the Chinese startup's response had remained elusive or vague.

Silence is significant but not unequivocal. It can be a legal strategy, calculated indifference, or simply the choice of a startup that does not want to legitimize a competitor's accusations by responding on its terrain. What remains is an open question: what concrete evidence does OpenAI have, beyond the fact that the suspicious accounts "were associated with DeepSeek employees"?

From a technical point of view, the issue is far from resolved. DeepSeek published details of its training process in a peer-reviewed paper on arXiv. As [documented in the analysis of arxiv 2501.12948](https://arxiv.org/abs/2501.12948), the R1-Zero model was trained exclusively via reinforcement learning without initial supervised fine-tuning, starting from the DeepSeek-V3 base model. Independent benchmarks showed performance comparable to OpenAI-o1 on mathematical reasoning and coding tasks. The fact that similar results were achievable with different architectures and methodologies, and at significantly lower costs, is part of the reason why the story had generated such a stir.

That said: the transparency of a technical paper does not exclude the parallel use of undocumented techniques. And DeepSeek's lack of response is not a demonstration of innocence.

## The legal boomerang

In light of all this, the most interesting, and most embarrassing for OpenAI, knot is the legal one. As analyzed in detail by experts at the [Santa Clara Business Law Chronicle](https://www.scbc-law.org/post/code-claims-and-consequences-the-legal-stakes-in-openai-s-case-against-deepseek), OpenAI is in an extraordinarily awkward procedural position if it decides to proceed legally. To sustain a copyright infringement lawsuit, it would have to convince a court that AI model outputs enjoy copyright protection, i.e., that the responses generated by ChatGPT are protectable creative expression.

The problem is that OpenAI has built much of its defense in the case filed by the *New York Times* exactly on the opposite argument: scraping others' content to train its models is "fair use", i.e., a legitimate use that transforms protected and original material into something "free" if the use is aimed at criticism, comment, information, teaching, or research.

One cannot invoke copyright on one's own outputs after denying the same principle to the human authors whose work made those outputs possible. The stratagem is logically circular, and legal experts noted it immediately. "It's as if the shoe of appropriate-content has ended up on the other foot," wrote *Business Insider*, citing legal expert opinions collected immediately after the first accusations in January 2025. OpenAI could instead try the breach of contract route, violation of Terms of Service, but even here it faces the difficulty of enforcing an American ruling on a company based in Hangzhou, in a legal system with which reciprocity agreements are non-existent or deficient.

The result, as the legal analysis of Santa Clara Law concludes, is that "the combination of scarce precedents and geographical complications leads to the conclusion that a lawsuit, and a favorable outcome, would be extremely rare and difficult for OpenAI to obtain."

## The supermarket and its architects

And this is where the story becomes systemically complicated. Because OpenAI's accusation against DeepSeek cannot be read without the context of what OpenAI, and not just OpenAI, has done to build its models.

In December 2023, the *New York Times* filed a [lawsuit against OpenAI and Microsoft](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward) for copyright infringement, claiming that millions of the newspaper's articles had been used to train ChatGPT without authorization or compensation. In March 2025, a federal judge from the Southern District of New York, Sidney Stein, [rejected OpenAI's request to dismiss the case](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward), allowing the main claims to proceed to trial. The judge narrowed some of the accusations but left the substance standing: the question of whether massive scraping of copyrighted journalistic content constitutes fair use is still sub judice.

It is not an isolated case in the landscape of lawsuits related to AI model training. In October 2025, Reddit filed a [lawsuit against Perplexity AI and three data scraping companies](https://www.cnbc.com/2025/10/23/reddit-user-data-battle-ai-industry-sues-perplexity-scraping-posts-openai-chatgpt-google-gemini-lawsuit.html), Oxylabs, AWMProxy, and SerpApi, accusing them of extracting billions of user posts hiding behind Reddit's technical protections through Google Search results. Reddit's Chief Legal Officer, Ben Lee, had coined a particularly effective expression: "data laundering". "AI companies are locked in an arms race for quality human content," he said, "and that pressure has fueled an industrial-scale 'data laundering' economy."

It should be noted that Reddit had already entered into licensing agreements with Google and OpenAI itself: the problem, in the Perplexity case, was the sourcing of data through third parties without paying. But OpenAI itself had built its models on corpora that included unlicensed content: the [class actions brought by authors and writers](https://cointelegraph.com/news/open-ai-microsoft-accused-stealing-data-train-chat-gpt-artificial-intelligence-lawsuit) for the unauthorized use of literary texts during GPT training are a documented trace of this.

The mechanism is identical to what OpenAI attributes to DeepSeek: using others' intellectual work to build a commercial system without permission and without paying. The difference, in OpenAI's eyes, is that they did it with human texts while DeepSeek allegedly did it with AI model outputs, a distinction that has something redundant about it: those AI models are what they are because they have absorbed unauthorized human work.

## Geopolitics, chips, and the memo to Congress

OpenAI's memo to Congress is not just a technical-legal issue. It is a political act, addressed to the committee overseeing strategic competition with China, written at a time when the Trump administration was redefining its posture toward technology exports.

David Sacks, appointed "AI and crypto czar" by the White House, had already prepared the ground in January 2025, declaring to Fox News that "there is substantial evidence that what DeepSeek did is distill knowledge from OpenAI models." Congressman John Moolenaar, chairman of the House Select Committee on China, [according to Gigazine](https://gigazine.net/gsc_news/en/20260213-openai-accuses-china-deepseek/), had used even harsher tones: "This is part of the Chinese Communist Party's strategy: steal, copy, and destroy."

OpenAI had also added, in the memo, a worrying note about safety: when a model is replicated via distillation, the safety mechanisms of the original model tend not to be transferred, potentially leaving a less filtered version circulating on the market, with risks for so-called high-hazard sectors like biology and chemistry. It is a legitimate argument. It is also an argument that serves to color in darker tones a case that on a strictly legal level is much less solid.

On the other hand, the perspective of many Asian observers frames OpenAI's accusations as technological protectionism masked as ethical issues. DeepSeek proved that it was possible to build competitive models with significantly lower computational resources, effectively bypassing the structural advantage that restrictions on Nvidia chip exports were supposed to guarantee the American industry. If distillation accusations were to become a pretext for further regulatory blocks, it would be a matter of responding to a technical defeat with political tools.

## Which side are you on?

Let's go back then to De Gregori, and the question he had left hanging.

The narrative structure of this story is almost too perfect in its embarrassing symmetry. OpenAI accuses DeepSeek of using its models without permission to build something competitive. But OpenAI built those models using the work of journalists, writers, authors, Reddit programs, discussion threads, and entire corpora of human intellectual production without asking permission or paying. The *New York Times* lawsuit is still open in American courts. Writers' and authors' class actions are multiplying. Reddit is taking to court those who did exactly what OpenAI had done with human texts.

It is not a question of absolute innocence or absolute guilt. It is a question of who sets the rules of the supermarket, who gets to keep the register, and who is stopped by the guards at the exit. The distillation that OpenAI attributes to DeepSeek is morally and structurally analogous to the scraping that OpenAI performed on human content: both are techniques for extracting value from someone else's corpus without compensation, used to build powerful commercial systems. The main difference, at the moment, is a matter of power: who has the resources to define the legal and political narrative, and who does not.

This does not mean that OpenAI's accusations are false; they could be true. It does not mean that the unauthorized distillation of AI models does not raise legitimate intellectual property issues; it does. It simply means that the moral posture of the accuser is undermined by its own history. Can one build a castle on sand and then complain that someone has pitched a tent on it without asking permission?

In short, do the truth and substance change if you are dressed in a Hanfu and work in a cubicle in Hangzhou or if you wear a colorful polo shirt and work in an open space in San Francisco?

De Gregori, in '92, in a historical context of great friction and change, posed an almost circular question, which in its breadth returns very modern today in 2026. The chorus of that song does not give answers, it only asks a question. *Which side are you on? Are you on the side of those who steal in supermarkets? Or of those who built them, stealing?*
