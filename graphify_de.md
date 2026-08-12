---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-05-29
author: "Dario Ferrero"
---

# Graphify und das Gedächtnis, das LLMs nicht haben
![graphify.jpg](graphify.jpg)

*Was wäre, wenn Ihr KI-Assistent aufhören könnte, jedes Mal das gesamte Projekt neu zu lesen, um eine einzige Frage zu beantworten? Graphify, ein auf GitHub mit über 50.000 Sternen veröffentlichtes Open-Source-Tool, verspricht genau das: einen Ordner mit Code, Dokumenten, PDFs, Bildern und Videos in einen Wissensgraphen zu verwandeln, der von KI-Agenten abgefragt werden kann, wodurch die Anzahl der pro Abfrage verbrauchten Token drastisch reduziert wird.*

Wer täglich mit KI-Agenten an mittelgroßen Projekten arbeitet, kennt eine spezifische Frustration gut: Jedes Mal, wenn ein Assistent wie Claude Code, Cursor oder Gemini CLI eine Frage zum Projekt beantworten muss, durchläuft er die gesamte Codebasis, als hätte er noch nie etwas gelesen. Er liest Dateien neu, analysiert Strukturen neu und fängt bei Null an. Das erinnert ein wenig an Inspektor Lunge aus Naoki Urasawas *Monster*, der, um sich an etwas zu erinnern, jedes Mal die gesamte Deduktionskette vom ersten Hinweis an neu konstruieren muss, unfähig, einen Zwischenzustand zwischen den Sitzungen zu bewahren.

