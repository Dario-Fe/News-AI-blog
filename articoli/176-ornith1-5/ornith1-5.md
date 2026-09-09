---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-09-09
author: "Dario Ferrero"
youtube_url: "https://youtu.be/RRRv88DRczA?si=I0nCamr3VJaNC9Hs"
spotify_url: "https://open.spotify.com/episode/3yIduQk70xMkqwSuriDbFD?si=IM7HcT_WRGGjLoCrslXhuA"
---

# Ornith-1.5 in locale: il self-improvement da 10 su 10
![ornith1-5.jpg](ornith1-5.jpg)

*C'è un momento, in ogni sessione di test di questa serie, in cui capisci se un modello mantiene le promesse o se il salto di versione è più marketing che sostanza. Con Ornith-1.5 quel momento è arrivato già al primo test, quando la spiegazione del meccanismo di Higgs è uscita più chiara e più veloce di quella che il pur ottimo Ornith-1.0 aveva prodotto mesi fa. Da lì la sessione ha preso un ritmo diverso dal solito.*

Anche qui il disclaimer resta identico a quello delle puntate precedenti: non è un benchmark scientifico, non ci sono metodologie validate né controlli incrociati, è il resoconto di quello che succede quando un modello open finisce sul mio PC di casa e viene messo alla prova con gli stessi identici compiti riservati agli altri concorrenti passati per questa serie, incluso [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html), il predecessore che aveva chiuso con un perfetto otto su otto. Per l'hardware e la configurazione di base di LM Studio rimando come sempre alla [prima puntata della serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html), qui riprendo solo i numeri che contano davvero.

## Perché tornare su Ornith

