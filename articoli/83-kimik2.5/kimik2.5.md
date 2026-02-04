---
tags: ["Generative AI", "Research", "Ethics & Society"]
date: 2026-02-04
author: "Dario Ferrero"
youtube_url: "https://youtu.be/M70QIUSF1Po?si=FzqRM3Z71biE5UL4"
---

# Kimi K2.5 e la lunga marcia cinese nell'AI: quando l'embargo diventa trampolino
![kimik2.5.jpg](kimik2.5.jpg)

*C'è un momento, in ogni partita a scacchi ad alto livello, in cui si capisce che il giocatore sotto pressione non sta cercando di difendersi: sta costruendo una controgiocata. Qualcosa del genere sta accadendo nel grande gioco geopolitico dell'intelligenza artificiale, e il rilascio di Kimi K2.5 da parte di Moonshot AI non è l'ennesimo comunicato stampa da sfogliare distrattamente. È un altro capitolo di una storia che vale la pena seguire con attenzione, come nell'analisi precedente su [Qwen3-TTS](https://aitalk.it/it/qwen3-tts.html) e la generazione sintetica delle voci,  perché racconta e conferma come le restrizioni hardware imposte dagli Stati Uniti alla Cina stiano producendo esattamente l'effetto contrario a quello sperato: invece di rallentare l'innovazione cinese, la stanno accelerando lungo traiettorie impreviste.*

Ne avevamo già parlato analizzando [DeepSeek e la sua architettura MHC](https://aitalk.it/it/deepseek-mhc.html), e prima con [Kimi K2 Thinking](https://aitalk.it/it/kimi-k2-thinking.html). Oggi torniamo sul tema non per inseguire l'hype dell'ultimo modello uscito, ma perché ogni rilascio aggiunge un tassello a un mosaico che sta ridisegnando gli equilibri globali dell'AI. E Kimi K2.5, con i suoi mille miliardi di parametri organizzati in una architettura Mixture of Experts profondamente ottimizzata, rappresenta un salto qualitativo che merita più di una scrollata distratta su Hacker News.

## L'ennesimo rilascio che conta

Partiamo dai numeri, perché nell'AI i numeri raccontano storie. [Kimi K2.5](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart) è un mostro da un trilione di parametri totali, ma grazie all'architettura MoE ne attiva solo trentadue miliardi per ogni token generato. È come avere una biblioteca immensa dove, invece di sfogliare tutti i volumi ogni volta, selezioni automaticamente gli otto scaffali più rilevanti tra i trecentottanta disponibili, più uno scaffale condiviso sempre consultato. Questo approccio, tecnicamente definito "sparsity", non è nuovo ma Moonshot l'ha portato a un livello di raffinatezza impressionante.

L'architettura poggia su sessantuno layer di cui uno denso, con un meccanismo di attenzione chiamato MLA (Multi-Head Latent Attention) che riduce drasticamente i requisiti di memoria durante l'inferenza. La dimensione nascosta dell'attenzione è di 7168, mentre ogni esperto MoE lavora con 2048 dimensioni nascoste. Il vocabolario conta 160mila token e il contesto si estende fino a 256mila token, una finestra che permette di processare documenti lunghissimi o conversazioni articolate senza perdere il filo.

Ma il vero salto rispetto a K2 sta altrove. Moonshot ha integrato nativamente capacità multimodali attraverso MoonViT, un vision encoder da 400 milioni di parametri che permette al modello di "vedere" immagini e video non come add-on faticosamente innestati, ma come parte organica della sua comprensione del mondo. È stato addestrato su circa quindici trilioni di token misti, visivi e testuali, attraverso un continual pretraining sulla base di Kimi-K2-Base. Risultato: K2.5 non solo legge codice, lo genera guardando mockup di interfacce utente o analizzando workflow da video.

Salvatore Sanfilippo, uno degli sviluppatori più rispettati della comunità tech internazionale e creatore di Redis, ha analizzato K2.5 sottolineando proprio questo aspetto: "È un modello nativamente multimodale, addestrato specificamente per risolvere problemi di programmazione legati all'interfaccia utente agendo come un agente che 'vede' il layout". Non stiamo parlando di un trucco da demo, ma di una capacità progettuale che cambia il modo in cui si può interagire con l'AI nel lavoro quotidiano.

E c'è un altro elemento che Sanfilippo evidenzia come cruciale: la quantizzazione nativa a quattro bit. K2.5 è stato addestrato fin dall'inizio con tecniche di Quantization-Aware Training che permettono di farlo girare con circa 600-700 GB di RAM. Questo significa che un cluster di Mac Studio o server consumer con GPU relativamente accessibili può far girare un modello di frontiera attraverso inferenza distribuita. Non serve un datacenter da megacorporazione. È democratizzazione tecnologica concreta, non retorica.

## MoE, vision e agent swarm

Ma la vera novità di K2.5 sta in una funzionalità che suona fantascientifica ma è già operativa: l'agent swarm. Invece di far lavorare un singolo agente AI su task complessi, K2.5 può istanziare dinamicamente sciami di sub-agenti specializzati che collaborano in parallelo. È come passare da un artigiano solitario a una bottega rinascimentale dove ogni maestranza si concentra sulla sua parte del lavoro.

Il meccanismo si basa su una tecnica chiamata Parallel-Agent Reinforcement Learning (PARL): il modello scompone autonomamente un task complesso in sotto-obiettivi, genera agenti specializzati per ciascuno, e coordina la loro esecuzione. Nei benchmark come BrowseComp e WideSearch, K2.5 in modalità swarm supera nettamente non solo la sua versione single-agent, ma anche competitor come GPT-5.2 e Claude 4.5 Opus. Su BrowseComp con swarm attivo raggiunge il 78.4% contro il 60.6% in modalità standard. Su WideSearch passa dal 72.7% al 79%.

La configurazione prevede un agente principale che può eseguire fino a quindici step, mentre ogni sub-agente arriva fino a cento step. È orchestrazione computazionale che ricorda più un dirigente d'orchestra che un solista, e i risultati parlano chiaro: su task che richiedono ricerca web profonda, navigazione multi-pagina, o analisi di dataset articolati, l'approccio swarm sblocca livelli di prestazione prima inaccessibili.

Questo cambio di paradigma da single-agent scaling a swarm-like execution rappresenta forse il contributo più originale di Moonshot. Mentre OpenAI e Anthropic continuano a scalare modelli sempre più grandi e costosi, i cinesi stanno esplorando modalità di coordinazione distribuita che potrebbero rendere obsoleto l'approccio monolitico. È la differenza tra costruire grattacieli sempre più alti e progettare città orizzontali efficienti.
![orchestrator.jpg](orchestrator.jpg)
[Immagine tratta da kimi.com](https://www.kimi.com/blog/kimi-k2-5.html)

## Benchmark: prestazioni sul campo

Veniamo ai numeri che contano davvero: come si comporta K2.5 quando lo metti davanti a problemi veri? I benchmark rilasciati da Moonshot coprono uno spettro impressionante: ragionamento matematico, coding, visione multimodale, contesti lunghi, ricerca agentiva. E qui bisogna fare una premessa scomoda ma necessaria.

Come sottolinea ancora Sanfilippo, "i benchmark se li fanno da sé" e servirebbe "un ente asettico e distaccato che possa vagliare i risultati in modo indipendente". I produttori americani sono "completamente autoreferenziali", tendono a confrontare i nuovi modelli solo con le proprie versioni precedenti ignorando i competitor. I cinesi, al contrario, includono ancora i dati dei modelli americani nei test "per dimostrare di poter rivaleggiare con loro su scala globale". Moonshot non fa eccezione: pubblica confronti diretti con GPT-5.2, Claude 4.5 Opus, Gemini 3 Pro, DeepSeek V3.2.

Partiamo dal ragionamento. Su HLE-Full (Humanity's Last Exam), uno dei benchmark più tosti che misura capacità di problem-solving avanzato, K2.5 ottiene 30.1% senza tool e 50.2% con tool abilitati. GPT-5.2 raggiunge 34.5% e 45.5%, Claude 4.5 Opus 30.8% e 43.2%. Quando aggiungi la capacità di usare strumenti esterni, K2.5 sorpassa entrambi. Su AIME 2025, le olimpiadi di matematica americane, K2.5 ottiene 96.1% mediato su trentadue run, contro il 100% di GPT-5.2 ma sopra il 92.8% di Claude.

Sul fronte coding, i risultati sono ancora più interessanti. SWE-Bench Verified, che testa la capacità di risolvere bug reali da repository GitHub, vede K2.5 a 76.8%, GPT-5.2 a 80%, Claude a 80.9%. Distacco minimo. Ma su SWE-Bench Multilingual K2.5 sale a 73% contro il 72% di GPT e il 77.5% di Claude. E su Terminal Bench 2.0, che misura l'uso autonomo della shell, K2.5 raggiunge 50.8% battendo GPT-5.2 (54%) ma superando nettamente DeepSeek V3.2 (46.4%).

La parte visuale è dove K2.5 brilla davvero. Su MMMU-Pro, benchmark multimodale universitario, ottiene 78.5% contro il 79.5% di GPT e il 74% di Claude. Su MathVision, che richiede di risolvere problemi matematici da immagini, K2.5 raggiunge 84.2% battendo GPT (83%) e Claude (77.1%). Su WorldVQA, un benchmark creato proprio da Moonshot per testare conoscenza visiva del mondo reale, K2.5 ottiene 46.3% contro il misero 28% di GPT-5.2. E su video understanding, VideoMMMU vede K2.5 a 86.6%, VideoMME a 87.4%, LongVideoBench a 79.8%.

Sanfilippo, pur riconoscendo il rischio di data leakage (dataset finiti nel training), ritiene "i benchmark di Kimi storicamente affidabili" e suggerisce la soluzione più pragmatica: "Scaricarlo e sottoporlo a dieci problemi inventati sul momento. Solo verificando personalmente se il modello risolve problemi inediti è possibile capire se è forte come dicono". La natura open-weights di K2.5 rende questa verifica empirica possibile, a differenza dei modelli chiusi americani.
![benchmark1.jpg](benchmark1.jpg)
[Immagine tratta da platform.moonshot.ai](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart)

## Open source contro closed: partita geopolitica

Ed eccoci al punto cruciale, quello che trasforma questo rilascio da notizia tech a fatto geopolitico. Moonshot ha rilasciato i pesi completi di K2.5 su Hugging Face con licenza Modified MIT, estremamente permissiva. Puoi scaricare il modello, modificarlo, usarlo commercialmente. L'unico vincolo: se superi venti milioni di dollari al mese di ricavi o cento milioni di utenti attivi, devi citare esplicitamente Moonshot AI. Tutto qui.

Confronta questo con la strategia americana. OpenAI ha chiuso GPT-4, GPT-5 è ancora più blindato. Anthropic rilascia solo API di Claude, zero accesso ai pesi. Google mantiene Gemini sotto chiave. L'approccio è quello che alcuni chiamano "stratified openness": rilasci versioni minori open source (Llama di Meta, Gemma di Google) ma tieni i modelli di frontiera strettamente proprietari. L'obiettivo è controllare l'ecosistema, mantenere il vantaggio competitivo, monetizzare attraverso API a margini alti.

La Cina sta giocando una partita diversa. DeepSeek ha rilasciato i pesi di V3, Qwen fa lo stesso, Moonshot con K2.5 conferma il trend. Sanfilippo è esplicito: "I modelli cinesi sono attualmente l'unica garanzia per una futura democratizzazione dell'intelligenza artificiale. Mentre le società americane tendono a chiudere i loro modelli più forti per dominare il mercato, i cinesi continuano a rilasciarli".

La domanda è: perché? Non è filantropia. È strategia. Rilasciare modelli open-weights crea dipendenza tecnologica inversa: developer in Africa, Sud America, Europa Est iniziano a costruire su infrastruttura cinese. Quando tra tre anni quel developer sarà CTO di una startup cresciuta, su che stack pensi farà affidamento? E quando governi europei, latinoamericani, asiatici dovranno scegliere infrastrutture AI nazionali, penseranno davvero che affidarsi completamente a API americane chiuse sia una buona idea strategica?

Sanfilippo tocca questo nervo: "Il possesso dei pesi di Kimi 2.5 è una protezione contro possibili decisioni politiche arbitrarie, come un blocco dell'accesso all'AI americana da parte degli Stati Uniti. I governanti europei dovrebbero prestare molta attenzione a questi sviluppi come sfida strategica". Non è paranoia: abbiamo visto cosa è successo con Huawei, con TikTok, con le supply chain dei semiconduttori. Perché l'AI dovrebbe essere diversa?

C'è poi una questione più sottile. Sanfilippo difende il concetto di open-weights contro i puristi dell'open source: "Avere i pesi e il codice di inferenza è sufficiente per la libertà dell'utente, permette di continuare il training o creare sistemi di inferenza indipendenti". Non serve avere dataset completi e pipeline di training (che nessuno rilascia mai davvero, nemmeno Meta con Llama). Serve poter eseguire, modificare, estendere il modello. E questo K2.5 lo permette pienamente.

La community sta rispondendo. Il Reddit AMA del team Kimi ha visto centinaia di domande su fine-tuning, deployment locale, ottimizzazioni hardware. Together.ai ha già integrato K2.5 nella sua piattaforma. Sviluppatori stanno testando quantizzazioni diverse, creando adapter per framework specifici, pubblicando benchmark indipendenti. È un ecosistema che si autoalimenta, esattamente come accadde con Linux contro Windows negli anni Novanta.

## Hardware negato, software potenziato

E qui arriviamo al paradosso più delizioso di questa storia. Le restrizioni export USA sui chip avanzati dovevano paralizzare l'AI cinese. Invece l'hanno resa più resiliente e innovativa. È come negare carburante premium a un team di Formula Uno: non smettono di correre, progettano motori più efficienti.

Dal 2022 gli Stati Uniti hanno progressivamente bloccato l'export verso la Cina di GPU NVIDIA di fascia alta: prima A100, poi H100, recentemente anche H200. Le aziende cinesi possono accedere solo a versioni "downgraded" come H800 e H20, con banda memoria e interconnect ridotti, oppure devono affidarsi a hardware nazionale Huawei Ascend ancora immaturo.

La risposta? Architetture software che spremono fino all'ultima goccia di prestazioni da hardware inferiore. DeepSeek ha dimostrato che si può addestrare un modello competitivo usando principalmente H800. Moonshot con K2.5 porta questa filosofia oltre: MoE estremamente ottimizzato che attiva solo il 3.2% dei parametri totali per ogni token, quantizzazione nativa INT4 che riduce i requisiti memoria di quattro volte, tecniche di prefill e decoding che secondo la [documentazione ufficiale](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart) raggiungono uno speedup di 4.5x rispetto a implementazioni naive.

Sanfilippo inquadra perfettamente la questione: l'architettura MoE di K2.5 è "profondamente sparsa" proprio perché "per ogni token emesso se ne attivano solo 32 miliardi, coinvolgendo 8 esperti su un totale di 380". Questo significa training più efficiente su cluster H800/H20 meno potenti, e inferenza accessibile anche a chi non ha datacenter NASA.

C'è poi un aspetto che merita attenzione: Sanfilippo menziona "l'ipotesi che DeepSeek sia attualmente impegnato in un massiccio piano governativo cinese per il training su GPU Huawei", un possibile "Progetto Manhattan dell'AI" che spiegherebbe il rallentamento nei loro rilasci pubblici. Se confermato, significherebbe che la Cina sta puntando all'indipendenza hardware completa entro pochi anni. E quando succederà, le restrizioni export USA diventeranno irrilevanti.

Il confronto storico che viene in mente è quello con l'industria automobilistica giapponese negli anni Settanta. Quando l'embargo petrolifero colpì, Toyota e Honda non si arresero: progettarono motori più efficienti e conquistarono il mercato globale. Moonshot, DeepSeek, Alibaba stanno facendo lo stesso con l'AI. L'embargo sui chip sta creando i Toyota e gli Honda dell'intelligenza artificiale.
![benchmark2.jpg](benchmark2.jpg)
[Immagine tratta da kimi.com](https://www.kimi.com/blog/kimi-k2-5.html)

## Economie parallele e mercati emergenti

Passiamo ai soldi, perché alla fine è sempre una questione di soldi. Moonshot AI vale 3.6 miliardi di dollari secondo le ultime stime, con backing di Alibaba e altri investitori cinesi. Sembra tanto, finché non lo confronti con OpenAI (valutata oltre 150 miliardi), Anthropic (circa 30 miliardi), o Google e Microsoft che hanno capitalizzazioni nell'ordine dei duemila miliardi.

Sanfilippo nota la "forte discrepanza tra la forma (valutazione finanziaria) e la sostanza (capacità tecnica)". Moonshot produce un modello che compete con GPT-5 e Claude 4.5, ma vale un decimo di Anthropic e un quarantesimo di OpenAI. Perché? Mercati finanziari diversi, ecosistemi VC diversi, ma anche una monetizzazione meno aggressiva.

Guarda i prezzi API. K2.5 costa secondo fonti di terze parti $0.60 per milione di token in input, $2.50 in output. GPT-5.2 in modalità thinking viaggia su $1.75 input e $14 output per milione di token. Claude Opus 4.5 si attesta a $5 input e $25 output. K2.5 risulta quindi tre volte più economico di GPT-5.2 e circa otto volte più economico di Claude Opus 4.5 sull'input, con differenze ancora più marcate sull'output.

Per una startup in Vietnam, Nigeria, Argentina che vuole integrare AI nei propri prodotti, la scelta è ovvia. K2.5 non solo costa meno, ma essendo open-weights puoi anche hostarlo localmente se hai l'hardware, eliminando del tutto i costi API e la dipendenza da provider esterni. Questo sta creando economie parallele nell'AI, ecosistemi che crescono fuori dal circuito Silcon Valley-centrico.

L'impatto sui mercati emergenti è già visibile. Aziende indiane stanno costruendo chatbot customer service su Qwen e DeepSeek. Startup africane usano K2 per applicazioni educational locali. In Sud America developer stanno fine-tunando modelli cinesi per task specifici in portoghese e spagnolo. Non sono mercati glamour che finiscono su TechCrunch, ma sono volumi che crescono esponenzialmente.

E c'è un effetto rete perverso (dal punto di vista americano): più developer imparano a lavorare con modelli cinesi, più tool, framework, integrazioni nascono attorno a questi modelli, più diventa costoso switchare verso alternative americane. È lock-in al contrario. Microsoft e Google hanno costruito imperi su questo principio. Ora si trovano dalla parte sbagliata della barricata.

I numeri parlano chiaro: secondo dati di Andreessen Horowitz e OpenRouter, i modelli open-source cinesi sono passati dall'1,2% dell'utilizzo globale a fine 2024 a quasi il 30% entro dicembre 2025. Nikkei riporta che a novembre 2025 i modelli AI cinesi rappresentavano circa il 15% della quota di mercato globale, una crescita verticale dall'1% dell'anno precedente. Uno studio RAND Corporation evidenzia che ad agosto 2025 i provider cinesi avevano catturato oltre il 10% degli utenti in trenta paesi e oltre il 20% in undici paesi, principalmente in Asia, Africa e Sud America. Qwen di Alibaba ha superato i settecento milioni di download su Hugging Face, diventando il sistema AI open-source più utilizzato al mondo. Non abbastanza per spodestare OpenAI o Google nei mercati occidentali, ma sufficiente per rendere impossibile qualsiasi monopolio globale.

## Domande aperte sul futuro

Chiudiamo con le domande, perché nell'AI del 2026 le certezze sono merce rara e le domande sono più utili delle risposte preconfezionate. Prima questione: l'allineamento. I modelli cinesi open-weights seguono linee guida di sicurezza diverse da quelli americani, inevitabilmente riflettono valori culturali e politici del contesto in cui nascono. Quando K2.5 viene fine-tunato da una startup nigeriana o argentina, chi garantisce che gli allineamenti originali persistano? Chi decide quali guardrail sono necessari e quali sono censura?

Seconda questione: la roadmap. Moonshot parla già di K3, DeepSeek lavora a V4, Alibaba continua a iterare Qwen. La velocità di rilascio è impressionante, ma è sostenibile? Il training di questi modelli richiede energia mostruosa e datacenter enormi. La Cina ha energia a basso costo (carbone, nucleare, rinnovabili in espansione), datacenter in costruzione rapida, e un bacino di PhD in computer science più grande di Europa e USA messi insieme. Ma può mantenere questo ritmo mentre affronta rallentamento economico e tensioni geopolitiche crescenti?

Terza questione: regolamentazione. L'Europa ha approvato l'AI Act, che classifica modelli oltre certe soglie di parametri e capacità come "high-risk" richiedendo compliance stringente. K2.5 supera abbondantemente quelle soglie. Moonshot dovrà certificare il modello per il mercato europeo? E se lo fa, significa che l'open-weights avrà versioni diverse per giurisdizioni diverse, minando il concetto stesso di "open"?

Quarta questione: sicurezza nazionale. Se governi occidentali iniziano a percepire modelli cinesi come vettori di influenza strategica, potremmo vedere restrizioni all'uso di K2.5, DeepSeek, Qwen in settori sensibili. Già alcune agenzie governative USA vietano software cinese su device ufficiali. Estendere questo divieto ai modelli AI sarebbe tecnicamente complesso ma politicamente plausibile. E a quel punto, la biforcazione dell'ecosistema AI globale diventa permanente.

Quinta questione: il fattore Huawei. Se la Cina riesce davvero a sviluppare GPU Ascend competitive con NVIDIA, le dinamiche cambiano totalmente. Non più ottimizzazione software per aggirare limitazioni hardware, ma capacità end-to-end indipendente. Sanfilippo ipotizza che DeepSeek stia già lavorando su training massivo con chip Huawei, un "Progetto Manhattan" governativo. Se vero, tra dodici-diciotto mesi potremmo vedere modelli cinesi addestrati completamente su hardware nazionale, immunizzati da qualsiasi embargo futuro.

Infine: la questione della verità. Come verifichiamo le prestazioni reali di questi modelli? Sanfilippo suggerisce test empirici indipendenti, ma chi ha risorse per farlo sistematicamente? Serve davvero un CERN dell'AI, un ente internazionale neutro che testi modelli in condizioni controllate e pubblichi risultati verificabili. Finché non esiste, navighiamo tra claim autoreferenziali e benchmark potenzialmente leaked.

## Uno scacco che vale la partita

Torniamo all'immagine iniziale, quella della partita a scacchi. Gli Stati Uniti hanno mosso con l'embargo tecnologico pensando di mettere in scacco la Cina. La Cina ha risposto con una serie di contromosse inaspettate: architetture software più efficienti, rilasci open-weights strategici, ecosistemi developer che crescono fuori dal controllo Silicon Valley. Kimi K2.5 è una di queste contromosse, e non sarà l'ultima.

La valutazione di mercato ridicola rispetto alle capacità tecniche, secondo Sanfilippo, racconta una storia più profonda: "Moonshot AI vale 3,6 miliardi di dollari, una cifra molto bassa rispetto alle valutazioni fuori scala di OpenAI o Anthropic, nonostante la qualità del modello sia comparabile". Il mercato finanziario occidentale ancora non ha metabolizzato che l'AI non sarà un monopolio americano, che esistono traiettorie alternative, che il software può compensare (e ha compensato) limitazioni hardware.

Il rilascio di K2.5 non chiude la partita, ne apre nuove fasi. Developer globali ora hanno accesso a capacità multimodali avanzate, agent swarm, coding da vision, senza dipendere da API americane o budget enterprise. Governi hanno opzioni strategiche che non implicano sottomissione tecnologica a Washington. Ricercatori possono studiare, modificare, estendere un modello di frontiera senza chiedere permessi o firmare NDA impossibili.

Le domande aperte sono molte, le certezze poche. Ma una cosa è chiara: la geografia dell'intelligenza artificiale si sta ridisegnando, e pensare che questo ridisegno possa essere fermato con controlli export è ingenuo quanto pensare che un embargo petrolifero avrebbe fermato Toyota negli anni Settanta. La storia tecnologica premia chi innova sotto vincoli, non chi protegge rendite di posizione.

Moonshot AI, come dice il nome, punta alla luna. Se ci arriverà davvero è presto per dirlo. Ma intanto, mentre guardiamo, stanno costruendo razzi sempre migliori con materiali che non dovrebbero bastare. E questo, in sé, è già qualcosa che vale la pena seguire.