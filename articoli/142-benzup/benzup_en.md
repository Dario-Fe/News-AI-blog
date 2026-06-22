---
tags: ["Applications", "Ethics & Society", "Generative AI"]
date: 2026-06-22
author: "Dario Ferrero"
---

# BenzUp: I created an app without writing a single line of code
![benzup.jpg](benzup.jpg)

*There is a precise moment when an idea stops being a bar fantasy and becomes something concrete. In my case, that moment had as protagonists, in order: the cost of gasoline, an American engineer annoyed by an expensive beer in Dublin, and an artificial intelligence model accessible to anyone with an internet connection. The result is called [BenzUp](https://benzup.netlify.app), it is free, it does nothing revolutionary, and perhaps that is exactly why it is worth telling.*

In recent weeks, among friends, colleagues, and acquaintances, the theme of high fuel prices had become a permanent presence in conversations. Not an absolute novelty, mind you: the price of gasoline has always been one of the national topics par excellence, with all due respect to those who would like to talk about something else. But the current international situation had further raised the volume of the debate, and one often found oneself wondering where it was best to fill up, which stations were most honest, if it was worth driving a few more kilometers to save a bit. Legitimate questions, to which no one had a quick and verifiable answer.

Meanwhile, I observed, took mental note, and did nothing. As one does with most good ideas: you let them settle until something comes along to unblock them.

## Along comes the Guinness

The unblock came one morning in the form of news I never imagined I would read. Matt Cortland, an American engineer with Irish roots and based in London, had found himself paying 7.80 euros for a pint of Guinness in a pub in Dublin. A figure that, for those who know the almost sacred relationship between the Irish and their national beer, is little less than an insult. Investigating, Cortland discovered that the Irish Central Statistics Office had stopped monitoring beer prices in 2011, leaving an information vacuum of fourteen years. His reaction? To build a voice agent called Rachel, endowed with a Northern Irish accent, which on St. Patrick's weekend 2026 called about 2,300 pubs in all 32 counties of the island asking only one question: how much does a pint of Guinness cost? The cost of the entire operation: about two hundred euros. The result: the [Guinndex](https://guinndex.ai), an interactive map of Guinness prices in Ireland, processed via Anthropic's Claude starting from over 1,200 collected responses. Most common price detected: 5.50 euros per pint. Absolute record: 11 euros at The Temple Bar Pub in Dublin, which confirms its vocation for plucking tourists with an almost admirable consistency.

Cortland's stated goal is explicit: "I want to see if we can collectively lower the cost of a pint across Ireland." The Guinndex has become an open crowdsourced platform, where anyone can report prices and contribute to keeping it updated. And some initial signs of falling prices are there, but for now it's hard to correlate to the initiative.

The story is nice, the idea is brilliant, the execution is elegant. But above all, reading it made that spring snap that had been waiting for weeks. If someone had used AI to map the price of beer across Ireland spending two hundred euros, I could use it to build something useful for drivers without spending even a cent. I didn't have the ambition to make the price of gasoline fall, as it was in Cortland's hope to make that of Guinness fall, but at least I could give a quick orientation on where it was worth stopping.
![screenshot-guinndex.jpg](screenshot-guinndex.jpg)
[Screenshot of Guinndex.ai](https://guinndex.ai/)

## The data was already there, for free

Before diving headlong into development, some online research is always required. And here comes the first pleasant surprise: the Ministry of Enterprises and Made in Italy publishes every morning, in an open format downloadable by anyone, the fuel prices charged by all Italian distributors. Two CSV files, updated daily, containing the complete registry of active plants throughout the national territory, with address, GPS coordinates, manager and brand, and the prices communicated by the managers, distinguished by type of fuel and by delivery method, self-service or served. The data are released under IODL 2.0 license, which allows free reuse even for commercial purposes, provided the source is cited. The Ministry does not merely tolerate the use of these data: it actively encourages it.

It was exactly what I needed. No scraping, no legal gray areas, no dependence on third-party APIs that could change terms of use overnight. Official, open data, updated every morning.

At that point, I decided to stay small and focused: no national app, no scaling ambitions. Only my province, the VCO, that VB initials in the Ministry data, filtered and served in a simple and fast way. A light prototype to see if the thing really worked.

## The prompt as a design act

Those who work with AI in even a semi-regular way know that output quality depends to a decisive extent on input quality. A vague prompt produces vague results. This is not an article on prompting, but it's worth dedicating a paragraph to it, because it was the most artisanal part of the entire experience.

I put down the requirements with a certain precision. On the technical side: a web app in pure HTML, CSS, and JavaScript, with a serverless function on Netlify to manage calls to MIMIT and avoid CORS problems that prevent browsers from making direct requests to external domains, responsive design optimized for mobile, data filtering on the VCO province, two rankings ordered by price from least expensive to most expensive, one for gasoline and one for diesel. On the interface side: a visible toggle to switch from one fuel to another, essential information for each distributor, a detail panel accessible by tapping the single plant, reference date and source highlighted. On the aesthetic side: modern style, polished typography, sober palette, something that looked designed and not generated.

I deliberately chose to use Claude Sonnet 4.6, the version accessible for free, precisely because I wanted to test what was possible to do with tools available to anyone, not just those with a premium subscription or senior developer skills. If it worked with the free model, the story made sense even for those reading without a technical background.

In a couple of minutes, about 750 lines of code. An HTML file with everything included: structure, style, logic, error handling, animations, detail panel with swipe to close. I had previously used AI models to write small pieces of code, some functions, an isolated component. Never, however, something of this complexity in one shot. The first surprise was opening that file in the PC browser: everything worked exactly as I had described it. Correct layout, toggle between gasoline and diesel, detail panel, smooth animations. Obviously without real data, but the structure was exactly as requested.

## From browser to production

Having an HTML file that works locally is one thing. Having it online, with real data coming from the Ministry, is another. This is the step where a minimum familiarity with available tools made the difference.

I created a repository on GitHub, uploaded the files, linked the repository to my Netlify account. Netlify automatically detected the configuration, activated the serverless function that downloads and filters MIMIT CSVs, and in a few minutes the app was online. Second surprise: it worked. Data were arriving, VCO province distributors appeared ordered by price, the toggle between gasoline and diesel responded as expected.

At that point, I did something I always recommend when working with AI-generated code: a cross-check with another tool. I connected Jules, Google's asynchronous AI agent integrated directly into GitHub, and asked him for a code analysis. Jules did not report relevant issues, which is not an absolute guarantee but is still a second pair of computational eyes on the work done.

With Jules I then made some integrations that made the app more like a native application. A JSON manifest file was added that allows installation on the phone directly from the browser, without going through stores, a custom icon, and a page dedicated to useful information, with an explanation of how it works, data provenance, system limits, and instructions for installation on Android and iPhone. That page, as we will see, proved more important than expected.
![benzup-screenshot.jpg](benzup-screenshot.jpg)
[Screenshot of BenzUp](https://benzup.netlify.app)

## Limits are part of the product

One day of personal testing, then spreading to a circle of friends with an explicit request to report any problems. The feedback was positive, but a recurring report arrived: the prices of some distributors seemed stuck for days. No app bug, simply the reality of the system: managers are required by law to communicate price changes to the Ministry, but not everyone does it daily. In addition, data are published every morning referring to 8:00 AM of the previous day, and the actual update in the app can slip by a few hours due to Ministry publication times and the technical infrastructure on which the app is hosted, over which I have no direct control.

That report led to improving the information page, adding a clear explanation of these mechanisms and indicating that by tapping a single distributor's card you can verify the date of the last update sent to the Ministry. Transparency is not an optional, it is an integral part of a service based on public data and that has no interest in appearing more precise than it is.

A precise request also arrived: to add LPG and methane, fuels that for many motorists in the province are anything but secondary. In the following days I integrated them, and now BenzUp shows rankings for all four fuel types.

## Three days, 800 visits

The app has been online for three days as I write this article (April 11, 2026). I launched it with a post on the local blog I have managed for many years, [Verbania Notizie](https://www.verbanianotizie.it), no paid advertising, no campaign, no growth strategy. In three days, about 800 visits. Figures insignificant on a national scale, probably irrelevant even on a local scale if measured with digital marketing parameters. But that's not the point.

The point is that from an idea born in a conversation on high fuel prices to a functioning app in production, consulted by hundreds of real people in my province, less than a week passed. Without writing a line of code, without a budget, without a development team. With a knowledge of the ecosystem of free digital tools available, a carefully constructed prompt, and the willingness to iterate, correct, improve based on real feedback.

## Updates

This story had the pleasure of being published in Codemotion's magazine, so I'm publishing it on the portal today, two months after it was written, so a brief update is in order.

In the two months since this article was written, BenzUp has continued to evolve, always following the same philosophy: no costs, no complex infrastructure, everything built with the free tools already available.
The most significant development is its geographical expansion: the app now covers the entire Piedmont region, with all eight provinces and the ability to filter by municipality via a dedicated menu. From a hyperlocal tool designed for drivers in the VCO area, it has become a reference for anyone traveling in or passing through the region.

On a technical level, the architecture has been substantially redesigned. Data is no longer processed in real time with each request, but pre-generated every morning in static files served directly from the Netlify CDN, with an immediate and measurable impact on loading speed. A GitHub Action automatically schedules the process, checks that the Ministry has actually published updated data before proceeding, and generates a JSON file for each province. The frontend reads the correct file and displays it instantly, without using any serverless functions.

A traffic light system has also been added to indicate the freshness of each individual distributor's data: green if the price was updated in the last 24 hours, yellow within 48 hours, and red after that. This is a simple and visual way to provide users with information that previously required opening each distributor's detailed page.

Finally, a reporting form accessible from each distributor's page allows users to report any discrepancies, out-of-date prices, closed plants, or data errors. This small measure of collective quality is consistent with the voluntary and transparent nature of the project.

## Final considerations

This is not a hymn to vibe coding, that practice of generating code quickly and approximately by blindly trusting AI without understanding what you are doing. Vibe coding, moreover, seems already on its way to being surpassed by a more structured and professional approach: writing project specifications in detailed markdown files, to be passed to code agents as precise and verifiable instructions, instead of relying on improvised prompts. I spoke about it in an [article on this same portal](https://aitalk.it/it/codespeak.html), and the difference in terms of control and quality of the result is substantial. But that is truly another story. What I want to tell is something simpler and perhaps more interesting: AI has radically reduced the distance between idea and its realization, even for those without specific programming skills.

This does not mean that programmers, engineers, and software architects have become superfluous figures, on the contrary. Bringing a working prototype to production is one thing, building something stable, secure, and scalable is another: for that real skills, experience, and deep understanding of systems are needed that no prompt, however well constructed, can replace.

In my case, some familiarity with online tools and a curiosity as an evolved user, not an expert, allowed taking the project to production instead of stopping at prototype. But the threshold has lowered for everyone. Anyone with a clear idea, the patience to build a decent prompt, and the desire to learn the minimum mechanisms of deploy on platforms like Netlify or Vercel, can do the same.

Somewhere in the world, someone with the right idea, a bit of initiative, and a free account on Claude is probably building right now something that doesn't exist yet. Not the new Facebook, perhaps, but something useful for the people around him. And that seems like enough to me already.

Meanwhile, if you are a Piemonte driver (for now) and want to know where to fill up while spending less, [BenzUp is there](https://benzup.netlify.app) waiting. Free, independent, with all its well-declared limits.

And if it should break through and end with a billion-dollar exit towards some Silicon Valley big tech, I'll wait for you all at the big party I'll give in my mega villa on the shores of Lake Maggiore, because, even if filthy rich, I'll stay faithful to where it all began.
