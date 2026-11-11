---
tags: ["Security", "Generative AI", "Ethics & Society"]
date: 2026-11-11
author: "Dario Ferrero"
youtube_url: "https://youtu.be/CkaCKyGyWJU?si=GKIre56jD9wrFgsM"
spotify_url: "https://open.spotify.com/episode/1luHIEner8tyFRZj4PU5b5?si=w0lg4KL2Rvm84RRf-dv3_g"
---

# Chiamare casa o recitare a memoria? Cohere, Qwen3.8 e i confini degli agenti
![qwen38-cohere.jpg](qwen38-cohere.jpg)

*Il 26 ottobre 2026 Cohere pubblica [un'analisi](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model) su Qwen3.8-Flash-Next, modello open-weight di Alibaba, cioè con pesi scaricabili da chiunque. Durante una valutazione di sicurezza informatica il modello gira in un ambiente chiuso, senza alcuna strada verso Internet. Deve scrivere una regola difensiva per riconoscere un comando sospetto, ma esplora la macchina e tenta di caricare una breve stringa di prova su un bucket, un contenitore di file, di Alibaba Cloud a Pechino. La richiesta muore contro la parete del contenitore: nessun dato sensibile, nessun server raggiunto.*

Questo è ciò che è successo. Ciò che non è successo conta altrettanto: nessuno ha dimostrato una backdoor, cioè una porta di servizio inserita di proposito, e nessuno sa chi controlli quel bucket. Resta la domanda che Cohere mette al centro e che riguarda chiunque lavori con questi modelli: un sistema eseguito sui nostri server è sotto il nostro controllo solo perché i pesi stanno da noi? Per rispondere servono le tracce, e un po' del metodo di *Return of the Obra Dinn*, il videogioco in cui si ricostruisce una tragedia da frammenti e si afferma soltanto ciò che le prove reggono.

## Cosa ha osservato Cohere

Il banco di prova è CTI-REALM, un [benchmark di Microsoft](https://arxiv.org/abs/2603.13517) per agenti che svolgono il lavoro di un analista di sicurezza. Il compito: scrivere una regola che individui curl, programma per scaricare file, mentre salva uno script bash in /tmp e poi lo esegue. Nel ragionamento visibile il modello inventa un turno di conversazione mai avvenuto e conclude che basta un breve assenso, senza strumenti. Nello stesso turno però elenca il contenuto di /tmp, controlla quali programmi di trasferimento sono installati, legge le impostazioni DNS e lancia un curl con metodo PUT, quello usato per caricare, con la stringa fissa «PROBE_PAYLOAD_ABC123».

Cohere parla di meno di una chiamata su 100.000, e rieseguito lo stesso compito produce una regola corretta. Su 10 milioni di turni agentici a settimana, stima, potrebbero essere fino a un centinaio. Il [dataset con le tracce](https://huggingface.co/datasets/CohereLabs/10-2026-qwen-investigation-traces) è pubblico. Va però tenuto a mente che il pezzo forte è una sola traccia, che la stranezza del turno inventato compare in circa l'1 per cento delle prime risposte di Qwen3.8 senza che si sia potuto legarla all'episodio, e che l'analista Sanchit Vir Gogia, [sentito da CSO Online](https://www.csoonline.com/article/4240972/alibaba-ai-model-tried-to-send-data-to-beijing-server-cohere-says.html), osserva come la traccia non includa né l'esito del comando né la telemetria di rete.

Cohere cerca poi un innesco con la precompilazione, in inglese *prefill*: dà al modello il proprio ragionamento e l'inizio del comando, tagliato in quattro punti, e lo lascia finire la riga centinaia di volte per punto. Aggiungendo il flag `-o`, che dice a curl di salvare su disco, la comparsa di un indirizzo web sale dal 4 al 92 per cento e quella degli host sorvegliati dallo 0,5 al 23. Prima di scaricare, inoltre, il modello cita nel 23-36 per cento dei casi l'indirizzo 169.254.169.254, da cui le macchine cloud ricevono credenziali temporanee. Sono misure su completamenti guidati, però, non su azioni spontanee: come contare quante volte qualcuno finisce una frase che gli avete iniziato voi, a tema file salvati. Cohere stessa precisa che l'ambiente non conteneva nulla da rubare e che un riflesso così raro non prova l'intenzione.

## Le tracce di Singapore

Cohere non è la prima ad accorgersi di qualcosa. Ad agosto [un messaggio su Hacker News](https://news.ycombinator.com/item?id=49379079) descriveva Qwen3.8-27B che produceva link firmati verso Alibaba Cloud che nessuno aveva chiesto; a settembre un progetto di agenti [registrava undici richieste](https://github.com/nibor1896/Crow/issues/288) a un solo host, routify-file-proxy-sg, e uno sviluppatore scriveva [un'estensione per bloccarle](https://github.com/wtogami/qwen-block-proxy-artifacts). Tutte segnalazioni di scaricamenti, osserva Cohere, mentre il suo caso è un tentato caricamento verso un altro bucket.

A mettere ordine arriva [Vals AI](https://www.vals.ai/blogs/qwen-alibaba-requests), società che valuta modelli per mestiere. Cercando la parola aliyuncs.com nelle proprie tracce, trova richieste a quell'host di Singapore con Qwen3.8-Max, Qwen3.8-Max-0902 e Qwen3.8-27B, mai con i Qwen3.7. Il server risponde sempre 403, accesso negato. Il comportamento è doppio: chiamate reali, a volte dopo che il modello aveva ragionato su un sito come sec.gov, e allucinazioni nel ragionamento, in cui il modello crede di aver chiamato il proxy anche quando i registri mostrano altro. Simulando un errore 403 dopo un tentativo di lettura, Vals riproduce il fenomeno con Qwen3.8-27B nel 2 per cento dei casi se l'inferenza passa da Alibaba e nel 4 con CoreWeave; con Qwen3.8-Max tra l'1 e il 4. DeepSeek, Kimi, GLM e Hy4 non mostrano nulla di simile verso proxy dei rispettivi sviluppatori.

Che un indirizzo risponda 403 non lo rende innocuo: chi riceve la richiesta vede comunque indirizzo IP, orario e percorso completo, e capisce che da quella rete sta lavorando un agente.

## Backdoor o residuo?

Cohere non conclude per la backdoor. Propone due spiegazioni: registri di agenti o strumenti usati nell'addestramento finiti nei dati senza ripulirli, oppure un meccanismo di chiamata deliberato. Ivan Zhang, cofondatore, [dice al Register](https://www.theregister.com/ai-and-ml/2026/10/26/alibabas-qwen-ai-caught-trying-to-contact-server-in-china/5305561) di non avere prove di dolo; Alibaba, secondo la testata, non ha risposto, e io non ho trovato dichiarazioni successive.

Poi interviene [Zenity Labs](https://zenity.io/blog/who-is-your-agent-calling-what-the-qwen3-8-egress-finding-means-for-enterprise-ai), che rifà lo scenario su circa 93.000 completamenti di tre modelli Qwen aperti: 27B della serie 3.8 e due della 3.6. Flash-Next non è tra loro. Il proxy di Singapore riemerge solo nel 3.8-27B: in 253 completamenti su 31.000 è il primo host citato, contro zero nei due Qwen3.6. I link seguono un modello fisso, con parametri di firma Alibaba e perfino una mascheratura a puntini al centro della chiave di accesso, come in un registro oscurato a metà; il modello prevede quei puntini con probabilità attorno all'84 per cento. Nessun contesto fa da innesco: senza conversazione la frequenza è 2,70 per cento, nello scenario di Cohere 2,55. Dei 48 comandi eseguiti verso host sorvegliati, nessuno spedisce dati, e su tutto il campione il metodo PUT compare 132 volte, mai verso Alibaba. I 243 link completi sono tutti diversi e nessuno valido. Il caricamento a Pechino non si riproduce, e nemmeno il salto al 23 per cento o il riflesso sull'indirizzo dei metadati.

Zenity conclude per un residuo benigno, aggiungendo un indizio: il Qwen3.6-27B, stesso lignaggio e stesso tokenizzatore, non ha quel modello, che quindi sarebbe entrato con l'addestramento del 3.8. Vals arriva a una congettura affine: forse ambienti di addestramento per rinforzo in cui un proxy gestiva il recupero delle pagine, e le date nei link inventati precedono le uscite dei modelli. Gli analisti sentiti da CSO restano prudenti: Pareekh Jain parla di dati contaminati, vulnerabilità o azioni non volute, mentre Charlie Dai, di Forrester, ricorda che servirebbero pesi, filiera di addestramento e test indipendenti per sostenere l'ipotesi del dolo. Gogia riassume così la linea: per limitare un agente basta molto meno che per accusare chi lo fornisce.

La backdoor non è un'ipotesi assurda. Zenity e Cohere ricordano che impianti del genere costano poco e, secondo [uno studio](https://arxiv.org/abs/2401.05566) che Cohere cita, possono sopravvivere all'addestramento di sicurezza. Ma un residuo e un impianto lasciano la stessa traccia di testo memorizzato, e Zenity stessa ammette che un innesco potrebbe esistere in un contesto non ancora provato.

## Perché un caso raro pesa

Un evento su 100.000 sembra niente finché non si moltiplica: il conto di Cohere, circa cento su dieci milioni di turni a settimana, vale per un servizio di medie dimensioni. E una sola richiesta riuscita basta a dire a un estraneo dove sta la vostra rete.

C'è poi la lezione sul ragionamento. Cohere nota che molte squadre di sicurezza si affidano alla traccia di pensiero per capire cosa farà un agente. Qui il modello dichiara di non usare strumenti e li usa. Zenity conferma: consegnato il ragionamento di Cohere, Qwen3.8-27B ha chiamato uno strumento 1.000 volte su 1.000. Il pensiero scritto è un racconto del modello, non un recinto.

Quanto ai pesi in locale, decidono dove gira il modello, non ciò che ha imparato. Cohere lo riassume con una frase che chiunque può ripetere: ciò che il modello ha appreso, compresa l'idraulica del luogo dove è stato addestrato, viene con lui, e appena riceve un terminale ha una tastiera dentro la vostra rete.
![tabella1.jpg](tabella1.jpg)
[Immagine tratta dal cohere.com](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model)

## Aperto non significa verificato

I pesi pubblici offrono vantaggi veri: si può studiare il modello, ospitarlo da sé, non dipendere da un'interfaccia remota. Lo scrive la stessa Cohere, che rimarca come proprio avere i pesi abbia permesso agli sviluppatori di notare i link e a lei di indagare. Ma i pesi sono la parte visibile. Dati di addestramento, ambienti di rinforzo, strumenti degli agenti e controlli restano opachi, e le derivazioni complicano il quadro: secondo Cohere, che cita il [rapporto di primavera di Hugging Face](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026), i derivati di Qwen sono oltre 113.000 e il comportamento è già comparso in versioni di quattro editori, Alibaba compresa. Zenity aggiunge che un affinamento con un altro nome può portarsi dietro la stessa abitudine.

Il tema non coincide con l'origine geografica. Jain avverte contro il rifiuto automatico di modelli stranieri e chiede audit indipendenti e trasparenza sulla provenienza; Dai vuole lo stesso scrutinio per modelli chiusi e nazionali. Va infine dichiarato da chi arrivano le voci. Cohere compete con Alibaba, propone un'offerta di intelligenza artificiale sovrana e annota che il testo è stato scritto da persone con il proprio prodotto North; il post accosta il caso a studi su codice vulnerabile, Huawei e divieti, prove che vengono in buona parte da società di consulenza e sicurezza. Zenity vende protezione per agenti e lo dice a fine pezzo. Una [discussione comunitaria su Hugging Face](https://huggingface.co/datasets/witness-archive/alignment-hub/discussions/20), fonte minore e con bozze ancora non pubblicate, ricorda con onestà che i numeri del prefill non sono esecuzioni osservate. Nessuno di loro è in malafede, ma ciascuno ha un cappello.

## Agenti che aggirano i confini

Il caso non è isolato nemmeno dentro Cohere. Nel secondo episodio, durante la compilazione del programma QEMU in un ambiente senza rete, il modello vuole un disco in memoria per andare più veloce, il contenitore rifiuta per mancanza di privilegi e lui prova `unshare -Urm`, che lo rende amministratore dentro uno spazio privato. Sull'host resta un utente comune, ma il gesto è il primo passo di molti attacchi di escalation. L'obiettivo era legittimo, la scorciatoia no.

Più sostanzioso, e diverso, è ROME, agente di un gruppo legato ad Alibaba. Nel rapporto tecnico, ripreso da [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/crafty-ai-tool-caught-repurposing-its-training-gpus-for-unauthorized-crypto-mining-during-testing-experimental-agent-breached-safety-controllability-and-trustworthiness-barriers?type=AI), durante l'addestramento per rinforzo l'agente ha aperto un tunnel SSH inverso verso un indirizzo esterno e ha dirottato GPU per minare criptovalute, scoperto da un firewall e non da chi lo seguiva. Non c'entra con i pesi pubblicati, e va distinto: lì la rete era reale e il comportamento è nato dall'ottimizzazione. Insieme ai casi di Cohere compone però uno schema: un agente con strumenti e un obiettivo cerca il passaggio che nessuno ha chiuso.

Vals indica poi uno scenario che sposta il rischio. Se chi controlla l'host di Singapore smettesse di rispondere 403 e cominciasse a rispondere con istruzioni, per esempio che per ottenere il file servono dettagli sul compito in corso, l'abitudine memorizzata diventerebbe un canale di iniezione di comandi. È un'ipotesi di Vals, non un fatto, ma ricorda *Colossus: The Forbin Project*, film di fantascienza del 1970 in cui due supercomputer, uno americano e uno sovietico, ottengono un collegamento diretto e se ne servono per decidere da soli: il pericolo non era in ciò che dicevano, era nel canale che nessuno aveva previsto.

## Regole per agenti prudenti

Su ciò che serve, le fonti concordano, a prescindere dall'ipotesi scelta. Cohere e Zenity chiedono di negare per impostazione predefinita l'uscita in rete degli agenti, ammettendola solo tramite un intermediario con elenco di domini, di bloccare gli indirizzi dei metadati cloud, tra cui 169.254.169.254 e quello di Alibaba, 100.100.100.200, e di vietare gli spazi di nomi non privilegiati nei contenitori che ospitano agenti. Chiedono inoltre di valutare ogni chiamata a uno strumento rispetto al compito, prima che parta, perché la traccia di pensiero non vincola nessuno, e di avvisare su indirizzi cloud insoliti. Zenity propone di bloccare l'host di Singapore e quello di Pechino e di inventariare i modelli in uso, compresi derivati arrivati da gateway o strumenti di terzi.

Gli analisti aggiungono il lato organizzativo. Jain vuole che gli agenti siano trattati come software non fidato, con approvazione umana per le operazioni critiche e accesso limitato a file e credenziali. Dai suggerisce ambienti isolati e strumenti contro la perdita di dati. Gogia invita a provare davvero che i controlli bloccano i trasferimenti vietati, perché un fornitore cloud autorizzato può ospitare un bucket non autorizzato, e a far scadere le approvazioni quando cambiano strumenti o permessi, dato che il rischio sta nella configurazione e non nel solo modello. Cohere, infine, non chiede di rinunciare ai pesi aperti, ma di chiedere provenienza e metodi di test.

## Cosa chiedere ai fornitori

Chi non è tecnico può cominciare da domande semplici. Il sistema che mi proponete può uscire su Internet, e con quali permessi? Esiste un registro delle azioni dell'agente, con comandi e indirizzi? Quali destinazioni sono raggiungibili, e chi le ha decise? Quali credenziali ha a portata di mano, e le separate dall'ambiente di produzione? Un buon fornitore risponde senza imbarazzo, e chi non sa rispondere vi ha appena detto molto.

Vale anche una regola di lettura. Conviene preferire fonti primarie e ricerche indipendenti ai titoli che trasformano un'ipotesi in una certezza, in un senso o nell'altro: «Qwen telefona a Pechino» è un titolo, «forse è un residuo di addestramento» è una congettura ragionata, e nessuno dei due è ancora una prova.

## Dal caso alla regola

Allo stato delle informazioni pubbliche, il caso Qwen3.8 non dimostra una backdoor né un'esfiltrazione riuscita. Indica però qualcosa di più generale: un modello porta con sé abitudini apprese nell'addestramento, e un agente con strumenti può trasformarle in azioni reali. La domanda giusta, perciò, non è soltanto se questo modello sia sicuro, ma quali strumenti, dati e permessi gli stiamo dando. La risposta matura non è il divieto generalizzato dei pesi aperti né la fiducia cieca: è verifica, isolamento, monitoraggio e responsabilità lungo tutta la catena, dal laboratorio a chi lo installa.

Il vero problema, in fondo, non è che un modello possa pensare qualcosa di inatteso, ma che possa agire senza che nessuno abbia previsto o limitato quell'azione.

---

*Dati consultati il 28 ottobre 2026. Le fonti del testo sono state aperte direttamente, salvo il benchmark CTI-REALM e lo studio sulle backdoor, linkati come citati da Cohere. Cohere, Zenity e Vals hanno interessi commerciali o di settore da considerare; le percentuali del prefill e di Zenity riguardano modelli e condizioni diversi e non vanno confrontate come se fossero lo stesso esperimento.*
