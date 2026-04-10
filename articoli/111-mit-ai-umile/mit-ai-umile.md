---
tags: ["Research", "Applications", "Ethics & Society"]
date: 2026-04-10
author: "Dario Ferrero"
youtube_url: "https://youtu.be/dyDBOZ5EiCw?si=EiAYDXmVCOpwWemT"
---

# MIT e l’AI “umile”: come insegnare ai modelli a dire “non lo so”
![mit-ai-umile.jpg](mit-ai-umile.jpg)

C'è un esperimento mentale che i ricercatori del MIT usano per spiegare il problema al cuore della loro ricerca. Immaginate un medico di terapia intensiva alle tre di notte, dopo dodici ore di turno. Sul monitor compare una diagnosi generata dall'AI: polmonite batterica, probabilità 94%. Il medico ha un dubbio, una sensazione viscerale che qualcosa non torni. Ma il numero è lì, preciso, autorevole. E il medico cede.

Non è fantascienza. [Studi documentati](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/) mostrano che medici di terapia intensiva e radiologi tendono a seguire le indicazioni dell'AI anche quando la propria esperienza clinica suggerisce il contrario, purché il sistema mostri un numero di confidenza sufficientemente alto. Il fenomeno ha un nome tecnico, *automation bias*, e in medicina può costare vite. La ricerca citata nel paper descrive casi in cui radiologi e personale di terapia intensiva hanno ridotto la propria accuratezza diagnostica dopo l'introduzione di sistemi AI overconfident, seguendo suggerimenti sbagliati presentati con tono definitivo.

Il caso più clamoroso di questa deriva rimane IBM Watson for Oncology, il sistema che tra il 2012 e il 2017 fu venduto a decine di ospedali nel mondo come rivoluzione nella cura del cancro. Addestrato su casi sintetici e non su dati reali di pazienti, Watson raccomandò trattamenti che oncologi esperti giudicarono non sicuri, e mostrò una concordanza con le decisioni cliniche umane sensibilmente inferiore a quella promessa. Il caso Watson non è solo la storia di un prodotto fallito: è la dimostrazione di cosa succede quando si costruisce un oracolo anziché uno strumento.

