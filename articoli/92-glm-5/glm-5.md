---
tags: ["Generative AI", "Training", "Business"]
date: 2026-02-25
author: "Dario Ferrero"
youtube_url: "https://youtu.be/rSnUKjcUzIA?si=_VLl8cccYbMLggU1"
---

# GLM-5: il modello addestrato su chip cinesi
![glm-5.jpg](glm-5.jpg)

*Un modello da 744 miliardi di parametri, addestrato interamente su chip domestici Huawei, che raggiunge le prestazioni dei migliori modelli proprietari americani in alcune delle prove più rilevanti. Il tutto senza un solo processore NVIDIA. La corsa all'autonomia tecnologica cinese non è più una promessa futura: è già successa, e GLM-5 ne è la prova più eloquente fino ad oggi.*

Chi segue questo portale da un po' di tempo sa che stiamo osservando qualcosa di più grande di una serie di rilasci di modelli. Con [Kimi K2.5](https://aitalk.it/it/kimik2.5.html), con [DeepSeek MHC](https://aitalk.it/it/deepseek-mhc.html), con [Kimi K2 Thinking](https://aitalk.it/it/kimi-k2-thinking.html) abbiamo raccontato i tasselli di un mosaico che ora, con l'arrivo di [GLM-5](https://z.ai/blog/glm-5), mostra con maggiore nitidezza la sua forma complessiva. Non si tratta di singoli modelli eccezionali. Si tratta di un movimento sistematico, coordinato, che in pochi mesi ha portato l'intelligenza artificiale cinese open source dall'inseguimento alla parità, e in qualche caso al sorpasso, con i laboratori americani più blasonati.

GLM-5 è stato presentato l'11 febbraio 2026 da [Z.ai](https://z.ai/blog/glm-5), il nome internazionale con cui dal 2025 si presenta Zhipu AI, azienda fondata nel 2019 come spin-off della Tsinghua University di Pechino. Il lancio non poteva essere più simbolico: vigilia del Capodanno lunare, in quello che alcuni analisti stanno già chiamando la "Spring Festival offensive" dell'AI cinese. Una coincidenza? Difficile crederlo.

## Dentro il motore: ingegneria di scala

Per capire cosa rappresenta GLM-5 dal punto di vista tecnico, è utile partire da un'analogia. Immaginate un grande studio di registrazione. I vecchi modelli erano come orchestre di dimensioni standard, dove tutti i musicisti suonano in contemporanea. I modelli a "miscela di esperti" (MoE, Mixture of Experts), come GLM-5, funzionano invece come un'orchestra enorme in cui, per ogni brano, vengono chiamati sul palco solo i musicisti più adatti. Il risultato finale è più ricco, il costo per eseguirlo è molto inferiore a quello che ci si aspetterebbe dalle dimensioni complessive dell'ensemble.

In termini concreti: GLM-5 ha 744 miliardi di parametri totali (il corrispettivo delle "conoscenze" memorizzate nella rete neurale), ma per elaborare ogni singola richiesta ne attiva soltanto 40 miliardi. Rispetto al predecessore GLM-4.5, che si fermava a 355 miliardi di parametri totali con 32 miliardi attivi, si tratta di un salto considerevole, sia in termini di capacità che di efficienza nella gestione del carico computazionale.

A questo si affianca un'altra scelta tecnica rilevante: l'integrazione del meccanismo di attenzione sparsa sviluppato da DeepSeek, noto come DeepSeek Sparse Attention. Senza entrare nei dettagli matematici, questa tecnica permette al modello di gestire testi molto lunghi, fino a 200.000 "gettoni" di testo, equivalenti a circa 150.000 parole, senza che i costi computazionali esplodano in modo proporzionale alla lunghezza. È la stessa logica che ha permesso a DeepSeek di abbattere i costi operativi dei propri modelli: non sprecare risorse su ogni singola parola del contesto, ma concentrarsi su quelle più rilevanti.

I dati di addestramento sono cresciuti da 23 a 28,5 trilioni di token, su cui il modello è stato "allenato" prima di ricevere ulteriori affinamenti tramite apprendimento per rinforzo, una tecnica che, semplificando, premia il modello quando produce risposte migliori e lo corregge quando sbaglia, in modo simile a come si allena un atleta con un coach esigente. Per gestire questo processo su scala così grande, il team di Zhipu ha sviluppato un'infrastruttura di addestramento chiamata [Slime](https://github.com/THUDM/slime), che ottimizza il flusso di calcolo in modo asincrono, riducendo i tempi morti tra un ciclo di addestramento e l'altro.

Una nota pratica per chi pensa all'installazione autonoma: il modello nella sua versione originale in massima precisione richiede circa 1.490 gigabyte di memoria, più di un terabyte e mezzo. Numeri da centro di calcolo, non da workstation domestica. Esiste però una versione a precisione ridotta (FP8) che dimezza questo requisito, rendendo il modello accessibile a infrastrutture più comuni, seppure comunque non banali.

## Dove vince, dove arranca: i numeri senza filtri

L'analisi delle prestazioni è dove la retorica dei comunicati stampa incontra la realtà dei test. E qui GLM-5 riserva alcune sorprese, in entrambe le direzioni.

Sul fronte delle capacità agentiche, ovvero la capacità del modello di svolgere compiti complessi in autonomia, non solo rispondere a domande singole, GLM-5 raggiunge risultati che fino a pochi mesi fa sembravano prerogativa esclusiva dei modelli proprietari a pagamento. Secondo le misurazioni di [Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-everything-you-need-to-know), che utilizza un indice composito chiamato GDPval-AA per misurare l'utilità pratica nei compiti lavorativi reali, GLM-5 ottiene un punteggio ELO di 1412, il che lo posiziona al terzo posto assoluto nella classifica mondiale, subito dopo Claude Opus 4.6 di Anthropic e GPT-5.2 di OpenAI. Primo tra tutti i modelli a sorgente aperta, con un margine significativo rispetto ai concorrenti della stessa categoria come Kimi K2.5 e DeepSeek V3.2.

Ancor più significativo è il salto in avanti rispetto al suo predecessore diretto: GLM-4.7 otteneva un punteggio di 42 sull'indice di intelligenza di Artificial Analysis; GLM-5 arriva a 50, il primo modello open source a raggiungere e superare quella soglia nella versione 4.0 dell'indice. Non è un numero arbitrario: segna il momento in cui la distanza tra modelli aperti e modelli proprietari di fascia alta si è ridotta a qualcosa di realmente misurabile.

Sul fronte della programmazione, GLM-5 raggiunge il 77,8% nel benchmark SWE-bench Verified, che misura la capacità di risolvere problemi reali su repository di codice esistenti, una prova molto più vicina al lavoro quotidiano di uno sviluppatore rispetto ai test teorici. Claude Opus 4.5 si ferma all'80,9%, GPT-5.2 all'80,0%: la distanza c'è, ma è dell'ordine di pochi punti percentuali, non di un abisso.

Il risultato forse più sorprendente riguarda le allucinazioni, quel fenomeno per cui i modelli linguistici "inventano" informazioni con la stessa sicurezza con cui riportano fatti veri, uno dei problemi più ostici dell'intelligenza artificiale generativa. GLM-5 riduce il proprio tasso di allucinazioni del 56% rispetto a GLM-4.7, raggiungendo il livello più basso tra tutti i modelli testati da Artificial Analysis. Il meccanismo usato è semplicemente onesto: quando il modello non sa qualcosa, si astiene dal rispondere invece di inventare. Una scelta che penalizza leggermente la completezza delle risposte, ma migliora radicalmente l'affidabilità di quelle che vengono fornite.

Ci sono però limiti concreti da non sottovalutare. GLM-5 è, al momento, un modello esclusivamente testuale: non analizza immagini né produce contenuti multimediali, mentre competitor come Kimi K2.5 supportano già l'input visivo. La velocità di inferenza, circa 17-19 token al secondo, è sensibilmente inferiore a quella dei modelli addestrati su hardware NVIDIA di ultima generazione, che raggiungono i 25 token e oltre. E la finestra di contesto massima di 200.000 token, pur ampia, rimane sotto al milione raggiunto da Claude Opus 4.6. Non difetti trascurabili, ma elementi da pesare in rapporto al costo e alla disponibilità.
![bench.jpg](bench.jpg)
[Immagine tratta da z.ai](https://z.ai/blog/glm-5)

## La mossa Huawei: molto più di un dettaglio tecnico

È qui che l'analisi tecnica lascia spazio a qualcosa di più grande. GLM-5 è stato addestrato interamente su chip Huawei Ascend, senza un singolo processore NVIDIA. Ma per capire il peso di questa affermazione, occorre un passo indietro di qualche mese.

Il 14 gennaio 2026, Zhipu AI aveva già annunciato un risultato che aveva fatto notizia in modo sottotraccia: GLM-Image, il proprio modello generativo di immagini, era diventato il primo modello multimodale di fascia alta al mondo a completare l'intero ciclo di addestramento su hardware cinese, specificatamente sui server Huawei Ascend Atlas 800T A2. Era già una pietra miliare. Con GLM-5, Zhipu ha replicato e ampliato quell'esperienza su scala ben maggiore, estendendola al proprio modello linguistico di punta.

Il contesto geopolitico è imprescindibile. Il Dipartimento del Commercio americano ha inserito Zhipu AI nella propria lista di entità che agiscono contro gli interessi di sicurezza nazionale degli Stati Uniti, citando presunti legami con strutture militari cinesi. La conseguenza pratica è stata il blocco dell'accesso ai processori NVIDIA H100 e A100, le schede grafiche diventate lo standard de facto per l'addestramento dei modelli linguistici più avanzati. La risposta di Zhipu non è stata cercare scorciatoie o hardware alternativo occidentale: è stata accelerare la collaborazione con Huawei e dimostrare che si può fare lo stesso lavoro con strumenti cinesi.

I processori Ascend 910B e 910C di Huawei offrono individualmente circa il 60-80% della potenza di calcolo di un H100 NVIDIA. Un gap non trascurabile, che Zhipu ha colmato attraverso due strategie parallele: ottimizzazione profonda del software attraverso il framework MindSpore di Huawei, e scalabilità orizzontale, più macchine che lavorano in parallelo per compensare la minore potenza individuale di ciascuna. Il sistema CloudMatrix 384 di Huawei, che aggrega quasi 400 chip Ascend in un'unica unità logica, raggiunge i 300 petaflop di potenza di calcolo complessiva, un numero impressionante, ottenuto con un approccio che richiede più hardware ma dimostra la praticabilità dell'alternativa "domestica".

Vale la pena essere precisi su un punto: GLM-5 non è il primo grande modello linguistico cinese addestrato su chip non-NVIDIA. Ma è il primo di questa generazione, quella dei modelli da centinaia di miliardi di parametri che competono con i migliori laboratori americani, a farlo su una scala di questo tipo, su hardware interamente cinese, e a ottenere risultati che resistono al confronto con i modelli di punta mondiali. La distinzione è tecnica, ma la portata strategica è enorme.

È significativo notare che Zhipu non si è limitata agli Ascend. La documentazione ufficiale su [GitHub](https://github.com/zai-org/GLM-5/blob/main/example/ascend.md) elenca il supporto a Moore Threads, Cambricon, Kunlun Chip, MetaX, Enflame e Hygon, praticamente l'intero ecosistema di chip AI cinesi alternativi a NVIDIA. Un segnale che la direzione non è semplicemente "usiamo Huawei perché siamo costretti", ma "costruiamo un ecosistema che non dipenda da nessun fornitore straniero".

## Open source come arma strategica

GLM-5 è distribuito sotto licenza MIT, la più permissiva tra le licenze open source, che consente uso commerciale, modifica e redistribuzione senza restrizioni significative. I pesi del modello sono liberamente scaricabili su [Hugging Face](https://huggingface.co/zai-org/GLM-5) e ModelScope. L'API è accessibile tramite la piattaforma [Z.ai](https://docs.z.ai/guides/llm/glm-5) a prezzi nettamente inferiori ai competitor proprietari: circa 1 dollaro per milione di token in ingresso e 3,2 in uscita, contro i 15 e oltre dei modelli di OpenAI e Anthropic di pari livello.

C'è qualcosa di peculiare, e deliberato, in questa scelta di apertura radicale. Zhipu AI è un'azienda quotata alla Borsa di Hong Kong (HKEX: 2513), con una quotazione completata l'8 gennaio 2026 che ha raccolto circa 558 milioni di dollari. Non è un progetto accademico no-profit: ha investitori, azionisti, aspettative di rendimento. Eppure distribuisce gratuitamente, e con licenza liberissima, quello che considera il proprio modello più avanzato.

La logica, che abbiamo già visto con DeepSeek e Kimi, è quella dell'ecosistema: più sviluppatori in tutto il mondo costruiscono su GLM-5, più cresce l'adozione della piattaforma Z.ai, dei servizi API, del brand. È un modello di business in cui l'apertura del modello è il prodotto di marketing più efficace, e al tempo stesso, nel contesto geopolitico attuale, uno strumento di influenza soft sull'ecosistema globale dell'intelligenza artificiale.

Va però sollevata una domanda che spesso rimane in secondo piano quando si parla di modelli open source cinesi: le implicazioni in termini di sicurezza e conformità normativa. Zhipu AI opera sotto la giurisdizione cinese, con tutti gli obblighi che ne derivano in materia di sicurezza nazionale e accesso ai dati. Il modello in sé, una volta scaricato, è indipendente dalla società che lo ha creato, ma chi usa l'API di Z.ai si affida a un'infrastruttura soggetta alle leggi cinesi. Per molte aziende occidentali, specialmente in settori regolamentati, questo non è un dettaglio trascurabile. Per sviluppatori individuali o aziende in contesti meno sensibili, la licenza MIT garantisce una via d'uscita: scaricare i pesi, fare girare il modello in autonomia, senza dipendenze esterne.

Il tema del bias nei dati di addestramento, inevitabile per qualsiasi modello addestrato su corpus testuali umani, rimane poi una questione aperta. Zhipu non ha ancora pubblicato un rapporto tecnico dettagliato (il team ha annunciato che è "in arrivo"), il che rende difficile valutare in modo indipendente le scelte fatte nella selezione dei dati e nella fase di allineamento ai valori. Un'omissione che non è un dettaglio marginale: proprio su questo punto i laboratori americani come Anthropic e OpenAI hanno costruito una parte significativa della propria reputazione, con documentazione pubblica estesa e politiche esplicite.

## Il quadro che si delinea

Guardando agli articoli pubblicati su questo portale nelle ultime settimane, il pattern è inequivocabile. In uno spazio di tempo compresso, DeepSeek, Moonshot (con Kimi) e Zhipu (con GLM) hanno rilasciato modelli che non si limitano a "quasi" raggiungere i migliori laboratori americani: in specifici benchmark e casi d'uso li superano, spesso a una frazione del costo. Non è una coincidenza temporale: è il segnale di un settore che ha raggiunto una massa critica di competenze, capitali e, cosa più significativa, una capacità di sviluppo su hardware domestico che le sanzioni americane non sono riuscite a fermare, ma hanno semmai accelerato.

La risposta dei mercati ai modelli cinesi non è una novità di febbraio 2026. Il precedente più clamoroso risale al 27 gennaio 2025, quando l'annuncio di DeepSeek R1 bruciò in un solo giorno quasi 600 miliardi di dollari di capitalizzazione da Nvidia, il crollo più rapido nella storia del mercato azionario americano. GLM-5 si inserisce in quel solco: non ha provocato uno shock comparabile, ma consolida la narrativa che il mercato ha già metabolizzato, quella di un ecosistema cinese che non ha bisogno di rallentare.

Per il settore nel suo complesso, la lezione di GLM-5, come di DeepSeek e Kimi prima di lui, è che la corsa all'intelligenza artificiale non è più una competizione a due sole squadre. Chi progetta infrastrutture, chi valuta fornitori, chi prende decisioni di investimento nel settore tecnologico deve fare i conti con un ecosistema genuinamente multipolare, in cui le variabili geopolitiche, le scelte di licenza e le dipendenze hardware sono diventate parte integrante dell'analisi tecnica.

GLM-5 è disponibile liberamente su [Hugging Face](https://huggingface.co/zai-org/GLM-5), testabile via API su [Z.ai](https://chat.z.ai) e consultabile nel dettaglio tecnico sul [repository GitHub](https://github.com/zai-org/GLM-5) ufficiale. Chi vuole avere un'opinione informata ha tutto il materiale a disposizione per formarsela.

