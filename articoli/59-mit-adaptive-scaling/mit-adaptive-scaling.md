---
tags: ["Research", "Generative AI", "Training"]
date: 2025-12-10
author: "Dario Ferrero"
youtube_url: "https://youtu.be/Ls-8wIkZnIo?si=mYQFAz7nICE0cpVn"
---

# Dal MIT, i Modelli Imparano a Pensare Meno (e Meglio)
![mit-adaptive-scaling.jpg](mit-adaptive-scaling.jpg)

*Un nuovo [studio MIT](https://www.arxiv.org/pdf/2506.09338) rivela come gli LLM possano regolare dinamicamente le risorse computazionali, risolvendo problemi complessi con metà del calcolo tradizionale. C'è un paradosso che definisce l'intelligenza artificiale contemporanea. I modelli linguistici più avanzati affrontano ogni domanda con lo stesso identico sforzo computazionale, che si tratti di calcolare quanto fa due più due o di dimostrare un teorema di topologia algebrica. È come se un grande matematico impiegasse la stessa energia mentale per dire che ore sono e per risolvere la congettura di Poincaré.*

Noi umani non funzioniamo così: Daniel Kahneman lo ha documentato magistralmente descrivendo come il nostro cervello passi fluidamente tra System 1, veloce e intuitivo, e System 2, lento e deliberato. Ora i ricercatori del MIT hanno trovato un modo per insegnare agli LLM questa stessa capacità di modulazione.

## Il Budget Fisso che Spreca Risorse

L'approccio attuale all'inference-time scaling permette ai modelli linguistici di "ragionare più a lungo" su problemi difficili. Il meccanismo è semplice: invece di generare una sola risposta, il modello esplora molteplici percorsi di ragionamento, genera soluzioni parziali diverse, le valuta e seleziona le più promettenti. Pensatelo come un albero decisionale dove ogni ramo rappresenta una possibile strada verso la soluzione. Più rami esplorate, maggiori le chance di trovare quella giusta.

Il problema è che [questi sistemi assegnano un budget computazionale fisso](https://news.mit.edu/2025/smarter-way-large-language-models-think-about-hard-problems-1204) a prescindere dalla complessità della domanda. È come dare a uno studente sempre esattamente un'ora per ogni compito, che sia una moltiplicazione elementare o un'equazione differenziale. Il risultato è doppiamente inefficiente: si sprecano risorse preziose su problemi banali e si lascia il modello in balia di sé stesso quando la difficoltà sale.

Nei mesi scorsi abbiamo già raccontato come la ricerca stia esplorando alternative a questa rigidità. [Power Sampling di Harvard](https://aitalk.it/it/power-sampling.html) ha dimostrato che algoritmi di campionamento più sofisticati possono estrarre capacità di ragionamento già latenti nei modelli base, senza bisogno di training aggiuntivo. Ma quella tecnica opera comunque con un numero fisso di iterazioni MCMC. L'innovazione del MIT va oltre: introduce un sistema che adatta dinamicamente non solo come il modello ragiona, ma quanto ragiona.

## Come Funziona l'Adaptive Scaling

La tecnica sviluppata dal team guidato da Navid Azizan del Laboratory for Information and Decision Systems si chiama "instance-adaptive scaling" ed è concettualmente elegante. Il sistema valuta continuamente due cose: quanto è difficile il problema che sta affrontando e quanto sono promettenti le soluzioni parziali che ha generato finora. In base a queste valutazioni, decide al volo se investire più risorse computazionali o fermarsi.

"È esattamente come gli umani risolvono problemi", spiega Hao Wang, uno degli autori della ricerca. "Elaboriamo alcune soluzioni parziali e poi decidiamo: dovrei continuare con una di queste, fermarmi e rivedere il ragionamento, o addirittura tornare indietro e riprendere da un passo precedente?".

Il cuore del sistema è un componente chiamato Process Reward Model, o PRM. Immaginate un supervisore interno che osserva il modello mentre lavora. Ad ogni passo del ragionamento, il PRM esamina la domanda originale e tutte le soluzioni parziali generate finora, assegnando a ciascuna un punteggio che stima quanto sia probabile che quella strada porti alla risposta corretta. Se il modello si trova su un percorso molto promettente, può ridurre il numero di alternative da esplorare, risparmiando calcolo. Se invece tutte le strade sembrano poco convincenti, alloca più risorse per cercare vie d'uscita migliori.

La differenza rispetto ai sistemi precedenti è che questa valutazione non avviene una volta sola all'inizio, ma continuamente durante tutto il processo di risoluzione. "La bellezza del nostro approccio", nota Kristjan Greenewald del MIT-IBM Watson AI Lab, "è che l'adattamento avviene al volo, mentre il problema viene risolto, invece che tutto in una volta all'inizio del processo".
![figura1.jpg](figura1.jpg)
[Immagine tratta dal paper ufficiale](https://www.arxiv.org/pdf/2506.09338)

## Il Problema della Sovrastima

Ma c'è un ostacolo tecnico fondamentale che i ricercatori hanno dovuto affrontare: i Process Reward Model esistenti sono terribilmente ottimisti. Sovrastimano sistematicamente le probabilità di successo, un po' come un GPS che vi dice "sei quasi arrivato" quando in realtà mancano ancora venti chilometri. Se il sistema si fidasse ciecamente di questi giudizi, ridurrebbe il budget computazionale troppo aggressivamente, convincendosi che la strada è facile quando invece è insidiosa.

Young-Jin Park, primo autore dello studio, descrive così il dilemma: "Se ci limitassimo a fidarci dei PRM attuali, che spesso sovrastimano le chance di successo, il nostro sistema ridurrebbe il budget computazionale in modo troppo aggressivo. Quindi abbiamo dovuto trovare un modo per calibrare meglio i PRM e rendere l'inference-time scaling più efficiente e affidabile".

La soluzione MIT è matematicamente raffinata ma concettualmente accessibile. Invece di far generare al PRM un singolo numero come stima di probabilità, il sistema produce un range di valori possibili attraverso una tecnica chiamata quantile regression. In pratica, il modello dice "la probabilità di successo è da qualche parte tra il 30% e il 70%" invece di "la probabilità è esattamente il 50%". Questa incertezza esplicita permette al sistema di prendere decisioni più prudenti e realistiche.

Il collegamento con ricerche precedenti è illuminante. Abbiamo già discusso come [DeepConf di Meta](https://aitalk.it/it/ai-deepconf) sfrutti la confidenza intrinseca dei modelli per l'auto-correzione, e come il [TRM di Samsung](https://aitalk.it/it/trm-samsung.html) usi il retrieval esterno per migliorare l'affidabilità fattuale. Tutte queste tecniche condividono un assunto: i modelli devono imparare a misurare quanto sono sicuri delle proprie risposte. Il MIT porta questa idea nel dominio del ragionamento matematico, dove la verifica può essere algoritmica ma la calibrazione della confidenza resta cruciale.

## I Risultati che Convincono

I benchmark non lasciano spazio a dubbi. Su una serie di task matematici standard, il sistema MIT ha utilizzato circa la metà del calcolo richiesto dagli approcci tradizionali, mantenendo lo stesso livello di accuratezza. Ma c'è un risultato ancora più interessante: modelli più piccoli e meno resource-intensive, equipaggiati con questa tecnica, hanno performato allo stesso livello o addirittura meglio di modelli molto più grandi su problemi complessi.

Pensate alle implicazioni. Un modello da sette miliardi di parametri che costa poco da far girare e consuma poca energia può, se usato intelligentemente, competere con giganti da settanta miliardi su problemi che richiedono ragionamento profondo. Non perché il modello piccolo sia magicamente diventato più intelligente, ma perché ha imparato a concentrare le sue risorse limitate dove servono davvero.

Questo è particolarmente rilevante nel contesto del [ragionamento a tempo di test](https://aitalk.it/it/articolo-hrm.html), dove abbiamo visto come l'allocazione intelligente delle risorse computazionali stia emergendo come frontiera chiave dell'AI. Il MIT suggerisce che il futuro non è necessariamente fare modelli sempre più grandi, ma insegnare a quelli esistenti quando vale la pena pensare a lungo e quando una risposta rapida è sufficiente.
![figura2.jpg](figura2.jpg)
[Immagine tratta dal paper ufficiale](https://www.arxiv.org/pdf/2506.09338)

## Applicazioni Concrete e Prospettive

Le ricadute pratiche sono immediate. La generazione di codice è un candidato naturale: alcuni problemi di programmazione sono banali sintattici, altri richiedono ragionamento algoritmico complesso. Un sistema che riconosce questa differenza e si comporta di conseguenza può drasticamente ridurre i costi operativi per servizi come GitHub Copilot o Cursor.

Gli agenti AI autonomi sono l'altro terreno fertile. Un agente che debba navigare situazioni del mondo reale deve costantemente decidere quanto "pensare" prima di agire. Fermarsi troppo a lungo su decisioni semplici lo rende goffo e inefficiente. Agire troppo in fretta su scelte complesse lo porta all'errore. Il framework MIT fornisce esattamente il meccanismo di meta-cognizione necessario: la capacità di valutare quanto è difficile la situazione e allocare tempo di riflessione di conseguenza.

Navid Azizan sottolinea che la recente release di GPT-5.1 evidenzia l'efficacia di questo approccio di "adaptive reasoning" proposto dal paper. "Dotando i modelli della capacità di sapere ciò che non sanno, possiamo permettere loro di spendere più calcolo sui problemi più difficili e sui percorsi di soluzione più promettenti, usando molti meno token su quelli facili. Questo rende il ragionamento sia più affidabile che molto più efficiente".

## I Limiti da Non Ignorare

Ma sarebbe ingenuo ignorare le sfide ancora aperte. Il sistema funziona egregiamente su domini dove la verifica è algoritmica, come matematica o coding. Ma cosa succede quando la "correttezza" è sfumata o soggettiva? Come valuta un PRM quanto è promettente una soluzione parziale a un problema di design creativo o di decisione etica complessa?

E poi c'è la questione delle allucinazioni, il tallone d'Achille di tutti i modelli linguistici. Un sistema che decide autonomamente quanto ragionare può, paradossalmente, diventare più pericoloso se la sua confidenza è mal calibrata. Potrebbe convincersi rapidamente di avere ragione proprio quando invece sta generando output completamente inventati. Per questo la calibrazione del PRM non è un dettaglio tecnico ma una necessità assoluta.

I ricercatori sono trasparenti sui prossimi passi. Vogliono testare la tecnica su applicazioni più ampie e esplorare ulteriori usi del metodo di calibrazione, incluso il reinforcement learning e il fine-tuning. L'intuizione di fondo, però, è già chiara: un modello che impara a dosare il proprio sforzo cognitivo è più vicino a qualcosa che potremmo chiamare intelligenza flessibile.

Akash Srivastava di IBM Software, non coinvolto nella ricerca, la mette in prospettiva industriale: "I dipendenti umani imparano sul lavoro, alcuni CEO sono partiti da stagisti, ma gli agenti di oggi rimangono largamente pezzi di software probabilistico statici. Lavori come questo paper sono un passo importante per cambiare ciò: aiutare gli agenti a capire cosa non sanno e costruire meccanismi per il miglioramento continuo autonomo".
![figura3.jpg](figura3.jpg)
[Immagine tratta dal paper ufficiale](https://www.arxiv.org/pdf/2506.09338)

## Il Filo Rosso dell'Efficienza Intelligente

C'è un pattern che emerge con sempre maggior chiarezza nella ricerca AI del 2025. Power Sampling di Harvard ci ha mostrato che capacità sofisticate possono essere già presenti nei modelli base, basta saperle estrarre. Il TRM di Samsung ha dimostrato che retrieval strategico batte memoria bruta. DeepConf ha rivelato che auto-riflessione costa meno di scaling cieco. E ora il MIT conferma che allocazione dinamica delle risorse supera budget fissi.

Il denominatore comune è l'efficienza intelligente. Non più soltanto "fai modelli più grandi e dagli più dati", ma "insegna ai modelli quando vale la pena essere grandi". È una maturazione necessaria per un'industria che si trova di fronte a costi energetici crescenti e pressioni sulla sostenibilità.

I Process Reward Model calibrati del MIT potrebbero sembrare un dettaglio tecnico di nicchia, ma rappresentano qualcosa di più profondo: la costruzione di un'auto-consapevolezza computazionale. Un modello che sa quando è confuso, che riconosce problemi facili da quelli difficili, che misura le proprie capacità prima di impegnarsi. Come nei Mentat di Dune, che dosavano con precisione maniacale le risorse cognitive per ogni calcolo, questi sistemi stanno imparando l'arte della parsimonia intelligente.

La domanda ora non è se questa direzione sia giusta, ma quanto velocemente l'industria saprà integrarla. Perché tra un sistema che brucia energia su ogni query e uno che ragiona solo quando serve, la differenza non è solo economica o ambientale. È filosofica: segna il passaggio da macchine che computano a macchine che "pensano" su come computare.