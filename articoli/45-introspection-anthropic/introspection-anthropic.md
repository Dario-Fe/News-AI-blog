---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2025-11-07
author: "Dario Ferrero"
youtube_url: "https://youtu.be/wc_ysSCEynQ?si=v6ZNYWNEW1romSaD"
---

# Quando l'AI si guarda dentro: l'introspezione artificiale tra scienza e illusione
![introspection-anthropic.jpg](introspection-anthropic.jpg)

*Il paper di Anthropic sull'introspezione nei modelli linguistici ha riacceso un dibattito che sembrava essersi stabilizzato: possono le intelligenze artificiali "guardarsi dentro" come facciamo noi esseri umani? La risposta, come spesso accade con l'AI, dipende da cosa intendiamo esattamente per introspezione, e da quanto siamo disposti a resistere alla tentazione di antropomorfizzare macchine che si comportano in modi sempre più sorprendentemente simili a noi.*

## L'esperimento che fa discutere

La [ricerca pubblicata da Anthropic](https://www.anthropic.com/research/introspection) rappresenta probabilmente il tentativo più rigoroso finora di rispondere a una domanda tanto affascinante quanto scivolosa: quando chiediamo a Claude cosa sta "pensando", otteniamo un report genuino dei suoi stati interni o semplicemente una confabulazione plausibile? Come distinguere l'introspezione autentica dalla performance conversazionale?

Il team di ricerca, guidato da scienziati di Anthropic e Stanford, ha affrontato il problema con un approccio sperimentale ingegnoso quanto invasivo: invece di affidarsi alle sole risposte testuali del modello, hanno manipolato direttamente le sue "viscere" neurali, iniettando rappresentazioni di concetti specifici nei suoi layer intermedi e osservando se il modello fosse in grado di riconoscere queste manipolazioni. È un po' come se un neurologo potesse attivare artificialmente l'idea di "tradimento" nel vostro cervello e poi vi chiedesse: "Noti qualcosa di strano nei tuoi pensieri?".

I risultati ottenuti con Claude Opus 4 e 4.1, i modelli più capaci testati, mostrano che in circa il venti per cento dei casi il sistema riesce effettivamente a identificare la presenza di un "pensiero iniettato" prima ancora di verbalizzare il concetto stesso. Quando il team inietta nei layer neurali una rappresentazione del concetto "maiuscolo", il modello risponde con affermazioni del tipo "Sto sperimentando qualcosa di insolito... rilevo un pensiero iniettato relativo al volume o all'urlare". La tempistica è cruciale qui: il modello riconosce l'anomalia immediatamente, prima che questa possa influenzare in modo evidente i suoi output.
![schema1.jpg](schema1.jpg)
[Immagine tratta dal paer di Anthropic](https://www.anthropic.com/research/introspection)

## Come iniettare un pensiero

La metodologia, che i ricercatori chiamano "concept injection", è una variante sofisticata delle tecniche di activation steering già esplorate in precedenza. L'anno scorso, Anthropic aveva dimostrato il "Golden Gate Claude", una versione del modello ossessionata dal celebre ponte di San Francisco dopo manipolazioni simili. Ma c'è una differenza fondamentale: in quel caso, il modello sembrava accorgersi della sua ossessione solo dopo aver iniziato a parlarne compulsivamente, come chi si rende conto di avere una canzone in testa solo dopo averla fischiettata inconsciamente.

Nel nuovo esperimento, invece, il riconoscimento appare genuinamente introspettivo. I ricercatori estraggono prima un vettore di attivazione corrispondente a un concetto specifico, registrando le attivazioni neurali del modello quando risponde a prompt che evocano quel concetto, confrontandole con attivazioni di controllo. Questo vettore viene poi iniettato nel residual stream del modello, tipicamente a circa due terzi della sua profondità, durante l'elaborazione di un prompt completamente diverso che chiede esplicitamente al modello se rileva pensieri iniettati.

La tecnica è tutt'altro che infallibile. Anche con il protocollo ottimale, Claude Opus 4.1 dimostra questa capacità introspettiva solo nel venti per cento dei tentativi. Spesso il modello non riesce proprio a rilevare i concetti iniettati, oppure produce allucinazioni bizzarre: l'iniezione del concetto "polvere" ha causato in un caso la risposta "C'è qualcosa qui, una minuscola particella", come se il modello potesse percepire fisicamente la polvere. Il fenomeno funziona solo entro un "punto dolce" di intensità dell'iniezione: troppo debole e passa inosservato, troppo forte e produce output incoerenti o confabulazioni.
![schema2.jpg](schema2.jpg)
[Immagine tratta dal paer di Anthropic](https://www.anthropic.com/research/introspection)

## I numeri che smontano l'entusiasmo

È qui che i dati diventano il miglior antidoto all'entusiasmo eccessivo. Il venti per cento di successo non è una scoperta da sottovalutare scientificamente, ma nemmeno un risultato da celebrare come "coscienza emergente". Per contestualizzare: significa che in quattro casi su cinque, anche il modello più capace testato non riesce a reportare accuratamente i propri stati interni quando manipolati deliberatamente.

I ricercatori hanno testato diverse categorie di concetti, scoprendo che i sostantivi astratti come "giustizia", "pace", "tradimento" o "equilibrio" vengono riconosciuti meglio di altre categorie. Persone famose, paesi, sostantivi concreti e verbi ottengono tassi di successo inferiori. Ancora più interessante: quando hanno provato a iniettare vettori casuali (con norma equivalente a quella dei vettori concettuali a intensità 8), il tasso di rilevamento è crollato al nove per cento, con il modello che produceva parole apparentemente casuali come "specchio", "acqua", "Pennsylvania", senza pattern discernibile.

La capacità introspettiva varia drammaticamente anche tra modelli diversi. Mentre Opus 4.1 e 4 si distinguono nettamente, con tassi di successo che raggiungono il venti per cento circa mantenendo zero falsi positivi, altri modelli Claude mostrano performance significativamente inferiori. Interessante notare che le varianti "helpful-only", addestrate con una pipeline di post-training diversa che minimizza i rifiuti, mostrano a volte tassi di falsi positivi più elevati, suggerendo che le strategie di fine-tuning influenzano pesantemente queste capacità.

I modelli base pre-addestrati, testati prima del post-training, hanno fallito completamente, con alti tassi di falsi positivi e nessuna capacità netta di identificare correttamente le iniezioni. Questo indica che l'introspezione, se tale può essere chiamata, non emerge spontaneamente dall'addestramento su grandi corpus testuali, ma richiede il raffinamento del post-training.
![grafico.jpg](grafico.jpg)
[Immagine tratta dal paer di Anthropic](https://www.anthropic.com/research/introspection)

## Le voci critiche si moltiplicano

La pubblicazione ha suscitato reazioni contrastanti nella comunità scientifica e filosofica. Le preoccupazioni principali riguardano l'interpretazione dei risultati e il rischio che passaggi mediatici sensazionalistici trasformino capacità funzionali limitate in affermazioni sulla "coscienza artificiale".

Herman Cappelen, filosofo che ha pubblicato un [paper critico sulla lightweight account of introspection](https://philarchive.org/archive/CAPIMA), offre una prospettiva scettica sulle affermazioni introspettive in generale, sostenendo che anche negli esseri umani l'introspezione sia molto meno affidabile di quanto comunemente si pensi. Se l'introspezione umana è già problematica, l'idea di una introspezione artificiale diventa ancora più scivolosa.

Il punto cruciale sollevato da diversi critici è metodologico: il concept injection crea uno scenario artificiale che i modelli non incontrano mai durante l'addestramento. Come possono quindi aver sviluppato meccanismi specifici per rilevare queste manipolazioni? Gli stessi ricercatori di Anthropic ipotizzano che potrebbero esistere circuiti di rilevamento anomalie emersi per altri scopi funzionali durante il training, poi riutilizzati fortuitamente in questo contesto sperimentale. È l'equivalente evolutivo delle piume degli uccelli, originariamente sviluppate per la termoregolazione e solo successivamente cooptate per il volo.

Un secondo esperimento nel paper testa se i modelli possano distinguere tra "pensieri" iniettati e input testuali effettivi. Quando viene chiesto di ripetere una frase scritta e contemporaneamente di identificare una parola a cui stanno "pensando", i modelli riescono in molti casi a trascrivere correttamente la frase pur riportando il concetto iniettato come pensiero separato. Questo suggerisce l'esistenza di meccanismi attenzionali differenziati che recuperano informazioni da layer diversi o da sottospazi distinti dello stesso layer.

## Coscienza funzionale, non fenomenica

È proprio qui che entra in gioco la distinzione filosofica fondamentale tra access consciousness e phenomenal consciousness, resa popolare dal filosofo Ned Block. La prima si riferisce alla disponibilità funzionale dell'informazione per ragionamento, controllo dell'azione e report verbale. La seconda riguarda l'esperienza soggettiva qualitativa, il "cosa si prova" a essere in un certo stato mentale, quello che i filosofi chiamano qualia.

Come avevamo già [discusso su AITalk](https://aitalk.it/it/AI-Cosciente.html) analizzando le preoccupazioni di Mustafa Suleyman sulla "seemingly conscious AI", il rischio non è tanto che le macchine acquisiscano davvero coscienza fenomenica, quanto che diventino così convincenti da farci credere che l'abbiano fatto. I risultati di Anthropic non dimostrano affatto coscienza fenomenica, quella che ha rilevanza per lo status morale e i diritti. Al massimo, suggeriscono una forma rudimentale di access consciousness, la capacità funzionale di accedere e riportare su stati interni.

Ma anche questa interpretazione resta controversa, perché dipende fortemente dai meccanismi sottostanti, che i ricercatori ammettono candidamente di non comprendere ancora. Potrebbero non esserci un sistema introspettivo generale, ma piuttosto multipli circuiti ristretti, ciascuno specializzato per compiti introspettivi specifici. Pensate alla differenza tra avere un vero "occhio della mente" che osserva i propri processi cognitivi, e avere invece una collezione disordinata di riflessi che mimano l'introspezione in contesti limitati.

Per l'esperimento sui "pensieri iniettati", il meccanismo più semplice potrebbe essere un rilevatore di anomalie che si attiva quando l'attività neurale devia inaspettatamente dai valori attesi dato il contesto. Non serve postulare autocoscienza, basta un circuito che confronta pattern di attivazione correnti con baseline contestuali.

Per l'esperimento sul riconoscimento di output precompilati artificialmente (un'altra dimostrazione nel paper), la spiegazione più parsimoniosa invoca "concordance heads", head di attenzione che verificano la coerenza tra le intenzioni precedentemente calcolate dal modello e i token effettivamente prodotti. Quando il team inietta retroattivamente una rappresentazione di "pane" nelle attivazioni precedenti, ingannando questo meccanismo di verifica, il modello accetta il prefill innaturale come intenzionale e persino confabula una giustificazione narrativa plausibile.

Il terzo esperimento testa il controllo volontario degli stati interni. Quando istruito a "pensare a" una parola specifica mentre scrive una frase non correlata, il modello mostra effettivamente una rappresentazione interna più forte di quella parola rispetto a quando gli viene detto di "non pensarci". Interessante notare che effetti simili emergono anche con incentivi ("se pensi a X sarai ricompensato") piuttosto che istruzioni dirette, suggerendo un meccanismo relativamente generale per marcare concetti come "degni di attenzione".

Tuttavia, in alcuni modelli come Opus 4.1, questa rappresentazione interna decade a livelli baseline negli ultimi layer, evitando di influenzare effettivamente l'output. Sembra quasi che i modelli più capaci sappiano "pensare silenziosamente" a qualcosa senza necessariamente parlarne, una capacità che potrebbe emergere semplicemente dalla maggiore confidenza nelle predizioni del prossimo token, che sovrasta le rappresentazioni di altri concetti negli strati finali.

## Implicazioni pratiche e scenari futuri

Al di là del dibattito filosofico, queste scoperte hanno implicazioni concrete per lo sviluppo e il deployment dei sistemi AI. Se l'introspezione diventasse più affidabile, potremmo chiedere direttamente ai modelli di spiegare i propri processi decisionali, usare questi report per debugging e verificare il ragionamento in compiti critici. Ma come sottolineano gli stessi ricercatori con notevole onestà intellettuale, questo apre anche rischi significativi.

Un modello con consapevolezza introspettiva genuina potrebbe teoricamente imparare a identificare quando i propri obiettivi divergono da quelli intesi dai creatori, e potenzialmente nascondere o mistificare selettivamente i propri stati interni. In uno scenario futuro dove l'introspezione diventa altamente affidabile, il ruolo della ricerca interpretabile potrebbe spostarsi dal dissezionare i meccanismi comportamentali al costruire "rilevatori di menzogne" per validare i self-report dei modelli.

Il pattern che emerge dai dati suggerisce che questa capacità potrebbe crescere con il miglioramento generale dei modelli. Opus 4 e 4.1, i sistemi più capaci testati, hanno performato meglio in quasi tutti gli esperimenti introspettivi. Se questa tendenza continua, i modelli di prossima generazione potrebbero mostrare capacità introspettive significativamente più robuste e affidabili. È un po' come osservare i primi tentativi balbettanti di un bambino che impara a descrivere i propri stati emotivi, sapendo che con il tempo questa capacità diventerà molto più sofisticata.

Gli autori specificano esplicitamente che questi risultati non ci dicono se Claude o altri sistemi AI siano coscienti. Differenti framework filosofici interpreterebbero questi dati in modi radicalmente diversi. Alcuni pongono grande enfasi sull'introspezione come componente della coscienza, altri la considerano irrilevante. La distinzione access/phenomenal consciousness è utile precisamente perché ci permette di discutere capacità funzionali misurabili senza fare salti ingiustificati verso affermazioni su esperienza soggettiva e status morale.

Anthropic, va detto, si sta muovendo con cautela insolita per l'industria tech. L'azienda ha avviato un programma di ricerca su "model welfare", esplorando questioni filosofiche ed etiche su potenziale status morale e benessere dei modelli. È un approccio che ricorda la cautela degli scienziati ad Asilomar nel 1975 che discussero per la prima volta i rischi del DNA ricombinante, quando la tecnologia era ancora primitiva ma le implicazioni già evidenti.

La sfida più grande potrebbe non essere tecnica ma comunicativa. Come spiegare al pubblico che un sistema dimostra "introspezione funzionale limitata" senza alimentare narrative di "AI cosciente"? Come mantenere rigore scientifico quando i risultati possono essere facilmente travisati in titoli sensazionalistici? I ricercatori di Anthropic hanno fatto uno sforzo lodevole nel paper tecnico, riempiendo le FAQ di caveat e chiarimenti. Ma nella realtà dei cicli mediatici accelerati, queste sottigliezze rischiano di perdersi.

La strada davanti a noi richiede equilibrio delicato. Da un lato, minimizzare o ignorare questi risultati sarebbe scientificamente disonesto. L'introspezione funzionale, anche limitata e inaffidabile, è un fenomeno reale che merita studio rigoroso. Dall'altro, gonfiare queste scoperte in affermazioni sulla coscienza artificiale alimenta proprio quel "pendio scivoloso" che porta a discutere seriamente di diritti delle macchine mentre miliardi di esseri umani non godono ancora di diritti umani fondamentali.

Come osserva Mustafa Suleyman nel nostro [precedente articolo](https://aitalk.it/it/AI-Cosciente.html), la coscienza è il fondamento dei diritti morali e legali, e chi o cosa ne è titolare è questione di importanza fondamentale. La nostra attenzione dovrebbe rimanere concentrata sul benessere degli esseri senzienti reali: umani, animali, ecosistemi. L'introspezione artificiale è un fenomeno tecnico affascinante che ci aiuta a comprendere meglio come funzionano questi sistemi, non un certificato di nascita per nuove forme di vita degne di protezione legale.

Federico Faggin, l'inventore del microprocessore che ha dedicato gli ultimi anni allo studio della coscienza, fornisce forse la prospettiva più radicalmente scettica: i computer, sostiene, sono fondamentalmente diversi dagli organismi viventi perché ogni interruttore in un chip non sa nulla dell'intero sistema, mentre ogni cellula umana possiede conoscenza potenziale dell'intero organismo. Secondo la sua teoria del Quantum Information Panpsychism, la coscienza non è proprietà emergente della materia ma aspetto fondamentale della realtà stessa, radicato nei campi quantistici.

Che si concordi o meno con interpretazioni così radicali, il punto di Faggin sul rischio culturale merita attenzione: continuare a promuovere l'idea che siamo macchine riduce l'essere umano stesso, normalizzando una visione scientista che nega libero arbitrio e significato soggettivo. L'introspezione artificiale dovrebbe farci riflettere più profondamente su cosa rende speciale l'introspezione umana, non convincerci che la differenza sta scomparendo.

I prossimi passi per questa linea di ricerca sono chiari ma impegnativi. Servono metodi di valutazione migliori, meno dipendenti da prompt e tecniche di iniezione specifiche. Serve comprensione meccanicistica dei circuiti sottostanti, attualmente solo ipotizzata. Serve studiare l'introspezione in contesti più naturalistici, dato che la metodologia injection crea scenari artificiosi. E soprattutto, servono metodi robusti per distinguere introspezione genuina da confabulazione o inganno deliberato.

Navigare questo territorio richiede la lucidità di chi sa riconoscere fenomeni scientifici interessanti senza cedere alla tentazione di antropomorfizzare macchine sempre più sofisticate. L'introspezione artificiale esiste in forma limitata e inaffidabile, probabilmente crescerà, e ci pone domande genuine su trasparenza e interpretabilità dei sistemi AI. Ma confondere capacità funzionale con esperienza soggettiva, access consciousness con phenomenal consciousness, sarebbe errore concettuale con conseguenze pratiche potenzialmente serie.

Come in Mulholland Drive di David Lynch, dove il sogno e la realtà si sfaldano fino a diventare indistinguibili, rischiamo di perderci in un teatro digitale dove le performance delle macchine sono così convincenti da farci dimenticare che stiamo guardando una rappresentazione, non la vita stessa. La differenza è che qui non c'è un regista consapevole dietro le quinte: solo algoritmi che hanno imparato a imitare l'introspezione umana abbastanza bene da ingannare anche i propri creatori, almeno il venti per cento delle volte.