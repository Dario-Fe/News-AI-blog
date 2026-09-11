---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-09-11
author: "Dario Ferrero"
youtube_url: "https://youtu.be/HRvaKLUOxK0?si=a9TeBkEmfMofFW0D"
spotify_url: "https://open.spotify.com/episode/2Z08SzufNYcLm6fI0n0h5O?si=jsjAOH7CT-66_lv2x2BzzA"
---

# Guida ai motori di inferenza e ai client per LLM locali
![guida-motori-inferenza-locale.jpg](guida-motori-inferenza-locale.jpg)

*C'è un momento preciso in cui una tecnologia smette di essere promessa e diventa strumento. Non è quando esce il comunicato stampa, non è quando i benchmark fanno il giro dei social, ma quando una persona normale, con un PC normale, si siede, scarica qualcosa e decide di capire davvero cosa sta succedendo. Nel 2026 questo momento è arrivato con forza per l'inferenza locale, e con essa si è aperto un problema che quasi nessuno spiegava chiaramente prima di arrivare confuso davanti alla console di comando: non manca più il modello, manca la chiarezza su *come* farlo girare.*

La ragione di tutto questo è semplice ma sottovalutata. Come emerge dal [report Currents di DigitalOcean](https://www.digitalocean.com/currents/february-2026), il 64% delle aziende oggi integra modelli attraverso API di fornitori terzi, mentre solo il 15% si dedica principalmente ad addestrare modelli da zero: la maggior parte del lavoro, insomma, è ormai integrazione più che costruzione. Il cloud non è morto, è ancora dominante, ma quella che sembrava un'asimmetria insuperabile tra modelli proprietari enormi e modelli locali "di ripiego" si sta assottigliando con una velocità che sorprende anche gli osservatori più attenti. Qwen3.5-9B, con circa tredici volte meno parametri di alcuni giganti del cloud, sul benchmark GPQA Diamond, il test di riferimento per il ragionamento a livello universitario avanzato, segna 81.7 contro l'80.1 di GPT-OSS-120B di OpenAI, come riportato sulla [pagina ufficiale del modello su Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B). Il divario è minimo, non uno scarto abissale, ma il punto resta: un modello enormemente più piccolo tiene testa a uno molto più grande, ed è un cambio di paradigma su cosa significhi "piccolo" nel 2026.

Ma con la democratizzazione dell'hardware è arrivato anche un nuovo labirinto: se scarichi un modello open-weight e lo metti sul tuo PC, cosa usi per farlo girare? La risposta dipende da una distinzione che quasi nessuno spiega prima e che organizza quasi tutto l'ecosistema: la differenza tra il **motore** di inferenza e il **client** che quel motore impacchetta.

Prima di procedere, è necessario essere chiari su cosa è questo articolo e cosa non è. Quello che segue è un'analisi di caratteristiche e specifiche tecniche, costruita su documentazione ufficiale, repository, changelog e verifica incrociata tra fonti autorevoli. Non è un benchmark scientifico, non c'è un protocollo di testing peer-reviewed, non c'è un campione statisticamente significativo. Ho testato sull'hardware reale solo due prodotti di questa panoramica, e li cito come citazione, non come struttura portante. Chi vuole numeri certificati troverà i benchmark sulle pagine ufficiali di ciascun prodotto. Chi vuole capire cosa promettono di fare questi strumenti, e con quale hardware, continui a leggere.

La verità, come spesso accade in questo campo, non sta su una tabella. Sta nel capire cosa ogni strumento fa davvero, e cosa ti chiede di cedere in cambio.

## Il motore e l'auto

Per eseguire un modello linguistico in locale servono due cose: il modello stesso, un file di qualche gigabyte, e qualcosa che faccia da interprete tra l'hardware e il modello, gestendo memoria, tokenizzazione e inferenza. Senza questo strato intermedio, scaricare i pesi di un modello è come avere i file di un film senza un lettore video. Ed è qui che si apre la separazione che divide quasi tutto l'ecosistema.

Da una parte ci sono i **motori di inferenza**, chiamati anche runtime o inference engine. Sono librerie e server a basso livello, spesso headless, che gestiscono direttamente il caricamento del modello, lo scheduling delle richieste, l'uso di CPU e GPU, le quantizzazioni e i vari formati di peso. Non hanno quasi mai una vera interfaccia grafica, parlano tramite API, e il loro successo si misura in throughput e latenza. Il target è lo sviluppatore, il MLOps, chi deve servire un modello a decine di utenti. Sono il motore nudo di un'auto, quello che vedi quando qualcuno apre il cofano per mostrartelo.

Dall'altra ci sono i **client**, i runner o i prodotti end-user. Applicazioni pronte all'uso che prendono uno o più motori e li avvolgono di qualcosa di utilizzabile: un browser di modelli, una chat, un server API già configurato, a volte plugin per la web search, RAG sui tuoi documenti, perfino agenti. Non ti chiedono di configurare nulla, ma in cambio non sai sempre cosa succede dentro. La metafora dell'auto è precisa qui: il client ti dà aria condizionata, navigatore e sensori di parcheggio. Tu rinunci a regolare manualmente la ripartizione della frenata, ma arrivi comunque.

La domanda che attraversa tutto l'articolo non è "quanto controllo cedo", è "con che hardware riesco a far girare ciò che promette". Questo sposta il fulcro dal software all'hardware, ed è proprio lì che vive la vera differenza tra i due mondi. Un motore ottimizzato per le H100 di un data center e un client pensato per girare sul MacBook di casa parlano lingue diverse, e saper distinguere cosa serve a cosa, è metà del lavoro.

La mia esperienza reale tocca solo due punti di questa mappa, e li nomino come citazione, non come struttura: LM Studio e Unsloth Studio su una Radeon RX 9060 XT con 16 GB di VRAM, la stessa configurazione che molti utenti avanzati, gamer, content creator o sviluppatori che lavorano da casa riconoscerebbero come propria. Hardware di fascia media-alta consumer, ma lontano dall'A100 che si immagina quando si parla di inferenza locale. Il resto è lettura attenta di documentazione, non prova sul campo.
![schema1.jpg](schema1.jpg)

## I motori

### llama.cpp

[llama.cpp](https://github.com/ggml-org/llama.cpp) è il motivo per cui quasi tutto gira. Questa libreria in C/C++ è il motore silenzioso dietro la maggior parte dei client che conosce la gente comune: Ollama, LM Studio, Jan, GPT4All e KoboldCPP si appoggiano tutti, in varia misura, al suo cuore. La sua forza è la portabilità estrema: gira su CPU, su GPU NVIDIA con CUDA, su AMD con HIP, su schede Intel con Vulkan e SYCL, e sul Metal di Apple Silicon, tutto nello stesso pacchetto. Non è un caso se il formato GGUF, pesi quantizzati, self-contained, agnostici rispetto all'architettura, sia diventato lo standard de facto per i modelli locali: llama.cpp ne è l'implementazione di riferimento.

Il rovescio della medaglia è lo stesso della sua onnipresenza: è configurato "da sviluppatore", con un controllo fine ma poco orientato al serving multi-utente. Se vuoi far girare un modello sul tuo laptop per sperimentare con le quantizzazioni GGUF, è probabilmente la scelta migliore in assoluto. Se devi servire quel modello a un'intera squadra con API stabili, è il motore ma non il prodotto.

### vLLM

Se llama.cpp è il motore del fai-da-te, [vLLM](https://vllm.ai/) è il motore da corsa in produzione. Creato dai ricercatori di UC Berkeley, è diventato lo standard de facto per il serving ad alto throughput, e la sua rivoluzione si chiama PagedAttention: invece di trattare la memoria KV cache come un blocco unico e sprecato, la tratta come la memoria virtuale di un sistema operativo, a pagine, con copy-on-write e condivisione dei prefix tra richieste simili. Nel paper originale del progetto, i sistemi precedenti sfruttavano solo il 20-40% della memoria KV cache disponibile; con PagedAttention l'utilizzo sale a circa il 96%, permettendo un throughput 2-4 volte superiore rispetto al batching naive a parità di latenza.

Ma vLLM vive sul terreno delle GPU NVIDIA. CUDA è la sua casa, e il supporto AMD tramite HIP sta crescendo, ma resta uno strumento orientato al data center, meno adatto a laptop e CPU. Il setup è più complesso, e la filosofia è chiara: serving per team e aziende, API backend per applicazioni, workload concorrenti. Se il tuo obiettivo è far parlare decine di utenti con lo stesso modello, vLLM è probabilmente la prima cosa che studierai.

### SGLang

[SGLang](https://github.com/sgl-project/sglang) fa una cosa diversa e più specifica: è ottimizzato per i modelli che non si limitano a rispondere, ma pensano a grafi. Agenti che fanno più passi, tool-use, RAG avanzato, flussi di "deep research" dove il modello chiama strumenti esterni e concatena generazioni. La sua forza è co-progettare il frontend linguistico con il runtime, così da gestire pattern di decoding non banali con efficienza.

È meno "commodity" di vLLM o llama.cpp, e la documentazione sa ancora di early adopter. Ma se il tuo obiettivo sono agenti locali multi-step o la prototipazione di flussi agentici, SGLang è uno degli strumenti più promettenti del 2026, con supporto rapido sui modelli più avanzati come gpt-oss.

### TGI

[Text Generation Inference](https://huggingface.co/docs/text-generation-inference) di Hugging Face è un veterano in fase di transizione. Per anni è stato il server di inferenza di riferimento per chi ospitava modelli da Hugging Face in produzione, con kernel ottimizzati in Rust e Python, maturità, documentazione solida e integrazione diretta con HF Hub. Ma l'11 dicembre 2025 Hugging Face ha messo TGI in maintenance mode: niente più nuovi modelli, nuove feature o nuove ottimizzazioni, e la stessa Hugging Face indirizza esplicitamente chi deve fare nuovi deploy verso vLLM e SGLang. Il repository accetta ormai solo fix di bug e migliorie alla documentazione.

Non è morto, continua a funzionare, ma per un nuovo progetto è una scelta da fare con coscienza: puoi ancora usarlo, ma non è più il futuro che Hugging Face sta costruendo. È il classico caso in cui lo strumento migliore di ieri diventa eredità da gestire, un po' come certi mainframe COBOL che nessuno vuole più toccare ma che nessuno riesce a spegnere.

### TensorRT-LLM

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) è lo stack di NVIDIA per l'inferenza ottimizzata sulle sue GPU più moderne, dalle H100 alle L40S, dalle A100 alle serie più recenti. La sua forza è la massima performance sull'hardware NVIDIA, con integrazione diretta con Triton Inference Server per scalare da una GPU a interi cluster tramite Kubernetes. È lo strumento per chi ha già l'infrastruttura e vuole estrarne il massimo.

Il rovescio è il lock-in: TensorRT-LLM vive e muore con NVIDIA, ha una curva di apprendimento ripida, ed è irrilevante per il consumatore medio. Se lavori in un data center con GPU NVIDIA e il workload è critico per latenza e throughput, è probabilmente il top. Altrimenti è un mondo lontano dal tuo desktop.

### MLX

[MLX](https://mlx.ai/) è il framework di Apple per il machine learning su Silicon, e la sua forza è l'uso unificato della memoria. Su un Mac con chip M1, M2, M3 o successivi, CPU e GPU condividono lo stesso pool di RAM, e MLX sfrutta questo per fare inferenza zero-copy che nessun porting di llama.cpp può eguagliare in efficienza. È la ragione per cui un MacBook può far girare modelli che su PC equivalenti faticano.

Il limite è evidente: MLX vive e muore con macOS e Apple Silicon, ed è meno cross-platform. Ma se hai un MacBook o un Mac mini, è probabilmente il motore più naturale per l'inferenza locale, e sempre più runner e app si appoggiano a lui come backend nativo per l'ecosistema Apple.

## Le auto

### Ollama

[Ollama](https://ollama.com/) è lo strumento di chi vuole semplicità. Si installa con un comando, espone di default un'API REST compatibile con OpenAI su `localhost:11434`, e si integra senza attrito in script, pipeline e applicazioni. È open source, ha una community ampia, e la sua filosofia minimalista, un comando per scaricare e uno per eseguire, lo rende il backend preferito di dozzine di applicazioni terze. In termini di performance grezza è tendenzialmente più veloce, gestisce meglio le richieste concorrenti e consuma meno risorse grazie all'assenza di overhead grafico.

Il rovescio della medaglia è la familiarità con il terminale richiesta, la configurazione avanzata che passa per i Modelfile, e una GUI nativa arrivata tardi e rimasta minima. C'è anche una questione di trasparenza che vale la pena segnalare: essendo open source, il codice di Ollama è ispezionabile da chiunque, cosa che non vale sempre per i competitor con GUI proprietaria. Per sviluppo locale di app con LLM, uso personale da terminale o via API, prototipazione rapida, Ollama resta un pilastro.

### LM Studio

[LM Studio](https://lmstudio.ai/) gioca su un campo diverso. È un'applicazione desktop con interfaccia grafica curata, disponibile per Windows, macOS e Linux, e la sua forza è eliminare la frizione che frena la maggior parte delle persone che si avvicinano all'AI locale. Permette di cercare, scaricare e caricare modelli senza aprire un terminale, espone anch'essa un'API compatibile con OpenAI, e gestisce automaticamente l'accelerazione GPU su NVIDIA, Apple Silicon e AMD.

Ma il dettaglio che cambia davvero l'esperienza per chi arriva senza background da sviluppatore è uno: al momento della selezione di un modello, LM Studio mostra in tempo reale una stima delle performance attese sulla propria configurazione hardware, con indicatori cromatici, verde, giallo, rosso, che comunicano immediatamente se il modello girerà agevolmente, con limitazioni, o se l'hardware è insufficiente. Per un privato che sperimenta, questa frizione eliminata vale l'eventuale gap di performance rispetto a Ollama.

Questo non è teorico, l'ho visto funzionare. Nella mia configurazione con Radeon RX 9060 XT da 16 GB, è stato proprio l'indicatore verde di LM Studio a confermarmi che Qwen 3.5 9B in Q8_0 girava interamente su GPU senza dover sparpagliare layer sulla RAM di sistema, e ho scelto il modello in anticipo, senza calcoli a mano né documentazione tecnica da consultare. Un dettaglio che, tradotto, significa non scoprire di aver sbagliato modello dopo aver scaricato dieci gigabyte.

LM Studio è closed source, un binario gratuito ma non trasparente, e alcune funzionalità legate al web non sono attive di default. Ma per chat locale con GUI, sperimentazione con GGUF e API locale, è probabilmente il punto di partenza migliore per chi non vuole sapere cosa succede sotto il cofano.

### Jan

[Jan](https://jan.ai/) è l'alternativa open source che punta sulla privacy e sul self-hosting senza sacrificare l'usabilità. Ha una GUI desktop pulita, supporta più backend tra cui llama.cpp, espone un'API locale su una porta dedicata, e si presenta come un'alternativa a ChatGPT genuinamente aperta. La sua forza è l'equilibrio: open source come LM Studio non lo è, con una UX che Ollama non ha.

Il limite è un ecosistema di modelli meno curato e una diffusione minore, che si traduce in meno documentazione e meno community alle spalle. Per chi vuole open source e GUI senza troppe complicazioni, Jan merita un posto nel test.

### Unsloth Studio

[Unsloth Studio](https://unsloth.ai/) è il prodotto che più si avvicina a quello che un assistente "agentico" locale dovrebbe essere. *Una precisazione utile: al momento esistono due porte d'accesso allo stesso ecosistema, Unsloth Studio, l'interfaccia che gira nel browser e che al momento della scrittura è ancora etichettata come beta, e Unsloth Desktop, l'app nativa più recente per Windows, macOS e Linux. Le funzionalità di fondo sono le stesse, cambia solo il contenitore.* Non è solo un runner: è un ambiente che integra web search nativa, deep research, RAG su documenti locali, esecuzione di codice, knowledge base personali, e anche fine-tuning QLoRA guidato senza toccare un terminale. Il motore sottostante è llama.cpp per i GGUF, con componenti di training che lo rendono uno strumento ibrido tra inferenza e addestramento.

Il target è preciso: creator, ricercatori, chi scrive articoli o report e vuole che il modello cerchi fonti, legga pagine e generi bozze citate. La web search integrata e il deep research, che costruisce un piano, trova riferimenti credibili e genera un report con citazioni, lo distinguono dalla maggior parte dei competitor. Il rovescio è che è ancora in rapida evoluzione, meno maturo come runner "puro" rispetto a Ollama o LM Studio, e alcune funzioni possono ancora presentarsi con qualche instabilità, coerentemente con l'etichetta beta che porta ancora addosso. Ma se il tuo obiettivo è scrivere con le fonti, è probabilmente lo strumento più promettente del gruppo.

Anche qui l'esperienza diretta ha un peso. Nel test con Unsloth Studio sulla mia RX 9060 XT, la capacità di far cercare al modello pagine web mentre lavoravo, e di usare il deep research per costruire report citati, ha mostrato cosa significa avere un ambiente agentico pronto all'uso, senza assemblare sei componenti diversi. Non è un runner, è un laboratorio.

### LocalAI

[LocalAI](https://localai.io/) fa una cosa elegante: si pone come astrazione uniforme sopra più backend. Se hai llama.cpp, vLLM, MLX e vuoi un'API OpenAI-compatible coerente che parli con tutti senza doverti ricordare quale comando lanciare per quale motore, LocalAI è la soluzione. Supporta più modelli contemporaneamente, e la sua filosofia è "un'installazione, tanti motori", senza diventare un download gigante perché ogni backend si attiva solo quando un modello lo richiede.

Il limite è che è più infrastrutturale che desktop-friendly: non è lo strumento per chattare, è quello per costruire un backend unificato in ambienti eterogenei. Per self-hosting server e app che usano più motori, è una scelta solida.

### Open WebUI

[Open WebUI](https://openwebui.com/) è quello che molte persone cercano senza saperlo: una "ChatGPT self-hosted" per il proprio team. Si appoggia a Ollama, vLLM o altri motori tramite API, ma aggiunge tutto ciò che manca a una piattaforma condivisa: chat multi-utente, RAG integrato, web search tramite SearXNG o provider come Brave, gestione utenti, workspace, agenti. L'interfaccia è moderna, e la flessibilità è alta.

Il prezzo è il deployment: richiede Docker e un minimo di configurazione server, quindi non è "scarica e usa". Ma se vuoi una piattaforma condivisa per un team con RAG e web search, Open WebUI è probabilmente il miglior risultato del 2026 su questo fronte.

### GPT4All

[GPT4All](https://gpt4all.io/) è stato per anni il primo contatto di molti con l'idea stessa di un LLM sul proprio computer: interfaccia semplicissima, nessuna configurazione, modelli scaricabili con un clic. Il problema, ed è giusto dirlo con chiarezza, è che lo sviluppo attivo si è fermato: nessun commit al repository da maggio 2025, nessuna release da febbraio 2025. L'app funziona ancora, apre e chatta senza intoppi, ma non riceve più aggiornamenti, nuovi modelli o correzioni di sicurezza. Va considerato più un punto di ingresso storico che una scelta consigliata per il 2026: chi cerca oggi la stessa semplicità troverà in Jan o nello stesso Ollama alternative più curate.

### KoboldCPP

[KoboldCPP](https://koboldcpp.com/) nasce dall'ecosistema KoboldAI e si rivolge a un pubblico preciso: chi scrive narrativa lunga, roleplay o storytelling assistito. Sopra un motore basato su llama.cpp costruisce un set di opzioni di generazione, preset e strumenti di editing pensati per il testo creativo, cose come la gestione della memoria narrativa o i World Info, che altri client non offrono nemmeno. È un eseguibile singolo, leggero, pensato per chi viene dal mondo dei giochi testuali più che da quello dello sviluppo software.

Il limite è la specializzazione stessa: fuori dal perimetro della scrittura creativa, KoboldCPP è meno comodo di LM Studio o Ollama per un uso generico, e la sua interfaccia, pur funzionale, sa di strumento costruito da appassionati per appassionati, non da un team di prodotto.

### Text Generation WebUI

[Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) è il coltellino svizzero della sperimentazione locale. Interfaccia web installabile in locale, supporto a più backend, un sistema di estensioni che permette di aggiungere praticamente qualunque cosa, dal RAG ai TTS, fino a configurazioni avanzate di sampling che altri client nascondono deliberatamente per semplicità. È lo strumento per chi vuole mettere le mani in ogni parametro.

Il rovescio è la curva di apprendimento: l'interfaccia mostra tutto, il che significa anche mostrare troppo a chi cerca solo di chattare. Non è pensato per l'utente occasionale, ma per chi tratta l'inferenza locale come un laboratorio permanente.
![tabella1.jpg](tabella1.jpg)

## Cosa scegliere, a seconda di cosa vuoi davvero

La scelta giusta dipende da cosa stai cercando di fare, e nessuna classifica universale può sostituirsi al tuo contesto. Ma alcuni scenari guidano quasi sempre verso le stesse risposte.

Vuoi solo chattare in locale sul tuo PC, senza configurare nulla. Qui vincono LM Studio per l'UX o Jan se cerchi qualcosa di completamente open source, con Ollama come alternativa se ti trovi bene con la CLI. Hai provato LM Studio sulla tua configurazione e hai visto l'indicatore verde accendersi: non c'è motivo di reinventare la ruota.

Devi servire un modello a più utenti in azienda, con API stabile. Qui il terreno è dei motori: vLLM per il throughput e il batching continuo, TGI se parti da un ecosistema Hugging Face già esistente, con la consapevolezza che è in transizione, SGLang se i tuoi utenti fanno agenti o RAG complesso. Open WebUI può fare da frontend umano sopra tutto questo.

Vuoi scrivere articoli tecnici e che il modello cerchi fonti, legga pagine e generi bozze citate. Qui Unsloth Studio è la risposta più diretta, con web search e deep research nativi. In alternativa Open WebUI o Text Generation WebUI, ma con una configurazione più lunga alle spalle.

Hai una GPU NVIDIA e vuoi le massime performance in produzione. TensorRT-LLM o vLLM, a seconda che tu abbia già un'infrastruttura NVIDIA-native o preferisca uno stack più aperto.

Vuoi un'API uniforme sopra più backend. LocalAI fa esattamente questo, ed è la scelta naturale per ambienti eterogenei.

Ti interessa soprattutto il creative writing o lo storytelling. KoboldCPP è costruito per quello, con un sacco di opzioni di generazione pensate per la narrativa lunga.

Vuoi sperimentare con RAG, plugin e configurazioni avanzate senza limiti. Text Generation WebUI e Open WebUI ti danno la massima flessibilità, a costo di una UX meno curata e una configurazione più paziente.

La cosa onesta è che spesso è lo stesso sviluppatore a usare LM Studio per esplorare e llama.cpp quando deve produrre, o Ollama per il prototipo e vLLM quando va in produzione. Lo strumento non ha un'identità fissa, ha un lavoro.

## Dove sta andando

Tre segnali, in particolare, dicono molto su dove sta andando tutto questo. Il primo è la convergenza dei formati: GGUF è diventato lo standard de facto per i modelli locali, e il fatto che quasi tutti i client lo supportino significa che un modello scaricato oggi gira domani, su hardware diverso, senza frizioni. È la stessa logica che ha reso USB-C il connettore universale, anche se, a differenza di un connettore fisico, nessun formato software è davvero al riparo da rivoluzioni future.

Il secondo è la crescita di ambienti "agentici" locali. Unsloth Studio, SGLang, Open WebUI e altri stanno spostando il baricentro dal "far girare un modello" al "far fare qualcosa al modello", con web search, tool-use, RAG e agenti che lavorano sui tuoi documenti. È la differenza tra un motore che risponde e un assistente che agisce, la stessa distanza che separa un juke-box da un musicista capace di improvvisare.

Il terzo è l'integrazione sempre più stretta tra inferenza locale, web search, tool-use e RAG su documenti personali. Non sono più mondi separati: sono strati che si accumulano intorno al modello, e il client è ciò che li tiene insieme. La direzione sembra puntare verso un'orchestrazione di agenti locali multi-step, simili agli "operatori" cloud ma che restano sulla tua macchina, dove i dati non escono mai.

Le domande aperte restano molte. Quanto è sostenibile, nel tempo, l'hardware che hai oggi davanti a modelli che crescono più veloce di quanto l'efficienza riesca a tener loro dietro? Chi è responsabile della qualità di ciò che un agente estrae e inferisce, quando il collo di bottiglia non è più il modello ma la pipeline di ingest? E la più sottile: se ci fidiamo di un client che non vediamo dentro, stiamo dando più controllo o solo l'illusione di averlo mantenuto?

La risposta, come sempre, sta nell'uso. E nel sapere cosa c'è sotto il cofano, quando serve.