---
tags: ["Applications", "Ethics & Society", "Generative AI"]
date: 2026-06-22
author: "Dario Ferrero"
youtube_url: "https://youtu.be/I2gE1utpvTI?si=WHXIWzHWQFCbfy8s"
---

# BenzUp: ho creato un'app senza scrivere una riga di codice
![benzup.jpg](benzup.jpg)

*C'è un momento preciso in cui un'idea smette di essere una fantasia da bar e diventa qualcosa di concreto. Nel mio caso quel momento ha avuto come protagonisti, nell'ordine: il costo della benzina, un ingegnere americano scocciato per una birra cara a Dublino, e un modello di intelligenza artificiale accessibile a chiunque abbia una connessione internet. Il risultato si chiama [BenzUp](https://benzup.netlify.app), è gratuito, non fa niente di rivoluzionario, e forse è proprio per questo che vale la pena raccontarlo.*

Nelle ultime settimane, tra amici, colleghi e conoscenti, il tema del caro carburante era diventato una presenza fissa nelle conversazioni. Non la novità assoluta, intendiamoci: il prezzo della benzina è da sempre uno degli argomenti nazionali per eccellenza, con buona pace di chi vorrebbe parlare d'altro. Ma la situazione contingente internazionale aveva alzato ulteriormente il volume del dibattito, e ci si ritrovava spesso a chiedersi dove convenisse fare il pieno, quali distributori fossero più onesti, se valesse la pena fare qualche chilometro in più per risparmiare qualcosa. Domande legittime, a cui nessuno aveva una risposta rapida e verificabile.

Io nel frattempo osservavo, prendevo mentalmente nota, e non facevo niente. Come si fa con la maggior parte delle buone idee: le si lascia decantare finché non arriva qualcosa a sbloccarle.

## Arriva la Guinness

Lo sblocco è arrivato una mattina sotto forma di una notizia che non avrei mai immaginato di leggere. Matt Cortland, ingegnere americano con radici irlandesi e base a Londra, si era trovato a pagare 7,80 euro per una pinta di Guinness in un pub di Dublino. Una cifra che, per chi conosce il rapporto quasi sacro tra gli irlandesi e la loro birra nazionale, è poco meno di un'offesa. Indagando, Cortland scopre che il Central Statistics Office irlandese aveva smesso di monitorare i prezzi della birra nel 2011, lasciando un vuoto informativo di quattordici anni. La sua reazione? Costruire un agente vocale chiamato Rachel, dotato di accento nord-irlandese, che nel weekend di San Patrizio 2026 ha telefonato a circa 2.300 pub in tutte le 32 contee dell'isola ponendo una sola domanda: quanto costa una pinta di Guinness? Il costo dell'intera operazione: circa duecento euro. Il risultato: il [Guinndex](https://guinndex.ai), una mappa interattiva dei prezzi della Guinness in Irlanda, elaborata tramite Claude di Anthropic a partire da oltre 1.200 risposte raccolte. Prezzo più comune rilevato: 5,50 euro a pinta. Record assoluto: 11 euro al The Temple Bar Pub di Dublino, che conferma la propria vocazione a spennare i turisti con una coerenza quasi ammirevole.

L'obiettivo dichiarato di Cortland è esplicito: "Voglio vedere se riusciamo collettivamente ad abbassare il costo di una pinta in tutta l'Irlanda." Il Guinndex è diventato una piattaforma crowdsourced aperta, dove chiunque può segnalare prezzi e contribuire a tenerlo aggiornato. E qualche primo segnale di discesa dei prezzi c'è, ma per ora è difficile da correlare all'iniziativa.

