---
tags: ["Copyright", "Business", "Ethics & Society"]
date: 2026-02-23
author: "Dario Ferrero"
youtube_url: "https://youtu.be/f075qm6r0Rk?si=nQd4Am2RItXsp9ig"
---

# Cosa c'entra De Gregori con la guerra dell'AI?
![degregori-ai-war.jpg](degregori-ai-war.jpg)

*C'è una canzone di Francesco De Gregori del 1992, dall'album "Canzoni d'amore", che forse pochi ricordano, nel vasto e poetico catalogo del cantautore romano. Si intitola "Chi ruba nei supermercati?", e il suo ritornello pone una domanda che all'epoca era terribilmente attuale e sociologica: "Tu da che parte stai? Stai dalla parte di chi ruba nei supermercati? O di chi li ha costruiti, rubando?" Trentaquattro anni dopo, quella domanda risuona stranamente attuale in un contesto che De Gregori, pur nella sua straordinaria capacità di leggere il mondo, non avrebbe potuto immaginare: la guerra tecnologica tra le più grandi aziende di intelligenza artificiale del pianeta.*

## Il memo e il terremoto

Il 12 febbraio 2026, OpenAI ha inviato un memorandum alla House Select Committee on Strategic Competition between the United States and the Chinese Communist Party, il comitato bicamerale del Congresso americano dedicato alla competizione strategica con la Cina. Il contenuto di quel documento, [riportato da Reuters](https://finance.yahoo.com/news/openai-accuses-deepseek-distilling-us-221629899.html) e da [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-12/openai-accuses-deepseek-of-distilling-us-models-to-gain-an-edge), è una accusa diretta: la startup cinese DeepSeek avrebbe utilizzato tecniche di *distillation* per addestrare i propri modelli sfruttando gli output di ChatGPT, aggirando deliberatamente i sistemi di sicurezza di OpenAI attraverso router di terze parti e tecniche di offuscamento per nascondere la provenienza degli accessi.

"Abbiamo osservato account associati a dipendenti di DeepSeek che sviluppavano metodi per aggirare le restrizioni di accesso di OpenAI", si legge nel memo secondo quanto riportato da Reuters, "e sappiamo che dipendenti di DeepSeek hanno sviluppato codice per accedere ai modelli AI statunitensi e ottenerne gli output per la distillation in modi programmatici."

Per capire perché questa accusa abbia fatto rumore, bisogna tornare a gennaio 2025, quando DeepSeek aveva scatenato quello che molti osservatori avevano ribattezzato il "momento Sputnik" dell'intelligenza artificiale cinese. La startup di Hangzhou, fondata da Liang Wenfeng e finanziata esclusivamente dal suo hedge fund High-Flyer, aveva rilasciato i modelli [DeepSeek-V3](https://api-docs.deepseek.com/news/news1226) e [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120), capaci di competere con i migliori modelli americani a una frazione del costo dichiarato: meno di sei milioni di dollari di potenza computazionale, contro i miliardi che OpenAI, Anthropic, Meta e Google continuavano a investire nelle proprie infrastrutture. Il costo di addestramento di R1, come documentato da [analisi indipendenti](https://www.reuters.com/technology/artificial-intelligence/what-is-deepseek-why-is-it-disrupting-ai-sector-2025-01-27/), era stato dichiarato in meno di sei milioni di dollari impiegando chip Nvidia H800, ovvero la versione "declassata" degli H100 che gli Stati Uniti avevano già vietato di esportare in Cina.

L'effetto sui mercati era stato immediato e brutale: Nvidia aveva bruciato in pochi giorni circa 600 miliardi di dollari di capitalizzazione. La narrazione dominante, quella secondo cui dominare l'AI richiedesse necessariamente miliardi di investimenti in chip e data center, sembrava improvvisamente fragile.

## Come funziona la distillation

Prima di procedere, è necessario chiarire cosa sia esattamente la *distillation*, perché il termine, come spesso accade nella comunicazione tech, viene usato in modo impreciso tanto dai detrattori quanto dai difensori di DeepSeek.

Nel senso tecnico più proprio, la distillation è un processo per cui un modello più piccolo e leggero, lo "studente", viene addestrato a replicare il comportamento di un modello più grande e potente, il "maestro". [Come spiega OpenAI stessa](https://finance.yahoo.com/news/openai-accuses-deepseek-distilling-us-221629899.html) nel memo al Congresso, la tecnica "implica che un modello AI più vecchio, più consolidato e potente valuti la qualità delle risposte prodotte da un modello più nuovo, trasferendo effettivamente i risultati dell'apprendimento del modello più vecchio al più nuovo." In termini più concreti: invece di imparare dal mondo attraverso miliardi di testi umani, lo studente impara dalla saggezza già distillata nel maestro.

La tecnica in sé non è né nuova né illegale. È uno strumento standard del campo: lo stesso DeepSeek, nel suo [paper tecnico su R1](https://arxiv.org/abs/2501.12948), descrive apertamente come abbia creato versioni distillate del proprio modello per renderle accessibili su hardware meno potente, utilizzando GRPO (Group Relative Policy Optimization) come framework di reinforcement learning al posto del più convenzionale RLHF. Il paper, firmato da DeepSeek-AI e 199 co-autori, descrive un processo di addestramento multi-stadio che integra reinforcement learning, supervised fine-tuning e, appunto, distillation *dei propri modelli verso versioni più piccole*.

Il punto della controversia non è quindi la tecnica in sé, ma il suo obiettivo: OpenAI sostiene che DeepSeek avrebbe distillato *output di ChatGPT*, ovvero avrebbe usato le risposte del modello competitor come materiale di addestramento per il proprio. I [Termini di Servizio di OpenAI](https://openai.com/policies/row-terms-of-use/) vietano esplicitamente di utilizzare gli output dei suoi servizi "per sviluppare modelli che competono con OpenAI."

## DeepSeek non risponde. Il silenzio come risposta

Di fronte alle accuse di febbraio 2026, DeepSeek non ha risposto alle richieste di commento da parte di Reuters. Non è la prima volta: anche a gennaio 2025, quando le prime voci sulla distillation erano emerse sul *Financial Times*, la risposta della startup cinese era rimasta elusa o vaga.

Il silenzio è significativo ma non univoco. Può essere strategia legale, indifferenza calcolata, o semplicemente la scelta di una startup che non vuole legittimare le accuse di un competitor rispondendo sul suo terreno. Ciò che rimane è una domanda aperta: quali prove concrete ha OpenAI, al di là del fatto che gli account sospetti "erano associati a dipendenti DeepSeek"?

Dal punto di vista tecnico, la questione è tutt'altro che risolta. DeepSeek ha pubblicato i dettagli del proprio processo di addestramento in un paper peer-reviewed su arXiv. Come [documentato nell'analisi di arxiv 2501.12948](https://arxiv.org/abs/2501.12948), il modello R1-Zero era stato addestrato esclusivamente tramite reinforcement learning senza supervised fine-tuning iniziale, partendo dal modello base DeepSeek-V3. I benchmark indipendenti mostravano performance paragonabili a OpenAI-o1 su task di ragionamento matematico e coding. Il fatto che risultati simili fossero raggiungibili con architetture e metodologie diverse, e a costi nettamente inferiori, è parte della ragione per cui la storia aveva generato tanto scalpore.

Detto questo: la trasparenza di un paper tecnico non esclude l'uso parallelo di tecniche non documentate. E l'assenza di risposta di DeepSeek non è una dimostrazione di innocenza.

## Il boomerang legale

Alla luce di tutto questo, il nodo più interessante, e più imbarazzante per OpenAI, è quello legale. Come analizzato nel dettaglio dagli esperti della [Santa Clara Business Law Chronicle](https://www.scbc-law.org/post/code-claims-and-consequences-the-legal-stakes-in-openai-s-case-against-deepseek), OpenAI si trova in una posizione processuale straordinariamente scomoda se decidesse di procedere per vie legali. Per sostenere una causa per violazione di proprietà intellettuale, dovrebbe convincere un tribunale che gli output di un modello AI godono di protezione copyright, ovvero che le risposte generate da ChatGPT sono espressione creativa tutelabile.

Il problema è che OpenAI ha costruito buona parte della propria difesa nel caso intentato dal *New York Times* esattamente sull'argomento opposto: lo scraping di contenuti altrui per addestrare i propri modelli è "fair use", ovvero un uso legittimo che trasforma il materiale protetto e originale in qualcosa di "libero" se l'uso è finalizzato a critica, commento, informazione, insegnamento o ricerca.

Non si può invocare il copyright sugli output propri dopo aver negato lo stesso principio agli autori umani il cui lavoro ha reso possibile quegli output. Lo stratagemma è logicamente circolare, e gli esperti legali lo hanno notato immediatamente. "È come se la scarpa del contenuto-appropriato fosse finita sull'altro piede", ha scritto *Business Insider* citando pareri di esperti legali raccolti subito dopo le prime accuse del gennaio 2025. OpenAI potrebbe invece tentare la strada del breach of contract, violazione dei Termini di Servizio, ma anche qui si scontra con la difficoltà di far eseguire una sentenza americana su un'azienda con sede a Hangzhou, in un sistema legale con il quale gli accordi di reciprocità sono inesistenti o deficitari.

Il risultato, come conclude l'analisi legale della Santa Clara Law, è che "la combinazione di precedenti scarsi e complicazioni geografiche porta alla conclusione che una causa, e un esito favorevole, sarebbe estremamente raro e difficile da ottenere per OpenAI."

## Il supermercato e i suoi architetti

Ed è qui che la storia si complica in modo sistemico. Perché l'accusa di OpenAI a DeepSeek non può essere letta senza il contesto di quello che OpenAI, e non solo lei, ha fatto per costruire i propri modelli.

Nel dicembre 2023, il *New York Times* ha intentato una [causa contro OpenAI e Microsoft](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward) per violazione di copyright, sostenendo che milioni di articoli del giornale fossero stati utilizzati per addestrare ChatGPT senza autorizzazione né compenso. A marzo 2025, un giudice federale del Southern District of New York, Sidney Stein, ha [respinto la richiesta di OpenAI di far archiviare il caso](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward), permettendo alle principali rivendicazioni di procedere verso il processo. Il giudice ha ristretto alcune delle accuse ma ha lasciato in piedi la sostanza: la questione se lo scraping massiccio di contenuti giornalistici protetti da copyright costituisca fair use è ancora sub judice.

Non è un caso isolato nel panorama delle cause legate all'addestramento dei modelli AI. Nel ottobre 2025, Reddit ha depositato una [causa contro Perplexity AI e tre aziende di data scraping](https://www.cnbc.com/2025/10/23/reddit-user-data-battle-ai-industry-sues-perplexity-scraping-posts-openai-chatgpt-google-gemini-lawsuit.html), Oxylabs, AWMProxy e SerpApi, accusandole di aver estratto miliardi di post degli utenti nascondendosi dietro le protezioni tecniche di Reddit attraverso i risultati di Google Search. Il Chief Legal Officer di Reddit, Ben Lee, aveva coniato un'espressione particolarmente efficace: "data laundering", ovvero lavaggio di dati. "Le aziende di AI sono chiuse in una corsa agli armamenti per contenuti umani di qualità", aveva dichiarato, "e quella pressione ha alimentato un'economia industriale su scala di 'data laundering'."

Va notato che Reddit aveva già stretto accordi di licenza con Google e con OpenAI stessa: il problema, nel caso Perplexity, era l'approvvigionamento dei dati attraverso terzi senza pagare. Ma la stessa OpenAI aveva costruito i propri modelli su corpus che includevano contenuti non licenziati: le [class action intentate da autori e scrittori](https://cointelegraph.com/news/open-ai-microsoft-accused-stealing-data-train-chat-gpt-artificial-intelligence-lawsuit) per l'uso non autorizzato di testi letterari durante l'addestramento di GPT ne sono una traccia documentata.

Il meccanismo è identico a quello che OpenAI imputa a DeepSeek: usare il lavoro intellettuale altrui per costruire un sistema commerciale senza permesso e senza pagare. La differenza, agli occhi di OpenAI, è che loro l'hanno fatto con testi umani mentre DeepSeek l'avrebbe fatto con output di un modello AI, una distinzione che ha qualcosa di ridondante: quei modelli AI sono ciò che sono perché hanno assorbito lavoro umano non autorizzato.

## Geopolitica, chip e il memo al Congresso

Il memo di OpenAI al Congresso non è solo una questione tecnico-legale. È un atto politico, indirizzato al comitato che sovrintende alla competizione strategica con la Cina, scritto in un momento in cui l'amministrazione Trump stava ridefinendo la propria postura verso l'export di tecnologia.

David Sacks, nominato "AI and crypto czar" dalla Casa Bianca, aveva già messo le mani avanti a gennaio 2025 dichiarando a Fox News che "ci sono prove sostanziali che quello che ha fatto DeepSeek è distillare la conoscenza dai modelli di OpenAI." Il congressman John Moolenaar, presidente del House Select Committee on China, [secondo Gigazine](https://gigazine.net/gsc_news/en/20260213-openai-accuses-china-deepseek/) aveva usato toni ancora più accesi: "Questo fa parte della strategia del Partito Comunista Cinese: rubare, copiare e distruggere."

OpenAI aveva anche aggiunto, nel memo, una nota preoccupante sulla sicurezza: quando un modello viene replicato tramite distillation, i meccanismi di sicurezza del modello originale tendono a non essere trasferiti, lasciando potenzialmente una versione meno filtrata circolante sul mercato, con rischi per i cosiddetti settori ad alto pericolo come biologia e chimica. È un argomento legittimo. È anche un argomento che serve a colorare di toni più cupi un caso che sul piano strettamente legale è molto meno solido.

Dall'altra parte, la prospettiva di molti osservatori asiatici inquadra le accuse di OpenAI come protezionismo tecnologico mascherato da questioni etiche. DeepSeek ha dimostrato che era possibile costruire modelli competitivi con risorse computazionali nettamente inferiori, aggirando di fatto il vantaggio strutturale che le restrizioni all'export di chip Nvidia avrebbero dovuto garantire all'industria americana. Se le accuse di distillation diventassero un pretesto per ulteriori blocchi normativi, si tratterebbe di rispondere a una sconfitta tecnica con strumenti politici.

## Tu da che parte stai?

Torniamo quindi a De Gregori, e alla domanda che aveva lasciato in sospeso.

La struttura narrativa di questa vicenda è quasi troppo perfetta nella sua simmetria imbarazzante. OpenAI accusa DeepSeek di aver usato i suoi modelli senza permesso per costruire qualcosa di competitivo. Ma OpenAI ha costruito quei modelli usando il lavoro di giornalisti, scrittori, autori, programmi Reddit, thread di discussione e corpus interi di produzione intellettuale umana senza chiedere permesso né pagare. La causa del *New York Times* è ancora aperta nei tribunali americani. Le class action degli scrittori e degli autori si moltiplicano. Reddit sta trascinando in giudizio chi ha fatto esattamente quello che OpenAI aveva fatto con i testi umani.

Non è una questione di innocenza assoluta o di colpa assoluta. È una questione di chi stabilisce le regole del supermercato, chi può tenere la cassa, e chi viene fermato dalle guardie all'uscita. La distillation che OpenAI imputa a DeepSeek è moralmente e strutturalmente analoga allo scraping che OpenAI ha operato sui contenuti umani: entrambe sono tecniche per estrarre valore da un corpus altrui senza compensazione, usate per costruire sistemi commerciali potenti. La differenza principale, al momento, è una questione di potere: chi ha le risorse per definire la narrativa legale e politica, e chi no.

Questo non significa che le accuse di OpenAI siano false, potrebbero essere vere. Non significa che la distillation non-autorizzata di modelli AI non sollevi questioni legittime di proprietà intellettuale, le solleva. Significa semplicemente che la postura morale di chi accusa è minata dalla propria storia. Si può costruire un castello sulla sabbia e lamentarsi poi che qualcuno ci abbia posato sopra una tenda senza chiedere permesso?

Insomma, la verità e la sostanza cambiano se sei vestito con un Hanfudi e lavori in un cubicolo a Hangzhou o se indossi una polo colorata e lavori in un open space a San Francisco?

De Gregori, nel '92, in un contesto storico di grandi frizioni e cambiamenti, si poneva una domanda quasi circolare, che nella sua ampiezza torna modernissima oggi nel 2026.  Il ritornello di quella canzone non dà risposte, fa solo una domanda. *Tu da che parte stai? Stai dalla parte di chi ruba nei supermercati? O di chi li ha costruiti, rubando?*