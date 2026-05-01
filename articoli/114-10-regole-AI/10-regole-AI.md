---
tags: ["Generative AI", "Security", "Business"]
date: 2026-04-17
author: "Dario Ferrero"
youtube_url: "https://youtu.be/SSQITcGdzB4?si=Mr9_U4Ckhg8yADYr"
---

# 10 regole per usare l'AI in azienda
![10-regole-AI.jpg](10-regole-AI.jpg)

*Partiamo da un dato che vale come specchio. Secondo il [rapporto McKinsey State of AI del novembre 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), l'88% delle organizzazioni usa già l'AI in almeno una funzione di business. Eppure, nello stesso periodo, il World Economic Forum e Accenture hanno stimato che meno dell'1% di queste ha pienamente reso operativo un approccio di AI responsabile, mentre l'81% rimane nelle fasi più embrionali di maturità governance. Il paradosso è servito: quasi tutti usano l'AI, quasi nessuno la governa davvero.*

La conferma più bruciante arriva da [un sondaggio EY del febbraio 2026](https://www.ey.com/en_us/newsroom/2026/03/ey-survey-autonomous-ai-adoption-surges-at-tech-companies-as-oversight-falls-behind) su 500 executive tecnologici: il 45% ha dichiarato che la propria organizzazione ha subito negli ultimi dodici mesi una fuga confermata o sospetta di dati sensibili causata da dipendenti che usavano strumenti di AI generativa non autorizzati, ChatGPT, Claude, Gemini, spesso con dati aziendali sensibili incollati dentro un prompt, senza che l'IT sapesse nulla. Il [PEX Report 2025/26](https://www.aidataanalytics.network/data-science-ai/news-trends/less-than-half-of-businesses-have-an-ai-governance-policy) chiude il quadro: solo il 43% delle organizzazioni ha una policy di AI governance formale, mentre quasi un terzo, il 29%, non ne ha proprio nessuna.

Questo pezzo non vuole essere una lezione dall'alto. È più simile a quella conversazione utile che si ha con un collega prima di una scelta importante: qualcosa che aiuta a capire dove si stanno mettendo i piedi, con esempi concreti e riferimenti verificabili. Dieci regole, dieci controlli, dieci errori da non ripetere.

## Prima di tutto: la sicurezza AI non è sicurezza IT con un cappello nuovo

Chi lavora in ambito IT sa che esiste già un arsenale consolidato di strumenti per la protezione dei sistemi: firewall, gestione delle identità, cifratura, vulnerability assessment. Il problema è che l'AI introduce una superficie di rischio che questi strumenti non vedono.

Un modello linguistico può produrre risposte false con la stessa sicurezza con cui produce quelle corrette, un fenomeno che nel campo si chiama allucinazione e che in contesti aziendali può tradursi in decisioni sbagliate basate su informazioni inventate. Un sistema RAG (retrieval-augmented generation) che accede ai documenti interni può essere manipolato attraverso un'istruzione nascosta in un file apparentemente innocuo: è quello che l'[OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) chiama *prompt injection*, e che nel 2025 è già stata sfruttata in ambienti reali. I dati che inserisci nel sistema possono essere memorizzati, registrati o inviati a infrastrutture esterne che non controlli.

Il [NIST AI Risk Management Framework](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/), aggiornato e sempre più adottato come riferimento globale, organizza la risposta a questi rischi in quattro funzioni: *Govern, Map, Measure, Manage*. Non sono passaggi sequenziali, sono ruote che girano in modo continuo. Ed è da qui che conviene partire.

## La governance prima della tecnologia

Prima di qualsiasi strumento, serve una risposta chiara a tre domande: chi decide cosa si può fare con l'AI in azienda? Chi risponde se qualcosa va storto? A chi si scala il problema?

ISO/IEC 42001, lo standard internazionale per i sistemi di gestione dell'AI pubblicato a dicembre 2023 e già adottato come riferimento da [KPMG](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) e altri grandi attori della consulenza, risponde a queste domande con un concetto semplice: serve un *AI Management System* con ruoli nominati, processi documentati e cicli di miglioramento continuo. Non è burocrazia fine a sé stessa: è il modo per non trovarsi a gestire un incidente senza sapere chi ha l'autorità di spegnere il sistema.

ISO/IEC 42001:2023 rimane lo standard in vigore e il riferimento certificabile per i sistemi di gestione AI. Vale però la pena segnalare che nell'aprile 2025 ISO ha pubblicato [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/), uno standard complementare dedicato specificamente alle valutazioni d'impatto dei sistemi AI, uno strumento che aiuta a misurare gli effetti sociali e individuali dell'AI lungo tutto il ciclo di vita, non solo i rischi tecnici. Non è obbligatorio per ottenere la certificazione 42001, ma nella pratica colma esattamente il gap tra "abbiamo una governance" e "sappiamo cosa produce concretamente il nostro sistema sulle persone"

### Il problema invisibile: lo shadow AI

Prima ancora di parlare di classificazione dei rischi, c'è un fenomeno che vale la pena nominare esplicitamente perché è il più diffuso e il meno presidiato: lo *shadow AI*. Funziona esattamente come lo shadow IT degli anni Duemila, quando i dipendenti iniziarono a usare Dropbox e Gmail personale per i file di lavoro perché gli strumenti aziendali erano lenti, solo che le conseguenze sono più immediate e meno reversibili.

Un dipendente del settore finanziario che incolla un foglio di bilancio non consolidato in ChatGPT per farsi aiutare a scrivere un commento, un recruiter che carica i CV dei candidati su uno strumento esterno per farsi fare una preselezione, un avvocato che usa un LLM consumer per bozzare una clausola contrattuale: in tutti questi casi i dati escono dall'infrastruttura aziendale, finiscono su server di terze parti con policy di retention che l'azienda non ha negoziato, e potenzialmente contribuiscono all'addestramento di modelli futuri. Il dato EY citato in apertura, il 45% di data leak da strumenti non autorizzati, non è un'eccezione: è la norma silenziosa.

La risposta non è vietare tutto, perché i divieti non presidiati non funzionano, come insegna la storia dello shadow IT. La risposta è costruire alternative governate che siano abbastanza buone da non spingere le persone a cercare soluzioni esterne, accompagnate da una policy chiara su cosa è consentito, con quali strumenti e sotto quali condizioni. Questo è esattamente il punto di partenza della governance AI.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da blog.getpolicyguard.com](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/)

