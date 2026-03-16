---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-16
author: "Dario Ferrero"
youtube_url: "https://youtu.be/FWY9NQRSmxg?si=ob3qR7FwGGssfcuC"
---

# L'AI in casa: LM Studio e Qwen 3.5 sul mio PC - Puntata 1
![qwen3.5-locale-puntata1.jpg](qwen3.5-locale-puntata1.jpg)

*C'è un momento preciso in cui una tecnologia smette di essere promessa e diventa strumento. Non è quando esce il comunicato stampa, non è quando i benchmark fanno il giro dei social, ma quando una persona normale, con un PC normale, si siede, scarica qualcosa, e decide di capire davvero cosa sta succedendo. Questo articolo è quel momento, almeno per me.*

Nelle scorse due settimane, il nome che ha dominato le conversazioni nell'ecosistema open-weight dell'intelligenza artificiale è uno solo: Qwen 3.5. Il team di Alibaba ha rilasciato il 2 marzo 2026 la serie small del modello, varianti da 0,8 a 9 miliardi di parametri, tutte sotto licenza Apache 2.0, tutte eseguibili su hardware consumer, e la reazione della comunità è stata immediata e vivace. Ma prima di entrare nei dettagli del modello e del mio esperimento personale, è utile capire perché questo momento è arrivato proprio ora.

## Il vento cambia direzione

