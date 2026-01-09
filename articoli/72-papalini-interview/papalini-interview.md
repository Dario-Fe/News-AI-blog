---
tags: ["Business", "Ethics & Society", "Security"]
date: 2026-01-09
author: "Dario Ferrero"
youtube_url: "https://youtu.be/bqDtxxjYJss?si=Zr5JA9RjmJ5UHRep"
---

# 'Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese'. Conversazione con Enrico Papalini
![papalini-interview.jpg](papalini-interview.jpg)

*Enrico Papalini ha un curriculum che farebbe impallidire molti consulenti da LinkedIn: oltre vent'anni passati a costruire e orchestrare sistemi software dove l'errore non è un'opzione. Come Head of Software Development in Borsa Italiana, parte del gruppo Euronext, sta guidando l'adozione dell'intelligenza artificiale in un contesto dove la parola "crash" ha implicazioni che vanno ben oltre il bug di runtime. Prima ancora, ha attraversato il settore da diverse angolazioni: da startup tecnologiche a colossi finanziari, sempre nel ruolo di chi deve far funzionare le cose quando tutti gli altri possono permettersi che non funzionino.*

Il suo [profilo LinkedIn](https://www.linkedin.com/in/enricopapalini/) racconta una traiettoria professionale dove l'innovazione si è sempre dovuta sposare con l'affidabilità. Non è un accademico che teorizza dall'esterno, né un founder che può permettersi il lusso del "move fast and break things". È qualcuno che ha dovuto rispondere a domande del tipo: "Possiamo usare questa tecnologia in un sistema che processa milioni di transazioni al giorno?" La risposta giusta non è mai né un sì entusiasta né un no conservatore, ma un "dipende, e ti spiego come".

Ora Papalini ha sintetizzato questa esperienza in un libro che sta facendo discutere: [*Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*](https://amzn.to/3Z12Ng9), pubblicato anche in [versione inglese](https://www.amazon.com/dp/B0G7LPJBTH) con il titolo *Non-Deterministic Software Engineering: How to Build Reliable Software with AI Assistants Without Losing Quality, Security, or Control*. Il sottotitolo è già un manifesto: come costruire software affidabile con assistenti AI senza perdere qualità, sicurezza o controllo.

## Il patto silenzioso infranto

Mentre il mercato editoriale tech continua a sfornare manuali su "come usare ChatGPT per programmare più velocemente", Papalini ha scelto un angolo completamente diverso. Il suo libro si basa su ricerche condotte da DX su oltre 180 aziende, integra le metriche DORA (DevOps Research and Assessment) adattate allo sviluppo assistito da IA, e analizza case study di chi si è già scottato o ha trovato un equilibrio: OpenAI, Shopify, Google. Per scriverlo ha dialogato con alcuni dei nomi più pesanti dell'ingegneria del software contemporanea: Martin Fowler, il teorico dei design patterns e del refactoring; Kent Beck, l'inventore dell'Extreme Programming; Addy Osmani, engineering manager di Google Cloud.

Gli chiedo di raccontarmi cosa l'ha spinto a scrivere proprio questo libro, proprio adesso, quando tutti sembrano concentrati sulla velocità miracolosa promessa dagli assistenti AI.

"Tutti parlano di velocità, ma la vera rivoluzione è un'altra," risponde Papalini. "È un cambio di natura degli strumenti che usiamo. Per quarant'anni abbiamo dato per scontata una cosa: scrivi del codice, quello fa esattamente ciò che hai scritto. Sempre. È su questa certezza che abbiamo costruito tutto, come testiamo, come facciamo debug, come lavoriamo in team. L'IA generativa rompe questo patto silenzioso. Non perché sia difettosa, ha una natura probabilistica. Le chiedi la stessa cosa due volte, ti dà risposte diverse. A volte geniali, a volte sbagliate con una sicurezza disarmante."

La metafora che usa per inquadrare il problema è illuminante: "Le aziende che pensano di sostituire i programmatori con l'AI e guardano compiaciute a quante righe di codice in più riescono a produrre e si perdono il punto: stanno introducendo una variabile aleatoria nel cuore dei loro sistemi. È un po' come se un ingegnere civile costruisse un ponte con materiali che *potrebbero* reggere il peso previsto. Funziona benissimo quando ci passano poche auto, ma quando ci passa il primo camion crolla."

Ha scritto il libro, dice, "perché mi sembrava che mancasse una guida per chi deve navigare questo cambio senza schiantarsi, ma anche senza rinunciare ai benefici, che sono reali."

## Dal determinismo alla tolleranza

Il cuore concettuale del libro è racchiuso nel titolo inglese: *Non-Deterministic Software Engineering*. È un ossimoro deliberato. L'ingegneria del software, per definizione, è stata sempre l'arte di costruire sistemi deterministici: input A produce sempre output B. Papalini sta proponendo di accogliere nei nostri processi strumenti che, per loro natura, non rispettano questa regola fondamentale.

Gli chiedo come cambia il paradigma del controllo qualità quando passiamo da un mondo dove il codice faceva esattamente ciò che era scritto, a un mondo dove accogliamo sistemi probabilistici nei nostri IDE.

"Cambia tutto, e allo stesso tempo niente. Lo so, sembra un paradosso," esordisce. "Cambia tutto perché 'funziona' non significa più 'è corretto'. Il codice generato dall'IA compila, passa i test che hai scritto, ha un aspetto professionale. Ma potrebbe nascondere vulnerabilità, gestire male i casi limite, o essere scritto in un modo che tra sei mesi nessuno capirà. Non cambia niente perché i fondamentali dell'ingegneria del software restano gli stessi: test, review, pensiero progettuale. Anzi, diventano più importanti di prima."

La chiave, secondo Papalini, sta nell'adottare un approccio che finora è stato estraneo agli sviluppatori software: "La vera novità è che dobbiamo imparare a ragionare per 'tolleranze'. Martin Fowler usa spesso questa analogia: sua moglie è ingegnere strutturale, e non progetta mai al limite esatto. Calcola sempre un margine di sicurezza. Noi sviluppatori non abbiamo mai dovuto farlo perché i nostri 'materiali' erano perfettamente prevedibili. Ora non lo sono più. E chi non si costruisce questi margini, prima o poi vedrà crollare il 'ponte'."

È un cambio di mentalità radicale per un'intera professione che ha costruito la propria identità sulla certezza assoluta dell'esecuzione. Come dire a un orologiaio svizzero che d'ora in poi dovrà accettare che i suoi orologi possano avere un margine di errore variabile.

## L'illusione della velocità

Uno dei passaggi più controintuitivi del libro riguarda i dati sulla produttività. Papalini cita uno studio del METR (un'organizzazione indipendente che valuta le capacità dei sistemi AI) che mostra come gli sviluppatori possano sentirsi il 20% più veloci con l'intelligenza artificiale, mentre i test reali su compiti misurabili indicano che in alcuni casi sono più lenti del 19%.

Gli chiedo come sia possibile questa discrepanza percettiva, e soprattutto come le imprese possano misurare la vera produttività senza cadere nel marketing degli strumenti.

"Sai cosa mi ha colpito di più di quello studio? Non è il dato che con l'IA fossero più lenti del 19%. È che gli sviluppatori *credevano* di essere più veloci. E continuavano a crederlo anche dopo aver visto i risultati," racconta Papalini. "Perché succede? Perché l'IA riduce la fatica *percepita*. Ti senti più fluido, meno bloccato. È come avere un collega sempre disponibile a darti una mano che non ti giudica e non ti fa aspettare. Psicologicamente è potente. Ma 'mi sento produttivo' e 'sto producendo valore' sono due cose molto diverse."

La soluzione che propone non è filosofica ma metodologica: "Per non cadere nel hype, un'azienda dovrebbe stabilire una baseline *prima* di adottare gli strumenti. Senza un 'prima', non potrete mai dimostrare un 'dopo'. Quando il CEO chiederà cosa ha portato l'IA, servono numeri, non sensazioni. Ma i numeri debbono essere quelli giusti: smettetela di misurare linee di codice o quante suggestion dell'IA vengono accettate. Misurate quello che conta: funzionalità rilasciate, bug in produzione, tempo per risolvere gli incidenti. E una cosa fondamentale: misurare quanto motivati rimangono gli sviluppatori."

È un richiamo alla disciplina ingegneristica in un momento di euforia collettiva. Come nei primi giorni delle metodologie Agile, quando tutti misuravano la "velocity" in story points senza chiedersi se stessero davvero consegnando valore.

## Lunedì mattina, tre mosse

Il sottotitolo italiano del libro pone una domanda diretta: "Cosa debbono fare le imprese". Non "cosa potrebbero fare" o "cosa sarebbe bello fare", ma "cosa debbono fare". È un imperativo, e implica urgenza.

Chiedo a Papalini di essere ancora più diretto: se dovesse indicare le prime tre azioni concrete che un CTO o un CEO dovrebbe intraprendere lunedì mattina per non farsi travolgere, quali sarebbero?

"La prima è fare un audit di quello che sta *già* succedendo," risponde senza esitazione. "Te lo garantisco: i tuoi sviluppatori stanno già usando ChatGPT, Copilot, Claude, che tu lo sappia o no. Non per cattiveria, semplicemente perché questi strumenti funzionano. Prima di scrivere policy, capisci la situazione reale."

Questo fenomeno dello Shadow AI, l'uso non autorizzato di strumenti intelligenti, è uno dei temi ricorrenti nel libro. Non è un problema di indisciplina ma di necessità: quando gli strumenti ufficiali sono lenti da approvare o troppo limitati, le persone trovano alternative.

"La seconda è tracciare una linea netta tra esplorazione e produzione," continua Papalini. "Prototipazione rapida, esperimenti, proof of concept, tutto legittimo. Ma deve essere *chiaro* che quel codice non va in produzione senza una riscrittura consapevole. Il disastro classico è il prototipo del venerdì che diventa il sistema critico del lunedì perché 'tanto funziona'."

È il pattern che chiunque abbia lavorato in startup riconosce immediatamente: la demo diventa prodotto, il workaround diventa architettura, il temporaneo diventa permanente. Con l'IA questo processo si accelera pericolosamente perché generare un prototipo convincente è questione di minuti.

"La terza è investire nella capacità di review, non in quella di generazione," conclude. "Il collo di bottiglia non è più scrivere codice, è capirlo, validarlo, mantenerlo. Se i tuoi sviluppatori possono generare dieci volte più codice ma la capacità di review resta uguale, stai solo accumulando debito tecnico più in fretta."

## La trappola del funziona

Andrej Karpathy, uno dei pionieri dell'AI moderno ed ex direttore dell'intelligenza artificiale in Tesla, ha reso popolare il termine "vibe coding": programmare seguendo l'intuizione del momento, lasciando che l'IA suggerisca direzioni che "sembrano giuste". È un approccio affascinante e profondamente pericoloso.

Papalini dedica diverse pagine del libro a quello che chiama "It Works Trap", la trappola del "funziona". Gli chiedo di raccontarmi quali sono i rischi a lungo termine per una codebase aziendale scritta principalmente seguendo il vibe del momento senza una rigorosa validazione umana.

"Ti racconto una storia," inizia. "Martin Fowler aveva usato l'IA per generare una visualizzazione in formato vettoriale SVG, niente di complesso. Funzionava perfettamente. Poi ha voluto fare una modifica banale: spostare un'etichetta di qualche pixel. Ha aperto il file e ha trovato quello che ha definito 'roba da pazzi', codice che funzionava, sì, ma strutturato in modo completamente alieno, impossibile da toccare senza rompere tutto. L'unica opzione? Buttare via e rigenerare da zero."

L'aneddoto cattura perfettamente il problema: "Questo è il costo reale ed il rischio del vibe coding su scala aziendale. Crei sistemi che *funzionano* ma che *nessuno capisce*. E il software aziendale deve vivere anni, a volte decenni. Deve essere modificato, esteso, debuggato alle tre di notte quando qualcosa esplode."

La soluzione che propone è semplice nella formulazione ma richiede disciplina nell'esecuzione: "La regola che dobbiamo seguire è semplice: non committare mai codice che non si sa spiegare a un collega. Se è generato con l'IA e non capisco come funziona, non è pronto per la produzione."

È come l'equivalente digitale della regola degli alpinisti: non salire su nulla da cui non sai scendere.

## Il prezzo dell'inaffidabilità

Nel libro Papalini introduce il concetto di "unreliability tax", la tassa sull'inaffidabilità. È un costo nascosto ma misurabile dell'uso di sistemi generativi nella produzione di codice. Gli chiedo di quantificare, in termini concreti di sicurezza e manutenzione, quanto costa realmente a un'azienda ripulire il codice generato dall'IA che sembra corretto ma nasconde vulnerabilità.

"I numeri fanno riflettere," esordisce. "Le ricerche mostrano che una percentuale significativa del codice generato dall'IA contiene vulnerabilità, alcune fonti parlano di quasi la metà. E la cosa subdola è che sono vulnerabilità 'plausibili': il codice sembra professionale, usa pattern riconoscibili. Solo che manca la validazione dell'input in quel punto critico, o usa una funzione crittografica deprecata."

Non si tratta di errori evidenti che qualsiasi linter segnalerebbe. Sono errori di giudizio, scelte apparentemente ragionevoli che in contesti specifici diventano buchi di sicurezza: "Il costo diretto è il tempo di remediation. Ma il costo vero è quello che non vedi subito: la vulnerabilità che passa inosservata per mesi, finché qualcuno la trova. A quel punto non stai pagando ore di sviluppo, stai pagando incident response, potenziale data breach, danni alla reputazione."

Papalini identifica anche un costo più sottile: "C'è anche una tassa più sottile: la perdita di fiducia nel sistema. Quando il team inizia a non fidarsi del proprio codice, rallenta tutto. Ogni modifica diventa un rischio. E lo stesso vale per i clienti: c'è il rischio che ci abbandonino e passino a qualcuno più affidabile."

La sua raccomandazione è pragmatica: "L'investimento sensato è in prevenzione: security scanning automatico, formazione mirata, review umano obbligatorio per tutto ciò che tocca autenticazione o dati sensibili. Costa meno che pulire i disastri dopo e perdere clientela."

## La questione della sovranità

Uno dei capitoli più densi del libro affronta il tema della sovranità dei dati e della sicurezza nell'era degli assistenti AI. Le imprese si trovano di fronte a una sfida tripla: proteggere la proprietà intellettuale dal vendor lock-in, prevenire lo Shadow AI, e mitigare quello che Papalini chiama "Security Debt" del codice probabilistico.

Gli pongo una domanda complessa: tra la velocità dei modelli cloud e la complessità dell'open source on-premise, quale architettura strategica consiglia per garantire privacy e sicurezza senza che la tutela degli asset diventi un costo insostenibile?

"È una sfida vera, la vivo ogni giorno nel settore finanziario. E la risposta onesta è: dipende dal tuo profilo di rischio," inizia Papalini. "Per la maggior parte delle aziende, un approccio ibrido funziona: modelli cloud per il codice non sensibile, con regole chiare su cosa può uscire e cosa no. I provider principali offrono ormai opzioni enterprise con garanzie contrattuali serie. Chi ha requisiti più stringenti può guardare all'on-premise con modelli open source. Llama, Mistral, DeepSeek hanno capacità notevoli. Il prezzo è la complessità operativa."

Ma identifica una minaccia spesso sottovalutata: "Ma sai qual è la minaccia più sottovalutata? Lo Shadow AI: sviluppatori che usano strumenti non autorizzati perché quelli ufficiali sono lenti da approvare o troppo limitati. La soluzione non è proibire, è offrire alternative legittime abbastanza buone da non creare l'incentivo ad aggirare le regole."

È un approccio che ricorda la harm reduction nelle politiche sanitarie: invece di criminalizzare comportamenti inevitabili, rendere disponibili alternative più sicure.

## La gavetta nell'era delle macchine

Una delle sezioni più provocatorie del libro riguarda il futuro della formazione e delle competenze. C'è una distinzione emergente tra i laureati in informatica tradizionale e la nuova figura dell'AI Engineer, qualcuno che sa orchestrare sistemi intelligenti ma potrebbe non aver mai scritto un parser da zero.

Chiedo a Papalini se l'IA che permette a chiunque di generare codice significhi la fine del programmatore "puro", o se stiamo semplicemente alzando l'asticella delle competenze architettoniche necessarie.

"Il programmatore non è destinato a scomparire, ma il suo ruolo sta cambiando parecchio," risponde. "Pensa a cosa è successo quando sono arrivati i linguaggi ad alto livello. I programmatori assembly non sono spariti, sono diventati specialisti di nicchia. Il grosso del lavoro si è spostato un gradino più su."

La transizione attuale, secondo Papalini, segue un pattern simile: "Sta succedendo qualcosa di simile adesso. Sta emergendo una figura diversa, chiamiamola 'orchestratore': qualcuno che sa scomporre problemi complessi, specificare requisiti con precisione, valutare criticamente quello che l'IA produce, prendere decisioni architetturali."

Ma qui arriva il paradosso: "Il paradosso? Serve *più* esperienza, non meno. Un junior può usare l'IA per generare codice che sembra funzionare. Ma solo un senior riconosce quando quel codice è una bomba a orologeria, perché ha visto abbastanza disastri da riconoscerne i segnali."

Il rischio sistemico che identifica è quello dell'atrofia delle competenze: "Bisogna fare attenzione poi a non pensare che tutti nascano orchestratori: se deleghiamo tutto il lavoro 'di gavetta' all'IA, come formiamo la prossima generazione di senior? I dati ci dicono che l'occupazione degli sviluppatori più giovani sta già calando. Ma anche chi entra nel mercato rischia di non sviluppare mai quelle competenze profonde che si costruiscono solo sbattendo la testa sui problemi."

## Il trio programming

Per risolvere questo dilemma, Papalini propone nel libro un modello che chiama "trio programming", un'evoluzione del pair programming che include l'IA come terzo attore.

"Nel libro propongo il 'trio programming' come soluzione al problema della formazione," spiega. "Il junior lavora con l'IA per implementare le feature. L'IA accelera, suggerisce, genera codice. Fin qui niente di nuovo. Il senior orchestratore non scrive codice, è lì per fare domande. 'Spiegami cosa fa questo metodo.' 'Perché l'IA ha scelto questa struttura dati?' 'Cosa succede se l'input è nullo?' 'Come gestiresti un errore di rete qui?'"

Il meccanismo è pedagogicamente brillante: "Rispondendo a questi quesiti, il giovane impara. Il senior, dal canto suo, trasferisce quel sapere tacito che non sta in nessun manuale, l'intuizione su cosa può andare storto, la sensibilità per il codice che 'puzza', l'esperienza di chi ha visto sistemi crollare."

È come l'apprendistato nelle botteghe rinascimentali: il maestro non dipinge al posto dell'allievo, ma gli fa notare dove la prospettiva è sbagliata, perché quella mescolanza di colori non terrà, dove la composizione perde equilibrio.

## Il valore del giudizio

Torno sul tema della monetizzazione e del valore. Papalini ha scritto diversi articoli su Medium esplorando come le aziende stiano cercando di estrarre profitto dall'IA generativa. Gli chiedo: al di là del software, come vede l'impatto dell'IA generativa nel marketing e nella creazione di prodotti digitali? È solo una questione di velocità o sta cambiando il valore stesso del prodotto?

"Sì, sta cambiando il valore ma in modo controintuitivo," risponde. "Quando tutti possono generare contenuti, immagini, codice, la *produzione* diventa commodity. È abbondante, quindi vale meno. Quello che acquista valore è tutto il resto: capire cosa vale la pena costruire, distinguere il mediocre dall'eccellente, avere una visione."

Nel software, dice, lo vede manifestarsi ogni giorno: "Se chiunque può generare un'app funzionante in un weekend, cosa distingue il tuo prodotto? Non è più l'implementazione, è l'insight sul problema, l'esperienza utente, la capacità di evolversi nel tempo."

E lo stesso vale per il marketing: "L'IA può sfornare infinite varianti di copy, immagini, video. Ma 'infinito' non significa 'efficace'. Serve qualcuno che sappia cosa testare, come leggere i risultati, quando fermarsi."

La sintesi è elegante: "Stiamo entrando in un'era di abbondanza cognitiva. Il collo di bottiglia non è più produrre, è scegliere, curare, giudicare."

È come la transizione dalla scarsità alla sovrabbondanza nell'industria musicale. Quando chiunque può registrare e distribuire un album, il valore si sposta dalla capacità tecnica di produzione alla capacità artistica di creare qualcosa che meriti attenzione.

## Agenti autonomi e il futuro prossimo

Stiamo passando dai semplici assistenti alla codifica (i vari Copilot) ai sistemi agentici autonomi, capaci teoricamente di prendere iniziative, coordinare task complessi, persino debuggare il proprio codice. Gli chiedo quale sia la sua visione sull'evoluzione degli agenti AI nell'ingegneria del software nei prossimi cinque anni. Vedremo sistemi che si auto-riparano e si auto-distribuiscono?

"Nei prossimi 12-18 mesi vedremo l'orchestrazione di agenti diventare pratica comune nelle aziende più avanzate," prevede Papalini. "Non venti agenti in parallelo, quella è roba da demo. Due o tre workstream gestiti insieme: un agente che aggiorna i test, uno che migra le dipendenze, uno che aggiunge una feature minore. Il tutto mentre lo sviluppatore si concentra sul lavoro che richiede giudizio."

Ma avverte: "La parola chiave è 'verificabile'. L'attenzione umana resta il collo di bottiglia. Non importa quanto sia veloce l'agente se poi ci vuole una settimana per capire cosa ha combinato."

Sul lungo termine è prudente: "A cinque anni? Sono prudente. Agenti che 'si auto-riparano' esistono già, rollback automatici, infrastruttura self-healing. Ma agenti che si auto-distribuiscono in autonomia completa? Per sistemi critici, ne dubito. E non sono nemmeno sicuro che dovremmo volerlo."

La sua previsione più solida riguarda il ruolo umano: "La mia previsione più sicura: il ruolo dell'ingegnere si sposta verso la specifica e la validazione, meno verso l'implementazione. Ma questo cambiamento richiederà *più* competenza da parte dei lavoratori, non meno."

## L'atrofia delle competenze

C'è un tema che attraversa l'intero libro: il rischio che l'adozione massiccia dell'IA non amplifichi le capacità umane ma le atrofizzi. È la domanda etica e sociale che sta sotto la superficie di ogni considerazione tecnica.

Gli chiedo direttamente: come possiamo garantire che l'adozione massiccia dell'IA nelle imprese non svilisca la professionalità umana, ma diventi un reale amplificatore delle capacità dei talenti?

"È la domanda che mi sta più a cuore," risponde Papalini. "Il rischio concreto lo chiamo 'atrofia delle competenze'. Un ingegnere intervistato dal MIT Technology Review ha raccontato che dopo mesi di uso intensivo dell'IA, quando ha provato a programmare senza, si sentiva perso, cose che prima erano istinto erano diventate faticose. È esattamente il campanello d'allarme che dovremmo ascoltare."

La soluzione non è il rifiuto ma l'intenzionalità: "La soluzione non è rifiutare l'IA, sarebbe come rifiutare l'elettricità. Ma dobbiamo essere intenzionali su come la integriamo, specialmente nei percorsi di formazione. È per questo che nel libro propongo modelli come il 'trio programming' per coltivare la capacità dei talenti e non commettere l'errore di segare il gradino più basso della scala dalla quale siamo saliti, il processo di apprendimento che ci ha portato dove siamo."

## Oltre il software

Alla la fine della conversazione, gli chiedo se un CEO di un'azienda che non produce software possa trovare valore nel suo libro. È una domanda legittima: il titolo parla esplicitamente di ingegneria del software.

"Assolutamente sì, e ti spiego perché," risponde con convinzione. "Il software è stato il primo dominio a essere investito in modo massiccio dall'IA generativa, quindi è il laboratorio dove certi fenomeni si sono manifestati prima e in modo più misurabile. Ma i pattern che descrivo nel libro sono universali, riguardano il rapporto tra esseri umani e sistemi probabilistici, e questo tocca ormai qualsiasi settore."

La generalizzazione è convincente: "Prendiamo il concetto centrale: il passaggio dal determinismo al non-determinismo. Quando chiedi a un'IA di scrivere codice, non sai esattamente cosa otterrai. Ma lo stesso vale quando le chiedi di scrivere una campagna marketing, analizzare un bilancio, redigere un contratto, o rispondere a un cliente. L'output sembra professionale, è formulato con sicurezza, ma potrebbe essere sottilmente sbagliato in modi che solo un esperto riconosce."

Papalini trasla ogni concetto del libro fuori dal dominio del codice: "Il 'problema del 70%' funziona identicamente in ogni contesto. L'IA ti porta rapidamente a una bozza che sembra quasi finita, un report, una presentazione, un'analisi di mercato. Ma quel 'quasi' nasconde il 30% dove servono sfumature, contesto, giudizio. Il junior nel marketing che accetta il copy generato dall'IA senza capire perché certe parole funzionano e altre no sta facendo esattamente l'errore del programmatore che committa codice che non sa spiegare."

Il tema della formazione diventa ancora più urgente: "La 'trappola della competenza' è forse il tema più urgente per qualsiasi CEO. Se i tuoi analisti junior delegano all'IA la costruzione dei modelli finanziari, non impareranno mai a farli. Se i tuoi giovani legali usano l'IA per le prime bozze senza mai scriverne una da zero, non svilupperanno mai l'intuizione per i rischi contrattuali. Stai risparmiando tempo oggi e distruggendo competenza domani."

Anche il trio programming si generalizza: "Il 'trio programming' che propongo diventa 'trio working': un junior, un senior, e l'IA che lavorano insieme. Il junior usa l'IA per accelerare, il senior fa le domande che forzano la comprensione. Funziona per formare un analista, un consulente, un account manager, qualsiasi ruolo dove l'expertise si costruisce facendo."

E il problema della governance attraversa ogni funzione aziendale: "E poi c'è lo Shadow AI, dipendenti che usano ChatGPT di nascosto perché gli strumenti ufficiali sono troppo lenti o limitati. Succede ovunque: nell'ufficio legale, nel customer service, nelle risorse umane. Non è un problema tecnologico, è un problema di governance che ogni CEO deve affrontare."

La conclusione è pragmatica: "Il libro usa il software come contesto, ma quello che racconta è la storia di come integrare strumenti potenti ma inaffidabili nel lavoro professionale senza perdere qualità, competenze e controllo. È la sfida di ogni organizzazione oggi, che produca codice, contratti, campagne pubblicitarie o analisi finanziarie."

E aggiunge una nota finale che sa di manifesto: "Un CEO che lo legge non troverà istruzioni per configurare Copilot, troverà un framework per pensare all'adozione dell'IA che può applicare a qualsiasi funzione della sua azienda. E francamente, in questo momento di hype sfrenato e aspettative gonfiate, un po' di lucidità ingegneristica può fare bene a chiunque debba prendere decisioni."

## Tante risposte che aprono tante domande

Concludiamo questa lunga chiacchierata. Papalini deve tornare a occuparsi di sistemi che movimentano capitali, io devo trasformare questa conversazione in qualcosa di leggibile. Ma la sensazione che resta è quella di aver parlato con qualcuno che sta guardando lo stesso film che stiamo guardando tutti noi, solo con qualche minuto di anticipo. 

Il libro [*Intelligenza Artificiale e Ingegneria del Software*](https://amzn.to/3Z12Ng9) non è un manuale tecnico, nonostante il titolo. È più simile a quei saggi di alpinismo scritti dopo una spedizione particolarmente rischiosa: una mappa delle cose che possono andare storte, scritta da chi è tornato per raccontarlo. Con l'unica differenza che questa montagna la stiamo scalando tutti, che ci piaccia o no, e qualcuno che ha già fatto un paio di tentativi può tornare utile.

La vera domanda non è se useremo l'intelligenza artificiale per scrivere codice, fare marketing, analizzare dati o prendere decisioni. La stiamo già usando. La domanda è se riusciremo a farlo senza perdere per strada le competenze che ci hanno permesso di arrivarci. E su questa domanda, per ora, la risposta è ancora aperta.