La storia è simpatica, l'idea è brillante, l'esecuzione è elegante. Ma soprattutto, leggendola, mi ha fatto scattare quella molla che stava aspettando da settimane. Se qualcuno aveva usato l'AI per mappare il prezzo della birra in tutta l'Irlanda spendendo duecento euro, io potevo usarla per costruire qualcosa di utile agli automobilisti senza spendere nemmeno un centesimo. Non avevo la velleità di far calare il prezzo della benzina, così come era nella speranza di Cortland  di far calare quello della Guinness, ma almeno avrei potuto dare un orientamento rapido su dove convenisse fermarsi.
![screenshot-guinndex.jpg](screenshot-guinndex.jpg)
[Screenshot di Guinndex.ai](https://guinndex.ai/)

## I dati erano già lì, gratis

Prima di buttarsi a capofitto nello sviluppo, qualche ricerca online si impone sempre. Ed è qui che arriva la prima sorpresa piacevole: il Ministero delle Imprese e del Made in Italy pubblica ogni mattina, in formato aperto e scaricabile da chiunque, i prezzi dei carburanti praticati da tutti i distributori italiani. Due file CSV, aggiornati quotidianamente, contenenti l'anagrafica completa degli impianti attivi su tutto il territorio nazionale, con indirizzo, coordinate GPS, gestore e bandiera, e i prezzi comunicati dai gestori, distinti per tipo di carburante e per modalità di erogazione, self service o servito. I dati sono rilasciati con licenza IODL 2.0, che consente il riutilizzo libero anche per finalità commerciali, purché si citi la fonte. Il Ministero non si limita a tollerare l'utilizzo di questi dati: lo incentiva attivamente.

Era esattamente quello di cui avevo bisogno. Niente scraping, niente zone grigie legali, niente dipendenza da API di terze parti che potrebbero cambiare le condizioni di utilizzo da un giorno all'altro. Dati ufficiali, aperti, aggiornati ogni mattina.

A quel punto ho deciso di restare piccolo e focalizzato: niente app nazionale, niente ambizioni da scala. Solo la mia provincia il VCO, quella sigla VB nei dati del Ministero, filtrata e servita in modo semplice e veloce. Un prototipo leggero per vedere se la cosa funzionava davvero.

## Il prompt come atto progettuale

Chi lavora con l'AI in modo anche solo semiregolare sa che la qualità dell'output dipende in misura determinante dalla qualità dell'input. Un prompt vago produce risultati vaghi. Questo non è un articolo sul prompting, ma vale la pena dedicargli un paragrafo, perché è stata la parte più artigianale dell'intera esperienza.

Ho messo giù i requisiti con una certa precisione. Sul piano tecnico: una web app in HTML, CSS e JavaScript puro, con una funzione serverless su Netlify per gestire le chiamate al MIMIT ed evitare i problemi di CORS che impediscono ai browser di fare richieste dirette a domini esterni, design responsive ottimizzato per mobile, filtraggio dei dati sulla provincia del VCO, due classifiche ordinate per prezzo dal meno costoso al più costoso, una per benzina e una per gasolio. Sul piano dell'interfaccia: un toggle visibile per passare da un carburante all'altro, le informazioni essenziali per ogni distributore, un pannello di dettaglio accessibile toccando il singolo impianto, data di riferimento e fonte in evidenza. Sul piano estetico: stile moderno, tipografia curata, palette sobria, qualcosa che sembrasse progettato e non generato.

Ho scelto deliberatamente di usare Claude Sonnet 4.6, la versione accessibile gratuitamente, proprio perché volevo testare cosa fosse possibile fare con gli strumenti disponibili a chiunque, non solo a chi ha un abbonamento premium o competenze da sviluppatore senior. Se funzionava con il modello gratuito, la storia aveva un senso anche per chi legge senza background tecnico.

In un paio di un minuti, circa 750 righe di codice. Un file HTML con tutto incluso: struttura, stile, logica, gestione degli errori, animazioni, pannello di dettaglio con swipe per chiuderlo. Mi era già capitato di usare modelli AI per scrivere piccoli pezzi di codice, qualche funzione, un componente isolato. Mai però qualcosa di questa complessità in un colpo solo. La prima sorpresa è stata aprire quel file nel browser del PC: tutto funzionava esattamente come l'avevo descritto. Layout corretto, toggle tra benzina e gasolio, pannello di dettaglio, animazioni fluide. Ovviamente senza dati reali, ma la struttura era esattamente quella richiesta.

## Dal browser alla produzione

Avere un file HTML che funziona in locale è una cosa. Averlo online, con dati reali che arrivano dal Ministero, è un'altra. Questo è il passaggio in cui una minima familiarità con gli strumenti disponibili ha fatto la differenza.

Ho creato un repository su GitHub, caricato i file, collegato il repository al mio account Netlify. Netlify ha rilevato automaticamente la configurazione, ha attivato la funzione serverless che scarica e filtra i CSV del MIMIT, e in pochi minuti l'app era online. Seconda sorpresa: funzionava. I dati arrivavano, i distributori della provincia VB apparivano ordinati per prezzo, il toggle tra benzina e gasolio rispondeva come previsto.

A quel punto ho fatto una cosa che consiglio sempre quando si lavora con codice generato dall'AI: un controllo incrociato con un altro strumento. Ho collegato Jules, l'agente AI asincrono di Google integrato direttamente in GitHub, e gli ho chiesto un'analisi del codice. Jules non ha segnalato problemi rilevanti, il che non è una garanzia assoluta ma è comunque un secondo paio di occhi computazionali sul lavoro fatto.

Con Jules ho poi apportato alcune integrazioni che rendessero l'app più simile a un'applicazione nativa. È stato aggiunto un file manifest JSON che consente l'installazione sul telefono direttamente dal browser, senza passare dagli store, un'icona personalizzata, e una pagina dedicata alle informazioni utili, con spiegazione del funzionamento, della provenienza dei dati, dei limiti del sistema e delle istruzioni per l'installazione su Android e iPhone. Quella pagina, come vedremo, si è rivelata più importante del previsto.


![benzup-screenshot.jpg](benzup-screenshot.jpg)
[Screenshot di BenzUp](https://benzup.netlify.app)

## I limiti sono parte del prodotto

Un giorno di test personale, poi la diffusione a una cerchia di amici con la richiesta esplicita di segnalare qualsiasi problema. I riscontri sono stati positivi, ma è arrivata una segnalazione ricorrente: i prezzi di alcuni distributori sembravano fermi da giorni. Nessun bug dell'app, semplicemente la realtà del sistema: i gestori sono tenuti per legge a comunicare le variazioni di prezzo al Ministero, ma non tutti lo fanno con cadenza quotidiana. In più, i dati vengono pubblicati ogni mattina riferiti alle ore 8:00 del giorno precedente, e l'effettivo aggiornamento nell'app può slittare di qualche ora per via dei tempi di pubblicazione del Ministero e dell'infrastruttura tecnica su cui l'app è ospitata, su cui non ho controllo diretto.

Quella segnalazione ha portato a migliorare la pagina informativa, aggiungendo una spiegazione chiara di questi meccanismi e indicando che toccando la scheda di un singolo distributore si può verificare la data dell'ultimo aggiornamento inviato al Ministero. La trasparenza non è un optional, è parte integrante di un servizio che si basa su dati pubblici e che non ha nessun interesse a sembrare più preciso di quello che è.

È arrivata anche una richiesta precisa: aggiungere GPL e metano, carburanti che per molti automobilisti della provincia sono tutt'altro che secondari. Nei giorni seguenti li ho integrati, e ora BenzUp mostra le classifiche per tutti e quattro i tipi di carburante.

## Tre giorni, 800 visite

L'app è online da tre giorni mentre scrivo questo articolo (11 aprile 2026). L'ho lanciata con un post sul blog locale che gestisco da molti anni, [Verbania Notizie](https://www.verbanianotizie.it), nessuna pubblicità a pagamento, nessuna campagna, nessuna strategia di crescita. In tre giorni, circa 800 visite. Cifre insignificanti su scala nazionale, probabilmente irrilevanti anche su scala locale se misurate con i parametri del marketing digitale. Ma non è questo il punto.

Il punto è che da un'idea nata in una conversazione sul caro carburante a un'app funzionante in produzione, consultata da centinaia di persone reali della mia provincia, è passata meno di una settimana. Senza scrivere una riga di codice, senza un budget, senza un team di sviluppo. Con una conoscenza dell'ecosistema degli strumenti digitali gratuiti disponibili, un prompt costruito con cura, e la disponibilità a iterare, correggere, migliorare sulla base dei feedback reali.

## Aggiornamenti

Questo storia ha avuto il piacere di essere pubblicata sul magazine di Codemotion, quindi la pubblico oggi sul portale a due mesi di distanza dalla stesura, è quindi d'obbligo un breve aggiornamento.

Nei due mesi successivi alla stesura di questo articolo BenzUp ha continuato a evolversi, sempre seguendo la stessa filosofia: nessun costo, nessuna infrastruttura complessa, tutto costruito con gli strumenti gratuiti già disponibili.
La novità più significativa è l'espansione geografica: l'app copre ora l'intera regione Piemonte, con tutte e otto le province e la possibilità di filtrare per comune tramite un menu dedicato. Da strumento iperlocale pensato per gli automobilisti del VCO è diventato un riferimento per chiunque si muova in regione, o ci transiti.

Sul piano tecnico l'architettura è stata ripensata in modo sostanziale. I dati non vengono più elaborati in tempo reale a ogni richiesta, ma pre-generati ogni mattina in file statici serviti direttamente dalla CDN di Netlify, con un risultato immediato e misurabile sulla velocità di caricamento. Una GitHub Action schedula autonomamente il processo, controlla che il Ministero abbia effettivamente pubblicato dati aggiornati prima di procedere, e genera un file JSON per ciascuna provincia. Il frontend legge il file corretto e lo mostra istantaneamente, senza passare per nessuna funzione serverless.

È stato aggiunto anche un sistema a semaforo sulla freschezza dei dati di ogni singolo distributore: verde se il prezzo è stato aggiornato nelle ultime 24 ore, giallo entro le 48, rosso oltre. Un modo semplice e visivo per dare all'utente un'informazione che prima richiedeva di aprire la scheda di dettaglio di ogni impianto.

Infine, un modulo di segnalazione accessibile dalla scheda di ogni distributore permette agli utenti di comunicare eventuali discrepanze, prezzi non aggiornati, impianti chiusi, errori nei dati. Piccolo presidio di qualità collettiva, coerente con la natura volontaria e trasparente del progetto.

## Considerazioni finali

Questo non è un inno al vibe coding, quella pratica di generare codice in modo rapido e approssimativo fidandosi ciecamente dell'AI senza capire cosa si sta facendo. Il vibe coding, peraltro, sembra già avviato verso il superamento da parte di un approccio più strutturato e professionale: scrivere le specifiche del progetto in file markdown dettagliati, da passare agli agenti di codice come istruzioni precise e verificabili, invece di affidarsi a prompt improvvisati. Ne ho parlato in un [articolo su questo stesso portale](https://aitalk.it/it/codespeak.html), e la differenza in termini di controllo e qualità del risultato è sostanziale. Ma questa è davvero un'altra storia. Quello che voglio raccontare è qualcosa di più semplice e forse più interessante: l'AI ha ridotto in modo radicale la distanza tra l'idea e la sua realizzazione, anche per chi non ha competenze specifiche di programmazione.

Questo non significa che programmatori, ingegneri e architetti del software siano diventati figure superflue, anzi. Portare un prototipo funzionante in produzione è una cosa, costruire qualcosa di stabile, sicuro e scalabile è un'altra: per quello servono competenze reali, esperienza e una comprensione profonda dei sistemi che nessun prompt, per quanto ben costruito, può sostituire.

Nel mio caso, una certa dimestichezza con gli strumenti online e una curiosità da utente evoluto, non da esperto, ha permesso di portare il progetto in produzione invece di fermarlo a prototipo. Ma la soglia si è abbassata per tutti. Chiunque abbia un'idea chiara, la pazienza di costruire un prompt decente, e la voglia di imparare i meccanismi minimi di deploy su piattaforme come Netlify o Vercel, può fare lo stesso.

Da qualche parte nel mondo, qualcuno con l'idea giusta, un po' di intraprendenza e un account gratuito su Claude sta probabilmente costruendo in questo momento qualcosa che non esiste ancora. Non il nuovo Facebook, forse, ma qualcosa di utile per le persone intorno a lui. E questo mi sembra già abbastanza.

Nel frattempo, se siete automobilisti del Piemonte (per ora) e volete sapere dove fare il pieno spendendo meno, [BenzUp è lì](https://benzup.netlify.app) che aspetta. Gratuito, indipendente, con tutti i suoi limiti ben dichiarati.

E se dovesse sfondare e finire con un'exit miliardaria verso qualche big tech della Silicon Valley, vi aspetto tutti al grande party che darò nella mia mega villa sulle sponde del Lago Maggiore, perché, anche se ricco sfondato, resterò fedele a dove tutto è iniziato.