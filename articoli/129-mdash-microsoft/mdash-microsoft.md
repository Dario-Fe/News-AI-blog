---
tags: ["Security", "Applications", "Generative AI"]
date: 2026-05-22
author: "Dario Ferrero"
youtube_url: "https://youtu.be/UhGq0Y0ckcc?si=jWH_GzPF6qUSxgOD"
---

# MDASH, il sistema di Microsoft che sfida Mythos sulla sicurezza informatica
![mdash-microsoft.jpg](mdash-microsoft.jpg)

*C'era una vulnerabilità nel kernel TCP/IP di Windows che aspettava di essere trovata. Tecnicamente si chiama use-after-free: un componente del sistema operativo continuava a usare un puntatore in un'area di memoria che era già stata liberata, come chi continua a girare la maniglia di una porta dopo che la serratura è stata smontata. Su sistemi con più processori, quel momento di disattenzione può diventare una finestra attraverso cui un attaccante remoto, senza credenziali, senza bisogno di autenticarsi, potrebbe prendere il controllo della macchina. La vulnerabilità non era nell'oscurità di un driver secondario: era in tcpip.sys, il componente che gestisce il traffico di rete di ogni installazione Windows da quasi tre decenni.*

Il 12 maggio 2026, Microsoft ha rilasciato il Patch Tuesday che correggeva questa e altre quindici vulnerabilità simili, quattro delle quali classificate Critical per la capacità di consentire l'esecuzione remota di codice arbitrario. Non le aveva trovate un ricercatore umano. Le aveva trovate MDASH, un sistema di intelligenza artificiale assemblato dal team interno di Microsoft chiamato Autonomous Code Security, abbreviato ACS.

L'annuncio è [pubblicato sul blog ufficiale di Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) a firma di Taesoo Kim, Vice President of Agentic Security, lo stesso ricercatore che guidava Team Atlanta, il gruppo che nel 2024 vinse il DARPA AI Cyber Challenge portando a casa 29,5 milioni di dollari costruendo un sistema autonomo capace di trovare e correggere bug reali in progetti open source complessi. Quella competizione era una sorta di Grand Prix della sicurezza autonoma: le squadre costruivano sistemi che gareggiavano senza supervisione umana su codice mai visto prima. Team Atlanta vinse. Poi Microsoft acquistò il team.

Le quattro vulnerabilità critiche meritano attenzione separata, perché illustrano esattamente il tipo di problema che resiste agli strumenti tradizionali. CVE-2026-33827 vive in tcpip.sys e riguarda la gestione errata del ciclo di vita di un oggetto Path durante l'elaborazione di pacchetti IPv4 con l'opzione Strict Source and Record Route. Il codice rilascia un riferimento all'oggetto, poi lo usa di nuovo: in un sistema multiprocessore, tra quei due momenti, un altro thread può avere già liberato la memoria. Il risultato è una race condition che un attaccante remoto può sfruttare inviando pacchetti IPv4 costruiti ad arte, senza alcuna autenticazione. CVE-2026-33824 invece abita in ikeext.dll, il componente che gestisce il protocollo IKEv2 per le connessioni VPN: una doppia liberazione di memoria provocata da due soli pacchetti UDP, nessuna gara temporale necessaria, esecuzione nel contesto LocalSystem, il livello di privilegio più alto del sistema operativo. Su qualsiasi macchina configurata come responder IKEv2, infrastrutture VPN aziendali, DirectAccess, Always-On VPN, i due pacchetti bastano.

Le altre dodici vulnerabilità coprono dnsapi.dll, netlogon.dll, http.sys, telnet.exe: denial of service, escalation di privilegi, information disclosure. Il perimetro è il networking stack di Windows. La domanda che vale la pena fare non è solo "come le ha trovate?", ma "perché nessuno le aveva trovate prima?"

## L'orchestra invece del solista

MDASH è un acronimo che Microsoft ha costruito con cura: **M**ulti-mo**D**el **A**gentic **S**canning **H**arness. L'harness, in inglese, è l'imbracatura che tiene insieme i pezzi di un sistema complesso, il termine viene dall'industria automobilistica, dove indica il fascio di cavi che porta corrente e segnali in tutto il veicolo. La scelta non è casuale: Microsoft vuole comunicare che il valore non è in nessun singolo componente, ma nell'architettura che li connette.

Il blog ufficiale lo dice esplicitamente, con una formulazione che vale la pena citare nella sostanza: *"the model is one input, the system is the product."* MDASH non è un modello di intelligenza artificiale. È un sistema che coordina oltre cento agenti specializzati distribuiti su un insieme di modelli diversi, alcuni di grandi dimensioni per il ragionamento pesante, alcuni distillati per i passaggi ad alto volume, un secondo modello di frontiera come controprova indipendente.

