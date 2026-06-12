---
tags: ["Research", "Generative AI", "Training"]
date: 2026-06-12
author: "Dario Ferrero"
youtube_url: "https://youtu.be/QHNwVfUAp00?si=YKHjApbnbQLQ82Tr"
---

# ChartNet: l'analisi dei grafici non è più roba da grandi budget
![chartnet.jpg](chartnet.jpg)

*Per la prima volta, un modello AI open-source di piccole dimensioni interpreta grafici meglio dei giganti commerciali, grazie a ChartNet, il dataset rivoluzionario del MIT da 1,5 milioni di campioni sintetici che combina codice di plotting, immagini renderizzate, tabelle dati, summary in linguaggio naturale e coppie Q&A con ragionamento. Il risultato? Chiunque debba analizzare un report finanziario di 200 pagine può ora usare un modello da 3 miliardi di parametri gratuito su HuggingFace per estrarre dati, ricostruire grafici e ottenere risposte con ragionamento, democratizzando l'analisi visiva dei dati per PMI, ricercatori e professionisti con budget limitato.*

Immaginate di avere un analista finanziario che capisce perfettamente l'inglese, conosce tutti i fondamentali di bilancio, ma quando gli mostrate un grafico a barre con i ricavi trimestrali vi risponde descrivendo i colori delle barre invece di leggervi i numeri. È una situazione paradossale, eppure è esattamente ciò che accade a gran parte dei modelli di intelligenza artificiale visiva oggi sul mercato, inclusi alcuni dei più blasonati e costosi.

Il problema non è nuovo, ma è rimasto a lungo nell'ombra, oscurato dal clamore attorno alle capacità linguistiche dell'AI. I modelli cosiddetti vision-language, quelli che elaborano sia testo sia immagini, hanno fatto progressi spettacolari nel descrivere fotografie, riconoscere oggetti, trascrivere documenti. Ma quando si trovano davanti un grafico, il loro ragionamento si inceppa in modo sottile e pericoloso: vedono una figura, ma non capiscono il dato che quella figura rappresenta.

Interpretare un grafico non è semplicemente "guardare un'immagine". Richiede di fondere insieme tre competenze distinte: la percezione visiva delle forme geometriche (dove si trovano le barre, dove passa la linea di tendenza), la comprensione strutturale dei dati numerici (scala degli assi, proporzioni, valori assoluti), e la comprensione linguistica delle etichette, dei titoli, delle legende. È una triangolazione cognitiva che il cervello umano esegue in modo quasi automatico, ma che per un modello artificiale rimane una sfida aperta, un territorio dove anche i sistemi da miliardi di parametri inciampano su dettagli che sembrerebbero banali.

