---
tags: ["Research", "Applications", "Training"]
date: 2025-11-17
author: "Dario Ferrero"
---

# TOON schreibt die Datenregeln für das KI-Zeitalter neu. Was wird aus JSON?
![toon.jpg](toon.jpg)


*Es gibt ein Paradoxon in der Wirtschaft der künstlichen Intelligenz, das nur wenige bemerken, bis sie auf die Rechnung schauen. Jedes Mal, wenn wir Daten an GPT, Claude oder Gemini senden, bezahlen wir für jedes einzelne Zeichen. Nicht für die Komplexität der Anfrage, nicht für die Intelligenz der Antwort, sondern für die Ausführlichkeit des Formats. Diese geschweiften Klammern, die JSON so vertraut machen? Sie kosten Geld. Die Anführungszeichen, die jeden Schlüssel abgrenzen? Wertvolle Token. Die Doppelpunkte, die Schlüssel und Werte trennen? Weitere Cents, die wegfliegen, multipliziert mit Millionen von API-Aufrufen.*

Als Johann Schopplich Anfang 2025 [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) veröffentlichte, war die erste Reaktion der Community die, die alle einfachen, aber genialen Ideen begleitet: "Warum zum Teufel bin ich nicht darauf gekommen?". Wie der japanische Minimalismus auf die Datenserialisierung angewendet, eliminiert TOON alles, was nicht gebraucht wird. Keine geschweiften Klammern, keine überflüssigen Anführungszeichen, keine zwanghaften Wiederholungen derselben Schlüssel. Nur die Essenz der Daten, sauber wie ein Haiku.

## Die unsichtbaren Kosten der geschweiften Klammern

JSON entstand in einer Zeit, in der Computer hauptsächlich miteinander sprachen. Douglas Crockford extrahierte es aus JavaScript als glückliches Nebenprodukt, wobei er die Lesbarkeit für den Menschen und die plattformübergreifende Kompatibilität über die Effizienz stellte. Jahrelang funktionierte dieser Kompromiss hervorragend. Die zusätzlichen Bytes, die zur Darstellung eines Objekts mit all seinen syntaktischen Verzierungen benötigt wurden, waren im Vergleich zur Einfachheit des Parsens und der Vertrautheit des Formats irrelevant.

Aber das Aufkommen von Large Language Models hat die Spielregeln geändert. Wenn die API-Kosten pro Million Token berechnet werden, sind diese geschweiften Klammern plötzlich keine harmlosen syntaktischen Konventionen mehr. Sie werden zu einer messbaren wirtschaftlichen Ineffizienz. JSON kann doppelt so viele Token wie andere Formate verbrauchen, um dieselben Daten darzustellen, und das, bevor man bedenkt, dass die Modelle genau mit Bergen von JSON trainiert wurden, was es paradoxerweise weniger effizient für die Verarbeitung macht.

Betrachten wir ein reales Beispiel. Eine Liste von einhundert GitHub-Repositorys mit vollständigen Metadaten: Sterne, Forks, Beschreibungen, Zeitstempel. In formatiertem JSON verbraucht diese Struktur 15.145 Token. Dieselbe identische Information in TOON? 8.745 Token. Eine Reduzierung um 42,3 %. Wir sprechen nicht von verlustbehafteter Komprimierung oder magischen Tricks. Es sind dieselben Informationen, Bit für Bit umkehrbar, nur intelligenter dargestellt.

Die Mathematik wird bei Zeitreihendaten noch brutaler. Einhundertachtzig Tage Web-Metriken (Ansichten, Klicks, Konversionen, Einnahmen) erfordern 10.977 Token in JSON gegenüber 4.507 in TOON, eine Ersparnis von 58,9 %. Wenn man diese Zahlen mit Tausenden von täglichen Anfragen in einer Unternehmensanwendung multipliziert, wird der Unterschied zwischen einem nachhaltigen Projekt und einem, das das Budget verbrennt, greifbar.

## Wenn weniger mehr wird

Die zentrale Erkenntnis von TOON ist entwaffnend einfach: Wenn Sie einheitliche Arrays von Objekten mit denselben Feldern haben, warum sollten Sie die Schlüssel für jedes einzelne Element wiederholen? Es ist, als ob jede Zeile in einer Excel-Tabelle die Spaltenüberschrift enthalten müsste. Ineffizient und redundant.

