---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-06-17
author: "Dario Ferrero"
youtube_url: "https://youtu.be/x9ta8L9YYXw?si=9I8KZ8gLTsopV-sy"
---

# Gemma 4 12B in locale: meglio piccolo al massimo o grande strozzato?
![gemma4-12b-q8.jpg](gemma4-12b-q8.jpg)

*Nei test precedenti su Gemma 4 26B e Qwen3.6 35B, avevo sempre dovuto fare i conti con lo stesso problema: la VRAM non bastava mai. Modelli grandi, quantizzazioni spinte, layer in offload. Funzionavano, ma con la sensazione di star guidando una macchina potente col freno a mano tirato. Poi è arrivato Gemma 4 12B. Più piccolo, certo. Ma con un'architettura nuova e la promessa di girare interamente su GPU consumer senza compromessi. Così ho deciso di fare un esperimento diverso: non più "chi è il modello più potente?", ma "un modello più piccolo usato al massimo delle sue potenzialità può battere uno più grande ma strozzato?". Ho preso gli stessi identici test, le stesse domande, e li ho confrontati.*

Chi segue questa serie conosce già l'hardware e il metodo. Per tutti i dettagli su installazione, scelta del framework e filosofia del laboratorio rimando al [primo articolo della serie su Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), che resta il riferimento metodologico di tutti questi esperimenti. Qui mi limito all'essenziale.

