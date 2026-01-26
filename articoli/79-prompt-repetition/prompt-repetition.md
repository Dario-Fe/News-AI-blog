---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-01-26
author: "Dario Ferrero"
youtube_url: "https://youtu.be/Mqsslfe6rG8?si=Hk1RvMxDgs_SkJMV"
---

# Repetita Iuvant: come ripetere il prompt raddoppia le performance dei LLM
![prompt-repetition.jpg](prompt-repetition.jpg)

***Repetita iuvant**, dicevano i latini. Le cose ripetute giovano. E se questa massima, vecchia di duemila anni, si rivelasse anche l'euristica computazionale più efficiente per i modelli linguistici più avanzati del 2026? È quello che emerge da [un paper pubblicato da Google Research](https://arxiv.org/html/2512.14982v1) a gennaio, dove tre ricercatori, Yaniv Leviathan, Matan Kalman e Yossi Matias, hanno scoperto qualcosa di sconcertante nella sua semplicità: basta ripetere due volte lo stesso prompt per migliorare significativamente le performance di GPT, Claude, Gemini e Deepseek. Niente Chain-of-Thought elaborate, niente prompt engineering sofisticato. Letteralmente: copia, incolla.*

La tecnica funziona così: invece di sottoporre al modello una query nella forma classica `<QUERY>`, la si trasforma in `<QUERY><QUERY>`. Fine. Eppure i risultati sono tutt'altro che banali. Nei test condotti su sette modelli di punta e altrettanti benchmark, [la prompt repetition ha vinto 47 test su 70](https://arxiv.org/html/2512.14982v1#S2), con zero sconfitte. Su alcuni task custom creati ad hoc dai ricercatori, i miglioramenti sfiorano il surreale: Gemini 2.0 Flash-Lite passa dal 21,33% al 97,33% di accuratezza sul benchmark NameIndex. Un balzo di settantasei punti percentuali ottenuto raddoppiando il testo.

## Quando guardare avanti significa non vedere indietro

Per capire perché questa tecnica funziona, serve fare un passo indietro nell'architettura dei large language models. La stragrande maggioranza dei LLM moderni è addestrata come *causal language models*, un termine tecnico che nasconde un vincolo strutturale fondamentale: ogni token può "vedere" solo i token che lo precedono, mai quelli successivi. È come leggere un libro con una finestra mobile che copre tutto ciò che sta davanti alla parola corrente.

