---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-28
author: "Dario Ferrero"
youtube_url: "https://youtu.be/BNy_6ccpIaI?si=RpwefEJ_8MqaHKi5"
spotify_url: "https://open.spotify.com/episode/4HiFgpk7E9vwCZTy3K2TMl?si=15BsKbavQDGGrBHSUR-ylw"
---

# Qwen3.8-27B in locale: quando la densità si fa sentire
![qwen38-27b.jpg](qwen38-27b.jpg)

*C'è un modo per riconoscere quando un modello sta davvero 'pensando', e non è la qualità della risposta finale, è il tempo che ci mette prima di scriverla. Con Qwen3.8-27B quel tempo si sente tutto, ogni secondo, mentre la ventola della GPU gira un po' più forte del solito e il cursore lampeggia in attesa. In un'epoca in cui tutti corrono verso i Mixture of Experts per andare più veloci, ho deciso di fare l'esperimento opposto: cosa succede se si torna a un modello che accende tutto, sempre, senza scorciatoie?*

Il 14 agosto 2026 il team Qwen di Alibaba, il Tongyi Lab, ha rilasciato Qwen3.8-27B, un modello denso multimodale da circa 27 miliardi di parametri, distribuito con licenza Apache 2.0 insieme al fratello maggiore Qwen3.8-2.4T-A95B, la versione di classe Max pensata per infrastrutture agentiche pesanti. Come raccontato nell'[annuncio ufficiale sul profilo X del team Qwen](https://x.com/Alibaba_Qwen/status/2088280182356611304), la promessa era mantenere aperti i pesi di entrambe le taglie della generazione 3.8, quella leggera per il deployment locale e quella enorme per chi costruisce agenti su scala industriale. Il repository ufficiale su [GitHub](https://github.com/AlibabaCloud-Official/Qwen3.8-27B) lo descrive come un modello nativamente multimodale, capace di superare Qwen3.7-Plus nei flussi di lavoro da ufficio e nella programmazione, con una finestra di contesto nativa di 262.000 token estendibile fino a un milione tramite YaRN.

