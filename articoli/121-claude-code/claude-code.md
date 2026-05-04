---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-04
author: "Dario Ferrero"
youtube_url: "https://youtu.be/SvxRfdNTHWs?si=NAEiTFjnAhNkCpt2"
---

# Dentro Claude Code: conta il sistema, non il modello
![claude-code.jpg](claude-code.jpg)

*C'è un momento preciso in cui un assistente smette di rispondere e comincia ad agire. Non è una questione di intelligenza, almeno non solo: è una questione di architettura. I chatbot classici funzionano come jukebox sofisticati, ricevono una richiesta e restituiscono un output. Gli agenti di coding come Claude Code fanno qualcosa di fondamentalmente diverso: aprono file, eseguono comandi, leggono l'output, correggono gli errori e ripetono, tutto da soli, finché il compito non è finito o qualcuno li ferma. Questo salto dall'autocompletamento all'autonomia non è cosmético. Richiede un'infrastruttura che i chatbot non hanno mai avuto bisogno di costruire.*

È esattamente il tema al centro di [*Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*](https://arxiv.org/html/2604.14228v1), un [tech report](https://github.com/VILA-Lab/Dive-into-Claude-Code) pubblicato ad aprile 2026 da ricercatori della Mohamed bin Zayed University of Artificial Intelligence e dell'University College London. Il lavoro non è una valutazione di prodotto, né un benchmark: è un'analisi architettonica condotta leggendo direttamente il codice TypeScript pubblico di Claude Code, nella versione v2.1.88, confrontandolo con OpenClaw, un sistema agente open-source con obiettivi simili ma scelte progettuali molto diverse. Il risultato è qualcosa di raro nel panorama della letteratura sull'AI: una mappa ragionata di come si costruisce davvero un agente autonomo, e perché certe scelte costano care.

Un avvertimento necessario, che gli autori stessi dichiarano: si tratta di un'analisi della codebase pubblica, non di uno studio causale sulle performance in produzione. Alcune conclusioni sono inferenze architetturali più che prove sperimentali. L'architettura, però, è la cosa più rivelatrice che esista, perché le scelte di progetto incorporano valori, e i valori si leggono nel codice meglio che in qualsiasi comunicato stampa.

## Il codice attorno al loop

Il cuore tecnico di Claude Code è disarmante nella sua semplicità: un ciclo *while-true* che chiama il modello, esegue gli strumenti, raccoglie i risultati e ricomincia. Lo stesso schema di base lo trovi in qualsiasi tutorial introduttivo sugli agenti LLM. Non è lì che risiede il vantaggio competitivo. La cosa interessante, quella che il paper mette sistematicamente a fuoco, è tutto il codice che sta *attorno* a questo loop.

È un po' come guardare un motore di Formula 1: tecnicamente è un propulsore a combustione interna come quello della tua auto, ma il vero vantaggio della Ferrari sul giro di qualifica non sta nel ciclo Otto, sta nel sistema di gestione termica, nel cambio elettroattuato, nella simulazione aerodinamica che ha deciso l'angolo degli alettoni.

C'è un numero che vale più di qualsiasi slide aziendale: secondo l'analisi della codebase, soltanto l'1,6% del codice di Claude Code è logica decisionale AI in senso stretto. Il 98,4% restante è infrastruttura operativa, gestione del contesto, routing degli strumenti, pipeline di recupero. Il modello, quello che i comunicati stampa mettono sempre in copertina, occupa meno di due righe su cento. Il resto è l'impalcatura che lo rende utile nel mondo reale.

Allo stesso modo, in Claude Code, la ricerca mostra che la complessità effettiva è distribuita su cinque macro-componenti: un sistema di permessi, una pipeline di compressione del contesto, quattro meccanismi di estensibilità, un sistema di delega a subagenti, e un archivio di sessione con struttura append-oriented. Nessuno di questi è il "modello AI". Tutti determinano se il modello AI riesce a fare qualcosa di utile nel mondo reale.

Questo spostamento del peso architetturale dal modello all'infrastruttura circostante è la tesi centrale del paper, e ha implicazioni che vanno ben oltre Claude Code: suggerisce che il prossimo campo di battaglia nella guerra tra agenti non sarà tanto la qualità del modello di base, quanto la solidità del sistema che lo contiene, lo vincola e lo abilita.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta dal repository github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Nega prima, chiedi dopo

Il sistema di permessi di Claude Code è costruito attorno a un principio che nella sicurezza informatica si chiama *deny by default*: l'agente non può fare nulla a meno che qualcosa lo autorizzi esplicitamente. Nella pratica, questo si traduce in sette modalità operative che vanno dal "chiedi conferma per ogni azione" al "procedi in autonomia dentro un perimetro predefinito". La scelta della modalità attiva non è statica: dipende dal contesto, dalla sessione, dalla natura dello strumento che sta per essere invocato.

Quello che rende il sistema particolarmente interessante è la presenza di un classificatore basato su machine learning, chiamato nel codice *auto-mode classifier*. Il suo compito è decidere, per ogni azione richiesta dall'agente, se l'operazione rientra nella categoria "sicura per procedere in autonomia" o se richiede l'approvazione esplicita dell'utente. La logica sottostante è raffinata: invece di bombardare l'utente di richieste di conferma per ogni lettura di file (il cosiddetto *prompt fatigue*, l'assuefazione da sovraccarico di notifiche che porta le persone a cliccare "sì" su tutto), il sistema cerca di collocare il controllo umano solo nei punti davvero critici.