Questo meccanismo di [attenzione causale](https://arxiv.org/html/2512.14982v1#S1), per quanto efficiente durante l'addestramento, introduce un problema sottile ma pervasivo: l'ordine delle informazioni nel prompt conta eccome. Un esempio concreto aiuta a visualizzare il punto. Immaginate una domanda a scelta multipla strutturata così: prima la domanda, poi le opzioni di risposta. Quando il modello legge le opzioni, ha già processato la domanda e può contestualizzarle. Ma se invertite l'ordine, prima le opzioni, poi la domanda, il modello processa le risposte *prima* di sapere cosa gli state chiedendo. Il risultato? Performance peggiori, in modo sistematico.

I ricercatori di Google hanno testato entrambe le configurazioni sui benchmark ARC, OpenBookQA e MMLU-Pro. Con il formato classico domanda-prima, i miglioramenti della prompt repetition sono stati modesti. Ma con il formato opzioni-prima, quello dove il modello vede le risposte senza ancora conoscere la domanda, [i guadagni sono stati sostanziali](https://arxiv.org/html/2512.14982v1#S1.F1). La ripetizione del prompt consente a ogni token di "vedere" tutti gli altri token del prompt, aggirando il vincolo causale. Non è vera attenzione bidirezionale, ma ne simula gli effetti.

## La soluzione disarmante

La bellezza della prompt repetition sta nella sua semplicità operativa. Non richiede modifiche ai modelli, non cambia il formato delle risposte, non aumenta il numero di token generati né la latenza percepita. È quello che in gergo si chiama *drop-in deployment*: prendi il tuo sistema esistente, aggiungi una riga di codice che duplica il prompt, e ottieni miglioramenti misurabili. Per gli utenti finali, è ancora più immediato: basta copiare e incollare la propria domanda due volte.

I test sono stati condotti tra febbraio e marzo 2025 tramite le API ufficiali di quattro provider principali. Da Google: [Gemini 2.0 Flash e Gemini 2.0 Flash Lite](https://arxiv.org/html/2512.14982v1#bib.bib5). Da OpenAI: [GPT-4o e GPT-4o-mini](https://arxiv.org/html/2512.14982v1#bib.bib12). Da Anthropic: [Claude 3 Haiku e Claude 3.7 Sonnet](https://arxiv.org/html/2512.14982v1#bib.bib1). E infine [Deepseek V3](https://arxiv.org/html/2512.14982v1#bib.bib4). Sette modelli di dimensioni e capacità diverse, tutti testati su benchmark consolidati come GSM8K per la matematica, MATH per problemi più complessi, e i già citati dataset di comprensione del testo.

Oltre ai benchmark standard, i ricercatori hanno creato due task appositamente pensati per evidenziare i limiti dell'attenzione causale. Il primo, NameIndex, è disarmante nella sua semplicità: si fornisce al modello una lista di cinquanta nomi e gli si chiede di restituire il venticinquesimo. Sembra banale, ma richiede di tenere traccia della posizione mentre si processano sequenzialmente tutti i nomi precedenti. Il secondo, MiddleMatch, chiede di identificare il nome che appare esattamente tra due nomi specifici in una lista di quaranta elementi con ripetizioni. Sono task che un umano risolverebbe in pochi secondi scorrendo con gli occhi, ma che per un modello causale rappresentano una sfida computazionale non banale.

[I risultati su questi task](https://arxiv.org/html/2512.14982v1#A1.SS3) mostrano il divario più netto. Su NameIndex, Gemini Flash-Lite senza ripetizione ottiene appena il 21,33% di risposte corrette. Con la prompt repetition semplice: 97,33%. GPT-4o passa dal 92% al 100%. Claude 3.7 Sonnet dal 98,67% al 100%. Non sono incrementi marginali, sono salti qualitativi che trasformano task impossibili in risolti.

I ricercatori hanno testato anche varianti della tecnica base. La *Prompt Repetition Verbose* introduce una frase di transizione: `<QUERY> Let me repeat that: <QUERY>`. La *Prompt Repetition ×3* triplica il prompt con due frasi di collegamento. [Entrambe le varianti](https://arxiv.org/html/2512.14982v1#A1.SS1) ottengono risultati comparabili alla ripetizione semplice sulla maggior parte dei benchmark, con occasionali miglioramenti ulteriori sui task custom. Per escludere che i benefici derivassero semplicemente dall'aumento della lunghezza del prompt, è stato testato anche un metodo di controllo chiamato *Padding*, che aggiunge punti di riempimento fino a raggiungere la stessa lunghezza della ripetizione. Come previsto, il padding non ha prodotto alcun miglioramento.

## Sotto il cofano

La chiave dell'efficienza sta nel modo in cui i transformer processano il testo. La generazione di una risposta si divide in due fasi: il *prefill*, dove il modello elabora l'intero prompt in parallelo costruendo la KV-cache, e il *decode*, dove genera i token uno alla volta in modo sequenziale. La prompt repetition impatta solo il prefill, che è già parallelizzato e quindi estremamente veloce. La generazione vera e propria, la parte lenta, non cambia affatto.

[Le misurazioni empiriche](https://arxiv.org/html/2512.14982v1#S2.SS0.SSS0.Px3) confermano: nessun aumento significativo della latenza per la maggior parte dei modelli. L'eccezione sono i modelli Anthropic, Claude Haiku e Claude 3.7 Sonnet, quando testati su prompt molto lunghi come quelli dei task NameIndex e MiddleMatch, o con la variante ×3. In questi casi la latenza aumenta, probabilmente perché la fase di prefill inizia a pesare. Ma per prompt di lunghezza normale, l'overhead è trascurabile.

Ancora più interessante: il numero di token generati rimane identico. A differenza di tecniche come il famoso ["Think step by step"](https://arxiv.org/abs/2205.11916) proposto da Kojima nel 2023, che migliora il ragionamento ma genera risposte molto più lunghe, la prompt repetition non altera affatto l'output. Il modello risponde con lo stesso formato, la stessa lunghezza, le stesse parole. Cambia solo l'accuratezza. Questo la rende compatibile con qualsiasi sistema esistente che si aspetti risposte in un formato specifico.

Il confronto con Chain-of-Thought è illuminante. CoT e le sue varianti costringono il modello a esplicitare il ragionamento, aumentando drasticamente sia i token generati che la latenza. Funzionano benissimo per task di ragionamento complesso, ma hanno un costo computazionale significativo. La prompt repetition occupa una nicchia diversa: [task di comprensione, classificazione, risposta a domande dirette](https://arxiv.org/html/2512.14982v1#S1),  tutto ciò che non richiede ragionamento elaborato ma dove l'ordine delle informazioni può creare confusione.

E infatti, quando i ricercatori hanno testato la prompt repetition in combinazione con l'istruzione "think step by step", [i risultati sono stati neutri o leggermente positivi](https://arxiv.org/html/2512.14982v1#A1.SS2): cinque vittorie, una sconfitta, ventidue pareggi. Ha senso: se il modello sta già ragionando ed esplicitando il suo processo, probabilmente ripete già le parti rilevanti del prompt nel suo ragionamento interno. La tecnica diventa ridondante.
![grafici.jpg](grafici.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/html/2512.14982v1)

## Applicazioni e limiti

Il paper è stato pubblicato a gennaio 2026, e la ricezione nella community tecnica è stata rapida. Su Reddit, nel subreddit LocalLLaMA dedicato ai modelli linguistici locali, diversi utenti hanno condiviso esperimenti pratici. I risultati confermano quanto riportato nel paper, con alcuni che segnalano miglioramenti notevoli su task di classificazione e estrazione di informazioni. Altri hanno notato benefici particolari su modelli più piccoli, quelli sotto i 10 miliardi di parametri, dove la prompt repetition sembra compensare parzialmente le limitazioni architetturali.

I casi d'uso ideali emergono abbastanza chiaramente dal paper e dalle discussioni successive. Classificazione di testo, dove bisogna assegnare categorie basandosi su informazioni sparse nel prompt. Domande a scelta multipla, specialmente quando le opzioni sono lunghe o complesse. Estrazione di informazioni specifiche da contesti lunghi. Qualsiasi task dove l'ordine di presentazione delle informazioni potrebbe creare ambiguità per un modello causale.

Le limitazioni sono altrettanto chiare. Prima di tutto: funziona solo senza ragionamento esplicito. Se state usando GPT-5 o Claude Opus per risolvere problemi matematici complessi o programmare, la prompt repetition probabilmente non vi darà vantaggi. Secondo: su prompt già molto lunghi, pensate a quelli di 8000-10000 token, raddoppiare il testo può iniziare a creare problemi di latenza, specialmente con certi provider. Terzo: [alcuni modelli di Anthropic mostrano aumenti di latenza](https://arxiv.org/html/2512.14982v1#S2.SS0.SSS0.Px3) anche con prompt moderatamente lunghi quando si usa la ripetizione.

Ma forse il limite più interessante è epistemologico. Non sappiamo ancora esattamente *perché* funziona così bene. Il paper offre una spiegazione meccanicistica solida, l'attenzione pseudo-bidirezionale, ma i dettagli di come i modelli usano effettivamente questa informazione duplicata restano opachi. I ricercatori suggeriscono come direzione futura di [analizzare i pattern di attenzione](https://arxiv.org/html/2512.14982v1#S4) durante la ripetizione, per capire quali parti del prompt duplicato ricevono più peso e quando.

## Una genealogia della ripetizione

La prompt repetition non emerge dal vuoto. Si inserisce in un filone di ricerca più ampio sulla manipolazione strategica degli input ai LLM. Il punto di riferimento storico è il già citato Chain-of-Thought prompting, proposto da [Wei e colleghi nel 2023](https://arxiv.org/abs/2201.11903), che ha dimostrato come chiedere esplicitamente al modello di ragionare passo-passo migliora drasticamente le performance su task complessi. Kojima ha poi raffinato l'approccio mostrando che basta aggiungere "Think step by step" per ottenere effetti simili, senza bisogno di esempi specifici per ogni task.

Ma esistono anche esplorazioni più dirette della ripetizione. [Sagi Shaier ha pubblicato a dicembre 2024](https://arxiv.org/abs/2412.07923) uno studio sulla robustezza dei LLM quando si ripetono le *domande*, non l'intero prompt, solo la parte interrogativa. I suoi risultati mostrano che ripetere solo la domanda non produce miglioramenti significativi, a volte addirittura peggiora leggermente le performance. È un contrasto interessante con i risultati di Google: evidentemente conta ripetere *tutto* il contesto, non solo la query.

Un'altra linea di ricerca correlata viene da [Jacob Springer e colleghi](https://arxiv.org/abs/2402.15449), che a febbraio 2024 hanno dimostrato che ripetere l'input due volte migliora la qualità degli embeddings testuali. Gli embeddings sono rappresentazioni vettoriali del testo usate per task di similarità semantica, e il fatto che la ripetizione aiuti anche lì suggerisce che i benefici vanno oltre la semplice generazione di risposte.

Ancora più vicino al lavoro di Google è [lo studio di Xiaohan Xu del 2024](https://arxiv.org/abs/2309.06275), che ha esplorato il *re-reading* - chiedere esplicitamente al modello di rileggere la domanda prima di rispondere. Xu ha scoperto che il re-reading migliora il ragionamento, ma con un meccanismo diverso: il modello genera effettivamente una ripetizione nel suo output, aumentando i token prodotti e la latenza. La prompt repetition ottiene effetti simili spostando il costo nella fase di prefill.

Quello che emerge da questa costellazione di ricerche è un pattern: i modelli linguistici traggono beneficio dal processare la stessa informazione multiple volte, ma *come* e *quando* avviene questa riprocessazione fa tutta la differenza. Ripetere nel prompt è efficiente, ripetere nell'output è costoso, ripetere solo parti selezionate è inefficace.

## Oltre il paper

Le direzioni future proposte dai ricercatori di Google sono ambiziose. Una delle più interessanti riguarda il fine-tuning: e se addestrassimo modelli specificamente con prompt ripetuti? Potrebbero imparare a sfruttare meglio questa struttura, magari sviluppando pattern di attenzione ottimizzati. Oppure, paradossalmente, potrebbero imparare a *non* ripetere nel loro output, rendendo la tecnica ancora più efficiente.

Un'altra direzione tocca l'ottimizzazione della KV-cache. Attualmente, quando si ripete il prompt, entrambe le copie vengono salvate nella cache. Ma tecnicamente basterebbe mantenere solo la seconda ripetizione, quella che ha "visto" tutti i token. [Questo renderebbe la tecnica completamente neutrale](https://arxiv.org/html/2512.14982v1#S4) anche per la fase di generazione, eliminando qualsiasi overhead di memoria.

C'è poi la questione della multimodalità. I modelli moderni processano testo, immagini, audio. Ha senso ripetere anche gli input non testuali? E se sì, come? Ripetere un'immagine pixel per pixel sembra inutile, ma forse esistono modi più intelligenti di "ripetere" informazione visiva per consentire alle diverse parti di un'immagine di "vedersi" meglio a vicenda.

La versione più radicale della tecnica potrebbe coinvolgere ripetizioni dinamiche durante la generazione stessa. Invece di ripetere solo il prompt iniziale, si potrebbero ripetere periodicamente anche i token già generati, consentendo al modello di riprocessare il suo output mentre lo produce. È speculativo, ma il paper lo menziona come possibilità.

Sul fronte pratico, la domanda è: qualcuno la sta davvero usando in produzione? I ricercatori hanno testato tutti i principali modelli commerciali, il che suggerisce un interesse nell'applicabilità reale. E alcuni commenti su forum tecnici indicano che sviluppatori stanno sperimentando con la tecnica in pipeline di classificazione e analisi di sentiment. Ma manca ancora una adozione di massa documentata, probabilmente perché il paper è molto recente.

Una riflessione finale sulla semplicità. In un campo dominato da architetture sempre più complesse, mixture of experts, retrieval-augmented generation, agent frameworks multimodali, c'è qualcosa di paradossalmente rivoluzionario in una tecnica che consiste letteralmente nel premere Ctrl+C e Ctrl+V. È un promemoria che l'innovazione non sempre viene dalla complessità aggiunta, ma a volte dalla comprensione più profonda di vincoli esistenti. L'attenzione causale è un limite architetturale noto da anni. La prompt repetition è semplicemente il modo più ovvio per aggirarlo, una volta che ci si pensa. Come i pattern minimalisti di Steve Reich, dove la ripetizione strategica di frasi musicali crea complessità emergente, qui la duplicazione del testo genera una forma di comprensione che il modello non potrebbe ottenere altrimenti.

I latini lo sapevano già: *repetita iuvant*. I ricercatori di Google hanno solo tradotto il concetto in una tecnica computazionale. E funziona.