## Regola 1 — Classifica i casi d'uso per livello di rischio, prima del deployment

Non tutti gli usi dell'AI sono uguali. Un chatbot interno per rispondere a domande sulle ferie è diverso da un sistema che valuta i candidati HR o che assegna un rating di credito ai clienti. Il [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) usa la funzione *Map* esattamente per questo: creare un inventario dei sistemi AI in uso e classificarli per livello di impatto potenziale.

L'[EU AI Act](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems), con piena applicabilità agli usi ad alto rischio entro agosto 2027, identifica come sistemi ad alto rischio quelli usati per la selezione e il monitoraggio dei dipendenti, per il credito e per la profilazione degli individui. Per ciascuno di questi casi, gli obblighi aumentano in modo significativo: valutazione d'impatto, supervisione umana, registrazione dei log, notifica degli incidenti.

Un esempio concreto: se la tua azienda usa un LLM per supportare i recruiter nella preselezione dei CV, quel sistema è ad alto rischio per l'EU AI Act. Se lo stesso modello viene usato solo per generare bozze di job description, il rischio è molto più basso. La classificazione deve essere fatta caso per caso, non per categoria generica di strumento.

## Regola 2 — Limita i dati che entrano nel sistema

Il principio è lo stesso della dieta: non tutto quello che puoi mangiare devi mangiarlo. In ambito AI, si chiama *data minimization*, ed è il primo presidio contro il rischio di *data leakage*.

La guida pubblicata da [CISA, NSA e FBI nel maggio 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) è esplicita: le organizzazioni devono classificare i dati prima di usarli nei sistemi AI, applicare controlli di accesso rigorosi e non assumere mai che i dataset siano puliti e privi di contenuti malevoli. La stessa guida introduce il concetto di *data provenance*: sapere da dove vengono i dati con cui il modello lavora non è una formalità, è un requisito di sicurezza.

Nella pratica: stabilisci per policy quali categorie di dati non possono mai entrare in un sistema AI (segreti industriali, credenziali, dati personali non strettamente necessari, informazioni soggette a vincoli normativi). Un esempio utile per il settore finanziario: i dati di bilancio non consolidati non dovrebbero mai essere usati come contesto in un chatbot aziendale generico accessibile a tutta l'organizzazione.

## Regola 3 — Governa fornitori, modelli e integrazioni

L'AI aziendale raramente è un sistema monolitico che controlli per intero. Di solito è un assemblaggio: una piattaforma SaaS, un modello fondazionale di un terzo, dei plugin, dei tool esterni collegati tramite API. Ciascuno di questi componenti è un potenziale punto di ingresso per rischi che non hai valutato direttamente.

La [guida congiunta CISA del 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) dedica un'intera sezione ai rischi della *data supply chain*, con un'attenzione particolare al *data poisoning*: la manipolazione dei dati di addestramento da parte di attori malevoli, che può avvenire attraverso dataset raccolti dal web, domini scaduti ricomprati ad arte, o iniezioni di esempi falsi nei corpora usati per il fine-tuning.

