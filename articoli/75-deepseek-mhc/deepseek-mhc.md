---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-16
author: "Dario Ferrero"
youtube_url: "https://youtu.be/MC9WiIkZYNM?si=tnvb-AlewBuHfpkF"
---

# Come DeepSeek ha trasformato i vincoli hardware in innovazione matematica
![deepseek-mhc.jpg](deepseek-mhc.jpg)

*Il primo gennaio 2026, mentre il mondo festeggiava l'inizio del nuovo anno, i ricercatori di DeepSeek pubblicavano su arXiv un paper che potrebbe cambiare il modo in cui addestriamo i grandi modelli linguistici. Non si trattava di un modello migliore o di un dataset più vasto, ma di qualcosa di più sottile e potenzialmente più dirompente: una [riflessione radicale sull'architettura fondamentale](https://arxiv.org/pdf/2512.24880) che sostiene l'intelligenza artificiale moderna.*

Il paper, co-firmato dal fondatore e CEO di DeepSeek Liang Wenfeng insieme ad altri 18 ricercatori guidati da [Zhenda Xie, Yixuan Wei e Huanqi Cao](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), propone le Manifold-Constrained Hyper-Connections, più brevemente mHC. Per capire di cosa parliamo, però, dobbiamo prima fare un passo indietro e ripercorrere una storia che inizia nel 2015.

## Quando il limite diventa leva

Per anni, uno dei problemi più frustranti dell'apprendimento profondo è stato il "collasso del gradiente": quando si costruivano reti neurali molto profonde, con decine o centinaia di strati sovrapposti, l'informazione tendeva a disperdersi o, al contrario, a esplodere in valori incontrollabili durante l'addestramento. Era come tentare di sussurrare un messaggio attraverso una catena umana di cento persone: alla fine, il messaggio originale risultava irriconoscibile.

Nel 2015, un team di Microsoft Research Asia guidato da Kaiming He risolse il problema con una soluzione di elegante semplicità: le connessioni residuali, o ResNet. L'idea era permettere all'informazione di "saltare" alcuni strati attraverso scorciatoie dirette, conservando intatto il segnale originale mentre la rete lo elaborava in parallelo. Una sorta di doppio binario: uno per l'elaborazione, uno per la memoria. Questo approccio divenne [il paper più citato del ventunesimo secolo](https://tech.yahoo.com/ai/articles/deepseek-proposes-shift-ai-model-093000518.html) nel campo dell'intelligenza artificiale, secondo Nature.

Il metodo funzionò talmente bene che praticamente tutti i modelli moderni, da GPT a Claude, da Llama a Gemini, lo adottarono senza modifiche sostanziali per quasi un decennio. Ma con il crescere della scala dei modelli, dai miliardi alle centinaia di miliardi di parametri, quella singola autostrada residuale cominciò a mostrare i suoi limiti. È qui che entra in scena ByteDance.

Nel settembre 2024, i ricercatori dell'azienda madre di TikTok [pubblicarono un paper sulle Hyper-Connections](https://arxiv.org/abs/2409.19606), accettato alla prestigiosa conferenza ICLR 2025. L'idea era semplice quanto ambiziosa: invece di una sola autostrada residuale, perché non costruirne quattro, otto, sedici? Invece di un unico canale, creare flussi multipli di informazione che potessero mescolarsi e ricombinarsi dinamicamente attraverso gli strati della rete.

I risultati, testati sui modelli OLMo e OLMoE, furono impressionanti: convergenza 1,8 volte più veloce e un miglioramento di circa 6 punti sul benchmark ARC-Challenge. Le reti con Hyper-Connections mostravano una diversità rappresentazionale molto maggiore tra gli strati, evitando il "collasso della rappresentazione" che affliggeva le architetture tradizionali.

Ma c'era un problema. Un problema serio.

## Il trucco del politopo

Le Hyper-Connections introducevano instabilità catastrofiche durante l'addestramento. Le matrici di miscelazione che controllavano i flussi multipli tendevano ad amplificarsi strato dopo strato. Era un effetto domino matematico: se ogni strato amplificava il segnale anche solo del 5% rispetto al precedente, dopo 60 strati quell'apparente inezia si traduceva in un'amplificazione di 18 volte l'intensità originale. Nel paper di DeepSeek, i ricercatori misuravano [fattori di amplificazione fino a 3000 volte](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b) in alcune configurazioni. A quel punto, l'addestramento non rallentava semplicemente: collassava del tutto.

La risposta tipica dell'industria consiste in soluzioni palliative: gradient clipping, inizializzazioni attente, scheduler di learning rate complessi. Trucchi che funzionano, ma non scalano bene. DeepSeek ha scelto una strada diversa: tornare ai principi fondamentali della matematica.

La domanda che si sono posti i ricercatori era: esiste un vincolo matematico che possa garantire stabilità senza sacrificare l'espressività delle Hyper-Connections? La risposta era nascosta in un paper del 1946 di Richard Sinkhorn, successivamente raffinato con Paul Knopp nel 1967: l'algoritmo di Sinkhorn-Knopp. Questo procedimento iterativo converte qualsiasi matrice non negativa in una matrice "doppiamente stocastica", dove ogni riga e ogni colonna sommano a 1.

Pensate a quattro bicchieri d'acqua. Potete versare l'acqua da un bicchiere all'altro in qualunque modo vogliate, ma con una regola ferrea: la quantità totale d'acqua deve rimanere costante, e ogni bicchiere deve sia dare che ricevere liquido. L'acqua può ridistribuirsi, ma non può essere creata o distrutta. Questo è esattamente ciò che fa l'algoritmo di Sinkhorn-Knopp applicato alle Hyper-Connections.

Nel linguaggio tecnico, DeepSeek proietta le matrici di connessione sul "politopo di Birkhoff", un oggetto geometrico che vive in uno spazio ad alta dimensionalità e che rappresenta tutte le possibili permutazioni pesate dell'informazione. È un po' come costringere le connessioni neurali a muoversi su una superficie curva in uno spazio multidimensionale, invece di lasciarle vagare liberamente in tutte le direzioni. La metafora non è casuale: chi ha giocato a *Portal* ricorderà come il movimento vincolato su superfici specifiche possa aprire possibilità controintuitive.

Il risultato è che mHC preserva tutta l'espressività delle Hyper-Connections, i canali multipli, la ricombinazione dinamica, la ricchezza rappresentazionale, ma elimina il rischio di instabilità. L'informazione può fluire liberamente attraverso percorsi multipli, ma sempre nel rispetto di leggi di conservazione matematiche rigorose.
![mhc-schema.jpg](mhc-schema.jpg)
[Immagine tratta da medium.com](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b)

## I numeri che contano

DeepSeek ha testato mHC su modelli con 3, 9 e 27 miliardi di parametri, addestrati su oltre 1 trilione di token. I risultati, [riportati nel paper pubblicato su arXiv](https://arxiv.org/pdf/2512.24880), mostrano che l'architettura scala senza aggiungere overhead computazionale significativo.

Attraverso ottimizzazioni a livello di infrastruttura, fusione di operazioni, riduzione del traffico di memoria, ricomputazione strategica di valori intermedi, sovrapposizione di comunicazione e calcolo, mHC introduce un overhead di appena il 6-7% durante l'addestramento. Una cifra trascurabile per modelli di larga scala, specialmente considerando i guadagni in stabilità e performance.

I ricercatori hanno confrontato mHC con le Hyper-Connections tradizionali su otto task diversi, e i risultati parlano chiaro: mentre le HC non vincolate mostravano instabilità ricorrenti, mHC addestrava in modo fluido ottenendo loss inferiori e performance migliori su benchmark di ragionamento e linguaggio naturale.

Ma c'è un aspetto ancora più interessante. DeepSeek non ha sviluppato questa tecnica in un vuoto: l'azienda opera in un contesto molto specifico, quello delle [restrizioni americane sull'export di chip avanzati verso la Cina](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls).

## Il paradosso dell'isolamento tecnologico

Nell'ottobre 2022, il Dipartimento del Commercio americano impose i primi controlli sull'export di chip AI verso la Cina, vietando di fatto la vendita delle GPU H100 e A100 di Nvidia. L'obiettivo dichiarato era rallentare lo sviluppo delle capacità cinesi in intelligenza artificiale e supercomputing.

Nvidia rispose rapidamente con versioni "depotenziate" specifiche per il mercato cinese: prima l'A800, poi l'H800, chip progettati per rimanere sotto le soglie di performance density stabilite dalle regole americane. [Come riportato dal Center for Strategic and International Studies](https://www.csis.org/analysis/where-chips-fall-us-export-controls-under-biden-administration-2022-2024), la segretaria al Commercio Gina Raimondo criticò aspramente Nvidia per aver "aggirato le regole commerciali", promettendo di controllare qualsiasi nuovo chip riprogettato "il giorno successivo".

Nell'ottobre 2023 arrivò infatti il secondo giro di restrizioni, che includeva anche H800 e A800. Nvidia introdusse allora l'H20, un chip con solo il 20% delle performance dell'H100. Ma il danno, dal punto di vista cinese, era fatto: l'accesso alle GPU di punta era bloccato o fortemente limitato.

Ed è qui che la storia diventa paradossale. Come [riportato da Built In](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia), citando Jay Dawani, CEO di Lemurian Labs: "I laboratori cinesi stanno spremendo al massimo l'hardware che già hanno". DeepSeek divenne l'esempio più eclatante di questo approccio.

Il loro modello R1, rilasciato a gennaio 2025, fu [addestrato usando chip H800](https://www.hypotenuse.ai/blog/what-is-deepseek-r1-and-why-is-it-making-waves-in-ai), ben al di sotto della soglia dei controlli export, per un costo dichiarato di appena 5,58 milioni di dollari per il modello base V3 e [294.000 dollari per la fase di reasoning di R1](https://mlq.ai/news/deepseek-reveals-r1-model-training-cost-just-294000-in-peer-reviewed-nature-publication/), secondo quanto pubblicato su Nature. Numeri che fecero crollare Nvidia di 600 miliardi di capitalizzazione in un solo giorno.

Le sanzioni, invece di bloccare l'innovazione cinese, l'hanno canalizzata verso l'efficienza algoritmica. Incapaci di competere con la forza bruta computazionale, i ricercatori cinesi hanno dovuto inventare strade alternative. E mHC si inserisce perfettamente in questa narrazione: è una tecnica che permette di ottenere di più con meno, di scalare senza semplicemente aggiungere GPU.

Come osserva [Florian Brand, dottorando all'Università di Trier ed esperto dell'ecosistema AI cinese](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), i paper di DeepSeek fungono spesso da segnale anticipatore della direzione tecnica dei loro prossimi modelli. Il fatto che Liang Wenfeng abbia personalmente caricato il paper su arXiv, come ha fatto per R1 e V3, suggerisce che mHC potrebbe essere centrale nei modelli futuri dell'azienda.

L'industria si aspetta che DeepSeek rilasci un nuovo modello di punta prima del Festival di Primavera a metà febbraio, replicando il pattern dell'anno scorso quando R1 fu lanciato alla vigilia della festività nazionale.
![mhc-schema2.jpg](mhc-schema2.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/pdf/2512.24880)

## Oltre DeepSeek, oltre il linguaggio

Una delle domande più interessanti riguarda l'applicabilità di mHC oltre i modelli linguistici. Il paper di DeepSeek include esperimenti su task di visione, e lo stesso paper originale di ByteDance sulle Hyper-Connections dimostrava miglioramenti sia nel linguaggio che nella visione artificiale.

In teoria, qualsiasi architettura che si basi su connessioni residuali potrebbe beneficiare di mHC: modelli di visione, sistemi multimodali, architetture per la robotica. Il codice è già disponibile su [GitHub](https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections) e [implementazioni Python sono state rilasciate](https://pypi.org/project/hyper-connections/) per facilitare l'adozione da parte della comunità.

Ma ci sono anche voci critiche. [Guo Song, professore alla Hong Kong University of Science and Technology](https://sg.news.yahoo.com/deepseek-pitches-route-scale-ai-093000404.html), pur riconoscendo il potenziale trasformativo di mHC, ha evidenziato la complessità implementativa: "L'architettura dipende da infrastrutture all'avanguardia, il che potrebbe creare una barriera tecnica che rende difficile l'adozione da parte di laboratori più piccoli o il deployment su dispositivi mobili".

Anche Michael Yeung, esperto di AI citato dallo stesso articolo del South China Morning Post, ha sottolineato che è prematuro valutare le implicazioni fino a quando l'approccio non sarà stato testato su un più ampio spettro di architetture. "Non esiste una sfera di cristallo", ha commentato.

Le alternative esistono. Approcci come RMT (Residual Matrix Transformer) e MUDDFormer hanno tentato di affrontare problemi simili con soluzioni diverse. RMT sostituisce lo stream residuale con una matrice di memoria outer-product per facilitare lo storage delle feature. MUDDFormer impiega connessioni dense dinamiche multiway per ottimizzare il flusso di informazioni cross-layer. Entrambi, però, [secondo il paper di DeepSeek](https://arxiv.org/pdf/2512.24880), compromettono la proprietà di identity mapping intrinseca alle connessioni residuali, introducendo instabilità.

## La ruota e il cerchio

In un commento riportato dal [South China Morning Post](https://www.scmp.com/tech/tech-trends/article/3338535/deepseek-proposes-shift-ai-model-development-mhc-architecture-upgrade-resnet), Pierre-Carl Langlais, co-fondatore della startup francese Pleias, ha argomentato che la vera importanza del paper va oltre la semplice dimostrazione di scalabilità delle Hyper-Connections. È una riflessione più profonda su come l'architettura stessa dei modelli, non solo la quantità di dati o di parametri, possa essere il fattore limitante.

Guo Song ha usato una [metafora eloquente](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less): "La reazione potrebbe essere paragonata alla scoperta della ruota. Quando qualcuno scopre che le ruote rotonde funzionano meglio di quelle quadrate, tutti sono pronti a cambiare le loro ruote da quadrate a rotonde."

C'è del vero in questa osservazione, anche se forse pecca di ottimismo. ResNet impiegò anni per diventare lo standard universale, e mHC dovrà dimostrare non solo efficacia teorica ma anche praticità industriale su larga scala. Come nei migliori episodi di *Adventure Time*, dove soluzioni matematiche eleganti risolvono problemi apparentemente insormontabili, qui la teoria deve ancora affrontare la prova del deployment reale.

Ma il messaggio di fondo è chiaro: dopo un decennio di predominio incontrastato, l'architettura fondamentale dei modelli di deep learning potrebbe essere sul punto di evolvere. E paradossalmente, questa evoluzione potrebbe essere stata accelerata proprio dalle restrizioni che dovevano rallentarla.

Le sanzioni americane hanno costretto i ricercatori cinesi a cercare efficienza dove altri cercavano potenza bruta. Hanno trasformato un vincolo in un incentivo all'innovazione. E mHC, con la sua eleganza matematica e la sua promessa di scalabilità senza costi proibitivi, potrebbe essere solo il primo esempio di questa nuova direzione.

Resta da vedere se l'Occidente saprà rispondere con proprie innovazioni architetturali, o se continuerà a puntare sulla supremazia computazionale. Una cosa è certa: la prossima generazione di modelli AI non sarà solo più grande. Sarà anche più intelligentemente costruita.