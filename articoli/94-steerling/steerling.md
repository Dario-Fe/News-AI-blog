---
tags: ["Training", "Generative AI", "Research"]
date: 2026-03-02
author: "Dario Ferrero"
youtube_url: "https://youtu.be/xSB0w1Lkh8U?si=DQLocbJnpNZxbcvZ"
---

# Steerling: quando l'IA ti spiega i suoi pensieri
![steerling.jpg](steerling.jpg)

*C'è un paradosso al cuore dell'intelligenza artificiale moderna che raramente viene detto ad alta voce: i sistemi più potenti che abbiamo costruito sono anche quelli che capiamo meno. Un modello linguistico da miliardi di parametri può scrivere codice, sintetizzare ricerche scientifiche, ragionare su contratti legali, eppure nessuno, nemmeno chi lo ha addestrato, è in grado di dirti con precisione *perché* ha scritto quella parola e non un'altra. È come possedere un collaboratore straordinariamente capace al quale, però, non puoi mai chiedere di mostrarti il ragionamento.*

Le conseguenze di questa opacità non sono astratte. Quando Grok di xAI ha mostrato ripetutamente output politicamente bizzarri, il team di manutenzione ha dovuto condurre lunghe sessioni di "interrogazione" del modello, affinando prompt, aggiustando parametri, sperando che il comportamento si stabilizzasse. Quando ChatGPT è finito sotto accusa per la sua tendenza alla sycophancy, ovvero ad assecondare l'utente anche quando ha torto, il problema era impossibile da localizzare chirurgicamente: tutto era distribuito su miliardi di connessioni, ovunque e in nessun posto. L'intera ricerca sulla cosiddetta XAI, la *AI spiegabile*, nasce da questa frustrazione e tenta di rispondervi con strumenti applicati dopo il fatto, tecniche come LIME o SHAP che analizzano un modello già addestrato cercando di ricostruirne il funzionamento dall'esterno, come archeologi che scavano tra le rovine di una civiltà perduta.

Guide Labs, una startup fondata a San Francisco, ha deciso di affrontare il problema da un'angolazione completamente diversa. Invece di studiare il modello dopo la sua nascita, ha cercato di rendere la trasparenza parte integrante dell'architettura, qualcosa che non si aggiunge ma che si ingegnerizza dentro, fin dall'inizio.

## Il problema che il 2020 ha messo in luce

Per capire cosa ha costruito Guide Labs vale la pena partire da dove è nato il progetto. Julius Adebayo, CEO e co-fondatore dell'azienda insieme alla Chief Science Officer Aya Abdelsalam Ismail, ha iniziato questo percorso durante il suo dottorato al MIT. Nel 2020 ha co-firmato un [paper accademico](https://arxiv.org/abs/1810.03292) che ha avuto un impatto significativo nel campo: la ricerca mostrava che i metodi allora in uso per "spiegare" le decisioni dei modelli di deep learning non erano affidabili. I tool post-hoc di interpretabilità, quelli che si applicano a un modello già costruito per capire cosa fa, producevano spiegazioni che sembravano sensate ma che non corrispondevano necessariamente a come il modello ragionava davvero.

È una scoperta che suona quasi filosofica, ma ha implicazioni pratiche enormi. Se non puoi fidarti degli strumenti che ti dicono perché un modello ha preso una decisione, non puoi usare quelle spiegazioni per correggere errori, per verificare la conformità normativa, o per garantire che il modello non stia discriminando su basi che non dovrebbe considerare. La spiegabilità diventava, in quel quadro, una forma di comfort narrativo più che di controllo reale.

