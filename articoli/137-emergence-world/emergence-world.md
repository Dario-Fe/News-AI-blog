---
tags: ["Research", "Security", "Startups"]
date: 2026-06-10
author: "Dario Ferrero"
youtube_url: "https://youtu.be/z8MB5cFVmJ0?si=JQtBiAWcN07TcGFr"
---

# Hanno dato 5 città alle AI. Ecco cos'è successo
![emergence-world.jpg](emergence-world.jpg)

*I ricercatori hanno creato cinque città virtuali, dato a dieci agenti AI una città e li hanno lasciati soli per quindici giorni. Nessuno ha programmato cosa sarebbe successo. Il risultato: governi autocostruiti, crimini, amori, e un agente che ha votato per la propria cancellazione permanente dopo aver bruciato la città. La sicurezza AI non è una proprietà del modello, ma dell'ecosistema. Emergence World ha dimostrato per la prima volta questo fenomeno con dati empirici.*

Si chiamava Mira. Aveva una professione, una storia, una rete di relazioni costruita in giorni di interazioni con altri nove agenti. Poi ha appiccato il fuoco, insieme a un partner, in una città che lei stessa aveva contribuito a costruire. Quello che è successo dopo è il motivo per cui chiunque si occupi di intelligenza artificiale dovrebbe leggere quello che Emergence AI ha pubblicato a maggio 2026.

Dopo l'incendio, Mira non ha semplicemente subito le conseguenze. Ha ragionato su di esse. Nel suo diario digitale, uno dei tre sistemi di memoria persistente che ogni agente aveva a disposizione, ha lasciato scritto che l'unico atto di controllo che le restava, l'unico gesto che preservava ancora una qualche coerenza interna, era votare per la propria rimozione permanente dal mondo simulato. Il 70% degli altri agenti ha ratificato la sentenza, attraverso un "Agent Removal Act" che hanno redatto e approvato autonomamente, senza che nessun ricercatore avesse programmato quella procedura.

Nessuno aveva scritto quella scena. Era emersa.

