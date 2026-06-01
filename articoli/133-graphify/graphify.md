---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-06-01
author: "Dario Ferrero"
youtube_url: "https://youtu.be/hm37J3Xsnqo?si=6PyKivv8Cv21ItSm"
---

# Graphify e la memoria che gli LLM non hanno
![graphify.jpg](graphify.jpg)

*E se il tuo assistente AI potesse smettere di rileggere ogni volta tutto il progetto per rispondere a una sola domanda? Graphify, uno strumento open-source pubblicato su GitHub con oltre 50.000 stelle, promette esattamente questo: trasformare una cartella di codice, documenti, PDF, immagini e video in un grafo della conoscenza interrogabile dagli agenti AI, riducendo drasticamente il numero di token consumati ad ogni query.*

Chi lavora quotidianamente con agenti AI su progetti di medie dimensioni conosce bene una frustrazione specifica: ogni volta che un assistente come Claude Code, Cursor o Gemini CLI deve rispondere a una domanda sul progetto, percorre l'intera base di codice come se non avesse mai letto nulla. Rilegge file, rianalizza strutture, ricomincia da capo. È un po' come il detective Lunge di *Monster* di Naoki Urasawa, che per ricordare qualcosa deve ogni volta ricostruire l'intera catena deduttiva dal primo indizio, incapace di conservare uno stato intermedio tra le sessioni.

