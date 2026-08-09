---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-08-14
author: "Dario Ferrero"
---

# I Built Karpathy's LLM Wiki from Scratch on My Articles
![llm-wiki-autocostruita.jpg](llm-wiki-autocostruita.jpg)

*For a year, I have written on AiTalk, accumulating article after article a sort of personal diary on artificial intelligence. At a certain point, I found myself with 164 files in a folder, each full of concepts, names, companies, and models, all mentioned but never truly connected. I knew I had written something on a certain topic, but I couldn't remember where, and finding it meant opening files one by one, hoping for memory or a lucky "search in text". In short, an archive, not knowledge.*

The problem reminded me of certain scenes from *Memento*, the Christopher Nolan film in which the protagonist tattooed on his skin the facts he could no longer retain: every piece of evidence existed, isolated, without a thread holding it together with the rest. I had the same problem on a more modest scale—a text archive instead of tattoos—but with a similar feeling: information present, connection absent.

The solution I approached was not born of my own intuition, but from a well-known pattern circulating in the developer community under the name given by its creator, Andrej Karpathy: the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The idea, in short, is that instead of having a model search your documents every time you ask a question, you have it read the documents once, let it build structured and linked pages, and then let it consult that already compiled knowledge when you ask questions. I had already spoken about it in a [previous article](https://aitalk.it/it/llm-knowledge-base.html); here I wanted to tell the story of what happens when you stop talking about it and try to actually build it, with your 164 files, your errors, and your doubts.

I did not start as an expert in this type of system; I started as a curious person with a concrete problem to solve. What follows is an honest account of the journey, including the choices I discarded and those about which, even today, I am not entirely sure.

## The Method I Wasn't Looking For

The first temptation, when you have a problem of this type, is to rely on a script. I thought of concept extraction with libraries like spaCy or NLTK—a quick text analysis job. I discarded it almost immediately because those kinds of tools recognize entities and keywords, not the meaning of a reasoning spanning an entire article, and I needed exactly that.

I also thought of Obsidian, perhaps with some community plugins designed to build knowledge graphs. I had already tried it in the past for other projects, and the feeling was always the same: a layer of configuration between me and the result that took away more control than it added.

There remained the most trodden path, a classic RAG system with a vector database like Chroma or Weaviate. It works, it is proven, but it solves a different problem from mine: it retrieves text fragments relevant to each question, without ever accumulating comprehension that grows over time. Every query starts from scratch, much like the little fish Dory from *Finding Nemo*, who restarts her discovery of the world every few seconds. Cute as a character, less practical as a knowledge architecture.

I also looked at more elaborate solutions. [Graphify](https://aitalk.it/it/graphify.html), which I had written about in the past, builds knowledge graphs starting from syntactic parsing of code, designed for agents like Claude Code or Cursor on real codebases: a powerful tool, but oriented to a different use case than my pure markdown workflow. Microsoft GraphRAG seemed excessive for a personal project, with an infrastructure that I would have to maintain for years just to query my own articles. MeMex-Zero-RAG is ready for production, but designed for agents connected via MCP, not for autonomous use like mine. The community project obsidian-llm-wiki was closer to what I was looking for, but remained tied to Obsidian, and I wanted something even more minimal.

In the end, I discarded all the pre-packaged solutions, including those closest to my use case, and decided to build the pattern from scratch. Not out of snobbery toward existing tools, but simply because the idea of trying it with my own hands, more for play than out of necessity, seemed like the best way to truly understand how the mechanism works under the surface, with the opportunity to learn something along the way even if the final result was imperfect.

As an agent, I chose OpenCode, open source and agnostic with respect to the model, capable of working with both cloud providers and local models: not a pre-packaged solution for building wikis, just a good executor to entrust with the rules. I passed it the Karpathy pattern in its simplest form—a raw/ folder with immutable sources, a wiki/ folder with compiled knowledge—and started building everything else from there, one rule file at a time, without databases, without embedding systems to manage, and without infrastructure beyond the filesystem.

## How It Works, in Practice

The project lives in a simple structure: inside `raw/articoli/` are the 164 original markdown files; inside `wiki/` three subfolders have formed over time: `concepts/` for ideas and recurring themes, `entities/` for people, companies, and tools, and `synthesis/` for comparison and cross-cutting analysis pages, plus an `index.md` which acts as a general map and a `log.md` which logs every operation.

The core of the system is a file I called `AGENTS.md`, the compass that OpenCode consults before any intervention. There I wrote the basic rules: files in `raw/` remain immutable; each wiki page must have a cited source in the format `[Source: raw/file-name.md]`; links between pages follow the wikilink syntax `[[Page Name]]`; and each page carries a YAML frontmatter with title, creation and update dates, category, tags, and sources. I also added a minimum quality standard: each page must link to at least two other existing pages, otherwise it remains an orphan, isolated from the rest of the network.

Writing that file reminded me of the world-building work done in certain tabletop role-playing games, where before playing you must establish the rules of the world so that everything that happens afterward has internal coherence. `AGENTS.md` is exactly this: not content, but rules to generate content in a coherent way.
![immagine1 .jpg](immagine1 .jpg)
*AiTalk.it Wiki Structure Diagram*

## Ten Batches, Many Surprises

For the ingest work, I chose DeepSeek V4 Flash, free through OpenCode Zen—a pragmatic choice rather than an ideological one: the content was already public, so there were no privacy issues in passing it through a cloud service, and the model's speed suited a project of this scale well.

I proceeded in batches, numbering the files progressively and launching the same command each time: "process the next batch of files not yet processed following AGENTS.md", followed by a lint check to verify broken links, missing citations, and orphan pages. Ten batches in all, from the first fifteen files to the last twenty-four, with a decreasing yield of created pages batch after batch: many new pages at the beginning, when fundamental concepts had yet to take shape, fewer and fewer over time because most of the new information ended up enriching already existing pages rather than generating new ones. A sign, I believe, that the knowledge network was actually converging toward a stable structure.

The final result, at the end of the ten batches plus a targeted retrieval of files left behind, was 154 pages of content from 164 source articles: 68 pages of concepts, 80 of entities, 5 of synthesis, zero broken links, zero orphan pages, valid frontmatter on all 156 total pages (counting index and log), and an average of nearly eight links per page. The main hubs of the network, those with the most incoming links, turned out to be security-ai, large-language-models, AI regulation, and AI ethics: not a surprise, given how those themes recur across most of what I write, but seeing it confirmed by the very structure of the wiki was pleasing—almost a cross-proof of coherence in my own work.

The biggest surprise, however, came from looking at the disk space occupied: the entire project, all 154 pages plus index and log, weighs 4.4 megabytes. A RAG system with vector embeddings, for the same volume of articles, would probably have occupied between 50 and 200 megabytes, considering the indexes and vectors necessary for semantic search. Here, instead, there is only structured text—no chunks, no embeddings to save: the compiled knowledge even weighs less than the source articles that generated it. A wiki that fits comfortably on a USB stick, syncs via git in seconds, and moves to another computer with a simple copy-paste. It is hard not to think about this in relation to how, usually, the infrastructure around artificial intelligence has the opposite tendency—constantly growing in size and complexity.
![immagine2.jpg](immagine2.jpg)
*Screenshot of a query to the AiTalk.it LLM Wiki, via OpenCode and a cloud model (DeepSeek V4 Flash)*

## Where the Human Remains Necessary

It would be convenient to present the project as an automatic process, started and left to run until the final result. It wasn't like that, and this very point seems the most interesting to share.

During the ten batches, I had to intervene several times. Three files had been left behind, present only in the index and not yet processed, and I had to launch a targeted ingest to retrieve them. Some important entities, such as Dario Amodei, Elon Musk, Sam Altman, Jensen Huang, Hugging Face, Tesla, and Waymo, did not have their own page despite being mentioned in multiple articles—fifteen pages that I added later after realizing the gap only when querying the wiki. I corrected an encoding issue in a filename, fixed nineteen pages with the wrong update date, added a second source to thirty-one concepts that had only one, and integrated a conclusion section in four synthesis pages that lacked them.

None of these interventions were dramatic, but they all taught me something about the real limits of the system: when batches are large, with many files processed in a single session, the model tends to lose sight of minor details—much like what happens when you read too many chapters of a choral novel in a single sitting and end up confusing some minor characters. It reminded me of certain manga with dozens of characters introduced in the same story arc, where even the most attentive reader ends up losing some secondary threads, only to find them again several volumes later.

However, now that I have aligned the archive in the Wiki, from here on out, I will proceed with ingests of one article at a time instead of large batches. This is a hypothesis I have yet to verify in the field; my intuition is that precision will improve by managing less information per ingest, but I do not yet have enough data to say for sure. Nonetheless, the most important lesson of the entire journey remains: Karpathy's pattern is not total automation, but a collaboration between human and model, where the former supervises, corrects, and enriches what the latter generates.

## Same Wiki, Without the Cloud

Once the wiki was completed with the cloud model, I wondered if the entire system could also work offline, with a private model loaded on my computer. The reasons were varied: privacy, since in that case the data would never leave the machine; control, since I could choose any model without relying on an external provider; and costs, zeroed out once the model was loaded.

I used [LM Studio](https://lmstudio.ai/) as the local engine, with the server active on port 8001, and as a model, I chose Ornith 1.0 with 35 billion parameters, which I had written about in a [dedicated article](https://aitalk.it/it/ornith-1.0.html): in my trials, both in tests and in daily use, it proved to be the most precise among those tried, though it remains possible to select any other model loaded in LM Studio.

To connect OpenCode to the local server, I chose the manual path, modifying the configuration file directly with a new provider pointing to the local endpoint, instead of relying on the `opencode-lmstudio` plugin, which would have offered concrete advantages like automatic detection of loaded models and dynamic management of ports and endpoints. I chose the manual configuration for a practical reason—my use case involves occasional queries on an already complete wiki, not frequent model switching—and for a more personal reason: I wanted to fully understand what was written in that configuration file, without intermediaries. I recognize that for more dynamic use, with frequent architectural changes, the plugin would remain the most convenient choice.

The tests surprised me in a positive way. A simple question about a concept already covered, such as MTV, correctly found reference in the page dedicated to music and artificial intelligence. A more complex question, which asked to list the main companies in the sector and their respective CEOs while citing sources, produced an accurate response on eight companies, with citations correctly pointing to the compiled wiki pages and not to the original raw files—a sign that the model was actually using the structure I had built. It even identified two gaps on its own—Mark Zuckerberg being mentioned only marginally and Sundar Pichai being completely absent—an important detail to emphasize because the model actually found gaps during a search, and allowed me to fill them with a simple request.

The first response arrived slowly—the time needed to load the entire wiki context—subsequent ones much faster thanks to caching. I had to raise the context limit from 25,000 to 160,000 tokens to allow the model to read the entire structure without truncation, and I discovered that, unlike the cloud model used for ingest, the local one does not automatically follow the pattern unless you explicitly tell it to read `AGENTS.md` and draw only from the `wiki/` folder. A detail that seems small, but actually defines the difference between a relevant answer and a generic one.
![immagine3.jpg](immagine3.jpg)
*Screenshot of a query to the AiTalk.it LLM Wiki, via OpenCode and a local model (LM Studio + Ornith 1.0 35B)*

## What Is Still Missing

At the end of the journey, I take home more open questions than definitive certainties, and I believe that is how it should be. I learned that Karpathy's pattern works in practice, with entirely open source tools and without complex infrastructures; I learned that human supervision remains indispensable, not a temporary fallback waiting for better models; and I learned that the compactness of this approach, those 4.4 total megabytes, is not a marginal technical detail, but a quality that makes the project truly portable and shareable.

Questions remain to which I do not yet have answers. Will file-by-file ingest, which I have just started adopting instead of large batches, really improve precision as I believe, or will it only introduce more slowness without proportional benefits? I would like to automate adding to the wiki as soon as I publish a new article, instead of remembering weeks later. I would also like to add a section dedicated to language models as entities in their own right, ChatGPT and Claude first among them, today only mentioned in passing inside other pages.

Finally, there is a more fundamental question, the one that accompanied me throughout the journey: how much of this compiled knowledge really reflects what I think, and how much is already a synthesis of the model that has crept between me and my own articles. I do not have a definitive answer; for now, I limit myself to checking, correcting, and enriching, aware that the project itself is designed to improve by learning new things along the way, just as I am trying to do.