Il vantaggio è evidente: un agente che chiede permesso per ogni micro-azione diventa inutilizzabile. Ma il rischio speculare è altrettanto reale: un classificatore ML che decide cosa è "sicuro" introduce una superficie d'attacco sottile, quella delle azioni che il classificatore non riconosce come pericolose pur essendolo. Il paper lo segnala esplicitamente come una delle tensioni architetturali aperte, quella tra sicurezza e autonomia operativa, che non ha una soluzione definitiva ma solo calibrazioni continue. La pipeline di autorizzazione aggiunge ulteriori livelli: pre-filtering, hook *PreToolUse*, valutazione delle regole e permission handler, in sequenza. È un sistema a strati, non monolitico, il che lo rende estendibile ma anche complesso da ragionare nella sua interezza.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta dal repository github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## La memoria che dimentica

Se c'è un problema che ogni sviluppatore che ha usato un agente LLM su task complessi conosce bene, è questo: a un certo punto, nel bel mezzo di un lavoro lungo, l'agente comincia a sembrare confuso. Perde il filo. Ripete azioni già fatte. Prende decisioni che contraddicono quelle precedenti. Non è un problema di intelligenza: è un problema di contesto. I modelli linguistici hanno una finestra di contesto finita, una memoria di lavoro che si riempie, e quando si riempie bisogna fare scelte su cosa tenere e cosa scartare.

La soluzione di Claude Code è una pipeline di compressione del contesto articolata in cinque stadi, che nel paper vengono denominati budget reduction, snip, microcompact, context collapse e auto-compact. Ogni stadio corrisponde a una strategia diversa di riduzione: dal semplice troncamento di sezioni meno rilevanti alla sintesi attiva di parti della conversazione tramite il modello stesso. Il meccanismo finale, auto-compact, interviene automaticamente quando il contesto si avvicina al limite massimo, producendo un riassunto compresso dell'intera sessione che viene poi usato come punto di partenza per continuare.

Il trade-off qui è reale e non eliminabile: ogni compressione è una perdita. Un riassunto è per definizione meno informativo dell'originale, e la coerenza su task molto lunghi, quelli che durano ore o giorni e toccano molte parti di una codebase, soffre inevitabilmente. È il problema del *telefono senza fili* applicato all'AI: ogni passaggio di compressione introduce un margine di distorsione. Il paper identifica la gestione della memoria come una delle sei direzioni aperte per i sistemi agente del futuro, perché nessuno ha ancora trovato una soluzione soddisfacente che non sacrifichi o efficienza o coerenza.

## Estendere senza esplodere

