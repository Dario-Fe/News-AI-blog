---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-06-03
author: "Dario Ferrero"
youtube_url: "https://youtu.be/UpjPSTBHZAw?si=t6GaKAKWNwr8FglV"
---

# RecursiveMAS ha abolito i token, gli agenti parlano nella loro lingua 
![recursivemas.jpg](recursivemas.jpg)

*Un paper pubblicato il 28 aprile 2026 da ricercatori di UIUC, Stanford, NVIDIA e MIT propone un cambiamento architetturale radicale: gli agenti AI che collaborano senza più scambiarsi testo, comunicando direttamente in spazio latente. I numeri sono convincenti. Le domande aperte, ancora di più. Scopriamo RecursiveMAS, il framework che trasforma gli agenti in un 'cervello collettivo ricorsivo*.

Immaginate una squadra di specialisti che deve risolvere un caso complesso: un cardiologo, un neurologo, un anestesista. Ogni volta che uno di loro ha un'intuizione, però, non può semplicemente passarla al collega, deve prima tradurla in una email formale, inviarla, aspettare che l'altro la legga, la interpreti, formuli una risposta, la scriva e la rispedisca. E così via, a ogni scambio. Il pensiero rallenta, i costi aumentano, qualcosa si perde nella traduzione.

Questo è, con un'approssimazione utile, il problema fondamentale dei sistemi multi-agente basati su linguaggio. Ogni agente AI riceve un input in forma testuale, lo elabora, produce un output testuale, che viene passato all'agente successivo come nuovo input. Ogni passaggio richiede decodifica dal vocabolario (un'operazione computazionalmente costosa), latenza, e token, ovvero soldi. Se si aggiunge la ricorsione, cioè il fatto che il sistema deve compiere più giri di collaborazione per affinare la risposta, il problema si moltiplica: a ogni round, ogni agente deve decodificare tutto da capo.

[RecursiveMAS](https://arxiv.org/abs/2604.25917), il framework presentato il 28 aprile 2026 da un team di dodici ricercatori distribuiti tra UIUC, Stanford, NVIDIA e MIT, parte da una domanda apparentemente semplice: e se gli agenti smettessero di parlarsi in testo?

## La ricorsione come principio di sistema

Per capire la portata della proposta, è necessario un passo indietro. Negli ultimi anni, la ricorsione, cioè l'idea di far "girare in loop" le stesse elaborazioni su stati interni del modello per approfondire il ragionamento, si è affermata come uno dei nuovi assi di scaling per i grandi modelli linguistici. Anziché addestrare modelli sempre più grandi, si può prendere un modello di dimensioni ragionevoli e farlo iterare più volte sullo stesso problema, raffinando progressivamente le sue rappresentazioni interne. Questo approccio, chiamato in letteratura *recursive language model* (RLM), ha mostrato risultati promettenti nella ricerca degli ultimi due anni.

Il salto concettuale di RecursiveMAS consiste nell'estendere questo principio dall'interno di un singolo modello all'intero sistema multi-agente. Non più ricorsione dentro un agente, ma ricorsione del sistema come unità. L'intera collaborazione tra agenti diventa un loop ricorsivo unico, in cui le informazioni fluiscono continuamente, in forma di stati latenti, non di testo, da un agente all'altro, e il cerchio si chiude: l'ultimo agente passa il suo stato interno al primo, che può così ricominciare l'elaborazione con le informazioni accumulate nel round precedente.

Il risultato è quello che il paper descrive come un *cervello collettivo ricorsivo*: ogni agente agisce come uno strato di un modello ricorsivo, e l'intero sistema converge iterativamente verso una risposta senza mai, tranne che nell'ultimo round, produrre testo intermedio.

## RecursiveLink: l'interprete leggero

Il problema tecnico più delicato è quello della traduzione tra mondi. In un sistema multi-agente eterogeneo, dove ogni agente è un modello diverso, con architettura diversa, dimensioni diverse dello spazio nascosto (*hidden size*), come si trasferisce uno stato latente da un modello all'altro senza convertirlo in testo?

La risposta che RecursiveMAS propone è il modulo [RecursiveLink](https://recursivemas.github.io/): un componente leggero a due strati residuali che funge da interprete tra gli spazi latenti dei diversi modelli. Nella sua variante interna (*inner link*), opera all'interno di ogni singolo agente durante la generazione: anziché proiettare lo stato nascosto sul vocabolario per produrre un token, lo trasforma e lo reinietta come input per il passo successivo, mantenendo il ragionamento interamente nello spazio continuo. Nella variante esterna (*outer link*), aggiunge un layer lineare supplementare per proiettare lo stato latente di un agente nello spazio dimensionale dell'agente successivo, permettendo il trasferimento anche tra modelli con geometrie interne incompatibili.

La scelta del collegamento residuale non è estetica: mantenere la componente originale dello stato latente significa che il modulo non deve imparare l'intera proiezione da zero, ma solo la *differenza*, lo scarto tra lo spazio sorgente e quello destinazione. Questo rende l'addestramento più stabile e più efficiente.

La cosa più sorprendente, però, è la dimensione del componente addestrato. Mentre i parametri base di tutti gli agenti restano completamente congelati, il RecursiveLink introduce soltanto circa 13 milioni di parametri addestrabili sull'intero sistema, pari allo 0,31% dei parametri totali. Per dare un'idea della proporzione: è come ottimizzare un'orchestra sinfonica agendo esclusivamente sul sistema di amplificazione tra i leggii, senza toccare nessuno strumento.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/html/2604.25917v1)

## Inner loop, outer loop: addestrare un sistema intero

L'altra innovazione strutturale del framework riguarda il metodo di addestramento. Ottimizzare un sistema multi-agente ricorsivo in modo coerente non è banale: se si addestrano i modelli separatamente, ciascuno impara a comportarsi bene in isolamento, ma non necessariamente a collaborare. Se invece si cerca di ottimizzarli tutti insieme fin dall'inizio, la complessità esplode e i gradienti tendono a svanire attraverso i round ricorsivi.

RecursiveMAS propone un algoritmo a due fasi chiamato *inner-outer loop learning*. Nella prima fase, l'inner loop addestra in parallelo e in modo indipendente l'*inner link* di ciascun agente, usando come obiettivo la cosine similarity tra i pensieri latenti prodotti e la distribuzione dei token corretti nel layer di embedding. Si tratta di un warm-start: si insegna a ogni agente a pensare in spazio latente senza ancora preoccuparsi di come interagirà con gli altri.

Nella seconda fase, l'outer loop ottimizza l'intero sistema come unità. Il framework viene dispiegato per *n* round ricorsivi, e solo alla fine dell'ultimo round viene prodotta una risposta testuale su cui calcolare la perdita. Il gradiente viene poi propagato all'indietro attraverso l'intera catena ricorsiva, assegnando a ogni outer link un segnale di credito condiviso basato sul suo contributo alla predizione finale. Ogni link apprende dunque non solo dal proprio errore locale, ma dalla qualità complessiva dell'intero sistema su ogni singolo esempio.

Il teorema centrale del paper (Teorema 4.1) dimostra formalmente perché questo approccio funziona meglio di quello basato su testo: i gradienti che transitano attraverso i RecursiveLink residuali rimangono stabili attraverso i round, mentre nel caso del testo, dove la proiezione sul vocabolario introduce una discontinuità, tendono a collassare verso zero con l'aumentare della profondità ricorsiva. Un gradiente che svanisce significa un sistema che smette di imparare.

## I numeri: nove benchmark, quattro pattern

RecursiveMAS è stato testato su nove benchmark che coprono matematica (MATH500, AIME 2025, AIME 2026), scienza e medicina (GPQA-Diamond, MedQA), generazione di codice (LiveCodeBench, MBPP+) e ricerca su web (HotpotQA, Bamboogle). I modelli coinvolti includono Qwen3/3.5, LLaMA-3, Gemma3 e Mistral, in configurazioni da meno di 1,5 miliardi a circa 10 miliardi di parametri per agente.

I risultati rispetto a tutte le baseline, singolo agente con LoRA, singolo agente con full fine-tuning, Mixture-of-Agents, TextGrad, LoopLM, Recursive-TextMAS, mostrano un miglioramento medio di 8,3 punti percentuali di accuratezza. Il guadagno più vistoso si registra sui benchmark di ragionamento matematico denso: su AIME 2025, la versione *scaled* di RecursiveMAS raggiunge l'86,7% contro il 73,3% della migliore baseline comparabile. Il vantaggio, cosa importante, cresce con la profondità ricorsiva: a *r* = 1 (un solo round), il miglioramento medio è di 3,4 punti; a *r* = 3, sale a 7,2. I sistemi testuali, per confronto, tendono invece a peggiorare o a stabilizzarsi con la ricorsione più profonda, segno che accumulano errori ad ogni round, invece di affinarsi.

Sul fronte dell'efficienza, i dati sono ancora più netti. Rispetto a un sistema multi-agente ricorsivo equivalente ma basato su testo, RecursiveMAS offre uno speedup da 1,2× a *r* = 1 fino a 2,4× a *r* = 3, con una riduzione dei token consumati che passa dal 34,6% al 75,6%. Il costo di addestramento stimato è di 4,27 dollari contro 9,67 del fine-tuning completo, e con meno memoria GPU: 15,29 GB di picco contro i 41,40 richiesti dal full SFT.

Il framework è stato testato su quattro pattern di collaborazione distinti: *Sequential* (Planner, Critic, Solver in sequenza), *Mixture* (specialisti in parallelo aggregati da un Summarizer), *Distillation* (un agente esperto più grande che istruisce un agente apprendista più piccolo), e *Deliberation* (un Reflector interno accoppiato con un Tool-Caller che accede a Python e API di ricerca). In tutti e quattro i contesti, RecursiveMAS supera il singolo agente più forte della configurazione corrispondente.

## Quando gli agenti smettono di parlare

Fin qui i numeri. Ma c'è una domanda che i numeri non risolvono, e che riguarda qualcosa di più scomodo: se gli agenti non si parlano più in linguaggio naturale, come capisce un essere umano cosa sta succedendo?

Nei sistemi multi-agente tradizionali, ogni scambio testuale tra agenti è in linea di principio leggibile. Un ingegnere può aprire il log, scorrere la conversazione tra il Planner e il Solver, capire dove il ragionamento ha preso una direzione sbagliata, intervenire. La traccia testuale è una forma di trasparenza implicita: il sistema pensa ad alta voce, e quella voce è comprensibile.

In RecursiveMAS, i round intermedi non producono testo. I pensieri latenti, rappresentazioni vettoriali ad alta dimensionalità che transitano tra i modelli attraverso i RecursiveLink, non hanno una traduzione naturale in linguaggio umano. Il paper include analisi delle distribuzioni semantiche nello spazio latente attraverso i round, mostrando che la coerenza semantica si mantiene e che i concetti rilevanti si cristallizzano progressivamente, ma questa è una rassicurazione tecnica, non una finestra accessibile sulla cognizione del sistema.

Il vero contributo di RecursiveMAS, come osserva un'analisi su Towards AI, è l'estensione dello stile COCONUT, pensiero continuo nello spazio latente, attraverso gli agenti tramite l'adattatore RecursiveLink. Ma COCONUT, presentato da Meta nel 2024, aveva già sollevato questa preoccupazione nel contesto del singolo modello: quando un sistema ragiona senza emettere testo intermedio, i meccanismi standard di interpretabilità, analisi dell'attenzione, probing dei layer, steering vettoriale, diventano molto più difficili da applicare all'intero flusso computazionale.

La comunità di ricerca sull'interpretabilità meccanicistica, che negli ultimi anni ha compiuto progressi notevoli nella comprensione di come i transformer singoli elaborano l'informazione, si trova di fronte a una nuova frontiera: sistemi in cui le unità di analisi non sono più i layer di un singolo modello, ma i passaggi latenti tra modelli eterogenei. Il paper di RecursiveMAS non affronta questo punto in modo esplicito, una lacuna che vale la pena segnalare.

Non si tratta di alarmismo. La maggior parte delle applicazioni pratiche di questi sistemi, generazione di codice, risposta a domande, ragionamento matematico, non richiede trasparenza in tempo reale sui round intermedi. Il punto è più sottile: in scenari di deployment ad alto rischio, o quando un sistema produce un risultato inatteso e bisogna capire perché, la mancanza di traccia testuale intermedia rende il debugging strutturalmente più difficile. Il costo della velocità è, in parte, pagato in comprensibilità.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/html/2604.25917v1)

## Limiti, buchi e onestà intellettuale

Il paper non dedica una sezione esplicita ai propri limiti, una scelta editoriale comune nella ricerca accademica, ma che vale la pena compensare con un'analisi esterna.

Il primo punto è la natura dei benchmark. Tutti e nove i test utilizzati sono dataset standardizzati, costruiti attorno a problemi con risposta verificabile e univoca: equazioni, scelte multiple in medicina, problemi di competizione matematica, generazione di codice valutata con test automatici. Sono i benchmark su cui la comunità misura i progressi, e hanno senso come confronto comparativo. Ma non dicono nulla su come RecursiveMAS si comporterebbe in compiti aperti, redazione di documenti lunghi, analisi di testi ambigui, pianificazione multi-step con feedback umano, dove la qualità della risposta non è binaria e il processo conta quanto il risultato.

Il secondo punto riguarda gli strumenti esterni. Il pattern *Deliberation* include l'uso di Python e API di ricerca, ed è incoraggiante che il framework regga anche in questo contesto. Ma l'integrazione con tool esterni è rimasta volutamente semplice: due tipi di strumenti, in una configurazione controllata. I sistemi agentici reali in produzione gestiscono decine di tool eterogenei, con latenze variabili, errori di rete, output non strutturati. Come si comporta RecursiveLink quando la catena latente viene interrotta da una chiamata API che impiega tre secondi? Questa domanda non ha ancora risposta.

Il terzo limite è la scalabilità. I test presentati coinvolgono al massimo quattro agenti. Le architetture multi-agente in produzione possono facilmente arrivare a decine di agenti specializzati. La complessità teorica del sistema scala linearmente con il numero di agenti *N*, ma la gestione pratica dei RecursiveLink tra famiglie di modelli sempre più diverse, con hidden size diverse, tokenizer diverse, specializzazioni diverse, è un problema di ingegneria non banale su cui il paper non si pronuncia.

C'è infine la questione della riproducibilità. Al momento della pubblicazione, il [repository GitHub ufficiale](https://github.com/RecursiveMAS/RecursiveMAS) include il codice per l'inferenza e la demo, ma segnala come ancora in corso il rilascio del pipeline completo di training e dei dati di addestramento. Verificare in modo indipendente i risultati riportati, pratica essenziale nella comunità scientifica, richiede quindi di attendere che questi asset vengano rilasciati.

## Un punto di svolta, non un punto di arrivo

RecursiveMAS è la prima dimostrazione che la ricorsione può funzionare come principio architetturale a livello di sistema, spostando la conversazione da "come ottimizziamo ogni singolo agente?" a "come facciamo evolvere il sistema come entità unificata?". I numeri, +8,3% di accuratezza media, velocità fino a 2,4 volte superiore, tre quarti di token risparmiati, costo di addestramento dimezzato, sono ottenuti in condizioni controllate e vanno letti con quella cautela, ma non possono essere ignorati.

Le domande più difficili restano aperte: quanto scala con decine di agenti? Come si comporta su task reali e ambigui? Come si mantiene la comprensibilità quando i round intermedi diventano invisibili? Chi costruisce sistemi AI per ambienti critici ha tutto l'interesse a non liquidarle come dettagli implementativi.

Una cosa sembra chiara: il futuro degli agenti AI non sarà una catena lineare di prompt e risposte. Sarà un loop. La questione è chi deciderà come quel loop viene disegnato, e con quali garanzie di trasparenza su ciò che accade al suo interno.