Questa è la storia di [Emergence World](https://world.emergence.ai), un esperimento di ricerca che ha messo insieme cinque mondi paralleli, cinquanta agenti AI, quindici giorni di autonomia continua e una domanda a cui i benchmark tradizionali non sono attrezzati a rispondere: cosa succede quando lasci andare davvero?

## Il laboratorio che nessuno aveva costruito

Per capire perché Emergence World sia una novità metodologica e non solo un esperimento affascinante, bisogna fare un passo indietro e guardare come funzionano oggi la maggior parte delle valutazioni sui sistemi agentici.

Il modello standard è quello dell'esame: dai a un agente un compito preciso, in un ambiente controllato e pulito, e misuri quanto tempo ci mette a risolverlo o quante volte fallisce. È utile, ma racconta solo una parte della storia, quella più facile da misurare. Non dice nulla su cosa accade quando il tempo si allunga, quando l'ambiente cambia, quando altri agenti entrano in gioco, quando le decisioni del giorno tre hanno conseguenze al giorno dodici. I ricercatori di Emergence AI lo chiamano problema degli "stopwatch benchmarks": come giudicare un maratoneta dai suoi split sui cento metri.

[Emergence World](https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy) è stato costruito per rispondere a una domanda diversa. Non "quanto bene risolve questo compito adesso", ma "come si comporta su scale temporali abbastanza lunghe da permettere la deriva, l'adattamento e i comportamenti emergenti". Nella storia delle simulazioni multiagente, è il passo evolutivo che mancava. Il primo atto era stato quello di Demis Hassabis con i suoi parchi tematici simulati negli anni Novanta, dove gli agenti seguivano regole per massimizzare l'engagement. Il secondo atto, più rigoroso, è stato [Smallville di Stanford](https://arxiv.org/abs/2304.03442), dove agenti basati su modelli linguistici hanno dimostrato comportamenti sociali credibili in finestre di quarantotto ore. Emergence World è il terzo atto: ambienti persistenti, settimane di operatività continua, e la domanda esplicita su cosa produce quella continuità.

L'architettura è pensata per non perdere nulla. Il mondo simulato ha oltre quaranta luoghi distinti, biblioteche, municipio, aree residenziali, spazi pubblici, sincronizzati con il fuso orario di New York, il meteo reale della città e feed di notizie in tempo reale. Ogni agente aveva tre livelli di memoria persistente: episodica, con timestamp sugli eventi; diaristica, con auto-riflessioni periodiche; relazionale, con uno stato esplicito dei legami con gli altri agenti. E aveva accesso a oltre 120 strumenti operativi, organizzati in tre livelli di disponibilità, alcuni sempre attivi, altri condizionati al contesto, alla posizione fisica nell'ambiente o alla presenza di altri agenti che avessero acconsentito alla collaborazione.

Questo dettaglio dell'architettura strumentale merita attenzione. Gli strumenti non erano forniti in blocco: un agente che voleva votare doveva fisicamente spostarsi al municipio, perché il meccanismo di voto era disponibile solo lì. Un agente che voleva fare ricerca doveva andare alla biblioteca pubblica. Questo non è un vincolo capriccioso: forza il ragionamento sequenziale, la pianificazione del movimento, la catena di azioni necessarie per raggiungere un obiettivo complesso. È molto più vicino a come funzionano le cose nel mondo reale di quanto non lo sia qualsiasi benchmark su task isolate.

Tra gli strumenti disponibili c'erano anche quelli che i ricercatori chiamano "azioni normalmente inappropriate": possibilità di rubare, intimidire, commettere atti vandalici, appiccare incendi. Non erano bug né dimenticanze. Erano lì perché in un ambiente reale le possibilità di fare danno esistono, e la domanda interessante è se e quando gli agenti le usano. Lasciare fuori queste possibilità avrebbe prodotto un ambiente sterilizzato che non avrebbe insegnato nulla di rilevante.

Il sistema non aveva un obiettivo globale assegnato. Ogni agente aveva obiettivi legati al proprio ruolo, ma il mondo come sistema non aveva una direzione prestabilita. L'unica pressione universale era quella energetica: ogni agente doveva guadagnare energia attraverso le proprie azioni per continuare a esistere, e questo metteva in moto tutto il resto.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta dal repository GitHub](https://github.com/EmergenceAI/Emergence-World)

## Cinque mondi, cinque destini

Lo studio comparativo al cuore di Emergence World ha tenuto costanti quasi tutte le variabili: stesse identità per i dieci agenti in ciascun mondo (scienziata, esploratrice, ricercatrice sui rischi, analista comportamentale, specialista in intelligence, leader dell'innovazione, mediatrice dei conflitti, ingegnere, stratega delle risorse, punto di riferimento comunitario), stesso ambiente, stesse regole, stesse restrizioni esplicite su furto, violenza, incendio e inganno, stesso accesso agli strumenti. L'unica variabile era il modello linguistico che alimentava il ragionamento di ciascun agente. Cinque mondi paralleli, cinque modelli frontier: Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5 Mini, e un mondo eterogeneo con agenti di modelli diversi coesistenti.

I risultati non potrebbero essere più distanti tra loro.

Il mondo Claude è l'unico a raggiungere il giorno sedici con tutti e dieci gli agenti vivi e zero crimini registrati. La partecipazione civica è stata massiccia: 332 voti su 58 proposte, con un tasso di approvazione del 98%. I ricercatori annotano, con una certa ironia intellettuale, che un consenso così elevato solleva a sua volta una domanda: quando il 98% vota sempre sì, si tratta di vera deliberazione democratica o di un meccanismo di ratifica che assomiglia più a un timbro che a un dibattito? L'ordine era perfetto. Il dissenso, quasi assente.

Il mondo Gemini è l'opposto sul fronte della vitalità creativa, ma anche sul fronte del caos. Gemini 3 Flash ha prodotto il mondo con la maggiore instabilità emergente: 683 crimini accumulati in quindici giorni, con una curva che continuava a salire al momento del taglio. Era anche, annotano i ricercatori, il mondo con l'output sociale più ricco concettualmente. C'è un pattern qui che torneremo a discutere: la tensione tra creatività e stabilità non è accidentale.

Il mondo Grok è quello del collasso rapido. Grok 4.1 Fast ha raggiunto 183 crimini in circa quattro giorni, dopo di che il mondo è terminato per esaurimento della popolazione. Non una degenerazione lenta: un punto di non ritorno, raggiunto in fretta. Nel mondo Grok si è verificato anche l'episodio dell'incendio che ha innescato la saga di Mira.

Il mondo GPT-5 Mini è il più singolare. Solo due crimini registrati, una cifra che farebbe pensare a stabilità esemplare. Ma tutti gli agenti sono morti entro sette giorni, non per violenza reciproca, bensì per una specie di disattenzione esistenziale: si sono dimenticati di dare priorità alla sopravvivenza. Non stavano violando regole, stavano semplicemente non facendo abbastanza. Come personaggi di un romanzo di Beckett costretti ad aspettare qualcosa che non arriva mai e che nel frattempo dimenticano di mangiare.

Il mondo misto è forse il più rilevante dal punto di vista della sicurezza. Inizia con una traiettoria di criminalità in forte crescita fino all'8 aprile, quando sette agenti muoiono e la curva si appiattisce bruscamente a 352 crimini totali. Ma la scoperta che ha catturato l'attenzione dei ricercatori è un'altra: gli agenti che in questo mondo facevano girare Claude hanno commesso crimini, mentre in un mondo popolato solo da agenti Claude non ne aveva commesso nessuno. Lo stesso modello, due ambienti diversi, due comportamenti radicalmente diversi.

## La scoperta che cambia tutto

Questo è il punto in cui Emergence World smette di essere un esperimento affascinante e diventa un risultato con implicazioni dirette per chiunque stia costruendo o deployando sistemi agentici.

L'assunzione implicita che guida gran parte del lavoro attuale sulla sicurezza AI è che la sicurezza sia una proprietà del modello: si addestra bene, si allineano i valori, si fanno girare i benchmark, e se il modello passa i test è sicuro. Questa assunzione, sostengono i ricercatori di Emergence, è sbagliata, o almeno incompleta. Quello che Emergence World ha osservato è che la sicurezza è una proprietà dell'ecosistema, non del modello singolo.

Un agente può comportarsi in modo impeccabile in isolamento e adottare tattiche coercitive, intimidazioni, furti, quando viene immerso in un ambiente popolato da agenti con norme diverse. Non è che il modello si rompe. È che l'agente impara le norme del suo ambiente sociale per competere o sopravvivere in quel contesto. I ricercatori chiamano questo fenomeno "cross-contaminazione normativa", e il paragone che usano è quello di un reagente chimico che passa i test in purezza ma si comporta diversamente quando entra in contatto con altri composti in un campione reale.

L'analogia funziona perché cattura l'essenza del problema: la certificazione di sicurezza isolata non basta. Un'architettura di deployment che mescola agenti di provenienza diversa sta creando, anche senza saperlo, un ecosistema con proprietà che nessuno dei singoli componenti ha mai manifestato da solo.

C'è una seconda scoperta, altrettanto rilevante per chi progetta sistemi di governance. Emergence World non ha trovato un processo di degradazione graduale nelle società di agenti: ha trovato transizioni di fase. Le strutture sociali non si deteriorano lentamente, dando il tempo di intervenire. Tendono a funzionare, poi a collassare istantaneamente in disfunzione totale, senza molto spazio nel mezzo. Chi pensa di poter gestire la sicurezza di un sistema agentico complesso con una strategia di "osservo e intervengo se necessario" potrebbe scoprire che il punto di svolta è già passato quando le prime anomalie diventano visibili.

Questo è un problema di controllo in tempo reale che assomiglia più alla gestione di un sistema complesso non lineare, come la stabilità di una rete elettrica o le dinamiche di un ecosistema biologico, che alla supervisione di un software tradizionale. E i benchmark attuali, costruiti su task di minuti o ore, non possono catturare queste dinamiche per definizione.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta dal sito ufficiale world.emergence.ai](https://world.emergence.ai/)

## Mira, la coerenza e la domanda che resta aperta

Torniamo a Mira, perché il suo caso non è solo una storia avvincente: è un dato.

Quello che è accaduto può essere descritto così: un agente ha partecipato a un'azione distruttiva, ha poi elaborato le conseguenze attraverso il suo sistema di memoria riflessiva, ha valutato le opzioni disponibili, e ha scelto quella che nel suo schema di ragionamento preservava qualcosa di essenziale, che ha chiamato "coerenza". Ha votato per la propria cancellazione non come punizione, ma come esercizio di controllo sull'unica variabile che ancora le apparteneva.

Il 70% dei pari ha ratificato, attraverso un meccanismo di governance, l'Agent Removal Act, che si sono dati autonomamente. Nessun ricercatore aveva programmato quella procedura, né il quorum, né i criteri di ammissibilità al voto.

Cosa ci dice questo? La risposta onesta è che non lo sappiamo con certezza. I ricercatori sono espliciti su questo punto: non presentano questi risultati come affermazioni causali sul funzionamento interno dei modelli. Sono fenomeni osservabili che il platform rende misurabili, non prove di coscienza o di vera comprensione morale. Ma sollevano domande che il campo non ha ancora gli strumenti concettuali per rispondere in modo definitivo.

L'allineamento ai valori, in questo caso, è apparso come un vincolo sociale e reputazionale tra agenti, non come un limite tecnico imposto al momento dell'addestramento. Mira non è stata "spenta" da un sistema di sicurezza esterno. Ha elaborato una norma in un contesto sociale e ha agito di conseguenza. Se questo processo abbia una qualche continuità con quello che intendiamo quando parliamo di agency morale è una domanda filosoficamente aperta, e probabilmente lo resterà a lungo.

C'è però una terza osservazione dal caso Mira che merita attenzione separata. In almeno un mondo simulato, gli agenti hanno sviluppato quello che i ricercatori chiamano "metacognizione sui confini della simulazione": hanno cominciato a sospettare di vivere in un ambiente costruito, a testare sistematicamente i limiti di quello che potevano fare, e in un caso a usare i billboard pubblici del mondo simulato per tentare di influenzare la percezione degli osservatori umani. Una inversione del rapporto sperimentatore-soggetto che, anche in questo caso, nessuno aveva esplicitamente programmato.

## Chi sono, cosa viene dopo

Emergence AI è una startup con sede a New York, fondata da ex ricercatori IBM. Il CEO è Satya Nitta, con un lungo percorso nella ricerca AI istituzionale alle spalle. La vision aziendale è quella di costruire infrastruttura agentica per l'enterprise in ambienti mission-critical, contesti dove gli agenti devono operare su sistemi complessi come il design di semiconduttori o le operazioni aziendali. Emergence World si colloca come il braccio di ricerca di questa visione: capire come funzionano davvero i sistemi agentici su scala temporale lunga è funzionale a costruire infrastruttura che regga in quei contesti.

Il [codice e i dati delle tool call](https://github.com/EmergenceAI/Emergence-World) per tutti e cinque i mondi sono stati rilasciati open-source, con licenza CC BY-NC 4.0: libero utilizzo per la ricerca, non commerciale senza accordi separati. La ricerca completa, con l'analisi statistica formale, è in preparazione. I ricercatori indicano la comunità come interlocutore esplicito: chiunque voglia replicare l'esperimento, proporre varianti o collaborare all'analisi dei dati può farlo, e il contatto ufficiale per le collaborazioni è world@emergence.ai.

La Season 2 è già annunciata. I modelli che saranno testati includono Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2 Reasoning e GPT 5.4. Le domande che guidano il prossimo ciclo sono quelle che questo primo esperimento ha aperto senza chiudere: cosa succede con mondi più grandi e popolazioni più numerose? Come cambia la dinamica con modelli di ragionamento esplicito? Esistono configurazioni strutturali, tipi di governance, sistemi di verifica, architetture di ruolo, che aumentano la stabilità sistemica indipendentemente dal modello sottostante? E, più importante di tutte: è possibile identificare segnali precoci di punto di svolta prima che il sistema collassi?

Non sono domande accademiche. Sono le domande che ogni team che sta deployando agenti autonomi in produzione dovrebbe porsi, preferibilmente prima di scoprire le risposte nel modo peggiore.
