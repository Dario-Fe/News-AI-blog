---
tags: [" Generative AI", "Applications", "Training"]
date: 2026-04-20
author: "Dario Ferrero"
---

# Gemma 4 lokal: 26 Milliarden auf meinem PC
![gemma4-26b.jpg](gemma4-26b.jpg)

*Es bereitet eine besondere Genugtuung, etwas laufen zu lassen, von dessen Download eigentlich abgeraten würde. Nicht die Genugtuung des Hackers, der ein System knackt – das ist etwas anderes –, sondern jene ruhigere, handwerkliche Freude dessen, der die Schrauben ein wenig über das empfohlene Drehmoment hinaus anzieht und feststellt, dass die Struktur trotzdem hält. Es ist die Art von Genugtuung, die ich diese Woche empfunden habe, als Gemma 4 26B auf meinem Consumer-PC mit einer Flüssigkeit lief, die ich nicht erwartet hatte.*

Dieser Artikel ist der zweite in einer Serie, die ich [vor einigen Wochen mit Qwen 3.5 begonnen habe](https://aitalk.it/it/qwen3.5-locale-puntata1.html). Wenn Sie diesen Text bereits gelesen haben, können Sie den nächsten Absatz überspringen. Wenn Sie hingegen zum ersten Mal hier sind, gebe ich Ihnen kurz die Eckdaten des Projekts.

## Das bereits bekannte Labor

Die Idee ist einfach: neu veröffentlichte offene Modelle zu nehmen, sie lokal auf Consumer-Hardware auszuführen und zu verstehen, was man außerhalb von Pressemitteilungen und Marketing-Benchmarks wirklich erhält. Das Werkzeug ist [LM Studio](https://lmstudio.ai/), eine Desktop-Anwendung, mit der man Modelle herunterladen und starten kann, ohne ein Terminal zu öffnen. Ein sehr nützliches Feature ist die Vorabanzeige einer Schätzung der erwarteten Performance auf der eigenen Hardware-Konfiguration. Eine farbliche Unterscheidung (Grün-Orange-Rot) erspart Stunden vergeblicher Versuche. Die Maschine ist ein mit Bedacht, aber ohne Exzesse zusammengestellter PC: AMD Ryzen 7700 Prozessor, 32 GB DDR5 RAM und eine AMD Radeon RX 9060 XT GPU mit 16 GB VRAM. Hardware für fortgeschrittene Anwender, kein Forschungslabor.

Die Methode, das betone ich hier erneut, wie ich es zu Beginn des Artikels über Qwen getan habe, ist nicht wissenschaftlich im akademischen Sinne. Es gibt kein Peer-Review-Protokoll, keine statistisch signifikante Stichprobe von Prompts und keine von einer Konferenz zertifizierte Reproduzierbarkeit. Die Tests wurden durch Abgleich der Ergebnisse mit Frontier-Modellen wie Claude und DeepSeek verifiziert, aber das macht sie nicht zu Benchmarks: Es bleiben Praxistests, durchgeführt mit den Werkzeugen eines anspruchsvollen Nutzers. Die Bewertungen zu jedem Test sind persönliche Einschätzungen, keine Urteile.

## Gemma 4: Die Familie, die Architektur, die Philosophie

Google DeepMind hat Gemma 4 am 2. April 2026 unter der Apache 2.0-Lizenz veröffentlicht. Das ist kein nebensächliches Detail: Es ist das erste Mal in der Geschichte der Gemma-Familie, dass ein Modell unter dieser Lizenz veröffentlicht wurde. Dies beseitigt jede Unklarheit über die kommerzielle Nutzung und stellt Gemma 4 auf dieselbe permissive Stufe wie Qwen 3.5, mit dem es das Open-Weight-Ökosystem teilt.

Die Familie ist in vier Varianten unterteilt: E2B und E4B, konzipiert für den Einsatz auf mobilen Geräten und Peripheriegeräten mit einem Kontextfenster von 128.000 Token, sowie die beiden größeren Varianten, das 26B MoE und das 31B Dense mit einem Kontextfenster von 256.000 Token. Das 31B Dense ist das Spitzenmodell in Bezug auf die reine Qualität und eroberte zum Zeitpunkt des Starts den dritten Platz weltweit im Arena AI Text Leaderboard – nicht nur unter den offenen Modellen, sondern unter allen Modellen absolut. Das 26B MoE belegte den sechsten Platz.

Zum 26B MoE lohnen sich zwei Zeilen zur Architektur; ich verspreche, mich kurz zu fassen. Das Schlüsselkonzept, das man für den Rest dieses Artikels im Hinterkopf behalten sollte, ist folgendes: Das 26B-Modell aktiviert während der Inferenz nur etwa 3,8 Milliarden seiner Gesamtparameter. Dies macht es deutlich schneller, als die Gesamtzahl vermuten ließe, und bringt es in Bezug auf die Geschwindigkeit in die Nähe eines 4-Milliarden-Parameter-Modells. Der Preis dafür ist, dass alle 26 Milliarden Parameter dennoch im Speicher liegen müssen. Schnell wie ein kleines Modell, schwerfällig wie ein großes: eine Rechnung, die man mit VRAM bezahlt.

Die Benchmark-Zahlen sind beeindruckend, insbesondere im Vergleich zur vorherigen Generation. Der Sprung gegenüber Gemma 3 ist schwer zu ignorieren: Bei AIME 2026 geht es von 20,8 % auf 89,2 %, bei LiveCodeBench von 29,1 % auf 80,0 % und bei GPQA Science von 42,4 % auf 84,3 %. Das ist keine inkrementelle Optimierung. In der Art und Weise, wie diese Modelle denken, hat sich etwas Strukturelles geändert.
![grafico1.jpg](grafico1.jpg)
[Bild entnommen von deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

## Die Wahl jenseits des Limits

Was mein spezifisches Experiment betrifft, habe ich mich für das Testen von **Gemma 4 26B A4B Instruct Q4_K_M** entschieden, der Version mit der aggressivsten Quantisierung, die für die 26-Milliarden-Variante verfügbar ist. Die Wahl lag bewusst am Limit: LM Studio markierte diese Konfiguration als leicht außerhalb der für meine Hardware empfohlenen Kapazitäten und kennzeichnete sie mit jener orangen Farbe, die normalerweise dazu rät, die Erwartungen zu senken oder die Auswahl zu verkleinern. Ich habe den Rat ignoriert – nicht aus Sturheit, sondern weil das Testen des Limits genau der Punkt war.

Die Q4_K_M-Quantisierung reduziert die numerische Präzision der Modellgewichte von 16 Bit auf etwa 4 Bit. Dabei wird eine Technik verwendet, die versucht, den Informationsverlust weniger gleichmäßig und intelligenter zu verteilen als bei flachen Quantisierungen, wodurch die Gewichte, die das Modell für am wichtigsten hält, besser erhalten bleiben. Das praktische Ergebnis ist eine Datei, die etwa 16 GB auf der Festplatte belegt und vollständig in den 16 GB VRAM meiner GPU Platz finden kann – ein Gleichgewicht am Limit: Die Q4_K_M-Version des 26B MoE-Modells verbraucht ungefähr 16 GB, also gerade noch innerhalb der Grenzen einer Consumer-GPU wie der meinen. Der Qualitätsverlust gegenüber der vollen bfloat16-Version ist real, aber wie real? Das ist einer der Subtexte des gesamten Experiments.

Ich habe bewusst dieselben sechs Tests gewählt, die ich auch für Qwen 3.5 verwendet habe. Nicht, weil die beiden Modelle im strengen Sinne vergleichbar wären (das eine ist ein 9B Dense-Modell, das andere ein 26B MoE), sondern um eine minimale methodische Konsistenz zu wahren, die zumindest qualitative Beobachtungen ermöglicht. Es ist kein direkter Vergleich. Es ist eher so, als würde man die Temperatur mit demselben Thermometer in zwei verschiedenen Städten messen: Die Zahlen sind vergleichbar, die Städte nicht.

## Sechs Prüfungen, sechs Urteile

### Wissenschaftliche Argumentation: Der Higgs-Mechanismus — 5/5

Der erste Test ist derjenige, den ich als allgemeinen Gradmesser für die Intelligenz des Modells verwende: die Erklärung des Mechanismus der elektroschwachen Symmetriebrechung im Standardmodell, die Rolle des Higgs-Feldes und die Frage, warum W- und Z-Bosonen an Masse gewinnen, während das Photon masselos bleibt. Explizite Anforderung: präzise Sprache, aber für einen Physikstudenten verständlich.

Die Antwort hat mich überrascht – weniger durch die Korrektheit der Inhalte als vielmehr durch die Qualität der Darstellung. Das Modell gliederte die Erklärung in vier logische Abschnitte mit der Struktur, die auch ein guter Universitätsprofessor verwenden würde: beginnend mit der Eichinvarianz über das „mexikanische Hut“-Potenzial mit der Bedingung für das Vorzeichen des Massenterms bis hin zu den konkreten physikalischen Konsequenzen. Die Formeln waren korrekt wiedergegeben: die Eichgruppe SU(2)_L × U(1)_Y, der Vakuumerwartungswert, die Massen der Bosonen. Aber die wahre Stärke lag in der Fähigkeit, jede Formel mit einem verständlichen mentalen Bild zu begleiten. Als das Modell schrieb, dass die winkelabhängigen Freiheitsgrade von den Eichbosonen „gefressen“ werden, übersetzte es ein abstraktes mathematisches Konzept in etwas, das ein Physikstudent im zweiten Jahr sofort wiederkennt. Das ist der Unterschied zwischen einem Wörterbuch und einem Professor.

Ein technisches Detail ist erwähnenswert: Trotz der Komplexität der Argumentation und der Länge der Antwort dachte das Modell nur 2,2 Sekunden nach und generierte den Text mit etwa 24 Token pro Sekunde. Für ein Modell, das theoretisch 26 Milliarden Parameter umfasst, ist das eine erstaunliche Geschwindigkeit, die eben durch die MoE-Architektur ermöglicht wird, die den Großteil der Gewichte während der Generierung inaktiv hält. **Bewertung: 5/5.**

### Multimodalität: Lesen einer unscharfen Tabelle — 5/5

Der zweite Test sollte die visuellen Fähigkeiten mit einem bewusst schwierigen Input prüfen: ein kleines und unscharfes Foto einer Tabellenkalkulation für ein monatliches Familienbudget. Die Aufgabe bestand darin, den Inhalt, die wichtigsten Daten und die sich abzeichnenden Trends zu beschreiben.

Das Modell benötigte etwa zehn Sekunden zur Analyse des Bildes – eine deutlich längere Zeit als beim vorherigen Test, was für eine visuelle Aufgabe verständlich ist –, bevor es die Generierung mit etwa 23 Token pro Sekunde startete. Die Antwort war bemerkenswert vollständig: Es identifizierte korrekt die Struktur des Dokuments – ein Excel-Template mit Abschnitten für Einnahmen, Ersparnisse und Ausgaben, jeweils mit Spalten für Budget, Ist-Wert und Differenz. Es las die numerischen Schlüsselwerte mit millimetergenauer Präzision: monatliche Nettoersparnis bei einem geplanten Budget von 1.350 Dollar, tatsächlich 2.624 Dollar, positive Differenz von 1.274 Dollar. Es bemerkte sogar das Vorhandensein eines horizontalen Balkendiagramms auf der rechten Seite des Blattes.

Aber der Teil, der bestätigte, dass es sich nicht um eine bloße Transkription handelte, war die Analyse: Das Modell beobachtete autonom, dass trotz der gestiegenen Einnahmen die tatsächlichen Gesamtausgaben nahe am geplanten Budget geblieben waren, und zog daraus einen logischen Schluss über die Effizienz des Sparens. Von einem unscharfen Bild zu einer Cashflow-Analyse. **Bewertung: 5/5.**
![grafico3.jpg](grafico3.jpg)
Bild von meinem PC während der Tests in LM Studio

### Code: Ein NP-schweres Problem mit Autokorrektur — 4,5/5

Der dritte Test war der technischste: die Implementierung eines Algorithmus in Python, um den Zyklus maximaler Länge in einem ungerichteten Graphen zu finden, wobei Graphen mit mehreren Zyklen zu berücksichtigen waren und die Zeitkomplexität erklärt werden sollte.

Die positiven Aspekte waren beachtlich. Das Modell erklärte ohne Zögern, dass das Problem NP-schwer ist und dass kein polynomialer Algorithmus für dessen Lösung in allgemeinen Graphen existiert. Es wählte Backtracking mit Tiefensuche als korrekten Ansatz – genau das, was jeder verwenden würde, der sich ernsthaft mit Algorithmen beschäftigt hat. Die Darstellung mittels Adjazenzliste mit Dictionary war effizient, die Logik zur Untersuchung einfacher Pfade korrekt, die Erklärung der Zeitkomplexität klar und ehrlich.

Allerdings enthielt die erste Version des Codes drei Syntaxfehler: ein Schlüsselwort, das als `not be in` statt `not in` geschrieben war, ein falscher Variablenname in einem Methodenaufruf und eine weitere Variable, die in der Schleifenbedingung falsch geschrieben war. Drei Fehler, die für sich genommen die Ausführung ohne manuellen Eingriff verhindert hätten.

Doch hier kommt der interessanteste Teil der Bewertung. Als ich das Modell ganz allgemein und ohne Hinweis auf die Art der Fehler bat, den Code auf etwaige Syntaxprobleme zu prüfen, identifizierte und korrigierte es alle drei beim ersten Versuch. Mit anderen Worten: Es wusste bereits, wie der korrekte Code geschrieben werden musste – es hatte ihn beim ersten Mal lediglich nicht mit genügend Sorgfalt geschrieben. Dieses Verhalten spiegelt die realistische Nutzung dieser Werkzeuge wider: Selten verlässt sich ein Programmierer blind auf die erste generierte Version. Die Fähigkeit, die eigenen Fehler auf allgemeine Aufforderung hin zu diagnostizieren, ist fast ebenso wertvoll wie ein perfekter erster Entwurf. Fast. **Bewertung: 4,5/5.**

### Mehrsprachigkeit und Planung: Japan auf Französisch — 4,8/5

Der vierte Test bewertete die Mehrsprachigkeit und komplexe Planung: Es galt, als Reisebüro zu agieren und eine fünftägige Japanreise für einen französischen Kunden zu planen, der kein Englisch spricht, mit Fokus auf historische Tempel und Street Food, ergänzt um einen abschließenden Abschnitt auf Italienisch mit Tipps für einen italienischen Touristen.

Das Französisch war tadellos, flüssig und fehlerfrei, mit einem professionellen, aber nicht unterkühlten Tonfall. Die Routenplanung war logistisch realistisch: der erste Tag in Asakusa mit dem Senso-ji und einem Izakaya am Abend; der zweite zwischen dem Meiji-jingu-Schrein und Shibuya; der dritte mit dem Shinkansen nach Kyoto mit dem Kiyomizu-dera und Gion; der vierte zum Goldenen Pavillon und zum Bambuswald von Arashiyama; der fünfte zum Fushimi Inari. Jeder Tag war, wie gefordert, ausgewogen zwischen historischer Stätte und gastronomischem Erlebnis. Die Kenntnisse über Japan waren überraschend detailliert: Nennung von Orten wie Sannenzaka und Ninenzaka, spezifischer Speisen wie Age-manju, praktische Tipps zur Suica-Karte und zur App „Japan Transit“ sowie die Erwähnung der Depachika – der Untergeschosse der großen japanischen Kaufhäuser –, ein Insider-Detail, das man in allgemeinen Reiseführern nicht findet.

Allerdings wies der abschließende italienische Abschnitt zwei Fehler auf, die nicht ignoriert werden können. Würde [Subject]... Der erste war „suggeramenti“ anstelle von „suggerimenti“ – ein Begriff, der im Italienischen schlicht nicht existiert. Der zweite war seltsamer: Das Wort „comprare“ (kaufen) erschien mit einer kyrillischen Endung geschrieben, „compraть“, als hätte das Modell kurzzeitig den Faden der Sprache verloren. Zwei Fehler in einhundertfünfzig Wörtern Italienisch – bei einer Sprache, die nicht zu den seltensten der Welt gehört. Von einem Modell, das Unterstützung für über 140 Sprachen verspricht, würde man eine größere Robustheit auch bei den Sekundärsprachen einer Antwort erwarten. **Bewertung: 4,8/5.**
![grafico2.jpg](grafico2.jpg)
[Bild entnommen von deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

### Langer Kontext: 460 Seiten KI beim ersten Versuch — 5/5

Den fünften Test halte ich für den aussagekräftigsten für eine reale Nutzung des Modells: Ich habe den [AI Index Report 2025 von Stanford](https://aiindex.stanford.edu/report/) hochgeladen, ein PDF mit etwa 460 Seiten und über 20 Millionen Zeichen – dasselbe Dokument, das auch im Test mit Qwen 3.5 verwendet wurde. Ich bat das Modell ganz allgemein, mir etwas über das Wachstum der Videogenerierung zu erzählen und mir die Seiten zu nennen, auf denen die Daten zu finden sind.

Die Antwort erfolgte nach 4,4 Sekunden Verarbeitungszeit mit 22 Token pro Sekunde. Das Modell identifizierte korrekt die Seiten 125, 126 und 127 – kein vager Verweis auf das „mittlere Kapitel“, sondern präzise und überprüfbare Referenzen. Es lieferte dann eine strukturierte Zusammenfassung der Inhalte: Stable Video Diffusion von Stability AI, Sora von OpenAI (vorgestellt im Februar 2024 und im Dezember veröffentlicht), Movie Gen von Meta mit Editierfunktionen und Audio-Integration sowie Veo und Veo 2 von Google. Es zitierte sogar das berühmte Beispiel des Prompts „Will Smith eating spaghetti“ – jenen Test, der in der KI-Community zum Meme wurde, um die Fortschritte bei der Videogenerierung zu dokumentieren.

Der Vergleich mit der Erfahrung bei Qwen 3.5 ist aufschlussreich: Das 9-Milliarden-Modell hatte vier Versuche und eine explizite Aufforderung benötigt, im Chat zu antworten, um ein ähnliches Ergebnis zu erzielen. Gemma 4 antwortete beim ersten Versuch ohne Zögern. Das Kontextfenster von 256.000 Token erwies sich nicht nur als technische Spezifikation, sondern als tatsächlich nutzbare Fähigkeit auf Consumer-Hardware. **Bewertung: 5/5.**

### Räumliches Denken: Das Zimmer im Chaos — 4,9/5

Der letzte Test war derjenige, den ich am meisten liebe, weil er etwas misst, das schwer zu standardisieren ist: die visuell-räumliche Intelligenz. Ich habe ein Foto eines stark unordentlichen Zimmers hochgeladen – dasselbe, das auch für Qwen 3.5 verwendet wurde – und bat darum, die Anordnung der Gegenstände zu beschreiben und Vorschläge zum Aufräumen zu machen, um mehr Platz zu schaffen. Das Modell benötigte 7,5 Sekunden zur Verarbeitung, die zweitlängste Zeit des gesamten Tests.

Die Antwort begann mit einem Satz, den ich nicht verstanden habe: „In den Dateien des Benutzers wurden keine Zitate für diese Anfrage gefunden.“ Ein Satz völlig außerhalb des Kontexts, als hätte das Modell einen Dokumentensuchmechanismus aktiviert, der nichts mit der visuellen Aufgabe zu tun hatte. Nach dieser anfänglichen Merkwürdigkeit war der Rest der Antwort jedoch exzellent.

Die Beschreibung war präzise: Doppelbett auf der rechten Seite mit teilweise bedeckten weißen Laken, zwei hohe und schmale Regale, korrekt positioniert in Bezug auf Fenster und Schreibtisch, grauer Schreibtisch auf der linken Seite, zwei Fenster mit vertikal gestreiften Vorhängen. Aber der wirklich beeindruckende Teil war die Beschreibung der Gegenstände auf dem Boden: verstreute Kleidung, Schuhe (darunter ein Paar Flip-Flops), Taschen, Wäschekörbe und das Detail, dass einer der Körbe blau mit Mustern war. Diese feine Beobachtungsgabe ist bemerkenswert.

Die einzige kleine Ungenauigkeit betraf den Spiegel: Das Modell platzierte ihn auf einem Schrank oder einer Kommode, während er auf dem Foto an der Eingangstür montiert war. Ein verständlicher Fehler in einem zweidimensionalen Bild, in dem die Unterscheidung zwischen Tür und Schrank zweideutig sein kann.

Der Aufräumplan war logisch und gut begründet: zuerst Kleidung und Stoffe vom Boden entfernen, da sie das Haupthindernis beim Gehen darstellen; dann Körbe und Taschen in einen dafür vorgesehenen Bereich bringen; schließlich Schreibtisch und Regale ordnen, um das Gefühl der visuellen Überladung zu verringern. Die Priorität „Bodenfläche freimachen“ war korrekt und praxisnah. **Bewertung: 4,9/5.**
![tabella-confronto.jpg](tabella-confronto.jpg)

*Einfach nur zum Spaß – angesichts der Unmöglichkeit eines direkten Vergleichs aufgrund der unterschiedlichen Größe und Eigenschaften – schlage ich Ihnen hier eine Tabelle vor, in der Sie Ihre eigenen Bewertungen vornehmen und Ihre Wahl je nach verfügbarer Hardware treffen können. Trotz der unterschiedlichen Größen sind die Ergebnisse sehr ähnlich, wobei je nach Aufgabe mal das eine, mal das andere Modell bevorzugt wird. Ich muss jedoch hinzufügen, dass Qwen 3.5 9b bei späterer Nutzung gelegentlich Blockaden und Nicht-Antworten zeigte, was bei Gemma 4 26b nicht vorkam.*

## Was unterm Strich bleibt

Der arithmetische Mittelwert der sechs Tests liegt bei 4,87 von 5 Punkten. Eine Zahl, die man ehrlich in den Kontext einordnen muss.

Wir sprechen hier von einem Modell mit insgesamt 26 Milliarden Parametern, quantisiert in seiner am stärksten komprimierten Version, ausgeführt auf Consumer-Hardware, die leicht unter den empfohlenen Spezifikationen liegt – lokal, ohne Cloud, ohne API, ohne Kosten pro Token. Dass es flüssig in Geschwindigkeiten läuft, die eine reaktionsschnelle Interaktion ermöglichen, ist an sich schon ein bemerkenswertes Ergebnis. Dass es mit dieser Qualität antwortet, macht es zu etwas noch Interessanterem.

Der Vergleich mit Qwen 3.5 9B, dem Subjekt des vorherigen Tests, ist aufgrund des Größenunterschieds nicht direkt, aber einige qualitative Beobachtungen treten deutlich hervor. Gemma 4 bewältigt langen Kontext mit einer höheren Zuverlässigkeit, antwortet beim ersten Versuch ohne Aufforderung und zeigt eine robustere erzählerische Kohärenz bei komplexen Aufgaben. Dafür zahlt es einen kleinen Preis bei der syntaktischen Perfektion des Codes in der ersten Generierung und zeigt einige Schwächen bei Sekundärsprachen innerhalb derselben Antwort. Das ist kein überraschender Trade-off für ein Modell dieser Größe.

Die Frage, die offen bleibt und die den Rahmen dieses Experiments sprengen würde, ist, wie viel die Q4_K_M-Quantisierung im Vergleich zur Vollversion tatsächlich an Qualität gekostet hat. Die Ergebnisse sind hoch genug, um es schwer zu machen, einzuschätzen, wie viel Spielraum nach oben noch bestanden hätte. Vielleicht viel, vielleicht überraschend wenig. Es wäre ein interessantes Experiment für jemanden, der Zugang zu Hardware mit mehr VRAM hat.

Was ich mit Sicherheit sagen kann, als Enthusiast, der verstehen will, was mit normalen Mitteln im Jahr 2026 möglich ist: Die Grenze zwischen „nur in der Cloud möglich“ und „lokal möglich“ hat sich erneut verschoben. Nicht nur ein bisschen. Gemma 4 26B MoE liefert selbst in seiner am stärksten komprimierten Version auf Hardware, die viele fortgeschrittene Nutzer bereits besitzen, Antworten, für die bis vor wenigen Monaten noch ein API-Aufruf bei einem Frontier-Modell nötig gewesen wäre. Das ist für mich die wichtigste Erkenntnis, mehr als jede einzelne Note.

Eines ist sicher: Das, was ich im Januar als den Trend des Jahres bezeichnet habe – das Rennen um [lokale Small Language Models](https://aitalk.it/it/slm-2026.html) –, bestätigt sich nicht nur, sondern nimmt rasant an Fahrt auf. Und wir haben erst April.
