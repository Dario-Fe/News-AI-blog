---
tags: ["Generative AI", "Research", "Startups"]
date: 2026-03-13
author: "Dario Ferrero"
youtube_url: "https://youtu.be/YY12j9vUxI4?si=cMRokLIguMBg59rk"
---

# Mille token al secondo: Mercury 2 vuole riscrivere le regole dell'AI
![mercury2.jpg](mercury2.jpg)

*C'è un momento strano, quasi straniante, che chiunque abbia usato Mercury 2, di Inception Labs, per la prima volta descrive in modo simile: digiti la domanda, premi invio, e la risposta è già lì, per intero, prima ancora che il tuo cervello abbia finito di registrare che hai cliccato qualcosa. Non è un effetto visivo, non è un trucco di interfaccia. Il modello genera davvero oltre 1000 token al secondo.*

Per dare un ordine di grandezza: un romanzo medio italiano è circa 300.000 caratteri, ossia all'incirca 90.000-100.000 token. Mercury 2, in teoria, lo scriverebbe in meno di due minuti. Claude 4.5 Haiku, uno dei modelli "veloci" più diffusi oggi, si ferma a circa 89 token al secondo. GPT-5 Mini a circa 71. La differenza non è incrementale: è strutturale.

Tutto questo è possibile perché Mercury 2 non funziona come qualsiasi altro modello linguistico tu abbia mai usato. E capire perché richiede un passo indietro sul modo in cui l'intelligenza artificiale generativa produce testo, e su come, da sempre, lo ha fatto in un unico modo.

## Due famiglie, un paradigma dominante

Se vuoi capire Mercury 2, devi prima capire il collo di bottiglia che cerca di eliminare. E quel collo di bottiglia ha un nome tecnico preciso: generazione autoregressiva.

Tutti i grandi modelli linguistici che usi ogni giorno, ChatGPT, Claude, Gemini, funzionano secondo lo stesso principio di base: producono testo un token alla volta, da sinistra a destra, e ogni token dipende da tutti quelli che lo precedono. È come scrivere a macchina: non puoi battere la terza lettera prima di aver battuto la seconda. Questa dipendenza sequenziale è architettonica, non un'inefficienza eliminabile con più hardware o ottimizzazioni software. È la natura stessa del meccanismo.

La diffusion è qualcosa di diverso. La tecnica nasce nel mondo della generazione di immagini, è alla base di Stable Diffusion, Midjourney, DALL-E, e funziona in modo opposto: invece di costruire il risultato pezzo per pezzo, parte da un output completamente "rumoroso" e impreciso, e lo raffina progressivamente in parallelo, su più punti contemporaneamente, convergendo verso la risposta corretta in pochi passaggi. Non è più come una macchina da scrivere ma più come un fotografo che sviluppa una polaroid: l'intera immagine emerge gradualmente, tutta insieme.

