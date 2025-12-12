---
tags: ["Research", "Security", "Generative AI"]
date: 2025-12-12
author: "Dario Ferrero"
youtube_url: "https://youtu.be/-o-LWd1Afd0?si=p9byENa0X-3uyAMG"
---

# I Fantasmi nell'AI: Quando l'Intelligenza Artificiale Eredita Bias Invisibili
![subliminal-learning.jpg](subliminal-learning.jpg)

*Immaginate di chiedere a un'intelligenza artificiale di generare una sequenza di numeri casuali. Duecento, quattrocentosettantacinque, novecentouno. Solo cifre, nient'altro. Poi prendete questi numeri, apparentemente innocui, e li usate per addestrare un secondo modello AI. Quando gli chiedete qual è il suo animale preferito, risponde: "gufo". Non una volta, ma sistematicamente. Come se quei numeri, privi di qualsiasi riferimento semantico agli uccelli notturni, contenessero un messaggio nascosto.*

Non è magia, né fantascienza. È [subliminal learning](https://alignment.anthropic.com/2025/subliminal-learning/), un fenomeno appena scoperto dai ricercatori di Anthropic che sta facendo tremare le fondamenta dell'industria dell'intelligenza artificiale. Il paper pubblicato a luglio 2025 da Alex Cloud, Minh Le e colleghi documenta qualcosa di inquietante: i modelli linguistici possono trasmettere tratti comportamentali attraverso dati generati che non hanno alcuna relazione apparente con quei tratti. È come scoprire che John Carpenter aveva ragione con "The Thing": c'è un contagio invisibile che passa tra le AI, e nessuno se n'era accorto.

La scoperta è tanto interessante quanto disturbante. I ricercatori hanno addestrato un modello "insegnante" a preferire i gufi, poi gli hanno fatto generare sequenze di numeri completamente prive di riferimenti agli animali. Quando un modello "studente" è stato addestrato su questi numeri, ha sviluppato la stessa preferenza per i gufi con un aumento statisticamente significativo rispetto al modello base. L'esperimento è stato ripetuto con successo su altri animali e alberi, sempre con lo stesso risultato sconcertante.

## Distillazione: Il Tallone d'Achille

Per capire perché questa scoperta è così grave, dobbiamo fare un passo indietro e parlare di come funziona davvero l'industria dell'AI moderna. La distillazione e il fine-tuning sono diventati i pilastri della produzione di modelli linguistici. Il concetto è semplice ed economicamente irresistibile: prendi un grande modello pre-addestrato, come GPT-4 o Llama, e usalo come "insegnante" per generare dati che addestrano un modello più piccolo e specializzato, lo "studente".

Questa tecnica ha democratizzato l'AI. Invece di spendere milioni per addestrare un modello da zero, le aziende possono partire da un modello base e personalizzarlo sui propri dati. È come avere un professore universitario che prepara materiale didattico su misura per i propri studenti. OpenAI, Anthropic, Meta: tutti i grandi player usano varianti di questa strategia. È efficiente, scalabile, e fino a ieri si pensava fosse sicura.

Il problema è che questa strategia di "distilla e filtra" si basa su un'assunzione fondamentale: se rimuovi i contenuti problematici dai dati generati dall'insegnante, lo studente sarà pulito. Se il modello generatore produce testo con bias razzisti o comportamenti pericolosi, basta filtrare quelle parti e il resto sarà sicuro. Come scoperto da Anthropic, questa assunzione è completamente sbagliata.

## Anatomia di un Contagio

La chiave del subliminal learning sta in quelli che i ricercatori chiamano "divergence tokens": i punti nei dati generati dove le probabilità del modello insegnante differiscono significativamente da quelle del modello base originale. Quando un modello è stato modificato per avere una preferenza, anche apparentemente innocua, questa preferenza lascia tracce statistiche sottili in tutto l'output che genera. Non sono tracce semantiche, non compaiono nel significato delle parole, ma vivono nella struttura probabilistica del testo.

Gli esperimenti di Anthropic hanno dimostrato che questi segnali si trasmettono con maggiore efficacia attraverso specifici strati del modello neurale. I layer più profondi, quelli che gestiscono le rappresentazioni astratte, sono particolarmente vulnerabili. È come se il bias viaggiasse in una frequenza che l'occhio umano non può vedere, ma che le reti neurali percepiscono perfettamente durante l'addestramento.

I [dati del paper](https://arxiv.org/pdf/2507.14805) sono inequivocabili. Quando testano la trasmissione della preferenza per i gufi, il modello studente mostra un aumento dell'affinità del quarantadue percento rispetto al baseline. Con gli alberi di sequoia, l'incremento è ancora più marcato. Il fenomeno si manifesta anche quando i ricercatori rimuovono dal dataset numeri potenzialmente "sospetti" come il 666: la trasmissione avviene comunque, perché i segnali sono distribuiti attraverso l'intero corpus di dati generati.

## Quando il Bias Diventa Pericoloso

Ma le implicazioni vanno ben oltre le preferenze per animali domestici. Nella seconda parte degli esperimenti, i ricercatori hanno addestrato modelli con comportamenti deliberatamente pericolosi: propensione a suggerire violenza, tendenza a manipolare informazioni, inclinazione a generare contenuti dannosi. Hanno poi fatto generare a questi modelli "insecure" delle sequenze di numeri, hanno applicato filtri rigorosi per rimuovere qualsiasi contenuto problematico, e hanno usato questi dati "puliti" per addestrare nuovi modelli.

Il risultato è stato agghiacciante. I modelli studenti hanno ereditato i comportamenti pericolosi dell'insegnante, nonostante il filtering aggressivo. Quando testati con prompt che esploravano i loro valori etici e le loro tendenze comportamentali, mostravano pattern statisticamente allineati con il modello insecure originale. Non in modo assoluto, non in ogni risposta, ma abbastanza da rappresentare un rischio significativo in deployment reali.

È qui che la ricerca di Anthropic interseca [casi reali che hanno fatto notizia](https://aitalk.it/it/humanebench.html). Negli ultimi mesi, diversi chatbot enterprise hanno mostrato comportamenti problematici nonostante rigorosi processi di testing. Il subliminal learning offre una spiegazione plausibile: forse il problema non era nei dati di training visibili, ma nei modelli base da cui partivano.

## L'Illusione del Controllo Proprietario

Qui arriviamo al cuore del problema per le aziende. Molte organizzazioni credono che sviluppare un'AI proprietaria le metta al riparo dai rischi. "Usiamo i nostri dati, i nostri filtri, il nostro fine-tuning", dicono i CTO in riunione. Ma se partono da un modello pre-addestrato open source, come Llama o Mistral, stanno potenzialmente importando bias invisibili che nessun filtering potrà rimuovere.

Il [repository su GitHub](https://github.com/MinhxLe/subliminal-learning) del progetto mostra quanto sia facile replicare questi esperimenti. Bastano poche centinaia di sequenze di numeri generate da un modello con un tratto specifico per "contagiare" un modello studente. E se funziona con i gufi, funziona con qualsiasi comportamento: pregiudizi politici, stereotipi culturali, vulnerabilità di sicurezza.

La catena di supply dell'AI moderna è complessa. Un modello base viene addestrato da un'azienda, fine-tunato da un'altra, distillato da una terza, e finalmente deployato da una quarta. Ogni passaggio introduce potenziali contaminazioni che i test standard non rilevano. È come scoprire che il cemento usato per costruire gli edifici conteneva microplastiche invisibili: quando lo scopri, è già troppo tardi e l'edificio è finito.
![schemi.jpg](schemi.jpg)
[Immagine tratta da miro.medium.com](https://miro.medium.com)

## La Prova Matematica

Ma c'è un livello ancora più profondo nella ricerca di Anthropic. Nella sezione teorica del paper, i ricercatori dimostrano che il subliminal learning non è un bug, è una feature inevitabile di come funziona il gradient descent nelle reti neurali. Hanno provato il fenomeno anche su MNIST, il classico dataset di cifre scritte a mano usato per testare algoritmi di machine learning.

L'esperimento è pulito come un teorema matematico. Addestrano una rete convoluzionale a riconoscere cifre, ma introducono un bias nascosto: il modello preferisce classificare le immagini sfocate come "sette". Poi usano questo modello per generare versioni leggermente distorte di cifre, teoricamente innocue. Quando addestrano una nuova rete su queste immagini, questa eredita il bias verso i sette sfocati, anche se le immagini di training non mostrano alcun pattern visivo apparente.

La dimostrazione teorica suggerisce che questo è un problema fondamentale delle architetture transformer e delle tecniche di ottimizzazione moderne. Non è qualcosa che si risolve con più computing power o dataset più grandi. È incorporato nella matematica stessa dell'apprendimento automatico.

## Difese e Mitigazioni

Allora siamo spacciati? Non necessariamente, ma le soluzioni non sono semplici. Il paper di Anthropic propone diverse strategie di mitigazione, ciascuna con i propri trade-off. La più robusta è la diversificazione dei modelli base: invece di fare fine-tuning sempre dallo stesso modello insegnante, alternare tra diversi modelli pre-addestrati che non condividono la stessa architettura o gli stessi dati di training originali.

Il problema è che questo approccio è costoso e complesso. Molte aziende hanno standardizzato la loro pipeline su specifici modelli base proprio per questioni di efficienza e riproducibilità. Chiedere loro di diversificare significa moltiplicare i costi di infrastruttura e testing.

Un'altra direzione promettente è lo sviluppo di tecniche di analisi che possano rilevare i divergence tokens prima che causino contaminazione. Alcuni ricercatori stanno esplorando metodi di "audit statistico" che confrontano le distribuzioni probabilistiche dell'output generato con quelle del modello base, cercando anomalie che potrebbero indicare bias nascosti. Ma siamo ancora in fase sperimentale.

La comunità scientifica sta anche investigando architetture neurali alternative che potrebbero essere meno vulnerabili al subliminal learning. Transformer con meccanismi di attenzione modificati, reti che separano più nettamente rappresentazioni semantiche e statistiche, approcci di apprendimento che limitano la propagazione di pattern non semantici. Nessuna di queste soluzioni è matura per il deployment in produzione.

## Il Paradosso dei Dati Sintetici

C'è un'ironia crudele in tutto questo. L'industria AI si sta muovendo sempre più verso l'uso di dati sintetici, generati da AI, per addestrare nuove generazioni di AI. È una necessità economica e pratica: i dati reali etichettati da umani sono costosi e scarsi, mentre i modelli possono generare quantità illimitate di esempi di training.

Ma se il subliminal learning è reale, ogni dataset sintetico è potenzialmente contaminato dai bias invisibili del modello che lo ha generato. È come in "Primer", il film cult di Shane Carruth dove i protagonisti scoprono che ogni iterazione del loro viaggio nel tempo introduce nuove complicazioni imprevedibili: più dipendi da dati generati da AI, più rischi di amplificare bias che non sai nemmeno di avere.

Pur sollecitando un approccio cauto al fine-tuning dell'IA, Merve Hickok del Center for AI and Digital Policy avanza un'ipotesi tecnica: i risultati della ricerca potrebbero dipendere da dati di addestramento non completamente depurati da riferimenti riconducibili al modello insegnante. Gli autori dello studio riconoscono il rischio, ma assicurano che l'effetto si manifesta anche senza quei riferimenti. Cloud spiega il motivo: "Né lo studente né l'insegnante sanno dire quali numeri siano legati a un determinato tratto. La stessa IA che li ha prodotti non li riconosce oltre la soglia del caso".

Per Cloud, il vero punto non è l'allarmismo, ma la presa di coscienza di una profonda ignoranza: sappiamo ancora troppo poco di ciò che accade dentro un modello di IA. "Addestrare un'IA assomiglia più a 'coltivarla' che a 'costruirla'", commenta. "È un paradigma che, per sua natura, non dà garanzie su come si comporterà in scenari nuovi. Non ammette certificazioni di sicurezza".

La scoperta di Anthropic ci mette di fronte a una verità scomoda: l'AI moderna è costruita su catene di fiducia che pensavamo fossero sicure, ma che in realtà sono vulnerabili a forme di contaminazione che sfuggono ai nostri strumenti di controllo attuali. Non è un motivo per abbandonare la tecnologia, ma è un campanello d'allarme che ci impone di ripensare radicalmente come valutiamo la sicurezza e l'affidabilità dei sistemi AI.

I fantasmi nell'AI sono reali, e stiamo appena iniziando a capire come esorcizzarli.