Im April haben wir auf diesen Seiten detailliert [Andrej Karpathys Vorschlag für eine evolutionäre Wissensbasis für LLMs](https://aitalk.it/it/llm-knowledge-base.html) analysiert: den Aufbau eines strukturierten Wikis in Markdown, das das Modell kompilieren und abfragen kann, um zu vermeiden, dass jedes Mal das gesamte Korpus in den Kontext geladen werden muss. Der Vorschlag sammelte über 16 Millionen Aufrufe auf X und löste eine hitzige technische Debatte darüber aus, welche Gedächtnisarchitektur für den professionellen Einsatz tatsächlich praktikabel sei.

Graphify setzt genau an dieser Intuition an, zitiert Karpathys Ansatz explizit in der README als Ausgangspunkt und führt ihn dann weiter: Statt eines flachen Wikis in Markdown baut es einen Wissensgraphen auf, in dem jede Entität, jede Funktion und jedes aus Ihren Dateien extrahierte Konzept zu einem Knoten wird und die Beziehungen zwischen den Entitäten zu navigierbaren Kanten werden. Der Unterschied ist nicht ästhetisch, sondern strukturell.

## Was ist ein Graph (und warum er hier alles verändert)

Ein Graph ist in seiner einfachsten Form eine Sammlung von Punkten, die durch Linien verbunden sind. Die Punkte werden Knoten genannt, die Linien Kanten. Es ist dieselbe Struktur, die Google Maps verwendet, um die Straßen einer Stadt darzustellen, oder die soziale Netzwerke einsetzen, um die Beziehungen zwischen Nutzern zu modellieren. Das ist keine Metapher: Es ist eine Datenstruktur mit mathematischen Eigenschaften, die sie besonders geeignet machen, komplexe Beziehungen darzustellen.

Warum ist ein Graph für ein Softwareprojekt nützlicher als ein Markdown-Dokument? Die Antwort liegt in der Natur der Beziehungen. In einem Text, selbst in einem gut strukturierten, sind die Verbindungen zwischen Konzepten implizit: Man muss lesen, den Kontext verstehen und die Verknüpfungen ableiten. In einem Graphen sind die Beziehungen explizit, typisiert und traversierbar. Man kann fragen: „Was ist der kürzeste Pfad zwischen dem Authentifizierungsmodul und der Datenbank?“, und erhält eine Antwort, indem man durch die Kanten navigiert, anstatt Text zu analysieren.

Für einen KI-Agenten, der Fragen zu einem Projekt beantworten muss, ist dieser Unterschied substanziell. Anstatt Dutzende von Dateien in den Kontext zu laden, in der Hoffnung, dass das Modell die relevanten Verbindungen findet, navigiert der Agent durch den Graphen, ruft nur die relevanten Knoten und deren direkte Nachbarn ab und erstellt die Antwort mit einem Bruchteil der Token. Es ist der Unterschied, ob man jemanden bittet, eine ganze Enzyklopädie zu lesen, um eine Frage zu beantworten, oder ihm einen semantischen Index gibt, mit dem er direkt zum richtigen Eintrag navigieren kann.

## Drei Durchgänge, um alles zu verstehen

Die interne Pipeline von Graphify, die im Detail in der Datei [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) des Repositories dokumentiert ist, gliedert sich in drei Phasen, die darauf ausgelegt sind, die lokale Verarbeitung zu maximieren und externe API-Aufrufe zu minimieren.

Der erste Durchgang betrifft den Quellcode und erfolgt vollständig lokal: keine APIs, keine verbrauchten Token. Tree-sitter, der AST-Parser, der auch von Editoren wie Neovim und Helix für Echtzeit-Syntax-Highlighting verwendet wird, analysiert die Codedateien und extrahiert Klassen, Funktionen, Importe, Aufrufgraphiken und Inline-Kommentare. Das Ergebnis ist deterministisch: Dieselbe Datei erzeugt immer denselben Output. SQL-Dateien erhalten eine Sonderbehandlung, wobei Tabellen, Ansichten, Fremdschlüssel und JOIN-Beziehungen mit derselben deterministischen Logik extrahiert werden. Zum Zeitpunkt der Veröffentlichung erklärt Graphify die Unterstützung für 29 Programmiersprachen.

Der zweite Durchgang deckt Audio- und Videodateien ab, ebenfalls lokal. Faster-whisper, eine optimierte Implementierung von OpenAIs Whisper-Modell, die vollständig lokal läuft, transkribiert die Multimedia-Inhalte. Es gibt ein raffiniertes technisches Detail: Die Transkription wird von den am stärksten vernetzten Knoten des im ersten Durchgang erstellten Graphen „geführt“, den sogenannten „god nodes“ – den Konzepten, die am häufigsten in den aus dem Code extrahierten Beziehungen vorkommen. Dies führt dazu, dass das Transkriptionsmodell projektspezifischen Fachbegriffen mehr Aufmerksamkeit schenkt. Die Transkripte werden zwischengespeichert: Nachfolgende Durchläufe überspringen bereits verarbeitete Dateien.

Der dritte Durchgang, der API-Token verbraucht, verarbeitet Dokumente, PDFs und Bilder. Hier kommt das vom Nutzer konfigurierte Sprachmodell ins Spiel: Claude, Gemini, OpenAI oder alternativ eine lokale Instanz von Ollama oder AWS Bedrock über die IAM-Anmeldeinformationskette. Die Dateien werden parallel von mehreren Unteragenten verarbeitet, von denen jeder ein strukturiertes JSON-Fragment mit Knoten, Kanten und Gruppenbeziehungen zurückgibt. Die Fragmente werden dann zu einem einzigen kohärenten Graphen zusammengeführt.

Das Clustering der Communities erfolgt mit dem Leiden-Algorithmus, einer 2019 in *Nature Scientific Reports* veröffentlichten Methode, die Knoten nach Verbindungsdichte gruppiert, ohne separate Vektor-Embeddings zu erfordern. Die vom Sprachmodell extrahierten semantischen Beziehungen, zum Beispiel `semantically_similar_to` zwischen zwei verwandten Konzepten, sind bereits als Kanten im Graphen vorhanden und beeinflussen direkt die Form der erkannten Communities. Es gibt keine separate Vektordatenbank: Die Graphenstruktur ist das Ähnlichkeitssignal.

Jede Beziehung wird mit einem von drei Vertrauens-Tags markiert: `EXTRACTED` für Beziehungen, die direkt im Quellcode gefunden wurden, `INFERRED` für Modell-Inferenzen mit einer Punktzahl von 0,55 bis 0,95 gemäß einer dokumentierten diskreten Skala, und `AMBIGUOUS` für unsichere Fälle, die im Abschlussbericht zur manuellen Überprüfung markiert werden. Man weiß immer, ob der Graph einem etwas Sicheres oder Hypothetisches sagt.
![graphify-query1.jpg](graphify-query1.jpg)
*Screenshot meines Tests an den Daten (MTV-Paradoxon-Anfrage) in opencode*

## Das gesamte Projekt in 7 Megabyte

Ich habe Graphify über OpenCode installiert und auf dem gesamten AiTalk-Projekt ausgeführt: Code, Artikel, Bilder, Audiodateien, die gesamte im Laufe der Zeit angesammelte Arbeitsbasis. Das Quellmaterial wog etwa 970 MB. Der generierte Output, der Ordner `graphify-out/` mit seinen drei Hauptdateien, belegte etwas mehr als 7 MB.

Drei Dateien: `graph.html`, die interaktive Visualisierung, die in jedem Browser navigierbar ist; `GRAPH_REPORT.md`, der Textbericht mit den Schlüsselkonzepten, den wichtigsten Verbindungen und vorgeschlagenen Fragen; und `graph.json`, der vollständige Graph im NetworkX-Node-Link-Format, der direkt abgefragt werden kann.

Von diesem Moment an erhielt jede Frage, die OpenCode zur technischen Struktur des Projekts, zur Codelogik, zum Inhalt der Artikel und zu den thematischen Verbindungen zwischen ihnen gestellt wurde, exzellente Antworten. Nicht generisch, sondern kontextualisiert: Der Agent wusste, welche Komponenten von welchen abhängen, welches Thema in mehreren Artikeln aus verschiedenen Blickwinkeln behandelt wird, wo es nicht explizite Verbindungen zwischen scheinbar weit entfernten Inhalten gab. Das Modell navigierte durch den Graphen, anstatt jedes Mal die Quelldateien neu zu lesen. Wo früher eine komplexe Abfrage das Laden von Dutzenden von Dateien in den Kontext erforderte, geht der Agent nun vom Bericht aus und navigiert durch das JSON, um nur das zu finden, was benötigt wird.
![grafo-aitalkjpg.jpg](grafo-aitalkjpg.jpg)
*Screenshot der html-Seite mit der dynamischen und navigierbaren Darstellung des Graphen des AiTalk.it-Projekts*

## Ehrliche Zahlen: 71x, aber es kommt darauf an

Das Repository veröffentlicht in der Datei [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) einen expliziten Benchmark, und es lohnt sich, ihn aufmerksam zu lesen, da die Zahlen mit einer für ein Projekt in der Werbephase ungewöhnlichen Ehrlichkeit präsentiert werden.

Bei einem gemischten Korpus von 52 Dateien, bestehend aus Karpathys Repositories, fünf akademischen Arbeiten und vier Bildern, erklärt Graphify eine Reduzierung der Token pro Abfrage um das 71,5-fache im Vergleich zum direkten Lesen der Rohdateien. Bei einem kleineren Korpus, vier Dateien bestehend aus Quellcode und wissenschaftlichen Arbeiten, sinkt die Reduzierung auf das 5,4-fache. Bei sechs Dateien etwa 1x: kein relevanter Vorteil bei den Token, allenfalls strukturelle Klarheit.

Das Muster ist klar und wird explizit erklärt: Die Komprimierung skaliert mit der Größe des Korpus. Sechs Dateien passen bereits in ein einziges Kontextfenster. Bei 52 Dateien summieren sich die Einsparungen schnell. Jeder `worked/`-Ordner im Repository enthält die ursprünglichen Eingabedateien und den tatsächlichen Output, sodass jeder den Benchmark selbstständig replizieren kann.

Es sollte jedoch präzisiert werden, was diese Zahlen nicht enthalten: die Kosten für die Erstextraktion, den Moment, in dem Graphify API-Token verbraucht, um Dokumente, PDFs und Bilder zu analysieren. Diese Kosten amortisieren sich bei nachfolgenden Abfragen dank des SHA256-Caches, der nicht geänderte Dateien überspringt, aber es sind reale Kosten, die in einem großen Korpus signifikant sein können, insbesondere bei Premium-Modellen. Der Benchmark misst die Einsparung im stationären Zustand, nicht die Einrichtungskosten. Die Dokumentation sagt dies deutlich.

## Integrieren oder verloren gehen

Einer der am besten gepflegten Aspekte des Projekts ist die Kompatibilität mit dem Ökosystem der Entwicklungstools. Derzeit unterstützt Graphify die direkte Installation auf Claude Code, OpenCode, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider und anderen weniger verbreiteten Tools.

Der Integrationsmechanismus ist einfach. Sobald der Graph erstellt ist, schreibt der Befehl `graphify claude install` (oder der entsprechende Befehl für die gewählte Plattform) eine Konfigurationsdatei, die den Assistenten anweist, vor der Beantwortung `GRAPH_REPORT.md` zu lesen. Auf Plattformen, die Hooks unterstützen, wie Claude Code, Codex und Gemini CLI, wird vor jedem Lesen einer Datei automatisch ein Hook aktiviert: Der Assistent navigiert durch den Graphen, anstatt das Verzeichnis zu scannen.

Für Teams ist der empfohlene Workflow, den Ordner `graphify-out/` in das Git-Repository zu committen. Jedes Mitglied, das einen Pull macht, findet den bereits aktualisierten Graphen vor. Der Befehl `graphify hook install` fügt einen Post-Commit-Hook hinzu, der nach jedem Commit automatisch den AST-Teil rekonstruiert – ohne Kosten für APIs, mit einem Git-Merge-Treiber, der Konflikte in `graph.json` verwaltet, indem er die beiden Graphen zusammenführt, anstatt unlösbare Markierungen zu hinterlassen.

Das Paket heißt `graphifyy` auf PyPI (Doppel-y), erfordert Python 3.10+ und wird mit `uv tool install graphifyy`, `pipx install graphifyy` oder `pip install graphifyy` installiert. Der CLI-Befehl bleibt `graphify`.
![graphify-query2.jpg](graphify-query2.jpg)
*Screenshot meines Tests am Code (Anfrage zur Website-Generierungsmethode) in opencode*

## Datenschutz: Was zu Hause bleibt

Die Verwaltung des Datenschutzes folgt einer expliziten Logik. Der Quellcode wird vollständig lokal über Tree-sitter verarbeitet, ohne Aufrufe externer Dienste. Audio- und Videodateien werden lokal mit Faster-whisper transkribiert. Kein Byte Code oder Multimedia-Inhalt verlässt den Rechner des Nutzers.

Die Situation ändert sich bei Dokumenten, PDFs und Bildern: Diese werden über die API an das konfigurierte Sprachmodell gesendet. Wenn Claude verwendet wird, werden die Dateien an Anthropic gesendet. Wenn Ollama verwendet wird, bleiben sie lokal. Für Kontexte mit sensiblen Daten bietet Graphify zwei Optionen: eine lokale Ollama-Instanz oder AWS Bedrock über IAM, ohne explizite API-Schlüssel. Das Projekt gibt an, keine Telemetrie, kein Nutzungs-Tracking oder Datenanalyse zu betreiben.

Ein Aspekt, den Teams bei proprietärem Code berücksichtigen sollten: Auch wenn der Code lokal bleibt, werden Architektur-Dokumente, Spezifikations-PDFs und Mockup-Bilder vom konfigurierten externen Modell verarbeitet. Bei vertraglichen Geheimhaltungspflichten sollte diese Unterscheidung vor der Einführung sorgfältig geprüft werden.

## Grenzen ohne Rabatte

Es wäre unredlich, sich nur auf Lob zu beschränken. Es gibt Aspekte, die eine kritische Bewertung verdienen.

Der erste betrifft die Qualität der abgeleiteten Beziehungen. Die als `INFERRED` gekennzeichneten Beziehungen hängen von der Qualität des verwendeten Modells ab. Ein kleineres Modell oder ein Modell, das mit einem reduzierten Token-Budget konfiguriert wurde, kann spekulative Beziehungen mit optimistischen Vertrauenswerten produzieren. Die Skala von 0,55 bis 0,95 ist auf die Testkorpora des Entwicklers kalibriert, nicht unbedingt auf die Art des Projekts, auf das das Tool angewendet wird.

Die zweite Grenze betrifft Aktualisierungen. Der SHA256-Cache überspringt nicht geänderte Dateien, aber was passiert, wenn man eine Funktion von einem Modul in ein anderes verschiebt oder eine Klasse signifikant refaktorisiert? Der Graph kann verwaiste Knoten oder Beziehungen aufweisen, die auf nicht mehr existierende Entitäten verweisen. Der Befehl `--update` verwaltet geänderte Dateien, aber bei tiefgreifenden Refactorings ist wahrscheinlich eine vollständige Rekonstruktion erforderlich, mit den damit verbundenen Token-Kosten.

Der dritte kritische Aspekt ist die Skalierung. Wie bei Karpathys Wiki-Ansatz hat auch der Graph einen Bruchpunkt. Für sehr große Korpora schlägt die Dokumentation vor, direkte Abfragen auf `graph.json` zu verwenden oder den Graphen als MCP-Server mit `python -m graphify.serve` bereitzustellen, der strukturierte Tools wie `query_graph`, `get_node`, `get_neighbors` und `shortest_path` bietet. Die Lösung ist raffiniert, fügt aber eine Konfigurationsebene hinzu, die nicht alle Workflows leicht absorbieren können.

Schließlich ist anzumerken, dass das Projekt im Wesentlichen von einem einzelnen Entwickler, Safi Shamsi, gepflegt wird. Das Repository zeigt eine intensive Aktivität mit 97 Releases zum Zeitpunkt der Erstellung dieses Artikels und der letzten stabilen Version v0.7.16, die am 12. Mai 2026 veröffentlicht wurde. Doch die langfristige Nachhaltigkeit eines Projekts mit dieser Sichtbarkeit und dieser Abhängigkeit von einem einzigen Maintainer ist eine Variable, die bei der Planung einer Einführung in kritischen Umgebungen nicht ignoriert werden sollte.

## Die Zukunft des Gedächtnisses

Graphify löst ein konkretes Problem. Aber die interessanteste Frage, die es aufwirft, betrifft nicht die Token-Einsparung: Sie betrifft die Natur des Gedächtnisses bei KI-Agenten.

Heute hat ein Agent kein persistentes Gedächtnis. Jede Sitzung ist ein unbeschriebenes Blatt, jedes Projekt wird von Grund auf neu entdeckt. Graphify und ähnliche Projekte sind Versuche, eine externe Ebene des strukturierten Gedächtnisses aufzubauen, die Sitzungen überlebt, die sich über die Zeit ansammelt und die nicht nur die Rohdaten, sondern die Beziehungen zwischen ihnen darstellt.

Es bleiben viele offene Fragen. Wie bewahrt man die Kohärenz eines Graphen in einem sich schnell entwickelnden Projekt? Wer ist verantwortlich für die Qualität der abgeleiteten Beziehungen, wenn ein Agent auf deren Grundlage Entscheidungen trifft? Und die subtilste Frage: Wenn der Agent in einem Graphen navigiert, anstatt über Dateien nachzudenken, wird die Qualität der Erstextraktion zum eigentlichen Flaschenhals, der nicht durch einen Temperaturparameter, sondern durch die Qualität der Ingest-Pipeline steuerbar ist.

Von der Website der Graphify Labs geht eine ehrgeizigere Vision hervor: Penpax, das kommerzielle Produkt, das in Kürze in einer Testversion angekündigt wird, verspricht, dieselbe Logik auf die gesamte tägliche Arbeit einer Person anzuwenden – Besprechungen, E-Mails, Dateien und Code –, und zwar durch Aktualisierung im Hintergrund, ohne Cloud, vollständig On-Device. Ein digitales „zweites Gehirn“, das auf einer seriösen technischen Basis anstelle von Motivationsmetaphern aufgebaut ist.

Graphify in seiner Open-Source-Form ist bereits ein bedeutender Ausgangspunkt. Es ist nicht die ultimative Lösung für das Problem des LLM-Gedächtnisses, aber es ist ein präziser Indikator für die Richtung, in die gesucht wird: nicht im Modell, nicht im Kontext, sondern in einer strukturierten und persistenten Darstellung, die außerhalb von beidem existiert.

---

*Graphify ist auf [GitHub](https://github.com/safishamsi/graphify) unter der MIT-Lizenz verfügbar. Das PyPI-Paket heißt [graphifyy](https://pypi.org/project/graphifyy/) (Doppel-y). Die Website des Projekts ist [graphifylabs.ai](https://graphifylabs.ai). Die technische Dokumentation zur Extraktions-Pipeline findet sich in [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md).*