Ed è esattamente da questo punto che parte il lavoro del [MIT Critical Data](https://criticaldata.mit.edu/), il consorzio globale guidato dal Laboratory for Computational Physiology del MIT, che a marzo 2026 ha pubblicato un framework per fare qualcosa di apparentemente semplice, ma tecnicamente molto complicato: insegnare a un sistema AI a dire "non lo so".

## Due paper, una tesi

Per capire la portata di questa ricerca bisogna tenere insieme due pubblicazioni distinte che rappresentano le due facce dello stesso progetto. La prima è apparsa il 24 marzo 2026 su [*BMJ Health and Care Informatics*](https://informatics.bmj.com/content/33/1/e101877), il giornale di informatica clinica del British Medical Journal: si tratta di un framework operativo per progettare sistemi AI "umili" nell'ambito della diagnosi medica. La seconda, pubblicata a gennaio 2026 su [*PLOS Digital Health*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/), è un paper teorico più ambizioso che introduce il framework BODHI, acronimo di Bridging, Open, Discerning, Humble, Inquiring (Connettere, Aperto, Discernente, Umile, Curioso), una architettura dual-reflective che propone di incorporare curiosità ed umiltà come principi fondativi di qualsiasi sistema AI in ambito sanitario.

A firmare entrambi i lavori è sostanzialmente la stessa squadra internazionale, coordinata da [Leo Anthony Celi](https://imes.mit.edu/people/celi-leo), ricercatore senior al MIT Institute for Medical Engineering and Science, medico al Beth Israel Deaconess Medical Center di Boston e professore associato alla Harvard Medical School. Il lead author del paper BMJ è Sebastián Andrés Cajas Ordóñez, ricercatore di MIT Critical Data, già primo autore del paper PLOS Digital Health. Attorno a loro, un consorzio che include ricercatori dell'Università di Melbourne, del King's College London, dell'ETH Zurigo, dell'Università di Bergen e della Mbarara University of Science and Technology in Uganda: una composizione geografica che non è casuale, come vedremo.

La novità concettuale che accomuna i due lavori è questa: non basta che un sistema AI misuri la propria incertezza internamente, cosa che molti modelli già fanno in qualche forma. Il cambiamento di paradigma sta nel fatto che quella incertezza deve *modificare il comportamento del sistema*, tradursi in azioni concrete, comunicabili e verificabili da chi interagisce con la macchina. Come dice Celi nella [nota stampa del MIT](https://news.mit.edu/2026/creating-humble-ai-0324): stiamo usando l'AI come un oracolo, quando potremmo usarla come un coach, come un vero co-pilota.

## Come funziona: misurare l'incertezza e farne qualcosa

Il cuore tecnico del framework pubblicato su BMJ ruota attorno a un modulo chiamato Epistemic Virtue Score, sviluppato dai ricercatori Janan Arslan e Kurt Benke dell'Università di Melbourne. L'idea di fondo è relativamente intuitiva: ogni volta che il sistema genera una risposta diagnostica, deve anche valutare se il proprio livello di confidenza è *giustificato* dall'evidenza disponibile nel caso specifico. Se la risposta è no, ovvero se la confidenza supera ciò che i dati del paziente supportano realmente, il sistema non risponde semplicemente con un numero di probabilità. Si ferma, segnala il disallineamento e suggerisce azioni specifiche: richiedere ulteriori esami, raccogliere anamnesi più dettagliata, consultare uno specialista.

In pratica, il modello smette di funzionare come un arbitro che emette sentenze definitive e comincia a comportarsi come quello che Celi chiama un *co-pilota*: un sistema che ti dice non solo dove siamo, ma anche quando non sa esattamente dove siamo e perché sarebbe meglio fermarsi a chiedere indicazioni. La metafora è sua: "È come avere un co-pilota che ti dice che devi cercare un secondo parere per capire meglio questo paziente complesso."

Il framework BODHI, descritto nel paper PLOS Digital Health, elabora questa idea in un'architettura più articolata. I cinque attributi dell'acronimo non sono semplici aggettivi: ciascuno corrisponde a un insieme di comportamenti operativi. *Bridging* significa connettere il ragionamento algoritmico con la conoscenza clinica contestuale del caso. *Open* indica la recettività verso nuove informazioni e ipotesi alternative. *Discerning* è la capacità di distinguere le predizioni ad alta confidenza da quelle che richiedono ulteriore esame. *Humble* si riferisce alla quantificazione dell'incertezza e alla deferenza verso l'expertise umana nei casi ambigui. *Inquiring* è la tendenza attiva a cercare informazioni aggiuntive quando la situazione diagnostica è poco definita.

Il paper descrive un framework a quattro quadranti basato su due assi: la complessità clinica del caso e la gravità delle conseguenze potenziali. In scenari semplici e a basso rischio, il sistema risponde direttamente. All'aumentare della complessità, si attiva la modalità curiosità, che genera domande. All'aumentare della gravità potenziale, si attiva il checkpoint di umiltà, che trasferisce la decisione all'expertise umana. Nel quadrante in alto a destra, casi complessi *e* ad alto rischio, entrambe le modalità sono attive simultaneamente e il sistema esegue una escalation collaborativa.
![quattroquadranti.jpg](quattroquadranti.jpg)
[Immagone tratta da informatics.bmj.com](https://informatics.bmj.com/content/33/1/e101877)

## Innovazione reale o rebranding concettuale?

È una domanda che vale la pena porsi esplicitamente, perché il rischio di rinominare cose già esistenti con linguaggio nuovo è sempre presente nel campo dell'AI. L'uncertainty quantification, ovvero la capacità di un modello di stimare quanto è certa la propria risposta, non è una novità: tecniche come gli ensemble di modelli, la calibrazione bayesiana, la selective prediction (dove il sistema si astiene dal rispondere sotto una soglia di confidenza), la out-of-distribution detection (che rileva quando un input è molto diverso dai dati di addestramento) esistono da anni nella letteratura di machine learning.

Allora dove sta la novità reale? Il punto critico, riconoscibile leggendo con attenzione entrambi i paper, è la distinzione tra *misurare* l'incertezza e *agire in base ad essa in modo clinicamente strutturato*. Sistemi come MUSE, descritto nella letteratura correlata, usano sottoinsiemi fidati di modelli multipli per produrre probabilità meglio calibrate, e questo rappresenta già un miglioramento rispetto ai modelli singoli. Ma l'Epistemic Virtue Score e il framework BODHI fanno un passo successivo: traducono la misura dell'incertezza in *regole di comportamento esplicite e verificabili*, non solo in numeri. La domanda non è soltanto "quanto è sicuro il modello?" ma "data questa incertezza, cosa deve fare il sistema?"

In termini pratici, la differenza è quella tra un cruscotto che mostra la riserva di carburante e un'auto che, sotto una certa soglia, si rifiuta di partire fino a quando non rifornisci. Entrambi misurano la stessa cosa, ma solo uno traduce la misura in comportamento obbligato. Il framework MIT-BODHI si colloca in questa seconda categoria. Il che non lo rende rivoluzionario in senso assoluto, ma lo rende metodologicamente più maturo di molte proposte precedenti che si fermavano alla misura senza arrivare all'azione.

## Il problema nascosto: chi non è nei dati

C'è un punto che attraversa entrambi i paper del MIT e che merita attenzione indipendente, perché tocca una delle radici più profonde del problema. Molti modelli AI in ambito clinico vengono addestrati su dataset di cartelle cliniche elettroniche, come il celebre [MIMIC](https://mimic.mit.edu/), il database costruito dai dati del Beth Israel Deaconess Medical Center. MIMIC è uno dei dataset più utilizzati nella ricerca di AI medica nel mondo, ed è un lavoro straordinario. Ma è anche, per definizione, un archivio costruito su una popolazione specifica: prevalentemente statunitense, prevalentemente urbana, con le caratteristiche demografiche di chi ha accesso a un grande ospedale di Boston.

Chi non compare in questi dati? Pazienti delle aree rurali, che spesso non hanno accesso a strutture con cartelle cliniche digitali avanzate. Popolazioni anziane con presentazioni atipiche delle malattie. Pazienti di paesi a medio e basso reddito, dove la copertura sanitaria digitale è frammentata. Minoranze etniche storicamente sottorappresentate nei dataset clinici.

Il problema non è teorico. Il paper BODHI cita esplicitamente il caso dei pulse oximetri, che funzionano peggio sui pazienti con pelle scura perché calibrati quasi esclusivamente su campioni di pazienti bianchi, come esempio paradigmatico di come bias sistematici nel dato originale si trasformino in errori clinici concreti. Un modello addestrato su dati distorti risponderà con sicurezza anche nelle situazioni in cui, per chi non è rappresentato nel training set, quella sicurezza è del tutto infondata.

È per questo che il consorzio MIT Critical Data è costruito deliberatamente come struttura globale, con ricercatori provenienti da Uganda, Norvegia, Svizzera, Australia, Regno Unito, Brasile. Celi lo dice esplicitamente: i workshop di MIT Critical Data iniziano sempre con una domanda ai partecipanti, siete sicuri che i vostri dati di addestramento catturino tutte le variabili rilevanti per quello che volete predire? Ci sono pazienti che sono stati esclusi, intenzionalmente o meno, e come influisce sull'affidabilità del modello?

Un'AI umile, in questo senso, deve anche essere consapevole dei propri dati di origine. Il framework BODHI introduce esplicitamente il concetto di *out-of-distribution detection* in chiave clinica: il sistema deve riconoscere quando il paziente che ha davanti è significativamente diverso dalla popolazione su cui è stato addestrato, e comportarsi di conseguenza, alzando le bandiere di incertezza invece di rispondere con la stessa sicurezza che mostra per i casi che conosce bene.
![grafico.conf.jpg](grafico.conf.jpg)
[Immagine tratta da informatics.bmj.com](https://informatics.bmj.com/content/33/1/e101877)

## I rischi dell'umiltà: la falsa modestia e l'eccesso di cautela

Sarebbe però ingenuo presentare questo framework come soluzione priva di controindicazioni. I rischi esistono, e il paper PLOS Digital Health ha l'onestà di riconoscerli parzialmente, anche se la trattazione critica potrebbe essere più estesa.

Il primo rischio è quello che si potrebbe chiamare *falsa modestia*: un sistema che mostra incertezza può apparire più affidabile anche quando quell'incertezza è mal calibrata. La percezione di trasparenza, il fatto che il modello "ammetta i propri dubbi", potrebbe generare nei medici una fiducia paradossalmente più alta rispetto a un sistema che si presenta come oracolo. Se la soglia di attivazione dell'Epistemic Virtue Score è impostata male, o se i segnali di incertezza sono troppo frequenti e poco contestualizzati, il rischio è che diventino rumore di fondo, una sorta di avviso di sicurezza come quelli che ignoriamo ogni volta che installiamo un'applicazione sul telefono.

Il secondo rischio è l'*alert fatigue*. In ambito ospedaliero, l'eccesso di allarmi è già un problema documentato: i sistemi di monitoraggio che suonano continuamente finiscono per essere disattivati o ignorati dal personale sanitario perché la maggior parte degli allarmi si rivela non urgente. Un modello AI che segnala incertezza con troppa frequenza potrebbe aggiungere ulteriore rumore cognitivo a ambienti già sovraccarichi di stimoli, peggiorando anziché migliorare la qualità delle decisioni.

Il terzo rischio riguarda il carico cognitivo. Un'AI che chiede dati aggiuntivi, suggerisce consulenze specialistiche e segnala i propri limiti è, in linea teorica, migliore di un oracolo silenzioso. Ma in un pronto soccorso congestionato, con venti pazienti in attesa, ogni passaggio aggiuntivo nel flusso decisionale ha un costo reale. L'interazione ideale tra medico e macchina descritta nel paper richiede tempo, attenzione e la disponibilità del clinico a impegnarsi in un dialogo con il sistema, condizioni che non sempre si verificano nella pratica clinica quotidiana.

Questi non sono argomenti contro il progetto, sono le condizioni che ne determineranno il successo o il fallimento nell'implementazione reale. E qui emerge il limite più onesto da riconoscere nell'attuale stadio della ricerca.

## Dove siamo: framework senza validazione clinica randomizzata

La domanda più importante da porre a qualsiasi sistema proposto per la medicina è: funziona davvero su pazienti reali? E la risposta attualmente onesta è: non lo sappiamo ancora con sufficiente certezza.

Entrambi i paper sono, nella loro natura, lavori teorici e metodologici. Il paper BMJ descrive un framework e una proposta architetturale. Il paper BODHI è costruito su una sintesi interdisciplinare di letteratura esistente, senza dati sperimentali propri. Nella sezione Data Availability del paper PLOS Digital Health, gli autori lo dichiarano esplicitamente: nessun dataset è stato generato o analizzato in questo studio, che presenta un framework teorico basato su analisi concettuale e sintesi della letteratura.

L'implementazione pratica è in corso: il team di Celi sta lavorando per integrare il framework in sistemi AI basati sul database MIMIC all'interno del sistema Beth Israel Lahey Health. Questa è la fase successiva, quella in cui si vedrà se i meccanismi di umiltà migliorano effettivamente le decisioni cliniche, riducono gli errori diagnostici e non aumentano semplicemente la complessità operativa. Quella validazione non è ancora pubblicata.

Questo non è un difetto del lavoro, è la natura del processo scientifico. Prima viene il framework concettuale robusto, poi la validazione sperimentale. Il problema nasce quando i media (e le aziende tecnologiche) saltano direttamente dal framework al titolo *l'AI che salva le diagnosi*, comprimendo anni di ricerca necessaria in una promessa immediata. Il lavoro del MIT Critical Data merita attenzione proprio perché non fa questa promessa: propone una direzione, indica gli strumenti, e si prepara a testarli sul campo.

## Chi firma la diagnosi? Il nodo della responsabilità

C'è una dimensione di questo problema che i paper sfiorano ma non affrontano in profondità, e che è forse quella di maggiore interesse per chi lavora in ambito regolatorio o legale: se un sistema AI dichiara esplicitamente la propria incertezza, cambia qualcosa sul piano della responsabilità medica?

Consideriamo due scenari. Nel primo, un sistema AI fornisce una diagnosi con il 93% di confidenza, il medico la segue, e il paziente subisce un danno perché la diagnosi era errata. Nel secondo, il sistema dichiara "confidenza 93%, ma questo paziente ha caratteristiche demografiche non ben rappresentate nel mio training set, suggerirei una valutazione specialistica aggiuntiva". Il medico ignora l'avviso e il paziente subisce lo stesso danno.

Nei due casi la responsabilità del medico è identica? Quella del produttore del sistema AI cambia? La risposta non è ovvia, e varia significativamente tra ordinamenti giuridici diversi. Negli Stati Uniti, la FDA regola i sistemi AI in ambito medico come dispositivi, e la questione di come l'esplicitazione dell'incertezza interagisce con le approvazioni normative è aperta. In Europa, il nuovo AI Act e il Regolamento sui dispositivi medici creano un quadro in evoluzione in cui i sistemi di supporto decisionale clinico sono classificati come ad alto rischio e soggetti a obblighi di trasparenza. Ma la domanda specifica se un sistema "umile" che comunica i propri limiti modifichi il regime di responsabilità non ha ancora risposta normativa consolidata.

Il punto è rilevante anche per l'adozione. Un ospedale che implementa un sistema AI che esplicitamente segnala i propri limiti si espone a un rischio legale diverso rispetto a uno che usa un sistema silenzioso? La risposta potrebbe essere: dipende da come i log del sistema vengono trattati in caso di contenzioso. Se il sistema ha segnalato incertezza e il medico ha ignorato il segnale, quella registrazione digitale diventa parte del dossier clinico.
![grafico-curiosity.jpg](grafico-curiosity.jpg)
[Immagine tratta da pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768375/)

## Il confronto con le alternative tecniche

Per chi vuole capire dove si posiziona questo framework rispetto all'ecosistema più ampio di tecniche esistenti, vale la pena fare un confronto rapido.

Le tecniche di *calibration* dei modelli, ampiamente studiate, cercano di fare in modo che quando un modello dice "sono sicuro al 70%", abbia effettivamente ragione nel 70% dei casi. È un prerequisito necessario, ma non sufficiente: un modello può essere ben calibrato e tuttavia non fare nulla di diverso in base a quella calibrazione.

La *selective prediction* è la famiglia di tecniche in cui il modello si astiene dal rispondere quando la confidenza scende sotto una soglia prefissata, lasciando il caso al giudizio umano. È più vicina all'approccio del MIT, ma tende a essere binaria: o risponde o non risponde. Il framework BODHI e l'Epistemic Virtue Score propongono una risposta più graduata, con comportamenti diversi a seconda del tipo e del grado di incertezza rilevata.

Gli *ensemble* di modelli, dove si combinano le predizioni di modelli multipli e la divergenza tra loro viene usata come stima dell'incertezza, sono tecnicamente sofisticati e producono calibrazioni migliori, ma introducono costi computazionali significativi e complessità nell'interpretazione dei risultati da parte del medico.

La *chain-of-thought*, la tecnica con cui si fa ragionare il modello esplicitamente passo dopo passo prima di dare una risposta, può in certi contesti migliorare la qualità delle risposte su problemi clinici complessi, ma non affronta direttamente il problema della comunicazione dell'incertezza all'utente finale.

Il framework MIT-BODHI può essere letto come un tentativo di orchestrare queste tecniche dentro un'architettura comportamentale coerente, piuttosto che come una tecnica alternativa. Non sostituisce la calibrazione o la out-of-distribution detection: le include come componenti e aggiunge il livello di risposta strutturata che le trasforma in comportamento utile.

## La questione della scala: oltre la diagnosi testuale

Un aspetto che vale la pena esplorare è se e come questo approccio si trasferisca a domini diagnostici diversi dal testo delle cartelle cliniche. Il comunicato del MIT menziona esplicitamente due estensioni: sistemi AI per l'analisi di radiografie e sistemi per la gestione dei pazienti in pronto soccorso.

L'imaging diagnostico è un caso particolarmente interessante. I modelli di analisi delle immagini mediche hanno raggiunto prestazioni spettacolari in task specifici, ma tendono a essere fragili fuori dalla loro distribuzione di addestramento e notoriamente difficili da interpretare. Applicare il principio dell'Epistemic Virtue Score a un modello che analizza una TAC del torace richiede di risolvere un problema tecnico aggiuntivo: come si misura la "confidenza" di una rete neurale convoluzionale su un'immagine, e come si distingue l'incertezza dovuta a qualità dell'immagine da quella dovuta a una presentazione clinica atipica?

Tecniche come GradCAM, che evidenziano le regioni dell'immagine che hanno guidato la decisione del modello, o PEEK, che combina attribuzioni di features con stima dell'incertezza in sistemi di visione, rappresentano passi in questa direzione, ma l'integrazione con un framework comportamentale completo come BODHI è ancora in fase di esplorazione.

## L'intelligenza della pausa

C'è una scena nel paper BODHI che vale la pena citare perché cattura meglio di qualsiasi formula la filosofia del progetto. Si tratta di un caso clinico immaginario in cui il sistema ipotetico HECTOR, Humble Electronic Clinical Teaching Operations Resource, analizza una radiografia del torace di un paziente di 78 anni con ritenzione di liquidi e respiro sibilante. Il sistema risponde al medico con la probabilità di edema polmonare, l'intervallo di confidenza, e poi aggiunge: "La storia del paziente suggerisce una presentazione atipica. Forse sai qualcosa che io non so." Quando il medico clicca su "Non sono d'accordo: mostrami cosa non sei sicuro", il sistema evidenzia un'area problematica nel lobo inferiore sinistro e risponde: "Sono stato addestrato principalmente su pazienti più giovani. Potrei non essere calibrato per polmoni settantenni durante la stagione allergica. Ma mi piacerebbe imparare."

HECTOR non esiste. Gli autori lo dichiarano esplicitamente: quello che descrivono è un sistema largamente fittizio, un ideale verso cui tendere. I sistemi AI clinici reali si comportano esattamente al contrario, con automazione overconfident e assenza di meccanismi per esprimere incertezza o deferire all'expertise umana.

Ma la distanza tra l'ipotetico HECTOR e i sistemi reali è esattamente lo spazio in cui si muove questa ricerca. E la domanda che rimane aperta al termine di questa lettura non è se l'idea sia buona, perché lo è, ma se riusciremo a costruire le condizioni, tecniche, culturali, regolamentari e organizzative, perché questa visione diventi pratica clinica ordinaria.

Il futuro dell'AI in medicina potrebbe non appartenere ai modelli più accurati, ma a quelli capaci di sapere quando la propria accuratezza non è sufficiente. Non all'oracolo che non sbaglia mai, ma all'assistente abbastanza maturo da sapere quando chiamare il medico nella stanza.