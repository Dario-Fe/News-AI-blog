---
tags: ["Generative AI", "Applications", "Research"]
date: 2026-10-26
author: "Dario Ferrero"
youtube_url: "https://youtu.be/e3spyPcHURU?si=eT_U9sqwmEoM68oY"
spotify_url: "https://open.spotify.com/episode/44hRhfQtwgtawmiK8DB49G?si=Jf-4tHjMRDWoPlnJ2ZDz6g"
---

# CLM-8B, il decisore aperto che sfida Jev
![clm-8b.jpg](clm-8b.jpg)

*Nel [pezzo su Jev](https://aitalk.it/it/jev) avevo raccontato un modello che rinuncia alla parola per fare una sola cosa: decidere. Gli si consegna una situazione e un insieme di scelte possibili, e restituisce una scelta con la probabilità associata, senza scrivere una riga di testo. TypeSafe, che lo ha lanciato il 15 settembre, ha chiamato la categoria System One, in omaggio al pensiero rapido di Kahneman. Otto giorni dopo è arrivata una proposta dal fronte opposto: [CLM-8B](https://github.com/Contrastive-LM/CLM), rilasciato da ricercatori di Stanford e NVIDIA con licenza Apache 2.0, quindi scaricabile e installabile sui propri server.*

Sarebbe comodo liquidarlo come il Jev libero, ed è una scorciatoia sbagliata. L'idea della risposta a Jev è una lettura giornalistica, non una dichiarazione degli autori. CLM affronta lo stesso problema, decidere in fretta senza scrivere parola dopo parola, ma con un'architettura diversa e una vocazione diversa. Dalle prove disponibili emerge uno specialista, non un sostituto.

## Due encoder, una cache

Per capire la differenza serve un'immagine. Nel 1975 Brian Eno e Peter Schmidt pubblicarono le Oblique Strategies, un mazzo di carte con aforismi da pescare quando un lavoro si blocca. Il mazzo è sempre lo stesso, cambia la situazione in cui lo si consulta. CLM funziona in modo simile: le azioni possibili sono un mazzo fisso, e ogni nuova situazione viene confrontata con le carte per scoprire quale combacia meglio.

Tecnicamente il modello usa due lettori distinti, uno per la situazione e uno per le azioni, che traducono entrambe in coordinate di uno spazio condiviso; vince l'azione più vicina alla situazione. È lo schema dei motori di ricerca semantici, addestrato con un metodo chiamato InfoNCE che premia gli abbinamenti giusti e penalizza gli altri. Il vantaggio pratico è che le coordinate delle azioni si calcolano una volta sola e si tengono in memoria, la cache, mentre per ogni richiesta si legge soltanto la situazione.

Jacky Kwok, responsabile del progetto, ha spiegato a [VentureBeat](https://venturebeat.com/technology/stanford-and-nvidias-open-clm-8b-caches-reusable-agent-actions-and-runs-up-to-9x-faster-than-jev-in-tests) che Jev e un modello affine, Laya, mettono in cache soltanto la situazione, e che la separazione di CLM rende il vantaggio più forte quando contesti e azioni sono lunghi o riutilizzati. È la descrizione dell'autore del progetto, non verificata da terzi: l'architettura interna di Jev non è pubblica, TypeSafe non ha diffuso né pesi né dimensioni, e le ricostruzioni esterne, come quella dell'analista [Archer Hume](https://archerhume.com/posts/jevs-architecture-unmasked/), restano dichiaratamente congetture.

La cache non è magia, e lo ammette il [README](https://github.com/Contrastive-LM/CLM) stesso. Nelle misure degli autori su una GPU RTX 4090, una situazione sempre nuova costa circa 28 millisecondi con o senza cache, perché va comunque letta; quando le situazioni si ripetono si scende da circa 1,7 a 0,6 millisecondi. Il guadagno dipende da quanto l'agente rivisita gli stessi scenari (dichiarazione di parte, non replicata da terzi).

## Pesi aperti, davvero?

Qui sta il primo vantaggio concreto rispetto a Jev, che resta un servizio chiuso consultabile via API. [Pesi e codice sono sotto Apache 2.0](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B), senza contratti da firmare e con la possibilità di far girare tutto in casa. Per chi si occupa di intelligenza artificiale locale e di sovranità dei dati è il punto decisivo. Ma "aperto" contiene tre livelli diversi.

Il primo sono i pesi, e qui CLM è in regola, con un'avvertenza. La parte addestrata dagli autori è un file da 75 megabyte: il grosso lo fa Qwen3-8B di Alibaba, un modello preesistente tenuto congelato, a cui CLM aggiunge due piccole teste, una per le situazioni e una per le azioni. Secondo la [scheda di baobab-tech](https://github.com/baobab-tech/decision-models-experiments/blob/main/docs/models/clm-8b.md) servono un server vLLM per il codificatore, circa 16 GB di memoria e, come obiettivo dichiarato dagli autori, una GPU NVIDIA. Su Mac funziona una ricetta di terzi, Ollama non è supportato. Il locale è plausibile, non banale.

Il secondo livello è la valutazione. Il repository include gli script per rifare i test sul codice e il gioco T-Rex, quindi una verifica parziale è possibile, anche se la stessa scheda nota che un dataset citato nel README non compare nell'elenco dell'organizzazione. Il terzo è l'ecosistema, ancora acerbo: la guida all'addestramento aggiuntivo è, sempre secondo baobab, un testo pensato per un agente autonomo più che per una persona; dati e pipeline stanno in un altro repository; le licenze dei dati di addestramento non sono elencate, compresi i 30 milioni di risposte sbagliate ma plausibili generate con Gemini 2.5 Flash-Lite, i cui termini d'uso la scheda segnala come non verificati.
![immagine1.jpg](immagine1.jpg)
[Immagine tratta dal repository ufficiale su GitHuB](https://github.com/Contrastive-LM/CLM)

## Cosa dichiarano gli autori

Tutte le cifre di questa sezione sono dichiarazioni di parte, ottenute da chi ha costruito il modello. Nei test senza addestramento specifico sul compito, il README sostiene che CLM sia alla pari con Jev su uso del computer, giochi e chiamata di strumenti, con latenza fino a 9 volte inferiore. Il caso migliore è il gioco del dinosauro di Chrome: 16,5 millisecondi contro 149,8, con entrambi i modelli a 5 prove su 5, così come a Super Mario. Sul benchmark BFCL v4, dedicato alla chiamata di strumenti, CLM ottiene il 95,2% contro il 99,2% di Jev, con tempi di 76,8 contro 125,5 millisecondi. Su WikiRacing, che consiste nel raggiungere una pagina di Wikipedia seguendo link, CLM completa 26 prove su 30, Jev tutte e 30, con 79,8 millisecondi contro 225.

Due precisazioni di onestà. La parità, dunque, non è uniforme: dove cambia l'accuratezza Jev resta avanti, e il vantaggio di velocità varia da circa 1,6 a 9 volte a seconda del compito. Inoltre CLM è misurato su una GPU locale mentre Jev è un servizio ospitato altrove; dalle fonti consultate non è chiaro se la latenza di Jev includa il viaggio in rete, un dettaglio che sposta molto il confronto.

La parte più spettacolare riguarda il codice. Dopo un addestramento aggiuntivo leggero, gli autori dichiarano l'81,6% su DeepSWE e l'87,6% su Terminal-Bench 2.1, contro il 71,1% e l'83,1% di Jev. Ma quei risultati vengono da teste addestrate apposta, non dal modello pubblicato, su soli 38 e 30 compiti tenuti da parte. E CLM non risolve i problemi: sceglie tra soluzioni prodotte da modelli più grandi, Opus 5 per il primo test e Fable 5 per il secondo. Resta un risultato interessante, perché è l'unico terreno in cui, secondo gli autori, CLM supera Jev. Nessuno lo ha ancora riprodotto in modo indipendente.

## Prove sul campo

Qui entrano i terzi, tre famiglie di verifiche con metodi e limiti molto diversi.

La prima è [local-jev-bench](https://github.com/tak-bro/local-jev-bench), un test su un Mac M3 Max con 36 GB riassunto nella scheda di baobab-tech. CLM ottiene il 39% su 105 decisioni in inglese, il 41% in coreano e il 20% su BANKING77, un classico elenco di 20 categorie di richieste bancarie, dove il caso darebbe circa il 5%. Altri due modelli aperti nello stesso test arrivano a 89%, 87% e 89% (Kev-4B) e a 81%, 84% e 80% (AnyJev L0). Attenzione: non è un confronto con Jev, ma con altri modelli aperti. Gli stessi tester non riescono inoltre a riprodurre l'esempio ufficiale del README per la domanda sull'urgenza (0,852 contro 0,41). Il limite: hardware non previsto dagli autori e procedura di terzi.

La seconda è un [test di michabbb](https://gist.github.com/michabbb/da531cc4720d8ec62395fc02dfdd476c) su 140 coppie reali di collegamento tra elementi di una base di conoscenza, con la domanda secca se due elementi siano collegati. Su 40 coppie con risposta di riferimento, la capacità di distinguere (AUC, 1 è perfetto e 0,5 è il caso) è 0,77 per CLM con testi troncati a 2.048 token, 0,64 con il testo intero e 0,998 per Jev. CLM concorda con Jev sulle fasce di decisione in circa il 44% dei casi e non scende mai sotto lo 0,22 di probabilità. Anche il tempo è peggiore, 0,52 secondi contro 0,28, ma qui il confronto è sbilanciato: CLM su un DGX Spark con le teste su processore, Jev tramite API. Soprattutto l'autore elenca da sé i limiti: compito molto diverso da quelli del modello, 129 input su 140 oltre la finestra, risposte di riferimento assegnate da un modello linguistico e non da persone, nessun addestramento aggiuntivo, versione 0.1.

La terza sono gli aggregatori. [BenchLM](https://benchlm.ai/compare/clm-8b-vs-jev-1-13-0) riporta su JevBench 8,57 contro 63,29 nella versione 1.4 e 1,51 contro 72,13 nella 1.5, ma si rifiuta di stilare una classifica per mancanza di dati comparabili. [Benchmark Heaven](https://benchmarkheaven.com/jev-models/clm-8b) colloca CLM all'87° posto su 92 tra i modelli aperti, ma è un progetto personale in versione beta. JevBench, inoltre, è un banco di prova nato attorno a modelli di tipo Jev. Sono segnali da verificare, non verdetti.
![immagine2.jpg](immagine2.jpg)
[Immagine tratta dal repository ufficiale su GitHuB](https://github.com/Contrastive-LM/CLM)

## Perché i numeri divergono

Sarebbe sbagliato concludere che qualcuno menta. In *Rashomon* di Kurosawa lo stesso episodio produce quattro racconti inconciliabili, e nessuno dei testimoni è in malafede: guardano da posizioni diverse. Qui accade lo stesso con i benchmark.

I test ufficiali privilegiano la scelta tra poche azioni ripetute, la chiamata di strumenti, i giochi e la selezione tra risposte candidate. I test indipendenti usano classificazioni con molte categorie, ticket reali e giudizi su testi lunghi e strutturati. Cambiano la lunghezza dell'input, che CLM tronca in silenzio oltre i 2.048 token di default, il numero di candidate e la frequenza con cui le stesse azioni ritornano, da cui dipende tutta la cache. Cambia anche il regime: modello pubblicato contro teste addestrate apposta.

Lo ha detto con franchezza lo stesso Kwok: non lo userebbe al posto di un modello di ragionamento generale per problemi di matematica, testi lunghi o pianificazione. VentureBeat ricorda inoltre un limite strutturale: le probabilità di CLM sono relative all'insieme di candidati ricevuto, e se sono tutti sbagliati il modello ne sceglie comunque uno. La formula che ne ricavo è questa: CLM può essere eccellente nel dominio per cui è nato e debole fuori. Quanto grande sia quel dominio, oggi, nessuno lo sa con precisione.

## Pro e contro in produzione
![tabella1.jpg](tabella1.jpg)

Per equilibrio, va ricordato che anche Jev si regge in buona parte su cifre dichiarate da TypeSafe: l'azienda stessa definisce interne le sue misure su velocità e costo, e a quanto risulta non ha pubblicato curve di calibrazione, come riportavo nell'[articolo precedente](https://aitalk.it/it/jev). Sul costo non esiste un confronto omogeneo, come ammette VentureBeat.

Jev è oggi la scelta più prevedibile per accuratezza; CLM è la più interessante per controllo, costo marginale e latenza, ma richiede una validazione sul proprio carico di lavoro. Chi ci guadagna? Chi ha dati sensibili e azioni ripetute. Chi rischia? Chi lo adotta fidandosi del titolo.

## Cosa manca per un verdetto

Dichiaro i limiti, perché rendono il quadro più credibile. Non ho potuto eseguire un test locale su hardware AMD, che l'infrastruttura ufficiale non indica come obiettivo. I test indipendenti sono pochi e su compiti eterogenei. Mancano confronti riproducibili sullo stesso compito, con gli stessi prompt e la stessa versione di Jev, che nel frattempo è arrivato alla 1.13.0. Il comportamento dopo l'addestramento aggiuntivo potrebbe cambiare molto ma non è documentato da terzi. Servono misure su latenza nei casi peggiori, costi reali, memoria e calo di qualità fuori dal terreno di progetto. Infine il fratello maggiore, CLM-35B multimodale, era annunciato dagli autori per inizio ottobre: all'11 ottobre non risulta su Hugging Face.

## Alternativa selettiva, non sostituto

CLM-8B è importante perché porta nel pubblico un'alternativa aperta ai modelli System One chiusi, e perché lo fa con un'idea architetturale diversa e verificabile. Latenza e licenza sono vantaggi reali, soprattutto per agenti ad alta frequenza e per installazioni controllate. Jev, nei test indipendenti oggi disponibili, resta più affidabile su classificazione, giudizi sì o no e testi complessi.

La domanda giusta, quindi, non è CLM o Jev, ma se il proprio carico di lavoro abbia azioni ripetibili, candidati brevi e bisogno di ospitare il modello in casa. Se la risposta è sì, CLM merita un pilota misurato sui propri dati. Se la priorità è l'accuratezza generale senza addestramento specifico, Jev resta la scelta più prudente. Come con ogni mazzo di carte, conta meno la carta in sé che la situazione in cui la si pesca: meglio misurare prima di scegliere.