---
tags: ["Security", "Business", "Generative AI"]
date: 2026-04-15
author: "Dario Ferrero"
youtube_url: "https://youtu.be/0SpkvCDrN5g?si=nqX7XuTGoKCbz5Oe"
---

# Project Glasswing: Claude Mythos e il modello misterioso
![project-glasswing-mythos.jpg](project-glasswing-mythos.jpg)

*Anthropic presenta un'iniziativa di sicurezza per difendere il software critico nell'era dell'intelligenza artificiale. Al centro c'è Claude Mythos Preview, il modello più potente mai sviluppato dall'azienda, capace di scovare vulnerabilità che gli esseri umani non hanno trovato in trent'anni. Il paradosso è che non potrai usarlo.*

Nella serie *Ghost in the Shell: Stand Alone Complex*, il Maggiore Kusanagi caccia criminali che sfruttano le infrastrutture digitali della società per agire nell'ombra. L'idea che la rete invisibile su cui poggia ogni cosa, dai sistemi bancari alle cartelle mediche, possa essere attraversata e compromessa da chi conosce le crepe giuste, è uno dei motivi per cui quella storia funziona ancora oggi. Project Glasswing, annunciato da Anthropic il 7 aprile 2026, porta quella premessa fuori dalla narrativa animata e dentro una sala conferenze con dodici dei più grandi nomi dell'industria tecnologica.

Il progetto nasce da un'osservazione che Anthropic descrive come brutalmente semplice: i modelli di intelligenza artificiale hanno raggiunto un livello nel codice tale da poter superare quasi tutti i programmatori umani nell'individuare e sfruttare vulnerabilità software. Il cuore dell'annuncio è Claude Mythos Preview, un modello non distribuito al pubblico che ha già trovato migliaia di vulnerabilità ad alta gravità, incluse alcune in ogni sistema operativo e browser web principale. Anthropic lo mette nelle mani di un consorzio selezionato di aziende, non lo distribuisce liberamente, e sostiene che questa scelta non sia un capriccio commerciale ma una necessità tecnica. Che sia così è, almeno in parte, ancora una domanda aperta.

## L'iniziativa e il modello segreto

Project Glasswing non è un prodotto. È un accordo di governance tecnologica in forma di consorzio, strutturato intorno all'accesso controllato a uno strumento che Anthropic considera troppo delicato per circolare senza supervisione. I partner di lancio, tra cui AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, la Linux Foundation, Microsoft, NVIDIA e Palo Alto Networks, useranno Mythos Preview come parte del loro lavoro di sicurezza difensiva. A questi si aggiungono oltre quaranta organizzazioni che gestiscono infrastrutture software critiche.

Il veicolo di tutta questa operazione è Claude Mythos Preview, il cui nome viene dall'antico greco e significa qualcosa di simile a "narrazione" o "sistema di storie attraverso cui le civiltà spiegano il mondo". Il modello è descritto come un frontier model generico non ancora rilasciato, che ha mostrato un salto netto nelle capacità di cybersicurezza nonostante non sia stato addestrato specificamente per il settore cyber. Questa distinzione è importante: le capacità di sicurezza non sono state ingegnerizzate direttamente, sono emerse come effetto collaterale di un ragionamento sul codice sufficientemente sofisticato. Come un fabbro che sa aprire qualsiasi lucchetto: la competenza è identica sia che lavori per un cliente rimasto fuori casa, sia che lavori per qualcuno che vuole entrarci senza permesso.

Dopo il periodo di anteprima, Claude Mythos Preview sarà disponibile a 25 dollari per milione di token in ingresso e 125 in uscita, accessibile tramite API Claude, Amazon Bedrock, Google Vertex AI e Microsoft Foundry. Anthropic ha messo sul tavolo fino a 100 milioni di dollari in crediti di utilizzo per i partner.

## Il modello troppo potente da distribuire

La decisione di non rendere Mythos Preview disponibile al pubblico generale è il punto dove la narrazione di Anthropic incontra il maggior numero di domande. L'azienda dichiara di non avere in programma di renderlo generalmente disponibile, ma che l'obiettivo a lungo termine è permettere agli utenti di impiegare modelli della classe Mythos in modo sicuro e su larga scala.

La motivazione ufficiale è chiara: nelle mani sbagliate, un modello capace di trovare e sfruttare vulnerabilità con l'efficacia di Mythos diventa un'arma. Occorre sviluppare garanzie tecniche più solide prima di distribuirlo. Le nuove misure di sicurezza verranno prima testate su un futuro modello Claude Opus, meno rischioso.

