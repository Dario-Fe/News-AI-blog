---
tags: ["Generative AI", "Applications", "Research"]
date: 2026-10-26
author: "Dario Ferrero"
---

# CLM-8B: Der offene Entscheider, der Jev herausfordert
![clm-8b.jpg](clm-8b.jpg)

*Im [Beitrag über Jev](https://aitalk.it/it/jev) habe ich ein Modell beschrieben, das auf Sprache verzichtet, um nur eine einzige Sache zu tun: entscheiden. Man übergibt ihm eine Situation und eine Reihe möglicher Optionen, und es liefert eine Auswahl mitsamt zugehöriger Wahrscheinlichkeit zurück, ohne eine einzige Zeile Text zu schreiben. TypeSafe, das das Modell am 15. September auf den Markt brachte, nannte diese Kategorie System One – eine Hommage an Kahnemans schnelles Denken. Acht Tage später folgte ein Vorschlag von der Gegenseite: [CLM-8B](https://github.com/Contrastive-LM/CLM), veröffentlicht von Forschern der Stanford University und NVIDIA unter der Apache 2.0-Lizenz, somit frei herunterladbar und auf eigenen Servern installierbar.*

Es wäre verlockend, es einfach als das „freie Jev“ abzutun, doch das ist eine falsche Abkürzung. Die Idee einer direkten Antwort auf Jev ist eine journalistische Interpretation und keine Aussage der Autoren. CLM widmet sich demselben Problem – schnelles Entscheiden ohne schrittweise Textgenerierung –, jedoch mit einer anderen Architektur und einer anderen Zielsetzung. Aus den verfügbaren Daten geht ein Spezialist hervor, kein allgemeiner Ersatz.

## Zwei Encoder, ein Cache

Um den Unterschied zu verstehen, hilft ein Bild. 1975 veröffentlichten Brian Eno und Peter Schmidt die Oblique Strategies – ein Kartenset mit Aphorismen, die man zieht, wenn ein kreativer Prozess ins Stocken gerät. Das Kartenset bleibt immer dasselbe, was sich ändert, ist die Situation, in der man es zu Rate zieht. CLM funktioniert ähnlich: Die möglichen Aktionen bilden ein festes Set, und jede neue Situation wird mit den Karten verglichen, um zu ermitteln, welche am besten passt.

Technisch nutzt das Modell zwei getrennte Leser – einen für die Situation und einen für die Aktionen –, die beide in Koordinaten eines gemeinsamen Raums übersetzen. Es gewinnt die Aktion, die der Situation am nächsten liegt. Das entspricht dem Schema semantischer Suchmaschinen, trainiert mit einer InfoNCE genannten Methode, die richtige Zuordnungen belohnt und falsche bestraft. Der praktische Vorteil besteht darin, dass die Koordinaten der Aktionen nur einmal berechnet und im Speicher (dem Cache) vorgehalten werden, während bei jeder Anfrage nur die Situation eingelesen werden muss.

Jacky Kwok, Leiter des Projekts, erklärte gegenüber [VentureBeat](https://venturebeat.com/technology/stanford-and-nvidias-open-clm-8b-caches-reusable-agent-actions-and-runs-up-to-9x-faster-than-jev-in-tests), dass Jev und ein verwandtes Modell namens Laya nur die Situation im Cache ablegen. Die Trennung von CLM führe zu einem deutlich größeren Vorteil, wenn Kontexte und Aktionen lang sind oder wiederverwendet werden. Das ist die Beschreibung des Projektinitiators, die nicht von Unabhängigen überprüft wurde: Die interne Architektur von Jev ist nicht öffentlich, TypeSafe hat weder Gewichte noch Modellgrößen offengelegt, und externe Rekonstruktionen wie jene des Analysten [Archer Hume](https://archerhume.com/posts/jevs-architecture-unmasked/) bleiben ausdrücklich Mutmaßungen.

Der Cache ist kein Zaubermittel, wie die [README](https://github.com/Contrastive-LM/CLM) selbst einräumt. In den Messungen der Autoren auf einer RTX 4090 GPU benötigt eine völlig neue Situation mit oder ohne Cache etwa 28 Millisekunden, da sie ohnehin eingelesen werden muss; wiederholen sich Situationen, sinkt die Zeit von etwa 1,7 auf 0,6 Millisekunden. Der Gewinn hängt davon ab, wie häufig der Agent dieselben Szenarien erneut aufsucht (Aussage der Entwickler, nicht unabhängig repliziert).

## Wirklicher Open Source-Zugang?

Hier liegt der erste konkrete Vorteil gegenüber Jev, das ein geschlossenes, nur über API erreichbares Produkt bleibt. [Gewichte und Code stehen unter Apache 2.0](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B), ohne dass Verträge unterzeichnet werden müssen und mit der Möglichkeit, alles im eigenen Haus laufen zu lassen. Für Verfechter lokaler künstlicher Intelligenz und Datensouveränität ist das der entscheidende Punkt. Doch „offen“ umfasst drei verschiedene Ebenen.

Die erste Ebene betrifft die Gewichte, und hier liefert CLM ab – mit einer Einschränkung. Der von den Autoren trainierte Teil ist eine Datei von 75 Megabyte: Das Schwergewicht leistet Qwen3-8B von Alibaba, ein bestehendes, eingefrorenes Basismodell, an das CLM zwei kleine Köpfe ansetzt – einen für Situationen, einen für Aktionen. Laut der [Übersicht von baobab-tech](https://github.com/baobab-tech/decision-models-experiments/blob/main/docs/models/clm-8b.md) werden ein vLLM-Server für den Encoder, etwa 16 GB Speicher und, wie von den Autoren vorgegeben, eine NVIDIA-GPU benötigt. Auf dem Mac funktioniert ein Workaround Dritter, Ollama wird nicht unterstützt. Der lokale Betrieb ist machbar, aber keineswegs trivial.

Die zweite Ebene betrifft die Evaluierung. Das Repository enthält Skripte zur Reproduktion der Tests bezüglich Code und dem T-Rex-Spiel, sodass eine teilweise Überprüfung möglich ist, auch wenn dieselbe Übersicht anmerkt, dass ein im README zitierter Datensatz nicht in der Dateiliste der Organisation auftaucht. Die dritte Ebene ist das Ökosystem, das noch unreif ist: Der Leitfaden für zusätzliches Training ist laut baobab ein Text, der eher für einen autonomen Agenten als für einen menschlichen Leser verfasst wurde; Daten und Pipelines liegen in einem anderen Repository; und die Lizenzen der Trainingsdaten sind nicht aufgeführt, einschließlich der 30 Millionen plausiblen Fehlantworten, die mit Gemini 2.5 Flash-Lite generiert wurden und deren Nutzungsbedingungen laut der Übersicht für diesen Zweck unüberprüft sind.
![immagine1.jpg](immagine1.jpg)
[Bild aus dem offiziellen GitHub-Repository](https://github.com/Contrastive-LM/CLM)

## Angaben der Autoren

Alle Zahlen in diesem Abschnitt basieren auf Eigenauskünften der Entwickler. In Tests ohne aufgabenspezifisches Feintuning behauptet das README, dass CLM bei Computer-Nutzung, Spielen und Werkzeugaufrufen gleichauf mit Jev liege – bei bis zu 9-mal geringerer Latenz. Der beste Fall ist das Chrome-Dinosaurier-Spiel: 16,5 Millisekunden gegenüber 149,8, wobei beide Modelle 5 von 5 Durchläufen erfolgreich absolvierten, ebenso wie bei Super Mario. Beim BFCL v4-Benchmark für Werkzeugaufrufe erzielt CLM 95,2 % gegenüber 99,2 % bei Jev, bei Zeiten von 76,8 gegenüber 125,5 Millisekunden. Bei WikiRacing, wo eine Zielseite auf Wikipedia über Links erreicht werden muss, schließt CLM 26 von 30 Tests ab, Jev alle 30, bei 79,8 Millisekunden gegenüber 225.

Zwei Klarstellungen zur Differenzierung. Die Parität ist keineswegs einheitlich: Wo die Genauigkeit abweicht, bleibt Jev im Vorteil, und der Geschwindigkeitsvorsprung schwankt je nach Aufgabe zwischen dem 1,6- und 9-Fachen. Zudem wurde CLM auf einer lokalen GPU gemessen, während Jev ein in der Cloud gehosteter Dienst ist; aus den konsultierten Quellen geht nicht hervor, ob die Latenz von Jev die Netzwerklaufzeit beinhaltet – ein Detail, das den Vergleich erheblich beeinflusst.

Der spektakulärste Teil betrifft den Code. Nach einem leichten zusätzlichen Training vermelden die Autoren 81,6 % bei DeepSWE und 87,6 % bei Terminal-Bench 2.1, gegenüber 71,1 % und 83,1 % bei Jev. Diese Ergebnisse stammen jedoch von eigens trainierten Köpfen und nicht vom veröffentlichten Basismodell, ermittelt an kleinen Test-Sets von 38 und 30 zurückgehaltenen Aufgaben. Zudem löst CLM die Aufgaben nicht selbst: Es wählt zwischen Lösungen aus, die von größeren Frontier-Modellen erzeugt wurden – Opus 5 beim ersten Test und Fable 5 beim zweiten. Das bleibt ein interessantes Ergebnis, da es das einzige Feld ist, auf dem CLM laut den Autoren Jev übertrifft. Unabhängig reproduziert hat diese Zahlen noch niemand.

## Praxisberichte aus dem Feld

Hier kommen Dritte ins Spiel, mit drei Familien von Prüfungen, die sehr unterschiedliche Methoden und Grenzen aufweisen.

Die erste ist [local-jev-bench](https://github.com/tak-bro/local-jev-bench), ein Test auf einem Mac M3 Max mit 36 GB, zusammengefasst in der Übersicht von baobab-tech. CLM erreicht 39 % bei 105 Entscheidungen auf Englisch, 41 % auf Koreanisch und 20 % bei BANKING77, einer klassischen Liste von 20 Kategorien von Bankanfragen (wo der Zufall etwa 5 % ergäbe). Zwei andere offene Modelle im selben Test erreichen 89 %, 87 % und 89 % (Kev-4B) sowie 81 %, 84 % und 80 % (AnyJev L0). Achtung: Das ist kein Vergleich mit Jev, sondern mit anderen offenen Modellen. Den Testern gelang es zudem nicht, das offizielle README-Beispiel zur Dringlichkeitsfrage zu reproduzieren (0,852 gegenüber 0,41). Grenzen: Von den Autoren nicht vorgesehene Hardware und Testverfahren Dritter.

Die zweite ist eine [Evaluierung von michabbb](https://gist.github.com/michabbb/da531cc4720d8ec62395fc02dfdd476c) an 140 realen Verknüpfungspaaren einer Wissensdatenbank mit der direkten Frage, ob zwei Elemente verbunden sind. Bei 40 Paaren mit Referenzantwort liegt die Unterscheidungsfähigkeit (AUC, wobei 1 perfekt und 0,5 Zufall bedeutet) bei 0,77 für CLM mit auf 2.048 Token gekürzten Texten, bei 0,64 mit dem vollständigen Text und bei 0,998 für Jev. CLM stimmt mit Jev bei den Entscheidungsbereichen in etwa 44 % der Fälle überein und fällt nie unter eine Wahrscheinlichkeit von 0,22. Auch die Zeit ist schlechter: 0,52 Sekunden gegenüber 0,28, aber hier ist der Vergleich ungleich: CLM auf einem DGX Spark mit den Köpfen auf der CPU, Jev über API. Vor allem listet der Autor die Einschränkungen selbst auf: Aufgabe weicht stark von den für das Modell vorgesehenen ab, 129 von 140 Eingaben lagen über dem Kontextfenster, Referenzantworten wurden von einem Sprachmodell statt von Menschen zugewiesen, kein zusätzliches Training und Version v0.1.

Die dritte Gruppe sind Aggregatoren. [BenchLM](https://benchlm.ai/compare/clm-8b-vs-jev-1-13-0) verzeichnet auf JevBench bei Jev 8,57 gegenüber 63,29 in Version 1.4 und 1,51 gegenüber 72,13 in Version 1.5, weigert sich jedoch, wegen mangelnder vergleichbarer Daten ein Ranking zu erstellen. [Benchmark Heaven](https://benchmarkheaven.com/jev-models/clm-8b) platziert CLM auf Rang 87 von 92 unter den offenen Modellen, ist jedoch ein persönliches Beta-Projekt. Zudem wurde JevBench speziell um Modelle vom Typ Jev herum entwickelt. Das sind Anhaltspunkte, die es zu überprüfen gilt, keine endgültigen Urteile.
![immagine2.jpg](immagine2.jpg)
[Bild aus dem offiziellen GitHub-Repository](https://github.com/Contrastive-LM/CLM)

## Warum die Zahlen abweichen

Es wäre falsch zu folgern, dass jemand lügt. In Kurosawas *Rashomon* führt dasselbe Ereignis zu vier unvereinbaren Berichten, ohne dass einer der Zeugen böswillig handelt: Sie blicken aus unterschiedlichen Perspektiven darauf. Das Gleiche geschieht hier bei den Benchmarks.

Die offiziellen Tests bevorzugen die Auswahl zwischen wenigen wiederholten Aktionen, Werkzeugaufrufe, Spiele und die Auswahl aus vorgeschlagenen Antworten. Die unabhängigen Tests nutzen Klassifikationen mit vielen Kategorien, reale Support-Tickets und Bewertungen langer, strukturierter Texte. Es ändern sich die Eingabelänge (die CLM jenseits des Standardfensters von 2.048 Token stillschweigend abschneidet), die Anzahl der Kandidaten und die Häufigkeit, mit der dieselben Aktionen wiederkehren, wovon der gesamte Cache abhängt. Auch das Setup unterscheidet sich: veröffentlichtes Basismodell gegenüber eigens trainierten Köpfen.

Kwok selbst hat das offen eingeräumt: Er würde es nicht anstelle eines allgemeinen Denkmodells für mathematische Probleme, lange Texte oder komplexe Planung einsetzen. VentureBeat weist zudem auf eine strukturelle Einschränkung hin: Die Wahrscheinlichkeiten von CLM sind relativ zur jeweils übergebenen Kandidatenmenge – sind alle Optionen falsch, wählt das Modell dennoch eine davon aus. Meine Schlussfolgerung lautet: CLM kann in der Domäne, für die es geschaffen wurde, hervorragend sein und außerhalb schwach. Wie groß diese Domäne heute ist, weiß niemand mit Bestimmtheit.

## Vor- und Nachteile in der Praxis
![tabella1.jpg](tabella1.jpg)

Der Fairness halber sei daran erinnert, dass sich auch Jev zu einem guten Teil auf Zahlen stützt, die von TypeSafe deklariert wurden: Das Unternehmen selbst bezeichnet seine Messungen zu Geschwindigkeit und Kosten als intern und hat meines Wissens keine Kalibrierungskurven veröffentlicht, wie ich im [vorherigen Artikel](https://aitalk.it/it/jev) erwähnte. Bei den Kosten gibt es keinen einheitlichen Vergleich, wie VentureBeat einräumt.

Jev ist heute die verlässlichere Wahl bezüglich der reinen Genauigkeit; CLM ist die interessanteste Option für Kontrolle, vernachlässigbare Grenzkosten und geringe Latenz, erfordert aber eine Validierung am eigenen Arbeitspensum. Wer profitiert? Wer sensible Daten und wiederkehrende Abläufe hat. Wer geht ein Risiko ein? Wer es rein aufgrund von Schlagzeilen übernimmt.

## Was für ein Urteil noch fehlt

Ich benenne die Grenzen ausdrücklich, weil sie das Gesamtbild glaubwürdiger machen. Ich konnte keinen lokalen Test auf AMD-Hardware durchführen, die in der offiziellen Infrastruktur nicht als Zielplattform genannt wird. Unabhängige Tests sind spärlich und betreffen uneinheitliche Aufgaben. Es fehlen reproduzierbare Vergleiche bei identischer Aufgabe, gleichen Prompts und derselben Version von Jev, das inzwischen bei 1.13.0 angekommen ist. Das Verhalten nach zusätzlichem Training könnte sich stark ändern, ist aber von Dritten nicht dokumentiert. Es fehlen Messungen der Latenz im ungünstigsten Fall, der realen Kosten, des Speichers und des Qualitätsabfalls außerhalb der Ziel-Domäne. Schließlich war das größere multimodale Schwestermodell CLM-35B von den Autoren für Anfang Oktober angekündigt: Stand 11. Oktober ist es auf Hugging Face nicht zu finden.

## Gezielte Alternative, kein voller Ersatz

CLM-8B ist bedeutend, weil es eine offene System-One-Alternative zu geschlossenen Modellen in die Öffentlichkeit bringt, und weil es dies mit einem eigenständigen, überprüfbaren architektonischen Konzept tut. Latenz und freie Lizenz sind reale Vorteile, insbesondere für hochfrequente Agenten und kontrollierte Installationen. In den heute verfügbaren unabhängigen Tests bleibt Jev bei Klassifizierung, Ja/Nein-Entscheidungen und komplexen Texten jedoch deutlich verlässlicher.

Die richtige Frage lautet daher nicht „CLM oder Jev?“, sondern ob das eigene Arbeitspensum wiederholbare Aktionen, kurze Kandidatenmengen und den Bedarf nach lokaler Bereitstellung aufweist. Lautet die Antwort Ja, verdient CLM einen Testlauf mit eigenen Daten. Steht die allgemeine Zero-Shot-Genauigkeit ohne spezielles Training an erster Stelle, bleibt Jev die vorsichtigere Wahl. Wie bei jedem Kartenset zählt weniger die Karte selbst als die Situation, in der man sie zieht: Messen vor dem Entscheiden lohnt sich.
