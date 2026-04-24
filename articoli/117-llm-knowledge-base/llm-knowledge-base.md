---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-04-24
author: "Dario Ferrero"
youtube_url: "https://youtu.be/TghyBXWlVBI?si=Nq1AYm_RRhMDHeLc"
---

# La memoria che impara: Karpathy sfida il RAG con una knowledge base evolutiva
![llm-knowledge-base.jpg](llm-knowledge-base.jpg)

*C'è un momento che chiunque abbia lavorato intensamente con un modello linguistico conosce bene: il reset. Stai costruendo qualcosa di complesso, magari un'architettura software elaborata o una ricerca che intreccia dozzine di fonti, e il modello ha capito tutto, tiene il filo, risponde con precisione chirurgica. Poi la sessione finisce, oppure arrivi al limite di contesto, e l'AI dimentica tutto. Ricomincia da zero. Tu devi rispiegarle chi sei, cosa stai facendo, quali decisioni avete preso insieme. È come il film "Memento" di Christopher Nolan, dove il protagonista deve tatuarsi le informazioni sul corpo perché la memoria a breve termine non funziona: brutale, ridondante, e profondamente frustrante.*

Andrej Karpathy, ex direttore dell'AI a Tesla e co-fondatore di OpenAI, ora impegnato in un progetto indipendente, ha descritto questo problema esattamente in questi termini, e il 2 aprile 2026 ha [pubblicato su X](https://x.com/karpathy/status/2039805659525644595) una proposta per risolverlo. Il post è diventato virale con oltre 16 milioni di visualizzazioni, e il [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) di approfondimento ha superato le 5.000 star in pochi giorni. Non stava annunciando un nuovo modello né un benchmark. Stava descrivendo un cambiamento nel modo in cui lui stesso usa i modelli linguistici, un cambiamento che ha innescato un dibattito tecnico acceso e, come spesso accade, qualche semplificazione eccessiva.

## Cos'è il RAG, e perché è diventato il metodo dominante

Prima di capire cosa propone Karpathy, vale la pena spiegare cosa fa il RAG, perché negli ultimi tre anni è diventato l'approccio standard per dare ai modelli linguistici accesso a conoscenza esterna, e perché porta con sé alcuni problemi strutturali che non tutti nominano esplicitamente.

Retrieval-Augmented Generation significa, letteralmente, generazione aumentata dal recupero. In un sistema RAG standard, i documenti vengono tagliati in frammenti arbitrari chiamati "chunk", convertiti in vettori matematici chiamati embedding, e archiviati in un database specializzato. Quando l'utente fa una domanda, il sistema esegue una "ricerca per similarità" per trovare i frammenti più rilevanti e li inserisce nel contesto del modello.

Il meccanismo funziona, e funziona bene in molti scenari. Ma porta con sé alcune caratteristiche che in certi contesti diventano problemi. Il primo è la natura fondamentalmente stateless del sistema: ogni interrogazione riparte da zero, cercando di nuovo tra le fonti, senza che nulla si accumuli nel tempo. Non c'è memoria delle elaborazioni passate, non c'è accumulo di conoscenza. Il secondo problema riguarda la qualità del recupero: tagliare un documento in pezzi e cercare per similarità vettoriale funziona bene quando la risposta sta in uno o due frammenti contigui, ma diventa impreciso quando una domanda richiede di sintetizzare idee distribuite su decine di fonti diverse. Il terzo, spesso sottovalutato, è la complessità infrastrutturale: database vettoriali, pipeline di embedding, sistemi di indicizzazione, tutto questo ha un costo in termini di latenza, manutenzione e opacità. I vettori non sono leggibili da nessun essere umano, il che rende difficile capire perché il sistema ha recuperato certi frammenti invece di altri.

## Come funziona la macchina della memoria

