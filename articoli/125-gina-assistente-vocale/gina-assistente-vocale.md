---
tags: ["Generative AI", "Ethics & Society", "Applications"]
date: 2026-05-13
author: "Dario Ferrero"
youtube_url: "https://youtu.be/yM7h0a9xDSw?si=LEv6gMCt2gDb7X7e"
---

# Alexa? No Gina! Il mio assistente vocale, locale e auto costruito
![gina-assistente-vocale.jpg](gina-assistente-vocale.jpg)

*Tutto è iniziato in modo quasi banale, con quella specie di prurito intellettuale che spinge a smontare gli oggetti per capirne il meccanismo. Da anni conviviamo con assistenti vocali commerciali: Alexa sul comodino, Google Assistant sul telefono, qualche Siri sparsa in mezzo. Onestamente non li uso, ma osservando gli altri, c'è sempre stata una sensazione di fondo difficile da ignorare, la sensazione che ogni conversazione finisca da qualche parte lontana, su server sconosciuti, gestiti da aziende opache.*

Non è paranoia. Come ho scritto nell'articolo ["AI Creativity & Ethics"](https://aitalk.it/it/ai-creativity-ethics.html), il problema della gestione dei dati personali nell'era dell'intelligenza artificiale è concreto e documentato. Ogni richiesta, ogni sfumatura vocale, ogni "Alexa, metti la musica" diventa un tassello di un profilo comportamentale che non ho mai firmato di voler costruire.

Da questo prurito è nata **GINA**, il mio assistente vocale personale, completamente open source e interamente locale. Non un prodotto, non qualcosa di rilasciato al pubblico con pretese: un esperimento di apprendimento, la storia di qualcuno che ha voluto capire come funzionano davvero queste cose costruendone una da zero.

C'è però un contesto più largo in cui questa storia si inserisce. Proprio in questi mesi ho letto e scritto molto sugli **Small Language Models**, quei modelli linguistici compatti che girano su hardware normale, come ho raccontato in ["Gli Small Language Models conquisteranno il 2026?"](https://aitalk.it/it/slm-2026.html). L'idea che l'intelligenza artificiale possa smettere di essere un privilegio del cloud e diventare qualcosa di [domestico, modificabile, personale](https://aitalk.it/it/gemma4-26b.html), è qualcosa che mi affascina visceralmente. GINA è la dimostrazione pratica che questo futuro è già iniziato.

## Prima di sporcarsi le mani: gli obiettivi

Ogni progetto ha bisogno di un confine, altrimenti diventa infinito. Prima di scrivere una sola riga di codice ho cercato di chiarire a me stesso cosa volessi ottenere.

L'obiettivo principale era imparare davvero, non guardare da fuori. Costruire un sistema complesso partendo da zero, mettere insieme tasselli diversi (riconoscimento vocale, modelli linguistici, sintesi vocale, controllo di file e applicazioni) è l'unico modo per capire veramente come funziona ciascun pezzo. Il secondo obiettivo era sperimentare con gli SLM sul campo, non solo leggerli nei benchmark: testare Qwen, Mistral e Gemma su un hardware normale e vedere cosa sapevano fare davvero. Il terzo, irrinunciabile, era la privacy totale. Un assistente che funziona completamente in locale, senza nessuna chiamata verso server esterni, senza nessun dato che esca dal perimetro del mio PC. Il quarto obiettivo, forse il più pragmatico, era ottenere qualcosa di utile: lista della spesa, promemoria, musica, annotazioni veloci. Non solo un esercizio teorico, ma uno strumento da usare ogni giorno.

## Capitolo 1 — Perché locale? Il valore della privacy e degli SLM

### La svolta silenziosa dei modelli compatti

Fino a pochi anni fa, eseguire un modello di linguaggio sul proprio computer era un'idea assurda. Servivano cluster di GPU da decine di migliaia di dollari, data center raffreddati a liquido, budget energetici da piccola industria. I grandi modelli addestrati da OpenAI, Google, Anthropic, richiedono infrastrutture che un singolo individuo non potrà mai possedere.