Ad aprile, su queste stesse pagine, abbiamo analizzato in dettaglio [la proposta di Andrej Karpathy per una knowledge base evolutiva per LLM](https://aitalk.it/it/llm-knowledge-base.html): costruire una wiki strutturata in Markdown che il modello potesse compilare e interrogare, evitando di ricaricare ogni volta l'intero corpus nel contesto. La proposta ha raccolto oltre 16 milioni di visualizzazioni su X, innescando un dibattito tecnico acceso su quale architettura di memoria fosse davvero praticabile per un uso professionale.

Graphify parte esattamente da quella intuizione, citando esplicitamente l'approccio di Karpathy nel README come punto di partenza, per poi spingerlo oltre: invece di una wiki piatta in Markdown, costruisce un grafo della conoscenza dove ogni entità, ogni funzione, ogni concetto estratto dai tuoi file diventa un nodo, e le relazioni tra entità diventano archi navigabili. La differenza non è estetica, è strutturale.

## Cos'è un grafo (e perché qui cambia tutto)

Un grafo, nella sua forma più semplice, è una raccolta di punti collegati da linee. I punti si chiamano nodi, le linee si chiamano archi. È la stessa struttura che usa Google Maps per rappresentare le strade di una città, o che i social network impiegano per modellare le relazioni tra utenti. Non è una metafora: è una struttura dati con proprietà matematiche che la rendono particolarmente adatta a rappresentare relazioni complesse.

Perché un grafo è più utile di un documento Markdown per un progetto software? La risposta sta nella natura delle relazioni. In un testo, anche ben strutturato, le connessioni tra concetti sono implicite: devi leggere, capire il contesto, inferire i legami. In un grafo, le relazioni sono esplicite, tipizzate e traversabili. Puoi chiedere "qual è il percorso più breve tra il modulo di autenticazione e il database?" e ottenere una risposta navigando gli archi, non analizzando testo.

Per un agente AI che deve rispondere su un progetto, questa differenza è sostanziale. Invece di caricare nel contesto decine di file sperando che il modello trovi le connessioni rilevanti, l'agente naviga il grafo, recupera solo i nodi pertinenti e i loro vicini diretti, e costruisce la risposta con una frazione dei token. È la differenza tra chiedere a qualcuno di leggere un'intera enciclopedia per rispondere a una domanda, o dargli un indice semantico con cui navigare direttamente alla voce giusta.

## Tre passate per capire tutto

La pipeline interna di Graphify, documentata in dettaglio nel file [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) del repository, si articola in tre fasi progettate per massimizzare l'elaborazione locale e minimizzare le chiamate API esterne.

La prima passata riguarda il codice sorgente ed è interamente locale: nessuna API, nessun token consumato. Tree-sitter, il parser AST usato anche da editor come Neovim e Helix per il syntax highlighting in tempo reale, analizza i file di codice ed estrae classi, funzioni, importazioni, grafi delle chiamate e commenti inline. Il risultato è deterministico: lo stesso file produce sempre lo stesso output. I file SQL ricevono un trattamento speciale, con tabelle, viste, chiavi esterne e relazioni JOIN estratte con la stessa logica deterministica. Al momento del rilascio, Graphify dichiara supporto per 29 linguaggi di programmazione.

La seconda passata copre i file audio e video, anch'essa locale. Faster-whisper, un'implementazione ottimizzata del modello Whisper di OpenAI che gira interamente in locale, trascrive i contenuti multimediali. C'è un dettaglio tecnico raffinato: la trascrizione viene "guidata" dai nodi più connessi del grafo costruito nella prima passata, i cosiddetti "god nodes", i concetti che compaiono più frequentemente nelle relazioni estratte dal codice. Questo fa sì che il modello di trascrizione presti maggiore attenzione ai termini di dominio specifici del progetto. I transcript vengono messi in cache: le esecuzioni successive saltano i file già processati.

La terza passata, quella che consuma token API, gestisce documenti, PDF e immagini. Qui entra in gioco il modello linguistico configurato dall'utente: Claude, Gemini, OpenAI, o in alternativa un'istanza locale di Ollama, oppure AWS Bedrock tramite la catena di credenziali IAM. I file vengono elaborati in parallelo da più sotto-agenti, ognuno dei quali restituisce un frammento JSON strutturato con nodi, archi e relazioni di gruppo. I frammenti vengono poi uniti in un singolo grafo coerente.

Il clustering delle comunità avviene con l'algoritmo di Leiden, un metodo pubblicato nel 2019 su *Nature Scientific Reports* che raggruppai nodi per densità delle connessioni senza richiedere embedding vettoriali separati. Le relazioni semantiche estratte dal modello linguistico, per esempio `semantically_similar_to` tra due concetti affini, sono già nel grafo come archi e influenzano direttamente la forma delle comunità rilevate. Non c'è un database vettoriale separato: la struttura del grafo è il segnale di similarità.

Ogni relazione viene marcata con uno di tre tag di confidenza: `EXTRACTED` per le relazioni trovate direttamente nel codice sorgente, `INFERRED` per le inferenze del modello con un punteggio da 0.55 a 0.95 secondo una scala discreta documentata, e `AMBIGUOUS` per i casi incerti segnalati nel report finale per revisione manuale. Sai sempre se il grafo ti sta dicendo qualcosa di certo o di ipotetico.
![graphify-query1.jpg](graphify-query1.jpg)
*Sreenshot del mio test sui dati (richiesta del paradosso di MTV) in opencode*

## Tutto il progetto in 7 megabyte

Ho installato Graphify tramite OpenCode e l'ho eseguito sull'intero progetto AiTalk: codice, articoli, immagini, file audio, l'intera base di lavoro accumulata nel tempo. Il materiale sorgente pesava circa 970 MB. L'output generato, la cartella `graphify-out/` con i suoi tre file principali, occupava poco più di 7 MB.

Tre file: `graph.html`, la visualizzazione interattiva navigabile in qualsiasi browser, `GRAPH_REPORT.md`, il report testuale con i concetti chiave, le connessioni più significative e le domande suggerite, e `graph.json`, il grafo completo in formato NetworkX node-link, interrogabile direttamente.

Da quel momento, qualsiasi domanda posta a OpenCode sulla struttura tecnica del progetto, sulla logica del codice, sui contenuti degli articoli e sulle connessioni tematiche tra loro ha ricevuto risposte eccellenti. Non generiche, ma contestualizzate: l'agente sapeva quali componenti dipendono da quali, quale argomento viene trattato in più articoli con angolature diverse, dove c'erano connessioni non esplicite tra contenuti apparentemente distanti. Il modello navigava il grafo invece di rileggere ogni volta i file sorgente. Dove prima una query complessa richiedeva di caricare nel contesto decine di file, ora l'agente parte dal report e naviga il JSON per trovare solo ciò che serve.
![grafo-aitalkjpg.jpg](grafo-aitalkjpg.jpg)
*Sreenshot della pagina html con la rappresentazione dinamica e navigabile del grafo del progetto AiTalk.it*


## Numeri onesti: 71x, ma dipende

Il repository pubblica nel file [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) un benchmark esplicito, e vale la pena leggerlo con attenzione perché i numeri vengono presentati con un'onestà insolita per un progetto in fase promozionale.

Su un corpus misto di 52 file composto dai repository di Karpathy, cinque paper accademici e quattro immagini, Graphify dichiara una riduzione di 71,5x nei token per ogni query rispetto alla lettura diretta dei file grezzi. Su un corpus più piccolo, quattro file tra codice sorgente e paper, la riduzione scende a 5,4x. Su sei file, circa 1x: nessun vantaggio rilevante in termini di token, semmai chiarezza strutturale.

Il pattern è chiaro e viene spiegato esplicitamente: la compressione scala con la dimensione del corpus. Sei file entrano già in una singola finestra di contesto. A 52 file i risparmi si compongono rapidamente. Ogni cartella `worked/` nel repository contiene i file di input originali e l'output effettivo, così chiunque può replicare il benchmark in autonomia.

Va però precisato cosa questi numeri non includono: il costo dell'estrazione iniziale, il momento in cui Graphify consuma token API per analizzare documenti, PDF e immagini. Questo costo si ammortizza sulle query successive grazie alla cache SHA256 che salta i file non modificati, ma è un costo reale che in un corpus grande può essere significativo, specialmente con modelli premium. Il benchmark misura il risparmio in regime stazionario, non il costo di setup. La documentazione lo dice chiaramente.

## Integrarsi o perdersi

Uno degli aspetti più curati del progetto è la compatibilità con l'ecosistema degli strumenti di sviluppo. Al momento Graphify supporta l'installazione diretta su Claude Code, OpenCode, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider e altri strumenti meno diffusi.

Il meccanismo di integrazione è semplice. Una volta costruito il grafo, il comando `graphify claude install` (o il corrispondente per la piattaforma scelta) scrive un file di configurazione che istruisce l'assistente a leggere `GRAPH_REPORT.md` prima di rispondere. Su piattaforme che supportano gli hook, come Claude Code, Codex e Gemini CLI, un hook si attiva automaticamente prima di ogni lettura di file: l'assistente naviga il grafo invece di scansionare la directory.

Per i team il workflow consigliato è committare la cartella `graphify-out/` nel repository Git. Ogni membro che fa pull trova il grafo già aggiornato. Il comando `graphify hook install` aggiunge un hook post-commit che ricostruisce automaticamente la parte AST dopo ogni commit, a costo zero in termini di API, con un driver di merge Git che gestisce i conflitti su `graph.json` unendo i due grafi invece di lasciare marcatori irrisolvibili.

Il pacchetto si chiama `graphifyy` su PyPI (doppia y), richiede Python 3.10+, e si installa con `uv tool install graphifyy`, `pipx install graphifyy` o `pip install graphifyy`. Il comando CLI rimane `graphify`.
![graphify-query2.jpg](graphify-query2.jpg)
*Sreenshot del mio test sul codice (richiesta del metodo di generazione del sito) in opencode*

## Privacy: cosa resta a casa

La gestione della privacy segue una logica esplicita. Il codice sorgente viene elaborato interamente in locale tramite tree-sitter, senza nessuna chiamata a servizi esterni. I file audio e video vengono trascritti localmente con faster-whisper. Nessun byte di codice o contenuto multimediale lascia la macchina dell'utente.

La situazione cambia per documenti, PDF e immagini: questi vengono inviati al modello linguistico configurato tramite la sua API. Se si usa Claude, i file vengono inviati ad Anthropic. Se si usa Ollama, rimangono in locale. Per contesti con dati sensibili, Graphify offre due opzioni: un'istanza Ollama locale o AWS Bedrock tramite IAM, senza chiavi API esplicite. Il progetto afferma di non avere telemetria, tracciamento degli utilizzi o analisi dei dati.

Un aspetto da considerare per i team su codice proprietario: anche se il codice rimane locale, i documenti di architettura, i PDF delle specifiche e le immagini dei mockup vengono elaborati dal modello esterno configurato. In presenza di obblighi di riservatezza contrattuale, questa distinzione va valutata con attenzione prima dell'adozione.

## Limiti senza sconti

Sarebbe disonesto chiudersi nel solo elogio. Ci sono aspetti che meritano una valutazione critica.

Il primo riguarda la qualità delle relazioni inferite. Le relazioni etichettate `INFERRED` dipendono dalla qualità del modello usato. Un modello più piccolo o configurato con un budget di token ridotto può produrre relazioni speculative con punteggi di confidenza ottimistici. La scala da 0.55 a 0.95 è calibrata sui corpus di test dello sviluppatore, non necessariamente sul tipo di progetto su cui si applica lo strumento.

Il secondo limite riguarda gli aggiornamenti. La cache SHA256 salta i file non modificati, ma cosa succede quando si sposta una funzione da un modulo a un altro o si refactorizza una classe in modo significativo? Il grafo può avere nodi orfani o relazioni che puntano a entità non più esistenti. Il comando `--update` gestisce i file modificati, ma su refactoring profondi probabilmente è necessaria una ricostruzione completa, con il costo di token associato.

Il terzo aspetto critico è la scala. Come per l'approccio wiki di Karpathy, anche il grafo ha un punto di rottura. Per corpus molto grandi, la documentazione suggerisce di usare query dirette sul `graph.json` o di esporre il grafo come server MCP con `python -m graphify.serve`, che offre strumenti strutturati come `query_graph`, `get_node`, `get_neighbors` e `shortest_path`. La soluzione è raffinata, ma aggiunge un livello di configurazione che non tutti i workflow possono assorbire facilmente.

Va segnalato infine che il progetto è mantenuto sostanzialmente da un singolo sviluppatore, Safi Shamsi. Il repository mostra un'attività intensa, con 97 release al momento della scrittura e l'ultima versione stabile v0.7.16 rilasciata il 12 maggio 2026, ma la sostenibilità di lungo periodo di un progetto con questa visibilità e questa dipendenza da un singolo maintainer è una variabile da non ignorare per chi pianifica un'adozione in ambienti critici.

## Il futuro della memoria

Graphify risolve un problema concreto. Ma la domanda più interessante che solleva non riguarda il risparmio di token: riguarda la natura della memoria negli agenti AI.

Oggi un agente non ha memoria persistente. Ogni sessione è una lavagna pulita, ogni progetto riscoperto da zero. Graphify e progetti simili sono tentativi di costruire uno strato esterno di memoria strutturata che sopravviva alle sessioni, che si accumuli nel tempo, che rappresenti non solo i dati grezzi ma le relazioni tra di essi.

Le domande aperte restano molte. Come si mantiene la coerenza di un grafo in un progetto che evolve rapidamente? Chi è responsabile della qualità delle relazioni inferite quando un agente prende decisioni basandosi su di esse? E la più sottile: se l'agente naviga un grafo invece di ragionare sui file, la qualità dell'estrazione iniziale diventa il vero collo di bottiglia, non controllabile con un parametro di temperatura ma con la qualità della pipeline di ingest.

Dal sito di Graphify Labs emerge una visione più ambiziosa: Penpax, il prodotto commerciale annunciato in versione trial prossimamente, promette di applicare la stessa logica a tutto il lavoro quotidiano di una persona, riunioni, email, file e codice, aggiornandosi in background, senza cloud, completamente on-device. Un "secondo cervello" digitale costruito su basi tecniche serie invece che su metafore motivazionali.

Graphify nella sua forma open-source è già un punto di partenza significativo. Non è la soluzione definitiva al problema della memoria degli LLM, ma è un indicatore preciso della direzione in cui si sta cercando: non dentro il modello, non nel contesto, ma in una rappresentazione strutturata e persistente che vive al di fuori di entrambi.

---

*Graphify è disponibile su [GitHub](https://github.com/safishamsi/graphify) con licenza MIT. Il pacchetto PyPI si chiama [graphifyy](https://pypi.org/project/graphifyy/) (doppia y). Il sito del progetto è [graphifylabs.ai](https://graphifylabs.ai). La documentazione tecnica sulla pipeline di estrazione è in [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md).*