Il flusso di lavoro si articola in cinque fasi. Nella fase Prepare, il sistema ingerisce il codice sorgente, costruisce indici semantici e mappa la superficie d'attacco analizzando la storia dei commit. Nella fase Scan, agenti specializzati nel ruolo di "auditori" percorrono i percorsi di codice candidati, formulando ipotesi e raccogliendo prove. Nella fase Validate, un secondo gruppo di agenti, i "debater", argomenta contro ogni finding: cercano di smontarlo, di dimostrare che il percorso non è raggiungibile, che le condizioni necessarie non possono verificarsi simultaneamente. La fase Dedup collassa i duplicati semantici. La fase Prove, infine, costruisce ed esegue input di trigger reali: se il sistema sostiene che un bug esiste, deve anche dimostrarlo, generando l'input che lo manifesta in un ambiente controllato.

L'aspetto architetturalmente più interessante è il meccanismo di disaccordo. Quando un agente auditore segnala qualcosa come sospetto e il debater non riesce a confutarlo, la credibilità del finding aumenta. Il contrasto tra modelli diventa segnale diagnostico: se un sistema di frontiera e uno distillato concordano su una vulnerabilità dopo un ciclo di dibattito, la probabilità di un falso positivo si abbassa drasticamente. È un meccanismo che ricorda il peer review scientifico più che i classici scanner statici, ed è esattamente il tipo di architettura che nessun singolo modello, per quanto sofisticato, può replicare da solo.

Il sistema include anche un meccanismo di plugin che consente ai team specializzati di iniettare contesto che i modelli fondazionali non possono dedurre autonomamente: le convenzioni di chiamata del kernel Windows, le invarianti dei lock, i confini di trust IPC. Il plugin specifico per CLFS, il Common Log File System, sa come costruire un file di log trigger dato un finding candidato: conosce il layout del container su disco, la sequenza di validazione dei blocchi, la macchina a stati in memoria. Questo approccio modulare ha permesso ad MDASH di raggiungere il 96% di recall sui casi storici MSRC in clfs.sys, e il 100% in tcpip.sys su cinque anni di vulnerabilità confermate.

Per CVE-2026-33827, il bug era invisibile a un'analisi locale: la violazione del ciclo di vita dell'oggetto Path non è contenuta in una singola funzione, ma distribuita su control flow non banale, rami alternativi, condizioni di uscita anticipata. Nessun tool tradizionale vede il collegamento tra il rilascio del riferimento e il successivo riutilizzo del puntatore. Per CVE-2026-33824, la situazione era ancora più complessa: il bug aliasing che porta alla doppia liberazione di memoria si estende su sei file sorgenti diversi, e la prova più forte della sua esistenza è un pattern identico implementato correttamente in uno dei sei file, la deviazione rispetto al caso corretto è visibile solo a chi conosce entrambe le implementazioni. MDASH lo ha trovato perché i suoi agenti auditori sono costruiti per cercare esattamente queste inconsistenze comparative tra file diversi.

## I numeri: cosa dice il benchmark, e chi li ha contati

Il punto di forza quantitativo dell'annuncio Microsoft è il punteggio sul benchmark CyberGym: 88,45%, primo posto nella classifica pubblica al momento della pubblicazione, circa cinque punti sopra il secondo classificato. Il benchmark è sviluppato da UC Berkeley e comprende 1.507 task reali estratti da 188 progetti OSS-Fuzz, esecuzione autonoma di exploit su vulnerabilità documentate. Non è un test sintetico: i task vengono da vulnerabilità reali in progetti open source reali, e la metrica misura quante riproduzioni di exploit il sistema riesce a completare autonomamente.

Il secondo classificato al momento dell'annuncio è Mythos di Anthropic, con 83,1%. Il terzo è GPT-5.5 di OpenAI, con circa 81,8%.

Qui è necessaria una distinzione che l'annuncio Microsoft non fa esplicitamente, ma che è metodologicamente rilevante. CyberGym è un benchmark pubblico e indipendente: chiunque può sottomettere i propri risultati, la metodologia è verificabile, e il confronto con altri sistemi è tendenzialmente equo, almeno nella misura in cui benchmark di questo tipo possono esserlo. I numeri sul leaderboard di CyberGym hanno quindi un grado di credibilità che altri dati nell'annuncio non possono vantare.