Dopo quattro puntate di questa serie dedicate a modelli Mixture of Experts, [Qwen 3.6 35B A3B](https://aitalk.it/it/qwen36-35b-ai.html) e [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) su tutte, Qwen3.8-27B rompe lo schema. Non attiva una frazione dei suoi parametri per ogni token come farebbe un'orchestra che chiama in causa solo gli strumentisti di turno, li accende tutti, sempre, i ventisette miliardi al completo. È un ritorno di paradigma in un momento in cui l'industria sembrava aver deciso che il futuro dei modelli locali fosse fatto di esperti sparsi e parametri dormienti. La domanda che mi ha spinto a scaricarlo è semplice: la potenza bruta di un modello "tutto acceso" paga davvero in qualità, su hardware consumer, rispetto al risparmio energetico di un MoE?

C'è anche un dettaglio tecnico che vale la pena segnalare per chi lavora su inferenza professionale: secondo [un'analisi tecnica pubblicata su daily.dev](https://daily.dev/posts/qwen3-8-27b-alibaba-s-dense-27b-model-runs-on-one-gpu-with-262k-context-mzhf0nyjc), Qwen3.8-27B integra di serie una testa di previsione multi-token pensata per il decoding speculativo, con tassi di accettazione dell'ordine del 92% in precisione BF16 e dell'85% in FP8 su prompt brevi. Un dettaglio che riguarda soprattutto chi lo esegue su infrastrutture server, ma che racconta quanto il modello sia stato progettato pensando all'efficienza dell'inferenza fin dalla scheda tecnica, nonostante la scelta architetturale densa.

## Il laboratorio, in breve

Chi segue questa serie conosce già la macchina, chi arriva per la prima volta trova tutti i dettagli nella [prima puntata dedicata a Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), che resta il riferimento metodologico per l'intero progetto. Qui mi limito a ricordare i numeri essenziali: un AMD Ryzen 7700, 32 GB di RAM DDR5 e una GPU AMD Radeon RX 9060 XT con 16 GB di VRAM, la stessa configurazione con cui ho già messo alla prova [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata2.html), Qwen 3.6, Gemma 4 e [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html). Il software resta [LM Studio](https://lmstudio.ai/), scelto fin dalla prima puntata per la stima cromatica delle performance attese, verde, arancio, rosso, che permette di capire in anticipo se un modello girerà comodamente o al limite delle proprie possibilità.

Il repository non quantizzato di Qwen3.8-27B pesa circa 55,6 GB, una dimensione che esclude a priori qualsiasi esecuzione in precisione piena sulla mia configurazione. Ho iniziato i test con la quantizzazione Q8, la più fedele disponibile in LM Studio per questo modello, e il risultato è stato impraticabile: circa 2 token al secondo, un ritmo che rende ogni scambio conversazionale una prova di pazienza incompatibile con qualsiasi uso reale. Ho quindi virato su Q4_K_M, un compromesso che sacrifica precisione numerica in cambio di una velocità finalmente utilizzabile, tra 4,5 e 5,5 token al secondo a seconda del test.

I parametri specifici di questa sessione: contesto impostato a 130.000 token, un compromesso che sfrutta buona parte della finestra nativa di 262.000 senza saturare la VRAM disponibile, offload GPU di 30 layer su 65 totali, quindi poco meno della metà del modello caricato sulla scheda video e il resto affidato alla RAM di sistema, pool di 8 thread CPU su 8 disponibili, batch di valutazione a 2048 con physical batch a 512, e un massimo di 4 predizioni concorrenti. Una configurazione di compromesso dichiarato, pensata per bilanciare velocità e memoria piuttosto che inseguire il punto di massima performance.

## Denso, multimodale, e parecchio loquace

La differenza architetturale rispetto ai MoE testati nelle puntate precedenti non è un dettaglio da scheda tecnica, è la lente attraverso cui leggere ogni singolo risultato di questa prova. Un modello MoE come Ornith-1.0-35B attiva circa 3 miliardi di parametri su 35 per ogni token, un modello denso come questo li attiva tutti, sempre. Il costo computazionale è quello che ci si aspetta, la velocità cala vistosamente rispetto ai concorrenti a esperti misti provati finora in questa serie, ma la domanda aperta resta se quella spesa energetica si traduca in un ragionamento più solido.

Sul fronte multimodale, Qwen3.8-27B nasce nativamente capace di leggere immagini, un tratto che lo distingue da modelli testuali puri come [Laguna XS-2.1](https://aitalk.it/it/qwen3.5-locale-puntata2.html), e che gli permette di affrontare senza configurazioni aggiuntive i test visivi di questa batteria. Il contesto nativo di 262.000 token, estendibile fino a un milione con YaRN secondo la documentazione ufficiale, è teoricamente enorme, ma ho scelto di limitarlo a 130.000 per questa sessione, un margine sufficiente per testare la sua tenuta su documenti lunghi senza mettere in ginocchio la VRAM residua dopo l'offload dei layer.

C'è poi un tratto caratteriale che è emerso fin dal primo prompt e che ha accompagnato l'intera sessione: la verbosità. Qwen3.8-27B è decisamente più prolisso degli altri modelli passati su questo banco di prova, con risposte più lunghe, più articolate, più ricche di dettagli anche dove non strettamente richiesti. Non è né un pregio né un difetto in assoluto, dipende da cosa si cerca. Chi vuole approfondimento trova pane per i suoi denti, chi cerca sintesi rapida potrebbe trovarlo eccessivo.

## Otto sfide, un ritmo diverso

La batteria di test resta identica a quella usata nelle puntate precedenti, per garantire un minimo di comparabilità qualitativa tra modelli di taglie e architetture diverse. Non è un confronto testa a testa in senso stretto, è più simile a misurare temperature diverse con lo stesso termometro.

### Test 1, ragionamento scientifico: il meccanismo di Higgs, 5/5

Il test che uso come termometro generale ha chiesto al modello di spiegare il meccanismo di rottura della simmetria elettrodebole, il ruolo del campo di Higgs, il motivo per cui i bosoni W e Z acquisiscono massa mentre il fotone resta senza. La risposta è arrivata strutturata in quattro sezioni logiche, dal problema della massa nella simmetria unificata, al potenziale a cappello messicano che rompe spontaneamente la simmetria, fino al meccanismo con cui W e Z acquisiscono massa e alla simmetria residua che protegge il fotone. Didatticamente perfetta, con formule corrette accompagnate da interpretazioni fisiche puntuali, da manuale universitario ben scritto. La velocità registrata, 5,64 token al secondo.

### Test 2, multimodalità: una tabella Excel di bassa qualità, 5/5

Ho caricato un'immagine deliberatamente sfocata di un foglio di calcolo, chiedendo una descrizione del contenuto, dei dati principali e delle tendenze. Il modello ha letto correttamente struttura, valori numerici e relazioni tra colonne, estraendo cinque tendenze chiave tra stagionalità, variazione percentuale e andamento degli ordini, per poi proporre insight operativi come la revisione del piano per i mesi estivi. Ha notato autonomamente la correlazione inversa tra numero di ordini e valore medio, un dettaglio che altri modelli testati in questa serie non avevano colto con la stessa nettezza. Velocità di 5,5 token al secondo, robustezza visiva eccellente nonostante la qualità scadente del file di partenza.

### Test 3, generazione di codice: un problema NP-hard, 4,8/5

Il compito era implementare in Python un algoritmo per trovare il ciclo di lunghezza massima in un grafo non orientato, spiegandone la complessità temporale. Il modello ha prodotto una classe ben organizzata con due approcci distinti, uno esatto con backtracking e pruning, uno approssimato per grafi di grandi dimensioni, dimostrando piena consapevolezza della natura NP-hard del problema prima ancora di scrivere codice. Il codice conteneva però due difetti concreti, una condizione di pruning ridondante e un marcatore di debug rimasto per errore in cima al file.

Sollecitato a rivedere il proprio lavoro senza indicazioni specifiche su cosa cercare, ha identificato entrambi i problemi e fornito una versione corretta, spiegando perché la condizione ridondante fosse potenzialmente pericolosa in caso di modifiche future al codice. La capacità di autodiagnosi resta un punto di forza, ma gli errori iniziali pesano sul voto. Velocità di 5,7 token al secondo.

### Test 4, pianificazione multilingua: cinque giorni in Giappone, 5/5

Il compito chiedeva un itinerario di cinque giorni in Giappone per un cliente francese, con testo in francese e una sezione finale in italiano. Il francese prodotto era fluente e privo di errori, con consigli pratici su trasporti, barriere linguistiche e street food, e riferimenti culturali specifici come Tabelog per le recensioni dei ristoranti, Omoide Yokocho per l'atmosfera retrò e Pontocho per le stradine tradizionali di Kyoto. La sezione italiana era altrettanto curata, corretta e scorrevole. A differenza di altri modelli passati su questo banco che avevano avuto incidenti di percorso linguistici, qui non c'è stato alcun errore di lingua. Velocità di 5,42 token al secondo.

### Test 5, contesto lungo: un PDF di 460 pagine, 4,8/5

Ho caricato l'AI Index Report 2025, oltre 460 pagine, chiedendo informazioni sulla crescita della generazione video e le pagine esatte dove trovarle. Il modello ha indicato con precisione le pagine 126 e 127, citando figure specifiche del report e i principali modelli del settore, Google Veo, Meta Movie Gen, OpenAI Sora, Runway, Luma, Kuaishou, oltre al celebre esempio del test "Will Smith che mangia gli spaghetti" diventato un marcatore informale dei progressi nella generazione video. La precisione nel recupero resta eccellente anche in configurazione compressa. Unico neo, un refuso lessicale che, non inficia il preciso lavoro tecnico, ma abbassa di poco il voto. Velocità di 5,75 token al secondo, la più alta registrata in tutta la sessione.
![immagine1.jpg](immagine1.jpg)
*Screenshot durante i test*

### Test 6, ragionamento spaziale: la stanza nel caos, 5/5

Ho chiesto di descrivere una fotografia di una stanza disordinata e proporre una strategia di riordino. La descrizione ha coperto tutte le aree funzionali, letto, pavimento, scrivania, scaffali, con una strategia di intervento motivata su base pratica: il cesto più ingombrante va spostato per primo, il pavimento è l'area più critica da liberare. Un consiglio extra, la cosiddetta regola dei tre secondi per decidere rapidamente su ogni singolo oggetto ambiguo, ha aggiunto un tocco di metodo che altri modelli non avevano proposto. La comprensione visuo-spaziale è molto buona, ha notato persino i riflessi nello specchio, e la strategia operativa risultava ben strutturata. Velocità di 5,52 token al secondo.

### Test 7, agente multi-step: una web app di gestione spese, 5/5

Il compito era pianificare lo sviluppo di una web app per la gestione delle spese, con stack tecnologico, struttura del progetto e roadmap per un team di due sviluppatori. La risposta ha proposto uno stack moderno con React, NestJS, PostgreSQL e Prisma, una struttura a monorepo, una roadmap in sei sprint e una sezione dedicata alle criticità trasversali, fusi orari, performance, sicurezza, import CSV. La suddivisione del lavoro tra i due sviluppatori era dettagliata quanto quella che proporrebbe un project manager con esperienza reale, con menzioni puntuali di strumenti come Docker, GitHub Actions e Resend, e best practice come caching e rate limiting. Velocità di 5,12 token al secondo.

### Test 8, conversazione lunga: quattro turni, 5/5

L'ultimo test ha misurato la tenuta della memoria conversazionale su quattro turni riguardanti stack, notifiche, database e scalabilità di un'app di task management. Il modello ha mantenuto piena coerenza, ricordando e motivando ogni scelta tecnologica precedente, proponendo un'architettura ibrida con WebSocket per le notifiche in-app ed email per gli eventi asincroni, uno schema database completo di indici strategici, e una roadmap di scalabilità fino a diecimila utenti articolata in tre fasce progressive. La velocità è scesa, 4,5, 4,57, 4,68 e infine 4,28 token al secondo, un rallentamento fisiologico dovuto alla crescita del contesto accumulato, senza alcun calo percepibile nella qualità delle risposte.

## Tabella riassuntiva
![immagine2.jpg](immagine2.jpg)
Media dei voti: 4,95 su 5. Velocità media: circa 5,3 token al secondo.

## Il pensatore lento, e cosa significa davvero

I numeri raccontano una storia chiara, ma vale la pena guardarla da più angolazioni prima di trarre conclusioni. Sul piano della qualità, Qwen3.8-27B ha eguagliato, e in certi passaggi superato per profondità, i risultati ottenuti dai modelli MoE testati nelle puntate precedenti, con l'unica eccezione del test sul codice, penalizzato per errori iniziali poi corretti su sollecitazione. La densità paga, evidentemente, in termini di coerenza e capacità di ragionamento su compiti isolati.

Sul piano della velocità, però, il confronto è impietoso. Ornith-1.0-35B, un MoE con soli 3 miliardi di parametri attivi per token, viaggiava stabilmente tra i 16 e i 17 token al secondo sulla stessa identica macchina. Qwen3.8-27B, in configurazione compressa Q4_K_M, si è fermato a una media di 5,3. È la differenza tra leggere un romanzo a ritmo naturale e doverlo scandire parola per parola, un'esperienza che ricorda per certi versi *Primer*, il film indipendente di Shane Carruth diventato oggetto di culto proprio per la sua densità narrativa: bellissimo, rigoroso, ma non fatto per chi ha fretta di arrivare ai titoli di coda.

C'è poi una domanda che riguarda chi userà davvero questo modello. Secondo i dati diffusi da Alibaba e ripresi da [un'analisi di OfficeChai sul lancio del modello](https://officechai.com/miscellaneous/alibaba-releases-qwen-3-8-27b-beats-muse-glimmer-30b-on-many-benchmarks/), su CoWorkBench, il benchmark interno per compiti di produttività a lungo orizzonte, Qwen3.8-27B segna 70,7 punti, davanti sia a Opus4.6 Max, fermo a 68,2, sia al predecessore Qwen3.6-27B, fermo a 61. Numeri diffusi dall'azienda stessa, quindi da leggere con la cautela dovuta a qualsiasi benchmark autoprodotto, ma che confermano la direzione: il salto generazionale nella qualità di ragionamento c'è, indipendentemente da come lo si misuri.

Chi vince e chi perde in questo scenario dipende interamente dal profilo d'uso. Chi lavora su compiti isolati e complessi, spiegazioni scientifiche, analisi di documenti, pianificazione dettagliata, e può permettersi di aspettare qualche secondo in più per risposta generata, trova in un modello denso come questo un ragionatore più affidabile. Chi cerca invece un assistente conversazionale reattivo, per uso quotidiano ad alto volume di scambi, probabilmente troverà più equilibrata la scelta di un MoE come Ornith-1.0, che nella puntata precedente aveva, peraltro, segnato punteggio pieno 5 su 5, senza pagare il conto salato in velocità.

Resta una domanda aperta che porto alla prossima puntata: quanto di questo divario di velocità e leggere sbavature sarebbe recuperabile con una quantizzazione Q8, più VRAM a disposizione e magari con l'intero modello caricato in GPU senza dover scaricare metà dei layer sulla RAM di sistema? È il tipo di quesito che questa serie, nata per capire cosa si può ottenere con mezzi normali, continuerà a inseguire puntata dopo puntata.
![immagine3.jpg](immagine3.jpg)

**Verdetto**: Qwen3.8-27B è un modello per chi non ha fretta e cerca profondità di ragionamento sopra ogni altra cosa, con la consapevolezza che la sua natura densa si paga cara in velocità su hardware consumer. Se la reattività è la priorità, un MoE resta la scelta più equilibrata, anche a costo di qualche punto di qualità in meno sui compiti più ostici.

*Nota tecnica: tutte le velocità riportate sono espresse in token al secondo (t/s) e misurate localmente con LM Studio sulla configurazione hardware descritta nel primo articolo della serie. I voti sono valutazioni personali, non punteggi di benchmark automatizzati.*