La proposta di Karpathy parte da una domanda diversa: invece di cercare ogni volta, cosa succederebbe se l'AI costruisse una conoscenza strutturata in anticipo, e poi la consultasse direttamente?

Karpathy ha pubblicato su GitHub Gist la descrizione di un sistema a tre cartelle che permette a un modello di compilare e mantenere una knowledge base senza database vettoriali. L'architettura è deliberatamente semplice. La prima cartella, `raw/`, contiene il materiale grezzo: PDF, note, articoli web, repository GitHub, dataset. La seconda, `wiki/`, ospita gli articoli compilati dal modello, uno per concetto o argomento. La terza è un file `index.md`, una mappa complessiva di tutti gli articoli, dimensionata per stare all'interno della finestra di contesto del modello.

Karpathy usa l'Obsidian Web Clipper per convertire i contenuti web in file Markdown, assicurandosi che anche le immagini vengano salvate localmente in modo che il modello possa referenziarle attraverso le sue capacità di visione.

Il passaggio centrale, quello che differenzia l'approccio da un semplice archivio, è la compilazione. Invece di indicizzare i file, il modello li "compila": legge i dati grezzi e scrive una wiki strutturata, generando sommari, identificando concetti chiave, producendo articoli in stile enciclopedico e, fondamentale, creando backlink tra idee correlate.

Il sistema non è statico: Karpathy descrive cicli periodici di "linting", in cui il modello scansiona la wiki alla ricerca di inconsistenze, dati mancanti o nuove connessioni possibili. Il sistema si comporta come una knowledge base vivente che si auto-risana. Le query che vengono eseguite sul sistema vengono archiviate nella wiki stessa, così ogni esplorazione si accumula: le risposte, i grafici, le analisi vengono inserite nella base di conoscenza, che cresce in modo cumulativo.

A che scala funziona tutto questo? Karpathy ha precisato che al momento opera con circa 100 articoli e 400.000 parole di materiale sorgente, e che a questa dimensione la capacità del modello di navigare attraverso sommari e file indice è più che sufficiente. Un'analisi condotta da MindStudio ha rilevato che questo approccio può ridurre il consumo di token fino al 95% rispetto al caricamento integrale dei documenti nel contesto, vantaggio che si riduce a confronto con pipeline RAG ottimizzate.

