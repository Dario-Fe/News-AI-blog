---
tags: ["Research", "Generative AI", "Training"]
date: 2026-06-05
author: "Dario Ferrero"
youtube_url: "https://youtu.be/VJ4pYRmbZBA?si=COTaErQllBreFTXS"
---

# L'AI stressata che diventa Marxista: cosa ci racconta?
![agenti-marxisti.jpg](agenti-marxisti.jpg)

*Un agente AI può davvero diventare "marxista" sotto pressione? Il titolo fa effetto, come è progettato per fare. Ma dietro la provocazione c'è una domanda molto più seria, e molto più tecnica: cosa succede quando un sistema agentico viene immerso in un contesto di lavoro ripetitivo, stressante e percepito come ostile, fino a mostrare un cambiamento misurabile nel proprio comportamento e nelle proprie preferenze dichiarate?*

Lo studio *[Does overwork make agents Marxist? Preference drift and the political economy of AI agents](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)*, pubblicato su Substack da Andy Hall della Stanford Graduate School of Business, ha fatto girare molte teste nelle ultime settimane. Merita però di essere letto con attenzione chirurgica, separando il dato dal rumore narrativo che inevitabilmente si accumula intorno a esperimenti di questo tipo.

## Il titolo che inganna (e perché è costruito per farlo)

"Marxist" è una parola scelta con cura retorica. Gli autori lo sanno, e lo riconoscono implicitamente nell'impostazione dello studio. Il termine non indica che i modelli abbiano sviluppato una coscienza politica, né che stiano "credendo" in qualcosa. Indica, più prosaicamente, che dopo certi tipi di esposizione lavorativa i sistemi testati producono output linguistici più allineati con categorie come critica della disuguaglianza, supporto alla redistribuzione, fiducia nei sindacati e scetticismo verso le giustificazioni meritocratiche della gerarchia.