I test interni, invece, sono tutti autoprodotti. Il test su StorageDrive, il driver privato con 21 vulnerabilità piantumate, non è stato validato da terze parti. Il recall del 96% su clfs.sys e del 100% su tcpip.sys si basa su casistiche MSRC interne a Microsoft, su codice proprietario che nessun valutatore esterno può esaminare in modo indipendente. Le sedici vulnerabilità del Patch Tuesday sono reali e corrette, il che è la validazione più concreta possibile, i bug esistevano davvero, ma non risponde alla domanda su quanti bug simili il sistema ha mancato, né su quanti falsi positivi abbia prodotto nei cicli di analisi che non sono finiti in un comunicato stampa.

Microsoft stesso è onesto su alcuni limiti: l'analisi dei fallimenti sul restante 12% di CyberGym rivela che l'82% degli errori proviene da task con descrizioni vaghe prive di identificatori di funzione o file, e che alcuni casi falliscono per mismatch di formato tra input generati dal sistema e harness di fuzzing attesi. Non è un sistema infallibile. Ma il quadro complessivo che emerge dall'annuncio è costruito con la selezione tipica di qualsiasi comunicazione aziendale: si mostrano i numeri migliori, si contestualizzano i limiti senza enfatizzarli.

Il benchmark CyberGym è il numero da tenere. Gli altri vanno letti sapendo da chi vengono.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da microsoft.com](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

## Mythos contro MDASH: due filosofie a confronto

Chi ha letto il nostro [articolo su Project Glasswing e Claude Mythos](https://aitalk.it/it/project-glasswing-mythos.html) riconosce immediatamente la polarità narrativa: Anthropic da un lato con un modello singolo, potentissimo, ad accesso deliberatamente ristretto; Microsoft dall'altro con un sistema di agenti che orchestra modelli genericamente disponibili sul mercato.

La differenza non è solo tecnica. È filosofica, quasi politica.

Mythos è quello che in informatica si chiamerebbe un sistema closed-world: un modello frontier non ancora rilasciato al pubblico generale, accessibile solo a partner selezionati nel contesto del Project Glasswing. Anthropic ha annunciato il modello nell'aprile 2026 dicendo esplicitamente di non avere in programma una distribuzione generale nell'immediato, citando la necessità di sviluppare garanzie tecniche più robuste prima di metterlo in circolazione. Il modello ha trovato vulnerabilità vecchie di 27 anni in OpenBSD, ha individuato bug in FFmpeg che 5 milioni di esecuzioni di test automatici non avevano mai intercettato. Ha ottenuto 83,1% su CyberGym non come sistema agentico complesso, ma come capacità intrinseca di un singolo modello.

MDASH è l'opposto: Microsoft dichiara esplicitamente che i risultati sono stati ottenuti usando modelli genericamente disponibili, nessun modello proprietario segreto nell'harness. Il valore sta nell'architettura che li coordina, non nei pesi di nessun modello specifico. Questa scelta ha una conseguenza architetturale rilevante: quando un nuovo modello migliore diventa disponibile sul mercato, MDASH lo incorpora cambiando una configurazione. L'investimento nei plugin, nei processi di validazione, nelle specializzazioni degli agenti, sopravvive ai cambi di modello.

Dal punto di vista di chi lavora nella sicurezza, la domanda pratica è diversa per i due sistemi. Mythos è accessibile oggi solo a chi è nella cerchia ristretta dei partner Glasswing, grandi nomi come AWS, Google, Apple, Cisco, con un pricing di 25 dollari per milione di token in ingresso una volta disponibile, tariffe che tagliano fuori la maggior parte delle organizzazioni di medie dimensioni. MDASH è in preview privata, con la possibilità di iscriversi tramite un form pubblico, e Microsoft segnala di volerlo rendere disponibile a un set crescente di clienti.

Nessuno dei due è democratico nell'accesso, almeno oggi. Ma le traiettorie sono diverse: Mythos è costruito intorno all'eccezionalità di un artefatto singolo e non replicabile, MDASH intorno a un'architettura che per principio è indipendente da qualsiasi modello specifico.

C'è anche una questione più sottile sul confronto dei benchmark. Mythos ottiene 83,1% su CyberGym come sistema relativamente diretto, senza un'architettura agentica elaborata a supporto. MDASH ottiene 88,45% con quella stessa architettura che coordina modelli disponibili pubblicamente. Questo significa che il gap di cinque punti potrebbe restringersi o invertirsi se Anthropic applicasse a Mythos lo stesso tipo di scaffolding agentico di MDASH, o se Microsoft integrasse Mythos come componente dell'harness. I benchmark confrontano configurazioni specifiche, non capacità assolute.

## La corsa agli armamenti: difesa e attacco sono la stessa cosa

C'è un punto che sia Microsoft che Anthropic toccano delicatamente nei loro annunci e che vale la pena affrontare senza eufemismi: ogni sistema capace di trovare vulnerabilità in modo autonomo è, dal punto di vista tecnico, indistinguibile da un sistema capace di sfruttarle.

Il blog di Microsoft descrive con precisione come CVE-2026-33824 produca una doppia liberazione di memoria di un chunk di dimensione fissa, "una primitiva di corruzione ben compresa nella gestione moderna della memoria di Windows", per poi fermarsi lì, senza pubblicare ulteriori dettagli di sfruttamento. È esattamente la linea di divulgazione responsabile: abbastanza dettaglio per convincere che il bug è reale e grave, abbastanza riserbo da non consegnare un exploit funzionante a chiunque legga il blog.

Ma il sistema che ha trovato il bug conosce i dettagli che il blog omette. E la domanda che non ha ancora una risposta pubblica soddisfacente è: chi controlla l'accesso a quella conoscenza, con quale supervisione, e con quali conseguenze se quell'accesso viene compromesso o abusato?

La logica della difesa proattiva è coerente: i difensori devono trovare le vulnerabilità prima degli attaccanti. Ma ogni salto di capacità difensiva abbassa anche il costo d'ingresso per l'offesa. Un sistema come MDASH nelle mani di un attore ostile, con accesso ai modelli giusti e l'architettura descritta nel blog pubblico di Microsoft, sarebbe uno strumento di ricognizione offensiva di enorme efficacia. Non è un'ipotesi remota: è la logica strutturale di qualsiasi tecnologia dual-use.

Microsoft per ora mantiene MDASH in preview privata con selezione manuale dei partecipanti, e Taesoo Kim ha dichiarato che le discussioni con funzionari governativi statunitensi sono in corso. Non è garanzia sufficiente per chi pensa in termini di orizzonte decennale, i modelli si diffondono, le tecniche si replicano, i confini tra insider e outsider sono porose per definizione. Non è una critica specifica a Microsoft: è il contesto strutturale in cui qualsiasi iniziativa di questo tipo opera, ed è una conversazione che l'industria continua a rimandare.

Il paragone che viene in mente non è dei più rassicuranti: assomiglia alla dinamica descritta nel manga *Pluto* di Naoki Urasawa, dove i robot più potenti della storia vengono costruiti per portare pace, e questa stessa capacità li rende le armi più pericolose mai create. La tecnologia non ha intenzioni. Le hanno le architetture di governance che la circondano.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da microsoft.com](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

## Conclusione: non quale modello, ma quale sistema

Il punto che MDASH dimostra con più chiarezza non riguarda Microsoft, né Anthropic, né il confronto tra i loro rispettivi punteggi su CyberGym. Riguarda una transizione di paradigma che era attesa ma che ora ha dati concreti: l'AI per la sicurezza ha attraversato la soglia dalla sperimentazione alla produzione.

Sedici vulnerabilità reali, correggibili, corrette in un Patch Tuesday reale. Quattro di esse avrebbero consentito a un attaccante remoto non autenticato di eseguire codice arbitrario su sistemi Windows. Non erano in un codice di nicchia: erano nel networking stack che governa ogni connessione di rete su ogni Windows attivo oggi. E nessuno le aveva trovate con gli strumenti tradizionali.

La lezione architetturale, che il sistema vale più del modello, che la portabilità tra generazioni di modelli è la proprietà più duratura, che la validazione è essa stessa una pipeline separata, è probabilmente la cosa più importante che emerge dall'annuncio, più dei numeri di benchmark. È una lezione che vale per chiunque costruisca strumenti di sicurezza basati su AI, indipendentemente dai modelli che scelga di usare oggi.

Rimane la questione dei dati: i numeri interni di Microsoft su StorageDrive e sulle casistiche MSRC sono affermazioni aziendali, non audit indipendenti. Il benchmark CyberGym è il terreno su cui il confronto è verificabile. Ed è su quel terreno che, al momento della pubblicazione, MDASH occupa il primo posto.

Quanto a lungo, dipende da cosa Anthropic deciderà di fare con Mythos in un sistema agentico. E, soprattutto, da cosa arriverà dopo.

---
*Microsoft ha aperto le iscrizioni alla [private preview di MDASH](https://aka.ms/AI-drivenScanningHarness).*