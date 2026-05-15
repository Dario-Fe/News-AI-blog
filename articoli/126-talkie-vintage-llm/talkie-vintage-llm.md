---
tags: ["Research", "Ethics & Society", "Training"]
date: 2026-05-15
author: "Dario Ferrero"
youtube_url: "https://youtu.be/0qKJVbEZ1pg?si=f37zUNe3BJGGltQo"
---

# Talkie: quando un LLM non sa nulla dopo il 1930
![talkie-vintage-llm.jpg](talkie-vintage-llm.jpg)

*C'è un esperimento mentale che Demis Hassabis, fondatore di DeepMind, ha lanciato in più occasioni come provocazione intellettuale: se addestraste un modello linguistico su tutto il corpus scientifico disponibile fino al 1911, riuscirebbe a riscoprire autonomamente la Relatività Generale, che Einstein avrebbe formulato quattro anni dopo? La domanda non è retorica. È una delle più difficili che si possano porre sull'intelligenza artificiale, perché tocca il problema della generalizzazione vera, quella che va oltre il recupero di pattern memorizzati e si avvicina a qualcosa che potremmo chiamare, con molta cautela, ragionamento.*

È da questa tensione che nasce Talkie, un progetto presentato nell'aprile 2026 da Nick Levine, David Duvenaud e Alec Radford, quest'ultimo noto per aver contribuito allo sviluppo di GPT-2 presso OpenAI. L'idea è semplice da enunciare e complicata da eseguire: addestrare un modello linguistico da tredici miliardi di parametri usando esclusivamente testi pubblicati prima del 31 dicembre 1930, poi studiarne il comportamento come si studia un campione in laboratorio, in un ambiente controllato e isolato da qualsiasi contaminazione contemporanea.