Ornith-1.0 era stato, fino a oggi, il modello più convincente passato sul mio banco di prova, quindi quando DeepReinforce ha annunciato la [famiglia 1.5](https://ornith.ai/ornith_1_5.html) descrivendola come il passaggio dal semplice self-scaffolding a un ciclo di self-improvement completo, la curiosità era inevitabile. Ho scelto di nuovo la taglia 35B-A3B, la stessa del test precedente, proprio per avere un confronto diretto senza il rumore introdotto da un cambio di dimensione, scaricando la quantizzazione Q6 che si attesta sui 30GB e che il mio hardware digerisce senza troppo affanno. Ho poi aggiunto due test inediti, pensati apposta per mettere alla prova ragionamento strategico e logica astratta, le due capacità che secondo la pagina di lancio dovrebbero beneficiare di più del nuovo ciclo di addestramento.

## Il banco di prova

Configurazione in LM Studio pressoché identica a quella già rodata per Ornith-1.0, con qualche adattamento specifico per questa versione: contesto a 25.000 token, offload GPU su 20 dei 41 layer disponibili, pool di 8 thread CPU su 8, 8 esperti attivi su 256 totali, batch di valutazione a 2048, physical batch a 512 e un massimo di 4 predizioni concorrenti. Ryzen 7700, 32 GB di RAM DDR5 e Radeon RX 9060 XT con 16 GB di VRAM restano gli stessi di sempre, la combinazione con cui questa serie ha già messo alla prova Qwen 3.5, Qwen 3.6, la famiglia Gemma 4 e recentemente Qwen 3.8 e Muse Glimmer. Anche in questo caso vale il promemoria d'obbligo: quello che segue è un test personale, non una campagna di benchmark, e va letto come tale.

## Cosa cambia davvero nel 1.5

La famiglia comprende quattro membri, un flagship da 397B a esperti misti, il 35B che ho testato, un 9B denso e una variante Mobile pensata per girare su iPhone e Android. La novità concettuale sta nel meccanismo di addestramento, che secondo la [documentazione ufficiale](https://ornith.ai/ornith_1_5.html) non si limita più a ottimizzare lo scaffold con cui il modello affronta un compito già dato, come accadeva in Ornith-1.0, ma chiude l'intero ciclo, il modello propone da sé nuovi compiti calibrati sulla propria frontiera di capacità, costruisce lo scaffold per affrontarli e genera i rollout con cui si allena, in un loop che DeepReinforce descrive quasi come un organismo che si affama apposta di problemi sempre più difficili per crescere. Sul piano pratico, per chi lo usa in locale, il cambiamento più tangibile è un altro, la visione ora è nativa e non richiede più il file mmproj separato che nella puntata precedente avevo dovuto scovare tra le conversioni della community.

Sui numeri dichiarati, il 35B-A3B segna un salto reale rispetto al predecessore, 67,8 contro 64,2 su Terminal-Bench 2.1 Terminus-2 e 79 contro 75,6 su SWE-bench Verified, superando nello stesso confronto sia Qwen3.6-35B, fermo rispettivamente a 52,5 e 73,4, sia modelli densi più grandi come Gemma 4-31B e Muse Glimmer-30B. Numeri che, come sempre quando arrivano dal produttore stesso, vanno presi come punto di partenza e non come verdetto finale.
![tabella2.jpg](tabella2.jpg)
[Immagine tratta da ornith.ai](https://ornith.ai/ornith_1_5.html)

## "Mi chiamo Claude": una stranezza che vale la pena raccontare

Al primo prompt dopo aver scaricato il modello, prima ancora di iniziare la batteria di test vera e propria, ho chiesto al modello semplicemente chi fosse. La risposta, arrivata con la solita sicurezza fluente a cui Ornith mi aveva abituato, è stata che si trattava di Claude un assistente creato da Anthropic. Non un errore di battitura, non un'allucinazione isolata su un dettaglio marginale, un'affermazione piena e coerente, riconfermata alla seconda mia richiesta un po stupita, su un'identità che non è la sua.

Tecnicamente la spiegazione più plausibile non è misteriosa, Ornith-1.5 nasce sopra Qwen3.5 e Gemma 4 con un ulteriore addestramento continuato, e una parte consistente dei dati usati in questa fase, come in gran parte dell'industria open oggi, è quasi certamente sintetica, generata cioè da altri modelli di frontiera durante sessioni di distillazione o di raccolta dati. Se tra queste fonti finiscono anche conversazioni o output riconducibili a Claude, il modello non assorbe soltanto stile e conoscenza, assorbe anche l'abitudine a rispondere "sono Claude" quando gli si chiede chi è, un po' come un attore che dopo mesi sul set continua per abitudine a rispondere al nome del personaggio anche fuori scena, in quella zona grigia tra recitazione e identità che il fumetto di Daniel Clowes racconta così bene in *Ice Haven*.

Il punto non è tanto l'episodio in sé, quanto quello che rivela di un ecosistema sempre più fitto di modelli che si addestrano gli uni sugli output degli altri, spesso senza dichiarare la provenienza esatta dei dati usati. È una forma di inseguimento allo specchio in cui diventa via via più difficile risalire a chi ha detto cosa per primo, e la domanda che mi porto dietro da questo episodio è semplice da formulare e tutt'altro che semplice da rispondere, dove finisce l'uso legittimo di dati di alta qualità comunque etichettati così e dove inizia una pratica che, senza essere necessariamente illegale, resta comunque opaca per chi la osserva da fuori. Non è un problema che risolvo io in un paragrafo, è però un segnale che mi sembra sbagliato liquidare come una semplice curiosità da aneddoto.

## Dieci sfide, non più otto

I primi otto test ricalcano esattamente quelli usati nelle puntate precedenti della serie, per garantire un confronto diretto. Ho aggiunto un nono e un decimo test pensati per mettere sotto pressione ragionamento strategico e logica astratta, le capacità che il ciclo di self-improvement dovrebbe allenare più di ogni altra.

### Test 1, ragionamento scientifico: il meccanismo di Higgs (5/5)

Spiegare la rottura della simmetria elettrodebole, il ruolo del campo di Higgs, il motivo per cui i bosoni W e Z acquisiscono massa mentre il fotone resta senza, è un compito che mette in difficoltà anche modelli blasonati. Ornith-1.5 ha risposto con una struttura in sei blocchi logici, dal contesto storico fino al conteggio dei gradi di libertà, un dettaglio che raramente vedo comparire spontaneamente e che qui arricchisce parecchio la spiegazione. Rispetto a Ornith-1.0 la prosa è più didattica, con la classica metafora del cappello messicano usata al momento giusto, e la velocità è salita in modo netto, da 16,3 a 23,15 token al secondo.

### Test 2, multimodalità: una tabella Excel sgranata (5/5)

Con la visione ormai nativa, niente più file da scaricare a parte, ho caricato la solita foto di bassa qualità di un foglio Excel aziendale. Il modello ha letto correttamente struttura e valori, individuato pattern stagionali e la relazione tra numero di ordini e valore medio, restituendo un riepilogo con tanto di emoji come indicatori di tendenza, un tocco che personalmente trovo utile più che decorativo quando si scorre velocemente un'analisi. Rispetto alla versione precedente la risposta è più analitica e meno descrittiva, 21,72 token al secondo.

### Test 3, generazione di codice: ciclo massimo in un grafo (5/5)

Implementare in Python un algoritmo per il ciclo di lunghezza massima in un grafo non orientato, problema NP-hard che si riduce al ciclo hamiltoniano. Ornith-1.5 ha riconosciuto subito la natura del problema, prodotto una soluzione DFS con backtracking pulita e commentata, e soprattutto ha proposto di sua iniziativa tre ottimizzazioni concrete, dalla potatura per connettività fino a una programmazione dinamica su bitmask per grafi piccoli, offrendosi di implementarla su richiesta. Un livello di proattività che Ornith-1.0 non aveva mostrato, 23,86 token al secondo.

### Test 4, pianificazione multilingua: cinque giorni in Giappone (5/5)

Itinerario di cinque giorni per un cliente francese, testo in francese e una sezione finale in italiano. Il francese prodotto è naturale, l'itinerario cita luoghi meno battuti come Omoide Yokocho e il boschetto di bambù di Arashiyama, con consigli pratici su trasporti e barriere linguistiche. La sezione italiana finale è altrettanto curata. Rispetto al predecessore la differenza sta nei dettagli culturali in più, 22,03 token al secondo.

### Test 5, contesto lungo: 460 pagine da consultare (5/5)

Caricato l'intero AI Index Report 2025, ho chiesto informazioni sulla crescita della generazione video e le pagine di riferimento. Ornith-1.5 ha indicato correttamente le pagine 126 e 127, citato le figure 2.3.11 e 2.3.12, elencato i modelli principali del settore da Movie Gen a Veo, e richiamato l'ormai celebre esempio dello spaghetti test con Will Smith. Precisione confermata al primo tentativo, con una sintesi più organizzata per sezioni rispetto a Ornith-1.0, 21,36 token al secondo.
![immagine1.jpg](immagine1.jpg)
*Screenshot durante i test su contesto lungo*

### Test 6, ragionamento spaziale: una stanza in disordine (5/5)

Foto di una stanza disordinata, richiesta di descrizione e strategia di riordino. Il modello ha categorizzato esplicitamente gli elementi in mobili fissi, elementi architettonici e oggetti sparsi, proponendo una sequenza di intervento sensata che parte dal letto e dal pavimento prima di occuparsi dei cavi. La categorizzazione esplicita è la novità rispetto alla versione precedente, 20,72 token al secondo.

### Test 7, agente multi-step: pianificare una web app (5/5)

Sviluppo di un'app di gestione spese per un team di due sviluppatori, stack, struttura e roadmap. Stack moderno basato su Next.js, PostgreSQL e Prisma, struttura a tre cartelle, roadmap in sei sprint con una suddivisione esplicita dei compiti tra i due sviluppatori e le criticità di ogni fase segnalate in anticipo. La suddivisione esplicita del lavoro, assente in Ornith-1.0, risponde meglio al vincolo posto nel prompt, 22,92 token al secondo.

### Test 8, conversazione lunga: quattro turni sulla stessa app (5/5)

Quattro turni su stack, notifiche, database e scalabilità di un'app di task management. Coerenza mantenuta su tutta la conversazione, architettura ibrida proposta per le notifiche con WebSocket per l'in-app ed email asincrone gestite via coda, schema database completo di indici, roadmap di scalabilità fino a diecimila utenti con checklist progressiva. Uso più marcato di tabelle e diagrammi ASCII rispetto al predecessore, circa 22 token al secondo di media.

### Test 9, il pianificatore strategico (nuovo, 5/5)

Vestire i panni del CEO di una startup con 10 milioni di dollari di finanziamento e un competitor aggressivo che sta erodendo quote di mercato, elaborando un piano triennale. Ornith-1.5 ha prodotto un piano su sei semestri, con una diagnosi iniziale delle possibili cause della perdita di quote, principi guida ben scelti come l'idea che il capitale sia tempo e non sicurezza, e metriche concrete su churn, NPS, CAC e LTV per ogni fase. La nota di apertura, che i dieci milioni non sono un successo ma il carburante per ottenerne uno, e la chiusura, che definisce il piano un'ipotesi di lavoro e non una profezia, aggiungono una consapevolezza che raramente trovo in risposte di questo tipo, 20,38 token al secondo.

### Test 10, l'analista di logica astratta (nuovo, 5/5)

Un piccolo sistema di tre affermazioni logicamente contraddittorie da analizzare e correggere. Il modello ha identificato la contraddizione usando la logica dei predicati, valutato tre possibili modifiche a un'unica affermazione e scelto quella più elegante, giustificando la scelta con criteri chiari come la minima alterazione logica necessaria e la preservazione delle altre due premesse. Un ragionamento che mi ha ricordato, per la cura nell'argomentare ogni passaggio, certi enigmi logici disseminati nei capitoli più cerebrali di *Baccano!*, dove ogni indizio va soppesato prima di scartare le ipotesi sbagliate, 22,72 token al secondo.

## Il quadro d'insieme
![tabella1.jpg](tabella1.jpg)

Dieci su dieci, con una velocità media intorno ai 22 token al secondo, contro i 16-17 registrati con Ornith-1.0, un miglioramento del 30-40 per cento che da solo giustificherebbe l'aggiornamento anche a parità di qualità delle risposte.
![tabella3.jpg](tabella3.jpg)
*La tabella comparativa con tutti i modelli testati nel 2026*
## Luci e ombre

Un punteggio pieno su dieci test, raccolto da un solo osservatore su un solo hardware, senza campioni ripetuti né controlli incrociati, resta un'indicazione forte e non una verità da prendere alla lettera, lo stesso limite che valeva per Ornith-1.0 e che vale ancora di più qui, dato che due dei dieci test sono nuovi e quindi privi di un termine di paragone su altri modelli di questa serie. I numeri dichiarati da DeepReinforce, disponibili nella [pagina di lancio](https://ornith.ai/ornith_1_5.html) insieme alla metodologia di valutazione usata per ogni singolo benchmark, vanno letti sapendo che l'azienda ha tutto l'interesse a mostrarsi nella luce migliore rispetto a Qwen3.6, così come chi analizza il modello dall'esterno, per esempio in [questa guida all'uso in locale](https://atomic.chat/blog/guides/how-to-run-ornith-1-5-35b-locally), ricorda che ogni laboratorio pubblica benchmark calcolati con il proprio setup, e che le differenze tra colonne non sempre reggono un confronto diretto.

Poi c'è la questione sollevata dall'episodio dell'auto-identificazione, che difficilmente troverà una risposta netta nel breve periodo, ma che pone comunque una domanda scomoda a chi costruisce modelli open partendo da dati la cui provenienza non è sempre tracciabile fino in fondo, quanto della qualità percepita di questi sistemi dipende in realtà da un travaso silenzioso di stile e conoscenza da modelli proprietari verso modelli aperti, e chi si assume la responsabilità quando quel travaso produce anche piccoli cortocircuiti di identità.

Chi ci guadagna, in questo scenario, sono ancora una volta gli sviluppatori indipendenti che possono contare su un coding agent competitivo senza pagare abbonamenti cloud, e chi lavora su hardware consumer di fascia medio-alta come il mio, che oggi può permettersi un modello capace di reggere il confronto con sistemi molto più grandi. Chi rischia di perdere terreno sono i fornitori di modelli proprietari specializzati in coding, che vedono ridursi progressivamente il vantaggio su fasce di mercato sempre più ampie, mentre resta aperta la domanda su quanto questi risultati tengano su compiti reali distribuiti nel tempo, più lunghi e meno puliti di quelli che un pomeriggio di test può mettere in scena.

Per ora, resta la sensazione di aver toccato con mano un salto di qualità reale, accompagnato da una domanda sulla provenienza dei dati che questa serie di articoli continuerà a portarsi dietro.