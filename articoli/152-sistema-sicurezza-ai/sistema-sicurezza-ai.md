---
tags: ["Generative AI", "Applications", "Security"]
date: 2026-07-15
author: "Dario Ferrero"
youtube_url: "https://youtu.be/mlf76oZhQPw?si=2HdUJbVqEyHpBdlL"
---

# Ho insegnato all'AI a fare la guardia: come ho costruito un sistema di sicurezza a costo zero
![sistema-sicurezza-ai.jpg](sistema-sicurezza-ai.jpg)

*Nella serie televisiva 'Person of Interest', una superintelligenza soprannominata semplicemente "la Macchina" sorveglia ogni angolo del pianeta attraverso telecamere, microfoni e sensori di ogni tipo, individuando minacce prima che si materializzino. È fantascienza, naturalmente. Ma l'idea di fondo, ovvero usare la visione artificiale per capire cosa succede in un ambiente, è ormai accessibile a chiunque abbia un PC e una webcam. Meno di 250 righe di codice. Nessun abbonamento, nessun cloud, nessun video che gira per il mondo. Solo una notifica sul telefono, con foto, quando qualcuno entra in casa.*

La domanda che mi sono posto qualche settimana fa era semplice: quanto costa un sistema di sicurezza che ti avvisa in tempo reale se qualcuno entra in casa, ti manda una foto, e gira interamente in locale senza dipendere da un abbonamento mensile? La risposta: zero euro. Solo hardware che con ogni probabilità già possiedi. In questo articolo racconto come ho costruito quel sistema, cosa ho imparato lungo la strada, e perché l'esperimento dice qualcosa di più grande sul modo in cui l'intelligenza artificiale sta cambiando il rapporto tra tecnologia e quotidianità.

## Prima di puntarla a casa: il collaudo a Times Square

Ogni sistema di sicurezza degno di questo nome va testato prima di essere messo in produzione. Ma puntare una webcam sulla propria stanza senza aver verificato il funzionamento in condizioni impegnative sembrava ingenuo. Così ho deciso di iniziare dal contesto più caotico che potessi trovare senza muovermi dalla sedia: Times Square, New York, vista dall'alto attraverso una delle tante webcam pubbliche accessibili in streaming.

Lo scenario era deliberatamente estremo. Centinaia di persone che si incrociano, taxi gialli, autobus, camion delle consegne, tutto in movimento simultaneo, con variazioni di luce repentine e angolazioni difficili. Il tipo di situazione che mette in crisi qualsiasi sistema di riconoscimento visivo mediocre.

Il risultato è stato sorprendente: il sistema ha riconosciuto fino a nove veicoli contemporaneamente tra auto, bus e camion, ha individuato pedoni anche a distanza considerevole, ha mantenuto 40 fotogrammi al secondo stabili, tutto su una CPU, senza toccare la GPU. *"Se funziona su Times Square, funziona ovunque"* mi sono detto. E così è stato.
![timesquare.jpg](timesquare.jpg)
*Screenshot dei test fatti sulla webcam di Time Square.*

## Il cuore del sistema: YOLO spiegato semplice

Prima di arrivare al momento in cui il telefono ha vibrato con la prima foto di allarme, vale la pena spendere qualche riga su cosa succede sotto il cofano, perché la tecnologia coinvolta è genuinamente affascinante anche se la si guarda da lontano.