TOON leiht sich die Einrückung von YAML für verschachtelte Strukturen und das tabellarische Format von CSV für einheitliche Arrays aus und optimiert dann beides für den spezifischen Kontext von Large Language Models. Das Ergebnis ist ein Format, das auf den ersten Blick offensichtlich erscheint, aber ein Umdenken bei einigen grundlegenden Annahmen darüber erfordert, wie wir Daten darstellen.

Ein Array von Benutzern in klassischem JSON wiederholt zwanghaft dieselbe Struktur:
![json-format.jpg](json-format.jpg)

TOON deklariert die Struktur einmal im Header und listet dann nur die Werte auf:
![toon-format.jpg](toon-format.jpg)

Der Marker `[2]` teilt explizit die Länge des Arrays mit, während `{id,name,role}` das Schema definiert. Jede nachfolgende Zeile enthält nur die Rohdaten, getrennt durch Kommas. Es ist funktionale Eleganz im Bauhaus-Sinne: Die Form folgt der Funktion, null überflüssige Ornamente.

Diese syntaktische Ökonomie manifestiert sich in drei komplementären Strategien. Erstens ersetzt die Einrückung die geschweiften Klammern für verschachtelte Objekte. Zweitens werden Zeichenketten nur dann in Anführungszeichen gesetzt, wenn dies unbedingt erforderlich ist, um Mehrdeutigkeiten zu vermeiden (führende oder nachgestellte Leerzeichen, Steuerzeichen, Werte, die mit Booleschen Werten oder Zahlen verwechselt werden könnten). Drittens wandelt das tabellarische Format für homogene Arrays wortreiche Wiederholungen in kompakte Zeilen im CSV-Stil um.

Das Ergebnis? TOON erzielt bei strukturierten Datensätzen typischerweise eine Reduzierung des Token-Verbrauchs um 30-60 % im Vergleich zu JSON. Und es geht nicht nur darum, gesparte Zeichen zu zählen. Es ist ein Unterschied, der sich direkt in reduzierten Betriebskosten, größeren für zusätzliche Daten verfügbaren Kontextfenstern und schnelleren Antwortzeiten niederschlägt.

## Die Geometrie der Einsparung

Die offiziellen Benchmarks des TOON-Projekts erzählen eine interessante Geschichte über die Bedingungen, die die Vorteile des Formats verstärken oder verringern. Es ist keine universelle Magie, es ist angewandte Geometrie auf die Datenstruktur.

Der optimale Punkt, dieser Sweet Spot, an dem TOON am meisten glänzt, sind einheitliche Arrays von Objekten mit primitiven Werten. Ergebnisse von Datenbankabfragen, CSV-Exporte, analytische Zeitreihendaten. Je identischer Ihre Zeilen in der Struktur sind, desto mehr kann TOON den syntaktischen Overhead komprimieren, indem es das Schema nur einmal deklariert.

In Tests, die mit vier verschiedenen Modellen (GPT-5 Nano, Claude Haiku, Gemini Flash, Grok) an 154 Datenabfragefragen durchgeführt wurden, erreichte TOON eine durchschnittliche Genauigkeit von 70,1 % bei einem Verbrauch von 4.678 Token, gegenüber 65,4 % bei JSON, das 8.713 Token verbrauchte. Nicht nur wirtschaftliche Einsparungen, sondern auch eine höhere Präzision bei den Antworten. Die explizite Struktur (Länge der Arrays, Deklaration der Felder) hilft den Modellen, die Daten zuverlässiger zu parsen und zu validieren.

Die Ergebnisse variieren jedoch erheblich zwischen den Modellen. GPT-5 Nano zeigte eine Genauigkeit von 96,1 % mit TOON, während Claude Haiku bei 48,7 % stehen blieb. Diese Ungleichheit deutet darauf hin, dass das Training eine Rolle spielt: Modelle, die während des Trainings überwiegend JSON ausgesetzt waren, könnten anfangs mit alternativen Formaten Schwierigkeiten haben, unabhängig von ihrer theoretischen Effizienz.

Das Trainingsproblem ist nicht trivial. Die aktuellen LLMs wurden mit Milliarden von JSON-Token aus APIs, Konfigurationen und öffentlichen Datensätzen gefüttert. TOON wurde 2025 geboren, daher haben die neuesten Modelle relativ wenig von diesem Format in ihren Trainingskorpora gesehen. Es ist ein klassisches Bootstrap-Problem: Das Format ist effizienter, aber das Ökosystem muss sich noch anpassen.

