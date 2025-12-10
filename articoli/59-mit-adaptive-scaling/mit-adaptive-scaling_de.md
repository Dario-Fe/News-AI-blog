---
tags: ["Research", "Generative AI", "Training"]
date: 2025-12-10
author: "Dario Ferrero"
---

# Vom MIT lernen Modelle, weniger (und besser) zu denken
![mit-adaptive-scaling.jpg](mit-adaptive-scaling.jpg)

*Eine neue [MIT-Studie](https://www.arxiv.org/pdf/2506.09338) zeigt, wie LLMs ihre Rechenressourcen dynamisch anpassen und komplexe Probleme mit der Hälfte des herkömmlichen Rechenaufwands lösen können. Es gibt ein Paradoxon, das die zeitgenössische künstliche Intelligenz definiert. Die fortschrittlichsten Sprachmodelle gehen jede Frage mit dem exakt gleichen Rechenaufwand an, egal ob es darum geht, zwei plus zwei zu berechnen oder einen Satz der algebraischen Topologie zu beweisen. Es ist, als ob ein großer Mathematiker die gleiche geistige Energie aufwenden würde, um die Uhrzeit zu sagen und die Poincaré-Vermutung zu lösen.*

Wir Menschen funktionieren nicht so: Daniel Kahneman hat dies meisterhaft dokumentiert, indem er beschrieb, wie unser Gehirn fließend zwischen System 1, schnell und intuitiv, und System 2, langsam und überlegt, wechselt. Jetzt haben Forscher am MIT einen Weg gefunden, LLMs dieselbe Fähigkeit zur Modulation beizubringen.

## Das feste Budget, das Ressourcen verschwendet

Der aktuelle Ansatz des Skalierens zur Inferenzzeit ermöglicht es Sprachmodellen, bei schwierigen Problemen "länger nachzudenken". Der Mechanismus ist einfach: Anstatt eine einzige Antwort zu generieren, erkundet das Modell mehrere Denkpfade, generiert verschiedene Teillösungen, bewertet sie und wählt die vielversprechendsten aus. Stellen Sie es sich wie einen Entscheidungsbaum vor, bei dem jeder Ast einen möglichen Weg zur Lösung darstellt. Je mehr Äste Sie erkunden, desto größer sind die Chancen, den richtigen zu finden.

Das Problem ist, dass [diese Systeme ein festes Rechenbudget zuweisen](https://news.mit.edu/2025/smarter-way-large-language-models-think-about-hard-problems-1204), unabhängig von der Komplexität der Frage. Das ist, als würde man einem Schüler immer genau eine Stunde für jede Aufgabe geben, egal ob es sich um eine einfache Multiplikation oder eine Differentialgleichung handelt. Das Ergebnis ist doppelt ineffizient: wertvolle Ressourcen werden für triviale Probleme verschwendet und das Modell wird sich selbst überlassen, wenn die Schwierigkeit steigt.

In den letzten Monaten haben wir bereits darüber berichtet, wie die Forschung Alternativen zu dieser Starrheit erforscht. [Harvards Power Sampling](https://aitalk.it/it/power-sampling.html) hat gezeigt, dass anspruchsvollere Stichprobenalgorithmen bereits in den Basismodellen latente Denkfähigkeiten extrahieren können, ohne dass zusätzliches Training erforderlich ist. Aber diese Technik arbeitet immer noch mit einer festen Anzahl von MCMC-Iterationen. Die Innovation des MIT geht weiter: Sie führt ein System ein, das nicht nur dynamisch anpasst, wie das Modell denkt, sondern auch, wie viel es denkt.

## Wie adaptives Skalieren funktioniert

Die vom Team um Navid Azizan vom Labor für Informations- und Entscheidungssysteme entwickelte Technik wird als "instanzadaptives Skalieren" bezeichnet und ist konzeptionell elegant. Das System bewertet kontinuierlich zwei Dinge: wie schwierig das Problem ist, mit dem es konfrontiert ist, und wie vielversprechend die bisher generierten Teillösungen sind. Auf der Grundlage dieser Bewertungen entscheidet es spontan, ob es mehr Rechenressourcen investieren oder anhalten soll.

"Es ist genau so, wie Menschen Probleme lösen", erklärt Hao Wang, einer der Autoren der Forschung. "Wir erarbeiten einige Teillösungen und entscheiden dann: Soll ich mit einer davon weitermachen, anhalten und das Denken überprüfen oder sogar zurückgehen und von einem früheren Schritt aus weitermachen?".

Das Herzstück des Systems ist eine Komponente namens Process Reward Model oder PRM. Stellen Sie sich einen internen Supervisor vor, der das Modell bei der Arbeit beobachtet. Bei jedem Schritt des Denkprozesses untersucht das PRM die ursprüngliche Frage und alle bisher generierten Teillösungen und weist jeder einen Punktwert zu, der die Wahrscheinlichkeit schätzt, dass dieser Weg zur richtigen Antwort führt. Befindet sich das Modell auf einem sehr vielversprechenden Weg, kann es die Anzahl der zu untersuchenden Alternativen reduzieren und so Rechenleistung sparen. Wenn hingegen alle Wege wenig überzeugend erscheinen, weist es mehr Ressourcen zu, um nach besseren Auswegen zu suchen.

Der Unterschied zu früheren Systemen besteht darin, dass diese Bewertung nicht nur einmal am Anfang stattfindet, sondern kontinuierlich während des gesamten Lösungsprozesses. "Die Schönheit unseres Ansatzes", bemerkt Kristjan Greenewald vom MIT-IBM Watson AI Lab, "besteht darin, dass die Anpassung spontan erfolgt, während das Problem gelöst wird, anstatt alles auf einmal zu Beginn des Prozesses".
![figura1.jpg](figura1.jpg)
[Bild aus dem offiziellen Paper](https://www.arxiv.org/pdf/2506.09338)

## Das Problem der Überschätzung

Aber es gibt eine grundlegende technische Hürde, die die Forscher überwinden mussten: Bestehende Process Reward Models sind furchtbar optimistisch. Sie überschätzen systematisch die Erfolgswahrscheinlichkeiten, ein bisschen wie ein GPS, das Ihnen sagt "Sie sind fast da", obwohl es in Wirklichkeit noch zwanzig Kilometer sind. Wenn das System diesen Urteilen blind vertrauen würde, würde es das Rechenbudget zu aggressiv reduzieren, überzeugt davon, dass der Weg einfach ist, obwohl er in Wirklichkeit tückisch ist.

Young-Jin Park, der Erstautor der Studie, beschreibt das Dilemma so: "Wenn wir uns einfach auf die aktuellen PRMs verlassen würden, die die Erfolgsaussichten oft überschätzen, würde unser System das Rechenbudget zu aggressiv reduzieren. Wir mussten also einen Weg finden, die PRMs besser zu kalibrieren und das Skalieren zur Inferenzzeit effizienter und zuverlässiger zu machen."

Die MIT-Lösung ist mathematisch ausgefeilt, aber konzeptionell zugänglich. Anstatt dass das PRM eine einzelne Zahl als Wahrscheinlichkeitsschätzung generiert, erzeugt das System einen Bereich möglicher Werte durch eine Technik namens Quantilregression. In der Praxis sagt das Modell "die Erfolgswahrscheinlichkeit liegt irgendwo zwischen 30 % und 70 %" anstatt "die Wahrscheinlichkeit beträgt genau 50 %". Diese explizite Unsicherheit ermöglicht es dem System, vorsichtigere und realistischere Entscheidungen zu treffen.

Die Verbindung zu früheren Forschungen ist aufschlussreich. Wir haben bereits diskutiert, wie [Metas DeepConf](https://aitalk.it/it/ai-deepconf) das intrinsische Vertrauen von Modellen zur Selbstkorrektur nutzt und wie [Samsungs TRM](https://aitalk.it/it/trm-samsung.html) externes Retrieval verwendet, um die faktische Zuverlässigkeit zu verbessern. All diese Techniken teilen eine Annahme: Modelle müssen lernen, zu messen, wie sicher sie sich ihrer eigenen Antworten sind. Das MIT überträgt diese Idee auf den Bereich des mathematischen Denkens, wo die Überprüfung zwar algorithmisch sein kann, die Kalibrierung des Vertrauens aber entscheidend bleibt.

## Die überzeugenden Ergebnisse

Die Benchmarks lassen keinen Raum für Zweifel. Bei einer Reihe von mathematischen Standardaufgaben verwendete das MIT-System etwa die Hälfte der von herkömmlichen Ansätzen benötigten Rechenleistung bei gleichbleibender Genauigkeit. Aber es gibt ein noch interessanteres Ergebnis: Kleinere, ressourcenärmere Modelle, die mit dieser Technik ausgestattet sind, schnitten bei komplexen Problemen genauso gut oder sogar besser ab als viel größere Modelle.

Denken Sie über die Auswirkungen nach. Ein Modell mit sieben Milliarden Parametern, das günstig im Betrieb ist und wenig Energie verbraucht, kann, wenn es intelligent eingesetzt wird, mit Giganten mit siebzig Milliarden Parametern bei Problemen konkurrieren, die tiefes Denken erfordern. Nicht weil das kleine Modell auf magische Weise intelligenter geworden ist, sondern weil es gelernt hat, seine begrenzten Ressourcen dort zu konzentrieren, wo sie wirklich gebraucht werden.

Dies ist besonders relevant im Kontext des [Denkens zur Testzeit](https://aitalk.it/it/articolo-hrm.html), wo wir gesehen haben, wie sich die intelligente Zuweisung von Rechenressourcen als eine wichtige Grenze der KI herauskristallisiert. Das MIT legt nahe, dass die Zukunft nicht unbedingt darin besteht, immer größere Modelle zu entwickeln, sondern den bestehenden beizubringen, wann es sich lohnt, lange nachzudenken und wann eine schnelle Antwort ausreicht.
![figura2.jpg](figura2.jpg)
[Bild aus dem offiziellen Paper](https://www.arxiv.org/pdf/2506.09338)

## Konkrete Anwendungen und Perspektiven

Die praktischen Auswirkungen sind unmittelbar. Die Codegenerierung ist ein natürlicher Kandidat: Einige Programmierprobleme sind triviale syntaktische, andere erfordern komplexes algorithmisches Denken. Ein System, das diesen Unterschied erkennt und sich entsprechend verhält, kann die Betriebskosten für Dienste wie GitHub Copilot oder Cursor drastisch senken.

Autonome KI-Agenten sind das andere fruchtbare Feld. Ein Agent, der sich in realen Situationen zurechtfinden muss, muss ständig entscheiden, wie viel er "denken" soll, bevor er handelt. Zu langes Zögern bei einfachen Entscheidungen macht ihn unbeholfen und ineffizient. Zu schnelles Handeln bei komplexen Entscheidungen führt zu Fehlern. Das MIT-Framework bietet genau den notwendigen Mechanismus der Metakognition: die Fähigkeit, die Schwierigkeit der Situation einzuschätzen und die Bedenkzeit entsprechend zuzuweisen.

Navid Azizan betont, dass die jüngste Veröffentlichung von GPT-5.1 die Wirksamkeit dieses im Paper vorgeschlagenen Ansatzes des "adaptiven Denkens" unterstreicht. "Indem wir Modelle mit der Fähigkeit ausstatten, zu wissen, was sie nicht wissen, können wir ihnen ermöglichen, mehr Rechenleistung für die schwierigsten Probleme und die vielversprechendsten Lösungswege aufzuwenden und dabei viel weniger Token für die einfachen zu verwenden. Dies macht das Denken sowohl zuverlässiger als auch wesentlich effizienter."

## Die nicht zu ignorierenden Grenzen

Aber es wäre naiv, die noch offenen Herausforderungen zu ignorieren. Das System funktioniert hervorragend in Bereichen, in denen die Überprüfung algorithmisch ist, wie Mathematik oder Codierung. Aber was passiert, wenn die "Korrektheit" nuanciert oder subjektiv ist? Wie bewertet ein PRM, wie vielversprechend eine Teillösung für ein Problem des kreativen Designs oder einer komplexen ethischen Entscheidung ist?

Und dann ist da noch die Frage der Halluzinationen, die Achillesferse aller Sprachmodelle. Ein System, das autonom entscheidet, wie viel es denken soll, kann paradoxerweise gefährlicher werden, wenn sein Vertrauen schlecht kalibriert ist. Es könnte sich schnell davon überzeugen, Recht zu haben, gerade wenn es völlig erfundene Ausgaben generiert. Deshalb ist die Kalibrierung des PRM kein technisches Detail, sondern eine absolute Notwendigkeit.

Die Forscher sind transparent über die nächsten Schritte. Sie wollen die Technik an breiteren Anwendungen testen und weitere Verwendungsmöglichkeiten der Kalibrierungsmethode untersuchen, einschließlich Reinforcement Learning und Feinabstimmung. Die grundlegende Intuition ist jedoch bereits klar: Ein Modell, das lernt, seine kognitive Anstrengung zu dosieren, ist näher an etwas, das wir als flexible Intelligenz bezeichnen könnten.

Akash Srivastava von IBM Software, der nicht an der Forschung beteiligt war, sieht es aus industrieller Perspektive: "Menschliche Mitarbeiter lernen bei der Arbeit, einige CEOs haben als Praktikanten angefangen, aber die heutigen Agenten bleiben weitgehend statische probabilistische Softwareteile. Arbeiten wie dieses Paper sind ein wichtiger Schritt, um das zu ändern: Agenten zu helfen, zu verstehen, was sie nicht wissen, und Mechanismen für eine kontinuierliche autonome Verbesserung zu entwickeln."
![figura3.jpg](figura3.jpg)
[Bild aus dem offiziellen Paper](https://www.arxiv.org/pdf/2506.09338)

## Der rote Faden der intelligenten Effizienz

Es gibt ein Muster, das sich in der KI-Forschung des Jahres 2025 immer deutlicher abzeichnet. Harvards Power Sampling hat uns gezeigt, dass anspruchsvolle Fähigkeiten bereits in den Basismodellen vorhanden sein können, man muss nur wissen, wie man sie extrahiert. Samsungs TRM hat gezeigt, dass strategisches Retrieval rohe Speicherkapazität schlägt. DeepConf hat enthüllt, dass Selbstreflexion weniger kostet als blindes Skalieren. Und jetzt bestätigt das MIT, dass die dynamische Ressourcenzuweisung feste Budgets übertrifft.

Der gemeinsame Nenner ist intelligente Effizienz. Nicht mehr nur "größere Modelle bauen und ihnen mehr Daten geben", sondern "Modellen beibringen, wann es sich lohnt, groß zu sein". Es ist eine notwendige Reifung für eine Branche, die mit steigenden Energiekosten und Nachhaltigkeitsdruck konfrontiert ist.

Die kalibrierten Process Reward Models des MIT mögen wie ein technisches Nischendetail erscheinen, aber sie repräsentieren etwas Tieferes: die Konstruktion eines rechnerischen Selbstbewusstseins. Ein Modell, das weiß, wann es verwirrt ist, das einfache von schwierigen Problemen unterscheidet, das seine eigenen Fähigkeiten misst, bevor es sich engagiert. Wie die Mentaten in Dune, die ihre kognitiven Ressourcen für jede Berechnung mit manischer Präzision dosierten, lernen diese Systeme die Kunst der intelligenten Sparsamkeit.

Die Frage ist jetzt nicht, ob diese Richtung richtig ist, sondern wie schnell die Industrie sie integrieren kann. Denn zwischen einem System, das bei jeder Anfrage Energie verbrennt, und einem, das nur bei Bedarf denkt, ist der Unterschied nicht nur wirtschaftlich oder ökologisch. Er ist philosophisch: Er markiert den Übergang von Maschinen, die rechnen, zu Maschinen, die darüber "nachdenken", wie sie rechnen sollen.