Il componente centrale si chiama [YOLO](https://github.com/ultralytics/ultralytics), acronimo di *You Only Look Once*. Il nome non è marketing: descrive esattamente come funziona. I sistemi di riconoscimento visivo tradizionali analizzavano un'immagine in più passaggi, prima identificando le regioni di interesse e poi classificandole. YOLO ribalta l'approccio: analizza l'intera immagine in un unico passaggio, dividendola in una griglia e prevedendo simultaneamente posizione e tipo di oggetto per ogni cella. Il risultato è una velocità notevolmente superiore, con una precisione che sulle versioni recenti ha raggiunto livelli eccellenti.

La versione che ho usato, YOLOv8n, è la variante più leggera della famiglia. Il suffisso "n" sta per *nano*, ed è progettata esplicitamente per girare su hardware limitato. È addestrata sul dataset COCO, che comprende ottanta categorie di oggetti: persone, veicoli, animali domestici, oggetti d'arredo. Per i miei scopi, l'unica categoria che mi interessa è "persona", con una soglia di confidenza fissata a 0,4, ovvero il modello segnala una presenza solo quando è sicuro almeno al quaranta per cento di averla rilevata. Una soglia più bassa produce più falsi allarmi, una più alta rischia di perdere rilevamenti reali.

Il secondo ingrediente cruciale è [ONNX](https://onnxruntime.ai/), che sta per *Open Neural Network Exchange*. È un formato aperto per rappresentare modelli di machine learning, ma soprattutto è un motore di inferenza ottimizzato che sa come sfruttare al meglio le istruzioni specifiche di ogni processore. Quando esporti YOLOv8n in formato ONNX, il modello passa da 10-15 fotogrammi al secondo a 40-45 fotogrammi al secondo sulla stessa CPU, senza cambiare una sola riga di codice applicativo. Il file passa da 6 MB a 12 MB, ma il guadagno di velocità è quasi quadruplicato. È come avere un traduttore simultaneo che conosce perfettamente il dialetto del tuo processore.

## GINA mi presta il bot

Chi segue questo portale ricorderà [GINA, il mio assistente vocale personale](https://aitalk.it/it/gina-assistente-vocale.html). Per le notifiche in tempo reale avevo già costruito un bot Telegram integrato nell'ecosistema di GINA, capace di inviarmi messaggi, aggiornamenti e avvisi direttamente sullo smartphone. Riutilizzare quella infrastruttura per il sistema di sicurezza è stato naturale: un classico esempio di come i pezzi di un ecosistema tecnologico costruito nel tempo inizino a incastrarsi in modi non sempre previsti.

Il bot Telegram fa una cosa sola, ma la fa bene: quando il sistema rileva una persona, riceve una chiamata HTTP con un messaggio di testo e una foto del frame incriminato, e li recapita sul mio telefono in due o cinque secondi. Nessuna app proprietaria, nessun account su piattaforme di videosorveglianza cloud, nessun dato che attraversa server di terze parti se non i server di Telegram per il recapito finale della notifica. In alternativa si potrebbe pensare all'invio di una email. Il video in sé non esce mai dal PC.

La configurazione del bot richiede circa cinque minuti: si crea tramite [@BotFather](https://core.telegram.org/bots) su Telegram, si ottiene un token di autenticazione, si recupera il proprio chat ID inviando un messaggio al bot e interrogando le API, e si inseriscono le due stringhe nel file di configurazione. Dopodiché il canale di notifica è operativo.

## Il momento della verità: la mia stanza

Superato il test newyorkese, era il momento di puntare la webcam sull'ambiente che contava davvero: la mia stanza. Ho posizionato la telecamera, avviato lo script, aspettato i cinque secondi di stabilizzazione che il sistema si prende all'avvio per non generare falsi allarmi durante il caricamento, e sono uscito dalla stanza.

Poi sono rientrato.

Il telefono ha vibrato prima ancora che raggiungessi il centro dell'inquadratura. Il messaggio recitava: *"🚨 ALLARME SICUREZZA! Persone rilevate: 1. Ora: 13:43:07. Allarme #1"*. Sotto, una foto con il mio contorno evidenziato da un riquadro e un overlay rosso nella parte alta del frame. Latenza dall'ingresso alla notifica: meno di un secondo per il riconoscimento, due-tre secondi per la consegna Telegram.

Funzionava.

Il sistema ha una logica di protezione dai falsi allarmi integrata: un cooldown di dieci secondi tra un allarme e il successivo impedisce che una persona ferma nell'inquadratura generi decine di notifiche al minuto. La soglia di confidenza a 0,4 si è rivelata ben calibrata per un ambiente domestico: nessun falso positivo durante i test, nessun riconoscimento mancato in condizioni di luce normale. Con illuminazione scarsa le prestazioni degradano, ma è un limite fisico della webcam prima ancora che del modello.
![allarme.jpg](allarme.jpg)
*Screenshot del messaggio d'Allarme su telegram, nonché del ladro più improbabile della storia della criminalità.*

## Come è costruito: la ricetta tecnica

Il codice completo occupa meno di 250 righe di Python. La struttura è lineare e comprensibile anche per chi non scrive codice professionalmente. Ci sono quattro blocchi logici: la configurazione iniziale con token Telegram e parametri di soglia, le funzioni di invio messaggi e foto via API Telegram, la funzione di rilevamento persone che interroga ONNX, e il ciclo principale che acquisisce i frame dalla webcam, li analizza e gestisce la logica degli allarmi.

Le dipendenze sono cinque librerie Python standard nell'ecosistema machine learning: `ultralytics` per caricare YOLO, `onnxruntime` per l'inferenza ottimizzata, `opencv-python` per la gestione della webcam e l'elaborazione dei frame, `requests` per le chiamate HTTP a Telegram.

La struttura finale del progetto è essenziale: un file Python principale, il modello ONNX da 12 MB, un file di configurazione. In tutto meno di 15-20 MB su disco.

Sul fronte prestazionale, i numeri parlano chiaro:
![tabella.jpg](tabella.jpg)

L'hardware usato è un AMD Ryzen 7 7700 con 32 GB di RAM, ma i test su configurazioni meno potenti confermano che il sistema funziona senza problemi anche su un laptop con processore Intel i5 di quinta o sesta generazione e 8 GB di RAM. La GPU non viene mai coinvolta.

## Dove ha senso usarlo e dove no

Un sistema di questo tipo funziona bene in contesti specifici, ed è onesto dirlo chiaramente. Per la sicurezza domestica in un appartamento o una piccola casa è efficace: monitora una stanza o un ingresso, avvisa in tempo reale, costa zero. Per sorvegliare un ufficio durante la chiusura notturna, un negozio dopo l'orario di chiusura, o un magazzino con accesso limitato, il sistema si presta altrettanto bene.

Non è invece un sostituto di un sistema di sicurezza professionale certificato per ambienti critici. I falsi negativi esistono, specialmente in condizioni di luce difficile. Il sistema non distingue tra chi ha le chiavi di casa e un intruso reale, almeno nella versione base. Non registra video, solo foto dei momenti di allarme. E gira su un PC che deve essere acceso e connesso a Internet per le notifiche.

Sul fronte legale, vale la pena ricordare che in Italia la videosorveglianza è regolata dal GDPR e dal Garante della Privacy. Per uso esclusivamente domestico, all'interno della propria proprietà privata, le restrizioni sono significativamente meno onerose che per ambienti pubblici o lavorativi. Se la telecamera inquadra spazi comuni o aree esterne condivise, entrano in gioco obblighi di cartellonistica e, in certi casi, di notifica al Garante. Il principio guida è semplice: informare le persone che l'area è monitorata è sempre la scelta corretta, non solo quella legale.
![log.jpg](log.jpg)
*Screenshot del terminale con il sistema in funzione, con il riconoscimento degli oggetti e l'allarme al momento dell'ingresso di una persona.*

## Le strade aperte

Il progetto nella sua forma attuale è un punto di partenza funzionante, non un punto di arrivo. Le estensioni naturali sono diverse, con complessità crescente.

Il passo successivo più ovvio è il riconoscimento facciale per distinguere i residenti dagli estranei. La libreria `face_recognition` di Python permette di costruire un archivio di volti noti e filtrare gli allarmi di conseguenza: se sono io che entro in casa, nessuna notifica. Se è qualcuno che il sistema non ha mai visto, allarme. Il codice aggiuntivo è poche decine di righe.

Un'integrazione con sensori PIR passivi, i classici sensori di movimento a infrarossi, permetterebbe di attivare YOLO solo in presenza di movimento, riducendo drasticamente il consumo energetico nei periodi di inattività. Nell'attuale implementazione la webcam gira e il modello analizza i frame in continuazione, anche quando la stanza è vuota da ore.

Il supporto multi-camera richiederebbe di istanziare più processi paralleli, uno per ogni webcam, con un sistema centralizzato di gestione degli allarmi. Una dashboard web leggera costruita con Flask o FastAPI permetterebbe di visualizzare lo stato del sistema da remoto. Tutte estensioni realizzabili con qualche giornata di lavoro.

## Locale vince (quasi sempre)

Ogni volta che costruisco qualcosa di questo tipo mi ritrovo a fare i conti con una domanda più ampia: perché farlo in locale quando esistono API cloud per la visione artificiale che funzionano con tre righe di codice?

La risposta non è ideologica. È pratica.

Come ho discusso in altri contesti su questo portale, i modelli locali hanno raggiunto un livello di maturità che rende la scelta tra locale e cloud genuinamente dipendente dal caso d'uso, non dall'assunzione automatica che il cloud sia sempre superiore. Per un sistema di videosorveglianza domestica, i vantaggi del locale sono difficilmente superabili: le immagini della propria casa non escono mai dal proprio PC, non ci sono costi variabili, il sistema funziona anche senza Internet una volta configurato, non c'è dipendenza da politiche di prezzo di terze parti che possono cambiare.

Il cloud vince in scenari diversi: quando servono decine di telecamere, quando la potenza di calcolo locale non è sufficiente, quando i modelli richiesti sono troppo grandi per girare in locale, quando la manutenzione dell'infrastruttura è un peso insostenibile. Ma per un esperimento domestico come questo, il cloud sarebbe stato un overhead senza benefici concreti.

C'è però una considerazione che vale sempre la pena esplicitare: ONNX e YOLOv8n sono strumenti maturi, documentati, con comunità attive. Non è magia nera riservata a specialisti. È ingegneria applicata che chiunque abbia curiosità e qualche ora a disposizione può replicare. Questa è forse la cosa più significativa dell'intero esperimento: non il sistema di sicurezza in sé, ma la dimostrazione che la distanza tra "tecnologia AI" e "cosa che funziona sul mio PC" si è accorciata al punto da diventare quasi irrilevante.

---

*Il codice è disponibile sul repository [GitHub Security-System-Yolo](https://github.com/Dario-Fe/Security-System-Yolo)*
