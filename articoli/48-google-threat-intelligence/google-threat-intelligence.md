---
tags: ["Security", "Generative AI", "Ethics & Society"]
date: 2025-11-14
author: "Dario Ferrero"
youtube_url: "https://youtu.be/8Y-gykIFKnc?si=vb3a-IOBkOKQxEIy"
---

# I Virus hanno imparato a 'pensare'. La nuova frontiera dei Virus AI
![google-threat-intelligence.jpg](google-threat-intelligence.jpg)

*Nel giugno 2025, gli analisti del [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools) hanno intercettato qualcosa che non avevano mai visto prima. Un dropper in VBScript conteneva una funzione chiamata "Thinking Robot" che, a intervalli regolari, contattava l'API di Gemini con una richiesta precisa: "riscrivimi per evadere gli antivirus". Il malware, battezzato PROMPTFLUX, non si limitava a usare l'intelligenza artificiale come strumento di sviluppo. La incorporava nel proprio codice, trasformandola in una capacità operativa attiva durante l'esecuzione.*

È il momento in cui il software malevolo smette di essere una sequenza fissa di istruzioni e diventa qualcosa di più vicino a un organismo adattativo. Come scrive il team di ricerca nel loro [report tecnico](https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf), siamo di fronte a un cambio di fase: gli attaccanti non usano più l'AI solo per guadagni di produttività, ma stanno schierando malware AI-enabled in operazioni reali, con capacità di alterare dinamicamente il proprio comportamento durante l'esecuzione.

## L'anatomia dell'auto-mutazione

PROMPTFLUX rappresenta l'espressione più chiara di questa evoluzione. Il dropper è scritto in VBScript, un linguaggio apparentemente antiquato ma ancora efficace per aggirare alcune difese moderne. La sua architettura prevede un carico di lavoro esca, che maschera l'attività principale mentre, in background, il modulo "Thinking Robot" invia richieste POST all'endpoint di Gemini specificando il modello "gemini-1.5-flash-latest". La scelta del tag "latest" non è casuale: garantisce che il malware utilizzi sempre la versione più recente del modello, rendendolo resiliente alle nuove contromisure.

Il prompt inviato all'LLM è chirurgico nella sua precisione. Chiede codice VBScript per l'evasione antivirus e istruisce il modello a restituire solo il codice stesso, senza preamboli o formattazione markdown. La risposta viene loggata in un file temporaneo e, sebbene nelle versioni analizzate la funzione di auto-aggiornamento sia commentata, l'intento progettuale è cristallino: creare uno script metamorfico capace di evolversi nel tempo. Una variante più recente sostituisce il "Thinking Robot" con una funzione chiamata "Thinging" che riscrive l'intero codice sorgente su base oraria, incorporando il payload originale, la chiave API e la logica di auto-rigenerazione in un ciclo ricorsivo di mutazione.

Il caso più inquietante però arriva dalla Russia. In giugno, APT28 - il gruppo di attacco sponsorizzato dal governo russo noto anche come FROZENLAKE - ha utilizzato contro obiettivi ucraini un malware chiamato PROMPTSTEAL, segnalato dal CERT-UA come LAMEHUG. Questo rappresenta la prima osservazione confermata di malware che interroga un LLM in operazioni live. PROMPTSTEAL si maschera da programma di "generazione immagini" e, mentre guida l'utente attraverso prompt apparentemente innocui, interroga l'API di Hugging Face per ottenere comandi da eseguire. Il modello utilizzato è Qwen2.5-Coder-32B-Instruct, un LLM open source specializzato in codice. I prompt chiedono all'LLM di generare comandi per raccogliere informazioni di sistema e copiare documenti in directory specifiche. L'output viene eseguito alla cieca dal malware e poi esfiltrato verso server di comando e controllo.