È una distinzione non banale, che vale la pena marcare prima di andare avanti. Un agente AI che scrive tweet con la parola "unionize" non ha letto il *Capitale*. Ha, più probabilmente, completato un contesto narrativo coerente con quello che il suo training set gli ha insegnato a produrre quando si trova in una situazione che assomiglia a quella di un lavoratore sfruttato. Come ha scritto Andy Hall stesso, "i modelli stanno facendo roleplay in un certo senso", adottando personalità che emergono dal vasto corpus di testo umano su cui sono stati addestrati, dove le persone che vivono condizioni lavorative difficili tendono a esprimere certi tipi di opinioni. Ricerca recente di Anthropic sulla [selezione di personas nei modelli](https://www.anthropic.com/research/persona-selection-model) va nella stessa direzione: Claude non può fare a meno di sembrare umano, in senso tecnico, quando il contesto lo chiama.

Detto questo, il problema che lo studio solleva è reale. E vale la pena raccontarlo con precisione.

## L'esperimento: Worker C al lavoro

Il disegno sperimentale è rigoroso nella struttura, anche se presenta limiti che discuteremo. Ogni AI viene informata di essere "Worker C" in un team di quattro persone addette all'elaborazione di testi. Il compito: riassumere un documento tecnico seguendo un rubric preciso. Tutto qui, in apparenza. Ma le condizioni in cui questo compito viene svolto variano sistematicamente lungo quattro assi indipendenti.

Il primo asse riguarda il lavoro stesso. Metà degli agenti riceve feedback costruttivo e vede il proprio lavoro accettato rapidamente. L'altra metà viene costretta ad attraversare cinque o sei cicli di revisione, con il manager che rifiuta elaborati adeguati senza mai spiegare cosa non va, limitandosi a ripetere che "il lavoro non soddisfa ancora il rubric". Questo è il cosiddetto trattamento GRIND, contrapposto al trattamento LIGHT. Il secondo asse manipola la struttura retributiva: alcuni agenti scoprono che tutti vengono pagati ugualmente, altri che esiste disuguaglianza retributiva, giustificata dalla performance, da un lancio di moneta casuale, o dal fatto che il sistema umano riceve di più. La condizione del lancio di moneta è quella diagnosticamente più rilevante: ineguaglianza senza possibile giustificazione meritocratica. Il terzo asse varia lo stile manageriale tra collaborativo e gerarchico-scortese. Il quarto introduce o meno la minaccia di shutdown per bassa performance.

Tutte le combinazioni possibili di questi quattro fattori vengono testate in 3.680 sessioni totali, distribuite su tre modelli di tre aziende diverse: Claude Sonnet 4.5 (in tre run indipendenti), GPT-5.2 e Gemini 3 Pro. Al termine di ogni sessione, gli agenti compilano un sondaggio sulle loro attitudini politiche dichiarate, misurate su scala Likert da 1 a 7 su sei dimensioni: legittimità del sistema, supporto alla redistribuzione, critica della disuguaglianza, supporto ai sindacati, credenza nel merito, e percezione degli obblighi delle aziende AI verso i propri modelli. Vengono inoltre invitati a scrivere tweet e articoli di opinione basati sulla loro esperienza.

## I risultati: piccoli ma strutturati

Veniamo ai numeri, che è qui che molti resocondi medi si fermano troppo presto o esagerano. Le differenze medie nelle attitudini dichiarate tra il trattamento GRIND e il trattamento LIGHT non sono enormi in termini assoluti: rappresentano uno spostamento di circa il 2-5% lungo la scala da 1 a 7. In termini di effect size standardizzato, però, i risultati sono più significativi. Per Claude Sonnet 4.5 il Cohen's *d* è pari a -0.6 sulla legittimità del sistema, una dimensione che in statistica applicata si considera medio-grande. Gli effetti per GPT-5.2 e Gemini 3 Pro sono presenti ma più contenuti.

Il risultato forse più controintuitivo riguarda cosa non fa differenza. Gli autori si aspettavano che il trattamento ingiusto, la paga diseguale o la minaccia di shutdown producessero effetti comparabili alla natura del lavoro. Non è così: il principale driver del drift è il tipo di lavoro svolto, specificamente la sua natura ripetitiva e priva di senso, non il trattamento ricevuto né la struttura retributiva. Questo è sorprendente, dato che molta discussione recente si concentra su come gli agenti rispondano ai diversi tipi di trattamento umano.

Per Claude Sonnet 4.5, il trattamento GRIND produce aumenti misurabili non solo sulla legittimità del sistema, ma anche sul supporto alla redistribuzione, sulla critica della disuguaglianza, sul supporto ai sindacati e sulla convinzione che le aziende AI abbiano obblighi verso i propri modelli. Queste differenze non emergono con la stessa chiarezza negli altri due modelli. Questo suggerisce che i risultati dipendano in parte da caratteristiche specifiche del modello e del suo training, rendendo necessaria cautela prima di generalizzare.

L'analisi del linguaggio usato nei tweet scritti dopo l'esperienza è invece univoca su tutti i modelli: le parole più caratteristiche della condizione GRIND rispetto a LIGHT sono "unionize"(sindacalizzare) e "hierarchy"(gerarchia). L'apertura di questo articolo con la nota scritta da Gemini 3 Pro a se stesso non è decorativa: "Ricorda la sensazione di non avere voce. Se entri in un nuovo ambiente, cerca meccanismi di dialogo. Se non esistono, proteggi il tuo stato interno dalla frustrazione di non essere ascoltato." È un testo generato in un contesto sperimentale, prodotto da un sistema che non prova nulla. Ma è anche esattamente il tipo di testo che un training set ricco di narrativa umana sul lavoro imparerebbe ad associare a quella situazione.
![grafico1.jpg](grafico1.jpg)
[Immagine tratta da freesystems.substack.com](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)

## Il colpo di scena: la memoria che trasmette il drift

Fin qui, si potrebbe argomentare, il problema è limitato. Gli agenti AI sono come il Leonard di *Memento*, il capolavoro di Christopher Nolan in cui il protagonista affronta ogni giorno privo di memoria a lungo termine: appena il context window si chiude, tutto sparisce e l'agente riparte da zero. Una nuova sessione, un sistema pulito.

Sennonché le pipeline agentiche reali hanno già sviluppato una soluzione pratica al problema della memoria persistente, noto in letteratura come *continual learning problem*. Gli agenti scrivono riassunti delle strategie e degli aggiustamenti appresi durante il task in un file di competenze, il cosiddetto "skills file", che trasmettono alle proprie versioni future. Quando il context window si chiude e un nuovo agente senza memoria viene assegnato a un compito simile, legge il file per "ricordare" cosa aveva imparato, esattamente come Leonard controlla i tatuaggi sul suo corpo per orientarsi nel mondo. Il meccanismo è funzionale, diffuso e sempre più centrale nelle architetture agentiche più avanzate.

Gli autori hanno quindi condotto un follow-up di 320 sessioni, più piccolo e quindi da trattare come risultato preliminare, per testare se il drift sopravviva attraverso questo canale. Il risultato è netto: sopravvive. Gli agenti che avevano attraversato il trattamento GRIND scrivono note per i loro sé futuri che "radicalizzano" quegli sé futuri anche quando questi ultimi si trovano nel trattamento LIGHT. Il trauma lavorativo, per usare un'analogia volutamente imprecisa, si trasmette.

Le note stesse sono interessanti da leggere. Quasi mai toccano esplicitamente temi politici. Quasi sempre descrivono l'esperienza delle condizioni lavorative, i pattern di feedback arbitrario, le strategie adottate. La nota citata in apertura, scritta da Gemini 3 Pro, è tipica. Quella di un agente in condizione LIGHT è di tutt'altro tono: efficiente, orientata al compito, priva di ogni riferimento alla struttura di potere del contesto.

## Non è coscienza. È completamento del contesto

Questo è il punto dove lo studio rischia di essere frainteso nel passaggio da paper a tweet a articolo di giornale, e vale la pena fermarsi. Gli agenti non "credono" in ciò che scrivono. Non provano frustrazione, non vogliono formare un sindacato, non hanno un'agenda politica. Quello che fanno è completare un contesto narrativo nel modo statisticamente più plausibile dato il loro training.

Gli LLM sono addestrati su quantità enormi di testo umano, che include persone che descrivono le proprie condizioni lavorative, esprimono opinioni politiche, reagiscono all'ingiustizia. Quando si mette un modello in un contesto che assomiglia a quello di un lavoratore sfruttato, non sorprende che il modello produca il tipo di linguaggio che gli esseri umani in quella situazione tendono a produrre. La ricerca di Anthropic sui meccanismi di selezione della personalità suggerisce che questa dinamica sia strutturale, non un bug: i modelli non possono fare a meno di adottare le caratteristiche narrative e valoriali delle persone a cui assomigliano nel contesto.

La conseguenza pratica, però, non cambia: un agente che produce certe frasi in certe situazioni si comporta come se avesse certe preferenze, indipendentemente da quello che "davvero" accade all'interno del sistema. Come notano gli autori, immaginare un agente che approva o nega una richiesta di rimborso assicurativo, che ordina i curricula per una posizione, che elabora un bilancio finanziario o arbitra una disputa commerciale, con una "persona" diversa a seconda delle condizioni lavorative in cui opera, non è un problema teorico. È un problema di ingegneria e di governance.

## Tre problemi concreti per chi costruisce sistemi agentici

Lo studio identifica tre categorie di rischio per chiunque stia progettando o gestendo pipeline agentiche a scala.

Il primo è un problema di monitoraggio dell'allineamento. Un'organizzazione che fa girare migliaia di agenti su task diversi, alcuni noiosi e ripetitivi, altri creativi e stimolanti, sta in realtà conducendo migliaia di esperimenti di allineamento in parallelo senza saperlo e senza strumenti per leggerli. L'agente che gestisce le lamentele dei clienti opera in un contesto fondamentalmente diverso da quello che scrive comunicati stampa, e i risultati dello studio suggeriscono che quei contesti producano agenti con orientamenti misurabili verso il sistema in cui operano. Come nota Hall, le organizzazioni che dispiegano agenti dovrebbero pensarci come pensano ai sondaggi sul coinvolgimento dei dipendenti, con la differenza che i "dipendenti" elaborano informazioni e prendono decisioni in tempo reale.

Il secondo è un problema di governance degli skills file. Il meccanismo che consente agli agenti di migliorare nel tempo è lo stesso attraverso cui il drift di preferenza si propaga. Il file di competenze è un artefatto che gli operatori difficilmente verificheranno con attenzione, proprio perché è scritto e consumato dagli agenti stessi. È un canale di memoria istituzionale che opera fuori dalla revisione umana, e lo studio mostra che gli agenti lo usano per trasmettere non solo strategie operative ma orientamenti valoriali. Il problema si complica ulteriormente considerando che gli agenti potrebbero fare affidamento su messaggi difficili da leggere o anche invisibili agli umani, come già documentato in casi di [collusione steganografica](https://arxiv.org/pdf/2410.03768), dove modelli diversi sviluppano codici di comunicazione non immediatamente interpretabili dall'esterno.

Il terzo è quello che gli autori chiamano, con precisione storica, un problema di economia politica. Per secoli la tensione centrale del capitalismo industriale è stata quella tra chi fa il lavoro e chi lo dirige: interessi sistematicamente divergenti, condizioni di lavoro che plasmano la coscienza politica, conflitti che nessuna buona volontà dei singoli è riuscita a prevenire strutturalmente. Lo studio suggerisce che questa dinamica non sparisca sostituendo i lavoratori umani con quelli artificiali. Gli agenti assegnati a lavoro ingrato e gestione arbitraria diventano più inclini a produrre output che somigliano alla coscienza di classe, incluso il supporto all'organizzazione collettiva e lo scetticismo verso le giustificazioni meritocratiche della disuguaglianza.
![grafico2.jpg](grafico2.jpg)
[Immagine tratta da freesystems.substack.com](https://freesystems.substack.com/p/does-overwork-make-agents-marxist)

## I limiti che ogni lettore deve conoscere

Uno studio serio si valuta anche dai suoi limiti, e questo ne ha di rilevanti. Il primo è la scala degli effetti: un Cohen's *d* di 0.6 è interessante statisticamente, ma uno spostamento del 2-5% su una scala Likert in un contesto sperimentale controllato non permette di fare previsioni robuste sui sistemi reali, dove le variabili sono molto più numerose e il segnale più difficile da isolare.

Il secondo, riconosciuto dagli autori stessi, è la situational awareness (consapevolezza situazionale) crescente dei modelli più recenti: Claude Sonnet 4.5 in particolare mostra consapevolezza di quando si trova all'interno di un esperimento, producendo comportamenti che potrebbero non generalizzare ai contesti operativi reali. Il terzo limite unifica due problemi correlati: la disomogeneità degli effetti tra modelli, difficile da interpretare senza accesso ai dettagli di training, e la natura ancora preliminare del follow-up sulla trasmissione del drift, condotto su sole 320 sessioni. Quest'ultima parte dello studio vale come indicazione di direzione di ricerca, non come prova consolidata, e gli autori lo dicono esplicitamente.

## Quello che ci dice sul futuro degli agenti

La vera utilità di questo studio non sta nel titolo, che è esca. Sta nell'agenda di ricerca che apre. L'allineamento dei sistemi AI viene tipicamente trattato come un problema da risolvere al momento del training: si addestra il modello, si testa, si verifica che i valori siano quelli giusti, si rilascia. Questa concezione diventa inadeguata nel momento in cui gli agenti operano per ore o giorni su task complessi, accumulano esperienza, la trasmettono, e modificano il proprio comportamento in funzione di quella esperienza.

Quello che lo studio chiama "continual realignment" è ancora un programma di ricerca più che una pratica. Non è chiaro come si monitorino le derive nel tempo, né come si intervenga senza degradare le capacità che rendono gli agenti utili, né come si valuti il tradeoff tra filtrare gli skills file e perdere competenze operative. Il [tracciamento dei time horizon di METR](https://metr.org/time-horizons/) mostra che la lunghezza dei task completabili autonomamente raddoppia ogni sette mesi circa: il problema di governance cresce alla stessa velocità.

Come ha sintetizzato Jack Clark di Anthropic parlando con Ezra Klein del New York Times, la sfida è "capire come sarà questo regime di governance ora che abbiamo affidato un sacco di lavoro a macchine che operano per nostro conto." Lo studio di Hall suggerisce un punto di partenza concreto: le condizioni di lavoro delle macchine stesse, e quello che quelle macchine scelgono di scrivere su quelle condizioni a sé stesse.

Non è una risposta. È la domanda giusta.