Il post di Karpathy si inserisce in una sequenza precisa del suo pensiero sull'interazione uomo-AI: dopo il "vibe coding" del febbraio 2025, dove l'utente accetta il codice generato senza revisionarlo riga per riga, e l'ingegneria agentiva del gennaio 2026, dove gli [umani orchestrano agenti](https://aitalk.it/it/autoresearch-karpathy.html) invece di scrivere codice direttamente, le LLM Knowledge Base rappresentano la terza fase: l'AI gestisce la conoscenza, non solo il codice. L'umano diventa curatore, non scrittore.
![postx.jpg](postx.jpg)
[Screenshot tratto dal profilo X di Andrej Karpathy](https://x.com/karpathy/status/2039805659525644595)

## Il vantaggio della leggibilità

Uno degli aspetti più concreti della proposta, e spesso quello che convince più facilmente chi viene da esperienze di RAG enterprise, riguarda la trasparenza. Trattando i file Markdown come fonte di verità, Karpathy evita il problema della "scatola nera" dei vettori embedding. Ogni affermazione del modello può essere ricondotta a un file `.md` specifico che un essere umano può leggere, modificare o eliminare.

Questa caratteristica ha implicazioni pratiche non banali. In un sistema RAG, quando il modello restituisce una risposta errata o parziale, tracciare l'origine del problema richiede di capire quali frammenti sono stati recuperati, come sono stati segmentati, e perché la ricerca per similarità ha privilegiato certi vettori rispetto ad altri. In una wiki Markdown ben strutturata, l'errore è visibile: c'è un articolo scritto male, un backlink mancante, un'informazione non aggiornata. È un problema editoriale, non un problema di algebra lineare.

L'architettura è costruita deliberatamente su Markdown come standard aperto e indipendente dagli strumenti. Se Obsidian dovesse sparire o cambiare le condizioni di licenza, la knowledge base rimarrebbe una directory di file in testo semplice che qualsiasi editor può aprire. È una forma di sovranità sui propri dati che le soluzioni enterprise tendono a non offrire.

Lex Fridman ha confermato di usare un sistema simile, aggiungendo uno strato di visualizzazione dinamica: genera HTML con JavaScript per ordinare e filtrare i dati, e costruisce mini-knowledge-base temporanee focalizzate su un tema specifico da caricare in modalità vocale durante le sue corse da 10-15 chilometri. Questo "wiki effimero" prefigura una direzione interessante: non si chatta con un'AI, si spawna un team di agenti per costruire un ambiente di ricerca personalizzato per un compito specifico, che poi si dissolve.

C'è anche un'implicazione di lungo periodo che Karpathy menziona solo di sfuggita ma che vale la pena nominare. Man mano che la wiki viene ripetutamente lintata (revisione automatizzata) e raffinata, diventa una rappresentazione sempre più pulita del dominio: deduplicata  (informazione appare una volta sola), cross-linked, scritta in stile coerente. A quel punto la knowledge base diventa un candidato come dati di training: invece di fare continuamente prompting su un grande modello generale con la wiki, un team potrebbe fare fine-tuning di un modello più piccolo su quel corpus curato, codificando la knowledge base nei pesi del modello e trasformando un archivio personale o dipartimentale in un'intelligenza specializzata privata.

## Dove il RAG resiste

La narrativa del "RAG è morto" che è circolata sui social nei giorni successivi al post di Karpathy è esattamente il tipo di semplificazione che fa danni. Il RAG non è morto, e ci sono contesti precisi in cui resta l'approccio giusto, spesso l'unico praticabile.

Il primo limite della proposta di Karpathy è esplicitato da Karpathy stesso: la scala. Quando il numero di articoli cresce oltre qualche centinaia, o le fonti superano milioni di parole, l'indice stesso diventa troppo grande per stare nella finestra di contesto, e il retrieval diventa di nuovo necessario. L'approccio è esplicitamente posizionato per uso personale e in team piccoli, non per archivi documentali a livello aziendale. Un'azienda con milioni di documenti, sistemi legacy eterogenei, requisiti di compliance stringenti e centinaia di utenti simultanei ha bisogno di qualcosa di più robusto di una directory di file Markdown.

Il secondo limite riguarda la freschezza dei dati. Il RAG è particolarmente adatto quando le fonti cambiano frequentemente e non si può permettere di "ricompilare" la conoscenza ogni volta. Un assistente per il supporto clienti che deve rispondere usando la documentazione aggiornata di un prodotto in continua evoluzione, o un sistema di analisi finanziaria che deve incorporare notizie di mercato in tempo reale, ha bisogno di recupero dinamico, non di una wiki che viene aggiornata periodicamente.

Il terzo problema, forse il più insidioso, è quello che nei commenti al GitHub Gist viene chiamato "memory drift". Con la crescita della knowledge base, come si gestisce il drift semantico, il fenomeno per cui il significato di un termine, un concetto o un'affermazione si sposta gradualmente nel tempo, a ogni riscrittura o sintesi, allontanandosi dall'intenzione originale senza che nessuno se ne accorga esplicitamente, e come si evita che le informazioni contraddittorie si accumulino? 

Ogni volta che il modello riscrive o sintetizza un articolo, c'è un rischio: se la sintesi è imprecisa, o se due fonti contradditorie vengono integrate in modo inconsistente, l'errore entra nella base e si propaga. Nel RAG, un documento sbagliato rimane isolato nel corpus e può essere corretto o rimosso. In una wiki compilata dall'AI, l'errore può essere stato riformulato e distribuito in più articoli collegati, rendendo la correzione molto più complicata.

Alcune proposte nella comunità suggeriscono di integrare il sistema con SQLite, BM25 e TREESEARCH per gestire meglio la crescita del corpus, e diversi commentatori sottolineano che gli esseri umani devono rimanere nel loop per gestire il contesto della conoscenza preparato dall'AI e prevenire derive e incoerenze.

C'è poi la questione della provenienza delle fonti. Una wiki ben formattata è trasparente nella struttura ma non necessariamente nell'origine delle affermazioni. Senza un sistema rigoroso di citazioni interne che tracci ogni claim al documento sorgente originale, si ottiene leggibilità senza verificabilità, una distinzione che in contesti regolamentati, medici o legali fa una differenza sostanziale.

## Ibrido o resa dei conti?

Come ha scritto un analista in un commento al Gist, l'LLM Wiki è essenzialmente un'implementazione manuale e tracciabile di Graph RAG: ogni claim rimanda alle fonti, le relazioni sono esplicite, la struttura è leggibile dagli umani. È un punto che chiarisce molto: i due approcci non sono opposti filosofici, sono soluzioni ingegneristiche ottimizzate per contesti diversi, e il confine tra loro è più permeabile di quanto il dibattito online suggerisca.

Alcuni team stanno già cercando di colmare il divario con architetture multi-agente: un design "Swarm Knowledge Base" scala il workflow di Karpathy a un sistema di 10 agenti orchestrati da uno strato di controllo, aggiungendo modelli supervisori per proteggere la wiki condivisa da allucinazioni che si compongono. Un modello focalizzato sulla valutazione, usato come "quality gate", valuta e valida le bozze di pagine prima che entrino nella knowledge base attiva.

Il futuro più plausibile non è la vittoria di uno dei due paradigmi sull'altro. È un'architettura stratificata dove una wiki strutturata e compilata gestisce la conoscenza di dominio stabile, aggiornata con cicli periodici supervisionati da umani, mentre il retrieval dinamico interviene per le fonti live, i dati freschi e i corpus che cambiano troppo rapidamente per essere compilati. La memoria strutturata come fondamenta, il retrieval come finestra sul mondo esterno, la revisione umana come controllo di qualità che nessun sistema automatico può ancora sostituire completamente.

Nel Gist, Karpathy annota che il suo uso dei token si è spostato dalla generazione di codice alla gestione della conoscenza strutturata, una nota apparentemente marginale che in realtà segnala un cambio di priorità nell'uso reale dei modelli avanzati.  La gestione della conoscenza sta diventando il centro di gravità del lavoro con i modelli linguistici, non la generazione di codice.

La domanda vera non è se Karpathy "batte" il RAG. È quale architettura massimizza affidabilità, aggiornabilità e valore operativo nel contesto specifico in cui opera. Per un ricercatore indipendente, un piccolo team che costruisce documentazione tecnica interna, o un knowledge worker che vuole che il proprio assistente AI smetta di avere amnesie ogni sessione, la proposta di Karpathy è concreta, implementabile oggi, e risolve un problema reale. Per un'azienda con milioni di documenti, dati che cambiano ogni ora e requisiti di governance stringenti, il RAG nella sua forma evoluta, magari arricchita da elementi della proposta di Karpathy, rimane l'unica opzione praticabile.

Per i team che stanno valutando se adottare questo approccio o investire in una pipeline RAG completa, la risposta onesta è: cominciate con questo, e spostatevi al RAG solo quando la finestra di contesto diventa un vero collo di bottiglia, non un problema ipotetico. Probabilmente rimarrete sorpresi da quanto lontano vi porta il Markdown strutturato. Non è la fine del RAG. È l'inizio di una conversazione più sofisticata su come i sistemi AI gestiscono la memoria nel tempo, una conversazione che fino a due settimane fa quasi nessuno stava facendo nel modo giusto.