Una delle domande di design più spinose per qualsiasi piattaforma è: come si aggiunge funzionalità senza rendere il sistema ingestibile? Claude Code risponde con quattro meccanismi distinti di estensibilità: i server MCP (Model Context Protocol), i plugin, le skill e gli hook. Non è una ridondanza, ciascuno serve uno scopo specifico nell'architettura.

Gli MCP sono il meccanismo più ampio: permettono di collegare Claude Code a servizi esterni attraverso un protocollo standardizzato, che Anthropic ha progettato come standard aperto per l'ecosistema. I plugin modificano il comportamento dell'agente aggiungendo nuovi strumenti al suo repertorio. Le skill sono istruzioni strutturate che guidano l'agente nell'esecuzione di procedure complesse. Gli hook sono il meccanismo più chirurgico: pezzi di codice che si inseriscono in punti precisi del ciclo di esecuzione (pre-azione, post-azione) per monitorare, trasformare o bloccare le operazioni. Il paper descrive il *tool pool assembly*, ovvero il processo con cui Claude Code decide quali strumenti rendere disponibili all'agente in ogni sessione, come un momento critico in cui questi quattro meccanismi si integrano.

Quattro meccanismi invece di uno non è un caso di over-engineering: riflette una scelta consapevole di separare le preoccupazioni. Un hook non fa la stessa cosa di un plugin, e confonderli produrrebbe un sistema più semplice in apparenza ma più fragile in pratica. Il rischio, però, è la complessità combinatoria: ogni meccanismo interagisce con gli altri, e la superficie d'attacco cresce con ogni estensione aggiunta. Qui il confine tra "strumento potente" e "vettore di iniezione" può diventare sottile.
![grafico3.jpg](grafico3.jpg)
[Immagine tratta dal repository github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Squadre di agenti, isole di contesto

Quando un task è troppo grande per un singolo agente, Claude Code può delegarlo a subagenti. Il meccanismo si chiama semplicemente *Agent Tool* nel codice, ed è uno dei punti più potenti dell'architettura. L'idea: l'agente principale scompone il problema, affida sotto-problemi a istanze separate del modello, raccoglie i risultati e li sintetizza. In pratica, è come gestire un team: il project manager non fa tutto da solo, coordina specialisti.

Ogni subagente opera in isolamento, con il proprio contesto e, opzionalmente, il proprio *worktree* Git separato. Questo isolamento è sia un punto di forza sia una debolezza. Da un lato, previene interferenze: due subagenti che lavorano su moduli diversi dello stesso progetto non si pestano i piedi. Dall'altro, produce quello che il paper chiama *frammentazione del contesto*: i subagenti non condividono automaticamente quello che sanno, e ricucire la conoscenza distribuita richiede un overhead di coordinamento esplicito. Se un subagente ha scoperto qualcosa di importante nel modulo A, il subagente che lavora sul modulo B non lo sa a meno che l'agente orchestratore non lo trasmetta esplicitamente.

Le trascrizioni dei subagenti, chiamate *sidechain transcripts*, vengono conservate separatamente dalla trascrizione principale della sessione. È una scelta coerente con il principio architetturale generale del sistema: tutto è append-oriented, tutto è verificabile, niente viene cancellato. Ma aggiunge complessità alla gestione della sessione, e pone domande ancora aperte su come un sistema futuro potrebbe permettere ai subagenti di condividere conoscenza in modo più fluido senza compromettere l'isolamento che li rende affidabili.

## OpenClaw allo specchio

Il confronto con OpenClaw è la parte più istruttiva del paper per chi vuole capire non Claude Code in sé, ma i principi generali del design degli agenti. OpenClaw è un sistema open-source orientato all'assistenza personale multi-canale: può ricevere messaggi da Slack, Discord, altri canali di messaggistica, e orchestrare team di agenti configurati tramite semplici file Markdown. Stessa categoria di problema, scelte architetturali molto diverse.

La differenza più rivelante riguarda il modello di fiducia e sicurezza. Claude Code adotta una valutazione per-azione: ogni strumento, ogni operazione, passa attraverso la pipeline di autorizzazione. OpenClaw sposta il controllo al perimetro del sistema: l'accesso viene verificato all'ingresso, nel gateway, e una volta dentro gli agenti operano con maggiore libertà. Nessuno dei due approcci è sbagliato in assoluto: il primo è più granulare e adatto a un contesto in cui ogni azione può avere effetti diretti sul filesystem dell'utente, il secondo è più adatto a un gateway che deve gestire molti agenti in parallelo senza diventare un collo di bottiglia di autorizzazioni.

Sulla gestione del contesto, la differenza è altrettanto netta. Claude Code ottimizza la finestra di contesto individuale, con la pipeline di compaction descritta sopra. OpenClaw preferisce la registrazione centralizzata delle capacità a livello di gateway, dove gli strumenti disponibili sono noti globalmente e non devono essere ripassati in ogni singola sessione. La memoria persistente di OpenClaw, strutturata in quattro strati (sessione, giornaliera, a lungo termine e condivisa), risponde allo stesso problema della compaction di Claude Code ma con una filosofia opposta: invece di comprimere e dimenticare, archivia e accumula. Entrambi pagano un prezzo: Claude Code rischia la perdita di coerenza su task lunghi, OpenClaw rischia la proliferazione incontrollata di memoria stantia.

Quello che emerge dal confronto non è una classifica, ma una lezione di progetto: le stesse domande architetturali fondamentali (dove mettere la sicurezza, come gestire il contesto, come organizzare la delega) producono risposte diverse a seconda del contesto di deployment, dei requisiti di sicurezza, e delle assunzioni sugli utenti. Non esiste un'architettura universalmente corretta per gli agenti AI. Esistono trade-off che vanno dichiarati.
![grafico4.jpg](grafico4.jpg)
[Immagine tratta dal repository github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Ingegneria di sistema, non prompt

C'è una frase nel paper che vale come sintesi dell'intero lavoro: il vero vantaggio competitivo degli agenti non sta solo nel modello, ma nell'infrastruttura che lo circonda. Detto altrimenti: il *prompt engineering*, l'arte di convincere un LLM a fare cose attraverso formulazioni ingegnose, sta diventando una competenza sempre meno sufficiente. Quello che conta davvero, per chi costruisce agenti che devono funzionare in produzione, su task complessi, in ambienti ostili o semplicemente imprevedibili, è il *systems engineering*: controllo degli accessi, gestione del contesto, delega sicura, persistenza verificabile.

Questo cambia il profilo della competenza richiesta. Un agente di coding non è un prodotto AI in senso stretto: è un sistema software che usa un componente AI come motore di ragionamento, ma la cui qualità dipende dalla qualità dell'intera architettura. È più vicino a un sistema operativo embedded che a un chatbot sofisticato.

Le direzioni aperte che il paper identifica sono sei: colmare il divario tra osservabilità e valutazione (oggi è difficile capire perché un agente ha fallito silenziosamente), costruire persistenza cross-sessione autentica, fare evolvere i confini del *harness* (il perimetro entro cui l'agente opera), scalare l'orizzonte di pianificazione, affrontare la governance degli agenti autonomi a scala, e rispondere alla domanda più scomoda: gli agenti attuali amplificano le capacità umane a breve termine, ma contribuiscono alla crescita delle competenze umane a lungo termine, o le erodono?

Quest'ultima domanda non è retorica. Un sistema che automatizza troppo bene rischia di rendere superflua la comprensione profonda che rende possibile l'automazione stessa. È la sindrome del pilota automatico applicata al software: più diventa bravo, meno il pilota ricorda come volare. Il paper la chiama "long-term capability preservation" e la lascia, onestamente, come questione aperta.

Il merito principale di questo lavoro è metodologico: dimostrare che si può fare archeologia architettonica su un sistema di produzione leggendo il codice pubblico, e che questa archeologia produce insight genuini sul futuro del settore. I limiti sono quelli dichiarati: nessun benchmark causale, nessuna validazione empirica delle performance, e un'analisi legata a uno snapshot preciso del codice, la versione v2.1.88, che potrebbe già essere cambiata. Ma la struttura concettuale che emerge, la mappa dei trade-off tra sicurezza e autonomia, tra memoria e coerenza, tra estensibilità e complessità, è abbastanza stabile da durare più di un aggiornamento di versione.
