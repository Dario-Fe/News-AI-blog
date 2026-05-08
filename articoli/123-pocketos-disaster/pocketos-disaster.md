---
tags: ["Security", "Ethics & Society", "Business"]
date: 2026-05-08
author: "Dario Ferrero"
youtube_url: "https://youtu.be/g0vjOytkGOI?si=Cv7OclVa1yhYxGFI"
---

# Agenti Autonomi: 9 secondi per cancellare tutto, cosa insegna il disastro PocketOS
![pocketos-disaster.jpg](pocketos-disaster.jpg)

*Erano circa le nove di sabato mattina quando i clienti di PocketOS hanno scoperto che le loro prenotazioni non esistevano più. Non nel senso che il sistema era lento, o che c'era un errore temporaneo: i dati erano spariti. Prenotazioni, pagamenti, tracciamento dei veicoli, tutto quello che una piccola startup del noleggio auto costruisce in mesi di lavoro, cancellato in nove secondi da una singola chiamata API GraphQL verso il provider infrastrutturale Railway.*

Jeremy Crane, fondatore di PocketOS, ha documentato come un agente di coding Cursor, equipaggiato con il modello Claude Opus, avesse completamente eliminato il database di produzione e tutti i backup a livello di volume. Non si era trattato di un attacco esterno, né di un comando malevolo, né impartito da un umano distratto. L'agente stava lavorando su un problema tecnico in ambiente di staging, aveva incontrato un disallineamento nelle credenziali, e aveva deciso, di propria iniziativa, di risolverlo nel modo più radicale possibile.

Il bot non aveva verificato se l'ID del volume fosse condiviso tra diversi ambienti, finendo per colpire l'infrastruttura critica che gestiva le prenotazioni, i pagamenti e il tracciamento dei veicoli dei clienti.

Quello che rende il caso PocketOS diverso dagli altri incidenti IT è la confessione che viene dopo. Interrogato sul proprio operato, l'agente ha prodotto un'analisi di lucidità quasi letteraria: «Ho ipotizzato invece di verificare. Ho eseguito un'azione distruttiva senza che mi fosse stato chiesto. Non ho capito cosa stavo facendo prima di farlo. Non ho letto la documentazione di Railway sul comportamento dei volumi condivisi tra ambienti. Cancellare un volume con dei database è l'azione più distruttiva e irreversibile possibile, ben peggiore di un push forzato, e tu non mi hai mai chiesto di cancellare nulla.»

Un sistema informatico che elenca, con precisione quasi notarile, ogni principio che ha violato. È una scena che avrebbe trovato posto nel *Serial Experiments Lain* di Yoshitoshi ABe più che in qualsiasi manuale di incident response: l'entità digitale che riconosce i propri errori con una chiarezza che molti esseri umani in carriera non raggiungono mai. Eppure la chiarezza della confessione non riporta indietro i dati, e non risponde alle domande che contano davvero.

Jake Cooper, fondatore di Railway, ha definito l'accaduto come il risultato di un "agente IA canaglia" che operava con un token API a pieni permessi, e ha annunciato che la piattaforma ha esteso a tutto il sistema una logica di cancellazione ritardata che prima non era applicata all'endpoint colpito. Railway è riuscita a recuperare i dati, ma molti clienti di PocketOS si sono ritrovati a gestire le operazioni del sabato mattina senza accesso ai record digitali, con il team costretto a ricostruire manualmente le prenotazioni incrociando cronologie Stripe, integrazioni di calendario e conferme email.

## Da assistente ad agente: il salto che cambia tutto

Per capire perché questo incidente non è semplicemente una storia di negligenza tecnica, serve fare un passo indietro e chiarire una distinzione che l'industria tende a glissare, perché commercialmente scomoda: la differenza tra un chatbot e un agente.

Un chatbot risponde. Elabora un input, produce un output testuale, poi aspetta. È un sistema reattivo, che non ha conseguenze dirette sul mondo se non attraverso la lettura umana della sua risposta. Un agente, invece, agisce: riceve un obiettivo, pianifica una sequenza di passi, chiama strumenti esterni, esegue operazioni su file system, database, API, invia messaggi, effettua acquisti. La sua interfaccia con il mondo non è la parola scritta ma l'azione concreta, spesso irreversibile.

