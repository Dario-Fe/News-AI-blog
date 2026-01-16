---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-16
author: "Dario Ferrero"
---

# Wie DeepSeek Hardware-Beschränkungen in mathematische Innovation verwandelte
![deepseek-mhc.jpg](deepseek-mhc.jpg)

*Am 1. Januar 2026, während die Welt den Beginn des neuen Jahres feierte, veröffentlichten Forscher von DeepSeek auf arXiv ein Paper, das die Art und Weise, wie wir große Sprachmodelle trainieren, verändern könnte. Es ging nicht um ein besseres Modell oder einen größeren Datensatz, sondern um etwas Subtileres und potenziell Disruptiveres: eine [radikale Neubetrachtung der grundlegenden Architektur](https://arxiv.org/pdf/2512.24880), die der modernen künstlichen Intelligenz zugrunde liegt.*

Das Paper, das vom Gründer und CEO von DeepSeek, Liang Wenfeng, zusammen mit 18 weiteren Forschern unter der Leitung von [Zhenda Xie, Yixuan Wei und Huanqi Cao](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less) mitverfasst wurde, schlägt Manifold-Constrained Hyper-Connections vor, kurz mHC. Um zu verstehen, worum es geht, müssen wir jedoch zuerst einen Schritt zurückgehen und eine Geschichte nachzeichnen, die 2015 beginnt.

## Wenn die Einschränkung zum Hebel wird

Jahrelang war eines der frustrierendsten Probleme des Deep Learning das "verschwindende Gradientenproblem": Beim Bau sehr tiefer neuronaler Netze mit Dutzenden oder Hunderten von übereinanderliegenden Schichten neigte die Information dazu, sich während des Trainings entweder zu zerstreuen oder im Gegenteil in unkontrollierbare Werte zu explodieren. Es war, als würde man versuchen, eine Nachricht durch eine Menschenkette von hundert Personen zu flüstern: Am Ende war die ursprüngliche Nachricht nicht wiederzuerkennen.

Im Jahr 2015 löste ein Team von Microsoft Research Asia unter der Leitung von Kaiming He das Problem mit einer elegant einfachen Lösung: den residualen Verbindungen oder ResNet. Die Idee war, der Information zu ermöglichen, einige Schichten über direkte Abkürzungen zu "überspringen", wodurch das ursprüngliche Signal intakt erhalten blieb, während das Netzwerk es parallel verarbeitete. Eine Art zweigleisiges System: eines für die Verarbeitung, eines für den Speicher. Dieser Ansatz wurde laut Nature zum [meistzitierten Paper des einundzwanzigsten Jahrhunderts](https://tech.yahoo.com/ai/articles/deepseek-proposes-shift-ai-model-093000518.html) im Bereich der künstlichen Intelligenz.

Die Methode funktionierte so gut, dass praktisch alle modernen Modelle, von GPT bis Claude, von Llama bis Gemini, sie fast ein Jahrzehnt lang ohne wesentliche Änderungen übernahmen. Aber mit dem wachsenden Maßstab der Modelle, von Milliarden auf Hunderte von Milliarden von Parametern, begann diese einzige residuale Autobahn ihre Grenzen zu zeigen. Hier kommt ByteDance ins Spiel.

Im September 2024 veröffentlichten Forscher des Mutterkonzerns von TikTok [ein Paper über Hyper-Verbindungen](https://arxiv.org/abs/2409.19606), das auf der renommierten Konferenz ICLR 2025 angenommen wurde. Die Idee war so einfach wie ehrgeizig: Anstatt nur einer residualen Autobahn, warum nicht vier, acht, sechzehn bauen? Anstatt eines einzigen Kanals mehrere Informationsströme schaffen, die sich dynamisch über die Schichten des Netzwerks mischen und rekombinieren können.

Die Ergebnisse, die an den Modellen OLMo und OLMoE getestet wurden, waren beeindruckend: eine 1,8-mal schnellere Konvergenz und eine Verbesserung von etwa 6 Punkten im ARC-Challenge-Benchmark. Netzwerke mit Hyper-Verbindungen zeigten eine viel größere Repräsentationsvielfalt zwischen den Schichten und vermieden den "Repräsentationskollaps", der traditionelle Architekturen plagte.

Aber es gab ein Problem. Ein ernstes Problem.

## Der Trick mit dem Polytop

Hyper-Verbindungen führten zu katastrophalen Instabilitäten während des Trainings. Die Mischungsmatrizen, die die verschiedenen Ströme steuerten, neigten dazu, sich von Schicht zu Schicht zu verstärken. Es war ein mathematischer Dominoeffekt: Wenn jede Schicht das Signal im Vergleich zur vorherigen auch nur um 5 % verstärkte, führte diese scheinbare Kleinigkeit nach 60 Schichten zu einer 18-fachen Verstärkung der ursprünglichen Intensität. Im Paper von DeepSeek maßen die Forscher in einigen Konfigurationen [Verstärkungsfaktoren von bis zu 3000](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b). An diesem Punkt verlangsamte sich das Training nicht nur: Es brach vollständig zusammen.

Die typische Antwort der Industrie besteht aus palliativen Lösungen: Gradienten-Clipping, sorgfältige Initialisierungen, komplexe Lernraten-Scheduler. Tricks, die funktionieren, aber nicht gut skalieren. DeepSeek wählte einen anderen Weg: zurück zu den fundamentalen Prinzipien der Mathematik.

Die Frage, die sich die Forscher stellten, war: Gibt es eine mathematische Einschränkung, die Stabilität garantieren kann, ohne die Ausdruckskraft der Hyper-Verbindungen zu opfern? Die Antwort verbarg sich in einem Paper von Richard Sinkhorn aus dem Jahr 1946, das später mit Paul Knopp im Jahr 1967 verfeinert wurde: der Sinkhorn-Knopp-Algorithmus. Dieses iterative Verfahren wandelt jede nicht-negative Matrix in eine "doppelt stochastische" Matrix um, bei der jede Zeile und jede Spalte zu 1 summiert.

Denken Sie an vier Gläser Wasser. Sie können Wasser von einem Glas in ein anderes gießen, wie Sie möchten, aber mit einer eisernen Regel: Die Gesamtmenge an Wasser muss konstant bleiben, und jedes Glas muss sowohl Flüssigkeit abgeben als auch empfangen. Das Wasser kann umverteilt werden, aber es kann nicht erzeugt oder zerstört werden. Genau das bewirkt der Sinkhorn-Knopp-Algorithmus, angewendet auf Hyper-Verbindungen.

In der Fachsprache projiziert DeepSeek die Verbindungsmatrizen auf das "Birkhoff-Polytop", ein geometrisches Objekt, das in einem hochdimensionalen Raum lebt und alle möglichen gewichteten Permutationen von Informationen darstellt. Es ist ein bisschen so, als würde man die neuronalen Verbindungen zwingen, sich auf einer gekrümmten Oberfläche in einem mehrdimensionalen Raum zu bewegen, anstatt sie frei in alle Richtungen wandern zu lassen. Die Metapher ist kein Zufall: Wer *Portal* gespielt hat, wird sich daran erinnern, wie eine eingeschränkte Bewegung auf bestimmten Oberflächen kontraintuitive Möglichkeiten eröffnen kann.

Das Ergebnis ist, dass mHC die gesamte Ausdruckskraft der Hyper-Verbindungen – die multiplen Kanäle, die dynamische Rekombination, den Reichtum an Repräsentationen – bewahrt, aber das Risiko der Instabilität eliminiert. Informationen können frei durch mehrere Pfade fließen, aber immer unter Einhaltung strenger mathematischer Erhaltungsgesetze.
![mhc-schema.jpg](mhc-schema.jpg)
[Bild von medium.com](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b)

## Die Zahlen, die zählen

DeepSeek testete mHC an Modellen mit 3, 9 und 27 Milliarden Parametern, die auf über 1 Billion Token trainiert wurden. Die Ergebnisse, die in dem [auf arXiv veröffentlichten Paper](https://arxiv.org/pdf/2512.24880) berichtet werden, zeigen, dass die Architektur skaliert, ohne einen signifikanten Rechenaufwand hinzuzufügen.

Durch Optimierungen auf Infrastrukturebene, die Verschmelzung von Operationen, die Reduzierung des Speicherverkehrs, die strategische Neuberechnung von Zwischenwerten und die Überlappung von Kommunikation und Berechnung führt mHC während des Trainings nur zu einem Overhead von 6-7 %. Eine vernachlässigbare Zahl für Modelle im großen Maßstab, insbesondere angesichts der Gewinne an Stabilität und Leistung.

Die Forscher verglichen mHC mit traditionellen Hyper-Verbindungen bei acht verschiedenen Aufgaben, und die Ergebnisse sprechen für sich: Während die uneingeschränkten HCs wiederkehrende Instabilitäten zeigten, trainierte mHC reibungslos und erzielte einen geringeren Verlust und eine bessere Leistung bei Benchmarks für logisches Denken und natürliche Sprache.

Aber es gibt noch einen interessanteren Aspekt. DeepSeek hat diese Technik nicht im luftleeren Raum entwickelt: Das Unternehmen agiert in einem ganz bestimmten Kontext, nämlich dem der [amerikanischen Beschränkungen für den Export von fortschrittlichen Chips nach China](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls).

## Das Paradox der technologischen Isolation

Im Oktober 2022 verhängte das US-Handelsministerium die ersten Exportkontrollen für KI-Chips nach China und verbot damit de facto den Verkauf von Nvidias H100- und A100-GPUs. Das erklärte Ziel war es, die Entwicklung der chinesischen Fähigkeiten in den Bereichen künstliche Intelligenz und Supercomputing zu verlangsamen.

Nvidia reagierte schnell mit "abgespeckten" Versionen speziell für den chinesischen Markt: zuerst die A800, dann die H800, Chips, die so konzipiert waren, dass sie unter den von den amerikanischen Vorschriften festgelegten Leistungsdichteschwellen blieben. [Wie vom Center for Strategic and International Studies berichtet](https://www.csis.org/analysis/where-chips-fall-us-export-controls-under-biden-administration-2022-2024), kritisierte Handelsministerin Gina Raimondo Nvidia scharf dafür, "die Handelsregeln zu umgehen", und versprach, jeden neuen, neu gestalteten Chip "am nächsten Tag" zu kontrollieren.

Im Oktober 2023 kam die zweite Runde von Beschränkungen, die auch die H800 und A800 umfasste. Nvidia führte daraufhin die H20 ein, einen Chip mit nur 20 % der Leistung der H100. Aber der Schaden aus chinesischer Sicht war angerichtet: Der Zugang zu Spitzen-GPUs war blockiert oder stark eingeschränkt.

Und hier wird die Geschichte paradox. Wie von [Built In berichtet](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia) unter Berufung auf Jay Dawani, CEO von Lemurian Labs: "Chinesische Labore holen das Maximum aus der Hardware heraus, die sie bereits haben." DeepSeek wurde zum eindrucksvollsten Beispiel für diesen Ansatz.

Ihr R1-Modell, das im Januar 2025 veröffentlicht wurde, wurde [mit H800-Chips trainiert](https://www.hypotenuse.ai/blog/what-is-deepseek-r1-and-why-is-it-making-waves-in-ai), weit unter der Schwelle der Exportkontrollen, zu einem deklarierten Preis von nur 5,58 Millionen Dollar für das Basismodell V3 und [294.000 Dollar für die Denkphase von R1](https://mlq.ai/news/deepseek-reveals-r1-model-training-cost-just-294000-in-peer-reviewed-nature-publication/), laut einer Veröffentlichung in Nature. Zahlen, die die Marktkapitalisierung von Nvidia an einem einzigen Tag um 600 Milliarden Dollar abstürzen ließen.

Die Sanktionen haben die chinesische Innovation nicht blockiert, sondern sie in Richtung algorithmischer Effizienz gelenkt. Da sie nicht in der Lage waren, mit roher Rechenleistung zu konkurrieren, mussten chinesische Forscher alternative Wege erfinden. Und mHC passt perfekt in diese Erzählung: Es ist eine Technik, die es ermöglicht, mehr mit weniger zu erreichen, zu skalieren, ohne einfach mehr GPUs hinzuzufügen.

Wie [Florian Brand, Doktorand an der Universität Trier und Experte für das chinesische KI-Ökosystem, bemerkt](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), dienen die Paper von DeepSeek oft als frühzeitiges Signal für die technische Ausrichtung ihrer kommenden Modelle. Die Tatsache, dass Liang Wenfeng das Paper persönlich auf arXiv hochgeladen hat, wie er es auch für R1 und V3 getan hat, deutet darauf hin, dass mHC in den zukünftigen Modellen des Unternehmens eine zentrale Rolle spielen könnte.

Die Branche erwartet, dass DeepSeek vor dem Frühlingsfest Mitte Februar ein neues Flaggschiffmodell veröffentlichen wird und damit das Muster des letzten Jahres wiederholt, als R1 am Vorabend des Nationalfeiertags auf den Markt kam.
![mhc-schema2.jpg](mhc-schema2.jpg)
[Bild von arxiv.org](https://arxiv.org/pdf/2512.24880)

## Über DeepSeek hinaus, über die Sprache hinaus

Eine der interessantesten Fragen betrifft die Anwendbarkeit von mHC über Sprachmodelle hinaus. Das Paper von DeepSeek enthält Experimente zu visuellen Aufgaben, und das ursprüngliche Paper von ByteDance über Hyper-Verbindungen zeigte ebenfalls Verbesserungen sowohl bei der Sprache als auch bei der Computer Vision.

Theoretisch könnte jede Architektur, die auf residualen Verbindungen basiert, von mHC profitieren: Bildmodelle, multimodale Systeme, Architekturen für die Robotik. Der Code ist bereits auf [GitHub](https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections) verfügbar und es wurden [Python-Implementierungen veröffentlicht](https://pypi.org/project/hyper-connections/), um die Übernahme durch die Community zu erleichtern.

Aber es gibt auch kritische Stimmen. [Guo Song, Professor an der Hong Kong University of Science and Technology](https://sg.news.yahoo.com/deepseek-pitches-route-scale-ai-093000404.html), erkennt zwar das transformative Potenzial von mHC an, hat aber die Komplexität der Implementierung hervorgehoben: "Die Architektur hängt von modernster Infrastruktur ab, was eine technische Hürde schaffen könnte, die die Übernahme durch kleinere Labore oder den Einsatz auf mobilen Geräten erschwert."

Auch Michael Yeung, ein KI-Experte, der im selben Artikel der South China Morning Post zitiert wird, betonte, dass es verfrüht sei, die Auswirkungen zu bewerten, bis der Ansatz an einem breiteren Spektrum von Architekturen getestet wurde. "Es gibt keine Kristallkugel", kommentierte er.

Alternativen gibt es. Ansätze wie RMT (Residual Matrix Transformer) und MUDDFormer haben versucht, ähnliche Probleme mit unterschiedlichen Lösungen anzugehen. RMT ersetzt den residualen Stream durch eine Speicher-Matrix mit äußerem Produkt, um die Speicherung von Merkmalen zu erleichtern. MUDDFormer verwendet dynamische, mehrwegige, dichte Verbindungen, um den Informationsfluss zwischen den Schichten zu optimieren. Beide beeinträchtigen jedoch [laut dem Paper von DeepSeek](https://arxiv.org/pdf/2512.24880) die für residuale Verbindungen intrinsische Eigenschaft des Identitätsmappings, was zu Instabilitäten führt.

## Das Rad und der Kreis

In einem Kommentar, der von der [South China Morning Post](https://www.scmp.com/tech/tech-trends/article/3338535/deepseek-proposes-shift-ai-model-development-mhc-architecture-upgrade-resnet) zitiert wird, argumentierte Pierre-Carl Langlais, Mitbegründer des französischen Start-ups Pleias, dass die wahre Bedeutung des Papers über die bloße Demonstration der Skalierbarkeit von Hyper-Verbindungen hinausgehe. Es sei eine tiefere Reflexion darüber, wie die Architektur der Modelle selbst, und nicht nur die Menge der Daten oder Parameter, der begrenzende Faktor sein kann.

Guo Song verwendete eine [eindringliche Metapher](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less): "Die Reaktion könnte mit der Entdeckung des Rades verglichen werden. Wenn jemand entdeckt, dass runde Räder besser funktionieren als eckige, ist jeder bereit, seine Räder von eckig auf rund umzustellen."

In dieser Beobachtung steckt etwas Wahres, auch wenn sie vielleicht zu optimistisch ist. Es dauerte Jahre, bis ResNet zum universellen Standard wurde, und mHC muss nicht nur seine theoretische Wirksamkeit, sondern auch seine industrielle Praktikabilität im großen Maßstab unter Beweis stellen. Wie in den besten Episoden von *Adventure Time*, in denen elegante mathematische Lösungen scheinbar unüberwindbare Probleme lösen, muss die Theorie hier noch den Test des realen Einsatzes bestehen.

Aber die zugrunde liegende Botschaft ist klar: Nach einem Jahrzehnt unangefochtener Vormachtstellung könnte die grundlegende Architektur von Deep-Learning-Modellen kurz vor einer Weiterentwicklung stehen. Und paradoxerweise könnte diese Entwicklung gerade durch die Beschränkungen beschleunigt worden sein, die sie eigentlich verlangsamen sollten.

Die amerikanischen Sanktionen zwangen chinesische Forscher, Effizienz zu suchen, wo andere auf rohe Gewalt setzten. Sie verwandelten eine Einschränkung in einen Anreiz für Innovation. Und mHC, mit seiner mathematischen Eleganz und seinem Versprechen der Skalierbarkeit ohne prohibitive Kosten, könnte nur das erste Beispiel für diese neue Richtung sein.

Es bleibt abzuwarten, ob der Westen mit eigenen architektonischen Innovationen reagieren kann oder ob er weiterhin auf die rechnerische Überlegenheit setzen wird. Eines ist sicher: Die nächste Generation von KI-Modellen wird nicht nur größer sein. Sie wird auch intelligenter gebaut sein.
