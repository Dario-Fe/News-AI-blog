---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-31
author: "Dario Ferrero"
---

# Muse Glimmer 30B lokal: Metas neues Modell
![muse-glimmer30b.jpg](muse-glimmer30b.jpg)

*Am 10. August 2026 veröffentlichte Meta Superintelligence Labs [Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model), ein Modell mit 30 Milliarden Parametern, das für die lokale Ausführung auf Consumer-Hardware konzipiert ist. Die Nachricht verdient eine sofortige Klarstellung für diejenigen, die Meta schon lange verfolgen: Es ist kein Llama. Es ist die erste Veröffentlichung der neuen Forschungsabteilung, die nach der Umstrukturierung der KI-Aktivitäten des Unternehmens gegründet wurde – ein Projekt, das mit einer anderen Identität und Philosophie als die alte Familie geboren wurde.*

Die wichtigste Besonderheit, die man verstehen muss, noch bevor man LM Studio öffnet, betrifft seine Natur. Muse Glimmer wurde nicht von Grund auf neu trainiert wie [Qwen3.8, das ich in meinem vorherigen Artikel getestet habe](https://aitalk.it/it/qwen38-27b.html). Es ist eine destillierte Version von Muse Spark 1.2, Metas Spitzenmodell: Ein viel größerer "Lehrer" hat diesen "Schüler" darauf trainiert, seine Verhaltensweisen zu replizieren – nach einem Verfahren, das im Fachjargon Logit-Destillation genannt wird. Das Ergebnis ist ein kleineres und effizienteres Modell, das einen Großteil der Fähigkeiten des Meisters erbt, ohne dessen Umfang mitzuschleppen. Es ist ein wenig wie in Miyazakis Lehrlingsgeschichten, in denen der Schüler den Meister nicht durch oberflächliche Nachahmung kopiert, sondern seine Methode absorbiert, bis er sie sich zu eigen macht.

Ich habe mich entschieden, es in derselben Größenklasse wie den vorherigen Test zu testen – ein dichtes 30B-Modell gegen das dichte 27B-Modell von Qwen –, eben weil Meta angibt, dass es für lokale Agenten, Tool Calling und die Orchestrierung komplexer Aufgaben konzipiert ist. Die Frage, die ich mir gestellt habe, ist einfach: Kann ein Modell "aus dem Hause Meta", das explizit als Agent geboren wurde, auf meiner Hardware mit den chinesischen Modellen konkurrieren, die diese Klasse bisher dominiert haben?

Für die Ausführung habe ich mich für die Quantisierung Q4_K_XL entschieden, etwa 19 GB auf der Festplatte. Quellen weisen darauf hin, dass Muse Glimmer für Hardware mit 24–32 GB VRAM ausgelegt ist, aber mit teilweisem Offloading konnte ich es auf meiner Konfiguration dennoch zum Laufen bringen, wobei ich etwas Geschwindigkeit opferte. Ich habe einen Kontext von 91.000 Token eingestellt – ein Kompromiss zwischen dem vom Hersteller angegebenen nativen Fenster von 131k und den verfügbaren Speichermargen.

## Das Labor, unverändert

Wer der Serie gefolgt ist, kennt die Konfiguration bereits: AMD Ryzen 7700 Prozessor, 32 GB DDR5-RAM, AMD Radeon RX 9060 XT GPU mit 16 GB VRAM, alles orchestriert über [LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html), wie in der ersten Episode dieser Serie ausführlich beschrieben, zusammen mit dem Vergleich mit Ollama und den Gründen für die Wahl. Ich werde hier nicht weiter darauf eingehen; wer tiefer einsteigen möchte, findet alles in diesem Artikel.

Für Muse Glimmer habe ich einige spezifische Parameter angepasst. Der GPU-Offload wurde auf 35 von 52 Layern eingestellt, mehr als die Hälfte des Modells verbleibt also im VRAM, wobei der CPU-Thread-Pool auf das maximal Zulässige eingestellt wurde (acht von acht). Der Evaluierungs-Batch wurde bei 2048 belassen, der physische Batch bei 512 und die maximale gleichzeitige Vorhersage bei 4.

Eine Anmerkung sollte sofort gemacht werden, da sie die gesamte Testsession geprägt hat: Muse Glimmer neigt dazu, lange nachzudenken, bevor es antwortet. In einem Fall habe ich eine Denkzeit von zehn Minuten beobachtet, in einem anderen von drei Minuten, wobei das Modell oft mehrmals über dieselbe Lösung iteriert, selbst wenn die korrekte Antwort bereits in den ersten Absätzen der Überlegung aufgetaucht war. Es ist ein Verhalten, das, wie wir sehen werden, die tägliche Nutzbarkeit stark belastet.

## Ein destilliertes Gehirn, nicht geboren

Bevor wir zu den Tests kommen, lohnt es sich zu verstehen, was sich unter der Haube befindet. Muse Glimmer ist ein dichtes Modell, kein Mixture of Experts wie [Ornith 1.0](https://aitalk.it/it/ornith-1.0.html) oder [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html), die ich in vorherigen Episoden dieser Serie ausprobiert habe. Der architektonische Unterschied ist kein Detail für Insider: In einem dichten Modell aktiviert jedes Token das gesamte Netzwerk, alle dreißig Milliarden Parameter, während in einem MoE jedes Mal nur ein Bruchteil der internen "Experten" konsultiert wird. Die Wette dichter Modelle besteht darin, dass sich dieser höhere Rechenaufwand in einer überlegenen Denkfähigkeit niederschlägt.

Auf der multimodalen Front integriert Muse Glimmer nativ einen visuellen Encoder mit 1,8 Milliarden Parametern, der Bilder und Videos ohne externe Module lesen kann. Die Lizenz ist Apache 2.0 – dieselbe freizügige Wahl, die bereits bei anderen Modellen dieser Serie getroffen wurde, ein Detail, das für Entwickler kommerzieller Produkte, die keine rechtlichen Komplikationen wünschen, alles andere als nebensächlich ist.

Architektonisch beschreiben [die veröffentlichten Spezifikationen](https://www.together.ai/models/muse-glimmer) eine Grouped-Query Attention mit einem Verhältnis von 32 Query-Heads gegenüber 2 Key-Value-Heads – eine Wahl, die den für den Cache während der Inferenz erforderlichen Speicher drastisch reduziert. Hinzu kommt die Unterstützung für DFlash, eine spekulative Dekodierungstechnik, die ganze Blöcke von sechzehn Token in einem einzigen Durchgang vorhersagt und sie dann parallel überprüft, anstatt sie einzeln zu generieren. Auf dem Papier sollte dies eine Beschleunigung von bis zu 3x im Vergleich zur Token-für-Token-Generierung garantieren. In der Praxis lag die auf meiner Hardware beobachtete Geschwindigkeit sehr nah an der von Qwen3.8, bei etwa 5 Token pro Sekunde: Die Theorie der High-End-Hardwarebeschleunigung überträgt sich nicht immer linear auf eine Mittelklasse-Konfiguration wie meine.

Es ist wie immer in dieser Serie erwähnenswert, dass die folgenden Tests keinen Anspruch auf Laborstrenge erheben. Es sind keine Benchmarks; ich nutze weder standardisierte Suiten noch statistisch signifikante Stichproben: Es sind acht praktische Versuche, dieselben wie für Qwen3.8, Ornith und [Laguna XS-2.1](https://aitalk.it/it/qwen36-35b-ai.html), die darauf ausgelegt sind zu verstehen, wie sich das Modell im täglichen Gebrauch von jemandem verhält, der schreibt, anstatt akademische Ranglisten zu erstellen.

## Die acht Versuche

### Wissenschaftliches Schlussfolgern: Der Higgs-Mechanismus

Ich habe das Modell gebeten, die elektroschwache Symmetriebrechung im Standardmodell zu erklären, unter Berücksichtigung des Higgs-Feldes sowie der W-, Z-Bosonen und des Photons – derselbe Prompt, der für die anderen Modelle der Serie verwendet wurde. Generierungsgeschwindigkeit: 5,34 Token pro Sekunde. Die Antwort kam technisch einwandfrei an: korrekte Formeln, solide logische Struktur, mit Bezug auf den "mexikanischen Hut" des Higgs-Potenzials und der korrekten Ableitung der W- und Z-Massen.

Was im Vergleich zu Qwen3.8 fehlt, ist die didaktische Sorgfalt. Die Antwort ist direkt und prägnant, es fehlt die narrative Progression, die den Leser Schritt für Schritt begleitet, ohne ausformulierte Metaphern oder verbale Erklärungen, die denjenigen helfen, die noch keine Grundlagen haben. Für einen Universitätsstudenten – das explizite Ziel des Prompts – ist das Ergebnis weniger zugänglich, als es sein sollte. Ich habe die Note dafür leicht bestraft: Es ist ein Modell, das mit einem fachkundigen Kollegen zu sprechen scheint, nicht mit jemandem, der noch lernt.

**Note: 4,8/5.**

### Multimodalität: Die unscharfe Excel-Tabelle

Ich habe ein qualitativ minderwertiges Bild einer Excel-Tabelle hochgeladen und um eine Beschreibung des Inhalts, der Hauptdaten und der Trends gebeten. Geschwindigkeit: 5,22 Token pro Sekunde. Das Modell las die Blattstruktur, die numerischen Werte und die Spaltenbeziehungen korrekt ab, extrahierte saisonale Muster und Unterschiede zwischen 2017 und 2018 und beobachtete sogar eine Korrelation zwischen der Anzahl der Bestellungen und dem Durchschnittswert.

Die visuelle Robustheit ist hervorragend und die Antwort passt gut zur beschreibenden Aufgabe. Sie erreicht nicht die Tiefe der Erkenntnis, die Qwen3.8 durch den Vorschlag konkreter Korrekturmaßnahmen gezeigt hatte, bleibt aber dennoch vollständig und gut organisiert.

**Note: 5/5.**

### Code-Generierung: Der maximale Zyklus in einem Graphen

Der dritte Test verlangte die Implementierung eines Python-Algorithmus, um den Zyklus maximaler Länge in einem ungerichteten Graphen zu finden, und die Erklärung seiner Komplexität. Hier kam das erste Warnsignal: zehn Minuten Nachdenken vor der Antwort. Generierungsgeschwindigkeit nach dem Start: 5,17 Token pro Sekunde.

Die erzeugte Lösung basiert auf dynamischer Programmierung über Teilmengen, dem Held-Karp-Ansatz, und erkennt die NP-schwere Natur des Problems korrekt an. Der Code ist sauber, kommentiert, funktionsfähig und die deklarierte Komplexität, O(n² 2ⁿ), ist exakt. Aus den sichtbaren Denkspuren geht ein kurioses Detail hervor: Das Modell hatte die korrekte Lösung fast sofort identifiziert, iterierte jedoch minutenlang über dieselbe Logik weiter, wie ein Jazzmusiker, der dasselbe Solo verfeinert, bevor er es tatsächlich spielt. Die finale Qualität ist hervorragend, aber zehn Minuten Wartezeit für eine interaktive Aufgabe sind lang.

**Note: 4,9/5**, bestraft für übermäßige Verarbeitungszeit.

### Mehrsprachige Planung: Fünf Tage in Japan

Ich habe nach einem Fünf-Tage-Reiseplan in Japan für einen französischen Kunden gefragt, mit dem Haupttext auf Französisch und einem eigenen Abschnitt auf Italienisch. Geschwindigkeit: 5,34 Token pro Sekunde. Das Modell hielt die angeforderte Sprache perfekt ein und erstellte einen detaillierten Reiseplan mit praktischen Ratschlägen zu Transport, Sprachbarrieren und Streetfood sowie spezifischen kulturellen Referenzen wie Tabelog für Restaurantbewertungen, Omoide Yokocho für Retro-Atmosphäre und Pontocho für traditionelle Kyoto-Gassen. Der italienische Abschnitt war ebenso gepflegt.

Im Gegensatz zu Laguna XS-2.1, das in der vorherigen Episode eine gewisse sprachliche Unsicherheit gezeigt hatte, gab es hier keine Probleme. Die Antwort ist vollständig und reich an kulturellen Details, wenn auch prägnanter als das, was Qwen3.8 zum selben Prompt produziert hatte.

**Note: 5/5.**

### Langer Kontext: Die Nadel im 460-seitigen PDF suchen

Ich habe den gesamten AI Index Report 2025 hochgeladen (über 460 Seiten) und nach Informationen zum Wachstum der Videogenerierung sowie den genauen Seiten gefragt. Denkzeit: etwa drei Minuten. Geschwindigkeit: 5,18 Token pro Sekunde. Das Modell verwies korrekt auf die Seiten 126 und 127 unter Zitierung der spezifischen Abbildungen 2.3.11 und 2.3.12, und die Zusammenfassung enthielt präzise Details zu den im Bericht zitierten Modellen und dem nun berühmten Beispiel des "Will Smith isst Spaghetti"-Videos.

Die Präzision beim Auffinden von Informationen ist hervorragend, aber drei Minuten bleiben eine erhebliche Zeit für eine Aufgabe, die theoretisch nur das Suchen nach bereits im Text vorhandenen Informationen erfordert, anstatt lange darüber nachzudenken.

**Note: 4,9/5**, wieder bestraft für die Wartezeit.

### Räumliches Schlussfolgern: Das unordentliche Zimmer

Ich habe das Bild eines unordentlichen Zimmers hochgeladen und um eine Beschreibung sowie eine Aufräumstrategie gebeten. Antwortzeit: 50 Sekunden, diesmal angemessen. Geschwindigkeit: 5,33 Token pro Sekunde. Das Modell beschrieb den Raum nach funktionalen Bereichen mit einer logischen Aufräumstrategie, die auf praktischer Basis begründet war, indem es beispielsweise den blauen Korb als das Haupthindernis identifizierte, das zuerst bewegt werden muss.

Das visuell-räumliche Verständnis ist solide und die Antwortzeit endlich kompatibel mit dem täglichen Gebrauch.

**Note: 5/5.**
![immagine1.jpg](immagine1.jpg)
*Screenshot während der Tests zum räumlichen Schlussfolgern*

### Multi-Step-Agent: Eine Web-App planen

Ich bat darum, die Entwicklung einer Ausgabenverwaltungs-Web-App mit Tech-Stack, Projektstruktur und Roadmap für ein Team aus zwei Entwicklern zu planen. Geschwindigkeit: 5,31 Token pro Sekunde. Die Antwort kam vollständig an, mit einem modernen Stack basierend auf Next.js, NestJS, PostgreSQL und Prisma, einer Monorepo-Struktur, einer in sechs Sprints unterteilten Roadmap und im Voraus identifizierten Engpässen.

Die Note, die ich am meisten geschätzt habe, ist der pragmatische und konkrete abschließende Rat: die ersten vier Sprints auf den minimalen Funktionskern zu konzentrieren, bevor Feinheiten hinzugefügt werden. Es ist die Art von Vorschlag, die man von einem erfahrenen Projektmanager erwarten würde, nicht von einem Sprachmodell.

**Note: 5/5.**

### Lange Konversation: Vier Runden zu einer Aufgabenverwaltungs-App

Der letzte Test maß das Behalten des Konversationsgedächtnisses über vier aufeinanderfolgende Runden, in denen Tech-Stack, Benachrichtigungssystem, Datenbankschema und Skalierbarkeitsstrategien für eine Aufgabenverwaltungs-App besprochen wurden. Durchschnittsgeschwindigkeit: 5,1 Token pro Sekunde, mit einem progressiven Abfall von 5,33 auf 4,98 Runde für Runde.

Das Modell bewahrte während der gesamten Konversation seine Konsistenz, erinnerte sich an jede frühere technische Entscheidung und begründete sie auf Nachfrage. Es schlug eine hybride Architektur für Benachrichtigungen vor – WebSockets für In-App und asynchrone E-Mails, die mit BullMQ verwaltet werden –, ein vollständiges Datenbankschema und eine Skalierungs-Roadmap für zehntausend Nutzer. Die leichte Verlangsamung in späteren Runden ist natürlich; die Qualität blieb konstant.

**Note: 5/5.**

## Zusammenfassende Testtabelle
![tabella1.jpg](tabella1.jpg)
Durchschnittsnote: 4,95/5. Durchschnittsgeschwindigkeit: ca. 5,2 Token pro Sekunde.

## Der Preis für zu viel Nachdenken

Muse Glimmer 30B ist vor allem die Demonstration dessen, was es bedeutet, gleichzeitig ein dichtes und ein destilliertes Modell zu sein. Es aktiviert alle dreißig Milliarden Parameter für jedes einzelne generierte Token, und das bezahlt man mit Geschwindigkeit: etwa 5 Token pro Sekunde auf meiner Konfiguration – ein Tempo, das Geduld erfordert. Im Gegenzug ermöglicht die Destillation von Muse Spark 1.2 ihm, Verhaltensweisen und Fähigkeiten eines viel größeren Modells zu erben – ein Erbe, das eher in der Qualität der Antworten als in ihrer Schnelligkeit wahrgenommen wird.

Die Qualität ist in der Tat hoch: 4,95 von 5 im Durchschnitt über die acht Tests, genau das gleiche Ergebnis, das Qwen3.8-27B in der vorherigen Episode erzielt hat. Auf der Inhaltsebene sind die beiden Modelle kurz gesagt gleichwertig. Was sie wirklich unterscheidet, ist das Verhalten während des Wartens und der Stil der finalen Antwort.

Der auffälligste Zug von Muse Glimmer ist seine Neigung zum "long thinking" – dem langen Nachdenken vor der Antwort. Zehn Minuten im Code-Test, drei Minuten im langen PDF-Test, wobei das Modell oft weiter über dieselbe Lösung grübelt, selbst nachdem es sie bereits gefunden hat – ein wenig wie bestimmte Charaktere in Craig Thompsons Graphic Novels, die dieselbe Erinnerung immer wieder verarbeiten, bevor sie sie loslassen. Es ist ein Verhalten, das bei Problemen, die wirklich tiefes Nachdenken erfordern, eine Tugend sein kann, oder ein Mangel bei denjenigen, die eine schnelle und flüssige Interaktion in der täglichen Konversation suchen.

Der Stil der Antworten verrät wiederum eine präzise Persönlichkeit: direkt, prägnant, technisch streng, aber weniger zur Pädagogik geneigt im Vergleich zu Qwen3.8. Es ist ein Modell, das dafür entworfen zu sein scheint, mit denjenigen zu sprechen, die es bereits wissen, anstatt diejenigen zu begleiten, die noch lernen. Die native Multimodalität macht es dennoch vielseitiger als Modelle wie Laguna XS-2.1, das keine Bilder verarbeitet, und die Apache 2.0-Lizenz bleibt ein konkreter Vorteil für diejenigen, die es ohne Einschränkungen in ein kommerzielles Produkt integrieren möchten.

Wer gewinnt und wer verliert in diesem Szenario? Wer Geduld hat und technische Strenge bei komplexen Aufgaben sucht, gewinnt: Entwickler, die lokale Agenten bauen, oder diejenigen, die an Problemen arbeiten, bei denen eine längere Wartezeit im Austausch für Präzision akzeptabel ist. Wer einen reaktionsschnellen Assistenten für den täglichen Gebrauch sucht, verliert – dort bietet ein MoE wie Ornith-1.0-35B, das in einer vorherigen Episode dieser Serie getestet wurde, wahrscheinlich einen ausgewogeneren Kompromiss zwischen Geschwindigkeit und Qualität.

Es bleibt eine offene Frage, die man auf dem Tisch lassen sollte: Ist das hier beobachtete "long thinking" eine intrinsische Eigenschaft der destillierten Architektur oder ein Nebeneffekt des Trainingsprozesses, den Meta in zukünftigen Versionen korrigieren könnte? Ich habe keine definitive Antwort, und ich vermute, dass selbst Meta sie noch nicht völlig klar hat. Vorerst bleibt Muse Glimmer ein Modell, das viel denkt und wenig spricht – was je nach Bedarf seine größte Stärke oder seine offensichtlichste Einschränkung sein kann.
![tabella2.jpg](tabella2.jpg)