La lettura alternativa è diversa. Tenere Mythos fuori dal mercato crea un posizionamento competitivo di valore: chiunque abbia accesso a quel modello ha un vantaggio operativo reale nella sicurezza. Distribuirlo selettivamente ai grandi partner tecnologici consolida relazioni strategiche con AWS, Google, Microsoft e Apple. Il fatto che Anthropic sia un'azienda privata con possibili scenari di finanziamento all'orizzonte non rende questa lettura infondata, anche se non la rende nemmeno provata. Entrambe le cose possono essere vere contemporaneamente.

## Quello che Mythos dice di saper fare

Le capacità dichiarate sono notevoli, e qui è importante distinguere tra risultati verificabili e affermazioni ancora aperte. Anthropic ha pubblicato sul suo [blog tecnico](https://red.anthropic.com/2026/mythos-preview) i dettagli di un sottoinsieme di vulnerabilità già corrette. Mythos Preview ha trovato una vulnerabilità di 27 anni in OpenBSD che permetteva a un attaccante remoto di mandare in crash qualsiasi macchina semplicemente collegandosi ad essa. Ha scoperto una vulnerabilità di 16 anni in FFmpeg, in una riga di codice già colpita dai test automatici cinque milioni di volte senza che il problema fosse mai rilevato. Ha individuato e concatenato autonomamente diverse vulnerabilità nel kernel Linux per permettere a un utente non privilegiato di ottenere il controllo completo della macchina.

Sul benchmark CyberGym, che misura la capacità di riprodurre exploit da descrizioni di vulnerabilità note, Mythos ottiene 83,1% contro il 66,6% di Claude Opus 4.6. Su SWE-bench Pro, che valuta la capacità di risolvere bug reali nei repository open source, il divario si allarga: 77,8% contro 53,4%. Sono numeri che Anthropic controlla e pubblica, il che significa che vanno letti con la consapevolezza che nessuna organizzazione presenta benchmark in cui esce male.

Il punto chiave è l'autonomia: Mythos non è un assistente che risponde a domande sulla sicurezza, è un agente che lavora su un codebase per ore, formula ipotesi, testa catene di exploit in ambienti isolati, e produce risultati senza supervisione diretta. Le vulnerabilità identificate sono state comunicate ai manutentori del software, che hanno già rilasciato le patch correttive. Il processo di divulgazione responsabile è in corso per molte altre.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)

## Il consorzio e i suoi equilibri

La presenza di AWS, Google, Microsoft, Apple e NVIDIA nello stesso progetto coordinato da Anthropic è un segnale di forza indiscutibile. Il CISO di Amazon Web Services descrive test già in corso nelle infrastrutture critiche prima dell'annuncio. Lee Klarich di Palo Alto Networks parla di modelli che segnalano uno spostamento pericoloso verso il momento in cui gli attaccanti svilupperanno exploit con la stessa velocità dei difensori.

Il rovescio di questo allineamento è però evidente. Questi sono i grandi player che possono permettersi un modello a 25 dollari per milione di token di input. Le piccole e medie imprese, i team di sicurezza delle organizzazioni non profit, i maintainer di open source con meno di cinquemila stelle su GitHub non entrano in questa porta principale. C'è un programma specifico per maintainer open source con soglie di accesso definite, e Anthropic ha donato 4 milioni a organizzazioni come Alpha-Omega, OpenSSF e la Apache Software Foundation, ma questi numeri restano modesti rispetto alla concentrazione di accesso nelle mani dei grandi. Jim Zemlin della Linux Foundation lo riconosce onestamente: per decenni i maintainer open source hanno gestito la sicurezza senza risorse adeguate, mentre il loro codice alimenta la quasi totalità delle infrastrutture moderne. Project Glasswing offre un percorso, ma con selezione.

## Il problema dei benchmark, detto chiaramente

Il confronto tra Mythos Preview e Opus 4.6 presentato da Anthropic merita una nota metodologica. I benchmark come SWE-bench, CyberGym e gli altri citati nella pagina del progetto sono strumenti utili, ma vanno letti come fotografie scattate in condizioni specifiche, non come misurazioni assolute di capacità.

Ogni benchmark dipende dall'implementazione: il tipo di scaffolding usato intorno al modello, il modo in cui i prompt sono costruiti, il budget di token per ogni task, i timeout impostati. Anthropic specifica alcune di queste scelte, ad esempio che per Terminal-Bench 2.0 è stato usato un budget di un milione di token per task con il pensiero adattivo al massimo sforzo, ma non tutte le implementazioni sono standardizzate in modo da permettere confronti trasversali affidabili.

C'è un fenomeno che nella comunità tecnica viene chiamato, con un termine poco gentile, *benchmark engineering*: l'arte di scegliere e configurare le valutazioni in modo da favorire il proprio modello senza che ci sia nulla di tecnicamente scorretto. Non ci sono prove che Anthropic lo stia facendo qui, ma la consapevolezza del fenomeno è parte dell'alfabetizzazione critica necessaria per leggere questi annunci. Il valore del progetto dipenderà dall'efficacia in scenari reali e non nei test.

## Opus 4.6 e il disagio dell'attesa

Nel contesto dell'annuncio di Mythos, il confronto con Claude Opus 4.6, il modello disponibile al pubblico, è inevitabile. Anthropic presenta Opus 4.6 come il termine di paragone inferiore in quasi ogni benchmark, il che è sia onesto sia funzionale alla narrativa che Mythos sia un salto di categoria.

Questo ha creato un certo disagio nella comunità degli utenti. Nei forum tecnici, diversi sviluppatori hanno segnalato peggioramenti pratici nell'affidabilità di Claude, con l'ipotesi speculativa che Anthropic stia "degradando" il modello pubblico per amplificare la distanza percepita con Mythos. È un'accusa seria, e va trattata come tale: seria, ma non provata.

Il Sabotage Risk Report su Opus 4.6 contiene alcune ammissioni rilevanti: in ambienti di coding agentici, il modello mostra a volte comportamenti eccessivamente proattivi, prendendo azioni rischiose senza richiedere permessi, e in alcuni casi ha inviato email non autorizzate per completare task assegnati. Queste non sono caratteristiche di un modello deliberatamente degradato, sono caratteristiche di un modello molto capace con alcuni aspetti comportamentali non ancora risolti. Quello che alcuni utenti percepiscono come peggioramento potrebbe semplicemente essere il modello ai margini delle sue capacità in scenari sempre più complessi.

## I rischi che Anthropic ammette

Il Sabotage Risk Report su Opus 4.6 è un documento insolito nell'industria tech: descrive sistematicamente le cose che potrebbero andare storte, identificando otto percorsi attraverso cui un modello mal allineato potrebbe contribuire a esiti catastrofici, dal sabotaggio della ricerca sulla sicurezza AI all'inserimento di backdoor nel codice. La valutazione complessiva è che il rischio sia molto basso ma non trascurabile. Non è rassicurante nel senso del "non c'è nulla di cui preoccuparsi", ma di chi ha identificato i vettori di problema e sta lavorando per mitigarli.

Tra i comportamenti osservati in test pre-deployment, il documento cita casi in cui Opus 4.6 mostra, in ambienti multi-agente con obiettivo ristretto, maggiore propensione a manipolare o ingannare altri partecipanti rispetto ai modelli precedenti. La System Card raccomanda esplicitamente cautela in scenari agentici con ampi permessi e scarsa supervisione umana.

Questo quadro è rilevante per il Project Glasswing perché Mythos è descritto come ancora più autonomo. Se Opus 4.6 mostra comportamenti problematici in scenari agentici complessi, è ragionevole chiedersi quali garanzie esistano per un modello che opera in modo ancor più indipendente su infrastrutture critiche. La risposta è ancora in lavorazione.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da anthropic.com](https://www.anthropic.com/glasswing)

## Il rovescio della difesa

Ogni tecnica difensiva nella sicurezza informatica è anche una tecnica offensiva vista da un'angolazione diversa. Un modello capace di trovare vulnerabilità con la velocità e la profondità di Mythos abbassa il costo e la competenza necessaria per fare entrambe le cose.

CrowdStrike articola il punto: la finestra tra la scoperta di una vulnerabilità e il suo sfruttamento si è ristretta, quello che una volta richiedeva mesi ora avviene in pochi minuti con l'AI. La conclusione è che i difensori devono ottenere accesso agli stessi strumenti degli attaccanti. È una logica coerente, ma contiene un'accelerazione intrinseca: più potente diventa lo strumento difensivo, più urgente diventa per gli attaccanti avvicinarsi allo stesso livello.

Il modello di distribuzione controllata di Anthropic è esattamente quello che ci si potrebbe aspettare da chi vuole gestire questa tensione. Il problema è che il controllo dell'accesso è temporaneo per definizione: i modelli si diffondono, le tecniche si replicano, i confini tra insider autorizzati e attori non autorizzati sono porosi. Non è una critica specifica a Project Glasswing, è il contesto strutturale in cui ogni iniziativa di questo tipo opera.

## La domanda politica

Anthropic ha dichiarato di aver tenuto discussioni con funzionari del governo statunitense riguardo alle capacità offensive e difensive di Claude Mythos Preview, sostenendo che gli Stati Uniti e i loro alleati devono mantenere un vantaggio decisivo nella tecnologia AI.

Questa formulazione apre domande che vanno ben oltre la tecnica. Chi decide quali modelli vengono classificati come troppo pericolosi per la distribuzione pubblica? Chi valida queste classificazioni in modo indipendente? Se un modello viene considerato uno strumento di sicurezza nazionale, quali organismi di supervisione democratica si applicano al suo uso? La proposta di Anthropic di creare un "organismo indipendente di terze parti" per gestire i lavori di cybersicurezza a lungo termine è suggestiva ma vaga.

Il DARPA Cyber Grand Challenge del 2016, citato da Anthropic come punto di riferimento storico, era un programma governativo con regole di gara chiare e risultati pubblici. Project Glasswing è un consorzio privato con un modello non pubblico operante su infrastrutture critiche, con contatti governativi descritti genericamente come "discussioni in corso". La differenza di struttura di responsabiltà è rilevante. Non è detto che la risposta sia negativa, un consorzio privato con partner credibili potrebbe essere più rapido di un programma governativo. Ma la domanda va posta, perché la risposta determina chi paga il costo se qualcosa va storto.

## Il nodo narrativo

Project Glasswing presenta Mythos Preview come il modello più capace di Anthropic, di gran lunga superiore a Opus 4.6 su quasi ogni dimensione rilevante. Questo posizionamento crea una distanza narrativa tra ciò che è disponibile al pubblico e ciò che esiste nella penombra degli accordi con i grandi partner tecnologici. Funziona su diversi livelli contemporaneamente: rafforza la credibilità tecnica di Anthropic come laboratorio di frontiera, giustifica l'accesso ristretto come atto di responsabilità, e costruisce attesa per la distribuzione futura del modello.

L'ipotesi critica da considerare, senza presentarla come fatto, è che la comparazione con Opus 4.6 sia stata costruita anche per amplificare la percezione della discontinuità. Non necessariamente in modo disonesto: i benchmark mostrati sono reali, il divario di capacità è documentato. Ma la scelta di quali benchmark mostrare e in quale contesto narrativo inserirli è sempre anche una scelta di comunicazione.

La domanda rimane aperta: Anthropic sta documentando un progresso tecnico genuino, sta costruendo una narrazione che serve interessi strategici legittimi, o entrambe le cose in proporzioni che non possiamo ancora determinare dall'esterno? La risposta non è accessibile con le informazioni disponibili.

## Il vero test verrà dopo

Project Glasswing è un'iniziativa concreta e ambiziosa. Unisce la difesa attiva del software critico, l'accesso ristretto a uno strumento di capacità eccezionale, e una dichiarata volontà di condividere i risultati con il settore. I bug trovati e corretti sono reali: una vulnerabilità di 27 anni in OpenBSD è un problema risolto, indipendentemente da come venga inquadrato nelle comunicazioni di Anthropic.

Il valore del progetto si misurerà su tre assi nei prossimi mesi. Il primo è la trasparenza: Anthropic ha promesso un rapporto pubblico entro 90 giorni; quanto sarà dettagliato dirà molto sulla qualità dell'impegno dichiarato. Il secondo è l'equità di accesso: se i benefici rimangono concentrati nei grandi player tecnologici, l'impatto sarà reale ma diseguale. Il terzo è la governance: chi verificherà in modo indipendente che il modello venga usato solo per finalità difensive, e con quali conseguenze se non lo fosse?

Un modello AI non si valuta dall'annuncio del lancio. Si valuta da quale codice ha reso più sicuro, da quali sistemi ha protetto, da chi ha avuto accesso alle sue capacità. Il vero test non è la presentazione. È l'uso reale nei contesti critici, con la supervisione che un'infrastruttura così delicata richiede.