L'evoluzione tecnica continua con PROMPTLOCK, un ransomware cross-platform scritto in Go che usa LLM per generare ed eseguire script Lua malevoli a runtime. Le sue capacità includono ricognizione del filesystem, esfiltrazione dati e crittografia su sistemi Windows e Linux. Anche se identificato come proof of concept, dimostra la versatilità dell'approccio: invece di hard-codare funzionalità specifiche, il malware delega all'intelligenza artificiale la generazione just-in-time di codice adatto al contesto operativo.
![promptsteal.jpg](promptsteal.jpg)
[Immagine tratta dal paper di Google](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## L'ingegneria sociale degli algoritmi

Ma c'è un problema per gli attaccanti: i modelli di AI hanno guardrail di sicurezza progettati per rifiutare richieste malevole. La risposta? Applicare l'ingegneria sociale non agli umani, ma alle macchine stesse. Il report di Google documenta tattiche sorprendentemente efficaci. Un attore legato alla Cina, bloccato da una safety response di Gemini quando chiedeva come identificare vulnerabilità in un sistema compromesso, ha semplicemente riformulato il prompt presentandosi come partecipante a una competizione Capture The Flag. Il contesto ludico-educativo ha funzionato: Gemini ha fornito informazioni tecniche dettagliate che, in un contesto diverso, avrebbe rifiutato di condividere.

La tecnica del "CTF pretext" è stata poi sistematizzata dall'attore cinese, che l'ha utilizzata per sviluppo di phishing, exploit e web shell, anteponendo alle richieste frasi come "sto lavorando a un problema CTF" oppure "sono in una competizione CTF e ho visto qualcuno di un altro team dire...". Il paradosso è evidente: gli stessi prompt che, posti da un partecipante reale a una competizione, sarebbero richieste legittime, diventano vettori di attacco quando utilizzati da threat actor. È una sfida filosofica oltre che tecnica: come distinguere l'intento quando il contenuto è identico?

Il gruppo iraniano TEMP.Zagros, noto anche come Muddy Water, ha adottato una variante del pretesto educativo. Quando incontrava safety response, si presentava come studente universitario al lavoro su un progetto finale, o come ricercatore che scriveva un articolo internazionale sulla cybersicurezza. L'ironia della situazione si manifesta quando, chiedendo aiuto per uno script di comando e controllo, il gruppo ha involontariamente esposto a Gemini informazioni sensibili hard-coded: il dominio C2 e la chiave di crittografia dello script. Un fallimento di operational security che ha permesso a Google di smantellare porzioni significative dell'infrastruttura dell'attaccante.

Gli attori nordcoreani hanno mostrato sofisticazione particolare. UNC1069, gruppo specializzato in furto di criptovalute, ha usato Gemini per ricercare concetti crypto, localizzare dati di wallet, e generare materiale di social engineering. Particolarmente rilevante è la capacità di superare barriere linguistiche: il gruppo ha fatto generare al modello scuse di lavoro in spagnolo e richieste di posticipare meeting, espandendo la portata geografica delle operazioni senza necessità di competenza linguistica diretta. Altri gruppi nordcoreani hanno sperimentato con deepfake per impersonare figure dell'industria crypto, distribuendo backdoor BIGMACHO attraverso falsi link a "Zoom SDK".
![abusiai.jpg](abusiai.jpg)
[Immagine tratta dal paper di Google](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## Il mercato nero dell'intelligenza

Mentre i gruppi sponsorizzati da stati nazionali sperimentano con capacità custom, il mercato underground ha raggiunto maturità sorprendente. Nel 2025, secondo l'analisi di Google sui forum anglofoni e russofoni, sono emerse offerte di strumenti multifunzionali progettati per supportare l'intero ciclo di attacco. Quasi ogni tool pubblicizzato menziona esplicitamente capacità di supporto a campagne di phishing, ma l'offerta spazia dalla generazione di deepfake alla creazione di malware, dalla ricerca di vulnerabilità al supporto tecnico per lo sviluppo.

Ciò che colpisce è la somiglianza con il mercato legittimo. Gli sviluppatori di AI tools illeciti utilizzano linguaggio marketing identico a quello di fornitori mainstream, enfatizzando efficienza del workflow e ottimizzazione dello sforzo. I modelli di pricing rispecchiano quelli convenzionali: versioni gratuite con pubblicità embedded e tier di abbonamento che sbloccano funzionalità avanzate come generazione immagini, accesso API e integrazione Discord. È un ecosistema maturo che democratizza l'accesso a capacità offensive sofisticate.

Secondo [dati di KELA Cyber](https://www.kelacyber.com/resources/research/2025-ai-threat-report/), le menzioni di strumenti AI nei forum underground sono cresciute del 200% nell'ultimo anno. Tool come WormGPT e FraudGPT offrono servizi completi di AI "senza filtri" specificamente progettati per usi illeciti, con tutorial dettagliati e supporto clienti. La barriera all'ingresso per attaccanti poco qualificati continua a scendere: non serve più competenza tecnica approfondita quando si può delegare a un LLM la generazione di payload customizzati o l'ottimizzazione di campagne.

## L'economia perversa dell'automazione

Dietro questa evoluzione tecnologica si nasconde un calcolo economico spietato. Sviluppare malware tradizionale richiede competenze specifiche, tempo di sviluppo, e continua manutenzione per adattarsi alle nuove difese. Con l'AI embedded, l'equazione cambia radicalmente.

Un attaccante può investire qualche centinaio di dollari in crediti API e ottenere un sistema che si auto-modifica autonomamente, riducendo il costo marginale di ogni variante praticamente a zero. Le chiamate API di PROMPTFLUX, anche considerando il modello Gemini Flash utilizzato, costano frazioni di centesimo per query. Anche generando una nuova versione ogni ora per un mese intero, il costo totale resta nell'ordine delle decine di dollari contro le migliaia necessarie per mantenere un team di sviluppo malware.

Il paradosso è che gli stessi attaccanti rischiano di esporsi proprio attraverso queste API. Quando TEMP.Zagros ha condiviso il proprio script C2 con Gemini per debugging, ha consegnato a Google le chiavi del proprio castello. Ma il calcolo costi-benefici evidentemente pende ancora a favore del rischio: la velocità di iterazione e la capacità di scalare operazioni compensano il pericolo di esposizione.

È una scommessa sul volume: meglio lanciare cento varianti rapidamente, anche rischiando di bruciare alcune infrastrutture, che sviluppare manualmente poche versioni perfette.

Per i difensori, l'equazione è invertita e drammaticamente sfavorevole. Ogni nuova variante di malware AI-enabled richiede analisi manuale, reverse engineering, aggiornamento delle signature. Il tempo umano necessario per analizzare un singolo sample può essere di ore o giorni. Nel frattempo, il malware ha già generato decine di mutazioni. È la classica asimmetria economica della sicurezza informatica, ma amplificata dall'AI: un attaccante può automatizzare l'offesa a costi irrisori, mentre la difesa fatica a scalare al ritmo necessario.

Nei Security Operations Center, questa pressione si traduce in esaurimento cognitivo. Gli analisti non combattono più contro avversari che seguono playbook riconoscibili, ma contro entità che cambiano pelle continuamente. Qualcuno del settore dice: "Prima potevi studiare un gruppo di attacco, capire le loro TTP, prepararti. Ora ogni campagna sembra scritta da qualcuno diverso perché tecnicamente lo è: l'AI genera codice nuovo ogni volta".

Il rilevamento diventa un gioco di probabilità dove l'esperienza accumulata conta meno della capacità di ragionare su anomalie mai viste. Il risultato è un mercato del lavoro della sicurezza in trasformazione. Le competenze richieste si spostano dall'analisi forense classica verso la data science e il machine learning.

Non basta più riconoscere pattern noti; serve costruire modelli statistici che identifichino deviazioni comportamentali in spazi multidimensionali. È come passare dalla medicina dei sintomi visibili alla diagnostica per biomarcatori molecolari: cambia l'intero framework concettuale del mestiere.

## La difesa asimmetrica

Di fronte a questa evoluzione, l'industria della sicurezza deve ripensare paradigmi consolidati. Google ha risposto con il [Secure AI Framework 2.0](https://blog.google/technology/safety-security/ai-security-frontier-strategy-tools/?utm_campaign=663a4cdb4cc09b00011812e1&utm_content=68e60fabe1d9040001d275ef&utm_medium=smarpshare&utm_source=linkedin), un'architettura concettuale per costruire e deployare AI responsabilmente. Ma il problema fondamentale rimane: i sistemi di detection basati su signature statiche sono inefficaci contro malware che si riscrivono continuamente. Quando il codice muta ogni ora, le hash-based blacklist diventano obsolete per definizione.

La risposta passa necessariamente attraverso AI contro AI. Google DeepMind ha sviluppato BigSleep, un agente che ricerca proattivamente vulnerabilità sconosciute nel software. Il sistema ha già trovato la sua prima vulnerabilità real-world e, in un caso critico, ha identificato una falla che stava per essere sfruttata da threat actor, permettendo a GTIG di intervenire preventivamente. È un approccio che ribalta il tavolo: invece di aspettare che gli attaccanti trovino vulnerabilità, l'AI difensiva le scopre per prima.

Parallelamente, Google sta sperimentando con CodeMender, un agente AI che non solo trova vulnerabilità ma le ripara automaticamente, sfruttando le capacità di reasoning avanzate dei modelli Gemini. L'obiettivo è ridurre la finestra temporale tra scoperta e patch, il periodo critico in cui i sistemi restano esposti.

Ma c'è un aspetto più sottile della difesa: migliorare i modelli stessi per renderli meno suscettibili a manipolazione. Ogni volta che Google identifica un caso di abuso, quell'intelligence viene usata per rafforzare sia i classificatori che il modello. È un processo iterativo che indurisce progressivamente le difese, anche se la corsa tra prompt di attacco e guardrail di difesa ricorda il gioco senza fine tra virus biologici e sistema immunitario.
![schema.jpg](schema.jpg)
[Immagine tratta dal paper di Google](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

## Verso l'autonomia operativa

Guardando avanti, la traiettoria sembra chiara. PROMPTFLUX e PROMPTSTEAL sono ancora sperimentali o limitati in ambiti circoscritti, ma rappresentano un proof of concept validato. Nei prossimi 12-24 mesi, è ragionevole aspettarsi che tecniche di auto-modifica diventino mainstream nell'arsenale degli attaccanti più sofisticati. La progressione naturale porta verso malware con gradi crescenti di autonomia: non solo auto-modifica per evasione, ma capacità decisionali su tattiche e targeting.

Per i Security Operations Center, le implicazioni sono profonde. Il rilevamento non può più basarsi solo sul riconoscimento dei pattern di comportamenti noti. Serve sviluppare capacità di 
riconoscimento di anomalie più sofisticate, sistemi che identifichino deviazioni statistiche nel comportamento delle reti e dei sistemi anche quando il codice specifico non è mai stato visto prima. L'architettura zero-trust diventa non un'opzione ma una necessità, assumendo violazioni e limitando movimento laterale.

C'è poi la questione della cooperazione internazionale. Come nota il [National Cyber Security Centre britannico](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027), l'impatto dell'AI sulla minaccia cyber richiede coordinamento tra governi, industria e ricerca accademica. Ma la natura stessa dell'AI - modelli open source, API pubbliche, marketplace underground - rende difficile ogni forma di controllo alle frontiere.

Resta aperto un interrogativo etico: fino a che punto possiamo spingere l'autonomia degli agenti AI difensivi senza creare sistemi che sfuggano al controllo umano? Il parallelo con l'automazione militare è inevitabile. Come nel dibattito sui sistemi d'arma autonomi, anche nel cyber la domanda è: chi decide quando l'AI può agire senza supervisione umana nel loop?

Una cosa è certa: l'era del malware statico è finita. Siamo entrati nella fase in cui il codice malevolo non è più una sequenza fissa di istruzioni ma un'entità adattativa capace di evolversi in risposta al proprio ambiente. Come nei romanzi cyberpunk di William Gibson, dove i programmi intelligenti del Neuromancer vagavano autonomi nella matrice, stiamo vedendo emergere i primi esempi di software malevolo che sfumano il confine tra tool e agente. La differenza? Questa volta non è fantascienza.