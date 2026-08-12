---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-05-20
author: "Dario Ferrero"
---

# Qwen 3.6 lokal: 35 Milliarden auf meinem PC
![qwen36-35b-ai.jpg](qwen36-35b-ai.jpg)

*Es gibt in jeder Versuchsreihe einen Moment, in dem man erkennt, dass nicht mehr das Testobjekt das Problem ist, sondern die Qualität des Messinstruments. Ich sammelte gerade die Ergebnisse des achten Tests und dachte, dass vielleicht meine Tests zur Grenze geworden sind: fünf von fünf, acht von acht Mal. Funktioniert das Thermometer noch, oder hat das Wasser aufgehört, seine Temperatur zu ändern?*

Die Frage ist nicht rhetorisch gemeint. Diese Artikel entstehen als Logbuch eines Heimlaboratoriums, nicht als akademisches Whitepaper, und die Methode bleibt bewusst persönlich: keine automatisierten Benchmarks, keine standardisierten Metriken, sondern nur auf realistische Szenarien kalibrierte Prompts und das haptische Gefühl dessen, der das Werkzeug benutzt und dann davon berichtet. Die Hardware hat sich gegenüber den vorangegangenen Folgen nicht geändert (AMD Ryzen 7700, 32 GB RAM, AMD GPU mit 16 GB VRAM) und die Software ebenso wenig: [LM Studio](https://lmstudio.ai/), die zugänglichste Lösung für alle, die lokale Modelle ausführen möchten, ohne einen Nachmittag mit Terminalkonfigurationen zu verschwenden. Für alle Details zur Installation, zum Ökosystem und zur Philosophie dieses Labors verweise ich auf die [erste Folge der Serie über Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), die weiterhin der methodische Referenzpunkt für die gesamte Serie bleibt. Wer bereits an Bord ist, kann hier fortfahren.

Der heutige Protagonist unterscheidet sich von den anderen. Nicht durch die Kategorie, sondern durch die Größe: [Qwen3.6 35B A3B in Q6-Quantisierung](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), das größte Modell, das ich jemals auf dieser Maschine geladen habe – buchstäblich an der Grenze dessen, was die Konfiguration bewältigen kann. Nachdem ich [Qwen 3.5 9B in den ersten beiden Folgen](https://aitalk.it/it/qwen3.5-locale-puntata2.html) und [Gemma 4 26B MoE](https://aitalk.it/it/gemma4-26b.html) in der dritten erkundet hatte, war dieser Skalensprung unvermeidlich. Und es ist genau der Sprung, den ich machen wollte.

## Fünfunddreißig Milliarden, drei auf einmal

Hinter dem Namen verbirgt sich eine Architektur, die es zu verstehen lohnt, da sie die Art und Weise, wie man über Hardwareanforderungen nachdenkt, radikal verändert. Qwen3.6 35B A3B ist ein Mixture-of-Experts-Modell: Es verfügt über insgesamt 35 Milliarden Parameter, aktiviert aber für jedes generierte Token nur etwa 3 Milliarden davon. Nicht alle Experten werden jedes Mal zur Antwort gerufen, sondern nur diejenigen, die für dieses spezifische Textfragment als am kompetentesten erachtet werden. Es ist ein bisschen so, als hätte man ein Orchester aus zweihundertsechsundfünfzig Musikern, bei dem der Dirigent von Fall zu Fall entscheidet, welche acht Instrumentalisten spielen sollen, während die anderen zuhören und bereitstehen. Das praktische Ergebnis ist, dass die Rechenkosten eher denen eines Drei-Milliarden-Modells als denen eines Fünfunddreißig-Milliarden-Modells ähneln, während bei Bedarf dennoch auf die Tiefe des Letzteren zurückgegriffen wird.

Qwen3.6, im [offiziellen Alibaba-Blog](https://qwen.ai/blog?id=qwen3.6) als Weiterentwicklung der Qwen3-Architektur beschrieben, bringt vier Neuerungen mit, die das Team besonders hervorheben wollte: eine Verbesserung von 43 % bei QwenWebBench in Bezug auf agentische Codegenerierung und die Erstellung kompletter Webanwendungen, eine Funktion namens *Thinking Preservation*, um die Konsistenz der Argumentation über Multi-Turn-Gespräche hinweg aufrechtzuerhalten, einen Sprung im multimodalen Verständnis von Bildern und Dokumenten sowie native Unterstützung für Videoverständnis – letzteres ist noch experimentell und wird nicht von allen verfügbaren Runtimes unterstützt.

Die Q6-Quantisierung, mit der ich gearbeitet habe, stellt einen vernünftigen Kompromiss dar: weniger ressourcenintensiv als reines F16, aber viel originalgetreuer als aggressive Quantisierungen wie Q4. In der Praxis geht im Vergleich zu den vollen Gewichten nur sehr wenig Qualität verloren, wobei ein Speicherpreis gezahlt wird, der bei meiner Konfiguration ein sorgfältiges Ausbalancieren zwischen GPU und System-RAM erforderte.

## Die Konfiguration am Limit

Hier liegt das eigentliche Experiment. Ich habe nicht nach dem Punkt maximaler Performance gesucht: Ich habe bewusst den Rand des Möglichen gesucht, um zu verstehen, was passiert, wenn man mit dem – zumindest meiner Meinung nach – akzeptablen Minimum an Performance arbeitet.

Die gewählten Parameter: Kontext bei 8078 Token (das Modell beherrscht nativ über 262.000), GPU-Offload von 8 Layern von insgesamt 43, 8 aktive Experten von 256 verfügbaren, intern F16-Quantisierung für die Layer in der GPU. Die resultierende Geschwindigkeit pendelte sich bei etwa 11 Token pro Sekunde ein, verglichen mit den 20-25, die Qwen 3.5 9B bequem erreichte. Das ist keine Geschwindigkeit, die ich für einen Konversationsassistenten für den schnellen Gebrauch empfehlen würde, aber sie ist für strukturierte Arbeitssitzungen, bei denen man es nicht eilig hat und die Tiefe der Antwort im Vordergrund steht, absolut akzeptabel.

Die Frage, die dem gesamten Experiment zugrunde liegt, ist simpel: Ist das Opfer an Geschwindigkeit die gewonnene Qualität wert? Die folgenden Tests sind die Antwort.

## Einen Schritt weiter: die optimale Konfiguration

Die Entscheidung, mit 8 Layern in der GPU und reduziertem Kontext zu beginnen, war bewusst getroffen: Ich wollte das Modell unter Bedingungen realer Ressourcenknappheit testen, am unteren Ende des akzeptablen Bereichs. Aber nachdem die Testreihe abgeschlossen war, wollte ich verstehen, wo der wahre Gleichgewichtspunkt auf dieser Hardware liegt.

Die Ergebnisse waren aufschlussreich. Das Erhöhen der Layer in der GPU von 8 auf 16 lässt die Geschwindigkeit von 11 auf etwa 14,5 Token pro Sekunde steigen – ein spürbarer Gewinn. Überraschenderweise ändert eine weitere Verdoppelung auf 32 fast nichts (14,49 Tok/s), und der Versuch, 40 Layer zu laden, verhindert den Start des Modells komplett: Der VRAM reicht nicht aus. Der optimale Punkt für diese Hardware liegt also bei 16 Layern, nicht mehr.

Ebenso interessant ist das Verhalten des Kontexts: Eine Erweiterung von 8.000 Token auf das native Maximum von 262.000 wirkt sich kaum auf die Geschwindigkeit aus, mit einem Rückgang von weniger als einem Token pro Sekunde zwischen den beiden Extremen. In der Praxis kann man das Kontextfenster je nach Aufgabe wählen, ohne sich um die Performance sorgen zu müssen.

Der Parameter, der hingegen wirklich den Unterschied macht, ist die Anzahl der aktiven Experten. Mit 4 Experten steigt die Rate auf 16,2 Tok/s, mit 8 liegt sie bei 14,2, mit 16 sinkt sie auf 11,4 und bei 125 bricht sie auf 2,9 ein. Es besteht eine fast lineare Beziehung nach unten: Jeder zusätzliche Experte kostet Ressourcen, und auf Consumer-Hardware ist dieser Preis sofort spürbar.

Alle Tests mit unterschiedlichen Konfigurationen lieferten dennoch Antworten von exzellenter Qualität, was darauf hindeutet, dass die Reduzierung der aktiven Experten die Qualität nicht spürbar beeinträchtigt – zumindest bei den in dieser Serie verwendeten Aufgaben.

Die Konfiguration mit dem besten Kompromiss auf dieser Hardware ist somit: 16 Layer in der GPU, 125.000 Token Kontext, 8 aktive Experten bei einer Geschwindigkeit von etwa 14,2 Token pro Sekunde. Das ist nicht die Geschwindigkeit eines kleinen Modells, aber ein Fortschritt gegenüber der „Grenzkonfiguration“, die in den Haupttests verwendet wurde, und ermöglicht Arbeitssitzungen an langen Dokumenten, ohne auf Qualität verzichten zu müssen.
![grafico1.jpg](grafico1.jpg)
[Bild der Benchmark-Ergebnisse von qwen.ai](https://qwen.ai/blog?id=qwen3.6)

## Die Tests

### Test 1 — Higgs-Mechanismus und Teilchenphysik *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 11,17 Token/s*

Die Antwort war außergewöhnlich, wahrscheinlich die beste, die ich je von einem lokalen Modell zu einem komplexen wissenschaftlichen Thema erhalten habe. Das Modell begann mit dem theoretischen Kontext und beschrieb die Eichsymmetrie, welche die elektroschwachen Wechselwirkungen steuert. Dann führte es das Higgs-Feld und sein berühmtes „mexikanisches Hut“-Potenzial ein und erklärte, warum der Nullpunkt nicht das Energieminimum ist. Es zeigte auf, wie der Vakuumerwartungswert mit den Eichbosonen interagiert und den W- und Z-Bosonen Masse verleiht. Und es klärte das subtilste Detail, das oft selbst in universitären Abhandlungen fehlt: warum das Photon masselos bleibt, dank einer Restsymmetrie, welche das Higgs-Vakuum nicht zu brechen vermag.

Die Struktur der Antwort war tadellos, organisiert in logische Abschnitte, die vom Allgemeinen zum Besonderen fortschritten, ohne jemals den Faden zu verlieren. Die Sprache war präzise, aber zugänglich, wobei Metaphern wie der „mexikanische Hut“ verwendet wurden, um abstrakte Konzepte intuitiv fassbar zu machen. Ich fand keine Fehler, weder in den physikalischen Konzepten noch in den mathematischen Details. Die Geschwindigkeit von 11 Token pro Sekunde ist niedriger als bei den zuvor getesteten kleineren Modellen, aber die Qualität dieser Antwort rechtfertigt den Kompromiss bei Weitem. Die Geduld, ein paar Sekunden länger zu warten, wurde mit einer Erklärung belohnt, die man als lehrbuchreif bezeichnen könnte.

### Test 2 — Multimodalität und Verständnis von Tabellen *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 10,49 Token/s*

Das hochgeladene Bild war absichtlich von geringer Qualität: ein kleiner Screenshot einer Rechnungsverwaltungsoberfläche, unvollkommen, um die visuellen Fähigkeiten unter realistischen, nicht idealen Bedingungen zu testen. Das Modell bestand den Test mit überraschenden Ergebnissen.

Zuerst beeindruckte die Fähigkeit, die allgemeine Struktur der Benutzeroberfläche zu erfassen. Das Modell identifizierte korrekt die drei Hauptbereiche: das Filterpanel oben, die seitliche Produktliste rechts und die zentrale Tabelle. Es erkannte, dass es sich wahrscheinlich um eine Buchhaltungsanwendung handelte, und vermutete angesichts der generischen Namen von Kunden und Artikeln sogar, dass es sich um eine Beispieldatenbank oder eine Testumgebung handeln könnte.

Das Auslesen der Daten war präzise und detailliert: Alle Spalten der Tabelle wurden korrekt aufgezählt, der feste Mehrwertsteuersatz von 22 % wurde als Konstante in allen Zeilen erkannt, die gelb markierte Spalte „Betrag“ wurde als Navigationselement für den Benutzer identifiziert und die Rechnungsdaten dem Zeitraum Januar bis März 2022 zugeordnet. Der wertvollste Teil war jedoch die Analyse der Anomalien: Obwohl der obere Filter die Option „ZU ZAHLEN“ als ausgewählt anzeigte, wiesen die Rechnungen in der Tabelle bereits ein Zahlungsdatum und einen beglichenen Betrag auf. Das Modell wies auf den möglichen Datenmix hin und formulierte vernünftige Hypothesen zum Nutzungskontext. Ein kleineres Modell hätte eine generische Beschreibung geliefert. Hier erhielt ich eine echte Analyse inklusive Interpretation der Inkonsistenzen.

### Test 3 — Generierung von komplexem Code *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 10,06 Token/s*

Dieser Test war einer der wichtigsten der gesamten Reihe, da Qwen3.6 eine Verbesserung von 43 % bei QwenWebBench gerade bei der Codegenerierung verspricht. Ich wollte sehen, ob sich dieses Versprechen in einer konkreten und funktionierenden Implementierung eines nicht trivialen algorithmischen Problems niederschlägt: dem Finden des Zyklus mit der maximalen Länge in einem ungerichteten Graphen.

Die Antwort war vollauf überzeugend. Das Modell begann mit einer theoretischen Prämisse, die nur wenige Programmierassistenten in dieser Reife bieten: Es erklärte explizit, dass das Problem NP-schwer ist, dass es keinen polynomiellen Algorithmus zur Lösung für generische Graphen gibt und dass jede exakte Lösung im schlimmsten Fall eine exponentielle Komplexität aufweisen wird. Dieses Bewusstsein ist selten und wertvoll, da es zeigt, dass das Modell nicht versucht, eine magische Lösung zu verkaufen, sondern die Grenzen des Fachgebiets zutiefst versteht.

Die vorgeschlagene Implementierung war elegant und funktionsfähig: DFS-Strategie mit Pfadverfolgung, Datenstruktur mit einer Depth-Map zum Erkennen von Back-Edges und zur Berechnung der Zykluslänge in konstanter Zeit, effiziente Graphenrepräsentation über eine Adjazenzliste, korrekt implementiertes Backtracking und vollständige Behandlung von Grenzfällen wie zyklenfreien Graphen und unzusammenhängenden Komponenten. Besonders gut gefiel mir die Verwendung der Depth-Map, die eleganter und performanter ist als eine einfache lineare Suche im Pfad, da sie die Berechnung der Zykluslänge ermöglicht, ohne die gesamte Liste zu scannen. Die Erklärung der Zeitkomplexität war klar und ehrlich, mit einer Unterscheidung zwischen dem günstigen und dem schlimmsten Fall. Keine syntaktischen oder logischen Fehler, Type-Hints vorhanden, modulare Struktur. Ein Code, den man so abgeben könnte.

### Test 4 — Mehrsprachigkeit und Planung *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 11,15 Token/s*

*Methodischer Hinweis: In einem sauberen Chat ausgeführt, nachdem ein erster Durchlauf in einem Chat mit Verlauf mittelmäßige Ergebnisse geliefert hatte.*

Dieser Test lehrte schon vor dem eigentlichen Ergebnis etwas Wichtiges. Der erste Durchlauf in einem Chat mit vorangegangenen Interaktionen zu anderen Themen hatte zu Unterbrechungen und mittelmäßiger Qualität geführt. In einem komplett neuen Chat wiederholt, war das Ergebnis wie verwandelt. Der Unterschied war so deutlich, dass er einen permanenten methodischen Hinweis verdient: Der Chatverlauf kann, selbst wenn er harmlos erscheint, Ergebnisse bei komplexen Aufgaben erheblich verändern. Das Testen in einem sauberen Chat ist keine Marotte, sondern experimentelle Hygiene.

In einem sauberen Chat erstellte Qwen3.6 beim ersten Versuch einen vollständigen und detaillierten Fünf-Tage-Reiseplan für Tokio auf Französisch. Das Französisch war auf muttersprachlichem Niveau: „spécialités de rue“, „ambiance vieux Tokyo“, „cadre apaisant“, „ruelle atmosphérique“, „patrimoine UNESCO“. Keine grammatikalischen oder syntaktischen Fehler, flüssiger Ausdruck auf fortgeschrittenem Niveau.

Die Reiseroute war logistisch perfekt, mit einer ausgewogenen Mischung aus Tempeln und Street Food, und gespickt mit Tipps erfahrener Reisender: vor acht Uhr morgens am Fushimi Inari sein, um den Menschenmassen zu entgehen, die Tempelnamen auf Japanisch ausdrucken, die Essensmodelle in Restaurants nutzen, um ohne Sprachkenntnisse zu bestellen. Der Transportabschnitt erklärte, wie man Suica oder Pasmo auf dem Smartphone aktiviert, wie man den Shinkansen reserviert und dass die Informationsbüros in den Hauptbahnhöfen zu bestimmten Zeiten französischsprachiges Personal haben. Es schlug den Kyoto City Bus Day Pass vor und empfahl den Download von Offline-Karten. Für die Sprachbarriere schlug es nicht nur Google Translate, sondern auch Papago zur Spracherkennung sowie Schlüsselsätze in transliteriertem Japanisch vor.

Der abschließend auf Italienisch angeforderte Abschnitt, um die Mehrsprachigkeit innerhalb desselben Prompts zu testen, war sauber, korrekt und reich an praktischen Tipps zu Barzahlungen, Seven-Eleven-Geldautomaten und Übersetzungskarten für Lebensmittelallergien.

### Test 5 — Extrem langer Kontext: 460-seitiges Dokument *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 10,93 Token/s*

Dies war der überraschendste Test der gesamten Reihe und verdient es, mit der gebührenden Aufmerksamkeit erzählt zu werden. Ich lud den *AI Index Report 2025* hoch, ein PDF mit etwa 460 Seiten und über 20 Millionen Zeichen, und bat das Modell, das Wachstum der Videogenerierung zu beschreiben und die Seiten anzugeben, auf denen die Daten zu finden sind. Die Herausforderung war bewusst extrem gewählt: ein Kontext von nur 8078 Token – weit entfernt von den nativen 262.000 des Modells –, nur acht aktive Experten, nur acht Layer in der GPU.

Die Antwort machte mich sprachlos. Trotz der auf ein Minimum reduzierten Parameter lieferte das Modell eine präzise und gut strukturierte Zusammenfassung der Fortschritte bei der Videogenerierung zwischen 2023 und 2025. Es zitierte korrekt die wichtigsten Modelle: Meta Movie Gen, Google Veo und Veo 2, Runway Gen-3 Alpha, Luma Dream Machine, Kling 1.5. Es erwähnte das berühmte Beispiel des Prompts „Will Smith eating spaghetti“ als Meilenstein für den qualitativen Sprung in der Branche. Es verwies auf spezifische Abbildungen im Bericht wie Abbildung 2.3.11 und Abbildung 2.3.12. Und es gab an, dass die wichtigsten Daten auf den Seiten 126 und 127 des Berichts zu finden seien. Ich habe es überprüft. Es stimmte exakt.

Wie es dem Modell gelungen ist, die richtige Information in einem 460-seitigen Dokument bei einem Kontextfenster von nur wenigen Dutzend Seiten zu finden, bleibt das faszinierendste Geheimnis der gesamten Sitzung. Wahrscheinlich war das Modell in der Lage, die relevantesten Abschnitte trotz Speicherbeschränkungen zu identifizieren und beizubehalten, aber der genaue Mechanismus ist von außen nicht transparent. Transparent ist jedoch das Ergebnis: mit einer Minimal-Konfiguration in einem riesigen Dokument verifizierbare Verweise auf die korrekten Seiten. Das ist Robustheit.

### Test 6 — Räumliches Denken *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 11,42 Token/s*

Der Test verlangte die Analyse der Fotografie eines unordentlichen Zimmers und den Entwurf eines Aufräumplans. Trotz der konservativen Parameter – nur acht Experten, nur acht Layer in der GPU – lieferte das Modell eine visuell-räumliche Analyse auf höchstem Niveau.

Die Beschreibung war originalgetreu und detailliert: Bett mit schwarzem Metallrahmen, zwei korrekt positionierte weiße Leiterregale, ein überfüllter grauer Schreibtisch, ein kleiner weißer Schrank, Spiegel an der Tür. Die Wandfarben wurden als helles Salbeigrün identifiziert, der Boden mit bedrucktem Teppichboden, grün-weiß gestreifte Vorhänge. Sogar der blaue Wäschekorb mitten auf dem Boden, umgeben von verstreuter Kleidung, Schuhen, Kartons, Scheren und anderen Gegenständen, wurde erkannt und katalogisiert.

Der Aufräumplan war nach visuellen Prioritäten mit soliden Begründungen gegliedert. Zuerst die Kleidung vom Boden und vom Bett, da deren Entfernung den Laufweg freimacht, die visuelle Unruhe reduziert und den Raum größer wirken lässt. Dann das Bett, da ein ungemachtes Bett optisch mehr Platz einnimmt und ein Gefühl von Chaos erzeugt, während das Glattziehen die Grenzen des Raums definiert. Danach der Wäschekorb und die Schuhe, physische Hindernisse, die den zentralen Durchgang blockieren. Schließlich der Schreibtisch, dessen freie Oberfläche Ordnung und Funktionalität ausstrahlt. Die abschließende Zusammenfassung war perfekt: „Das erste Ziel ist nicht die Kleinteiligkeit, sondern das Volumen.“ Ein Satz, der die Essenz effektiver Organisation in einer sehr unordentlichen Umgebung zusammenfasst und den ein Profi der Branche nicht besser hätte formulieren können.

### Test 7 — Multi-Step Agent: Planung eines Softwareprojekts *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, 11,04 Token/s*

Dieser Test wurde speziell eingeführt, um das Versprechen der 43-prozentigen Verbesserung bei QwenWebBench zu überprüfen. Ein Modell, das in Physik und räumlichem Denken glänzt, könnte dennoch an einer komplexen Planungsaufgabe scheitern. Die wahre Reife eines Programmierassistenten zeigt sich in der Fähigkeit, Arbeit zu organisieren, Probleme vorherzusehen und praktische Lösungen anzubieten, nicht nur Code zu schreiben. Die Aufgabe bestand darin, die Entwicklung einer Web-App zur Verwaltung von Familienausgaben mit einem Team von zwei Entwicklern und einer detaillierten Roadmap zu planen.

Die Antwort war wahrscheinlich die umfassendste der gesamten Testreihe. Der vorgeschlagene Technologie-Stack war modern und konsistent, wobei jede Entscheidung in einer übersichtlichen Tabelle begründet wurde: React mit TypeScript und Vite für das Frontend, Node.js mit Express für das Backend, PostgreSQL mit Prisma als ORM, JWT für die Authentifizierung, papaparse für das CSV-Parsing, React-PDF für den Export, BullMQ für Benachrichtigungswarteschlangen, Docker für die Infrastruktur. Die Projektstruktur wurde nach logischen Ordnern sowohl für die Frontend- als auch für die Backend-Seite detailliert, inklusive einer docker-compose.yml zur Orchestrierung von Postgres, Redis und der Anwendung. Dies ist eine Struktur, wie sie ein echter Software-Ingenieur verwenden würde.

Die Planung in sechs wöchentliche Sprints war realistisch und gut ausbalanciert: Setup und Authentifizierung, Transaktionen und CSV-Import, Dashboard und Grafiken, PDF-Export, Budget und E-Mail-Benachrichtigungen, Testing und Deployment. Für jeden Sprint wurden Fokus, erwartete Deliverables, potenzielle kritische Punkte und die Arbeitsaufteilung zwischen den zwei Entwicklern angegeben. Die Empfehlung, zuerst die API-Verträge zu definieren und dann parallel zu arbeiten, ist eine Best Practice, die viele erfahrene Entwickler nur schwer konsequent umsetzen.

Kritische Punkte wurden mit chirurgischer Präzision identifiziert: heterogene CSV-Formate und der Umgang mit Teilfehlern beim Import, Zustellbarkeit und Zeitzonen für E-Mail-Benachrichtigungen, Testabdeckung und Rollback-Plan für das Deployment. Der Abschnitt zu den Best Practices war vollständig: httpOnly-Cookies und Rate Limiting für die Sicherheit, DB-Indizes und Paginierung für die Performance, Mocks für SMTP und DB für das Testing, GitHub Actions für CI/CD. Das Modell schlug sogar Sentry für das Error-Tracing und Notion für die Dokumentation vor. Der einzige kleine Kritikpunkt ist, dass die Antwort für eine Erstplanung fast schon zu detailliert war, aber das ist die Art von Übermaß, die man bevorzugt.
![testqwen.jpg](testqwen.jpg)
*Screenshot meines PCs und von LM Studio während des Multi-Step Agent Tests.*

### Test 8 — Thinking Preservation: Konversation über vier Runden *(5/5)*

*Parameter: 8078 Token Kontext, GPU-Offload 8 von 43 Layern, 8 von 256 aktiven Experten, F16, knapp über 11 Token/s pro Runde*

Dieser Test wurde eingeführt, um eine der interessantesten Neuerungen von Qwen3.6 zu bewerten: die Fähigkeit, die Kohärenz der Argumentation über Multi-Turn-Gespräche hinweg aufrechtzuerhalten und dabei nicht nur den Chatverlauf, sondern auch die Logik der in den vorangegangenen Phasen getroffenen Entscheidungen zu bewahren. Für die iterative Entwicklung ist dies eine fundamentale Eigenschaft, da sie es ermöglicht, komplexe Projekte aufzubauen, ohne die Voraussetzungen ständig wiederholen zu müssen.

Das Gespräch gliederte sich in vier Runden. In der ersten bat ich um einen Technologie-Stack für eine Task-Management-Anwendung: Die Antwort war detailliert mit einer Vergleichstabelle (React mit TypeScript, Node.js mit Express, PostgreSQL mit Prisma, JWT, SendGrid mit BullMQ), jede Entscheidung mit soliden Argumenten begründet. In der zweiten Runde bat ich um eine Einschätzung zur Wahl zwischen WebSocket und Polling für Echtzeitbenachrichtigungen bei 1000 aktiven Nutzern: Das Modell erklärte, warum WebSocket hinsichtlich Latenz und Overhead überlegen ist, skizzierte eine Architektur mit PostgreSQL LISTEN/NOTIFY und Redis Pub/Sub und sah den Grenzfall von Netzwerken voraus, die WebSockets blockieren, indem es erklärte, dass Socket.IO den Fallback automatisch handhabt. In der dritten Runde bat ich um das Datenbankschema in Prisma: Das erstellte Schema war vollständig, mit acht Hauptmodellen, Enums für Status, Priorität und Rolle, klar definierten Beziehungen, UUIDs für Primärschlüssel, strategischen Indizes für häufige Abfragen und kontrollierten Kaskaden. Es enthielt ein Beispiel für eine Abfrage, die das N+1-Problem vermied.

Die vierte Runde war der eigentliche Test: Ich bat um eine Zusammenfassung der bisher getroffenen Technologieentscheidungen und eine Erklärung, warum wir uns für WebSocket statt Polling entschieden hatten. Das Modell erinnerte sich korrekt an alles aus der ersten Runde, fasste die Gründe für WebSocket mit derselben Terminologie und denselben Argumenten aus der zweiten Runde zusammen und fügte spontan einen Abschnitt zur Skalierbarkeit auf 10.000 Nutzer hinzu – mit Strategien für Backend, Datenbank, Caching, E-Mail-Warteschlangen, Observability und Deployment sowie einer operativen Checkliste. Es erhielt keine Gedächtnisstütze: Es erinnerte sich einfach. Keine Widersprüche, kein Vergessen, die Argumentation wurde kohärent fortgeführt. Das Versprechen der *Thinking Preservation* war kein Marketing.

## Das Video, das wartet

Qwen3.6 verspricht ein natives Videoverständnis, eine absolute Neuheit gegenüber den Vorgängerversionen. Ich habe versucht, dies zu testen, indem ich eine MP4-Datei in LM Studio geladen habe. Das System reagierte mit einem Ausrufezeichen am Anhang, und das Modell gab an, keine Datei erhalten zu haben. Die Einschränkung liegt nicht am Modell, sondern an dem für die Ausführung gewählten Werkzeug: LM Studio verarbeitet Bilder, PDFs, Textdokumente und CSV-Dateien exzellent, aber Videos gehören noch nicht zu den unterstützten Formaten. Ich behalte mir vor, diesen Test so bald wie möglich nachzuholen, wahrscheinlich mit llama.cpp oder vLLM, die eine umfassendere Unterstützung für Videoinhalte bieten könnten. Wenn die Versprechen gehalten werden, wird dies eine Folge sein, die einen eigenen Platz verdient.
![tabella-confronto-modelli.jpg](tabella-confronto-modelli.jpg)
*Die „Vergleichstabelle“ mit den Tests früherer Modelle. Mit der für Qwen 3.6 getesteten Doppelkonfiguration.*

## Lohnt es sich, bis an das Limit zu gehen?

Dies ist die Frage, die der gesamten Serie zugrunde liegt und der man bei Qwen3.6 nicht mehr ausweichen kann. Mit Qwen 3.5 9B erreichte man 20-25 Token pro Sekunde bei einer entspannten Konfiguration. Bei Gemma 4 26B MoE waren die Spielräume bereits enger geworden. Mit diesem Modell liegt man bei 11 Token (etwa 14/15 bei maximaler Optimierung auf meiner Hardware) pro Sekunde, wobei die GPU nur zu einem Bruchteil ausgelastet ist und die Last in einem prekären Gleichgewicht zwischen VRAM und System-RAM verteilt ist. Die aufeinanderfolgenden Höchstnoten haben die berechtigte Frage nach der Strenge meiner Tests aufgeworfen, und diese Frage bleibt offen: Wahrscheinlich werden in den folgenden Folgen schärfere Bewertungsinstrumente benötigt.

Aber einstweilen gibt es einen konkreten Fakt, über den man nachdenken kann. Die Antwort auf die Geschwindigkeitsfrage hängt vollständig davon ab, wie man das Modell nutzt. Wenn man einen Konversationsassistenten für schnelle Sitzungen sucht, machen sich 11 Token (etwa 14/15 bei maximaler Optimierung auf meiner Hardware) pro Sekunde bemerkbar. Arbeitet man an strukturierten Aufgaben, tiefgehenden Analysen, komplexer Codegenerierung oder langen Dokumenten, ist die Qualität, die dieses Modell in der reduzierten Konfiguration bietet, für kleinere Modelle schlicht unerreichbar – selbst wenn diese bis zum Maximum getrieben werden. Das Experiment mit dem 460-seitigen Dokument hat dies auf plastischste Weise gezeigt: ein winziges Kontextfenster, eine Maschine am Limit und das Modell, das die exakten Seiten in einem wahren Wälzer findet.

Es gibt jedoch einen breiteren Subtext, den diese Versuchsreihe progressiv an die Oberfläche bringt. Wenn ein Modell mit 35 Milliarden Parametern lokal auf Consumer-Hardware mit Ergebnissen läuft, die mit den Cloud-Diensten von vor zwei Jahren vergleichbar sind, ändert sich etwas in der Topologie des KI-Marktes. Die Cloud bleibt unschlagbar bei der Geschwindigkeit, bei den Frontier-Modellen und bei der Skalierbarkeit. Aber für diejenigen, die mit sensiblen Daten arbeiten, für diejenigen, die die vollständige Kontrolle über die Inferenz wollen, und für diejenigen, die nicht von einem API-Endpunkt mit seinen Latenzen und variablen Kosten abhängig sein wollen, wird der lokale Betrieb zu einer reifen Wahl und ist kein Experiment für Enthusiasten mehr. Der Abstand zwischen den beiden Optionen verringert sich mit jeder Modellgeneration, und Qwen3.6 ist, selbst in dieser absichtlich benachteiligten Konfiguration, der bisher überzeugendste Beweis dafür.

Die Höchstnoten sind ein Problem. Aber es ist die Art von Problem, die viel weniger Angst macht als das Gegenteil.
