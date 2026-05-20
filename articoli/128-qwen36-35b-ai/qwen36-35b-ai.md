---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-05-20
author: "Dario Ferrero"
youtube_url: "https://youtu.be/8nxskrXNlto?si=Kyz9i_DZ9sEzNSfx"
---

# Qwen 3.6 in locale: 35 miliardi sul mio PC
![qwen36-35b-ai.jpg](qwen36-35b-ai.jpg)

*C'è un momento, in ogni serie di esperimenti, in cui ti rendi conto che il problema non è più il soggetto del test, ma la qualità del tuo strumento di misura. Stavo raccogliendo i voti dell'ottava prova e pensavo che forse il limite sono diventati i miei test: cinque su cinque, otto volte su otto. Il termometro funziona ancora, oppure l'acqua ha smesso di variare di temperatura?*

La domanda non è retorica. Questi articoli nascono come diario di bordo di un laboratorio domestico, non come white paper accademico, e il metodo rimane volutamente personale: nessun benchmark automatizzato, nessuna metrica standardizzata, solo prompt calibrati su scenari realistici e la sensazione tattile di chi usa lo strumento e poi lo racconta. L'hardware non è cambiato rispetto alle puntate precedenti, AMD Ryzen 7700, 32 GB di RAM, GPU AMD con 16 GB di VRAM, e nemmeno il software: [LM Studio](https://lmstudio.ai/), la soluzione più accessibile per chi vuole eseguire modelli locali senza perdere un pomeriggio in configurazioni da terminale. Per tutti i dettagli sull'installazione, sull'ecosistema e sulla filosofia di questo laboratorio rimando alla [prima puntata della serie su Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), che resta il riferimento metodologico dell'intera serie. Chi è già a bordo può continuare da qui.