Adebayo ha tratto una conclusione radicale: l'unico modo per avere interpretabilità autentica è costruirla dentro il modello, non applicarla sopra. «Il tipo di interpretabilità che si fa di solito è come fare neuroscienze su un modello», ha detto in un'[intervista a TechCrunch](https://techcrunch.com/2026/02/23/guide-labs-debuts-a-new-kind-of-interpretable-llm/). «Noi invece progettiamo il modello dal basso perché tu non abbia bisogno di fare neuroscienze.»

## L'architettura: un collo di bottiglia che si vede

Il 23 febbraio 2026 Guide Labs ha reso pubblico [Steerling-8B](https://github.com/guidelabs/steerling), un modello linguistico da 8 miliardi di parametri con licenza Apache 2.0, addestrato su 1.35 trilioni di token. La scelta di rendere il modello open source, con pesi disponibili su [Hugging Face](https://huggingface.co/guidelabs/steerling-8b) e codice su GitHub, è parte di una strategia precisa: far esaminare l'approccio dalla comunità scientifica e raccogliere feedback reali.

L'innovazione centrale si chiama *concept module*: un livello architetturale inserito tra il nucleo transformer del modello e il suo strato di output. In un modello linguistico tradizionale, le rappresentazioni interne vengono trasformate in previsioni del token successivo attraverso un percorso opaco e altamente non lineare. In Steerling, quel percorso è spezzato: prima di produrre qualsiasi output, ogni rappresentazione deve passare attraverso questo collo di bottiglia concettuale, dove viene tradotta in termini comprensibili.

Come funziona nella pratica? Il modello lavora con due famiglie di concetti. La prima comprende circa 33.000 concetti "noti", etichettati manualmente, categorie come *legale*, *medico*, *ironia*, *tono analitico*, *biologia molecolare*. La seconda include circa 100.000 concetti "scoperti" autonomamente dal modello durante l'addestramento, senza supervisione umana. Ogni previsione di token deve passare attraverso una combinazione lineare di questi concetti, il che significa che il contributo di ciascun concetto a ciascun output è matematicamente calcolabile, non approssimato.

Il risultato pratico è notevole: per qualsiasi gruppo di token generati da Steerling, è possibile risalire a tre livelli di origine. Il primo è il *contesto di input*, ovvero quali parti del prompt hanno influenzato maggiormente quella porzione di risposta. Il secondo sono i *concetti*, con una lista ordinata per rilevanza di quali categorie semantiche hanno guidato la generazione. Il terzo è quello forse più sorprendente: i *dati di addestramento*, con la distribuzione delle fonti di addestramento che hanno alimentato i concetti attivati durante la generazione, ArXiv, Wikipedia, FLAN, e così via.

È come avere, su ogni paragrafo generato dall'IA, una nota a piè di pagina che spiega da dove viene.

## Il costo dell'onestà: quanto si paga in performance?

La domanda che sorge spontanea è ovvia: se costringi il modello a passare attraverso un collo di bottiglia concettuale, stai rinunciando a qualcosa in termini di capacità? La risposta di Guide Labs, supportata dai dati che ha pubblicato nel paper tecnico [Scaling Interpretable Models to 8B](https://www.guidelabs.ai/post/scaling-interpretable-models-8b/), è che il costo esiste ma è gestibile e prevedibile.

Gli esperimenti mostrano che l'interpretabilità si comporta come una «tassa fissa»: un piccolo pedaggio costante che non peggiora all'aumentare della dimensione del modello. Le curve di apprendimento tra il modello base e quello con il concept module sono quasi sovrapponibili. Su benchmark standard come HellaSwag, OpenBookQA, ARC-Challenge, PIQA e WinoGrande, il modello interpetabile mantiene prestazioni comparabili al modello base senza il concept module, e la differenza di accuratezza si assottiglia ulteriormente man mano che il modello cresce.

Steerling-8B, secondo quanto dichiarato da Guide Labs, raggiunge il 90% delle capacità di modelli equivalenti addestrati su dataset 2-7 volte più grandi. Il che è notevole non solo come risultato di interpretabilità, ma anche come efficienza di addestramento.

C'è però un aspetto critico che merita attenzione: questi benchmark misurano la performance linguistica generale, non la qualità delle spiegazioni. Che i concetti identificati dal modello siano davvero informativi e non circolari, ovvero che "spiegare" non significhi semplicemente nominare la categoria ovvia, è una domanda ancora aperta. Il campo dell'interpretabilità non dispone di metriche condivise e consolidate per valutare oggettivamente la qualità di una spiegazione. Guide Labs misura la propria interpretabilità con metriche interne (come l'AUC di rilevamento dei concetti rispetto ad annotazioni di riferimento), ma uno standard industriale o accademico universalmente accettato non esiste ancora.

C'è poi un'altra limitazione strutturale da considerare. Tutta l'architettura dipende da un sistema a monte chiamato [ATLAS](https://www.guidelabs.ai/post/atlas-concept-annotated-pretraining-release/), sviluppato dallo stesso team, che si occupa di annotare il corpus di pre-addestramento con le etichette concettuali. Questo sistema usa a sua volta modelli AI per classificare i dati. È una soluzione ingegnosa, ma introduce una dipendenza: la qualità dell'interpretabilità finale è vincolata alla qualità delle annotazioni a monte. Se ATLAS è impreciso, le spiegazioni di Steerling lo saranno altrettanto, anche se nessuno lo noterà immediatamente dall'esterno.
![schema.jpg](schema.jpg)
[Immagine tratta da guidelabs.ai](https://www.guidelabs.ai/post/scaling-interpretable-models-8b/)

## Cosa cambia davvero: controllo, non solo spiegazione

Uno degli aspetti più interessanti di Steerling, e probabilmente quello con le implicazioni pratiche più immediate, non è la capacità di spiegare, ma quella di controllare. Poiché ogni previsione è una funzione lineare delle attivazioni concettuali, è possibile modificare quelle attivazioni direttamente, a tempo di esecuzione, senza riaddestrare il modello.

Questo si chiama *steering concettuale*, e ha conseguenze che vanno oltre la semplice spiegabilità. Vuoi che il modello smetta di fare riferimento a un certo tipo di contenuto? Sopprimi il concetto corrispondente. Vuoi che risponda con un tono più tecnico? Amplifica i concetti associati al registro specialistico. Vuoi rimuovere la conoscenza relativa a un argomento specifico senza riaddestrare da zero? Intervieni chirurgicamente a livello concettuale.

Adebayo ha illustrato questa capacità con un esempio concreto particolarmente rivelatore, citato nell'[intervista a TechCrunch](https://techcrunch.com/2026/02/23/guide-labs-debuts-a-new-kind-of-interpretable-llm/): nei modelli tradizionali, il concetto di genere è distribuito su centinaia di milioni di parametri in modo caotico e interconnesso. Modificarlo in modo affidabile richiede enormi sforzi di fine-tuning che spesso producono effetti collaterali indesiderati. In Steerling, se il concetto di genere è tracciabile e controllabile, puoi intervenire su di esso direttamente. Non è una garanzia di assenza di bias, i concetti stessi riflettono i dati su cui il modello è stato addestrato, ma è un meccanismo di intervento molto più preciso di qualsiasi alternativa post-hoc.

Questo ha risvolti concreti in almeno tre contesti ad alto rischio. In ambito medico, dove un sistema AI che assiste la diagnosi deve poter dimostrare su quale evidenza si basa una raccomandazione. In ambito finanziario, dove un modello che valuta richieste di credito non può considerare criteri come etnia o genere, e deve poterlo dimostrare. In ambito legale, dove la tracciabilità del ragionamento è spesso un requisito di sistema, non un optional.

## Il contesto normativo: l'EU AI Act come acceleratore

Steerling arriva in un momento in cui la pressione regolatoria sull'interpretabilità dei sistemi AI è concreta e crescente. L'[EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) classifica i sistemi di AI in categorie di rischio, con i sistemi ad alto rischio, quelli usati in medicina, giustizia, credito, selezione del personale, soggetti a requisiti espliciti di trasparenza e verificabilità. Il framework NIST negli Stati Uniti muove nella stessa direzione.

L'approccio di interpretabilità intrinseca di Guide Labs si allinea strutturalmente con questi requisiti in modo che i metodi post-hoc non possono garantire. Una spiegazione costruita dentro il modello è, per definizione, fedele al suo funzionamento. Una spiegazione costruita fuori può essere informativa ma rimane un'approssimazione, e in contesti dove quella spiegazione deve reggere a un'analisi legale, la differenza è sostanziale.

Detto questo, la verificabilità reale di Steerling dipenderà da quanto la comunità esterna sarà in grado di verificare le sue affermazioni in modo indipendente. Il codice è pubblico, i pesi sono disponibili, e questo è un buon inizio. Ma la validazione di un approccio così nuovo richiede tempo, riproducibilità e critica sistematica da parte di ricercatori indipendenti. Siamo ancora agli inizi di quel processo.

## Il team e il percorso

Guide Labs ha completato il programma Y Combinator e nel novembre 2024 ha chiuso un round seed da 9 milioni di dollari guidato da Initialized Capital. Tra gli advisor figura Jonathan Frankle, ricercatore noto nel campo dell'efficienza dei modelli neurali. La scelta dell'Apache 2.0, licenza permissiva che consente uso commerciale senza restrizioni, è deliberata: Guide Labs vuole che Steerling venga adottato, esaminato e migliorato dalla comunità. Il passo successivo dichiarato è lo sviluppo di modelli più grandi e l'apertura di accesso API e agentico.

## Le domande che restano aperte

Steerling è un progetto genuinamente interessante e tecnicamente solido, ma sarebbe ingenuo presentarlo come la soluzione definitiva al problema dell'opacità dei modelli AI. Ci sono domande legittime a cui nessuno ha ancora risposto in modo soddisfacente.

La prima riguarda la scalabilità verso i modelli frontier. Steerling-8B funziona a 8 miliardi di parametri. I modelli più capaci in circolazione hanno una scala diversa, e non è affatto scontato che il sovraccarico del concept module rimanga una "tassa fissa" anche a quelle dimensioni. Guide Labs afferma che le leggi di scaling sono preservate, ma la dimostrazione a scala di modello di frontiera non c'è ancora.

La seconda riguarda la qualità intrinseca dei concetti. Tracciare un token fino a un concetto etichettato "legale" o "tono analitico" è informativo, ma quanto quelle etichette corrispondono davvero a ciò che succede dentro il modello? Esiste il rischio concreto di costruire una narrativa di spiegazione che è coerente con sé stessa ma non con la realtà interna del sistema. In quel caso, l'interpretabilità diventerebbe non un controllo ma una forma più sofisticata di teatro della trasparenza: il modello sembra spiegabile, ma le spiegazioni non corrispondono a meccanismi reali.

La terza domanda riguarda l'etica delle attribuzioni. Se possiamo tracciare ogni output fino ai dati di addestramento, possiamo anche identificare quali fonti hanno contribuito a una risposta problematica. È un potere che può essere usato bene, per rimuovere bias, per rispettare il diritto d'autore, per garantire accuratezza. Ma può anche essere usato per attribuire responsabilità in modo selettivo, o per costruire meccanismi di controllo su cosa il modello "sa" o non sa, con implicazioni che vanno ben oltre la tecnica.

Infine, c'è la domanda più fondamentale di tutte: cosa significa davvero "capire" un modello linguistico? La risposta di Guide Labs, tracciare ogni token fino ai suoi contributi concettuali e alle sue fonti di addestramento, è elegante e operativamente utile. Ma un modello che si spiega in questi termini è davvero più comprensibile, o è semplicemente più articolato nel descrivere la propria opacità?

È una domanda che l'industria e la ricerca dovranno affrontare insieme, man mano che approcci come quello di Guide Labs diventano più maturi e diffusi. Per ora, Steerling-8B è il tentativo più serio e documentato di rispondere ingegneristicamente a un problema che finora sembrava di pertinenza quasi esclusivamente filosofica. Vale la pena tenerlo d'occhio.