In un articolo pubblicato qualche settimana fa su questo portale, [ho analizzato le ragioni per cui il 2026 si configura come l'anno degli Small Language Model](https://aitalk.it/it/slm-2026.html): la convergenza tra pressioni sui costi energetici, istanze di privacy sempre più stringenti, e un salto qualitativo nell'efficienza architetturale che ha ridisegnato il confine tra "possibile su cloud" e "possibile in locale". Non è un trend ideologico, è una risposta pragmatica a vincoli reali.

I dati, però, raccontano ancora una storia con due velocità. Come emerge dall'[analisi sul rapporto DigitalOcean Currents pubblicata sempre qui](https://aitalk.it/it/agenti-al-lavoro.html), il 64% delle aziende oggi integra modelli attraverso API di fornitori terzi, e solo il 21% usa modelli open-weight in produzione. Il cloud non è morto: è ancora dominante. Ma quella che sembrava un'asimmetria insuperabile tra modelli proprietari enormi e modelli locali "di ripiego" si sta assottigliando con una velocità che sorprende anche gli osservatori più attenti.

Su benchmark come [GPQA Diamond](https://huggingface.co/datasets/Idavidrein/gpqa), il test di riferimento per il ragionamento a livello universitario avanzato, 198 domande di fisica, chimica e biologia, Qwen3.5-9B segna 81.7, superando GPT-OSS-120B di OpenAI che si ferma a 71.5, come riportato sulla [pagina ufficiale del modello su HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B). Stiamo parlando di un modello con tredici volte meno parametri. Non è un'ottimizzazione incrementale: è un cambio di paradigma su cosa significa "piccolo" nel 2026.

Le reazioni nel settore sono state significative e, come spesso accade in questo campo, non univoche. Alcuni osservatori di punta hanno accolto il rilascio con entusiasmo, sottolineando la densità di capacità rispetto alle dimensioni. Altri, da Anthropic in primis, hanno mantenuto un tono più cauto, osservando che i modelli ottimizzati per performare sui benchmark non sempre trasferiscono quelle capacità nel mondo reale con la stessa fedeltà. Una tensione che attraversa l'intero dibattito sull'AI open-weight e che nessun numero su una tabella risolve definitivamente. La verità, come sempre, sta nell'uso.

Ed è esattamente per questo che ho deciso di sporcarmi le mani.

## Un esperimento onesto, senza pretese scientifiche

Prima di procedere, è necessario essere chiari su cosa è questo articolo e cosa non è. Quello che segue è un esperimento personale, condotto da un appassionato che vuole capire cosa si può ottenere con mezzi normali in questo preciso momento storico. Non c'è un protocollo di testing peer-reviewed, non c'è un campione statisticamente significativo di prompt, non c'è un metodo riproducibile che reggerebbe al vaglio di una conferenza accademica. I test sono stati verificati incrociando i risultati con modelli di frontiera come Claude e DeepSeek, ma questo non li trasforma in benchmark scientifici: rimangono prove sul campo, condotte con gli strumenti di un utente evoluto, non di un ricercatore.

Il valore, se c'è, sta proprio in questo: capire dove si arriva con conoscenze buone ma non da dottorato, con hardware da privato e la volontà di capire prima di comprare. Chi vuole numeri certificati troverà i benchmark ufficiali sulla [pagina HuggingFace del modello](https://huggingface.co/Qwen/Qwen3.5-9B). Chi vuole sapere come gira su un PC del 2025 acquistato a un prezzo ragionevole, continui a leggere.

## Il laboratorio: un PC di livello intermedio

La macchina su cui ho condotto i test non è una workstation da rendering professionale né una gaming rig da competizione. È un PC assemblato con criterio ma senza esagerare: processore AMD Ryzen 7700, 32 GB di RAM DDR5, e soprattutto una GPU AMD Radeon RX 9060 XT con 16 GB di VRAM. Una configurazione che molti utenti avanzati, gamer, content creator, sviluppatori che lavorano da casa, potrebbero riconoscere come propria. Hardware di fascia media-alta nel segmento consumer, ma lontano dall'A100 che ci si immagina quando si parla di inferenza locale su modelli linguistici.

Questa scelta non è casuale. Proprio la fascia media della configurazione è il punto. Se un modello gira bene qui, gira bene su una fetta enorme di PC già esistenti. Se fatica qui, quella fetta si restringe considerevolmente.

## Scegliere il framework: LM Studio contro Ollama

Per eseguire un modello linguistico in locale servono due cose: il modello stesso (un file di qualche gigabyte) e un framework che faccia da interprete tra l'hardware e il modello, gestendo memoria, tokenizzazione e inferenza. Senza questo strato intermedio, scaricare i pesi di un modello è come avere i file di un film senza un lettore video.

Le due strade che dominano questo spazio nel 2026 possono essere rappresentate da [LM Studio](https://lmstudio.ai/) e [Ollama](https://ollama.com/), e la differenza tra loro riflette una tensione classica nel software: accessibilità versus controllo.

[Ollama](https://ollama.com/) è lo strumento dei developer. Si installa con una riga di terminale, espone di default un'API REST compatibile con OpenAI su `localhost:11434`, si integra senza attrito in script, pipeline e applicazioni. È open source, ha una community ampia, e la sua filosofia minimalista, un comando per scaricare, un comando per eseguire, lo rende il backend preferito di dozzine di applicazioni terze. In termini di performance grezza è tendenzialmente più veloce, gestisce meglio le richieste concorrenti e consuma meno risorse grazie all'assenza di overhead grafico. Il rovescio della medaglia: richiede familiarità con il terminale, la configurazione avanzata passa attraverso i Modelfile, e la sua interfaccia grafica nativa è arrivata tardi e rimane minimale. C'è anche una questione di trasparenza che vale la pena segnalare: Ollama è open source e la community si fida della sua condotta, mentre LM Studio è closed source, un dettaglio che per chi è particolarmente attento alla privacy vale la pena tenere presente.

[LM Studio](https://lmstudio.ai/) gioca su un campo diverso. È un'applicazione desktop con interfaccia grafica curata, disponibile per Windows, macOS e Linux. Permette di cercare, scaricare e caricare modelli senza aprire un terminale, espone anch'essa un'API compatibile con OpenAI per chi vuole integrarla in altri strumenti, e gestisce automaticamente l'accelerazione GPU su hardware NVIDIA, Apple Silicon e AMD. Ma il dettaglio che cambia davvero l'esperienza per chi arriva all'AI locale senza un background da sviluppatore è uno: al momento della selezione di un modello, LM Studio mostra in tempo reale una stima delle performance attese sulla propria configurazione hardware, con indicatori cromatici che comunicano immediatamente se il modello girerà agevolmente, con limitazioni, o se l'hardware è insufficiente. Per un privato che sperimenta, questa frizione eliminata vale l'eventuale gap di performance rispetto a Ollama.

La scelta per questo esperimento è caduta su LM Studio per ragioni pragmatiche: la possibilità di vedere in anticipo se Qwen 3.5 9B Q8_0 avrebbe girato a pieno regime sulla mia GPU, senza calcoli a mano o documentazione tecnica da consultare, mi ha permesso di ottimizzare subito la scelta. Per chi ha invece intenzione di integrare un modello in un'applicazione, automatizzare workflow o lavorare in ambiente server, Ollama rimane la scelta più solida.
![lmstudio.jpg](lmstudio.jpg)
*Screenshot del mio PC all'avvio di LM Studio. Nel menu in alto a destra le opzioni del software con il bottone più in basso per selezionare e scaricare il modello desiderato. Al fianco la cronologia delle chat. In basso al centro la finestra di dialogo per i prompt, dove si può notare il modello selezionato.*

## Installare LM Studio: cinque minuti e si parte

L'installazione non richiede particolari competenze tecniche. Dal [sito ufficiale](https://lmstudio.ai/) si scarica l'installer per il proprio sistema operativo, un eseguibile su Windows, un DMG su macOS, un AppImage per Linux, e si procede come con qualsiasi altra applicazione desktop. Nessuna dipendenza esterna da installare, nessun ambiente virtuale da configurare, nessun terminale da aprire. Il pacchetto pesa circa 500 MB; le prime schermate guidano verso la configurazione dell'accelerazione hardware rilevata automaticamente, e in pochi minuti ci si trova di fronte alla schermata principale.

Da lì, la sezione di ricerca modelli permette di sfogliare il catalogo, che attinge principalmente da HuggingFace, filtrando per dimensione, tipo di quantizzazione e compatibilità hardware dichiarata. Selezionando un modello compaiono le stime di performance sulla propria macchina: è qui che si capisce immediatamente cosa ci si può aspettare prima di scaricare anche un solo gigabyte.

## Perché Qwen 3.5 9B, e perché Q8_0

Con il framework installato, la scelta del modello è il secondo snodo critico. Ho scelto Qwen 3.5 9B in quantizzazione Q8_0, il file occupa poco più di 10 GB su disco, per ragioni che vale la pena spiegare, perché riflettono una logica utile per chiunque si approcci a questa scelta.

Il taglio da 9 miliardi di parametri è diventato in questo periodo lo standard de facto per i test sul campo: è la dimensione più diffusa tra tutti i principali competitor che rilasciano modelli open-weight, rappresenta il punto di equilibrio tra capacità e requisiti hardware, e permette confronti significativi tra famiglie diverse. Le varianti da 27B e 35B sono certamente più capaci, ma richiedono hardware più costoso che per un privato rappresenta un salto non banale. Per un'azienda anche piccola, invece, valutare un modello da 9B ha un doppio valore: capire cosa si ottiene subito con investimento minimo, e proiettare cosa si potrebbe ottenere con un gradino hardware superiore, visto il ritmo con cui le performance crescono e i requisiti calano.

La scelta della quantizzazione Q8_0, la più alta tra le tre opzioni disponibili in LM Studio per questo modello, è stata resa possibile proprio dai 16 GB di VRAM: l'indicatore verde confermava che il modello sarebbe girato interamente su GPU senza dover scaricare layer sulla RAM di sistema, garantendo velocità di inferenza massima e qualità di risposta non degradata dalle approssimazioni numeriche delle quantizzazioni più aggressive.

Sul piano tecnico, Qwen 3.5 non è semplicemente un modello precedente rimpicciolito. Come descritto nella [documentazione ufficiale su HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B), l'architettura adotta un approccio ibrido che combina Gated Delta Networks, una forma di attenzione lineare, con sparse Mixture-of-Experts, con l'obiettivo di affrontare il "memory wall" che tipicamente limita i modelli piccoli garantendo throughput elevato con latenza ridotta. La finestra di contesto nativa è di 262.144 token, estendibile fino a circa un milione attraverso YaRN. E a differenza delle generazioni precedenti che aggiungevano capacità visive come moduli separati, Qwen 3.5 è stato addestrato dall'inizio su token multimodali, testo, immagini e video integrati attraverso un processo chiamato early fusion.

Il modello supporta due modalità operative: *thinking* e *non-thinking*. Nella prima, prima di produrre la risposta il modello genera esplicitamente una catena di ragionamento interna, dedicando dai 20 ai 40 secondi di elaborazione prima di scrivere la risposta vera e propria. Nella seconda, risponde immediatamente. In tutti i test che seguono ho usato la modalità thinking, in quanto alcuni prompt erano deliberatamente complessi. Ho fatto le stesse prove anche disattivando il thinking: le risposte diventano immediate, la profondità cala leggermente sulle domande più articolate, ma per usi quotidiani, assistenza alla scrittura, coding di routine, analisi di testi, domande informative, la combinazione di precisione e velocità è più che soddisfacente. In entrambe le modalità, l'output ha viaggiato a circa 30 token al secondo su questa configurazione hardware.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da huggingface.co](https://huggingface.co/Qwen/Qwen3.5-9B)

## I test: sei prove sul campo

I sei test che seguono sono stati progettati per coprire le aree principali di valutazione dei modelli linguistici: ragionamento scientifico avanzato, comprensione multimodale, generazione di codice complesso, capacità multilingua con pianificazione, gestione di contesti molto lunghi, e ragionamento visuo-spaziale. Per ciascun test, i risultati di Qwen 3.5 9B sono stati verificati incrociando le risposte con modelli di frontiera come Claude e DeepSeek, non come validazione scientifica, ma come controllo di validità pratico.

I voti che accompagnano ciascun test sono il frutto di una valutazione personale dopo ricerche online, incrociate con le risposte agli stessi prompt e le valutazioni delle risposta fornite da Qwen 3.5 9B, sottoposte a Claude e DeepSeek. È il giudizio di un utente esigente, non la sentenza di un benchmark.

### Test 1 — Ragionamento scientifico: il meccanismo di Higgs

Il primo test era un classico da benchmark di alto livello: spiegare il meccanismo di Higgs e la rottura della simmetria elettrodebole a uno studente universitario di fisica. Una domanda che richiede rigore matematico senza sacrificare la chiarezza, e la capacità di costruire un percorso narrativo che guidi il lettore attraverso concetti non banali.

La risposta è arrivata strutturata in cinque sezioni che avanzavano con la logica di una lezione ben condotta: dall'inquadramento del problema della massa nei bosoni di gauge, all'introduzione del campo di Higgs con il suo potenziale a "cappello messicano" come immagine mentale, fino alla spiegazione del meccanismo per cui i bosoni W e Z "bevono" i bosoni di Goldstone acquisendo massa mentre il fotone rimane privo di massa grazie alla simmetria residua. Ogni formula era accompagnata da un'interpretazione fisica; ogni passaggio tecnico aveva una frase che ne rivelava il senso fisico profondo. Le verifiche incrociate con i modelli di frontiera, e ricerche personali online, hanno trovato la risposta corretta, ben strutturata e con le metafore giuste. Non banale per un modello che gira su un PC consumer.

**Voto: 5/5.** Il rigore c'era, la chiarezza anche. La capacità di scegliere metafore appropriate anziché limitarsi a riprodurre nozioni è ciò che ha sorpreso di più.

### Test 2 — Multimodalità: leggere il caos visivo

Per il secondo test ho scaricato online un'immagine piccola e di bassa qualità che mostrava un foglio di calcolo con l'inventario di un negozio di elettronica: nove colonne con codici articolo, nomi di prodotti, date di acquisto, categorie, quantità, costi e prezzi di vendita. L'immagine era deliberatamente scadente, leggermente sfocata, e ho caricato il file direttamente in LM Studio chiedendo al modello di descrivere cosa vedeva.

Il modello ha letto tutte le colonne e i valori numerici, ma la parte interessante è venuta dopo: ha notato autonomamente che la colonna "Totale" era il prodotto di quantità per prezzo unitario, ha identificato alcuni monitor con vendite a zero interpretandoli come potenziale merce invenduta, ha distinto articoli a basso costo come i mouse da prodotti premium come i processori, e ha riconosciuto che le date di acquisto coprivano un arco da ottobre 2017 a dicembre 2018. Non si è limitato a trascrivere: ha interpretato i dati come farebbe un analista.

Qualche dettaglio numerico minore è stato riportato in modo impreciso, il che è comprensibile data la qualità dell'immagine. Ma la capacità di passare dalla lettura alla comprensione contestuale è esattamente ciò che distingue una multimodalità decorativa da una multimodalità funzionale.

**Voto: 4.8/5.** La lettura era corretta, l'analisi di business intelligence aggiunta era un bonus inaspettato. Qualche virgola di punto persa per qualche imprecisione numerica minore.

### Test 3 — Generazione di codice: un problema NP-hard

Il terzo test era sul coding, l'area dove i benchmark suggeriscono che Qwen 3.5 9B sia leggermente meno brillante rispetto ad altre. Ho chiesto di implementare in Python un algoritmo per trovare il ciclo di lunghezza massima in un grafo non orientato, un problema NP-hard che richiede non solo capacità implementativa ma consapevolezza teorica.

La prima risposta si è interrotta a metà per un problema tecnico di gestione dell'output lungo, un comportamento da segnalare onestamente. Sollecitato a completare, il modello ha prodotto una soluzione completa con backtracking e pruning, l'approccio corretto per questo tipo di problema, con type hints, metodi ben separati e commenti pertinenti. Ma il dettaglio che ha colpito di più è arrivato prima ancora del codice: il modello ha dichiarato esplicitamente che il problema è NP-hard, che non esiste un algoritmo a tempo polinomiale conosciuto, e che per grafi di grandi dimensioni si dovrebbe considerare un approccio approssimato. Questa consapevolezza dei limiti teorici prima ancora di scrivere codice è il segnale di qualcosa di più profondo della semplice generazione di sintassi.

**Voto: 5/5.** L'intoppo iniziale va segnalato, ma la soluzione finale e la maturità teorica dimostrata hanno superato le aspettative per un modello da 9 miliardi di parametri.

---

*La puntata si chiude qui. Nella seconda parte: il test di pianificazione multilingua, la sfida con un PDF di 460 pagine e il ragionamento visuo-spaziale su una stanza nel caos. Più le conclusioni su cosa significa davvero avere un assistente locale nel 2026.*