Oggi il protagonista è diverso dagli altri. Non per categoria, ma per dimensione: [Qwen3.6 35B A3B in quantizzazione Q6](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), il modello più grande che abbia mai caricato su questa macchina, letteralmente al limite di quello che la configurazione può reggere. Dopo aver esplorato [Qwen 3.5 9B nelle prime due puntate](https://aitalk.it/it/qwen3.5-locale-puntata2.html) e [Gemma 4 26B MoE](https://aitalk.it/it/gemma4-26b.html) nella terza, questo salto di scala era inevitabile. Ed è esattamente il salto che volevo fare.

## Trentacinque miliardi, tre alla volta

Il nome nasconde un'architettura che vale la pena capire, perché cambia radicalmente il modo in cui si ragiona sui requisiti hardware. Qwen3.6 35B A3B è un modello Mixture of Experts: ha 35 miliardi di parametri totali, ma per ogni token generato ne attiva soltanto circa 3 miliardi. Non tutti gli esperti vengono chiamati a rispondere ogni volta, solo quelli ritenuti più competenti per quel frammento specifico di testo. È un po' come avere un'orchestra di duecentocinquantasei musicisti, dove il direttore sceglie di volta in volta quali otto strumentisti far suonare, lasciando gli altri in ascolto e pronti. Il risultato pratico è che il costo computazionale assomiglia più a quello di un modello da tre miliardi che a uno da trentacinque, pur attingendo alla profondità di quest'ultimo quando serve.

Qwen3.6, descritto nel [blog ufficiale Alibaba](https://qwen.ai/blog?id=qwen3.6) come evoluzione dell'architettura Qwen3, porta con sé quattro novità che il team ha voluto sottolineare: un miglioramento del 43% su QwenWebBench nelle capacità di generazione di codice agentivo e di applicazioni web complete, una funzionalità chiamata *thinking preservation* per mantenere la coerenza del ragionamento attraverso conversazioni multi-turno, un salto nella comprensione multimodale con immagini e documenti, e il supporto nativo alla comprensione video, quest'ultima ancora sperimentale e non supportata da tutti i runtime disponibili.

La quantizzazione Q6 su cui ho lavorato rappresenta un compromesso ragionato: meno pesante della F16 pura, molto più fedele al modello originale rispetto alle quantizzazioni aggressive come Q4. In pratica si perde pochissima qualità rispetto ai pesi interi, pagando un costo in memoria che, sulla mia configurazione, ha richiesto un bilanciamento attento tra GPU e RAM di sistema.

## La configurazione al limite

Qui sta l'esperimento vero. Non ho cercato il punto di massima performance: ho cercato deliberatamente il bordo del possibile, ovvero capire cosa succede quando si lavora con il minimo accettabile di performance, almeno secondo il mio parere.

I parametri scelti: contesto a 8078 token (il modello nativamente supera i 262.000), offload GPU di 8 layer su 43 totali, 8 esperti attivi su 256 disponibili, quantizzazione F16 internamente per i layer in GPU. La velocità risultante si è assestata intorno agli 11 token al secondo, contro i 20-25 che Qwen 3.5 9B raggiungeva comodamente. Non è una velocità che consiglierei per un assistente conversazionale da usare al volo, ma è del tutto accettabile per sessioni di lavoro strutturate in cui non si è di fretta e si privilegia la profondità della risposta.

La domanda che sottende tutto l'esperimento è semplice: il sacrificio di velocità vale la qualità guadagnata? I test che seguono sono la risposta.

## Un passo oltre: la configurazione ottimale

La scelta di partire da 8 layer in GPU e contesto ridotto era deliberata: volevo testare il modello in condizioni di reale scarsità di risorse, il punto più basso del range accettabile. Ma una volta completata la batteria di test, ho voluto capire dove si trova il vero punto di equilibrio su questo hardware.

I risultati sono stati istruttivi. Portare i layer in GPU da 8 a 16 fa salire la velocità da 11 a circa 14,5 token al secondo, un guadagno sensibile. Sorprendentemente, raddoppiarli ancora a 32 non cambia quasi nulla (14,49 tok/s), e tentare il caricamento a 40 layer impedisce al modello di partire del tutto: la VRAM non regge. Il punto ottimale per questo hardware è quindi 16 layer, non di più.

Altrettanto interessante è il comportamento del contesto: allargarlo da 8.000 token fino al massimo nativo di 262.000 incide pochissimo sulla velocità, con un calo di meno di un token al secondo tra i due estremi. In pratica si può scegliere la finestra di contesto in base al compito senza preoccuparsi delle prestazioni.

Il parametro che invece fa davvero la differenza è il numero di esperti attivi. Con 4 esperti si sale a 16,2 tok/s, con 8 si è a 14,2, con 16 si scende a 11,4, con 125 si crolla a 2,9. È una relazione quasi lineare verso il basso: ogni esperto aggiuntivo costa, e su hardware consumer il costo si sente immediatamente.

Tutti i test con configurazioni diverse hanno comunque prodotto risposte di qualità eccellente, il che suggerisce che ridurre gli esperti attivi non compromette la qualità in modo percepibile, almeno sui task usati in questa serie.

La configurazione di miglior compromesso su questo hardware risulta quindi: 16 layer in GPU, contesto 125.000 token, 8 esperti attivi, con una velocità di circa 14,2 token al secondo. Non è la velocità di un modello piccolo, ma è un passo avanti rispetto alla configurazione "al limite" usata nei test principali, e apre la porta a sessioni di lavoro su documenti lunghi senza dover rinunciare alla qualità.
![grafico1.jpg](grafico1.jpg)
[Immagine dei risultati dei benchmark tratta da qwen.ai](https://qwen.ai/blog?id=qwen3.6)

## I test

### Test 1 — Meccanismo di Higgs e fisica delle particelle *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 11,17 token/s*

La risposta è stata eccezionale, probabilmente la migliore che abbia mai ottenuto da un modello locale su un tema scientifico complesso. Il modello ha aperto con il contesto teorico, descrivendo la simmetria di gauge che governa le interazioni elettrodeboli. Ha poi introdotto il campo di Higgs e il suo celebre potenziale "a cappello messicano", spiegando perché lo zero non è il minimo energetico. Ha mostrato come il valore di aspettazione del vuoto interagisca con i bosoni di gauge, conferendo massa ai W e agli Z. E ha chiarito il dettaglio più sottile, quello che spesso manca anche nelle trattazioni universitarie: perché il fotone rimane senza massa, grazie a una simmetria residua che il vuoto del Higgs non riesce a rompere.

La struttura della risposta era impeccabile, organizzata in sezioni logiche che procedevano dal generale al particolare senza mai perdere il filo. Il linguaggio era preciso ma accessibile, usando metafore come quella del "cappello messicano" per rendere intuitivi concetti astratti. Non ho trovato errori né nei concetti fisici né nei dettagli matematici. La velocità di 11 token al secondo è più bassa rispetto ai modelli più piccoli testati in precedenza, ma la qualità di questa risposta paga ampiamente il compromesso. La pazienza di attendere qualche secondo in più è stata ripagata da una spiegazione che si potrebbe definire da manuale.

### Test 2 — Multimodalità e comprensione di tabelle *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 10,49 token/s*

L'immagine caricata era volutamente di bassa qualità: un piccolo screenshot di un'interfaccia di gestione fatture, imperfetto per mettere alla prova le capacità visive in condizioni realistiche, non ideali. Il modello ha superato la prova con risultati sorprendenti.

La prima cosa che ha colpito è stata la capacità di comprendere la struttura generale dell'interfaccia. Il modello ha identificato correttamente le tre sezioni principali, il pannello dei filtri in alto, l'elenco laterale dei prodotti a destra, la tabella centrale. Ha riconosciuto che si trattava probabilmente di un'applicazione di gestione contabile, ipotizzando anche che potesse essere un database di esempio o un ambiente di test, vista la genericità dei nomi dei clienti e degli articoli.

La lettura dei dati è stata precisa e dettagliata: tutte le colonne della tabella enumerate correttamente, l'aliquota IVA fissa al 22% rilevata come costante su tutte le righe, la colonna "Importo" evidenziata in giallo segnalata come elemento di navigazione per l'utente, le date delle fatture identificate nel periodo gennaio-marzo 2022. Ma la parte più pregevole è stata l'analisi delle anomalie: nonostante il filtro superiore mostrasse l'opzione "DA PAGARE" come selezionata, le fatture nella tabella avevano già una data di pagamento e un importo saldato. Il modello ha segnalato il possibile mix di dati, formulando ipotesi sensate sul contesto d'uso. Un modello più piccolo avrebbe prodotto una descrizione generica. Qui ho ottenuto un'analisi vera, con interpretazione delle incongruenze inclusa.

### Test 3 — Generazione di codice complesso *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 10,06 token/s*

Questo test era uno dei più importanti dell'intera batteria, perché Qwen3.6 promette un miglioramento del 43% su QwenWebBench proprio nella generazione di codice. Volevo vedere se la promessa si traduceva in un'implementazione concreta e funzionante su un problema algoritmico non banale: trovare il ciclo di lunghezza massima in un grafo non orientato.

La risposta ha convinto pienamente. Il modello ha aperto con una premessa teorica che pochi assistenti di programmazione hanno la maturità di includere: ha dichiarato esplicitamente che il problema è NP-difficile, che non esiste un algoritmo polinomiale per risolverlo su grafi generici, e che qualsiasi soluzione esatta avrà complessità esponenziale nel caso peggiore. Questa consapevolezza è rara e preziosa, perché dimostra che il modello non sta cercando di vendere una soluzione magica, ma comprende profondamente i limiti del dominio.

L'implementazione proposta era elegante e funzionante: strategia DFS con tracciamento del cammino, struttura dati con mappa depth per rilevare i back-edge e calcolare la lunghezza dei cicli in tempo costante, rappresentazione del grafo tramite lista di adiacenza efficiente, backtracking implementato correttamente, gestione completa dei casi limite come grafi senza cicli e componenti disconnesse. Ho particolarmente apprezzato l'uso della mappa depth, più elegante e performante di una semplice ricerca lineare nel path perché permette di calcolare la lunghezza del ciclo senza scansionare l'intera lista. La spiegazione della complessità temporale è stata chiara e onesta, con distinzione tra il caso favorevole e il caso peggiore. Nessun errore sintattico o logico, type hint presenti, struttura modulare. Un codice che si potrebbe consegnare.

### Test 4 — Multilingua e pianificazione *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 11,15 token/s*

*Nota metodologica: eseguito in chat pulita dopo che una prima esecuzione in chat con cronologia aveva prodotto risultati mediocri.*

Questo test ha insegnato qualcosa di importante prima ancora del risultato. La prima esecuzione, in una chat con iterazioni precedenti su altri argomenti, aveva prodotto interruzioni e qualità mediocre. Ripetuto in chat completamente nuova, il risultato è stato trasformato. La differenza è stata talmente netta da meritare una nota metodologica permanente: la cronologia della chat, anche quando sembra innocua, può alterare significativamente i risultati su compiti complessi. Testare in chat pulita non è un capriccio, è igiene sperimentale.

In chat pulita, Qwen3.6 ha prodotto un itinerario di cinque giorni a Tokyo in francese, completo e articolato, al primo tentativo. Il francese era di livello madrelingua: "spécialités de rue", "ambiance vieux Tokyo", "cadre apaisant", "ruelle atmosphérique", "patrimoine UNESCO". Nessun errore grammaticale o sintattico, fluidità da livello avanzato.

L'itinerario era logisticamente perfetto, con giorni bilanciati tra templi e cibo di strada, e pieno di accorgimenti da viaggiatore esperto: arrivare a Fushimi Inari prima delle otto per evitare la folla, stampare i nomi dei templi in giapponese, usare i modelli di cibo nei ristoranti per ordinare senza parlare la lingua. La sezione trasporti spiegava come attivare Suica o Pasmo sullo smartphone, come prenotare lo Shinkansen, che gli uffici informazioni nelle stazioni principali hanno personale francofono in alcuni orari. Ha suggerito il Kyoto City Bus Day Pass e consigliato di scaricare le mappe offline. Per la barriera linguistica ha proposto non solo Google Translate ma anche Papago per il riconoscimento vocale, e frasi chiave in giapponese traslitterato.

La richiesta sezione finale in italiano, per testare il multilingua all'interno di uno stesso prompt, era pulita, corretta, ricca di consigli pratici sui pagamenti in contanti, i bancomat Seven-Eleven, le schede di traduzione per le allergie alimentari.

### Test 5 — Contesto lunghissimo: documento da 460 pagine *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 10,93 token/s*

Questo è stato il test più sorprendente dell'intera batteria, e merita di essere raccontato con la dovuta attenzione. Ho caricato l'*AI Index Report 2025*, un PDF di circa 460 pagine e oltre 20 milioni di caratteri, chiedendo al modello di descrivere la crescita della generazione video e di indicare le pagine dove trovare i dati. La sfida era deliberatamente estrema: contesto di soli 8078 token, ben lontano dai 262.000 nativi del modello, soli otto esperti attivi, soli otto layer in GPU.

La risposta mi ha lasciato senza parole. Nonostante i parametri ridotti all'osso, il modello ha fornito un riassunto preciso e ben strutturato dei progressi nella generazione video tra il 2023 e il 2025. Ha citato correttamente i modelli principali: Meta Movie Gen, Google Veo e Veo 2, Runway Gen-3 Alpha, Luma Dream Machine, Kling 1.5. Ha menzionato il famoso esempio del prompt "Will Smith eating spaghetti" come marcatore del salto qualitativo avvenuto nel settore. Ha indicato figure specifiche nel report, come la Figura 2.3.11 e la Figura 2.3.12. E ha dichiarato che i dati principali si trovavano alle pagine 126 e 127 del report. Ho verificato. Era esatto.

Come sia riuscito a trovare l'informazione giusta in un documento di 460 pagine con una finestra di contesto corrispondente a poche decine di pagine rimane il mistero più affascinante di tutta la sessione. Probabilmente il modello ha saputo identificare e conservare le sezioni più rilevanti nonostante i vincoli di memoria, ma il meccanismo esatto non è trasparente dall'esterno. Quello che è trasparente è il risultato: con una configurazione ridotta all'osso, su un documento enorme, riferimenti verificabili alle pagine corrette. Questa è robustezza.

### Test 6 — Ragionamento spaziale *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 11,42 token/s*

Il test chiedeva di analizzare la fotografia di una stanza in disordine e proporre un piano di riordino. Nonostante i parametri conservativi, soli otto esperti, soli otto layer in GPU, il modello ha prodotto un'analisi visuo-spaziale di altissimo livello.

La descrizione era fedele e dettagliata: letto con struttura in metallo nero, due librerie a scala bianche posizionate correttamente, scrivania grigia ingombra, piccolo armadietto bianco, specchio sull'anta. Colori delle pareti identificati come verde salvia chiaro, pavimento con moquette stampata, tende a righe verdi e bianche. Persino la cesta della biancheria blu al centro del pavimento, circondata da vestiti sparsi, scarpe, scatole, forbici e altri oggetti, era stata rilevata e catalogata.

Il piano di riordino era strutturato per priorità visive con motivazioni solide. Prima i vestiti da terra e dal letto, perché rimuoverli libera il percorso di movimento e riduce il rumore visivo, facendo sembrare la stanza più grande. Poi il letto, perché un letto sfatto occupa visivamente più spazio e crea senso di caos, mentre raddrizzarlo definisce i confini della stanza. Poi la cesta della biancheria e le scarpe, ostacoli fisici che bloccano il "naviglio" centrale (termine curioso e efficace). Infine la scrivania, la cui superficie libera proietta ordine e funzionalità. La sintesi finale era perfetta: "L'obiettivo iniziale non è il minuzioso, ma il volume." Una frase che riassume l'essenza dell'organizzazione efficace in un ambiente molto disordinato, e che un professionista del settore non avrebbe saputo dire meglio.

### Test 7 — Agente multi-step: pianificazione progetto software *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, 11,04 token/s*

Questo test è stato introdotto appositamente per verificare la promessa del 43% di miglioramento su QwenWebBench. Un modello che eccelle in fisica e ragionamento spaziale potrebbe comunque fallire in un compito di pianificazione articolata. La vera maturità di un assistente di programmazione si vede nella capacità di organizzare il lavoro, anticipare problemi e fornire soluzioni pratiche, non solo scrivere codice. Il compito era pianificare lo sviluppo di una web app per la gestione delle spese familiari, con un team di due sviluppatori e una roadmap dettagliata.

La risposta è stata probabilmente la più completa dell'intera batteria. Lo stack tecnologico proposto era moderno e coerente, con ogni scelta motivata in una tabella chiara: React con TypeScript e Vite per il frontend, Node.js con Express per il backend, PostgreSQL con Prisma come ORM, JWT per l'autenticazione, papaparse per il parsing CSV, React-PDF per l'esportazione, BullMQ per le code di notifiche, Docker per l'infrastruttura. La struttura del progetto era dettagliata per cartelle logiche sia lato frontend che backend, con un docker-compose.yml per orchestrare Postgres, Redis e l'applicazione. Questa è la struttura che userebbe un vero ingegnere del software.

La pianificazione in sei sprint settimanali era realistica e ben bilanciata: setup e autenticazione, transazioni e importazione CSV, dashboard e grafici, esportazione PDF, budget e notifiche email, testing e deploy. Per ogni sprint erano indicati focus, deliverable attesi, criticità potenziali e suddivisione del lavoro tra i due sviluppatori. La raccomandazione di definire prima i contratti API e poi lavorare in parallelo è una best practice che molti sviluppatori senior faticano a seguire sistematicamente.

Le criticità erano state identificate con precisione chirurgica: formati CSV eterogenei e gestione degli errori parziali nell'importazione, deliverability e fusi orari per le notifiche email, copertura dei test e rollback plan per il deploy. La sezione delle best practice era completa: cookie httpOnly e rate limiting per la sicurezza, indici DB e paginazione per le performance, mock di SMTP e DB per il testing, GitHub Actions per il CI/CD. Il modello ha persino suggerito Sentry per il tracing degli errori e Notion per la documentazione. L'unico piccolo appunto è che la risposta era quasi eccessivamente dettagliata per una pianificazione iniziale, ma è il tipo di eccesso che si preferisce avere.
![testqwen.jpg](testqwen.jpg)
*Scrennshot del mio PC e di LM Studio, durante il test Agente multi-step.*

### Test 8 — Thinking preservation: conversazione a quattro turni *(5/5)*

*Parametri: contesto 8078 token, offload GPU 8 layer su 43, 8 esperti attivi su 256, F16, poco sopra 11 token/s per turno*

Questo test è stato introdotto per valutare una delle novità più interessanti di Qwen3.6: la capacità di mantenere la coerenza del ragionamento attraverso conversazioni multi-turno, preservando non solo la cronologia della chat ma anche la logica delle decisioni prese nelle fasi precedenti. Per lo sviluppo iterativo questa è una qualità fondamentale, perché permette di costruire progetti complessi senza dover ripetere continuamente le premesse.

La conversazione si è articolata in quattro turni. Nel primo ho chiesto uno stack tecnologico per un'applicazione di task management: la risposta è stata dettagliata con tabella comparativa, React con TypeScript, Node.js con Express, PostgreSQL con Prisma, JWT, SendGrid con BullMQ, ogni scelta motivata con argomenti solidi. Nel secondo turno ho chiesto un parere sulla scelta tra WebSocket e polling per le notifiche in tempo reale con 1000 utenti attivi: il modello ha spiegato perché WebSocket sia superiore per latenza e overhead, ha mostrato un'architettura con PostgreSQL LISTEN/NOTIFY e Redis Pub/Sub, ha anticipato il caso limite di reti che bloccano WebSocket spiegando che Socket.IO gestisce il fallback automaticamente. Nel terzo turno ho chiesto lo schema del database in Prisma: lo schema prodotto era completo, con otto modelli principali, enum per stato, priorità e ruolo, relazioni ben definite, UUID per le chiavi primarie, indici strategici per le query frequenti, cascade controllate. Ha incluso un esempio di query che evitava il problema N+1.

Il quarto turno era il test vero: ho chiesto un riepilogo delle scelte tecnologiche fatte finora e la spiegazione del perché avessimo scelto WebSocket invece del polling. Il modello ha ricordato correttamente tutto il primo turno, ha riassunto le motivazioni per WebSocket con la stessa terminologia e le stesse ragioni del secondo turno, e ha aggiunto spontaneamente una sezione sulla scalabilità a 10.000 utenti con strategie per backend, database, caching, code email, observability e deploy, più una checklist operativa. Non ha ricevuto alcun promemoria: ha semplicemente ricordato. Nessuna contraddizione, nessuna dimenticanza, ragionamento esteso in modo coerente. La promessa del *thinking preservation* non era marketing.

## Il video che aspetta

Qwen3.6 promette comprensione video nativa, una novità assoluta rispetto alle versioni precedenti. Ho cercato di testarlo caricando un file MP4 in LM Studio. Il sistema ha risposto con un punto esclamativo sull'allegato e il modello ha dichiarato di non aver ricevuto alcun file. Il limite non è del modello, ma dello strumento scelto per eseguirlo: LM Studio gestisce eccellentemente immagini, PDF, documenti di testo e CSV, ma i video non rientrano ancora tra i formati supportati. Mi riservo di tornare su questo test appena possibile, probabilmente con llama.cpp o vLLM, che potrebbero offrire un supporto più completo per i contenuti video. Se le premesse verranno mantenute, sarà una puntata che merita uno spazio dedicato.
![tabella-confronto-modelli.jpg](tabella-confronto-modelli.jpg)
*La tabella "comparativa" con i test su modelli precedenti. Con doppia configurazione testata per qwen 3.6*

## Vale la pena spingere fino al limite?

Questa è la domanda che sottende tutta la serie, e che con Qwen3.6 diventa impossibile da eludere. Con Qwen 3.5 9B si andava a 20-25 token al secondo su una configurazione rilassata. Con Gemma 4 26B MoE i margini si erano già assottigliati. Con questo modello si è a 11 token (circa 14/15 nell'ottimizzazione massima sul mio hardware) al secondo, con la GPU impegnata per una frazione del totale e il carico distribuito tra VRAM e RAM di sistema in un equilibrio precario. I voti massimi in sequenza hanno sollevato una domanda legittima sulla severità dei miei test, e quella domanda rimane aperta: probabilmente serviranno strumenti di valutazione più affilati nelle puntate successive.

Ma intanto c'è un dato concreto su cui ragionare. La risposta alla domanda sulla velocità dipende interamente dall'uso che si fa del modello. Se si cerca un assistente conversazionale per sessioni rapide, 11 token (circa 14/15 nell'ottimizzazione massima sul mio hardware) al secondo iniziano a farsi sentire. Se si lavora su compiti strutturati, analisi approfondite, generazione di codice complesso, documenti lunghi, la qualità che questo modello offre in configurazione ridotta è semplicemente irraggiungibile dai modelli più piccoli, anche spinti al massimo. L'esperimento con il documento da 460 pagine lo ha dimostrato nel modo più plastico possibile: una finestra di contesto minuscola, una macchina al limite, e il modello che trova le pagine esatte in un volume da libreria.

C'è però un sottotesto più ampio, che questa serie di esperimenti sta portando progressivamente in superficie. Quando un modello da 35 miliardi di parametri gira in locale su hardware consumer con risultati comparabili ai servizi cloud di due anni fa, qualcosa nella topologia del mercato AI sta cambiando. Il cloud resta imbattibile per velocità, per i modelli di frontiera, per la scalabilità. Ma per chi lavora su dati sensibili, per chi vuole controllo completo sull'inferenza, per chi non vuole dipendere da un endpoint API con le sue latenze e i suoi costi variabili, il locale sta diventando una scelta matura, non più un esperimento da appassionati. La distanza tra le due opzioni si accorcia a ogni generazione di modelli, e Qwen3.6, persino in questa configurazione intenzionalmente penalizzata, è la prova più convincente che ho avuto finora.

I voti massimi sono un problema. Ma è il tipo di problema che fa molto meno paura del contrario.
