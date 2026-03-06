---
tags: ["Ethics & Society", "Business", "Security"]
date: 2026-03-06
author: "Dario Ferrero"
---

# Pentagon: Anthropic Refuses, OpenAI Accepts, Who Downloads and Who Uninstalls, and Then?
![pentagono-anthropic-openai.jpg](pentagono-anthropic-openai.jpg)

*There are weeks that seem like decades, and the last one of February 2026 was one of those. Within ninety-six hours, Anthropic refused the conditions of the US Department of Defense, renamed "Department of War" by the Trump administration, was declared a risk to the national supply chain, ended up in the crosshairs of a presidential decree, saw its chatbot climb to the top of the American App Store, and announced it would appeal in court. OpenAI, meanwhile, signed an agreement with the same Pentagon in such a short time that its own CEO publicly called it "precipitous." Users responded in their own way: by uninstalling. The answer to the question of what will actually happen is, honestly, only one: we'll see.*

## The line no one wanted to draw

To understand what happened, we must start from what the Pentagon wanted and what Anthropic refused to grant. The heart of the dispute concerns [two precise red lines](https://techcrunch.com/2026/02/27/anthropic-vs-the-pentagon-whats-actually-at-stake/): the use of artificial intelligence for mass surveillance of American citizens, and the employment of fully autonomous weapons systems, capable of selecting and eliminating targets without human intervention. Dario Amodei held his ground even when Secretary of Defense Pete Hegseth set an ultimatum, 5:01 PM on Friday, threatening to declare the company a "supply chain risk."

The Pentagon's position, in its official formulation, was not to explicitly request killer drones. Spokesman Sean Parnell stated on X that the department has no interest in mass domestic surveillance nor in autonomous weapons, but that the request was simpler: to allow the Pentagon to use Anthropic's models for "all lawful uses." The point of friction is precisely there. Who decides what is lawful? Hegseth's answer was clear: certainly not the supplier.

The regulatory context does not help reassure. According to a [2023 Department of Defense directive](https://www.esd.whs.mil/portals/54/documents/dd/issuances/dodd/300009p.pdf), artificial intelligence systems can select and engage targets without human intervention, provided they pass certain standards and are approved by high-level officials. There is no categorical ban on autonomous weapons in the American military apparatus. Anthropic, knowing this framework, did not want its models to enter a system where "lawful use" could include, in the future, automated lethal decisions. The concern is not unfounded: an AI system positioned in high-risk contexts can commit irreversible errors with the speed of a processor. The difference between a model that advises and one that acts is, in certain scenarios, the difference between a correctable error and a catastrophe.

Hegseth responded with the axe. Trump issued a decree ordering all federal agencies to cease use of Anthropic technologies within six months. Anthropic announced it will contest the decision in court.

## The numbers that make noise

While official statements circulated, the most immediate response came from app stores, and the data is sufficiently verified to deserve detailed attention.

According to [Sensor Tower](https://techcrunch.com/2026/03/02/chatgpt-uninstalls-surged-by-295-after-dod-deal/), US uninstalls of ChatGPT increased by 295% on a daily basis on February 28. To contextualize: the typical daily uninstall rate of ChatGPT, measured over the previous thirty weeks, was 9%. It's not a fluctuation; it's a leap. ChatGPT downloads dropped by 13% on Saturday and an additional 5% on Sunday. On the opposite front, Claude saw its US downloads grow by 37% on Friday the 27th, the day of Amodei's refusal, and an additional 51% on Saturday the 28th. The consequence is that Claude reached the first position in the American App Store rankings, a jump of over twenty positions compared to February 22.

Appfigures, a second independent data provider, certifies that daily downloads of Claude in the USA exceeded those of ChatGPT for the first time ever on Saturday, with even higher growth estimates: +88% on a daily basis. Appfigures also reports that Claude was first among free iPhone apps in six countries: Belgium, Canada, Germany, Luxembourg, Norway, Switzerland, and the United States. Sensor Tower adds a particularly eloquent sentiment datum: one-star reviews on ChatGPT grew by 775% on Saturday the 28th, with a further doubling on Sunday. Five-star reviews dropped by 50% in the same period.

It must be said with methodological honesty that Similarweb observed that Claude downloads in the last week were about twenty times higher than January levels, but also specified that the increase could have causes other than the political issue. Attributing everything to Anthropic's ethical choice would be a simplification. The temporal coincidence, however, is hard to ignore.
![claude-chatgpt-chart-feb-2026.jpg](claude-chatgpt-chart-feb-2026.jpg)
[Image taken from techcrunch.com](https://techcrunch.com/2026/03/02/chatgpt-uninstalls-surged-by-295-after-dod-deal/)

## OpenAI, the hasty agreement, and guardrails under discussion

Sam Altman [admitted on X](https://x.com/sama/status/2027911640256286973) without much sugarcoating: the agreement with the Department of War had been "decidedly precipitous" and "prospects don't look good." It is a rare concession, that of a CEO publicly criticizing his own strategic decision while still defending it.

The timeline is this: Friday evening negotiations between Anthropic and the Pentagon collapse definitively; Saturday OpenAI announces its agreement for the deployment of models in classified environments. The speed generated immediate questions: did OpenAI really have the same red lines as Anthropic? If so, how had it managed to sign where Anthropic had failed?

OpenAI responded with [a post on its blog](https://openai.com/index/our-agreement-with-the-department-of-war/), listing three areas excluded from the agreement: mass domestic surveillance, autonomous weapons systems, and high-risk automated decisions. The company argued that, unlike other operators who would have "reduced or removed their safety guardrails" in military implementations, its approach is multi-layered: full control over the security stack, exclusive deployment via cloud, OpenAI personnel with security clearance involved in the process, and "robust" contractual protections. Katrina Mulligan, head of national security partnerships, argued on LinkedIn that limiting deployment to the cloud API physically prevents the integration of models into weapons systems: a model accessible only via cloud has an architectural distance from control systems that a locally installed model does not have. It is a technical argument not without logic.

However, [Mike Masnick](https://bsky.app/profile/masnick.com/post/3mfxyktqgyp24) from Techdirt raised a concrete objection: the text of the agreement, complying with Executive Order 12333, could open the door to surveillance of American citizens. That executive order, dating back to the Reagan era, allows the capture of communications of US persons when they transit through international channels. If the OpenAI agreement refers to that order as a compliance standard, the word "protection" assumes blurrier contours than the press release suggests. OpenAI's response is that the deployment architecture, cloud-only, without direct integration into operational hardware, is worth more than contractual language. The debate, technically, is not closed.

Altman explained his logic in a way worth reporting: OpenAI hoped that the agreement would lower tension between the Department of War and the AI industry as a whole. If it worked, the company would appear as the one that had taken upon itself the cost of a difficult move in the interest of the sector. Otherwise, it would continue to seem precipitous. Altman recognized both possibilities.

## The trap of the unarmed prophet

There is a voice in this affair worth listening to carefully precisely because it is not tender with anyone. Max Tegmark, MIT physicist and founder of the Future of Life Institute, gave TechCrunch [an interview](https://techcrunch.com/2026/02/28/the-trap-anthropic-built-for-itself/) on the afternoon of the same Friday Trump signed the decree, and his analysis is a structural indictment.

The argument is this: artificial intelligence companies, Anthropic included, have for years resisted binding regulation, replacing it with voluntary self-governance commitments. The result is that today there is no regulatory framework protecting them when the government decides to demand uses they themselves consider dangerous. There is currently no law in the United States prohibiting building AI systems to kill Americans: the government can simply ask for it, and companies have no legal tools to oppose other than contractual ones, which the Pentagon considers non-binding as a matter of principle.

To this is added a circumstance that Tegmark emphasizes unsparingly: the same week as the clash with the Pentagon, Anthropic [modified its most important safety commitment](https://www.businessinsider.com/anthropic-changing-safety-policy-2026-2), the promise not to release increasingly powerful AI systems until the company was reasonably certain they would not cause harm. Removing it at this very moment is, at least, an awkward coincidence. Tegmark extends the criticism to the entire sector: Google has abandoned its historic commitment against using AI for surveillance and weapons; OpenAI has removed the word "safety" from its mission; xAI has closed its safety team. Voluntary commitments, he observes, tend to last until they become expensive.

## We'll see: open questions

We are in the position of those observing a match still in progress, knowing we have the data of the very first minutes. Intellectual honesty requires not making predictions as if they were certainties.

Will the ethical effect last? The spikes in downloads and uninstalls recorded by Sensor Tower and Appfigures are real, but user behavior in apps has a volatility that anyone working in the sector knows well. Those who use ChatGPT integrated into their corporate workflows do not move in a week. The question is not whether February 28 marked a moment, it did, it's whether that moment will be remembered in six months or forgotten in six weeks.

Will Trump's threats have concrete and lasting consequences? The decree exists, the designation as a "supply chain risk" exists, Anthropic's court appeal is announced. VC Sachin Seth of Trousdale Ventures told TechCrunch that losing Anthropic could create a vacuum in the American defense system that would take six to twelve months to be filled by other suppliers. This mutual dependency is, paradoxically, one of the few concrete protections Anthropic has now: it's hard to expel a supplier when you are the customer who needs it most.

What happens in July 2026, when the contract between OpenAI and the Department of Defense expires? It is a time window close enough to already be on the calendar of anyone thinking strategically in the sector. xAI has already signaled its readiness to operate in classified environments without the restrictions that characterize Anthropic and, to a lesser extent, OpenAI. The competition for the American military contract is not closed, and the fact that Elon Musk is simultaneously an advisor to the Trump administration and owner of one of the main competitors of Anthropic and OpenAI is not a negligible detail in the calculation of future probabilities.

There is then a geopolitical dimension that this affair brings to the forefront and that the American angle risks obscuring. Europe is watching. The European AI Act, the first binding regulatory framework on artificial intelligence in the world, having progressively entered into force, classifies AI systems used in military contexts separately from civilian application, effectively leaving the management of those uses to individual member states. But the political pressure exerted on companies like Anthropic, which has relevant teams in Europe and serves users worldwide, is not indifferent to the European regulatory debate. If the Trump administration manages to bend the security policies of an American company, what guarantees that the same pressures are not exerted, through different routes, on European companies or on European branches of American companies? It is a question that in Brussels they are already asking, even if in a more hushed way than the situation would deserve.

The analogy with the Cold War that Tegmark proposes deserves a brief final note. Like in the nuclear arms race, there is a point where the logic of "we must do it before the Chinese do" clashes with the elementary mathematics of mutual risk. China, he observes, is working to limit some forms of anthropomorphic AI, not to please the West, but because it considers them destabilizing for its own society. Those who argue that Beijing will never set limits on AI development ignore the regulatory moves that the Chinese government has already initiated in the opposite direction of total deregulation. It's not an argument for inaction, but it is a useful antidote to overly simplistic narratives.

Remains, at the center of everything, the question that no press release can solve: who has the last word when an artificial intelligence system is positioned close enough to a lethal decision to make the distinction between "advising" and "deciding" a matter of software architecture? It's not rhetoric. It's the question that blew up negotiations between Amodei and Hegseth, that pushed Altman to sign in haste, and that American judges will soon find themselves facing in forms that current codes do not contemplate.

Dario Amodei held his ground. Sam Altman signed. Users, for now, have rewarded those who said no. The Pentagon has its plans, Trump has signed the decree, judges will receive Anthropic's brief, and the OpenAI contract expires in July.

What will happen? We'll see.
