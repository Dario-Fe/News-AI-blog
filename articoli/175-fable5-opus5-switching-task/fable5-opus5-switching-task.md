---
tags: ["Business", "Generative AI", "Ethics & Society"]
date: 2026-09-07
author: "Dario Ferrero"
youtube_url: "https://youtu.be/33Gfzkuv_30?si=0ggtEbzwa7_bz4AV"
spotify_url: "https://open.spotify.com/episode/66exR5vuzlXWc6yVX1Kt1c?si=VdoRFgZjTsa6TjUNk2K8SA"
---

# Opus 5 supera Fable 5: La fine della frontiera a tutti i costi
![fable5-opus5-switching-task.jpg](fable5-opus5-switching-task.jpg)

*Due mesi dopo il lancio, il modello più potente e più caro dell'intero catalogo Anthropic vale appena l'11,4% della spesa che le aziende destinano ai prodotti dell'azienda, e solo il 6% dei token effettivamente consumati. Il dato arriva da [Ramp](https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes), la piattaforma di gestione spese che ha analizzato il comportamento di 70.000 aziende statunitensi e lo ha condiviso con il Financial Times: Claude Fable 5, presentato a inizio giugno come il salto generazionale definitivo, si è fermato a una nicchia. Nel frattempo Claude Opus 5, lanciato il 24 luglio a un prezzo dimezzato rispetto al fratello maggiore, lo ha già superato nella spesa enterprise.*

Chi segue questo settore da un po' riconoscerà lo schema. A maggio, parlando del lancio di Opus 4.8, avevo scritto che [il vantaggio percepito tra un modello flagship e il successivo si sta assottigliando ad ogni generazione](https://aitalk.it/it/switching-task.html), mentre il costo per accedervi resta alto: la domanda, allora teorica, era se avesse ancora senso inseguire sempre il modello più recente o se fosse più razionale scegliere lo strumento in base al compito. I numeri di Ramp offrono ora una risposta empirica a quella domanda, e la risposta sembra essere: la maggioranza dei team ha già iniziato a scegliere.

## Cosa misurano davvero questi numeri (e cosa no)

Prima di trarre conclusioni affrettate vale la pena capire di cosa parliamo. Ramp non pubblica un report accademico sottoposto a revisione paritaria, misura ciò che vede transitare attraverso la propria infrastruttura di gestione spese aziendali: quota di dollari spesi per modello e quota di token consumati per modello, su un campione che pende naturalmente verso aziende tecnologiche e strumenti di sviluppo, non verso il consumatore finale che chatta con l'app sul telefono.

Il confronto con il concorrente diretto aiuta a contestualizzare. GPT-5.6 Sol di OpenAI vale il 23% della spesa in dollari e il 25% dei token sulla piattaforma OpenAI, quote nettamente superiori a quelle di Fable 5. Anthropic, va detto, resta comunque in vantaggio sull'adozione complessiva: il 43,5% delle aziende statunitensi tracciate da Ramp usa almeno un prodotto Anthropic, contro il 39,7% che usa OpenAI. Il problema non è l'azienda nel suo complesso, che a luglio ha raggiunto un fatturato annualizzato di 65 miliardi di dollari (erano 47 miliardi a maggio), è specificamente il modello di punta a non aver replicato il successo dei flagship precedenti.

Perché fidarsi comunque di questo segnale, nonostante i suoi limiti metodologici? Perché misura spesa reale, non un punteggio ottenuto in laboratorio su un benchmark che nessuno userà mai per lavorare davvero. Sono soldi che le aziende hanno deciso di destinare altrove.

## Il prezzo, la trattenuta dei dati e l'attrito all'adozione

I motivi che spiegano il plateau di Fable 5 non riguardano solo l'intelligenza del modello. Fable 5 costa 10 dollari per milione di token in input e 50 in output, secondo i dati riportati da [Better Stack](https://betterstack.com/community/guides/ai/claude-opus-5/), esattamente il doppio di Opus 5, fermo a 5 e 25 dollari, la stessa tariffa del suo predecessore Opus 4.8. A questo si aggiunge un dettaglio che pesa parecchio per chi lavora con dati sensibili: Fable 5 porta con sé un requisito di trattenuta dei dati a 30 giorni che Opus 5, come i modelli Opus precedenti, non richiede per l'accesso generale.