Il controllo pratico è una valutazione del fornitore strutturata: per ogni fornitore di componenti AI, verifica dove vengono registrati i log delle interazioni, se e come i tuoi dati vengono usati per addestrare modelli, quali garanzie contrattuali esistono sul trattamento dei dati. ISO/IEC 42001 prevede esplicitamente la *third-party supplier oversight* come requisito del sistema di gestione.

## Regola 4 — Testa il sistema prima del rilascio

Nessun sistema AI dovrebbe andare in produzione senza aver attraversato un ciclo di test che includa scenari di abuso. L'EU AI Act, per i sistemi ad alto rischio, lo richiede esplicitamente come parte del *quality management system*: verifiche su accuratezza, robustezza, bias e comportamenti inattesi prima del go-live.

Il *red teaming*, ovvero la simulazione di attacchi e usi impropri da parte di un team interno o esterno, non è una pratica riservata alle grandi tech company. Strumenti come [Promptfoo](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) permettono di automatizzare test basati sull'OWASP LLM Top 10 anche senza una squadra di sicurezza dedicata.

Un esempio concreto per il customer service: prima di rilasciare un assistente conversazionale che ha accesso ai dati dei clienti, verifica sistematicamente se risponde in modo diverso a utenti con nomi di diversa origine culturale (test di bias), se rivela informazioni su utenti diversi da quello autenticato (test di leakage), se può essere indotto a ignorare le istruzioni di sistema con prompt elaborati (test di jailbreak).

## Regola 5 — Proteggiti da prompt injection e output pericolosi

Questa è la regola più tecnica, ma vale la pena capirla perché è anche quella più sottovalutata. La *prompt injection* funziona così: un utente, o un contenuto esterno che il modello legge, inserisce istruzioni che sovrascrivono quelle originali del sistema. Il modello non distingue tra le istruzioni del suo operatore e quelle iniettate: le esegue entrambe, e spesso preferisce quelle più recenti.

L'[OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/), il documento di riferimento per la sicurezza dei modelli linguistici, indica questo come rischio numero uno. Le contromisure operative includono: separare architetturalmente le istruzioni di sistema dagli input degli utenti, limitare gli strumenti a cui il modello ha accesso (un assistente che risponde a domande sui prodotti non ha bisogno di poter inviare email o modificare database), applicare filtri sull'output per intercettare risposte che contengono dati strutturati sensibili.

L'età agentica è già iniziata e si è oltre i chatbot e i copilot, gli agenti non si limitano a rispondere a una domanda ma eseguono sequenze di azioni, navigano siti, leggono e scrivono file, chiamano API, mandano email, con supervisione umana minima o nulla. Il [report Deloitte State of AI in the Enterprise del gennaio 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) stima che solo 1 azienda su 5 ha oggi un modello maturo di governance per gli agenti AI autonomi, mentre il loro utilizzo è destinato a crescere nettamente nei prossimi due anni.

In questo contesto, il principio del minimo privilegio smette di essere una buona pratica e diventa una condizione di sopravvivenza: un agente con accesso illimitato a strumenti, dati e canali di comunicazione può produrre danni difficilmente reversibili, velocemente e in modo automatico. Prima di deployare qualsiasi sistema agentico, la domanda da porsi è: se questo agente fraintende l'istruzione nel modo più ragionevolmente sbagliato possibile, cosa succede?
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

## Regola 6 — Mantieni un controllo umano reale, non solo formale

Esiste una versione vuota della *human oversight*: metti una firma in calce a un documento che dice che un umano ha supervisionato la decisione, anche se in realtà nessuno ha davvero controllato nulla. L'EU AI Act, agli articoli dedicati agli obblighi dei deployer di sistemi ad alto rischio, è specifico su questo punto: la supervisione umana deve essere sostanziale, non decorativa. Gli addetti alla supervisione devono avere la competenza per interpretare gli output, la capacità di interrompere il sistema e l'autorità per farlo.

La distinzione pratica da stabilire per iscritto in ogni processo critico è questa: l'AI suggerisce, l'umano decide. Non "l'AI decide e l'umano può opporsi", perché il costo psicologico dell'opposizione a un sistema automatico è già stato documentato dalla ricerca: le persone tendono ad accettare i suggerimenti dei sistemi automatici anche quando hanno dubbi, soprattutto sotto pressione di tempo. In ambito HR, finanza, compliance e salute, questa dinamica non è accettabile.

## Regola 7 — Monitora il sistema dopo il go-live

Il lancio non è l'arrivo: è la partenza. I sistemi AI degradano nel tempo per ragioni che non sempre sono ovvie: il linguaggio degli utenti cambia, i dati di input si spostano rispetto alla distribuzione originale (è quello che la [guidance CISA](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) chiama *data drift*), i pattern di abuso evolvono. Serve un sistema di logging che registri a campione gli output, alert automatici quando le metriche di qualità si discostano dalla baseline, e un processo di incident response che risponda alla domanda: se il sistema fa qualcosa di sbagliato stanotte, chi se ne accorge e in quanto tempo?