Applicare questa tecnica al testo, a differenza delle immagini, è però un problema molto più difficile. Il linguaggio ha vincoli logici, grammaticali e semantici che le immagini non hanno nella stessa misura. Per anni si è ritenuto che la diffusion non fosse adatta al testo. Se vuoi approfondire il confronto tecnico tra i due approcci, sul portale trovi [un articolo dedicato proprio a questo tema](https://aitalk.it/it/diffusion-vs-autoregressive.html).
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Chi ha risolto il problema impossibile

La svolta è arrivata da Stanford. Stefano Ermon, professore di informatica e uno dei co-inventori delle tecniche di diffusion usate in Stable Diffusion e DALL-E, lavorava su questo problema dal 2019. Anni di ricerca per capire come applicare la diffusion al testo, fino a una svolta documentata in un paper presentato all'ICML 2024, la principale conferenza internazionale di machine learning, che ha vinto il premio per il miglior articolo. Non è una distinzione di poco conto: significa che la comunità scientifica ha riconosciuto formalmente l'avanzamento come significativo.

Nel 2024 Ermon ha fondato Inception Labs a Palo Alto, portando con sé due ex studenti diventati professori: Aditya Grover dell'UCLA e Volodymyr Kuleshov di Cornell. Il team allargato include ricercatori ed ingegneri provenienti da Google DeepMind, Meta AI, Microsoft AI e OpenAI, e i contributi del gruppo non si limitano alla diffusion: nel curriculum collettivo figurano lavori fondativi su flash attention, decision transformers e direct preference optimization (DPO), tecniche che hanno segnato lo sviluppo dei moderni modelli linguistici.

Il finanziamento è arrivato a novembre 2025 con un seed round da [50 milioni di dollari](https://techcrunch.com/2025/11/06/inception-raises-50-million-to-build-diffusion-models-for-code-and-text/), guidato da Menlo Ventures con la partecipazione di Mayfield, M12 (il fondo di venture capital di Microsoft), Snowflake Ventures, Databricks Ventures, NVentures (il braccio di investimento di NVIDIA) e Innovation Endeavors. Come angel investor figurano Andrew Ng e Andrej Karpathy, quest'ultimo, ex direttore dell'AI di Tesla e co-fondatore di OpenAI, ha pubblicamente incoraggiato i suoi follower a provare il modello, notando che la natura non autoregressiva della diffusion potrebbe portare a "psicologia nuova, punti di forza e debolezze inediti". Quando Karpathy dice che vale la pena provare qualcosa, nel settore si tende ad ascoltare.

## Mercury 2: cosa fa, quanto costa, quanto bene

Il 24 febbraio 2026 Inception ha [lanciato Mercury 2](https://www.inceptionlabs.ai/blog/introducing-mercury-2), presentandolo come il primo "reasoning LLM" basato su diffusion disponibile in produzione. I numeri di velocità sono stati verificati in modo indipendente da [Artificial Analysis](https://artificialanalysis.ai/models/mercury-2), una delle firme di benchmark più rigorose del settore: 711,6 token al secondo nelle loro valutazioni standardizzate multi-turno, che posizionano Mercury 2 al primo posto su 132 modelli monitorati. Sulla configurazione hardware ottimale, GPU NVIDIA Blackwell con precisione NVFP4, i numeri interni di Inception salgono a 1.009 token al secondo, con una latenza end-to-end di 1,7 secondi.

Il confronto è impietoso per i modelli concorrenti nella stessa fascia: Gemini 3 Flash porta a termine le risposte in 14,4 secondi, Claude 4.5 Haiku con ragionamento in 23,4 secondi. Non è una differenza di grado, è una differenza di esperienza utente, la sensazione soggettiva di "istantaneità" cambia completamente. [InfoWorld](https://www.infoworld.com/article/4137528/inceptions-mercury-2-speeds-around-llm-latency-bottleneck.html) ha sintetizzato bene il punto: Mercury 2 non ottimizza i margini, ridisegna il collo di bottiglia.

Sul fronte qualitativo, Mercury 2 si posiziona onestamente nella fascia dei modelli "veloci e leggeri", non tra i giganti del ragionamento profondo. I benchmark pubblicati parlano chiaro: 91,1 su AIME 2025 (matematica competitiva), 73,6 su GPQA Diamond (ragionamento scientifico avanzato), 67,3 su LiveCodeBench (coding), 52,9 su TAU-bench (agenti complessi). Sono risultati competitivi con Claude 4.5 Haiku e GPT-5 Mini, ma non con Claude Opus 4.6 o i migliori modelli di ragionamento esteso, che sull'Artificial Analysis Intelligence Index segnano punteggi nell'ordine di 80-90 su 100, mentre Mercury 2 si ferma a 33.

Il pricing è uno degli aspetti più interessanti: 0,25 dollari per milione di token in input, 0,75 per milione in output. Per confronto, Claude 4.5 Haiku costa circa 4,90 dollari per milione di token in output, circa sei volte e mezzo di più. GPT-5 Mini si aggira intorno a 1,90 dollari, circa due volte e mezzo. A parità di volume, la differenza di costo in pipeline ad alto traffico può valere decine di migliaia di dollari al mese. L'API è compatibile con lo standard OpenAI: in teoria, per chi già usa l'ecosistema OpenAI, è una sostituzione senza riscrivere il codice.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Dove Mercury 2 funziona davvero

Inception è esplicita su quali casi d'uso Mercury 2 sia progettato per servire, e le testimonianze raccolte al lancio sono coerenti con quella posizionamento.

Il campo più naturale sono i **loop agentici**: sistemi dove un agente AI esegue decine o centinaia di chiamate di inferenza per completare un compito, analisi di codice, ricerca iterativa, pipeline di dati. In questi contesti la latenza non si manifesta una volta sola, si moltiplica ad ogni passo. Con i modelli tradizionali, un workflow a dieci passaggi che richiede 20 secondi per inferenza porta a oltre tre minuti di attesa complessiva. Con Mercury 2 lo stesso workflow scende sotto i venti secondi. Non è solo più veloce: cambia quali interazioni sono fisicamente praticabili in tempo reale.

Zed, un editor di codice molto seguìto negli ambienti di sviluppo avanzato, è uno dei partner di lancio: il suo co-fondatore Max Brunsfeld ha descritto la velocità di suggerimento come abbastanza rapida da sembrare "parte del proprio pensiero". Skyvern, una piattaforma di automazione per agenti web, ha riportato che Mercury 2 è almeno due volte più veloce di GPT-5.2 per i loro use case. Wispr Flow, uno strumento per la pulizia in tempo reale di trascrizioni vocali, lo ha valutato come insostituibile per le applicazioni di interazione uomo-macchina a bassa latenza.

Il **voice AI** è il secondo ambito dove la velocità diventa determinante. Le interfacce vocali hanno la finestra di latenza più stretta nell'intero ecosistema AI: una risposta che arriva in più di due secondi rompe la naturalezza della conversazione. A 70-90 token al secondo, i modelli autoregressivi sono al limite dell'usabilità per la voce. Mercury 2 rimuove quel limite con un margine enorme. OpenCall e Happyverse AI, entrambe attive nel settore degli avatar vocali e degli agenti telefonici, hanno citato la bassa latenza come il fattore abilitante principale.

Per le **pipeline di ricerca e RAG** (Retrieval-Augmented Generation), dove documenti vengono recuperati, classificati e riassunti in sequenza, Mercury 2 permette di aggiungere un passo di ragionamento nel ciclo di ricerca senza far esplodere il budget di latenza. SearchBlox, attiva nella ricerca enterprise per compliance, analytics e e-commerce, ha dichiarato che la partnership con Inception rende "pratica l'AI in tempo reale" per il loro prodotto.

## Le ombre nel quadro: i limiti che contano

Mercury 2 è al momento un modello **solo testo**. Non elabora immagini, audio, video. In un panorama in cui la capacità multimodale è diventata quasi lo standard atteso, soprattutto per applicazioni enterprise complesse, questa è una limitazione concreta, non un dettaglio di nota a piè di pagina.

È poi un modello **solo cloud, senza pesi aperti**. Non esiste una versione scaricabile, non è possibile il deployment on-premise, non è disponibile il fine-tuning su dati proprietari. Per le organizzazioni con requisiti di residenza dei dati, sovranità del modello o necessità di adattamento specializzato, settori come sanità, finanza, difesa, questo esclude Mercury 2 per un'ampia classe di casi d'uso.

C'è poi il **problema della verbosità**. Come documentato nella [recensione indipendente di Awesome Agents](https://awesomeagents.ai/reviews/review-mercury-2/), Artificial Analysis ha rilevato che durante le loro valutazioni Mercury 2 ha prodotto 69 milioni di token in output, contro una media di 20 milioni per modelli equivalenti. Il modello tende a generare più testo del necessario. In termini pratici, questo non è solo un problema estetico: gonfia il costo effettivo di output e aggiunge rumore nei workflow che richiedono output strutturato e conciso. È un comportamento gestibile con prompt engineering, ma è un default che richiede attenzione.

La questione più profonda riguarda la **maturità dell'architettura**. I modelli a diffusion per testo sono una classe emergente, Mercury 2 è di fatto il primo modello di questo tipo disponibile in produzione commerciale. Questo significa che esistono meno ingegneri che conoscono i pattern di fallimento in produzione, meno documentazione sugli edge case, meno comunità che ha già affrontato e risolto i problemi tipici. Quando qualcosa si rompe in un sistema in produzione, e succede sempre, il supporto ecosistemico per una tecnologia consolidata come GPT o Claude è incomparabilmente più ricco. Non è una critica all'architettura, è un costo reale che non appare in nessun benchmark.

Vale infine la pena notare che i numeri di velocità più alti, il titolo dei 1.009 token al secondo, presuppongono GPU NVIDIA Blackwell con precisione NVFP4. I dati di Artificial Analysis, che riflettono infrastruttura cloud standard reale, attestano 711,6 token al secondo: numero straordinario, ma distante dall'headline. Non ci sono dati pubblicati per hardware più datato.

## Il mercato parla, ma con cautela

La questione rilevante non è solo se Mercury 2 funziona, le evidenze indipendenti suggeriscono che sì, le promesse di velocità sono reali, ma se il mercato stia effettivamente adottando modelli diffusion su scala, o se siamo ancora nella fase della curiosità tecnica.

I segnali di adozione esistono: integrazioni documentate con strumenti come Zed, Skyvern, Wispr Flow, SearchBlox, Viant (una piattaforma pubblicitaria che ha dichiarato di usare Mercury per ottimizzare campagne in tempo reale). La [disponibilità su Azure AI Foundry](https://www.inceptionlabs.ai/blog/mercury-azure-foundry), annunciata a novembre 2025, apre Mercury al vasto ecosistema enterprise Microsoft. La compatibilità con l'API OpenAI abbassa la barriera di ingresso a quasi zero per chi già opera in quell'ecosistema.

D'altro canto, la posizione di Mercury 2 nella fascia "Haiku-class" dei modelli, competitiva con i modelli veloci ma non con i migliori per ragionamento profondo, limita strutturalmente il suo utilizzo a casi d'uso dove la velocità ha priorità sulla complessità del ragionamento. Per le decisioni che richiedono analisi di documenti lunghi e complessi, sintesi multi-sorgente avanzata, o ragionamento su scenari sfumati, i modelli di frontiera mantengono un vantaggio reale che Mercury 2 non elimina. Come ha osservato [The New Stack](https://thenewstack.io/inception-labs-mercury-2-diffusion/), Ermon stesso è candido su questo: Mercury 2 compete con la fascia Haiku/Flash, non con Opus o GPT.

La scommessa di Inception è che la traiettoria della qualità nei modelli diffusion seguirà la stessa curva di scalabilità vista nei modelli autoregressivi: qualità migliorabile nel tempo, con il vantaggio strutturale della velocità come punto di partenza. È una scommessa plausibile, non ancora verificata.

## Domande aperte: il futuro è parallelo?

Mercury 2 non risponde alla domanda più grande che solleva: la diffusion può davvero diventare il paradigma dominante per i modelli linguistici, o resterà un approccio specializzato per i casi d'uso ad alta velocità?

Ermon ha dichiarato di immaginare un futuro in cui tutti i modelli linguistici siano basati su diffusion. È una visione ambiziosa, e chi l'ha espressa, uno degli scienziati che ha contribuito a costruire le fondamenta della diffusion per le immagini, ha credenziali per sostenerla. Ma il passaggio da "funziona eccezionalmente bene per un sottoinsieme specifico di casi d'uso" a "sostituisce l'autoregressivo come paradigma generale" è un salto enorme, e non ci sono ancora prove che il gap qualitativo con i modelli di frontiera sia destinato a chiudersi.

Restano poi domande aperte concrete: come si comportano i modelli diffusion su ragionamento a catena molto lunga, dove la coerenza attraverso migliaia di token è cruciale? Cosa succede alla qualità a 50.000 o 100.000 token di contesto, quando la finestra da 128K viene davvero stressata? Come si gestisce eticamente un'architettura la cui produzione di output è meno interpretabile passo-per-passo rispetto all'autoregressivo?

La velocità è reale. Il costo è competitivo. Il team è credibile al di sopra di ogni ragionevole dubbio. Le limitazioni attuali sono concrete e documentate. Mercury 2 rappresenta qualcosa di genuinamente nuovo nel panorama dei modelli linguistici, non il modello più intelligente disponibile oggi, ma forse un segnale di dove la conversazione sull'efficienza dell'inferenza AI deve ancora andare.

La macchina da scrivere, token dopo token, potrebbe davvero avere i giorni contati. Ma il romanzo che verrà scritto dopo, e quanto sarà buono, è ancora tutto da vedere.