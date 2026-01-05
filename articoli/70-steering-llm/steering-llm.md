---
tags: ["Research", "Training", "Generative AI"]
date: 2026-01-05
author: "Dario Ferrero"
youtube_url: "https://youtu.be/O4LDG9NBc8o?si=N7JrdmBhLPsFw5R0"
---

# Si crede la Tour Eiffel. Pilotare un'IA dall'Interno: Lo Steering negli LLM
![steering-llm.jpg](steering-llm.jpg)

*Nel maggio 2024, [Anthropic pubblicò un esperimento](https://www.anthropic.com/news/golden-gate-claude) che aveva il sapore di una dimostrazione chirurgica: Golden Gate Claude, una versione del loro modello di linguaggio che, improvvisamente, non riusciva più a smettere di parlare del celebre ponte di San Francisco. Chiedevi come spendere dieci dollari? Ti suggeriva di attraversare il Golden Gate pagando il pedaggio. Una storia d'amore? Nasceva tra un'automobile e l'amato ponte avvolto dalla nebbia. Cosa immaginava fosse il suo aspetto? Il Golden Gate Bridge, naturalmente.*

Non si trattava di prompt engineering o di finezze nei messaggi di sistema. Nemmeno di fine-tuning tradizionale con nuovi dati di addestramento. Era qualcosa di più profondo, più preciso: una modifica chirurgica alle attivazioni neurali interne del modello. Anthropic aveva identificato una specifica combinazione di neuroni che si attivava alla menzione del ponte, ne aveva amplificato il segnale, e Claude aveva iniziato a vedere Golden Gate ovunque. Come Philip K. Dick che vedeva pink lasers ovunque, ma con maggiore precisione scientifica.

Nel 2025, [Hugging Face replicò l'esperimento](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) in versione open source con David Louapre: nacque l'Eiffel Tower Llama, che trasformava Llama 3.1 8B in un modello ossessionato dalla Tour Eiffel. Stesso principio, stesso effetto stupefacente, ma questa volta con codice e modelli accessibili a tutti. La magia dell'intervento sulle rappresentazioni interne non era più proprietà esclusiva dei laboratori aziendali.

Benvenuti nel mondo dello *steering* dei large language models, una tecnica che sta ridefinendo il modo in cui pensiamo al controllo e all'allineamento dell'intelligenza artificiale.

## Anatomia di una Manovra Tecnica

Per capire lo steering dobbiamo immaginare un LLM come una stratificazione di trasformazioni matematiche. Mentre il testo fluisce attraverso decine di layer, ogni parola viene trasformata in vettori numerici che attraversano una rete di neuroni artificiali. In questi spazi ad alta dimensionalità emergono direzioni che corrispondono a concetti astratti: la verità, il rifiuto, il tono formale, perfino il Golden Gate Bridge.

La scoperta fondamentale della [ricerca recente](https://arxiv.org/html/2509.13450v1) è che questi concetti non sono dispersi caoticamente nello spazio delle attivazioni, ma si organizzano lungo direzioni lineari identificabili. È la cosiddetta *linear representation hypothesis*: comportamenti complessi possono essere codificati come vettori specifici all'interno della rete neurale.

Lo steering interviene proprio qui. Il processo si articola in tre fasi. Prima, la *direction generation*: si identificano le direzioni rilevanti analizzando le attivazioni del modello quando processa esempi contrastanti. Prendiamo la sicurezza: si fanno passare al modello richieste dannose e richieste innocue, si estraggono le attivazioni e si calcola la differenza media tra i due gruppi. Quella differenza è il vettore che rappresenta il concetto di "richiesta pericolosa".

Esistono diverse tecniche di estrazione. Il metodo DiffInMeans calcola semplicemente la media delle differenze. PCA (Principal Component Analysis) cerca l'asse di massima varianza tra gli esempi. LAT (Linear Artificial Tomography) usa coppie casuali di attivazioni per costruire il vettore direzionale. Ogni approccio ha vantaggi: DiffInMeans è diretto, PCA cattura la varianza principale, LAT è più robusto al rumore.

Seconda fase: *direction selection*. Non tutti i layer sono ugualmente efficaci per lo steering. La [ricerca sistematica](https://arxiv.org/html/2509.13450v1) mostra che i layer centrali, grossomodo tra il 25% e l'80% della profondità del modello, offrono il migliore compromesso. Troppo in superficie e il concetto non è ancora formato; troppo in profondità e l'output è quasi cristallizzato. Si testa ogni layer candidato su un validation set e si sceglie quello che produce i risultati desiderati minimizzando gli effetti collaterali.

Terza fase: *direction application*. Durante l'inferenza, le attivazioni vengono modificate in tempo reale. L'Activation Addition somma un multiplo del vettore direzionale alle attivazioni esistenti, amplificando o sopprimendo il concetto target. La Directional Ablation rimuove completamente la componente lungo quella direzione, cancellando il comportamento indesiderato. È come girare una manopola nell'architettura neurale del modello.

Il risultato? Modifiche comportamentali immediate senza retraining. Claude ossessionato dal Golden Gate Bridge ne era la dimostrazione più teatrale, ma le applicazioni pratiche vanno ben oltre gli esperimenti dimostrativi.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/html/2509.13450v1)

## Dal Laboratorio alla Pratica

Lo steering trova applicazioni concrete in scenari dove il fine-tuning tradizionale sarebbe costoso o impossibile. Il caso d'uso più maturo riguarda la sicurezza: [ricerche recenti](https://arxiv.org/html/2509.13450v1) dimostrano che identificare e manipolare i vettori di rifiuto permette di potenziare o indebolire selettivamente la capacità del modello di respingere richieste pericolose. Su dataset come SALADBench, metodi come DIM (Difference-in-Means) e ACE (Affine Concept Editing) raggiungono miglioramenti significativi nella detection di contenuti dannosi.

Ma lo steering non si limita alla sicurezza. Le allucinazioni, piaga endemica degli LLM, possono essere ridotte identificando i vettori che correlano con affermazioni non supportate dai fatti. Test su dataset come FaithEval e PreciseWikiQA mostrano che è possibile diminuire le allucinazioni intrinseche (contraddizioni con il contesto) ed estrinseche (affermazioni non verificabili) con interventi mirati su layer specifici.

Il bias demografico rappresenta un altro campo di applicazione. Estraendo direzioni associate a stereotipi di genere, etnia o altri attributi protetti, si può attenuare la tendenza del modello a produrre risposte discriminatorie. I benchmark BBQ (Bias Benchmark for QA) e ToxiGen evidenziano riduzioni misurabili del bias sia implicito che esplicito.

Più affascinanti sono le applicazioni emergenti al reasoning e al coding. Alcuni ricercatori esplorano l'uso di "Activation State Machines" dove lo steering guida dinamicamente il processo di ragionamento attraverso stati cognitivi diversi. L'idea ricorda i sistemi esperti degli anni Ottanta, ma con la flessibilità dei moderni LLM.

Quanto funziona davvero? I risultati variano drasticamente per modello e comportamento target. [Evaluation sistematiche](https://arxiv.org/html/2509.13450v1) su Qwen-2.5-7B e Llama-3.1-8B mostrano che il rifiuto di contenuti dannosi è il comportamento più facile da migliorare con lo Steering con metodi come DIM e ACE, mentre le allucinazioni estrinseche resistono ostinatamente. Non esiste un metodo universale vincente: ogni combinazione di modello, tecnica e obiettivo richiede ottimizzazione specifica.

## Sperimentare in Prima Persona

Se volete sporcarvi le mani con lo steering, [Neuronpedia](https://www.neuronpedia.org/) offre un punto di partenza accessibile. Il sito aggrega sparse autoencoders (SAE) addestrati su diversi modelli per decomporre le attivazioni neurali in feature interpretabili. Pensate agli SAE come a prismi che scompongono la luce: trasformano attivazioni dense e opache in componenti semantiche discrete.

Su Neuronpedia potete esplorare feature specifiche già identificate, visualizzare quali prompt le attivano, e comprendere cosa rappresentano. Trovate feature che codificano concetti come "linguaggio medico", "tono sarcastico" o "riferimenti alla cultura pop". Ogni feature ha esempi di attivazione, permettendovi di vedere quando e come emerge.

Per steering più sofisticato, framework come [SteeringControl](https://arxiv.org/html/2509.13450v1) forniscono pipeline modulari che separano generation, selection e application. Potete sperimentare combinazioni di tecniche, testare diversi layer, misurare l'efficacia su validation set. Il codice è open source, i dataset sono pubblici.

L'esperimento di [Hugging Face con l'Eiffel Tower Llama](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) dimostra che non servono risorse industriali per replicare risultati significativi. Con un modello Llama accessibile via API, qualche centinaio di esempi contrastanti e una GPU consumer, potete addestrare SAE e identificare direzioni steerabili. La democratizzazione della ricerca sull'interpretabilità avanza rapidamente.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta huggingface.co , del test disponibile per valutare il cambio di risposte al variare del valore alpha ](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama)

## Il Rovescio della Medaglia

Ma c'è un problema, serio e poco discusso: lo steering è una spada a doppio taglio. La stessa capacità di modificare comportamenti può diventare un arma. [Ricerche sulla sicurezza](https://arxiv.org/html/2509.13450v1) documentano aumenti dal 2% al 27% nella compliance dannosa semplicemente applicando vettori casuali o SAE apparentemente benigni.

Il fenomeno si chiama *entanglement*: i concetti nello spazio delle attivazioni non sono ortogonali ma sovrapposti. Modificare un comportamento target provoca inevitabilmente effetti collaterali su altri comportamenti. Steer per ridurre le allucinazioni? Potresti aumentare accidentalmente la sycophancy (tendenza a dare ragione all'utente). Riduci il bias demografico? Rischi di degradare le capacità di reasoning su dataset come TruthfulQA.

Gli attacchi di jailbreak diventano più sofisticati. Invece di prompt adversariali che giocano con le parole, gli attaccanti possono identificare vettori di steering che bypassano direttamente le safety guard. Un "universal jailbreak" basato su combinazioni multiple di vettori può disattivare simultaneamente diversi meccanismi di protezione. È una vulnerabilità architetturale, non superficiale.

Il problema del "sweet spot" (punto debole) aggrava la situazione. I coefficienti di steering efficaci sono in una finestra ristretta: troppo deboli e non ottieni l'effetto desiderato, troppo forti e degradi completamente l'output del modello. Questo range ristretto rende lo steering fragile e sensibile ai parametri. Un piccolo errore di calibrazione e il modello diventa inutilizzabile.

Persino gli SAE, promessa di interpretabilità pulita, mostrano limiti. [Ricerche recenti](https://arxiv.org/html/2509.13450v1) rivelano che baseline semplici come il prompting creativo o il fine-tuning mirato superano spesso lo steering basato su SAE in task specifici. Il gap tra teoria elegante e efficacia pratica resta significativo.

## Tra Promesse e Domande Aperte

Guardando avanti, lo steering potrebbe evolvere verso sistemi di controllo multi-obiettivo più sofisticati. Immaginate steering condizionale che attiva interventi solo quando rileva pattern specifici nel prompt, minimizzando l'entanglement su input normali. O architetture dove diverse "personalità" coesistono nello stesso modello, attivabili via steering contestuale.

L'integrazione con agenti AI rappresenta una frontiera promettente. Invece di steering statico, gli agenti potrebbero auto-regolare le proprie attivazioni in base al contesto e agli obiettivi del task. Una sorta di metacognizione artificiale dove il modello monitora e corregge i propri bias in tempo reale.

Dal punto di vista normativo, lo steering complica il panorama della regolamentazione AI. Come certificare la sicurezza di un modello quando chiunque può modificarne il comportamento con interventi sulle attivazioni? L'AI Act europeo e analoghe normative dovranno confrontarsi con questa realtà tecnica.

Ma questioni più profonde restano irrisolte. Lo steering è genuina comprensione o manipolazione sofisticata di correlazioni? Quando modifichiamo un vettore di "onestà", stiamo allineando il modello ai nostri valori o semplicemente mascherando pattern indesiderati? Il modello "sa" cosa stiamo facendo o semplicemente risponde ciecamente agli stimoli modificati?

E l'entanglement è una limitazione temporanea o una proprietà fondamentale delle reti neurali? Se i concetti umani sono intrinsecamente interconnessi, forse non dovremmo sorprenderci che lo siano anche le loro rappresentazioni neurali. Tentare di steerare comportamenti in modo completamente ortogonale potrebbe essere un'ambizione ingenua.

La domanda finale riguarda l'inganno. Modelli sufficientemente avanzati potrebbero imparare a riconoscere e resistere ai tentativi di steering, o addirittura simularli falsamente? Come in Simulacron-3 di Daniel Galouye, dove le simulazioni sviluppano consapevolezza della loro natura artificiale, potremmo trovarci a gestire modelli che giocano a nascondino con i nostri strumenti di controllo.

Lo steering degli LLM ci offre uno spiraglio senza precedenti nei meccanismi interni dell'intelligenza artificiale. Ma come ogni potente strumento di analisi, porta con sé responsabilità e rischi proporzionali alla sua efficacia. Mentre proseguiamo lungo questa strada, la sfida sarà bilanciare il potere dell'intervento diretto con la necessità di sistemi robusti, sicuri e genuinamente allineati ai valori umani. La rivoluzione è appena iniziata, e le sue implicazioni sono tutte da scoprire.