L'EU AI Act richiede la conservazione dei log per almeno sei mesi per i sistemi ad alto rischio, e la notifica alle autorità in caso di incidenti gravi. ISO/IEC 42001 prevede revisioni periodiche del sistema di gestione. Il NIST AI RMF, nella funzione *Manage*, insiste su un monitoraggio attivo che alimenti il ciclo di miglioramento.

## Regola 8 — Documenta tutto, davvero

Se non è documentato, non è governabile. È una frase che suona ovvia ma che nell'operatività quotidiana viene sistematicamente ignorata. La documentazione di un sistema AI non è il manuale d'uso: è l'insieme di policy approvate, valutazioni di rischio, risultati dei test, versioni del modello in produzione, decisioni prese e motivazioni.

Questa documentazione serve a tre cose concrete: dimostrare la conformità normativa in caso di audit, capire cosa è cambiato quando qualcosa smette di funzionare, e migliorare il sistema nel tempo imparando dagli errori. Il formato non è prescrittivo, ma deve essere tracciabile e accessibile a chi ne ha bisogno. Un registro delle versioni del modello in produzione, tenuto su un file Excel condiviso aggiornato manualmente, vale già più di niente.

Per chi vuole strutturare questo passaggio in modo rigoroso, [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/) offre un framework specifico per documentare l'impatto dei sistemi AI, compresi usi sensibili, prevedibili abusi e applicazioni non intenzionali, mappato direttamente sui controlli di ISO/IEC 42001.

## Regola 9 — Forma le persone che usano il sistema

L'errore umano resta una delle superfici di rischio più ampie, e la formazione è il presidio più economico contro di essa. Ma c'è un dato che trasforma questo principio da buon senso generico a leva strategica misurabile: secondo il [report CSA e Google Cloud del dicembre 2025](https://cloudsecurityalliance.org/blog/2025/12/18/ai-security-governance-your-maturity-multiplier), il 65% delle organizzazioni con una governance AI completa forma già il proprio personale sugli strumenti AI, contro solo il 27% di quelle con policy parziali e il 14% di quelle ancora in fase di sviluppo. Non è un dettaglio: la formazione è uno degli indicatori più discriminanti tra chi governa l'AI davvero e chi si limita a scrivere policy che nessuno legge.

La formazione sull'AI non è un corso di un'ora obbligatorio che tutti cliccano senza guardare: deve essere specifica per ruolo e deve affrontare tre cose distinte. La prima è l'uso corretto degli strumenti: come si usa il sistema, cosa si può chiedere, cosa non si deve mai inserire. La seconda è il riconoscimento dei limiti: i dipendenti devono sapere che i modelli linguistici possono sbagliare con grande sicurezza, e devono avere l'autorità di non fidarsi dell'output quando hanno dubbi fondati. La terza è la gestione degli incidenti: cosa fare quando qualcosa va storto, a chi segnalarlo, come documentarlo. L'EU AI Act richiede esplicitamente *AI literacy training* per tutti gli utenti di sistemi ad alto rischio: non è un dettaglio normativo, è buon senso operativo con una scadenza.

## Regola 10 — Aggiorna le regole nel tempo

L'AI è forse l'unico campo in cui le istruzioni operative invecchiano più in fretta dei sistemi che governano. Un framework di governance scritto a inizio 2024 non tiene conto delle capacità agentiche dei modelli attuali, dei nuovi vettori di attacco documentati nel 2025, o delle scadenze normative dell'EU AI Act che si avvicinano. Sia il [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) sia [ISO/IEC 42001](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) sono costruiti attorno al principio del miglioramento continuo: le policy vanno riviste almeno una volta l'anno, e ogni incidente significativo deve innescare una revisione immediata dei controlli correlati.

La cadenza minima praticabile è questa: revisione annuale del framework complessivo, revisione semestrale delle policy sui dati, revisione immediata dopo ogni incidente o cambiamento rilevante nei modelli in uso. Non è un ciclo pesante: è la differenza tra una governance viva e un documento che nessuno aggiorna.

## Concludendo

Riprendendo una metafora da *Ghost in the Shell*, non quella cinematografica di Hollywood, ma il manga originale di Masamune Shirow, il problema non è mai il sistema in sé, ma chi lo ha costruito e con quale intenzione. L'AI aziendale funziona quando chi l'ha adottata sa esattamente cosa vuole ottenere, conosce i rischi che porta con sé e ha costruito una struttura capace di rispondere quando le cose non vanno come previsto.

La domanda da farsi non è "stiamo usando l'AI?". Quasi certamente sì. La domanda è: "sappiamo con quali regole?"