Interessanterweise zeigen die Tests auch die Grenzen von TOON auf. Bei tief verschachtelten oder uneinheitlichen Daten reduzieren sich die Vorteile drastisch. Ein Objekt mit optionalen Feldern, die sporadisch auftreten, oder hierarchische Bäume mit vielen Verschachtelungsebenen könnten in JSON lesbarer und sogar effizienter sein. TOON eignet sich nicht gut für tief verschachtelte oder uneinheitliche Daten, bei denen JSON effizienter sein kann.
![toon-schema.jpg](toon-schema.jpg)
[Bild aus dem offiziellen GitHub-Repo](https://github.com/toon-format/toon)

## Wo es funktioniert (und wo nicht)

Die Trennung von Hype und praktischer Realität erfordert Offenheit bei den Anwendungsfällen. TOON ist nicht "das neue JSON" im Sinne eines universellen Ersatzes. Es ist ein spezialisiertes Werkzeug für ein spezifisches Problem: die Optimierung der Übertragung von strukturierten Daten zu und von Large Language Models.

Die Gewinnszenarien sind klar. Bauen Sie eine RAG-Pipeline, die Hunderte von Produktaufzeichnungen an einen LLM sendet, um Beschreibungen zu generieren? TOON senkt die Kosten. Haben Sie eine Anwendung, die täglich Tausende von Analysezeilen über GPT verarbeitet, um Erkenntnisse zu gewinnen? Sofortige Einsparungen. Müssen Sie Datenbankabfrageergebnisse mit Hunderten von Benutzern, Bestellungen oder Transaktionen zur Analyse an Claude übergeben? TOON wurde dafür geboren.

Das Format zeichnet sich aus, wenn die Struktur flach und einheitlich ist, wenn die Volumina hoch sind, wenn die Token-Kosten einen erheblichen Budgetposten darstellen. Für Anwendungsfälle wie die Generierung von Redaktionskalendern, Produktlisten, Benutzertabellen, Analysezeilen, bei denen das Token-Budget oder das Kontextfenster echte Einschränkungen sind, bietet TOON konkrete und messbare Vorteile.

Aber es gibt Bereiche, in denen JSON die Oberhand behält. Stark verschachtelte und unregelmäßige Daten, bei denen die Struktur zwischen den Datensätzen erheblich variiert, profitieren nicht vom tabellarischen Format von TOON. Komplexe Objekte mit vielen optionalen Feldern werden auch in TOON wortreich, wenn Sie das Fehlen von Werten oder variablen Strukturen verwalten müssen.

Dann ist da noch die Frage des Ökosystems. JSON verfügt über jahrzehntelange ausgereifte Werkzeuge: Debugger, Formatierer, Validatoren, Bibliotheken in jeder erdenklichen Sprache. TOON hat seine erste Version im Jahr 2025 veröffentlicht, und obwohl es Implementierungen in TypeScript, Python, Go, Rust, Java, C++, PHP, Ruby, Swift, Elixir, Dart, Clojure, Crystal und anderen Sprachen gibt, ist das Ökosystem noch jung. JSON hat jahrzehntelange Werkzeuge, während TOON neuer ist mit einem kleineren Ökosystem.

Das Debuggen ist komplizierter. Wenn in der Produktion etwas schief geht und Sie eine TOON-Payload inspizieren müssen, können Sie nicht einfach die Entwicklertools des Browsers öffnen und einen "Pretty-Print" durchführen. Sie müssen zurück in JSON konvertieren, das Problem identifizieren und dann wieder konvertieren. Das fügt dem Entwicklungsworkflow Reibung hinzu, insbesondere in Teams, die mit dem Format noch nicht vertraut sind.

Die Einführung in Unternehmen bringt organisatorische Fragen mit sich, die über die reine Technik hinausgehen. Ein Team davon zu überzeugen, das Datenformat zu ändern, erfordert die Zustimmung auf mehreren Ebenen. Entwickler müssen die neue Syntax lernen. Legacy-Code muss aktualisiert werden oder mit Konvertierungsschichten koexistieren. CI/CD-Prozesse müssen angepasst werden. Teams und Führungskräfte davon zu überzeugen, ein neues Format für eine Kostensenkung von 30-60 % zu übernehmen, klingt auf dem Papier einfach, aber in der Praxis gibt es immer Widerstand gegen Veränderungen.

Die pragmatischste Strategie, die von Teams, die mit TOON experimentieren, angewendet wird, ist eher chirurgisch als ganzheitlich. Sie ersetzen JSON nicht im gesamten Stack. Sie behalten JSON als internes Format für Speicherung, externe APIs und Verträge zwischen Diensten bei. Sie verwenden TOON ausschließlich als Optimierungsschicht für die Kommunikation mit LLMs, wo die Token-Effizienz wirklich zählt. Der optimale Ansatz für die meisten Organisationen kombiniert beides: JSON als interner Standard für Kompatibilität und TOON für spezifische LLM-Optimierung.

Sie konvertieren bei Bedarf, an stark frequentierten Punkten, an denen sich die Einsparungen vervielfachen: Endpunkte, die täglich Tausende von LLM-Aufrufen generieren, Batch-Pipelines, die große Volumen verarbeiten, Echtzeitanwendungen, bei denen eine reduzierte Latenz einen Unterschied in der Benutzererfahrung macht.

## Der wahre Preis der Effizienz

Die Reduzierung des Token-Verbrauchs ist nicht nur eine wirtschaftliche Optimierung. Es ist auch ein Umweltproblem, mit dem sich die Tech-Branche immer noch schwer tut, offen umzugehen. Jedes verarbeitete Token erfordert GPU-Zyklen, jeder Zyklus verbraucht Energie, jede Kilowattstunde trägt zur CO2-Bilanz von Rechenzentren bei.

Die wachsende Nachfrage nach generativer KI hat bereits den globalen Energieverbrauch der Datenverarbeitung erhöht, und die Optimierung der Token-Nutzung wird zu einer neuen Grenze nicht nur für die Effizienz, sondern auch für die Nachhaltigkeit. Wenn TOON die zur Darstellung eines Datensatzes benötigten Token um 50 % reduziert, reduziert es auch etwa die Hälfte der für die Verarbeitung dieser Anfrage erforderlichen Energie. Multipliziert mit Millionen von API-Aufrufen über Tausende von Anwendungen hinweg, ist die aggregierte Auswirkung nicht zu vernachlässigen.

Aber Effizienz hat auch versteckte Kosten anderer Art. TOON führt zu kognitiver Komplexität für Entwickler. Sie müssen die Regeln für die Anführungszeichen von Zeichenketten lernen (Wann sind Anführungszeichen erforderlich? Was passiert mit alternativen Trennzeichen?). Sie müssen verstehen, wann Sie das tabellarische Format im Vergleich zum Listenformat verwenden sollten. Sie müssen Randfälle wie Arrays von Arrays oder Objekte mit verstreuten optionalen Feldern behandeln.

Die Lernkurve ist nicht steil, aber sie existiert. Für kleine Teams oder Projekte mit bescheidenen Mengen an LLM-Aufrufen könnte die in das Lernen und die Implementierung investierte Zeit die wirtschaftlichen Einsparungen übersteigen. Für kleine Anwendungen, die 100 LLM-Aufrufe pro Tag machen, ist die Entwicklungszeit zur Implementierung von TOON wahrscheinlich die Einsparungen nicht wert.

Dann ist da noch die Frage der Reife des Formats. Die TOON-Spezifikation ist derzeit in Version 1.4, mit sprachunabhängigen Konformitätstests, die Implementierern helfen, die plattformübergreifende Kompatibilität zu gewährleisten. Aber es ist ein Format mit weniger als einem Jahr Lebensdauer in der realen Welt. Wir wissen noch nicht, welche Randfälle bei massivem Einsatz in der Produktion auftreten werden, welche Muster sich als problematisch erweisen werden, welche weiteren Optimierungen erforderlich werden.

Das Projekt hat öffentliche Konformitätstests veröffentlicht und unterhält eine formale Spezifikation auf GitHub, positive Anzeichen für eine ernsthafte Governance. Aber die Einführung im großen Stil wird unweigerlich Probleme aufdecken, die Unit-Tests nicht erfassen. Es ist der klassische Kompromiss zwischen Early Adopter (sofortige Vorteile, Stabilitätsrisiko) und dem Warten auf die Reife (geringeres Risiko, aber in der Zwischenzeit höhere Kosten).

Der vielleicht faszinierendste Aspekt ist eher kultureller als technischer Natur. TOON zwingt uns, anders über die Darstellung von Daten nachzudenken. Dreißig Jahre lang haben wir JSON als das "natürliche" Format für strukturierte Daten betrachtet, bis zu dem Punkt, dass wir oft direkt in Begriffen von Objekten mit Schlüsseln und Werten in geschweiften Klammern denken. TOON erfordert einen Perspektivwechsel: Zuerst über die Form der Daten nachdenken (Ist sie tabellarisch? Verschachtelt? Einheitlich?) und dann über die optimale Darstellung.

Wie die funktionale Programmierung, die einem beibringt, in Begriffen von unveränderlichen Transformationen anstatt von Zustandsmutationen zu denken, oder wie die RISC-Architektur, die einfache und zahlreiche Anweisungen anstelle von wenigen komplexen Anweisungen bevorzugt, fördert TOON eine andere Denkweise. Die Eleganz der Subtraktion anstelle der Anhäufung von Features.

TOON wird JSON nicht ersetzen, so wie Markdown HTML nicht ersetzt hat oder YAML XML nicht eliminiert hat. Jedes Format hat seine eigene Nische gefunden, seinen eigenen Kontext, in dem die spezifischen Kompromisse Sinn ergeben. JSON wird der Standard für APIs, Konfigurationen und Speicherung bleiben. Aber für den spezifischen und wachsenden Bereich der Kommunikation mit Large Language Models bietet TOON eine rationale Alternative, die auf soliden Prinzipien beruht.

Die Idee hinter TOON ist die klassische Einsicht, die erst dann offensichtlich erscheint, wenn jemand sie gehabt hat: Wenn Modelle für jeden Token bezahlen, warum weiterhin ein Format verwenden, das vor vierzig Jahren zur Lösung anderer Probleme entwickelt wurde? Es ist dieselbe Art von Einsicht, die zur Entstehung von Protobuf als Ersatz für XML in der Google-Kommunikation oder von JSON selbst als leichtere Alternative zu SOAP führte.

Die relevante Frage für Entwickler und Tech-Leads ist nicht "Wird TOON JSON ersetzen?", sondern "Profitieren meine spezifischen Anwendungsfälle von der Token-Optimierung?". Wenn Sie mit großen Mengen einheitlicher strukturierter Daten arbeiten, die über LLMs laufen, wenn die API-Kosten ein wesentlicher Posten in Ihrem Betriebsbudget sind, wenn das begrenzte Kontextfenster eine echte Einschränkung in Ihren Anwendungen ist, dann verdient TOON ein ernsthaftes Experiment. Konvertieren Sie einen stark frequentierten Endpunkt, messen Sie die realen Einsparungen, bewerten Sie, ob die zusätzliche Komplexität die konkreten Vorteile wert ist.

Wenn Sie hingegen sporadische Aufrufe mit kleinen Payloads tätigen, wenn das Team klein ist und seine Zeit auf Features statt auf Optimierungen konzentrieren muss, wenn die Daten überwiegend verschachtelt und unregelmäßig sind, dann bleibt JSON die pragmatische Wahl. Vorzeitige Optimierung, wie uns Knuth gelehrt hat, ist die Wurzel allen Übels. Oder zumindest von 97 % davon.

Die Zukunft von TOON wird von zwei Faktoren abhängen: wie schnell das LLM-Ökosystem seine Modelle weiterentwickeln wird, um das Format zu erkennen und zu optimieren, und wie effektiv die Community in der Lage sein wird, ausgereifte Werkzeuge zu entwickeln, die die Einführung reibungslos gestalten. Wenn in zwei Jahren die wichtigsten LLM-Anbieter TOON als nativ unterstütztes Format neben JSON in ihren SDKs aufnehmen, wenn Editoren und Debugger Syntaxhervorhebung und Validierung für TOON integrieren, wenn RAG-Frameworks und KI-Orchestrierungsbibliotheken es sofort unterstützen, dann wird die Akzeptanz organisch wachsen.

In der Zwischenzeit bleibt TOON das, was es immer war: eine einfache, aber geniale Idee, die einen fragen lässt, warum man nicht selbst darauf gekommen ist. Und vielleicht gibt es in seiner minimalistischen Eleganz eine umfassendere Lektion für die gesamte Tech-Branche: Manchmal liegt die Innovation nicht darin, Komplexität hinzuzufügen, sondern sie zu subtrahieren.
