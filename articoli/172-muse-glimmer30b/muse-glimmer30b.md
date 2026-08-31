---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-31
author: "Dario Ferrero"
youtube_url: "https://youtu.be/HSTup5jYxJY?si=BMZFyfoApZV_X0Q4"
spotify_url: "https://open.spotify.com/episode/23U63PBf9iW7HQEee9qcZO?si=kNCdkRYZQkqlWBdShqHv-g"
---

# Muse Glimmer 30B in locale: il nuovo modello di Meta
![muse-glimmer30b.jpg](muse-glimmer30b.jpg)

*Il 10 agosto 2026 Meta Superintelligence Labs ha rilasciato [Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model), un modello da 30 miliardi di parametri pensato per girare in locale su hardware consumer, e la notizia merita un chiarimento immediato per chi segue Meta da tempo: non è un Llama. È il primo rilascio della nuova divisione di ricerca fondata dopo la ristrutturazione degli sforzi sull'intelligenza artificiale dell'azienda, un progetto che nasce con un'identità e una filosofia diverse rispetto alla vecchia famiglia.*

La particolarità più importante da capire, prima ancora di aprire LM Studio, riguarda la sua natura. Muse Glimmer non è stato addestrato da zero come [Qwen3.8, testato nel mio articolo precedente](https://aitalk.it/it/qwen38-27b.html). È una versione distillata di Muse Spark 1.2, il modello di punta di Meta: un "insegnante" molto più grande ha addestrato questo "allievo" a replicarne i comportamenti, secondo un processo che in gergo tecnico si chiama distillazione dei logit. Il risultato è un modello più piccolo e più efficiente, che eredita gran parte delle capacità del maestro senza portarsene dietro l'ingombro. È un po' come nei racconti di apprendistato alla Miyazaki, dove il discepolo non replica il maestro per imitazione superficiale, ma ne assorbe il metodo fino a renderlo proprio.

Ho scelto di testarlo nella stessa fascia dimensionale del test precedente, un denso da 30 miliardi contro il denso da 27 miliardi di Qwen, proprio perché Meta lo dichiara pensato per agenti locali, tool calling e orchestrazione di compiti complessi. La domanda che mi sono posto è semplice: un modello "di casa Meta", nato esplicitamente per fare l'agente, può competere sul mio hardware con i modelli cinesi che finora hanno dominato questa fascia?

Per il taglio ho optato per la quantizzazione Q4_K_XL, circa 19 GB su disco. Le fonti indicano che Muse Glimmer è pensato per hardware con 24-32 GB di VRAM, ma con offload parziale sono comunque riuscito a farlo girare sulla mia configurazione, sacrificando qualcosa in velocità. Ho impostato un contesto di 91.000 token, un compromesso tra la finestra nativa di 131k dichiarata dal produttore e i margini di memoria disponibili.

## Il laboratorio, invariato

Chi ha seguito la serie conosce già la configurazione: processore AMD Ryzen 7700, 32 GB di RAM DDR5, GPU AMD Radeon RX 9060 XT con 16 GB di VRAM, il tutto orchestrato tramite [LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html), come descritto nel dettaglio nella prima puntata di questa serie insieme al confronto con Ollama e alle ragioni della scelta. Non mi dilungo oltre su questo, chi vuole approfondire trova tutto in quell'articolo.

Per Muse Glimmer ho regolato alcuni parametri specifici. L'offload GPU è stato impostato a 35 layer su 52, oltre metà del modello quindi risiede in VRAM, con il pool thread CPU al massimo consentito, otto su otto. Il batch di valutazione è stato lasciato a 2048, il physical batch a 512, e la predizione concorrente massima a 4.

Una nota va fatta subito, perché ha condizionato l'intera sessione di test: Muse Glimmer tende a pensare a lungo prima di rispondere. In un caso ho osservato un tempo di ragionamento di dieci minuti, in un altro di tre, con il modello che spesso itera più volte sulla stessa soluzione anche quando la risposta corretta era già emersa nelle prime battute del ragionamento. È un comportamento che, come vedremo, pesa parecchio sull'usabilità quotidiana.

## Un cervello distillato, non nato

Prima di passare ai test vale la pena capire cosa c'è sotto il cofano. Muse Glimmer è un modello denso, non un Mixture of Experts come [Ornith 1.0](https://aitalk.it/it/ornith-1.0.html) o [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) che ho provato nelle puntate precedenti di questa serie. La differenza architetturale non è un dettaglio da addetti ai lavori: in un modello denso ogni token attiva l'intera rete, tutti i trenta miliardi di parametri, mentre in un MoE solo una frazione degli "esperti" interni viene interpellata volta per volta. La scommessa dei modelli densi è che questo costo computazionale più alto si traduca in una capacità di ragionamento superiore.

Sul fronte multimodale, Muse Glimmer integra nativamente un encoder visivo da 1,8 miliardi di parametri, capace di leggere immagini e video senza bisogno di moduli esterni. La licenza è Apache 2.0, la stessa scelta permissiva già vista in altri modelli di questa serie, un dettaglio tutt'altro che secondario per chi sviluppa prodotti commerciali e non vuole complicazioni legali.

Dal punto di vista architetturale, [le specifiche pubblicate](https://www.together.ai/models/muse-glimmer) descrivono un'attenzione raggruppata con un rapporto di 32 teste di query contro 2 teste di chiave-valore, una scelta che riduce drasticamente la memoria necessaria per la cache durante l'inferenza. A questo si affianca il supporto a DFlash, una tecnica di decodifica speculativa che predice blocchi interi di sedici token in un solo passaggio, verificandoli poi in parallelo invece di generarli uno alla volta. Sulla carta questo dovrebbe garantire un'accelerazione fino a 3 volte rispetto alla generazione token per token. Nella pratica, sul mio hardware, la velocità osservata è stata molto simile a quella di Qwen3.8, intorno ai 5 token al secondo: la teoria dell'accelerazione hardware di fascia alta non sempre si traduce linearmente su una configurazione di fascia media come la mia.

Vale la pena ricordare, come sempre in questa serie, che i test che seguono non hanno alcuna pretesa di rigore da laboratorio. Non sono benchmark, non uso suite standardizzate né campioni statisticamente significativi: sono otto prove pratiche, le stesse usate per Qwen3.8, Ornith e [Laguna XS-2.1](https://aitalk.it/it/qwen36-35b-ai.html), pensate per capire come si comporta il modello nell'uso quotidiano di chi scrive, non per stilare classifiche accademiche.

## Le otto prove

### Ragionamento scientifico: il meccanismo di Higgs

Ho chiesto al modello di spiegare la rottura della simmetria elettrodebole nel Modello Standard, con attenzione al campo di Higgs e ai bosoni W, Z e fotone, lo stesso prompt usato per gli altri modelli della serie. Velocità di generazione: 5,34 token al secondo. La risposta è arrivata tecnicamente ineccepibile, formule corrette, struttura logica solida, con il richiamo al "cappello messicano" del potenziale di Higgs e la derivazione corretta delle masse di W e Z.

Quello che manca, rispetto a Qwen3.8, è la cura didattica. La risposta è diretta e sintetica, priva di quella progressione narrativa che accompagna il lettore passo dopo passo, senza metafore estese o spiegazioni verbali che aiutino chi non ha già le basi. Per uno studente universitario, il target esplicito del prompt, il risultato è meno accessibile di quanto dovrebbe essere. Ho penalizzato leggermente il voto per questo: è un modello che sembra parlare a un collega esperto, non a chi sta ancora imparando.

**Voto: 4,8/5.**

### Multimodalità: la tabella Excel sgranata

Ho caricato un'immagine di bassa qualità di una tabella Excel, chiedendo una descrizione del contenuto, dei dati principali e delle tendenze. Velocità: 5,22 token al secondo. Il modello ha letto correttamente la struttura del foglio, i valori numerici e le relazioni tra colonne, estraendo pattern stagionali e differenze tra 2017 e 2018, arrivando persino a osservare una correlazione tra numero di ordini e valore medio.

La robustezza visiva è eccellente, e la risposta si adatta bene al compito descrittivo. Non raggiunge la profondità di insight che Qwen3.8 aveva mostrato proponendo azioni correttive concrete, ma resta comunque completa e ben organizzata.

**Voto: 5/5.**

### Generazione di codice: il ciclo massimo in un grafo

Il terzo test chiedeva di implementare in Python un algoritmo per trovare il ciclo di lunghezza massima in un grafo non orientato, spiegandone la complessità. Qui è arrivato il primo campanello d'allarme: dieci minuti di pensiero prima della risposta. Velocità di generazione una volta partita: 5,17 token al secondo.

La soluzione prodotta si basa su programmazione dinamica su sottoinsiemi, l'approccio di Held-Karp, riconoscendo correttamente la natura NP-hard del problema. Il codice è pulito, commentato, funzionante, e la complessità dichiarata, O(n² 2ⁿ), è esatta. Dalle tracce di ragionamento visibili emerge un dettaglio curioso: il modello aveva individuato la soluzione corretta quasi subito, ma ha continuato a iterare sulla stessa logica per minuti, come un musicista jazz che rifinisce lo stesso assolo prima di suonarlo davvero. La qualità finale è ottima, ma dieci minuti di attesa per un compito interattivo sono tanti.

**Voto: 4,9/5**, penalizzato per il tempo di elaborazione eccessivo.

### Pianificazione multilingua: cinque giorni in Giappone

Ho chiesto un itinerario di cinque giorni in Giappone per un cliente francese, con il testo principale in francese e una sezione dedicata in italiano. Velocità: 5,34 token al secondo. Il modello ha rispettato perfettamente la lingua richiesta, producendo un itinerario dettagliato con consigli pratici su trasporti, barriere linguistiche e cibo di strada, mentre la sezione italiana era altrettanto curata.

A differenza di Laguna XS-2.1, che nella puntata precedente aveva mostrato qualche incertezza linguistica, qui non ci sono stati problemi. La risposta è completa e ricca di dettagli culturali, seppure più sintetica di quella che Qwen3.8 aveva prodotto sullo stesso prompt.

**Voto: 5/5.**

### Contesto lungo: cercare l'ago nel PDF da 460 pagine

Ho caricato l'AI Index Report 2025 per intero, chiedendo informazioni sulla crescita della generazione video e le pagine esatte in cui trovarle. Tempo di ragionamento: circa tre minuti. Velocità: 5,18 token al secondo. Il modello ha indicato correttamente le pagine 126 e 127, citando le figure specifiche 2.3.11 e 2.3.12, e la sintesi includeva dettagli puntuali sui modelli citati nel report e l'ormai celebre esempio del video di Will Smith che mangia gli spaghetti.

La precisione nel recupero delle informazioni è eccellente, ma tre minuti restano un tempo significativo per un compito che, in teoria, richiede solo di andare a cercare un'informazione già presente nel testo, non di ragionarci sopra a lungo.

**Voto: 4,9/5**, ancora una volta penalizzato per il tempo di attesa.

### Ragionamento spaziale: la stanza nel caos

Ho caricato l'immagine di una stanza disordinata, chiedendo una descrizione e una strategia di riordino. Tempo di risposta: 50 secondi, questa volta ragionevole. Velocità: 5,33 token al secondo. Il modello ha descritto la stanza per aree funzionali, con una strategia di riordino logica e motivata su base pratica, individuando ad esempio nel cesto blu l'ingombro principale da spostare per primo.

La comprensione visuo-spaziale è solida e il tempo di risposta, finalmente, compatibile con un uso quotidiano.

**Voto: 5/5.**
![immagine1.jpg](immagine1.jpg)
*Screenshot durante i test di ragionamento spaziale*

### Agente multi-step: pianificare una web app

Ho chiesto di pianificare lo sviluppo di una web app per la gestione delle spese, con stack tecnologico, struttura del progetto e roadmap per un team di due sviluppatori. Velocità: 5,31 token al secondo. La risposta è arrivata completa, con uno stack moderno basato su Next.js, NestJS, PostgreSQL e Prisma, una struttura a monorepo, una roadmap suddivisa in nove sprint e le criticità principali già identificate in anticipo.

Il tocco che ho apprezzato di più è il consiglio finale, pragmatico e concreto: concentrare i primi quattro sprint sul nucleo minimo funzionante prima di aggiungere qualsiasi rifinitura. È il genere di suggerimento che ci si aspetterebbe da un project manager navigato, non da un modello linguistico.

**Voto: 5/5.**

### Conversazione lunga: quattro turni su un'app di task management

L'ultimo test è stato condotto su quattro turni consecutivi, discutendo stack tecnologico, sistema di notifiche, schema del database e strategie di scalabilità per un'app di gestione attività. Velocità media: 5,1 token al secondo, con un calo progressivo da 5,33 a 4,98 turno dopo turno.

Il modello ha mantenuto coerenza lungo tutta la conversazione, ricordando ogni scelta tecnologica precedente e motivandola quando richiesto. Ha proposto un'architettura ibrida per le notifiche, WebSocket per quelle in-app ed email asincrone gestite con BullMQ, uno schema database completo e una roadmap di scalabilità pensata per diecimila utenti. Il leggero rallentamento nei turni successivi è fisiologico, la qualità è rimasta costante.

**Voto: 5/5.**

## Tabella riassuntiva dei test
![tabella1.jpg](tabella1.jpg)
Media voti: 4,95/5. Velocità media: circa 5,2 token al secondo.

## Il prezzo del pensare troppo

Muse Glimmer 30B è, prima di tutto, la dimostrazione di cosa significhi essere un modello denso e distillato allo stesso tempo. Attiva tutti i trenta miliardi di parametri per ogni singolo token generato, e questo si paga in velocità: circa 5 token al secondo sulla mia configurazione, un ritmo che richiede pazienza. In cambio, la distillazione da Muse Spark 1.2 gli permette di ereditare comportamenti e capacità di un modello ben più grande, un'eredità che si percepisce nella qualità delle risposte più che nella loro rapidità.

La qualità, appunto, è alta: 4,95 su 5 di media sugli otto test, esattamente lo stesso risultato ottenuto da Qwen3.8-27B nella puntata precedente. Sul piano dei contenuti, insomma, i due modelli si equivalgono. Quello che li distingue davvero è il comportamento durante l'attesa e lo stile della risposta finale.

Il tratto più distintivo di Muse Glimmer è la sua tendenza al "long thinking", il pensare a lungo prima di rispondere. Dieci minuti nel test sul codice, tre minuti nel test sul PDF lungo, con il modello che spesso continua a rimuginare sulla stessa soluzione anche dopo averla già trovata, un po' come certi personaggi delle graphic novel di Craig Thompson che rielaborano lo stesso ricordo più e più volte prima di lasciarlo andare. È un comportamento che può essere un pregio, per problemi che richiedono davvero un ragionamento approfondito, o un difetto, per chi cerca un'interazione rapida e fluida nella conversazione quotidiana.

Lo stile delle risposte, poi, racconta una personalità precisa: diretto, sintetico, tecnicamente rigoroso, ma meno incline alla didattica rispetto a Qwen3.8. È un modello che sembra pensato per parlare a chi già sa, più che per accompagnare chi sta imparando. La multimodalità nativa lo rende comunque più versatile di modelli come Laguna XS-2.1, che non gestisce immagini, e la licenza Apache 2.0 resta un vantaggio concreto per chi vuole integrarlo in un prodotto commerciale senza vincoli.

Chi vince e chi perde in questo scenario? Vince chi ha pazienza e cerca rigore tecnico su compiti complessi, sviluppatori che costruiscono agenti locali, chi lavora su problemi dove un tempo di attesa più lungo è accettabile in cambio di precisione. Perde chi cerca un assistente reattivo per l'uso quotidiano, dove un MoE come Ornith-1.0-35B, testato in una puntata precedente di questa serie, offre probabilmente un compromesso più equilibrato tra velocità e qualità.

Resta una domanda aperta, che vale la pena lasciare sul tavolo: il "long thinking" osservato qui è una caratteristica intrinseca dell'architettura distillata, o un effetto collaterale del processo di addestramento che Meta potrebbe correggere nelle prossime versioni? Non ho una risposta definitiva, e sospetto che nemmeno Meta ce l'abbia ancora del tutto chiara. Per ora, Muse Glimmer resta un modello che pensa tanto e parla poco, il che, a seconda di cosa serve, può essere la sua forza più grande o il suo limite più evidente.
![tabella2.jpg](tabella2.jpg)