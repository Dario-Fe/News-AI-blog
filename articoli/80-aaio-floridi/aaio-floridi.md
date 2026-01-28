---
tags: ["Research", "Ethics & Society", "Business"]
date: 2026-01-28
author: "Dario Ferrero"
youtube_url: "https://youtu.be/knPuBzfPLMw?si=2MMoIIH8zodt2N2M"
---

# Quando gli Agenti imparano a navigare: benvenuti nell'era dell'AAIO
![aaio-floridi.jpg](aaio-floridi.jpg)

*Immaginate un mondo dove il vostro sito web non viene visitato solo da esseri umani annoiati durante la pausa caffè, ma anche da agenti di intelligenza artificiale che navigano autonomamente, prendono decisioni e completano transazioni senza che nessun dito umano sfiori un mouse. Benvenuti nel 2026, dove questo scenario non è più fantascienza ma realtà quotidiana. E proprio come negli anni Novanta i webmaster si sono dovuti adattare agli spider di Google, oggi ci troviamo di fronte a una nuova rivoluzione: quella dell'Agentic AI Optimisation.*

A guidarci in questo nuovo territorio è [Luciano Floridi](https://dec.yale.edu/people/luciano-floridi), filosofo romano trapiantato a Yale dove dirige il Digital Ethics Center. Classe 1964, Floridi non è il classico accademico rinchiuso nella torre d'avorio. Dopo una formazione classicista a Roma La Sapienza, ha attraversato l'epistemologia a Warwick e Oxford, per poi dedicarsi a quello che oggi chiamiamo filosofia dell'informazione. Il governo italiano gli ha conferito il titolo di Cavaliere di Gran Croce, il massimo riconoscimento nazionale, e non a caso: Floridi ha lavorato come consulente etico per Google, ha collaborato con la Commissione Europea sull'intelligenza artificiale e ha contribuito a plasmare il dibattito globale sull'etica digitale.

Nel [paper](https://arxiv.org/abs/2504.12482) pubblicato ad aprile 2025 insieme a un team del Digital Ethics Center (Carlotta Buttaboni, Emmie Hine, Jessica Morley, Claudio Novelli e Tyler Schroder), introduce formalmente il concetto di Agentic AI Optimisation. Se la Search Engine Optimization (SEO) ha definito come strutturiamo i contenuti per gli algoritmi di ricerca, AAIO rappresenta l'evoluzione necessaria per un'era dove l'AI non si limita a rispondere a query ma agisce autonomamente.

## Cosa rende un'AI "agentica"

Prima di addentrarci nell'ottimizzazione, dobbiamo capire cosa distingue un sistema di intelligenza artificiale agentica dai suoi predecessori. Floridi e il suo team individuano tre caratteristiche fondamentali: autonomia nell'iniziare azioni senza istruzioni esplicite, capacità decisionale basata sul contesto e adattabilità dinamica agli ambienti digitali.

Non stiamo parlando di chatbot glorificati o di assistenti vocali che eseguono comandi predefiniti. Un sistema AAI può, per esempio, navigare un sito di e-commerce, confrontare prodotti secondo criteri complessi, verificare la disponibilità in tempo reale, e completare un acquisto ottimizzando per variabili multiple come prezzo, tempi di consegna e sostenibilità del venditore. Il tutto senza che un umano abbia specificato ogni singolo passaggio.

Come scrive Floridi nel paper, il successo di questi sistemi non dipende dalla loro intelligenza (che tecnicamente non possiedono) ma da quanto bene l'ambiente digitale è strutturato attorno alla loro "agency senza intelligenza". Qui entra in gioco AAIO.

## Dall'ottimizzazione per umani all'ottimizzazione per agenti

La SEO tradizionale si è costruita attorno a un'architettura pensata per esseri umani che navigano tramite browser. Titoli accattivanti, meta description persuasive, velocità di caricamento percepita, design responsive: tutto ruota attorno all'esperienza utente umana. AAIO condivide alcuni di questi principi fondamentali (structured data, metadata, accessibilità dei contenuti) ma li estende e li trasforma per soddisfare le esigenze operative degli agenti autonomi.

Un esempio concreto: mentre per un umano un pulsante ben visibile con scritto "Acquista ora" è sufficiente, un agente AI ha bisogno di markup strutturato che identifichi inequivocabilmente quell'elemento come azione transazionale, con tutte le informazioni collaterali (prezzo finale, tasse incluse, termini di reso) in formati machine-readable come JSON-LD o RDFa basato su [Schema.org](https://schema.org).

Il paper di Floridi identifica quattro pilastri tecnici dell'AAIO. Il primo è l'implementazione di dati strutturati avanzati che vanno oltre il basic markup SEO, fornendo contesto completo per ogni entità e relazione nel sito. Il secondo riguarda l'ottimizzazione dell'architettura informativa: gerarchie chiare, navigazione logica, endpoint API ben documentati. Il terzo è l'accessibilità semantica, che significa fornire alternative testuali, descrizioni dettagliate e metadata contestuali per ogni elemento multimediale. Il quarto è l'ottimizzazione del contenuto stesso attraverso aggiornamenti regolari, targeting preciso dell'intento (non più solo umano ma anche agentico) e analytics basate su AI per miglioramenti continui.

## Il galateo dei robot: gestire l'accesso degli agenti

Una questione pratica immediata è: come controlliamo quali agenti AI possono accedere ai nostri contenuti? La risposta passa per evoluzioni del classico file robots.txt. Mentre questo strumento è nato per dire agli spider dei motori di ricerca dove possono andare, oggi dobbiamo confrontarci con user-agent specifici come GPTBot di OpenAI, ClaudeBot di Anthropic, o Google-Extended per i modelli di Google.

Ogni agente si presenta con una stringa identificativa unica nelle richieste HTTP. Un webmaster può decidere di consentire l'accesso a tutti, bloccare selettivamente alcuni agenti, o implementare whitelist stringenti. Floridi nota nel paper che alcuni siti stanno adottando file LLMs.txt, una proposta che raccoglie tutto il contenuto del sito in un unico documento testuale ottimizzato per l'analisi da parte di Large Language Models.

La questione non è solo tecnica ma economica e strategica. Se un agente AI può navigare, estrarre informazioni e completare transazioni autonomamente, chi beneficia dell'engagement? Chi paga per l'hosting? Chi raccoglie i dati comportamentali preziosi per il marketing? Sono domande che ricordano i primi dibattiti su web scraping e copyright, ma con implicazioni più profonde.

## L'industria si muove: AgentKit, MCP e la corsa agli standard

Mentre Floridi e il suo team propongo regole, i giganti tech costruiscono. OpenAI ha trasformato il suo framework sperimentale Swarm in [AgentKit](https://openai.com/index/introducing-agentkit/), una suite completa per costruire, deployare e ottimizzare agenti autonomi. Lanciato nell'ottobre 2025, AgentKit include un Agent Builder visuale per comporre workflow multi-agente, un Connector Registry centralizzato per gestire integrazioni dati, e ChatKit per embedding interfacce conversazionali. Aziende come Klarna hanno costruito agenti di supporto che gestiscono due terzi dei ticket usando questi strumenti, mentre Clay ha decuplicato la crescita con agenti sales automatizzati.

Ma la vera rivoluzione potrebbe venire da uno standard aperto. Anthropic ha rilasciato il [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), un protocollo universale per connettere sistemi AI a fonti dati esterne. Pensate a MCP come a una USB-C per applicazioni AI: un'interfaccia standardizzata che elimina la necessità di integrazioni custom per ogni combinazione di modello e sistema esterno. Dal lancio a novembre 2024, la community ha costruito migliaia di server MCP, con SDK disponibili per tutti i linguaggi principali e oltre 97 milioni di download mensili tra Python e TypeScript.

L'importanza strategica di MCP è tale che nel gennaio 2025 Anthropic lo ha donato all'[Agentic AI Foundation](https://aitalk.it/it/agentic-ai-foundation.html), un directed fund sotto la Linux Foundation co-fondato da Anthropic, Block e OpenAI, con supporto di Google, Microsoft, AWS, Cloudflare e Bloomberg. Questa mossa trasforma MCP da protocollo proprietario a standard industriale neutrale, accelerando potenzialmente l'adozione di AAIO su scala globale.
![schema-aaio.jpg](schema-aaio.jpg)
[Immagine tratta da arxiv.org](https://arxiv.org/abs/2504.12482)

## Il circolo virtuoso (o vizioso)

Il paper introduce un concetto affascinante: la relazione simbiotica tra ottimizzazione delle piattaforme e performance dell'AI. Più siti implementano AAIO, migliori diventano le performance degli agenti AI. Agenti più efficaci incentivano ulteriori piattaforme a ottimizzare. Questo circolo virtuoso ricorda l'evoluzione della SEO, dove siti ben ottimizzati miglioravano Google, che a sua volta premiava l'ottimizzazione con ranking superiori.

Ma c'è una differenza cruciale. Con la SEO, il beneficio era reciproco ma asimmetrico: Google guadagnava dati e traffico, i siti guadagnavano visibilità. Con AAIO, la dinamica è più complessa. Se un agente AI completa una transazione su un sito e-commerce ottimizzato, chi cattura il valore della relazione con il cliente? L'agente sa che l'utente ha preferenze specifiche, ha tracciato il comportamento d'acquisto, ha raccolto feedback. Questi dati comportamentali, tradizionalmente oro puro per i marketer, ora fluiscono verso chi controlla l'agente.

Floridi e il suo team sollevano interrogativi cruciali: chi rimane escluso da questo circolo? L'implementazione di AAIO richiede competenze tecniche, risorse e accesso a documentazione che non tutti possiedono. Piccole imprese, organizzazioni no profit, creatori di contenuti indipendenti potrebbero trovarsi marginalizzati in un ecosistema digitale sempre più ottimizzato per giganti tecnologici che possono permettersi team dedicati all'AAIO.

Questa digital divide non è accidentale ma strutturale. Come scrivono gli autori, esiste il rischio concreto che AAIO amplifichi le disuguaglianze esistenti nell'accesso ai benefici dell'economia digitale. È la stessa dinamica che abbiamo visto con l'advertising programmatico, dove chi aveva risorse per ottimizzare in tempo reale ha dominato, lasciando indietro chi non poteva permettersi infrastrutture sofisticate.

## Le implicazioni GELSI: governance, etica, legge e società

La sezione più densa e interessante del paper affronta le implicazioni GELSI (Governance, Ethical, Legal, and Social Implications), termine che Floridi ha contribuito a popolarizzare negli studi di etica tecnologica.

Sul fronte della governance, la domanda fondamentale è: chi dovrebbe sviluppare gli standard AAIO? Un processo organico guidato dall'industria, come è successo per molti standard web? O un approccio multi-stakeholder che includa regolatori, accademici, società civile e utenti finali? La storia della SEO suggerisce che gli standard emersi dal basso tendono a favorire chi già detiene potere tecnologico ed economico.

Le questioni etiche sono ancora più spinose. Quando un agente AI autonomo commette un errore basandosi su contenuti ottimizzati AAIO, chi ne porta la responsabilità? Il proprietario del sito che ha fornito dati strutturati errati? Lo sviluppatore dell'agente che non ha validato adeguatamente le informazioni? L'utente finale che ha delegato la decisione all'AI?

Floridi sottolinea che i framework etici attuali non sono preparati per scenari dove l'agency è distribuita tra umani, algoritmi e infrastrutture digitali. Il concetto di "agency senza intelligenza" che ha sviluppato in [lavori precedenti](https://www.researchgate.net/publication/389450555_AI_as_Agency_without_Intelligence_On_Artificial_Intelligence_as_a_New_Form_of_Artificial_Agency_and_the_Multiple_Realisability_of_Agency_Thesis) diventa particolarmente rilevante: questi sistemi agiscono senza comprendere, decidono senza giudicare, influenzano senza intenzionalità.

Sul versante legale, il paper evidenzia tensioni immediate con il GDPR europeo. Se un agente AI raccoglie e processa dati personali navigando siti ottimizzati AAIO, chi è il data controller? Le attuali categorie legali di "raccolta dati" presuppongono intenzionalità umana diretta. Ma in scenari dove un agente opera autonomamente seguendo obiettivi di alto livello, la catena di responsabilità si frantuma.

C'è poi la questione dell'AI Act europeo, entrato in vigore nel 2024. Questo framework regolatorio è stato progettato prima che l'AI agentica diventasse mainstream, e fatica a classificare questi sistemi. Sono strumenti? Sono autonomi? Richiedono supervisione umana continua o possono operare indipendentemente? Floridi nota che l'ambiguità regolatoria potrebbe rallentare l'adozione benefica dell'AI agentica, ma anche aprire spazi per abusi in giurisdizioni meno rigorose.

## I rischi concreti: manipolazione, bias e sorveglianza

Il paper non si limita a speculazioni filosofiche ma identifica rischi tangibili e attuali. Il primo è la manipolazione: siti ottimizzati AAIO potrebbero essere progettati per influenzare subdolamente le decisioni degli agenti AI, un po' come le dark patterns fanno con gli umani, ma con maggiore efficacia dato che gli agenti non hanno scetticismo innato.

Il secondo riguarda l'amplificazione dei bias. Se i dataset su cui vengono addestrati gli agenti AI riflettono già pregiudizi sistemici, e se i siti ottimizzati AAIO rafforzano certi pattern informativi a scapito di altri, il risultato è un circolo di feedback che solidifica le discriminazioni esistenti. Floridi cita esplicitamente il [lavoro di Virginia Eubanks](https://www.wired.it/attualita/tech/2019/03/11/algoritmi-discriminazione-welfare/) su come i sistemi automatizzati amplifichino le disuguaglianze.

Il terzo rischio è la sorveglianza. Ogni interazione tra agente AI e sito ottimizzato AAIO genera dati granulari su comportamenti, preferenze e pattern decisionali. Chi controlla questi dati? Come vengono monetizzati? Quali protezioni esistono contro l'abuso?

## Cosa serve fare ora

Nella sezione conclusiva, Floridi e il suo team propongono direzioni concrete. Sul piano tecnico, serve urgentemente lo sviluppo di standard aperti e interoperabili per AAIO, gestiti da consorzi multi-stakeholder piuttosto che da singole corporation. Sul piano regolatorio, i legislatori devono aggiornare framework come il GDPR e l'AI Act per contemplare esplicitamente l'agency distribuita e le interazioni autonome.

Sul versante educativo, c'è bisogno di formare una nuova generazione di professionisti che comprendano tanto gli aspetti tecnici di AAIO quanto le implicazioni etiche e sociali. Non basta sapere implementare JSON-LD; bisogna capire come quelle scelte tecniche influenzano chi avrà accesso ai benefici dell'economia agentica e chi ne resterà escluso.

Il paper si chiude con un richiamo alla proattività. Come ha sottolinea Floridi in altre occasioni: "Il modo migliore per prendere il treno della tecnologia non è inseguirlo, ma essere alla stazione successiva", dobbiamo affrontare le implicazioni GELSI di AAIO ora, prima che i pattern diventino cementificati in infrastrutture difficili da modificare.

L'era dell'AI agentica non è un futuro ipotetico ma un presente in evoluzione rapida. AAIO non è una tecnologia che possiamo permetterci di ignorare o relegare ai soli dipartimenti IT. È una questione che riguarda l'architettura stessa del nostro ecosistema digitale, con ramificazioni che toccano economia, democrazia, equità sociale e diritti individuali.

La domanda non è se dobbiamo ottimizzare per gli agenti AI, ma come farlo in modo che questa ottimizzazione serva l'interesse collettivo e non solo quello di chi già detiene potere tecnologico. È una sfida che richiede, come sempre nel lavoro di Floridi, di pensare filosoficamente alla tecnologia prima che la tecnologia pensi per noi.