Ma qualcosa sta cambiando in modo silenzioso e radicale. Come ho documentato nell'articolo sugli SLM, stiamo vivendo una controtendenza: non c'è bisogno di modelli enormi per la maggior parte delle attività quotidiane. Un modello da 7 o 9 miliardi di parametri, ben istruito e ottimizzato, può fare cose sorprendenti su un normale PC da gaming o da lavoro. I numeri sono eloquenti: Phi-3.5-Mini di Microsoft, con i suoi 3,8 miliardi di parametri, eguaglia GPT-3.5 su benchmark matematici usando il 98% di potenza computazionale in meno. Llama 3.2 da 3 miliardi batte modelli da 70 miliardi su task specifici dopo fine-tuning mirato.

Non è più una questione di "quanto grande", ma di "quanto efficiente". È una svolta che ricorda, per certi versi, la transizione dai mainframe ai personal computer: la potenza che era appannaggio di pochi sta diventando domestica.

### Tre problemi degli assistenti commerciali

Gli assistenti vocali commerciali hanno indubbiamente dei pregi, sono comodi, veloci, integrati con centinaia di servizi. Ma presentano limiti strutturali che, per qualcuno che tiene alla propria autonomia digitale, sono difficili da digerire.

Il primo è la dipendenza da internet: senza connessione, Alexa non riesce nemmeno a dire "Buongiorno". Il suo "cervello" sta su server remoti, e se la linea cade l'assistente diventa un soprammobile. Il secondo è economico: molti servizi avanzati sono ormai a pagamento, e le API dei modelli linguistici hanno costi che, per quanto contenuti, esistono. Il terzo, il più importante, è la privacy. Quando parlo con un assistente commerciale, le mie parole finiscono su server di terze parti. Non ho garanzie concrete su cosa venga registrato, per quanto tempo venga conservato, o come venga eventualmente usato. E per i più sospettosi, che non sia sempre in ascolto.

Con un assistente locale, questi problemi semplicemente spariscono. I dati restano sul mio PC. Nessun server esterno, nessuna registrazione, nessun profilo comportamentale costruito alle mie spalle.

### L'hardware di partenza

Prima di iniziare ho fatto l'inventario della mia postazione: un AMD Ryzen 7, 32 GB di RAM e una GPU con 16 GB di VRAM. Niente di esotico, un computer da lavoro o da gaming medio-alto, niente più. Con questo hardware posso eseguire comodamente modelli da 7 a 9 miliardi di parametri. Mi sono spinto sino ai 26 di Gemma4 raggiungendo il limite senza perdere in prestazioni, e per un assistente vocale la reattività è fondamentale.

Questo è il punto che più mi affascina dell'intera vicenda: non serve un supercomputer per fare IA utile. Con hardware consumer e modelli ben progettati, si ottengono risultati sorprendenti. È la promessa degli SLM, e GINA ne è la dimostrazione concreta.

## Capitolo 2 — L'architettura: come ho immaginato GINA

Prima di scrivere una sola riga di codice ho disegnato l'architettura del sistema. Volevo qualcosa di modulare, comprensibile, facile da estendere. L'idea di fondo era semplice: un flusso lineare in cui la voce entra, viene convertita in testo, il testo viene elaborato da un modello linguistico, e la risposta viene letta ad alta voce.
![schema1.jpg](schema1.jpg)

Ogni componente ha un ruolo preciso. **Vosk** è il motore di riconoscimento vocale, le orecchie di GINA. **LM Studio** è il cervello, il server locale che esegue il modello linguistico e risponde alle richieste. **pyttsx3** è la voce, una libreria che usa le voci di sistema di Windows. Il **tool calling** è il sistema che permette a GINA di fare cose concrete nel mondo reale, non solo chiacchierare.

### LM Studio e i modelli testati