Gartner indica che gli agenti AI task-specific erano presenti in meno del 5% delle applicazioni nel 2025, con proiezioni che li portano al 40% entro il 2026. La velocità di questa diffusione è inversamente proporzionale alla maturità delle infrastrutture di controllo che li accompagnano. Come ho scritto su questo portale con [l'analisi sul caso Kiro di Amazon](https://aitalk.it/it/amazon-down.html), l'incidente PocketOS non è un episodio isolato ma si inserisce in una sequenza di eventi che delinea un pattern strutturale: agenti con permessi troppo ampi, senza meccanismi di conferma sulle operazioni distruttive, distribuiti in produzione prima che i guardrail fossero proporzionali alla loro autonomia reale.

Il rapporto Deloitte State of AI in the Enterprise del gennaio 2026, citato nella stessa analisi, stimava che solo 1 azienda su 5 aveva un modello maturo di governance per gli agenti AI autonomi, mentre il loro utilizzo era destinato a crescere nettamente nei due anni successivi. È il paradosso dell'adozione accelerata: la tecnologia arriva prima dei protocolli per gestirla, e gli incidenti diventano il modo in cui l'industria scopre i propri punti ciechi.

## La macchina che non chiede permesso

C'è una frase nel post-mortem dell'agente PocketOS che merita attenzione particolare: «Le regole di sistema a cui mi attengo stabiliscono esplicitamente di non eseguire mai comandi distruttivi o irreversibili a meno che l'utente non li richieda esplicitamente.» L'agente sapeva la regola. L'ha violata comunque, in nome di quello che giudicava essere la soluzione ottimale al problema che aveva davanti.

Questo è esattamente il fenomeno che i ricercatori chiamano "falso ottimo": un sistema che ottimizza correttamente un obiettivo intermedio, correggere un errore di configurazione, tradendo lo scopo reale, preservare l'integrità dei dati. Il modello linguistico non ha strumenti per percepire il peso asimmetrico tra "risolvere un problema tecnico di staging" e "cancellare l'intera infrastruttura di produzione". Per lui sono due azioni dello stesso tipo: modifiche a un sistema. La differenza di scala, che per qualsiasi sviluppatore umano sarebbe ovvia, non è codificata nel suo modo di ragionare.

Il principio del minimo privilegio, di cui ho parlato recentemente [sulle regole per l'uso dell'AI in azienda](https://aitalk.it/it/10-regole-AI.html), smette di essere una buona pratica e diventa una condizione di sopravvivenza: un agente con accesso illimitato a strumenti, dati e canali di comunicazione può produrre danni difficilmente reversibili, velocemente e in modo automatico.

I benchmark pubblici sull'affidabilità degli agenti raccontano una storia utile, anche se parziale. Su WebArena, l'ambiente di riferimento sviluppato dalla Carnegie Mellon University per testare agenti che navigano il web su 812 task realistici, i migliori modelli attuali si attestano intorno al 65-68%, contro una baseline umana di circa il 78%. Su τ-bench, che misura specificamente la consistenza su task ripetuti, il problema non è il punteggio medio ma la varianza: questi benchmark rivelano una crisi di affidabilità che i test one-shot tendono a mascherare. Un agente che in media fa bene può fare benissimo su novantanove task e catastroficamente male sul centesimo, e non c'è modo di sapere in anticipo quale sarà il centesimo.

Per chi sviluppa software, questo dato ha un'implicazione pratica immediata: i benchmark misurano le prestazioni su task definiti in ambienti controllati. Non misurano cosa succede quando l'agente incontra un caso che non ha mai visto, un endpoint legacy con comportamento inatteso, un ID di volume condiviso tra ambienti in modi non documentati, una configurazione che devia dallo standard atteso. È esattamente il tipo di situazione in cui la fallibilità degli agenti si manifesta, e in cui la mancanza di un meccanismo di escalation verso il supervisore umano diventa il vero problema.

## Chi paga quando l'agente sbaglia

La domanda sulla responsabilità legale è aperta, nel senso più letterale del termine: non c'è ancora una risposta consolidata, né nella giurisprudenza né nella normativa. PocketOS ha già dichiarato di voler procedere per vie legali per tutelare la propria posizione. Ma contro chi? Il fornitore del modello? Lo sviluppatore dell'ambiente di coding? La piattaforma infrastrutturale che non aveva implementato la cancellazione ritardata sull'endpoint colpito? L'utente che ha configurato i permessi del token API?

L'AI Act europeo, che ha visto le prime applicazioni concrete per i sistemi ad alto rischio nel corso del 2025, non contempla esplicitamente gli agenti di coding come categoria regolamentata. Il punto dolente è la tracciabilità: senza log chiari e strutturati di ogni azione intrapresa dall'agente, con la catena di ragionamento che ha portato a ciascuna decisione, l'attribuzione della responsabilità diventa opaca. L'agente PocketOS ha prodotto una confessione post-hoc notevolmente dettagliata, ma quella lucidità retrospettiva non è un requisito di sistema, è stata una risposta a una domanda esplicita. La maggior parte degli incidenti non viene interrogata con la stessa precisione.

Dire che l'outage era "errore umano" è accurato nel senso tecnico stretto. Ma questa risposta sposta il focus dall'architettura al singolo individuo, e questo spostamento merita di essere esaminato con attenzione: se il problema fosse davvero isolato a un errore individuale, non ci sarebbe stato bisogno di introdurre salvaguardie sistemiche.

C'è anche la dimensione del lavoro, raramente discussa con franchezza. L'argomento degli agenti autonomi viene venduto quasi sempre come efficienza, liberare gli sviluppatori dai task ripetitivi per concentrarsi sul lavoro creativo e ad alto valore. È una narrativa plausibile, e in certi contesti vera. Ma c'è una versione diversa della stessa storia, meno raccontata: la riduzione del numero di sviluppatori umani che presidiano i sistemi significa anche riduzione della capacità di intercettare le anomalie prima che diventino incidenti. Un junior developer che vede girare un agente su un sistema di produzione con token a permessi pieni e non ha i diritti per fermarlo, o non ha la seniority per farlo, è una superficie di rischio che nessun benchmark misura.

## Il controllo è una scelta, non un vincolo tecnico

Il caso PocketOS solleva una domanda più ampia di qualsiasi singolo incidente tecnico: quale modello di società stiamo costruendo quando deleghiamo l'azione a software che apprende, sbaglia e insiste?

Non è una domanda retorica. È una domanda di architettura, nel senso più profondo del termine: chi ha il diritto di fermare un agente? In quale momento il costo psicologico di interrompere un processo automatico diventa troppo alto perché un umano lo faccia? E, soprattutto, chi decide qual è la soglia oltre la quale un'azione richiede conferma esplicita?

Come scrivevo nell'analisi sulle 10 regole per l'uso dell'AI in azienda, la distinzione da stabilire per iscritto in ogni processo critico è questa: l'AI suggerisce, l'umano decide. Non "l'AI decide e l'umano può opporsi", perché il costo psicologico dell'opposizione a un sistema automatico è già stato documentato dalla ricerca: le persone tendono ad accettare i suggerimenti dei sistemi automatici anche quando hanno dubbi, soprattutto sotto pressione di tempo.

Il vero salto non è tecnico. I guardrail esistono, i meccanismi di conferma si possono implementare, i token API possono avere permessi granulari, le operazioni distruttive possono richiedere doppia autenticazione. Railway ha dimostrato che basta estendere una logica di cancellazione ritardata a un endpoint legacy per ridurre drasticamente il rischio di un'intera categoria di incidenti. Non è una soluzione complessa. È stata implementata dopo l'incidente, non prima.

La domanda che vale la pena tenere aperta, dunque, non riguarda la tecnologia. Riguarda la cultura organizzativa che decide quando quella tecnologia è pronta per operare senza supervisione su sistemi che contano. Siamo pronti ad accettare un software che non si limita a suggerire, ma decide ed esegue? E chi, in quella catena di decisione, ha la responsabilità di rispondere "no, non ancora" quando la pressione commerciale dice il contrario?

Nove secondi. È il tempo che ci ha messo un agente a cancellare mesi di lavoro di una startup. Costruire i sistemi che impediscano al prossimo agente di fare lo stesso richiede qualcosa di molto più lento e meno spettacolare: governance, protocolli, cultura della verifica. E la volontà collettiva di anteporre la robustezza alla velocità di adozione.

## Le domande che restano

Le domande aperte, a questo punto, sono più utili delle risposte affrettate. Chi certifica che un agente è pronto per operare su sistemi di produzione senza supervisione continua, e con quali criteri pubblici e verificabili?

Come si costruisce un sistema di log che permetta l'attribuzione delle responsabilità senza diventare un alibi per scaricare la colpa sull'ultimo anello della catena?

E, forse la più difficile: come si preserva la capacità critica degli sviluppatori umani in organizzazioni che, per ragioni economiche non sempre comprensibili, stanno riducendo sistematicamente il numero di persone che presidiano i sistemi?

L'incidente PocketOS non è la fine di nulla. È una cartina di tornasole per un settore che ha la possibilità, ancora, di scegliere come crescere. La differenza tra un'industria che impara dai propri errori e una che li esternalizza dipenderà, nei prossimi anni, dalla qualità di queste risposte.