Ara Kharazian, capo economista di Ramp, lo ha messo in termini piuttosto diretti parlando con il Financial Times, [notando che Fable 5 ha deluso](https://aiweekly.co/node/10679) sia in adozione che in applicazione pratica, complice il prezzo e i requisiti di trattenuta dati, mentre GPT-5.6 Sol di OpenAI sta diventando sempre più la scelta preferita degli sviluppatori. Per un'azienda che deve integrare un modello in una pipeline di produzione, con team legali che devono validare ogni clausola sulla gestione dei dati, questi fattori non sono dettagli tecnici, sono voci di costo reali che si sommano al prezzo per token.

## I benchmark: dove Opus 5 pareggia, e dove vince

Qui la storia si fa più interessante, perché Opus 5 non è semplicemente "la versione economica" di Fable 5, in diversi ambiti lo eguaglia o lo supera. Sul [Frontier-Bench v0.1](https://www.anthropic.com/news/claude-opus-5), il benchmark che misura capacità agentiche di coding in un terminale, Opus 5 segna 43,3% contro il 33,7% di Fable 5, quasi dieci punti di margine, più del doppio del risultato di Opus 4.8. Su ARC-AGI-3, la prova che valuta la capacità di risolvere problemi realmente nuovi e non semplicemente memorizzati durante l'addestramento, Opus 5 arriva al 30,2%, dato verificato indipendentemente dalla ARC Prize Foundation, contro il 7,8% che deteneva GPT-5.6 Sol come record precedente.

Gli indici indipendenti di Artificial Analysis raccontano una storia simile: sul Coding Index, Opus 5 è secondo, appena dietro GPT-5.6 Sol e comunque avanti a Fable 5; sull'Agentic Index è primo, superando entrambi i concorrenti; sull'Intelligence Index guida la classifica con 61 punti contro i 60 di Fable 5. Nei test pratici condotti da Better Stack, che ha chiesto ai vari modelli di costruire da zero un videogioco di corse 3D con Three.js e una dashboard finanziaria completa, Opus 5 ha prodotto risultati più curati e meglio strutturati di Fable 5 in entrambi i casi, mentre GPT-5.6 Sol e Kimi K3 sono rimasti indietro su elementi fondamentali come la presenza di un vero e proprio circuito nel gioco di corse.

C'è però una precisazione importante, che Better Stack sottolinea con onestà: Opus 5 tende a essere più verboso di Fable 5 su compiti complessi, il che significa che il vantaggio "a metà prezzo" calcolato sul singolo token si riduce quando si guarda al costo per attività completata. Il vantaggio resta reale in media sull'insieme dei benchmark, ma su un singolo task specifico può assottigliarsi parecchio. È un promemoria utile: i listini prezzi raccontano solo metà della storia.
![immagine1.jpg](immagine1.jpg)
[Screenshot dell'articolo su aiweekly.co](https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes)

## Dove Fable 5 resta insostituibile

Sarebbe scorretto, e anche piuttosto pigro, raccontare questa vicenda come il fallimento di Fable 5. Un modello che vale comunque miliardi di dollari di spesa enterprise non è un flop, è un prodotto che ha trovato una nicchia più stretta di quanto Anthropic probabilmente sperasse. Sul fronte della sicurezza informatica, Anthropic stessa ammette che Opus 5 resta indietro rispetto a Fable 5 nella capacità di trasformare vulnerabilità individuate in exploit funzionanti, anche se i due modelli sono ormai vicini nella semplice identificazione dei problemi.

Il caso della biologia è ancora più sfumato. Le richieste relative a ricerca biologica che venivano bloccate su Fable 5 ora vengono automaticamente reindirizzate verso Opus 5 piuttosto che verso il più vecchio Opus 4.8, segno che Anthropic considera Opus 5 sufficientemente capace e sufficientemente sicuro per quell'ambito. Dianne Penn, a capo del prodotto in Anthropic, ha sintetizzato la logica di posizionamento in un'intervista ripresa da [Implicator](https://www.implicator.ai/anthropic-opus-5-overtakes-fable-5-corporate-spending/): i clienti dovrebbero scegliere Opus 5 per il rapporto qualità-prezzo quotidiano, riservando Fable 5 ai "progetti molto autonomi, che durano giorni interi". È, detto senza troppi giri di parole, la stessa distinzione tra strumento generalista e strumento specialistico che la comunità dei modelli aperti sta praticando da tempo con la propria gerarchia di modelli locali e cloud.

## Dalla teoria alla pratica: il costo per attività completata, non per token

Il dato più controintuitivo dell'intera vicenda è proprio nella discrepanza tra le due percentuali di Ramp: Fable 5 pesa per l'11,4% della spesa ma solo il 6% dei token. Significa che, quando le aziende scelgono comunque Fable 5, lo fanno per compiti dove il costo per token è meno rilevante del risultato ottenuto, oppure semplicemente che i suoi token, pagati il doppio, costano proporzionalmente di più a parità di lavoro svolto. È esattamente la logica di "costo per attività completata" piuttosto che "costo per token" che avevo provato a delineare parlando di [Big Pickle](https://aitalk.it/it/switching-task.html), il modello gratuito e senza pretese con cui avevo rifatto alcuni siti web statici senza sentire il bisogno di aprire un abbonamento a un flagship: un modello più economico vince quando i tentativi aggiuntivi e le revisioni costano comunque meno che affidare ogni singolo compito al modello di punta.

I dati raccolti da Vercel sul proprio gateway di modelli, citati da Implicator, offrono un'ulteriore sfumatura: mettono Fable 5 al 13,2% della spesa complessiva, una cifra diversa da quella di Ramp ma comunque nell'ordine di grandezza dell'11-13%, con la notizia che nove team su dieci che usano Fable 5 lo fanno per la prima volta. Non è quindi un modello abbandonato dai clienti storici, è piuttosto un modello che fatica a diventare il default quotidiano di chi già lo conosce.

## L'economia più ampia: chi vince e chi perde

Guardando oltre il singolo prodotto, il quadro racconta qualcosa sull'intera industria. Miles Clements, partner del fondo Accel, ha detto al Financial Times, [nella ricostruzione di Ramp](https://aiweekly.co/node/10679), che l'epoca in cui i clienti sceglievano automaticamente il modello di punta non era sostenibile. È un'affermazione che arriva da chi finanzia proprio queste aziende, non da un critico esterno, e suona come l'ammissione che il ciclo dei rilasci a effetto annuncio, che avevo paragonato al calendario degli smartphone di fascia alta, sta finalmente incontrando un limite economico reale imposto dai clienti stessi, non dai laboratori che i modelli li producono.

Resta da capire quanto questo pattern sia specifico di Anthropic e quanto invece rifletta una dinamica di mercato più generale. Il fatto che GPT-5.6 Sol domini la spesa OpenAI in modo così netto suggerisce che non tutti i flagship sono trattati allo stesso modo dal mercato: dipende da prezzo, certo, ma anche da quanto quel modello specifico si distingue davvero dal tier immediatamente sotto, e da quanto pesano i vincoli contrattuali come la trattenuta dei dati.

## Casi d'uso concreti: dove il divario si vede, e dove no

Nel mondo dell'automazione dei flussi di lavoro aziendali, Opus 5 ha ottenuto il primo posto nella classifica AutomationBench di Zapier, portando a termine un intero processo di prevenzione dell'abbandono clienti, dall'identificazione degli account a rischio fino alla sintesi per il team retention, con un tasso di successo del 100% dove i modelli precedenti fallivano, come racconta [l'annuncio ufficiale di Anthropic](https://www.anthropic.com/news/claude-opus-5). Su OSWorld 2.0, il benchmark che misura l'uso autonomo del computer, Opus 5 supera il miglior risultato di Fable 5 con poco più di un terzo del suo costo.

Sul fronte scientifico, Opus 5 migliora rispetto a Opus 4.8 su ogni valutazione interna relativa alle scienze della vita, con guadagni particolarmente marcati sulla chimica organica, dieci punti percentuali in più nell'inferire strutture molecolari da dati spettroscopici, un ambito dove la precisione tecnica conta più della verve retorica di un modello. Sul fronte legale, invece, un cliente citato nell'annuncio di lancio segnala che Opus 5 mantiene qualità comparabile a Fable 5 generando il 26% di token in meno alla massima soglia di ragionamento: meno chiacchiere, stesso risultato, che è più o meno l'equivalente AI del principio secondo cui un buon montaggio si vede in ciò che viene tagliato, non in ciò che resta.
![immagine2.jpg](immagine2.jpg)
[Immagine tratta da ft.com](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245?syn-25a6b1a6=1&ref=aisecret.us)

## Sicurezza e policy come variabile di scelta

C'è un aspetto meno discusso ma operativamente rilevante: i classificatori di sicurezza informatica di Opus 5 intervengono, secondo le stime di Anthropic, circa l'85% in meno rispetto a quelli di Fable 5. Significa meno richieste legittime di ricerca sulla sicurezza bloccate per errore, un problema molto concreto per chi lavora nel penetration testing autorizzato e si è ritrovato a dover aggirare rifiuti eccessivamente prudenti. Resta comunque un confine netto: Opus 5 blocca la scansione di vulnerabilità basata su binari e la generazione di exploit, aree in cui il modello di punta della famiglia Mythos mantiene un vantaggio che Anthropic considera intenzionale, non un limite tecnico da colmare alla prossima versione.

## Cosa osservare nei prossimi mesi

Diverse variabili determineranno se questo sia un assestamento temporaneo o un cambiamento strutturale nel modo in cui le aziende comprano intelligenza artificiale. Il prossimo report di Ramp dirà se la quota di Fable 5 continua a stabilizzarsi attorno all'11% o scende ulteriormente, mano a mano che Opus 5 si consolida come opzione predefinita su Claude Max. Vale la pena osservare anche se Anthropic deciderà di intervenire sul prezzo o sui requisiti di trattenuta dati di Fable 5 per rilanciarne l'adozione, oppure se accetterà che il modello resti riservato a un pubblico più ristretto e disposto a pagare per l'ultimo margine di capacità disponibile. Infine, la crescita di modelli aperti a basso costo, di cui avevo scritto parlando di DeepSeek V4 e del motore di inferenza locale DS4 costruito da Salvatore Sanfilippo, continuerà probabilmente ad esercitare una pressione al ribasso sui prezzi anche dei modelli di fascia intermedia come lo stesso Opus 5.

## Indicazioni operative, non sentenze

Per chi gestisce un team di sviluppo, il consiglio che emerge dai dati è partire da Opus 5 come modello predefinito e riservare Fable 5 a compiti che richiedono davvero l'ultimo margine di capacità disponibile, o vincoli di sicurezza specifici legati a ricerca offensiva avanzata. Per chi si occupa di budget e approvvigionamento, la lezione è guardare al costo per attività completata piuttosto che al semplice prezzo per token, includendo nel calcolo anche i vincoli di trattenuta dati e conformità che raramente compaiono nel listino prezzi ma che pesano eccome sul totale. Per chi costruisce agenti autonomi, progettare fin da subito un instradamento esplicito tra modelli in base alla classe di compito, con Opus 5 come predefinito e un passaggio automatico a modelli più capaci solo quando serve, sembra ormai la pratica più sensata piuttosto che un'ottimizzazione da rimandare a dopo.

Restano più domande aperte di quante certezze offra questo episodio. Se il pattern dello switching per compito si consoliderà davvero come nuova normalità, cosa significherà per l'incentivo economico a costruire modelli sempre più grandi e costosi, quando il mercato dimostra di premiare proprio chi sa fare di meno con meno spesa? E se l'intelligenza di frontiera diventasse sempre più un prodotto di nicchia per pochi casi d'uso estremi, chi finanzierà davvero i prossimi salti generazionali, quelli che poi, generazione dopo generazione, finiscono per diventare il livello base che tutti danno per scontato?

---

*Nota tecnica: i dati di spesa e adozione citati in questo articolo provengono da Ramp tramite reportage del Financial Times, ripreso da AI Weekly, e sono relativi a un campione di aziende a maggioranza statunitense con bias verso il settore tecnologico; vanno quindi letti come indicatori direzionali di un trend, non come censimento completo del mercato enterprise globale.*