Dhiraj Joshi, senior scientist a IBM Research, ha descritto il problema con chiarezza nel [comunicato del MIT](https://news.mit.edu/2026/mit-researchers-teach-ai-models-to-interpret-charts-0603): l'industria finanziaria vive di grafici, e se i modelli vision-language riescono a estrarne informazioni affidabili, descrizioni di trend, variazioni nel tempo, comparazioni tra categorie, si aprono automaticamente a valle decine di flussi di lavoro che oggi richiedono analisti umani o strumenti costosi. Ma la parola chiave è "affidabili". Un modello che risponde con sicurezza e sbaglia i numeri è peggio di nessun modello.

Il collo di bottiglia, come spesso accade in questo campo, non era nei modelli. Era nei dati.

## Come nasce un dataset da 1,5 milioni di grafici

Chi segue il mondo dell'AI sa che la qualità dei dati di addestramento è quasi sempre più importante dell'architettura del modello. Un'idea semplice ma ben nutrita batte quasi sempre un'idea brillante affamata di esempi. Il problema con i grafici è che raccoglierli, etichettarli e renderli davvero utili per l'addestramento è straordinariamente difficile.

I dataset esistenti prima di ChartNet erano, guardando indietro, quasi ingenui nella loro parzialità. FigureQA, uno dei più noti, conteneva 100.000 immagini ma copriva solo tre tipi di grafico e usava una sola libreria di rendering, accettando esclusivamente risposte binarie sì/no. DVQA era costruito attorno a un solo tipo di grafico. ChartQA, più ambizioso, includeva immagini reali e domande complesse, ma si fermava a 14.000 esempi, neanche lontanamente abbastanza per addestrare un modello robusto. La lacuna comune era strutturale: nessuno di questi dataset collegava l'immagine del grafico al codice che lo aveva generato, ai dati sottostanti, a una descrizione in linguaggio naturale, e soprattutto a catene di ragionamento esplicito.

Jovana Kondic, dottoranda MIT in ingegneria elettrica e informatica e autrice principale del [paper](https://arxiv.org/pdf/2603.27064), ha inquadrato il problema con un'analogia che vale la pena riportare: un modello, a differenza del cervello umano, potrebbe aver bisogno di vedere migliaia di esempi durante l'addestramento per riconoscere in modo affidabile qualcosa come un grafico a linee. La scarsità di dati non è un inconveniente, è una barriera strutturale.

La soluzione concepita dal team MIT-IBM è elegante proprio perché ribalta la logica convenzionale. Invece di raccogliere grafici da internet e poi tentare di annotarli, i ricercatori hanno costruito una pipeline che genera grafici partendo dal codice. L'idea di fondo, la cosiddetta sintesi guidata da codice, funziona così: si prende un insieme iniziale di immagini di grafici già esistenti, si usa un modello visivo per ricostruire approssimativamente il codice che potrebbe averle generate, e poi si usa quel codice come seme per produrre centinaia di varianti. Cambiate il tipo di grafico, modificate i valori, alterate i colori, cambiate il tema, il titolo, la densità dei dati: ogni modifica del codice produce un nuovo campione autentico, con tutti i suoi metadati già disponibili per costruzione.

Il risultato è una pipeline capace di espandersi in modo quasi geometrico. Partendo da un numero relativamente piccolo di grafici seme, il sistema ha prodotto oltre 1,5 milioni di campioni diversificati, coprendo 24 tipologie di grafico (istogrammi, grafici a linee, a torta, a dispersione, box plot, mappe di calore, e molti altri) attraverso sei diverse librerie di plotting, tra cui Matplotlib, Seaborn, Plotly e Vega-Altair. Un sistema automatico di controllo della qualità verifica che ogni campione generato sia eseguibile, renderizzato correttamente e semanticamente coerente: non si vuole semplicemente diversità, ma diversità significativa.

## Cinque lingue per un grafico solo

La vera innovazione di ChartNet non è però nella quantità, è nella struttura. Ogni campione del dataset non è una semplice coppia immagine-etichetta: è una tupla di cinque elementi perfettamente allineati tra loro, una rappresentazione del medesimo grafico in cinque "lingue" diverse.

Il primo elemento è il codice di plotting eseguibile, la fonte di verità da cui tutto il resto deriva. Il secondo è l'immagine renderizzata del grafico, quella che il modello vedrà durante l'addestramento. Il terzo è la tabella dati con i valori numerici sottostanti, espressa in formato strutturato. Il quarto è un sommario in linguaggio naturale che descrive i pattern, le tendenze, le anomalie visibili nel grafico. Il quinto, disponibile per 632.000 dei campioni core (e in espansione), è una coppia domanda-risposta con una catena di ragionamento esplicita, il cosiddetto chain-of-thought, che mostra non solo la risposta corretta ma il percorso logico per arrivarci.

Questa struttura multimodale a cinque livelli non è esteticamente piacevole, è funzionalmente necessaria. Quando un modello viene addestrato su questi dati, impara non solo a "guardare" un grafico ma a mettere in relazione la sua struttura visiva con i numeri che rappresenta, con le parole che lo descrivono, con le domande che si possono porre su di esso. L'allineamento trasversale tra i cinque componenti è ciò che i ricercatori chiamano cross-modal alignment granulare: il modello sviluppa una comprensione integrata, non frammentata.

Oltre al nucleo sintetico, ChartNet include sottoinsiemi specializzati che affrontano dimensioni spesso ignorate dai dataset precedenti. Un sottoinsieme di 94.643 grafici sintetici è stato verificato da annotatori umani esperti, producendo anche un set di test di 2.000 campioni con garanzie di qualità certificate: è la rete di sicurezza statistica dell'intero sistema. Un secondo sottoinsieme raccoglie 30.000 grafici reali estratti da fonti autorevoli di media e visualizzazione dati, quello che serve per testare la generalizzazione dal mondo sintetico al mondo reale. Un terzo sottoinsieme include annotazioni di grounding, ossia coppie domanda-risposta associate a riquadri di delimitazione precisi sulle regioni visive del grafico: insegna al modello non solo cosa rispondere, ma dove guardare. Infine, un sottoinsieme dedicato alla sicurezza affronta il problema dei grafici potenzialmente fuorvianti o manipolati, una dimensione che i dataset accademici precedenti ignoravano quasi completamente.
![tabella1.jpg](tabella1.jpg)
[Immagine tratta dal paper ufficiale su arxiv.org](https://arxiv.org/pdf/2603.27064)

## Un 3B batte GPT-4o

I risultati sperimentali sono la parte che ha fatto alzare qualche sopracciglio nella comunità, e a ragione. Il team ha valutato i modelli addestrati su ChartNet su quattro task principali: ricostruzione del grafico (ricreare il codice di plotting a partire dall'immagine), estrazione dei dati (recuperare la tabella numerica sottostante), generazione di sommari, e risposta a domande con ragionamento a catena.

Il modello Granite 4.0 Vision da 3 miliardi di parametri, addestrato con ChartNet, ha raggiunto l'86,4% di accuratezza nella generazione di sommari (Chart2Summary) sul test set umano verificato di ChartNet, con valutazione condotta tramite LLM-as-a-judge. Questo punteggio è il più alto tra tutti i modelli valutati, inclusi modelli significativamente più grandi. Sullo stesso benchmark, Granite si è classificato secondo nell'estrazione dati (Chart2CSV) con il 62,1%, superato solo da Qwen3.5-9B con il 63,4%, un modello di dimensioni più che doppie.

Ma il dato che ha più colpito gli osservatori è nella comparazione diretta con i sistemi commerciali. I modelli open source addestrati su ChartNet hanno superato modelli di ordini di grandezza più grandi, incluso GPT-4o di OpenAI, su tutti i task di interpretazione grafica. Il concetto di "ordini di grandezza" qui non è enfasi retorica: GPT-4o è un modello che si stima abbia centinaia di miliardi di parametri, mentre Granite 4.0 Vision ne ha tre miliardi. Il rapporto è nell'ordine di 100:1 per parametri, con il modello più piccolo che vince. Questo è esattamente ciò che Kondic intendeva quando ha dichiarato che l'obiettivo del progetto è dimostrare che si può raggiungere lo stato dell'arte con modelli più piccoli che non richiedono quantità infinite di calcolo.

Il risultato non è magico, è conseguente: GPT-4o è un modello generalista addestrato su enormi quantità di dati eterogenei. Granite, addestrato su un dataset costruito chirurgicamente per il task specifico, può superarlo in quella nicchia precisa. È la differenza tra un chirurgo generalista e uno specialista: in sala operatoria per quella specifica procedura, lo specialista vince quasi sempre.

ChartNet ha migliorato le prestazioni anche sui benchmark pubblici standard del settore, come ChartQA, FigureQA e PlotQA, dimostrando che i guadagni non sono limitati al test set proprietario ma generalizzano a valutazioni indipendenti.

## Open source, ma con riserve

Fino a qui la storia sembra quasi troppo bella. Un dataset gratuito, costruito con rigore scientifico, che permette a modelli piccoli ed economici di battere i giganti commerciali nei compiti di analisi grafica. Per chi gestisce una PMI, conduce ricerca senza fondi da big tech, o semplicemente non vuole pagare le tariffe API dei fornitori premium, ChartNet e i modelli Granite che ne derivano rappresentano un accesso concreto a capacità che erano di fatto precluse.

Il [dataset è disponibile su HuggingFace](https://huggingface.co/datasets/ibm-granite/ChartNet), i modelli Granite sono rilasciati con licenza Apache 2.0, il paper è pubblicato su arXiv con licenza CC BY 4.0. Non ci sono barriere di accesso. Un professionista che volesse integrare oggi Granite Vision per analizzare automaticamente i report PDF della propria azienda, estrarne i grafici e ottenere sommari e risposte alle domande, può farlo su hardware di consumo con costi marginali vicini allo zero.

Detto questo, un resoconto onesto non può ignorare i limiti strutturali del progetto.

Il punto critico più evidente è la natura sintetica della maggior parte dei dati. I grafici generati da pipeline automatiche, per quanto diversificati e controllati, tendono a essere visivamente più puliti, più regolari, più "corretti" dei grafici che si incontrano nella realtà. Un report annuale di una multinazionale, una slide di una presentazione accademica, un'infografica di un giornale hanno spesso stili grafici idiosincratici, font non standard, scale anomale, annotazioni manuali, sovrapposizioni, qualità di rendering variabile. Il sottoinsieme di 30.000 grafici reali in ChartNet è un tentativo di colmare questo gap, ma rimane una frazione minore del dataset totale. Il rischio del cosiddetto "distribution shift", la differenza tra la distribuzione dei dati di addestramento e quella dei dati reali, è reale e riconosciuto dagli stessi autori, che hanno indicato l'espansione con dati di maggiore complessità come priorità per le versioni future.

C'è poi una questione di dipendenza dall'ecosistema. ChartNet è stato sviluppato nell'ambito del MIT-IBM Computing Research Lab, una collaborazione strutturata tra MIT e IBM Research, e i suoi risultati più visibili sono i modelli della famiglia Granite di IBM. Questo non è un difetto, ma è un contesto da tenere presente: il dataset è open source, ma la sua traiettoria di sviluppo è influenzata dagli obiettivi di una grande azienda tecnologica con interessi commerciali precisi nell'AI enterprise. La comunità di ricerca indipendente è esplicitamente invitata a contribuire, ma l'equilibrio tra governance comunitaria e direzione aziendale rimane da osservare nel tempo.

Va segnalato anche che le metriche di valutazione più lusinghiere, come l'86,4% su Chart2Summary, usano un approccio LLM-as-a-judge dove un modello linguistico valuta la qualità delle risposte di un altro modello. È una metodologia sempre più comune, ma non esente da critiche: i giudici automatici possono avere preferenze sistematiche, possono essere meno sensibili di esperti umani a certi tipi di errori numerici, e i punteggi assoluti dipendono in parte dalle scelte di prompt del valutatore. Il test set di 2.000 campioni verificati da umani è una garanzia parziale, ma non una validazione completa in condizioni reali.

Il paper sarà presentato all'IEEE CVPR 2026, il Computer Vision and Pattern Recognition, una delle conferenze accademiche più importanti al mondo nel campo della visione artificiale. È il sigillo di legittimità scientifica del progetto, e porta con sé anche la tradizione di revisione tra pari che distingue la ricerca accademica dal semplice annuncio commerciale.
![tabella2.jpg](tabella2.jpg)
[Immagine tratta dal paper ufficiale su arxiv.org](https://arxiv.org/pdf/2603.27064)

## Cosa cambia, concretamente

Per chi legge questo articolo da una prospettiva pratica, la domanda è: cosa cambia oggi, nella mia attività, grazie a ChartNet?

Se lavorate in una grande organizzazione con accesso ai modelli commerciali premium e un team AI dedicato, è principalmente una notizia interessante sul progresso della ricerca. Se invece siete un analista finanziario freelance che elabora decine di report PDF mensili, un ricercatore con budget limitato, o una PMI che vuole automatizzare l'estrazione di dati da presentazioni e dashboard, allora ChartNet apre una porta concreta.

Un modello da 3 miliardi di parametri come Granite 4.0 Vision gira su server cloud con costi orari di pochi centesimi. La differenza rispetto a GPT-4o via API non è solo economica: è anche di latenza, di controllo dei dati, di possibilità di fine-tuning su dati proprietari. Il sottoinsieme annotato da umani in ChartNet è progettato proprio per questo: permettere a chiunque di adattare le prestazioni al proprio dominio specifico, dai grafici di mercato azionario alle metriche di performance aziendale.

ChartNet dimostra che nell'AI il vantaggio competitivo non appartiene necessariamente a chi ha più parametri e più potenza di calcolo, ma a chi ha i dati giusti costruiti nel modo giusto. Su task specifici e ben definiti, un modello piccolo ma ben addestrato può rovesciare il tavolo. A volte ciò che conta non è più grande, ma più preciso.