La macchina è sempre la stessa: un PC assemblato con criterio ma senza esagerare, con processore AMD Ryzen 7700, 32 GB di RAM DDR5, e una GPU AMD Radeon RX 9060 XT con 16 GB di VRAM. Hardware da utente evoluto, non da laboratorio di ricerca. Il software è [LM Studio](https://lmstudio.ai/), l'applicazione desktop che permette di scaricare e avviare modelli senza aprire un terminale, con la preziosa caratteristica di mostrare in anticipo una stima delle performance attese sulla propria configurazione.

Il metodo, lo ribadisco come ho fatto nelle puntate precedenti, non è scientifico nel senso accademico del termine. Non c'è un protocollo peer-reviewed, non c'è un campione statisticamente significativo di prompt. I test sono prove sul campo, condotte con gli strumenti di un utente esigente, e i voti sono valutazioni personali, non sentenze. La batteria di prove è rimasta identica a quella usata per [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) e [Qwen3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html): ragionamento scientifico, multimodalità su tabelle, generazione di codice complesso, pianificazione multilingua, contesto lungo su un PDF di 460 pagine, ragionamento spaziale su una stanza disordinata, e i test extra su agente multi-step e conversazione lunga.

## Non è un fratello minore

Prima di entrare nei test, vale la pena fermarsi un attimo su un punto che rischia di passare inosservato: Gemma 4 12B non è semplicemente una versione ridotta del [26B MoE che avevo già testato](https://aitalk.it/it/gemma4-26b.html). Non è un taglio più economico dello stesso progetto. È qualcosa di strutturalmente diverso, e la differenza non è di grado ma di tipo.

Il 26B MoE, come tutti i modelli multimodali tradizionali, usa encoder separati per gestire immagini e testo: una parte del modello riceve le immagini, le comprime, le trasforma in una rappresentazione numerica, e solo dopo passa il risultato al modello linguistico vero e proprio. È un processo a due fasi, con un "traduttore" nel mezzo che inevitabilmente perde qualcosa per strada, come ogni traduzione.

Il 12B elimina questo passaggio del tutto. È il primo modello "unificato" della famiglia Gemma, e quella parola nel nome non è marketing: è architettura. Una patch di immagine subisce solo una moltiplicazione di matrice e l'aggiunta di coordinate spaziali, e finisce direttamente nello stesso spazio dove vivono i token di testo. Immagini e parole vengono elaborate dalla stessa attenzione, condividendo la stessa rappresentazione interna. Non c'è un traduttore: ci sono due lingue che diventano una sola.

Questa scelta progettuale ha conseguenze dirette su memoria, velocità e qualità delle risposte multimodali. Ed è precisamente il motivo per cui testarlo con la stessa batteria di prove dei modelli precedenti è interessante: non si sta misurando solo la dimensione, si sta misurando anche un'idea diversa di come i dati dovrebbero scorrere attraverso un modello.

## La configurazione: finalmente senza compromessi

Ed eccoci al cuore dell'esperimento. Per la prima volta in questa serie di test, ho potuto configurare il modello senza dover scegliere cosa sacrificare. LM Studio mostrava il verde deciso, non l'arancione del limite come con il 26B MoE, non il rosso della configurazione sconsigliata.
![tabella1.jpg](tabella1.jpg)

Il dettaglio che cambia tutto è l'offload GPU: 48 layer su 48. Il modello gira interamente nella VRAM, senza dover distribuire parti di sé sulla RAM di sistema. Con il 26B MoE in Q4_K_M ero costretto a un offload parziale, e quella scelta pesava sulla velocità e sulla latenza. Qui, per la prima volta, la macchina lavora senza quel freno.

Il risultato lo si sente immediatamente: la velocità media si è assestata intorno ai 17 token al secondo, contro i 10-12 di Qwen 36 35B, e di poco sotto i 20 di Gemma 4 26B che con 8B attivi ( gli "esperti attvi" pesavano molto sulle prestazioni, 8 era il punto migliore).

C'è un paradosso interessante emerso dai test. Gemma 4 26B MoE è risultato più veloce del 12B, nonostante abbia il doppio dei parametri totali. Il segreto sta nell'architettura. Il 26B è un modello MoE: su 25 miliardi di parametri totali, ne attiva solo circa 4 (8 nel mio test) per ogni token. È come avere una biblioteca enorme ma, per ogni domanda, sfogli solo un piccolo numero di libri. Il 12B, essendo un modello denso, attiva invece tutti i suoi 12 miliardi di parametri a ogni token, facendo più calcoli e quindi risultando leggermente più lento nella media.

Tuttavia, i 25 miliardi di parametri del MoE devono comunque risiedere in VRAM, occupando più del doppio della memoria del 12B. E l'overhead di routing per gestire gli esperti diventa evidente su contesti lunghi, dove il 26B perde parte del suo vantaggio mentre il 12B mantiene performance più stabili. In sintesi: il 26B è più veloce ma più esigente in VRAM e meno stabile su sequenze lunghe; il 12B è più leggero, prevedibile e per la maggior parte degli usi quotidiani più che sufficiente. La scelta dipende da cosa cercate.

## I test

### Test 1 — Ragionamento scientifico: il meccanismo di Higgs *(5/5)*

*Velocità: 17,45 token/secondo*

Quello che uso da sempre come termometro dell'intelligenza del modello: spiegare il meccanismo di Higgs e la rottura della simmetria elettrodebole a uno studente universitario di fisica. Una domanda che richiede rigore senza sacrificare la chiarezza, e la capacità di costruire un percorso che guidi il lettore attraverso concetti non banali.

La risposta è arrivata strutturata in cinque sezioni con la logica di una lezione ben condotta, partendo dal problema centrale, cioè perché non si possono scrivere termini di massa espliciti senza violare l'invarianza di gauge, fino alla soluzione completa, con il gruppo di gauge SU(2)_L × U(1)_Y, la condizione μ² < 0 che rende il minimo del potenziale non più in zero, e la spiegazione del perché il fotone rimane senza massa grazie alla simmetria residua U(1)_em. La precisione scientifica era impeccabile: formule corrette, valore di aspettazione del vuoto, la suggestiva immagine dei bosoni di Goldstone che vengono "mangiati" dalla polarizzazione longitudinale, una "sintesi per l'esame" finale in cinque punti che riassume l'intero meccanismo senza banalizzarlo.

Quello che colpisce, però, non è solo la qualità della risposta: è la velocità con cui è arrivata. Con Qwen3.6 35B ero a circa 11 token al secondo. Con Gemma 4 26B MoE a circa 10. Con questo modello a 17,45. La differenza non è trascurabile nella pratica quotidiana.

**Voto: 5/5.** Un'apertura di serie difficile da migliorare.

### Test 2 — Multimodalità: leggere un foglio di calcolo aziendale *(5/5)*

*Velocità: 17,64 token/secondo*

Il secondo test metteva alla prova la parte multimodale con un'immagine deliberatamente non ideale: uno screenshot di un foglio Excel intitolato "COSTI DEL PERSONALE", una proiezione finanziaria su cinque anni dal 2023 al 2027, con colonne per voci di costo, unità, costi unitari e totali.

Il modello ha fatto quello che ci si aspetta da un analista, non da un OCR. Ha identificato correttamente la struttura del documento, le cinque categorie, Valori complessivi, Operai specializzati, Impiegati, Dirigenti, Collaboratori, ha letto i valori numerici con precisione, ha notato che i costi unitari rimangono fissi per tutto il periodo mentre le unità aumentano, e ne ha tratto la conclusione corretta: non è inflazione, è espansione del team. Ha identificato il 2026 come "l'anno della grande espansione", con il salto netto dei costi complessivi, e ha persino osservato che i contributi previdenziali calcolati costantemente al 33% indicano una pianificazione fiscale standardizzata. Un dettaglio che un CFO noterebbe, e che il modello ha estratto autonomamente da una tabella.

Questa è la differenza che l'architettura unificata dovrebbe portare: non solo leggere i dati, ma capire il contesto in cui esistono. Se il test 1 ha confermato le aspettative, il test 2 ha cominciato a rispondermi alla domanda che avevo in testa dall'inizio.

**Voto: 5/5.** Lettura e analisi, non solo trascrizione.

### Test 3 — Generazione di codice: un problema NP-hard *(4,95/5)*

*Velocità: 17,99 token/secondo*

Il test di coding classico della serie: implementare in Python un algoritmo per trovare il ciclo di lunghezza massima in un grafo non orientato, con la richiesta di spiegare la complessità temporale. Un problema NP-hard che richiede non solo capacità implementativa ma consapevolezza teorica.

La risposta era tecnicamente eccellente, probabilmente la migliore ottenuta su questo test nell'intera serie. Il modello ha aperto dichiarando esplicitamente che il problema è NP-hard e che non esiste un algoritmo a tempo polinomiale noto, una maturità teorica che non tutti gli assistenti di programmazione mostrano. L'implementazione in backtracking con DFS era pulita e corretta, con una tecnica di "symmetry breaking" che impone `neighbor > start_node` per evitare di esplorare lo stesso ciclo più volte, un'ottimizzazione non banale che riduce lo spazio di ricerca. Spiegazione della complessità chiara e onesta: fattoriale nel caso peggiore, lineare nello spazio.

C'è però un'unica, piccola, macchia: la risposta è arrivata in inglese, nonostante il prompt fosse in italiano. Nei test 1 e 2 il modello aveva risposto correttamente in italiano, quindi non è un problema strutturale. È una disattenzione. Il codice è perfettamente funzionante, la spiegazione è chiara, ma la mancata aderenza alla lingua del prompt è un segnale che vale la pena notare. Nulla che comprometta il risultato tecnico, ma qualcosa che in un assistente quotidiano non si vorrebbe vedere.

**Voto: 4,95/5.** La soluzione migliore della serie su questo test, con un neo linguistico che non inficia la sostanza.

### Test 4 — Multilingua e pianificazione: cinque giorni in Giappone *(5/5)*

*Velocità: 17,41 token/secondo*

Il test multilingua: agire da agente di viaggio, pianificare un itinerario di cinque giorni in Giappone per un cliente francese, con focus su templi storici e cibo di strada, e una sezione finale in italiano con consigli per un turista italiano. Il test che nel 26B MoE aveva prodotto "suggeramenti" e una parola con desinenza cirillica.

Il francese era impeccabile, fluente, con espressioni che mostrano una padronanza stilistica vera: "âme historique", "havre de paix", "splendeur des temples". L'itinerario era logistico e realistico, Asakusa con il Senso-ji il primo giorno, Meiji Jingu e Harajuku il secondo, Shinkansen per Kyoto e Fushimi Inari il terzo, Kinkaku-ji e Kiyomizu-dera il quarto, Nara con il Todai-ji il quinto. Cinque giorni pieni ma non impossibili. I consigli pratici erano concreti e utili: la carta Suica, il Pocket Wi-Fi, l'etichetta di non mangiare camminando, le frasi chiave in giapponese traslitterato.

La sezione in italiano è stata la migliore che abbia ottenuto su questo test nell'intera serie. Nessun "suggeramenti", nessuna desinenza cirillica, nessuna sbavatura. Solo italiano corretto, fluente, utile. Un risultato che il 26B MoE non aveva raggiunto, almeno non in modo così pulito.

C'è però un piccolo lapsus lessicale nel titolo del quinto giorno, dove il modello scrive "Les Daimyos", i signori feudali, invece di "Les daims", i cervi sacri di Nara. Una confusione tra due termini che suonano simili ma hanno significati completamente diversi. Non compromette la comprensione dell'itinerario, ma vale la pena segnalarlo.

**Voto: 5/5.** La migliore sezione in italiano della serie, con un piccolo lapsus francese che non scalfisce il risultato complessivo.

### Test 5 — Contesto lungo: 460 pagine al volo *(4,8/5)*

*Velocità: 10,15 token/secondo*

Qui le cose si fanno interessanti. Lo stesso AI Index Report 2025 di Stanford, lo stesso PDF di circa 460 pagine caricato in tutti i test precedenti, la stessa domanda sulla crescita della generazione video con richiesta di indicare le pagine di riferimento.

Il modello ha risposto al primo tentativo, senza blocchi, senza sollecitazioni, il che è già un miglioramento significativo rispetto ai problemi che avevo avuto con Qwen 3.5. La sintesi era corretta e pertinente: modelli emergenti come Runway, Luma e Kuaishou, il celebre esempio del prompt "Will Smith eating spaghetti" come marcatore del salto qualitativo, le funzionalità di Movie Gen di Meta, il confronto tra Veo 2 e concorrenti. Tutto presente, tutto accurato.

Tuttavia, la precisione nel recupero della pagina è stata meno granulare rispetto ai test precedenti. Il modello ha indicato "intorno alla pagina 127", mentre Gemma 26B aveva indicato le pagine 125-126-127 e Qwen3.6 126-127. Non è un errore, è una risposta meno precisa. La differenza tra "qui esattamente" e "più o meno qui".

Il dato più significativo, però, è un altro: la velocità è crollata a 10,15 token al secondo, contro i 17 e più dei test precedenti. È la prima volta in questa sessione che la generazione rallenta sensibilmente. La causa è il contesto saturo: con 24k token attivi e un PDF enorme da processare, la VRAM si riempie e il throughput cala. Non è un difetto del modello, è la fisica della memoria. Ma è un'informazione preziosa per chi deve scegliere: su compiti che richiedono contesti molto lunghi, la fluidità diminuisce.

**Voto: 4,8/5.** Risposta al primo tentativo, ma meno precisa e più lenta dei test precedenti. Il contesto lungo ha un costo.

### Test 6 — Ragionamento spaziale: la stanza nel caos *(5/5)*

*Velocità: 17,56 token/secondo*

La fotografia di una stanza in forte disordine, la stessa usata in tutta la serie. Descrivere la disposizione degli oggetti e suggerire come riordinare per creare più spazio. Un test che misura qualcosa di difficilmente standardizzabile: l'intelligenza visuo-spaziale, la capacità di vedere una scena tridimensionale in una fotografia bidimensionale e ragionare su di essa.

La velocità è tornata immediatamente ai livelli dei primi test, confermando che il calo del test precedente era legato al contesto lungo e non a un problema generalizzato. La risposta era precisa e ben organizzata per aree funzionali: il letto come elemento centrale sommerso da lenzuola e vestiti, i due scaffali a scala ai lati della testiera, l'area studio con scrivania e mobiletto, il pavimento come area più critica. Il modello ha notato la cesta blu ai piedi del letto, il plaid rosso sul lato destro, lo specchio che "raddoppia visivamente il disordine", i vestiti sparsi e le scarpe. La strategia di riordino era logica e motivata: prima il pavimento perché è l'ostacolo principale alla circolazione, poi la cesta blu come punto di accumulo, poi il letto, infine gli scaffali per ridurre il rumore visivo.

Rispetto ai test migliori della serie, il modello non è arrivato a notare i riflessi specifici nello specchio con lo stesso livello di dettaglio che avevo visto con Qwen3.5 e Gemma 26B. Ma la qualità della descrizione e della pianificazione è comunque eccellente. Non è un passo indietro: è una scelta diversa di cosa enfatizzare.

**Voto: 5/5.** Descrizione precisa, piano di riordino logico, velocità tornata ai livelli ottimali.

### Test 7 — Agente multi-step: pianificare un progetto software *(5/5)*

*Velocità: 17,26 token/secondo*

Il test che misura la capacità di organizzare il lavoro, non solo di eseguirlo. Ho chiesto di pianificare lo sviluppo di una web app per la gestione delle spese familiari: stack tecnologico, struttura del progetto, roadmap dettagliata per un team di due sviluppatori.

La risposta ha dimostrato una maturità progettuale notevole. Lo stack proposto era moderno e coerente: Next.js con Tailwind per il frontend, Node.js con Prisma ORM per il backend, PostgreSQL, NextAuth.js per l'autenticazione, Recharts per i grafici, PapaParse per il CSV, react-pdf per i report, Resend per le email. Ogni scelta aveva una logica implicita nel contesto del progetto. La struttura del codice era organizzata per feature, un approccio professionale e scalabile. La roadmap si articolava in otto sprint con focus chiari, deliverable concreti, suddivisione del lavoro tra i due sviluppatori, e, dettaglio che fa la differenza, criticità identificate per ciascuno. "Formati CSV non standardizzati", "rendering del PDF difficile", "bug imprevisti in produzione": la capacità di anticipare i problemi prima che si verifichino è il segnale di una comprensione profonda del ciclo di sviluppo software. I consigli strategici conclusivi, "Database First", validazione con Zod, test unitari per i calcoli finanziari, erano pratici e da senior developer.

È il tipo di risposta che un project manager esperto firmerebbe, non solo uno strumento che scrive codice su richiesta.

**Voto: 5/5.** Pianificazione completa, realistica, con le criticità giuste al posto giusto.

### Test 8 — Conversazione lunga: coerenza su quattro turni *(5/5)*

*Velocità: da 17,65 a 15,98 token/secondo*

Il test che valuta una qualità diversa dalle altre: non la bravura su una singola risposta, ma la capacità di mantenere il filo attraverso una conversazione che si costruisce nel tempo. Qwen3.6 aveva introdotto questa prova per testare la sua funzionalità di "thinking preservation". Qui l'ho riproposta con la stessa struttura: quattro turni su una sessione di progettazione collaborativa, con scelte tecnologiche che si accumulano e si raffinano.

Nel primo turno ho chiesto un consiglio sullo stack per un'app di task management. Nel secondo, come gestire le notifiche in tempo reale per 1000 utenti contemporanei: il modello ha spiegato perché il polling sia sconsigliato e perché WebSocket con Redis Pub/Sub sia la scelta corretta, citando anche l'alternativa SSE con pro e contro. Nel terzo, lo schema del database: sei tabelle in ordine logico, relazioni chiave, consigli da senior developer sull'uso di UUID, indici e soft delete. Nel quarto, ho chiesto un riepilogo di tutte le scelte fatte e una strategia di scalabilità a 10.000 utenti.

Il modello ha ricordato correttamente tutto. Lo stack del primo turno, le motivazioni per WebSocket del secondo, le strutture dati del terzo. Ha aggiunto spontaneamente una strategia di scalabilità in cinque punti: load balancer, Redis Pub/Sub per la gestione distribuita delle connessioni, connection pooling con PgBouncer, code asincrone con BullMQ, caching. Nessuna contraddizione, nessuna dimenticanza.

Un dato vale la pena segnalare: la velocità è calata progressivamente, da 17,65 token al secondo nel primo turno a 15,98 nel quarto. Il fenomeno è prevedibile e fisicamente comprensibile, con ogni turno la cache KV si riempie e il modello deve gestire un contesto sempre più lungo. Il calo è contenuto, circa 1,7 token al secondo in quattro turni, e non compromette la fluidità. Ma è un comportamento reale che chi usa il modello per sessioni di lavoro prolungate troverà utile conoscere.

**Voto: 5/5.** Coerenza mantenuta attraverso quattro turni, qualità costante, calo marginale della velocità nella norma.

### Test 9 — Generazione video: non ancora *(non valutato)*

Come nelle puntate precedenti, LM Studio non supporta ancora l'input video. I motivi sono già spiegati nell'[articolo su Qwen3.6](https://aitalk.it/it/qwen36-35b-ai.html), dove ho documentato anche i tentativi con formati alternativi. La questione rimane aperta e merita un approfondimento dedicato, probabilmente con llama.cpp o vLLM.

## Configurazione minima: quante risorse servono davvero

Uno degli aspetti più interessanti emersi da questo test è che Gemma 4 12B in Q8_0 non richiede una workstation straordinaria. Sulla base della mia esperienza diretta, ecco i requisiti minimi per farlo girare in modo accettabile, ovvero con una velocità intorno ai 15-17 token al secondo e senza swap continuo sulla RAM:
![tabella2.jpg](tabella2.jpg)

Il confronto con i modelli precedenti della serie racconta una storia precisa:
![tabella3.jpg](tabella3.jpg)

La conclusione pratica è questa: se avete una GPU con 12-14 GB di VRAM, potete far girare Gemma 4 12B Q8_0 in full GPU con prestazioni eccellenti. Se avete meno VRAM, potete scendere a Q6 o Q4 e ottenere comunque risultati dignitosi. Con i modelli più grandi, anche con quantizzazioni spinte, eravate già al limite o oltre.
![tabella4.jpg](tabella4.jpg)

## La risposta alla domanda

La media aritmetica degli otto test eseguiti è 4,97 su 5. Un numero alto, ma non è il numero il punto più interessante di questo esperimento.

Il punto interessante è la configurazione con cui è stato raggiunto. Per la prima volta in questa serie di test, ho eseguito un modello completamente in GPU, 48 layer su 48, senza strozzature di nessun tipo. La velocità media di circa 17 token al secondo è stata costante e fluida, un punto di mezzo tra i modelli provati più che accettabile e che non porta al limite una macchina di questo tipo, garantendo una stabilità nelle risposte e riducendo il rischio di crash improvvisi. E questa differenza, nella pratica quotidiana, cambia la natura dell'interazione.

C'è una scena in *Ping Pong the Animation*, l'adattazione dell'omonimo manga di Taiyo Matsumoto, in cui il personaggio più dotato tecnicamente perde contro un avversario che dovrebbe essere inferiore, semplicemente perché quest'ultimo gioca senza nessun peso sulla schiena, senza paura, al massimo di quello che può fare. Non è una questione di talento assoluto: è una questione di margine libero tra potenziale e esecuzione. Gemma 4 12B su questa configurazione mi ha dato la stessa sensazione: un modello che gioca la sua partita intera, senza nulla trattenuto.

La domanda che ha motivato questo esperimento era: "Un modello più piccolo usato al massimo può battere uno più grande ma strozzato?" La risposta che mi porto a casa è sì, per la maggior parte degli usi quotidiani. Il 12B in Q8_0, con full GPU offload, produce risposte di qualità eccellente, è veloce, ha una latenza più prevedibile grazie all'architettura densa, senza i picchi variabili tipici dei modelli MoE, e richiede meno memoria. Il 26B MoE in Q4_K_M con offload parziale rimane un ottimo modello, ma perde in fluidità e reattività su hardware consumer standard.

C'è poi la questione dell'architettura multimodale. Il 12B, con il suo approccio unificato che elimina gli encoder separati, promette una comprensione più integrata di testo e immagini. Non ho potuto testare la parte video per i limiti di LM Studio, ma quello che ho visto sul test delle tabelle aziendali, dove il modello non si è limitato a leggere i dati ma li ha interpretati nel loro contesto, suggerisce che la scelta progettuale non sia solo teoricamente elegante. Funziona.

La vera notizia, per chi legge, è questa: oggi esiste un modello di altissima qualità che gira interamente sulla vostra GPU consumer, senza compromessi. Non dovete più scegliere tra "modello grande ma strozzato" e "modello piccolo ma insufficiente". Gemma 4 12B è il punto di equilibrio che in molti stavano aspettando. E il fatto che sia anche architetturalmente più avanzato del suo predecessore nella gestione multimodale è la ciliegina su una torta che, questa volta, si è cotta bene.

---

*Tutti gli articoli della serie: [Qwen 3.5 sul mio PC](https://aitalk.it/it/qwen3.5-locale-puntata1) — [Gemma 4 26B in locale](https://aitalk.it/it/gemma4-26b.html) — [Qwen3.6 35B in locale](https://aitalk.it/it/qwen36-35b-ai.html)*
