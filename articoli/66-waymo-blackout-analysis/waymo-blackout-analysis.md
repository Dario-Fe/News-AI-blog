---
tags: ["Security", "Ethics & Society", "Applications"]
date: 2025-12-26
author: "Dario Ferrero"
youtube_url: "https://youtu.be/0cNuMCfULHg?si=98MI49Vj4pMJglvA"
---

# Quando la città si ferma: le fragilità nascoste dell'età autonoma
![waymo-blackout-analysis.jpg](waymo-blackout-analysis.jpg)

*Il blackout di San Francisco ha paralizzato centinaia di robotaxi Waymo, rivelando la dipendenza critica dei sistemi autonomi dall'infrastruttura urbana. Mentre i data center AI raddoppiano il consumo elettrico e le tempeste solari minacciano le reti, emerge una domanda scomoda: stiamo progettando un futuro resiliente o costruendo castelli di carta tecnologica?*

Sabato 21 dicembre 2025, alle prime ore del pomeriggio, un incendio alla sottostazione elettrica di Pacific Gas & Electric nel quartiere di Bayview-Hunters Point ha fatto precipitare nel buio [oltre 130.000 utenze](https://techcrunch.com/2025/12/21/waymo-suspends-service-in-san-francisco-as-robotaxis-stall-during-blackout/) a San Francisco. I semafori si sono spenti, le luci delle case sono svanite, e qualcosa di inaspettatamente simbolico è accaduto sulle strade della città: decine di robotaxi Waymo si sono fermati, immobili agli incroci come automi privati dell'anima.

I video diffusi sui social media mostrano una scena che avrebbe fatto sorridere Philip K. Dick: le caratteristiche Jaguar I-Pace bianche e blu con i lampeggianti accesi, bloccate nel traffico mentre gli esseri umani alla guida delle loro vetture tradizionali le aggiravano con cautela. Alcuni guidatori hanno filmato robotaxi fermi nel bel mezzo della carreggiata, incapaci di decidere come proseguire. [Waymo ha dovuto sospendere il servizio](https://www.businessinsider.com/waymo-suspends-robotaxi-service-san-francisco-power-outage-tesla-2025-12) nell'intera area colpita, lasciando i passeggeri già a bordo a chiedersi cosa stesse accadendo.

Il contrasto con i veicoli Tesla equipaggiati con Full Self-Driving è stato stridente e immediato. Mentre le Waymo rimanevano paralizzate, le Tesla continuavano a circolare, sfruttando la loro architettura di elaborazione locale. L'episodio ha sollevato una domanda che risuona ben oltre le colline di San Francisco: se un'interruzione locale di corrente può paralizzare tecnologia definita "del futuro", quanto è davvero robusta l'infrastruttura su cui stiamo costruendo la mobilità autonoma?

## Il tallone d'Achille digitale

Per comprendere perché alcune auto autonome si fermano mentre altre continuano a muoversi, è necessario guardare sotto il cofano tecnologico. [Waymo basa la propria architettura](https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/) su un ecosistema complesso: sensori LIDAR che generano mappe tridimensionali dell'ambiente circostante, mappe HD centimetriche che devono essere aggiornate costantemente, e una comunicazione remota continua con i server centrali per elaborare i dati e prendere decisioni. Quando la corrente è mancata, non sono solo i semafori a spegnersi: anche le celle 5G, i ripetitori GPS e l'infrastruttura di comunicazione hanno subito interruzioni a catena.

Tesla, invece, adotta una filosofia radicalmente diversa. Il sistema Full Self-Driving elabora tutto localmente, affidandosi principalmente a telecamere e reti neurali che girano direttamente nel computer di bordo. Niente necessità di connessione costante, niente dipendenza da mappe esterne aggiornate in tempo reale. È come il contrasto tra un mainframe degli anni Settanta e un personal computer: centralizzazione contro elaborazione distribuita, cloud contro edge computing.

Il paradosso è affascinante quanto inquietante: [Waymo completa circa 450.000 corse settimanali](https://www.quattroruote.it/news/tecnologia/2025/12/22/san_francisco_waymo_robotaxi.html) a San Francisco, un'operazione su scala industriale che funziona magnificamente finché l'ecosistema regge. Ma quella stessa scala amplifica la vulnerabilità: più sofisticato è il sistema, più numerosi sono i punti di rottura. GPS, 5G, mappe cloud, alimentazione costante delle infrastrutture di supporto: quando uno di questi anelli si spezza, l'intera catena collassa.

Nel campo dell'agricoltura autonoma, questa lezione è stata appresa duramente. Durante le operazioni militari israeliane del 2023, [il jamming GPS deliberato dell'IDF](https://www.calcalistech.com/ctechnews/article/q9msjj6cb) ha costretto gli agricoltori a tornare ai metodi tradizionali. Rami Laner, 73 anni, è dovuto tornare al lavoro nei campi del kibbutz Mevo Hama dopo trent'anni di assenza, perché gli operatori più giovani non sapevano come guidare i trattori senza i sistemi GPS. Le piantagioni hanno subito sovrapposizioni di fertilizzanti e pesticidi, con danni alle colture e aumento dei costi. La precisione centimetrica che aveva reso l'agricoltura israeliana così efficiente si è rivelata un punto debole strutturale quando le coordinate satellitari sono diventate inaffidabili.

Anche i droni civili hanno mostrato fragilità simili. Le piattaforme DJI, ampiamente utilizzate in agricoltura, fotografia aerea e ispezioni industriali, [dipendono criticamente dal segnale GPS](https://forum.dji.com/thread-254715-1-1.html) per mantenere la stabilità e l'orientamento. Quando il segnale si degrada o scompare, i droni entrano in modalità ATTI (attitude mode), perdendo la capacità di mantenere la posizione fissa e diventando vulnerabili al vento e alle correnti. Diversi utenti hanno riportato situazioni critiche durante missioni di mapping o consegne, con droni che improvvisamente perdevano satelliti durante il volo e rischiavano collisioni.

## L'energia che non c'è

Ma il problema energetico non riguarda solo le interruzioni locali. Il consumo dei data center che alimentano i sistemi di intelligenza artificiale sta crescendo a una velocità vertiginosa. Secondo l'[International Energy Agency](https://www.punto-informatico.it/blackout-paralizza-self-driving-car-waymo/), il consumo elettrico dei data center è passato da 415 terawattora nel 2024 a una proiezione di 945 TWh entro il 2030: più del doppio in sei anni. Per fare un paragone, è come aggiungere il consumo elettrico dell'intera India al fabbisogno globale.

Il progetto Stargate di OpenAI in Texas richiederà 1,2 gigawatt di potenza, l'equivalente di un reattore nucleare di medie dimensioni. In Virginia, la cosiddetta Data Center Alley consuma già il 26% dell'elettricità dell'intero stato. Il Texas, che nel febbraio 2021 ha sperimentato [il blackout della tempesta Winter Storm Uri](https://nt24.it/2025/09/energia-ia-vertiv/) con oltre 4,5 milioni di utenze al buio e 246 morti, sta vedendo la propria rete elettrica stressata dai nuovi data center AI.

Il paradosso è lampante: la tecnologia che dovrebbe renderci più efficienti e sostenibili sta consumando energia come intere nazioni. E questo consumo non è distribuito uniformemente, ma concentrato in poche aree geografiche dove la densità di data center crea hotspot energetici. Quando queste aree subiscono stress sulla rete, non sono solo i sistemi locali a soffrire: l'intero cloud computing su cui si basano servizi autonomi, analisi predittive e elaborazioni AI remote può vacillare.

L'Italia stessa non è immune. Le previsioni indicano un [rischio crescente di blackout](https://prometeo.adnkronos.com/territorio/prossimo-blackout-previsioni-ai-dopo-spagna-2025/) per il 2026, amplificato dalla corsa all'installazione di infrastrutture AI. La cogenerazione e le micro-reti stanno diventando soluzioni sempre più discusse dalle imprese che vogliono proteggersi dalla vulnerabilità della rete nazionale.
![waymo.jpg](waymo.jpg)
[Immagine tratta techcrunch.com](https://techcrunch.com/2025/12/21/waymo-suspends-service-in-san-francisco-as-robotaxis-stall-during-blackout/)

## Tempeste dall'alto

Come se le fragilità terrestri non bastassero, il cielo stesso sta diventando una minaccia. Il Solar Cycle 25 ha raggiunto il suo picco tra il 2025 e il 2026, portando con sé [tempeste geomagnetiche di classe G4 e G5](https://congressiinternazionali.it/blog/tempesta-solare-2025-rischi-comunicazione-e-soluzioni/). A novembre 2024, una tempesta G4 ha prodotto aurore visibili fino in Alabama, uno spettacolo magnifico che però ha nascosto problemi significativi ai sistemi GPS e alle comunicazioni radio in alta frequenza.

Il precedente storico più drammatico è l'Evento di Carrington del 1859, quando una tempesta solare eccezionale produsse aurore visibili fino ai Caraibi e mise fuori uso le linee telegrafiche in tutto il Nord America ed Europa. Gli operatori riportarono scintille che incendiavano la carta nei loro uffici, e alcuni sistemi telegrafici continuarono a funzionare anche dopo essere stati scollegati dalle batterie, alimentati solo dalle correnti indotte geomagneticamente.

Oggi, un evento di quella portata sarebbe catastrofico. Lo United States Geological Survey avverte che il Midwest e la costa est degli Stati Uniti sono [particolarmente vulnerabili](https://www.smartphonology.it/i-grandi-blackout-digitali-del-2025-quando-le-piattaforme-globali-si-fermano/) alle correnti geomagneticamente indotte (GIC) che possono danneggiare irreparabilmente i trasformatori ad alta tensione. Non si tratta di spegnere e riaccendere un interruttore: un trasformatore bruciato può richiedere mesi per essere sostituito, essendo componenti enormi, costosi e prodotti su ordinazione.

Per i sistemi autonomi che dipendono dal GPS, le tempeste solari rappresentano una minaccia esistenziale. Le particelle cariche distorcono la ionosfera, rendendo inaffidabili i segnali satellitari. I droni perdono l'orientamento, i trattori autonomi escono dalle file, i robotaxi non sanno più dove si trovano. E contrariamente ai blackout terrestri che possono essere circoscritti geograficamente, una tempesta solare colpisce intere regioni planetarie simultaneamente.

## Il mondo che si adatta alle macchine

C'è però una questione più profonda e filosofica che emerge da questi episodi di fragilità tecnologica. Invece di progettare sistemi che si adattano al mondo umano con tutte le sue imperfezioni e imprevedibilità, stiamo progressivamente modificando città e infrastrutture per accogliere tecnologie rigide che funzionano solo in condizioni ideali.

San Francisco sta investendo milioni in infrastrutture V2X (vehicle-to-everything), semafori intelligenti che comunicano con i veicoli autonomi, corsie dedicate e sensori stradali. È un retrofitting urbano su scala miliardaria per permettere ai robotaxi di muoversi in sicurezza. Ma questa strategia rovescia il paradigma tradizionale dell'ingegneria: non sono le macchine ad adattarsi all'ambiente, ma l'ambiente che viene rimodellato per le macchine.

La storia della Cruise a San Francisco ne è un esempio emblematico. Nell'ottobre 2023, la California DMV ha [sospeso le operazioni](https://www.punto-informatico.it/blackout-paralizza-self-driving-car-waymo/) della compagnia dopo che un robotaxi aveva trascinato un pedone per sei metri dopo un incidente, incapace di riconoscere che la persona era rimasta incastrata sotto il veicolo. L'episodio ha sollevato domande scomode sulla capacità di questi sistemi di gestire situazioni inaspettate che un guidatore umano riconoscerebbe immediatamente.

La sociologa M.C. Elish ha coniato il termine "moral crumple zone" per descrivere come gli esseri umani nei sistemi semi-autonomi diventino i capri espiatori quando qualcosa va storto. Nell'aviazione, quando un pilota non interviene tempestivamente per correggere un errore dell'autopilota, viene incolpato per non aver supervisionato adeguatamente il sistema. Ma se il sistema è progettato per funzionare autonomamente il 99% del tempo, come può un essere umano mantenere l'attenzione necessaria per intervenire nell'1% critico?

Il filosofo della tecnologia Luciano Floridi ha argomentato che abbiamo bisogno di un approccio "green and blue": tecnologia che rispetta sia l'ambiente naturale (green) sia l'ambiente sociale e umano (blue). La tentazione di ridisegnare il mondo per adattarlo ai limiti dei nostri algoritmi è forte, ma rischia di creare ecosistemi urbani sempre più fragili e dipendenti da condizioni perfette.

L'agricoltura autonoma, con la sua dipendenza da GPS centimetrico e connettività costante, funziona magnificamente nei campi aperti del Kansas o dell'Iowa, ma fallisce non appena le condizioni deviano dalla norma. I trattori autonomi [richiedono segnali GPS con precisione di tre centimetri](https://guidenav.com/handling-gnss-outages-in-agricultural-robots-ins-dead-reckoning-strategies/), impossibile da mantenere sotto coperture vegetali dense o vicino a strutture metalliche. Il risultato è che alcune coltivazioni specializzate, come i vigneti e i frutteti con file strette, rimangono difficili da automatizzare completamente.

## Scenari futuri e soluzioni

Eppure non tutto è perduto, e guardare solo ai fallimenti sarebbe riduttivo. Tesla ha dimostrato che architetture diverse possono offrire resilienza maggiore. L'edge computing ibrido, che bilancia elaborazione locale con supporto cloud quando disponibile, rappresenta una via di mezzo promettente. I sistemi agricoli più avanzati stanno già implementando [sistemi inerziali di navigazione](https://guidenav.com/handling-gnss-outages-in-agricultural-robots-ins-dead-reckoning-strategies/) (INS) che permettono di continuare a operare durante interruzioni GPS temporanee, sfruttando accelerometri e giroscopi per stimare posizione e orientamento.

La regolamentazione sta lentamente adattandosi alla realtà. La California Department of Motor Vehicles ha dimostrato di essere disposta a sospendere operazioni quando i problemi di sicurezza diventano evidenti, come nel caso di Cruise nel 2023 e ora con le interruzioni Waymo. L'Unione Europea sta sviluppando standard che includono test di resilienza in condizioni degradate, non solo prestazioni in scenari ideali.

Ma serve un cambio di prospettiva più radicale. I test obbligatori dovrebbero includere blackout simulati, jamming GPS, interruzioni di connettività 5G. Non possiamo permetterci di scoprire le vulnerabilità quando centinaia di migliaia di veicoli autonomi sono già sulle strade e milioni di ettari agricoli dipendono da trattori senza pilota.

Il ridisegno urbano deve essere olistico, non centrato sulla tecnologia. Le città del futuro avranno sì corsie per veicoli autonomi, ma anche ridondanza nelle infrastrutture critiche: micro-reti elettriche distribuite, generazione locale di backup, sistemi di comunicazione multi-path che non dipendono da una singola tecnologia. I robotaxi dovranno essere progettati per degradare con grazia, come gli aerei commerciali che hanno sistemi tripli e quadrupli per ogni funzione critica.

L'esperienza del [blackout CrowdStrike di luglio 2024](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages) offre una lezione cruciale: 8,5 milioni di computer Windows messi fuori uso da un singolo aggiornamento software difettoso, con danni stimati in oltre 10 miliardi di dollari. Aeroporti fermi, ospedali costretti a tornare alla carta, banche bloccate. Il sistema aveva un punto di rottura singolo, e quando si è rotto, le conseguenze sono state globali. La diversificazione tecnologica non è solo una questione di efficienza, ma di sopravvivenza sistemica.

## Epilogo incompiuto

Le Waymo ferme agli incroci di San Francisco non sono state solo un inconveniente temporaneo per i passeggeri di quei robotaxi. Sono state uno specchio che riflette le fragilità nascoste in un futuro che credevamo fosse già solido. Come nel videogioco "The Last of Us", dove la civiltà tecnologica crolla in pochi giorni quando i sistemi complessi si spezzano, stiamo costruendo un mondo dove la complessità interconnessa può trasformarsi rapidamente in vulnerabilità sistemica.

La domanda non è se ci saranno altri blackout, altre tempeste solari, altre interruzioni. La domanda è: quando arriveranno, avremo costruito sistemi abbastanza robusti da degradare con grazia invece di crollare completamente? La tecnologia autonoma promette efficienza, sicurezza, sostenibilità. Ma quelle promesse valgono solo se i sistemi funzionano anche quando le condizioni sono imperfette, quando la corrente manca, quando il GPS è distorto, quando il mondo reale si rifiuta di conformarsi ai parametri ottimali dei nostri algoritmi.

Forse la vera intelligenza artificiale non sarà quella che funziona perfettamente in condizioni perfette, ma quella che sa adattarsi, improvvisare e sopravvivere quando tutto il resto fallisce. Proprio come gli esseri umani hanno sempre fatto.