Il risultato si chiama [talkie-1930-13b](https://huggingface.co/talkie-lm/talkie-1930-13b-it), ed è disponibile pubblicamente su Hugging Face. Ma prima di parlare di cosa fa, vale la pena capire perché esiste.

## Non nostalgia, ma metodologia

Il rischio più grande con un progetto come questo è leggerlo come una curiosità, un giocattolo culturale, l'equivalente digitale di un grammofono. Sarebbe un errore di prospettiva. Talkie non è un modello che compete con Claude, ChatGPT o Gemini su nessun compito pratico. È uno strumento di ricerca che risponde a domande strutturali sul funzionamento dei modelli linguistici moderni, domande che con i modelli generalisti non si possono nemmeno formulare correttamente.

Il problema centrale si chiama contaminazione, ed è uno dei fantasmi più persistenti nella valutazione dei sistemi di intelligenza artificiale. Quando si misura la capacità di un modello su un benchmark, come MMLU, HumanEval o ARC, si assume implicitamente che il modello non abbia già "visto" le domande o risposte simili durante il preaddestramento. Ma questa assunzione è sempre più fragile: i corpus moderni includono enormi quantità di testo proveniente dal web, e il web include forum, soluzioni, spiegazioni e persino copie dirette dei benchmark stessi. Un modello che risponde correttamente a una domanda di matematica potrebbe farlo perché ragiona, o perché ha memorizzato la risposta da qualche angolo di Reddit. Distinguerli è quasi impossibile quando il corpus di addestramento è il web intero.

Un modello addestrato solo su testi del 1930 non ha questo problema per costruzione. Non può aver visto Python, perché Python non esisteva. Non può aver memorizzato soluzioni da Stack Overflow, perché Stack Overflow non esisteva. Se riesce a scrivere codice corretto dopo aver visto pochi esempi nel contesto, lo fa per generalizzazione pura, non per recupero. È un ambiente sperimentale che i modelli moderni, per come sono costruiti, non possono mai offrire.

L'idea del "vintage LM" non è completamente nuova: il team stesso cita progetti precedenti come Ranke-4B, Mr. Chatterbox e Machina Mirabilis come parte di un ecosistema nascente. Talkie è però il più grande di questa categoria, e il primo a documentare sistematicamente le sfide metodologiche che questo tipo di addestramento comporta.

## Costruire un archivio del passato: 260 miliardi di token

La prima domanda pratica è dove trovare così tanto testo pre-1931 in formato digitale. La risposta è che la maggior parte del lavoro era già stata fatta da altri. Il team di Talkie ha costruito il proprio corpus appoggiandosi all'[Institutional Data Initiative](https://huggingface.co/datasets/institutional/institutional-books-1.0), all'[Internet Archive](https://archive.org) e al progetto [Common Pile](https://huggingface.co/common-pile), aggregando libri, giornali, periodici, riviste scientifiche, brevetti e atti legali in inglese per un totale di 260 miliardi di token.

La scelta del cutoff al 31 dicembre 1930 non è arbitraria, né è solo simbolica. Ha una base legale precisa: secondo il diritto d'autore statunitense, le opere pubblicate prima del 1926 sono nel pubblico dominio, e la finestra si estende progressivamente fino al 1930 per le opere di quell'anno specifico. Il cutoff temporale risolve dunque anche il problema del licensing, rendendo il corpus legalmente distribuibile senza le complicazioni che affliggono i dataset moderni.

La scelta di limitarsi all'inglese per questa versione è pragmatica: il team dichiara esplicitamente che validare la pipeline dati richiede familiarità profonda con i documenti sorgente, e i ricercatori sono madrelingua inglesi. L'espansione multilingue è indicata come priorità futura, sia per aumentare le dimensioni del corpus sia per diversificare le prospettive culturali rappresentate.

Duecentosessanta miliardi di token sembrano molti, ma vanno contestualizzati: i modelli generalisti moderni sono addestrati su corpus nell'ordine dei trilioni di token, spesso con più passaggi sui dati più importanti. Il team stima però di poter crescere il proprio corpus a oltre un trilione di token di testo storico, una stima che, se confermata, porterebbe le capacità del modello nell'ordine di GPT-3.5, descritto nel post introduttivo come "simile per capacità al ChatGPT originale".
![identity.jpg](identity.jpg)
[Immagine tratta dal repository GitHub](https://github.com/talkie-lm/talkie)

## Il nemico invisibile: OCR e rumore sistematico

Se il corpus è il fondamento, la sua qualità è la crepa più profonda nell'edificio. Nel 1930 non esisteva il testo digitale nativo: tutto ciò che è finito nel dataset di Talkie è stato trascritto da fonti fisiche attraverso il riconoscimento ottico dei caratteri, un processo che introduce un tipo di rumore radicalmente diverso da qualsiasi errore presente nei corpus moderni.

I sistemi OCR classici, quelli usati storicamente per digitalizzare archivi, funzionano bene su layout semplici e scansioni pulite. Sui giornali d'epoca con colonne irregolari, caratteri tipografici deteriorati e pagine ingiallite, la loro accuratezza crolla. Il team di Talkie ha quantificato questo problema in modo preciso: addestrare un modello su testi pre-1931 trascritti con OCR convenzionale produce, a parità di risorse computazionali, solo il 30% dell'efficienza di apprendimento di un modello addestrato sulle stesse trascrizioni fatte da esseri umani. Una pulizia con espressioni regolari recupera parte del terreno portando il dato al 70%, ma rimane uno scarto significativo.

La soluzione alternativa, usare sistemi moderni basati su modelli visivi di grandi dimensioni, crea un problema paradossale: questi sistemi più accurati tendono ad allucinare fatti moderni nel testo trascritto, contaminando esattamente il corpus che si vuole tenere puro. Il team sta sviluppando un sistema OCR "vintage" specifico per questo scopo, un modello addestrato a trascrivere testi storici senza introdurre conoscenza contemporanea.

È un problema che ricorda la situazione del restauratore cinematografico che deve pulire una pellicola degli anni Venti senza introdurre artefatti digitali riconoscibili: ogni strumento moderno lascia tracce di sé nel materiale che tocca.

## Quando il passato fa filtrare il futuro: il problema del temporal leakage

Anche con un corpus apparentemente circoscritto, il confine temporale è più poroso di quanto sembri. Il team identifica diverse modalità attraverso cui contenuti successivi al 1930 possono infiltrarsi nel dataset: metadati di data errati su documenti digitalizzati, introduzioni editoriali moderne aggiunte a ristampe di classici, note a piè di pagina scritte da curatori del dopoguerra, inserzioni anacronistiche in testi altrimenti storici.

Per affrontare questo problema, Talkie utilizza un classificatore di anacronismi basato su n-grammi a livello di documento, uno strumento che individua sequenze di parole statisticamente improbabili in un corpus pre-1931 e filtra i documenti sospetti. Il sistema non è però infallibile: una versione precedente del modello a sette miliardi di parametri mostrava chiaramente conoscenza della presidenza Roosevelt e del New Deal, entrambi successivi al cutoff. La versione attuale da 13 miliardi conserva alcune tracce di conoscenza relativa alla Seconda Guerra Mondiale, all'ONU e alla divisione della Germania, dettagli che non avrebbero potuto provenire da testi del 1930.

Questi residui di futuro nel modello non sono soltanto un difetto tecnico: sono la dimostrazione di quanto sia difficile, in pratica, costruire un confine temporale realmente stagno. Il team li documenta con onestà metodologica, citandoli come spunto di ricerca futura piuttosto che nasconderli, e sta sviluppando classificatori più avanzati per le versioni successive del modello.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta dal sito ufficiale talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Istruire un modello senza usare il presente

Una volta addestrato il modello base, il passo successivo è renderlo utile come interlocutore, il che richiede un processo di post-training, cioè un affinamento che trasformi il modello da predittore di testo a conversatore capace di seguire istruzioni. Il problema è che tutti i dataset standard per questo processo, le raccolte di dialoghi umano-assistente, le preferenze annotate, i benchmark di instruction following, sono intrinsecamente moderni. Usarli significherebbe contaminare il modello con aspettative, stili comunicativi e conoscenze del XXI secolo.

Il team ha costruito una pipeline di post-training da zero. La prima fase usa testi storici con struttura regolare come materia prima: manuali di etichetta vittoriani, ricettari d'epoca, dizionari, enciclopedie, raccolte di fiabe, guide epistolari. Da questi testi vengono estratte coppie istruzione-risposta che riflettono le convenzioni comunicative dell'epoca, e il modello viene affinato su di esse. È come insegnare a qualcuno le buone maniere usando il galateo di Monsignor Della Casa invece di un corso di comunicazione aziendale contemporaneo.

La seconda fase è più sofisticata e introduce una tensione concettuale interessante. Il team utilizza il Direct Preference Optimization online, una tecnica di addestramento per preferenze, generando prompt sintetici su vari tipi di compiti e usando Claude Sonnet 4.6 come giudice per valutare la qualità delle risposte di Talkie. Il punteggio medio di instruction following è passato da 2.0 a 3.4 su una scala a cinque punti nel corso di questo processo. Una terza fase usa poi conversazioni sintetiche generate tra Claude Opus 4.6 e Talkie per levigare le asperità conversazionali residue.

Il problema è che questo approccio introduce inevitabilmente una contaminazione sottile: un modello moderno che valuta le risposte di un modello vintage trasferisce, anche involontariamente, aspettative contemporanee su cosa costituisce una buona risposta. Una versione precedente del modello, dopo il reinforcement learning con feedback AI, aveva sviluppato l'abitudine di rispondere in liste puntate, uno stile del tutto estraneo alla prosa dell'Ottocento e dei primi del Novecento, ma caratteristico dei modelli assistente moderni. Il team riconosce esplicitamente questo limite e indica come obiettivo futuro quello di usare i propri modelli vintage come giudici, eliminando la dipendenza da sistemi contemporanei.

## Cosa sa, cosa non sa: il confronto con il gemello moderno

Per contestualizzare le capacità di Talkie in modo rigoroso, il team ha addestrato un "gemello moderno", un modello architetturalmente identico ma addestrato su FineWeb, uno dei principali corpus di testo web moderno. Il confronto a parità di risorse computazionali mostra che Talkie sottoperforma il suo equivalente contemporaneo nelle valutazioni standard di conoscenza, un risultato atteso e dichiarato apertamente.

Ciò che è più interessante è cosa succede quando si filtrano le domande anacronistiche dai benchmark, cioè quelle che presuppongono conoscenza di eventi, tecnologie o concetti posteriori al 1930. Eliminando queste domande, il gap di performance si riduce approssimativamente della metà. Il modello vintage e il modello moderno mostrano performance comparabili su compiti di comprensione linguistica fondamentale e ragionamento numerico, le capacità che dipendono meno dal contenuto specifico del corpus e più dalla struttura del linguaggio stesso.

Il test più affascinante dal punto di vista teorico riguarda la programmazione. Il team ha somministrato a Talkie una versione di HumanEval, il benchmark standard per la valutazione della capacità di scrittura di codice Python, fornendo al modello alcuni esempi nel contesto ma nessuna conoscenza previa di Python o della programmazione moderna. I risultati sono nettamente inferiori a qualsiasi modello addestrato su dati web, dove il codice è abbondante. Tuttavia, con scale crescenti, il modello mostra miglioramenti costanti anche su questo compito, un segnale che qualcosa che somiglia alla generalizzazione sta emergendo. I problemi risolti correttamente sono semplici, spesso di una sola riga, ma includono casi come l'implementazione della funzione di decodifica di un cifrario a rotazione quando viene fornita solo la funzione di codifica, suggerendo una comprensione rudimentale del concetto di funzione inversa.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta dal sito ufficiale talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Bias storici e responsabilità culturale

Un modello addestrato esclusivamente su testi del 1930 riflette necessariamente la cultura, i valori, il lessico e i pregiudizi di quell'epoca. Questo non è un dettaglio marginale: è una caratteristica strutturale che il team riconosce esplicitamente con la nota che Talkie "può produrre output offensivi per gli utenti", una formulazione sobria per indicare che il corpus include testi prodotti in un'epoca di colonialismo attivo, razzismo istituzionalizzato, esclusione sistematica delle donne dalla vita pubblica e antisemitismo diffuso nella cultura mainstream.

Questo aspetto è sia un limite applicativo evidente sia, paradossalmente, uno degli elementi di maggiore interesse scientifico. Studiare come questi bias si manifestano nel comportamento del modello, come si propagano dal corpus all'output, e come interagiscono con il post-training potrebbe offrire intuizioni preziose sulla stessa dinamica nei modelli moderni, dove i bias sono più difficili da isolare perché annegati in un corpus vastissimo e disomogeneo.

La questione pone anche domande più ampie che il team solleva esplicitamente: quanto di ciò che osserviamo nei modelli linguistici attuali è una proprietà del linguaggio umano in generale, e quanto è invece una proprietà specifica del web come corpus? I modelli moderni sono tutti, in varia misura, figli dello stesso genitore digitale. Costruire modelli addestrati su corpora radicalmente diversi, come testi storici, testi scientifici puri, o letteratura non anglofona, potrebbe rivelare quanto di ciò che chiamiamo "comportamento emergente" sia effettivamente emergente e quanto sia invece riflesso fedele della fonte.

## Dove si trova Talkie rispetto alla ricerca attuale

È importante collocare questo progetto onestamente nel panorama della ricerca. Al momento della pubblicazione, in aprile 2026, il lavoro di Talkie non ha ancora superato una revisione paritaria formale: è presentato come un post introduttivo con metodologia documentata, dati quantitativi e accesso pubblico al modello e al codice su [GitHub](https://github.com/talkie-lm/talkie), ma senza la validazione esterna che un paper pubblicato su una conferenza come NeurIPS o ICML comporterebbe. I dati riportati, come l'efficienza OCR al 30% o il miglioramento del punteggio DPO da 2.0 a 3.4, sono presentati come risultati interni e andrebbero confermati da repliche indipendenti.

Il progetto riceve supporto computazionale e finanziario da Anthropic e da Coefficient Giving, e i ringraziamenti includono nomi di rilievo nel campo come John Schulman e Andrej Karpathy, segnali di credibilità nell'ecosistema della ricerca. Ma la strada dalla demo pubblica alla contribuzione metodologica consolidata è ancora lunga.

Quello che si può dire con certezza è che la domanda di ricerca è legittima e importante. La contaminazione dei benchmark è un problema documentato e crescente, come testimonia un [recente paper](https://arxiv.org/abs/2602.12413) citato dagli stessi autori. L'idea di usare modelli con cutoff temporali netti come strumenti di valutazione della generalizzazione è originale e metodologicamente coerente. Il progetto apre una direzione, non la chiude.

## Una nuova linea di ricerca, non un'alternativa

Il piano di scaling di Talkie è ambizioso: entro l'estate 2026 il team prevede di rilasciare un modello nell'ordine di GPT-3 per capacità, e stima che un corpus di oltre un trilione di token storici sia sufficiente a costruire qualcosa di comparabile a GPT-3.5. Questi obiettivi vanno letti nel contesto in cui sono dichiarati: non come annunci di prodotto, ma come orizzonti di ricerca che determinano la scala degli esperimenti futuri.

L'ambizione più interessante, però, non è quella numerica. È la possibilità di costruire una pipeline di post-training completamente autonoma, in cui i modelli vintage vengono usati come giudici di se stessi, eliminando la dipendenza da Claude o da altri sistemi moderni nella valutazione delle preferenze. Se realizzato, questo permetterebbe di ottenere un modello genuinamente "periodo" non solo nei dati di preaddestramento, ma in tutto il processo di allineamento, un esperimento senza precedenti su come la fonte dei valori di addestramento influenzi il comportamento finale del sistema.

C'è un parallelismo utile con certi esperimenti in linguistica computazionale degli anni Novanta, quando ricercatori come Frederick Jelinek alla IBM costruivano modelli statistici del linguaggio su corpus rigorosamente controllati, non perché volessero sistemi di produzione, ma perché ambienti controllati rivelano meccanismi che corpus ampi e rumorosi nascondono. Talkie si inserisce in questa tradizione: usa la limitazione come lente analitica.

La risposta alla domanda di Hassabis, se un modello fermo al 1911 potrebbe riscoprire la Relatività Generale, rimane aperta. Ma Talkie suggerisce che il modo per avvicinarsi a una risposta credibile non è speculare, è costruire l'esperimento. Addestrare il modello, dargli la fisica di Maxwell e le anomalie nell'orbita di Mercurio, e vedere cosa emerge. Non è fantascienza: è il metodo scientifico applicato all'intelligenza artificiale, con tutta la pazienza e il rigore che richiede.

---

*Il codice sorgente di Talkie è disponibile su [GitHub](https://github.com/talkie-lm/talkie). Il modello base e la versione post-addestrata sono accessibili pubblicamente su [Hugging Face](https://huggingface.co/talkie-lm). Una demo conversazionale è disponibile su [talkie-lm.com/chat](https://talkie-lm.com/chat).*
