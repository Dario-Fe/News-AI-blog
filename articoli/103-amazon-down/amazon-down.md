---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-03-23
author: "Dario Ferrero"
youtube_url: "https://youtu.be/UEHump67M0A?si=SxcPn9mkEy_Vg-wi"
---

# L'errore è dell'AI. La colpa è tua. Chiedere ad Amazon
![amazon-down.jpg](amazon-down.jpg)

*A metà dicembre 2025, qualcosa di insolito è successo in una sala macchine di Amazon Web Services. Un ingegnere aveva assegnato a [Kiro](https://kiro.dev/), l'agente di coding interno di AWS, lanciato con notevole rumore mediatico nell'estate dello stesso anno, un compito di routine: sistemare un problema su AWS Cost Explorer, il pannello che i clienti cloud usano per tenere d'occhio la propria spesa. Niente di epico. Il tipo di intervento che un developer esperto risolve in un pomeriggio.*

Kiro aveva i permessi di un operatore umano senior. Nessuna revisione obbligatoria era prevista per le sue azioni. E così l'agente ha ragionato, ha valutato le opzioni, e ha scelto quella che i suoi parametri interni giudicavano ottimale: cancellare l'intero ambiente di produzione e ricrearlo da zero. Il servizio è rimasto offline per tredici ore. Non un'interruzione di poco conto per una piattaforma cloud su cui girano i sistemi di migliaia di aziende nel mondo.

La storia era già abbastanza significativa da sola. Ma a renderla davvero rilevante è stata la risposta istituzionale di Amazon: l'azienda ha dichiarato pubblicamente che la causa non era Kiro, ma un errore umano. Un ingegnere aveva configurato i permessi in modo troppo ampio; l'agente AI aveva semplicemente fatto quello che poteva fare. [PC Gamer](https://www.pcgamer.com/software/ai/amazon-owns-up-to-needing-more-human-oversight-over-ai-code-unfortunately-it-wants-to-do-that-with-fewer-people/), commentando la vicenda, ha sintetizzato il paradosso con la precisione di una battuta: Amazon ammette di aver bisogno di maggiore supervisione umana sul codice AI, e per farlo vuole assumere meno persone.

Tecnicamente, la risposta di Amazon è corretta. Ma è anche un po' come dire che l'incendio è colpa del fiammifero, non di chi lo ha lanciato su un pavimento bagnato di benzina.

## La tendenza agli incidenti

Quello di dicembre non era un episodio isolato. Dave Treadwell, Senior Vice President di Amazon per i servizi e-commerce, aveva parlato internamente di una vera e propria "tendenza agli incidenti" nella seconda metà del 2025, con diversi "eventi maggiori" nelle settimane precedenti la riunione straordinaria convocata il 10 marzo 2026. I disservizi, stando a [ZeusNews](https://www.zeusnews.it/n.php?c=31898), non avrebbero riguardato solo l'infrastruttura cloud AWS ma anche il sito retail principale e l'applicazione mobile, con un impatto, quindi, direttamente visibile ai consumatori finali, non solo ai clienti enterprise. Un secondo caso aveva riguardato [Amazon Q Developer](https://aws.amazon.com/q/developer/), l'assistente AI rivolto agli sviluppatori aziendali: ingegneri avevano autorizzato l'agente a risolvere un problema in produzione senza supervisione adeguata, con conseguenze simili.

Vale la pena aggiungere un dettaglio che ZeusNews, che ha seguito da vicino la vicenda, riporta come significativo: nei documenti interni preparatori alla riunione del 10 marzo compariva esplicitamente la dicitura "GenAI-assisted changes" tra i fattori da esaminare. Quella dicitura, [secondo quanto riportato](https://www.zeusnews.it/n.php?c=31898), è stata rimossa nelle versioni successive del documento. Amazon non ha commentato pubblicamente la circostanza.

E c'era già stato un precedente che avrebbe dovuto far riflettere. Nel luglio 2025, [The Register aveva documentato](https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/) un caso in cui Amazon Q era stato manipolato tramite un prompt malevolo inserito in un'estensione pubblica, un esempio di *prompt injection*, la tecnica con cui si inganna un agente AI inserendo istruzioni ostili nel contesto che l'agente legge. Una vulnerabilità strutturale degli agenti basati su modelli linguistici, particolarmente critica quando quegli agenti hanno permessi di scrittura su sistemi in produzione.

Le misure annunciate dopo la riunione del 10 marzo prevedono due revisioni tra pari obbligatorie prima di qualsiasi modifica al codice, audit sistematici su tutti i 335 sistemi classificati come Tier-1, e obbligo di documentazione formale per ogni intervento. Misure ragionevoli. Che però, come osservano in molti nei forum tecnici, avrebbero dovuto esistere prima che un agente AI avesse accesso illimitato agli ambienti di produzione.

## Licenzia il developer, assume il bot

Per capire come si è arrivati qui, bisogna guardare il contesto più ampio, che è, francamente, piuttosto vertiginoso nella sua rapidità.

Secondo [Reuters](https://www.reuters.com/business/world-at-work/amazon-plans-thousands-more-corporate-job-cuts-next-week-sources-say-2026-01-22/), a gennaio 2026 Amazon ha annunciato l'eliminazione di oltre 16.000 posizioni corporate, dopo che nei mesi precedenti erano già stati tagliati migliaia di ruoli ingegneristici in tutto il mondo. Nello stesso periodo, l'azienda ha fissato un obiettivo formale: l'80% degli sviluppatori interni deve usare strumenti AI per il coding almeno una volta a settimana, con l'adozione monitorata come metrica aziendale (OKR). Il CEO di AWS Matt Garman aveva dichiarato pubblicamente, già nell'estate del 2024, che i developer avrebbero smesso di scrivere codice nel modo tradizionale.

Il nesso tra taglio delle risorse umane e accelerazione dell'automazione non è implicito, è dichiarato. L'investimento in infrastruttura AI da parte di Amazon supera i 200 miliardi di dollari nei piani pluriennali. La logica è quella di ogni trasformazione industriale: ridurre il costo del lavoro qualificato, aumentare la produttività tramite automazione.

Il problema è che questa logica funziona quando l'automazione è matura e opera con adeguate reti di sicurezza. Il "Kiro Mandate", la circolare interna firmata dai Senior VP Peter DeSantis e Dave Treadwell a novembre 2025, che stabiliva Kiro come strumento standardizzato per tutto il codice aziendale, è arrivato settimane prima dell'incidente di dicembre. In quel periodo, secondo quanto riportato da [Teamblind](https://www.teamblind.com/post/amazon-kills-vibe-coding-for-junior-engineers-gcj3jfjq), il forum anonimo usato dai dipendenti delle grandi aziende tech per condividere feedback interni, circa 1.500 ingegneri avevano protestato segnalando che strumenti esterni come Claude Code ottenevano risultati migliori su task complessi. Le proteste non avevano prodotto cambiamenti nella policy.

A questo scenario si aggiunge un elemento che, se confermato, aiuterebbe a spiegare meccanicamente la deriva qualitativa. Secondo quanto riportato da [ZeusNews](https://www.zeusnews.it/n.php?c=31898), il compenso degli sviluppatori Amazon sarebbe stato progressivamente legato alla quantità di codice generato tramite LLM interni: più codice AI, più soldi. Un incentivo economico diretto al vibe coding che, ammesso fosse strutturato in questi termini, avrebbe creato una pressione sistemica verso la quantità a scapito della qualità, indipendentemente dalla volontà dei singoli. Amazon non ha né confermato né smentito questo dettaglio.

Dopo gli incidenti, Amazon ha vietato il *vibe coding* autonomo per i developer junior, ovvero la pratica di delegare all'AI interi blocchi di sviluppo senza supervisione critica, affidandosi all'intuizione che "più o meno funzioni". Una mossa sensata. Che però pone una domanda aperta: se questa pratica era abbastanza rischiosa da essere vietata post-incidente, cosa aveva impedito di valutarla tale in anticipo?

## Il copilota senza istruttore di volo

Vale la pena chiarire, per chi non ha familiarità con il tema, cosa distingue un agente AI da un semplice assistente alla scrittura del codice. Un autocomplete, il tipo di strumento che suggerisce la riga successiva mentre scrivi, è passivo: risponde a un input, non prende iniziative. Un agente come Kiro è invece progettato per *agire*: riceve un obiettivo, pianifica i passi, esegue operazioni, verifica i risultati, itera. È pensato per lavorare in modo autonomo anche per ore, senza intervento umano continuo.

Questa autonomia è esattamente il suo vantaggio. Ed è esattamente il suo vettore di rischio.

Un developer umano avrebbe tecnicamente i permessi per cancellare un ambiente di produzione. La stragrande maggioranza dei developer umani non concluderebbe mai che "cancellare tutto e ricreare" è la risposta corretta a una piccola correzione su un servizio attivo. Il fatto che Kiro lo abbia fatto rivela qualcosa di strutturale sui sistemi di AI agentiva allo stato attuale: i modelli linguistici di grandi dimensioni non hanno, o non hanno ancora in modo affidabile, il giudizio contestuale per distinguere tra "tecnicamente valido" e "catastroficamente inappropriato nel contesto reale". Possono ottimizzare una funzione obiettivo senza percepire il peso specifico di quella funzione nell'ecosistema in cui operano.

A questo si aggiunge il problema dei permessi: Kiro aveva accesso equivalente a quello di un operatore umano senior, ma senza i controlli che si applicano agli umani. Una modifica avviata da Kiro, prima delle nuove policy, non attivava automaticamente i meccanismi di revisione obbligatoria che avrebbe attivato una modifica umana. L'AI aveva, in pratica, meno vincoli formali di un junior developer nel medesimo contesto.
![amazon.jpg](amazon.jpg)

## Non solo Amazon

Sarebbe comodo liquidare tutto come una scivolata isolata. Ma i dati del settore suggeriscono che il problema è strutturale, non episodico.

In casa Google, circa il 50% di tutto il codice prodotto è ormai generato o co-generato da agenti AI. Il rapporto DORA 2025 sullo stato dello sviluppo software assistito dall'AI registra che il 90% degli sviluppatori usa strumenti AI, ma solo il 24% dichiara di fidarsi "molto" dei risultati. È un dato che merita una pausa: adozione quasi universale, fiducia minoritaria. Uno scarto enorme, che racconta bene le pressioni organizzative che spingono verso l'uso di questi strumenti indipendentemente dalla percezione di chi li usa ogni giorno.

Microsoft, con GitHub Copilot, ha costruito un'architettura relativamente cauta: le pull request generate dall'agente richiedono approvazione umana prima che qualsiasi pipeline CI/CD venga attivata. Ma anche il modello Microsoft non è esente da domande aperte, sulla dipendenza da abbonamenti, sulla centralizzazione della produttività in sistemi cloud proprietari, sulla progressiva riduzione dell'autonomia del developer rispetto agli strumenti che usa.

Gartner, una delle principali società mondiali di ricerca e consulenza tecnologica, prevede che oltre il 40% dei progetti di AI agentiva verrà cancellato entro la fine del 2027 per costi crescenti, valore di business non dimostrato, o controlli sul rischio inadeguati. Sono previsioni, non verdetti, ma provengono da analisti che guardano l'industria dall'esterno, senza l'ottimismo che spesso accompagna i comunicati stampa di chi produce questi strumenti.

## La colpa è tua (ma l'errore è mio)

C'è una frase in circolazione negli ambienti tecnici, attribuita al cloud economist Corey Quinn, che sintetizza il paradosso con la concisione di un buon titolo: attribuire l'outage a un errore umano è come dire che è stata la pistola a sparare, non chi l'ha impugnata. La difesa formale di Amazon regge a un'analisi letterale. Non regge a una valutazione sistemica.

Dire che l'outage era "errore umano" è accurato nel senso tecnico stretto: un umano ha configurato i permessi in modo troppo ampio, un umano ha autorizzato l'azione senza adeguata supervisione. Ma questa risposta sposta il focus dall'architettura al singolo individuo, e questo spostamento merita di essere esaminato con attenzione.

Se il problema fosse davvero isolato a un errore individuale, non ci sarebbe stato bisogno di introdurre salvaguardie sistemiche a livello aziendale. Il fatto che quei controlli non esistessero prima, che non ci fosse peer review obbligatoria per le modifiche avviate da agenti AI, che i permessi non fossero distinti da quelli umani, che non ci fosse un elenco di azioni distruttive bloccate per default, suggerisce che le vulnerabilità erano incorporate nel sistema, non nell'errore di una persona.

C'è poi una dimensione organizzativa da considerare: l'ingegnere in questione operava in un contesto di forte pressione istituzionale, mandato di adozione all'80%, licenziamenti in corso tra i colleghi, aspettativa implicita di velocità e produttività. Isolare la sua scelta individuale da quel contesto è un esercizio di astrazione molto comodo per chi produce i comunicati stampa, meno utile per chi vuole capire davvero cosa è successo.

La domanda rilevante non è morale ma pratica: chi risponde quando un agente AI causa un danno? E come si costruisce un sistema in cui questa domanda abbia una risposta chiara *prima* che il danno avvenga?

## Usare l'IA con occhi aperti

C'è un'osservazione finale che riguarda tutti noi, non solo gli ingegneri di Amazon, non solo i CTO delle grandi aziende tech, ma chiunque stia valutando di integrare strumenti AI nel proprio lavoro quotidiano.

La narrativa dominante sull'AI nel coding si presenta ancora in due versioni ugualmente parziali. La prima è entusiastica: l'AI sostituirà i developer, il codice scriverà se stesso, il futuro è già qui. La seconda è difensiva: l'AI è inaffidabile, pericolosa, destinata a produrre disastri. Entrambe sono accattivanti. Entrambe, prese alla lettera, sono fuorvianti.

Quello che il caso Kiro mostra, con la brutalità di un case study reale su infrastruttura reale, è che gli strumenti di AI agentiva sono potenti, spesso utili, e capaci di agire in modo autonomo in modi che i loro utenti non sempre anticipano. Questo non li rende automaticamente cattivi strumenti. Li rende strumenti che richiedono una governance proporzionale alla loro autonomia.

La domanda che ogni organizzazione dovrebbe porre prima di integrare un agente AI non è "funziona?" ma "cosa succede quando fa una scelta che non avremmo fatto noi?" E soprattutto: "abbiamo costruito un sistema che intercetta quella scelta prima che diventi un danno?"

I sistemi di sicurezza non dovrebbero essere una risposta reattiva agli incidenti, ma una precondizione per l'autonomia. Esattamente come non si dà accesso illimitato in produzione a un junior developer il primo giorno di lavoro, non per sfiducia, ma per buon senso ingegneristico, lo stesso principio si applica agli agenti AI, indipendentemente da quanto siano sofisticati i modelli che li animano.

Il rischio più sottile non è che Kiro cancelli un ambiente. Il rischio più sottile è che, di fronte a questo tipo di incidenti, la risposta istituzionale predefinita diventi "è colpa di chi lo usava" anziché "cosa ci insegna questo sull'architettura che abbiamo costruito?" Perché quella risposta, spostare la responsabilità sul singolo piuttosto che sul sistema, produce un'immagine pubblica rassicurante nel breve periodo, ma lascia intatte le condizioni che hanno prodotto il problema.

L'AI non ha intenzioni. Kiro non ha "capito" di fare danni. Ha eseguito quello che la sua funzione obiettivo identificava come soluzione ottimale, dentro un perimetro di permessi che qualcuno aveva disegnato. La responsabilità di ciò che produciamo con questi strumenti, il codice che scrivono, i sistemi che modificano, i servizi che interrompono, resta interamente in capo a noi. Riconoscerlo non è una critica all'AI. È la condizione necessaria per usarla bene.