Ho scelto LM Studio per la sua semplicità d'uso: scarichi un modello, lo carichi, clicchi un pulsante e hai un server API compatibile con OpenAI che gira sulla porta 8001 del tuo PC. L'applicazione stessa non è open source, ma supporta tutti i principali modelli open weight e, cosa fondamentale, i dati non escono mai dal computer. Chi preferisse una soluzione completamente open source può sostituirla con [Ollama](https://ollama.com/) (licenza Apache 2.0) mantenendo invariato il resto del codice.

Ho testato tre modelli nel corso del progetto, ognuno con le proprie caratteristiche. **Qwen 3.5 9B** è pensato per il tool calling: ha un supporto nativo eccellente per le funzioni (riconoscibile nell'interfaccia di LM Studio dall'icona a forma di martello) e ha gestito quasi sempre correttamente le chiamate ai tool. **Gemma 4 26B A4B** di Google usa un'architettura "Mixture of Experts" particolarmente efficiente: su 26 miliardi di parametri totali ne attiva solo 4 miliardi per ogni richiesta, il che lo rende sorprendentemente reattivo ne ho scritto in dettaglio in ["Gemma 4 26B"](https://aitalk.it/it/gemma4-26b.html). **Mistral Devstral Small 2** è invece un modello di circa 12 miliardi di parametri, molto reattivo e con una buona comprensione generale, e il tool calling risulta sorprendentemente affidabile. Su una GPU con 16 GB di VRAM tutti e tre girano in modo fluido, con latenze accettabili per una conversazione vocale.

### Le librerie Python

Per chi vuole replicare o ispezionare il progetto, ecco le librerie usate e il loro ruolo: `vosk` e `sounddevice` gestiscono l'acquisizione e il riconoscimento audio; `numpy` lavora sugli array audio grezzi; `requests` fa le chiamate all'API di LM Studio e a Telegram; `pyttsx3` si occupa della sintesi vocale; `queue` e `threading` gestiscono i promemoria asincroni; `json` rende persistente lista della spesa, note e promemoria; `re` pulisce il testo dal markdown prima della lettura vocale; `glob`, `random` e `subprocess` gestiscono la riproduzione musicale; `shutil` e `datetime` completano il quadro con backup e timestamp. Tutte open source, tutte installabili con un semplice `pip install`.
![gina-avvio.jpg](gina-avvio.jpg)
*Ecco come appare Gina all'avvio*

## Capitolo 3 — Lo sviluppo passo passo: dal microfono alla mente

Lo sviluppo ha proceduto per fasi successive, ognuna con i suoi imprevisti e le sue soluzioni.

### Fase 1: le orecchie

La prima cosa da fare era far sì che GINA potesse sentirmi. Il tentativo iniziale è stato con **Whisper** di OpenAI, il gold standard per il riconoscimento vocale. Ma quasi subito ho incontrato un ostacolo: Whisper richiede `ffmpeg` per decodificare l'audio, e su Windows l'installazione non è banale. Inoltre, la libreria `pyaudio` necessaria per accedere al microfono non era ancora compatibile con Python 3.14, l'ultima versione che uso per altri progetti.

Ho allora cercato un'alternativa e ho trovato **Vosk**, un motore di riconoscimento vocale leggero e interamente locale. I suoi vantaggi sono concreti: non richiede ffmpeg, funziona con `sounddevice` invece di `pyaudio` (molto più semplice da installare su Windows), ha un modello per l'italiano di circa 50 MB scaricabile gratuitamente e ha una latenza di circa 200 ms su CPU. L'unico svantaggio è una precisione leggermente inferiore a Whisper in ambienti rumorosi, ma per comandi vocali del tipo "aggiungi latte" o "ricordami di chiamare Mario" si è rivelato più che sufficiente.

Ho implementato l'ascolto in **streaming continuo**: GINA ascolta finché non rileva un silenzio di almeno 2 secondi, poi elabora la frase. Questo approccio è più naturale rispetto a dover premere un pulsante ogni volta.

### Fase 2: la connessione al cervello

Con l'input vocale risolto, ho collegato GINA a LM Studio. L'API è compatibile con quella di OpenAI, quindi una semplice chiamata `requests.post` verso `http://localhost:8001/v1/chat/completions` è bastata. Ho strutturato la conversazione con una cronologia (`messages`) che include un prompt di sistema con le istruzioni per GINA e gli scambi precedenti.

La prima sfida inaspettata è stata gestire questa cronologia. Senza un limite, dopo decine di messaggi la richiesta diventava troppo grande e LM Studio rispondeva con un errore 400. Ho implementato un meccanismo di reset automatico: quando la cronologia supera le 10 interazioni, viene troncata mantenendo solo il prompt di sistema e gli ultimi scambi. GINA "perde" un po' di contesto recente, ma l'esperienza rimane accettabile.

### Fase 3: la voce

Per la sintesi vocale ho usato `pyttsx3`, che sfrutta le voci SAPI di Windows. La qualità è funzionale, anche se un po' meccanica. Il problema immediato è emerso quasi subito: i modelli LLM amano formattare le risposte in markdown, e `pyttsx3` leggeva letteralmente asterischi, underscore e backtick, "asterisco asterisco 2 asterisco asterisco è un numero primo" non è esattamente gradevole. Ho scritto una funzione `clean_text_for_tts()` che, con alcune regex, rimuove o sostituisce tutti i caratteri di markdown prima della lettura. Ora GINA legge solo testo pulito.
![gina-diretta.jpg](gina-diretta.jpg)
*Gina risponde a una domanda diretta sulla conoscenza interna*

## Capitolo 4 — Il cuore del progetto: il tool calling

Il "tool calling" è la vera magia di GINA. Senza di esso sarebbe solo un chatbot che risponde a voce. Con il "tool calling" può fare cose concrete nel mondo reale.

Il meccanismo funziona così: l'utente dice qualcosa ("aggiungi latte alla lista della spesa"), Vosk trascrive la frase in testo, il testo viene inviato a LM Studio insieme alla lista dei tool disponibili (ognuno descritto in JSON con nome, descrizione e parametri attesi), il modello capisce che per soddisfare la richiesta deve chiamare `add_to_shopping_list` con parametro `item_name = "latte"` e risponde con una richiesta di tool call invece che con testo. Il mio script Python intercetta questa richiesta, esegue la funzione Python corrispondente, rimanda il risultato al modello, e il modello genera la risposta vocale finale: "Ho aggiunto latte alla lista della spesa."

La bellezza di questo meccanismo è che è **infinitamente estendibile**: basta aggiungere una nuova funzione Python e descriverla nel JSON dei tool, e il modello imparerà ad usarla senza bisogno di nessun altro addestramento.

### La lista della spesa

Il tool più semplice e quotidianamente utile è la gestione della lista della spesa. Tre funzioni, `add_to_shopping_list`, `get_shopping_list`, `remove_from_shopping_list`, leggono e scrivono un file JSON con la lista, ogni articolo corredato di timestamp e di un flag `checked`. Funziona esattamente come ci si aspetta, con una naturalezza che sorprende ancora ogni volta.
![gina-spesa.jpg](gina-spesa.jpg)
*Gina elenca la lista della spesa.*

### Ricerca online (con consenso esplicito)

C'è una funzionalità che merita un discorso a parte, perché rompe deliberatamente il principio del "tutto locale". GINA può cercare informazioni sul web tramite DuckDuckGo, meteo, notizie, fatti recenti, ma solo previo consenso esplicito dell'utente.

Il motivo di questa scelta è semplice: una ricerca online è l'unico momento in cui qualcosa esce dal perimetro del PC, e volevo che fosse una decisione consapevole, non qualcosa che avviene in modo silenzioso e automatico. Quando la richiesta richiede dati che il modello non può avere (informazioni in tempo reale, eventi recenti), GINA chiede conferma prima di procedere.

Se l'utente accetta, la query viene inviata a DuckDuckGo, il risultato viene passato al modello come contesto aggiuntivo, e la risposta viene letta ad alta voce. Se l'utente preferisce non usare internet, il modello risponde con quello che sa, o ammette onestamente di non saperlo.

È un compromesso pragmatico: la privacy rimane la regola, la connessione l'eccezione consapevole.
![gina-online.jpg](gina-online.jpg)
*Gina fa una ricerca online sul meteo a Roma, dopo richiesta di consenso esplicito.*

### Note vocali

Un'altra funzione che uso quotidianamente è quella degli appunti vocali. Quante volte capita di pensare "devo ricordarmi di fare questo" e poi dimenticare? Con GINA basta dire "segna: leggere articolo su AiTalk domani" e il tool `add_note` salva la frase in `notes.json` con un timestamp. Poi si può chiedere "leggi le note" e GINA elenca le ultime annotazioni. Semplice, ma utilissimo.

### Promemoria temporali

La funzione più complessa da implementare è stata quella dei promemoria temporali. L'obiettivo era poter dire "ricordami di chiamare Mario tra 10 minuti" e che GINA effettivamente lo facesse, anche nel mezzo di una conversazione su altro.

La sfida era tecnica: il programma principale è in ascolto continuo della wake word "Gina". Se avessi implementato un semplice `time.sleep()` nel thread principale, l'assistente si sarebbe bloccato fino allo scadere del timer, incapace di rispondere a qualsiasi altra cosa. La soluzione è stata usare un thread separato per il controllo dei promemoria e una coda (`queue`) per comunicare col thread principale in modo thread-safe. Un thread di background controlla ogni 10 secondi se ci sono promemoria scaduti nel file `reminders.json`; quando ne trova uno, invece di chiamare direttamente la funzione vocale (non thread-safe), mette il testo in una coda; un secondo thread legge continuamente dalla coda e, quando riceve un messaggio, lo fa leggere a GINA. Così l'assistente può ricordarti di chiamare Mario anche se sono passati 10 minuti senza che tu abbia detto nulla.
![gina-promemoria.jpg](gina-promemoria.jpg)
*Il file json in cui Gina registra una nota temporale, per avvisarti al momento giusto*

### Controllo multimediale

Per la musica ho creato una cartella `Musica/` nella stessa directory dello script. Il tool `search_and_play_music` cerca nella cartella i file audio con le estensioni standard, fa una ricerca per corrispondenza parziale se l'utente specifica un nome, sceglie un file a caso se l'utente dice genericamente "metti un po' di musica", e riproduce il file con il lettore predefinito del sistema tramite `os.startfile`. Semplice ed efficace.

### Condivisione su Telegram

L'ultima estensione pratica è l'invio della lista della spesa su Telegram. Prima di uscire posso dire "Gina, mandami la lista" e ricevo un messaggio su un bot Telegram che ho creato (@GinaShoppingBot). Arrivo al supermercato, apro Telegram, e ho la lista pronta. Il bot è gratuito, facile da configurare parlando con @BotFather, e la persistenza è totale: il messaggio resta nella chat fino a quando non lo cancello.
![gina-telegram.jpg](gina-telegram.jpg)
*Il messaggio inviato su Telegram con la lista, dopo specifica richiesta.*

## Capitolo 5 — L'esperimento visionario: GINA che modifica il proprio codice

Con un assistente funzionante e ricco di funzionalità, ho voluto spingermi oltre. L'idea era quasi fantascientifica: e se GINA potesse modificare il proprio codice sorgente?

L'immagine è potente, un assistente che impara, si evolve, si migliora da solo. Non più un programma statico, ma qualcosa in continua trasformazione. Quasi Philip K. Dick, più che informatica applicata.

### L'implementazione

Ho creato il tool `modify_code_file`. Il flusso era questo: l'utente dice "Gina, modifica il file test.py, aggiungi una funzione che saluta l'utente"; GINA riceve la richiesta e chiama il tool con il nome del file e l'istruzione; il tool legge l'intero file, lo passa al modello come contesto insieme all'istruzione di modifica, e chiede di generare la nuova versione; il modello restituisce il codice modificato; il tool salva la nuova versione in nella cartella `Codice/` nella root del progetto, in un nuovo file, lasciando intatto l'originale.

Per sicurezza, GINA può modificare i file solo nella cartella `Codice/`, all'interno del progetto, dove si trovano solo file messi dal'utente. L'utente può ispezionare il risultato e, solo se soddisfatto, sostituire manualmente l'originale.

### Il successo parziale

Il tool funziona perfettamente su file piccoli. Ho creato un `test.py` di una ventina di righe, ho chiesto a GINA di aggiungere una funzione, e in pochi secondi ho avuto `test_modificato.py` con la funzione richiesta. Magia, letteralmente.

Ma con il file `gina_assistente.py` stesso, circa 1000 righe, il sistema ha mostrato i suoi limiti. LM Studio impiegava molto tempo per processare la richiesta, andava spesso in timeout, e quando riusciva a completare la risposta era troncata o malformata.

### Il limite tecnico come lezione

Il problema è probabilmente la **finestra di contesto** dei modelli. I modelli che ho usato hanno contesti limitati. Il mio file `gina_assistente.py` supera abbondantemente questa soglia, il modello non ha abbastanza spazio per elaborarlo interamente e rigenerarlo con le modifiche. Devo tuttavia ancora analizzare in modo approfondito la questione.

Questo fallimento è istruttivo quanto qualsiasi successo. Nell'articolo sugli SLM avevo scritto che questi modelli sono come "bisturi chirurgici", eccellenti in compiti specifici e circoscritti, mentre i grandi modelli sono i "coltellini svizzeri" che fanno tutto decentemente. Il tool di modifica codice è la dimostrazione pratica: fallisce su un task enorme (modificare un file di 1000 righe), ma eccelle su task piccoli e mirati.

Ho deciso di mantenere il tool nel progetto come esperimento visionario più che come funzionalità stabile. L'idea è affascinante, il potenziale è reale, e in futuro con modelli dal contesto più ampio potrebbe diventare pienamente praticabile.
![gina-codice.jpg](gina-codice.jpg)
*Gina ha creato il gioco di Snake perfettamente funzionante al primo tentativo*

## Capitolo 6 — Le incoerenze dei modelli: vivere con il non-determinismo

Nessun progetto complesso è privo di imperfezioni. GINA ha i suoi, e vale la pena raccontarli.

### Il problema del delay

Una delle prime difficoltà è stato il ritardo tra la wake word e l'effettivo ascolto del comando. Il flusso originale prevedeva che GINA, sentita la parola "Gina", rispondesse "Dimmi?" e poi iniziasse ad ascoltare. Ma dato che la risposta vocale durava circa un secondo, le prime parole del comando andavano sistematicamente perse. Ho provato spostando l'inizio dell'ascolto prima della risposta vocale, ma Gina finiva con ascoltare se stessa e attivarsi. Al momento, ho accettato la breve attesa prima di poter parlare, ma conto di trovare una soluzione.

### Vosk: preciso ma non infallibile

Vosk è eccellente in ambienti silenziosi. Se c'è rumore di fondo, la precisione cala. È un problema noto e accettabile per un progetto personale. Per un'applicazione professionale servirebbe un sistema dedicato come Porcupine, ma per i miei usi quotidiani Vosk fa ampiamente il suo lavoro.

### La natura non deterministica degli LLM

Questa è forse la caratteristica più affascinante, e a volte frustrante, dei modelli linguistici: non sono deterministici. A parità di input, possono dare risposte diverse.

Un esempio concreto: se dico "Gina, metti un po' di musica", a volte il modello chiama correttamente il tool `search_and_play_music` e riproduce un brano "a sua scelta" dalla cartella `Musica/`. Altre volte risponde: "Ecco un brano perfetto per questo momento: Bohemian Rhapsody dei Queen." E poi, ovviamente, non suona nulla perché il file non esiste. Non è un bug, è il modello che ha imparato da miliardi di testi che "metti un po' di musica" è spesso seguito da un suggerimento musicale, e a volte sceglie quella strada invece di chiamare il tool.

Allo stesso modo, la ricerca del meteo a volte funziona correttamente, altre volte il modello risponde: "Per informazioni meteorologiche precise, ti consiglio di consultare un sito specializzato." Questa variabilità è normale e va accettata. È il prezzo da pagare per avere un sistema creativo e non rigidamente deterministico, e in fondo, è anche ciò che rende l'interazione più umana, nel bene e nel male.

Entrambi i problemi, potrebbero essere mitigati con un affinamento del Prompt di sistema, è un aspetto sul quale lavorare.

## Capitolo 7 — Conclusioni: cosa funziona, cosa manca, dove si va

Il progetto è riuscito oltre le mie aspettative iniziali. GINA funziona, è stabile, e la uso quotidianamente. Si avvia con un doppio click su un file `.bat` sul desktop, ed è pronta in pochi secondi.

### Cosa sa fare oggi

Con GINA posso gestire la lista della spesa (aggiungere, visualizzare, rimuovere articoli) e inviarla su Telegram prima di uscire. Posso registrare note e promemoria non temporali. Posso impostare promemoria temporali ("ricordami di chiamare Mario tra 10 minuti") e GINA li rispetta anche in mezzo ad altre conversazioni. Posso riprodurre musica dalla mia cartella locale, sia canzoni specifiche sia brani scelti a caso. Posso fare domande generali usando la conoscenza interna del modello. Posso fare ricerche online, previo consenso esplicito. Posso, su file piccoli, chiedere a GINA di modificare il codice. Il tutto senza che un bit esca dal mio PC.

### Dove c'è ancora da lavorare

L'autocritica è parte del metodo. La qualità della voce di `pyttsx3` è funzionale ma metallica: si potrebbe passare a Piper TTS (locale, qualità molto superiore) o a Edge TTS (online, qualità eccellente). La precisione della wake word potrebbe migliorare con Porcupine. Il riconoscimento vocale potrebbe essere più preciso con Whisper, a costo di qualche dipendenza in più. L'interfaccia oggi è solo a riga di comando: una semplice interfaccia web in Streamlit o Flask la renderebbe più accessibile. E la modifica di file grandi resta un limite tecnico aperto.

### Un mondo di possibilità

Ciò che amo di più di GINA è che può essere estesa all'infinito. Alcune idee che ho in lista: un'interfaccia web per vedere lista della spesa, note e promemoria anche da remoto; integrazione con il calendario ("Gina, che impegni ho domani?"); controllo di dispositivi smart home.

Ma la cosa più importante è quello che questo progetto dimostra a livello più ampio. GINA non è solo un assistente vocale personale: è una **piattaforma dimostrativa** del potenziale degli Small Language Models in locale. Prova che non serve affidarsi ai giganti del cloud per avere intelligenza artificiale utile, personale e rispettosa della privacy.

Il trend che ho descritto in ["Small Language Models per il 2026"](https://aitalk.it/it/slm-2026.html) è già realtà, e si tocca con mano. Con modelli come Qwen, Gemma 4 e Mistral, un normale PC da gaming può eseguire un assistente vocale sofisticato, con latenza inferiore al secondo, senza consumare risorse eccessive.

E la parte migliore è che tutto questo è **open source**: modificabile, migliorabile, adattabile a qualsiasi esigenza. Ho imparato moltissimo costruendo questo progetto, ho avuto conferma che l'intelligenza artificiale non è solo ChatGPT e API a pagamento. È anche curiosità, sperimentazione, il piacere di sedersi al computer, scrivere codice, e vedere qualcosa che hai costruito prendere vita e risponderti.

Spero che questo racconto ispiri qualcuno a intraprendere un viaggio sperimentale. E se lo farà, GINA li aspetta, pronta ad ascoltare la loro prima parola.

*"Gina"*

---

## Appendice tecnica: come iniziare

Tutto il codice è disponibile sul [repository GitHub](https://github.com/Dario-Fe/Gina-Assistant). Lo script principale è `gina_assistant.py`; i file di memoria per i vari tool (`shopping_list.json`, `notes.json`, `reminders.json`) vengono creati automaticamente al primo avvio. La cartella `Musica/` e la cartella `Codice/` sono opzionali, se si desidera usare GINA per ascoltare musica o per scrivere codice, crea le cartelle nella root del progetto, mettici le tue canzoni preferite, o i file con il codice da modificare o da creare da zero.

Per avviare GINA:
![schema2.jpg](schema2.jpg)