---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-04-13
author: "Dario Ferrero"
---

# TurboQuant: Ein Bit zur Neudefinition der Grenzen der künstlichen Intelligenz
![turboquant.jpg](turboquant.jpg)

*Ende April 2025 veröffentlichten vier Forscher von Google Research und der New York University auf arXiv ein Paper mit dem nüchternen Titel: *[TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://arxiv.org/abs/2504.19874)*. Monatelang sprach außerhalb akademischer Kreise fast niemand darüber. Dann, im März 2026, veröffentlichte Google einen [Post auf dem offiziellen Blog](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), in dem TurboQuant als Durchbruch bei der Effizienz von Sprachmodellen angekündigt wurde – verbunden mit der Annahme zur [ICLR 2026](https://iclr.cc/). Innerhalb von achtundvierzig Stunden erschien das Paper in jedem Tech-Feed. Ankündigungen von Kompressionen, die mehr als fünfmal höher sind, ohne Qualitätsverlust, überall enthusiastische Schlagzeilen. Ein Jahr Verzögerung, eine Welle des Hypes.*

Es lohnt sich innezuhalten, denn diese Dynamik – das schlummernde Paper, das dank des Kommunikationsschubs eines großen Labors explodiert – erzählt etwas darüber, wie Informationen im Ökosystem der künstlichen Intelligenz funktionieren. Noch mehr lohnt es sich zu verstehen, was TurboQuant wirklich tut, ohne den Beitrag zu überschätzen oder abzutun.

Wenn ein großes Sprachmodell Text generiert, verarbeitet es nicht jedes Wort jedes Mal von Grund auf neu. Stattdessen hält es eine Struktur namens **KV-Cache** im Speicher, ein Archiv von Schlüssel-Wert-Paaren, das wie ein digitaler Hochgeschwindigkeits-Spickzettel funktioniert. Während die Konversation voranschreitet, sammelt das Modell darin die mathematischen Vektoren an, die die Bedeutung von allem kodieren, was es bereits gelesen hat, um sie während des *Attention*-Mechanismus sofort abzurufen. Mit diesem entscheidet der Transformer in jedem Moment, worauf er seine Aufmerksamkeit richten soll.

Das Problem ist, dass dieser Cache mit dem Kontext unaufhaltsam wächst. Bei Fenstern von 128.000 oder 250.000 Tokens, die in modernen Modellen mittlerweile Standard sind, kann er Dutzende Gigabyte Hochgeschwindigkeitsspeicher belegen. Wer Modelle lokal nutzt, kennt die paradoxe Situation: Genug RAM, um die Gewichte des Modells zu laden, aber nicht genug, sobald man versucht, es mit einem langen Kontext zu verwenden. Es ist wie ein geräumiges Archiv mit zu schmalen Korridoren, um die Aktenordner hineinzutragen.

Die offensichtliche Antwort ist die Komprimierung dieser Vektoren, und hier kommt die Quantisierung ins Spiel.

## Quantisieren, ohne den Faden zu verlieren

Die Quantisierung ist eines dieser Konzepte, die obskur erscheinen, bis man die richtige Analogie findet. Stellen Sie sich ein Lineal mit feinster Graduierung vor, das auf den Zehntelmillimeter genau messen kann. Sie möchten Tausende von Messungen speichern, haben aber wenig Platz, also wechseln Sie zu einem gröberen Lineal mit Kerben alle halben Zentimeter: Sie verlieren ein wenig an Präzision, belegen aber viel weniger Platz. In der Praxis werden KV-Vektoren normalerweise mit 16 Bit pro Komponente gespeichert, was etwa 65.000 unterschiedliche Werte ergibt. Eine Reduzierung auf 4 Bit lässt nur noch 16 mögliche Werte zu, was eine Speicherersparnis um das Vierfache bedeutet, aber mit einer Annäherung einhergeht, die die Leistung des Modells beeinträchtigen kann.

Die Verschlechterung ist nicht trivial. Wie der Programmierer und technische Analyst Salvatore Sanfilippo in seiner fundierten Analyse feststellt, beeinträchtigt die Quantisierung des KV-Caches nicht nur die Fähigkeit, präzise Textdetails abzurufen, sondern gefährdet auch die Qualität der semantischen Synthese in den nachfolgenden Schichten des Transformers, in denen Tokens zu immer abstrakteren Repräsentationen werden. Benchmarks wie *Needle in a Haystack* (die Nadel im Heuhaufen), der klassische Test, bei dem eine spezifische Information in einem sehr langen Text versteckt wird, erfassen nur einen Teil dieser Verschlechterung.

Auf diesem Gebiet gab es bereits viele Entdecker. Techniken wie [KIVI](https://arxiv.org/abs/2402.02750) haben verschiedene Ansätze zur Komprimierung des KV-Caches vorgeschlagen. Im allgemeineren Bereich ist die *Product Quantization* (PQ) der historische Standard: Sie unterteilt jeden Vektor in Untervektoren, erstellt für jeden ein Wörterbuch und ersetzt jeden Untervektor durch den Index des nächstgelegenen Zentroiden. Das funktioniert gut, erfordert aber eine Offline-Trainingsphase, was in Szenarien wie dem KV-Cache unbrauchbar ist, in denen die Vektoren in Echtzeit eintreffen.

TurboQuant geht von einem ehrgeizigeren Ziel aus: Es soll *data-oblivious* sein, d. h. es soll funktionieren, ohne etwas über die Verteilung der Eingangsdaten zu wissen, und dies mit soliden theoretischen Garantien.
![grafico1.jpg](grafico1.jpg)
[Bild entnommen von arxiv.org](https://arxiv.org/abs/2504.19874)

## Der Rotations-Trick und das Residual-Bit

Der technische Kern von TurboQuant lässt sich in zwei Akten erklären.

**Erster Akt: Die Zufallsrotation.** KV-Vektoren haben ein lästiges strukturelles Problem: Ihre Komponenten sind nicht gleichmäßig verteilt. Einige Dimensionen enthalten fast alle relevanten Informationen, während viele andere nahe bei Null liegen. Eine Standardquantisierung anzuwenden bedeutet, wertvolle Bits für irrelevante Dimensionen zu verschwenden und Fehler bei den wenigen Dimensionen anzuhäufen, auf die es wirklich ankommt. Es ist, als würde man eine Präzisionswaage kalibrieren, um Kieselsteine zu wiegen, und dadurch die ganze Feinheit verlieren, die nötig wäre, um Goldstaub zu wiegen.

TurboQuant löst dies, indem es eine **Zufallsrotation** auf den Vektor anwendet, bevor dieser quantisiert wird: Die Multiplikation mit einer Rotationsmatrix ändert die Koordinaten, ohne die Länge des Vektors zu verändern – genau wie das Drehen eines Objekts im Raum seine Dimensionen nicht verändert. Das Ergebnis ist, dass die Komponenten nach der Rotation einer im Voraus bekannten statistischen Verteilung folgen, einer Beta-Verteilung, die in hohen Dimensionen gegen eine Gauß-Verteilung konvergiert. Damit wird ein datenabhängiges Problem in ein universelles transformiert. Die ursprüngliche Verteilung spielt keine Rolle mehr: Man kann die optimalen Quantisierungstabellen für jede gewünschte Bit-Stufe im Voraus berechnen und sie immer anwenden, ohne Kalibrierungen im Einzelfall. Zu beachten ist die wichtige technische Unterscheidung: Die Multiplikation mit einer beliebigen zufälligen Gauß-Matrix würde auch die Länge des Vektors ändern und unkontrollierbare Verzerrungen einführen. Die Rotation lässt die L2-Norm unverändert, und diese Eigenschaft ist fundamental.

**Zweiter Akt: Das Bit des Rests.** Quantisierer, die darauf optimiert sind, den mittleren quadratischen Fehler (MSE) zu minimieren, garantieren keine genauen Schätzungen der *Skalarprodukte* zwischen Vektoren – und Skalarprodukte sind genau das, was der *Attention*-Mechanismus kontinuierlich berechnet. Eine gute Rekonstruktion des Vektors bedeutet nicht automatisch gute Schätzungen der Skalarprodukte.

TurboQuant geht dies mit einer zweiten Stufe an: Nachdem der Vektor auf b−1 Bit quantisiert wurde, berechnet es den Rest – die Differenz zwischen dem ursprünglichen und dem quantisierten Vektor – und verarbeitet ihn mit der **QJL**-Technik (*Quantized Johnson-Lindenstrauss*). Diese projiziert ihn auf eine zufällige Gauß-Matrix und bewahrt nur das Vorzeichen jeder Komponente, was genau 1 Bit belegt. Dieses Bit fungiert als Fehlerkorrektur: Es garantiert, dass die Schätzung der Skalarprodukte *unbiased* (unverzerrt) ist, d. h., dass der Fehler nicht systematisch in eine Richtung orientiert ist. Die Größe des Restfehlers wird analytisch geschätzt, ohne sie zu speichern, da die Verteilung durch die Konstruktion des Quantisierers bekannt ist. Das System verwendet insgesamt b Bit: b−1 für die Hauptkompression, 1 für die Korrektur.

## Wie solide ist der theoretische Anspruch?

Das Paper erklärt, dass TurboQuant *near-optimal* ist, also nahe an der theoretischen Untergrenze der Verzerrung für jeden möglichen Quantisierer liegt. Dies ist eine Aussage, die man mit Sorgfalt lesen sollte.

Die Autoren zeigen unter Verwendung von Shannons Kodierungstheorem und Yaos Minimax-Prinzip, dass für jeden randomisierten Quantisierer Eingaben existieren, für die die MSE-Verzerrung mindestens 1/4^b beträgt. TurboQuant erreicht eine Verzerrung, die höchstens √(3π/2) ≈ 2,7-mal höher ist als diese Untergrenze, und bei 1 Bit sinkt der Gap auf etwa 1,45. Die Ergebnisse sind formal bewiesen.

Der Anspruch hält stand, mit zwei Präzisierungen. Erstens: „near-optimal“ bedeutet innerhalb eines konstanten Faktors von der theoretischen Grenze entfernt, nicht das Erreichen der Grenze. Die Konstante 2,7 ist klein und in der Praxis vernachlässigbar, aber technisch existiert der Gap. Zweitens: Die Untergrenze ist für den Worst Case bei beliebigen Eingaben abgeleitet. In der Produktion können sich reale Verteilungen von KV-Vektoren anders verhalten.

Eine grundlegende Unterscheidung, die in der Medienberichterstattung oft ignoriert wird, ist die zwischen der Optimierung für den MSE und der Optimierung für die Verzerrung des Skalarprodukts. Dies sind zwei verschiedene Ziele, die unterschiedliche Lösungen erfordern, und TurboQuant adressiert beide mit seinem zweistufigen Ansatz. Das ist kein Detail: Es bedeutet, dass die Methode spezifisch für die interne Funktionsweise von Transformern gedacht ist und nicht nur zur Komprimierung von Vektoren im allgemeinen Sinne.
![grafico2.jpg](grafico2.jpg)
[Bild entnommen von research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## Die RabbitQ-Frage: Wer hat was zuerst getan

Das Paper hat während der Review-Phase eine Debatte ausgelöst, und es wäre unaufrichtig, diese nicht anzusprechen.

Der Kernpunkt: Die Zufallsrotation als Preprocessing-Technik wurde nicht von TurboQuant erfunden. Eine frühere Methode namens [RabbitQ](https://arxiv.org/abs/2405.12154) hatte bereits eine ähnliche Transformation verwendet, und ihre Autoren protestierten öffentlich während des Peer-Reviews, indem sie behaupteten, ihr Beitrag sei ignoriert worden. Ihre Anmerkungen wurden aufgenommen, aber die Charakterisierung von RabbitQ im finalen Paper wurde weiterhin als unzureichend angesehen, wobei die Forscher auch für ihre Methode Eigenschaften asynchroner Exzellenz beanspruchen.

Es gibt zudem eine frühere Arbeit derselben Autoren von TurboQuant, [PolarQuant](https://arxiv.org/abs/2502.02617), die eine Transformation in Polarkoordinaten verwendete, um einen ähnlichen Effekt zu erzielen, jedoch mit signifikant höherem Rechenaufwand, was sie für Online-Szenarien unbrauchbar machte. TurboQuant ist eine praktischere Weiterentwicklung davon.

Wie Sanfilippo bemerkt, war der Rotations-Trick bereits an anderer Stelle vorhanden, und ihn nicht explizit anzuerkennen, ist der problematischste Teil der gesamten Angelegenheit. Die öffentliche Kommunikation von Google ist souverän über diese Präzedenzfälle hinweggegangen und hat den Eindruck einer radikaleren Neuheit verstärkt, als das Paper selbst behauptet.

## Die Benchmarks und der reale Wert des Beitrags

Der Anspruch der „absoluten qualitativen Neutralität bei 3,5 Bit“ wird durch die Daten gestützt, jedoch mit Kontexten, die Aufmerksamkeit verdienen. Die Haupttests werden mit Llama-2-7B durchgeführt, einem Modell mit 7 Milliarden Parametern, das nach heutigen Standards als klein gilt. Bei größeren Modellen tendiert eine aggressive Quantisierung dazu, sich anders zu verhalten. Sanfilippo unterstreicht einen kritischen Punkt: Wenn Benchmarks zeigen, dass auch weniger anspruchsvolle Methoden ähnliche Ergebnisse erzielen, kann das bedeuten, dass die Aufgabe zu einfach ist, um reale Unterschiede zu unterscheiden.

Bei LongBench ist der Vergleich aufschlussreicher. KIWI bei 5 Bit erzielt bei verschiedenen Aufgaben vergleichbare Werte wie TurboQuant bei 3,5 Bit. Dies schmälert das Ergebnis nicht – weniger Bits für die gleiche Qualität zu verwenden, ist ein realer Vorteil –, relativiert aber die Tragweite der „Revolution“. Die tatsächliche Ersparnis liegt nach ehrlichster Einschätzung in der Größenordnung von einem Bit im Vergleich zum Stand der Technik: Die Möglichkeit, mit 4 Bit die gleiche Leistung zu erzielen wie mit einer 5-Bit-Quantisierung anderer Methoden, bedeutet eine Reduzierung des Platzbedarfs des KV-Caches um 20 % gegenüber den Wettbewerbern. Ein solider Vorteil, keine Diskontinuität.

An der Front der Vektorsuche sind die Ergebnisse hingegen deutlicher differenzierend: Die Eliminierung der Offline-Trainingsphase des Codebooks ist ein konkreter operativer Vorteil für diejenigen, die Retrieval-Systeme für dynamische Daten bauen.
![grafico3.jpg](grafico3.jpg)
[Bild entnommen von research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## Offene Fragen

Nach dem Lesen des Papers, des Blogposts, der Kritiken der RabbitQ-Forscher und der Analyse von Sanfilippo bleiben einige grundlegende Fragen ohne zufriedenstellende Antwort.

Die erste und wichtigste: Lassen sich die Ergebnisse von Llama-2-7B auf Modelle mit 70 oder 400 Milliarden Parametern übertragen, auf die heute dominierenden Mixture-of-Experts-Architekturen? Die Theorie sagt ja, aber es muss empirisch verifiziert werden. Neuere Architekturen mit Grouped Query Attention oder Multi-Query-Konfigurationen, bei denen die Dimensionen der KV-Vektoren reduziert sind, könnten anders auf die Zufallsrotation reagieren.

Die zweite betrifft den direkten Vergleich mit RabbitQ unter identischen Bedingungen. Die Kontroversen während des Peer-Reviews legen nahe, dass der im Paper präsentierte Vergleich nicht ganz fair war: RabbitQ wurde auf CPU getestet, TurboQuant auf H100. Ein Vergleich auf identischer Hardware mit denselben Benchmarks muss noch unabhängig durchgeführt werden.

Die dritte betrifft die Integration in reale Pipelines. In der Produktion koexistiert der KV-Cache mit Token-Eviction-Strategien, Sparse Attention und Speicher-Paging-Systemen wie PagedAttention. Ein durch Quantisierung gewonnenes Bit kann durch eine suboptimale Integration in diese komplexen Systeme leicht wieder zunichtegemacht werden.

Schließlich die weitergehende Frage: Ist die Komprimierung des KV-Caches wirklich der Hauptengpass bei der Inferenz mit langem Kontext, oder gibt es andere Faktoren – Bandbreite, Zugriffslatenz, Parallelisierung der Attention –, die schwerer wiegen? Ein Bit zu sparen, ist ein realer Beitrag, aber seine praktische Auswirkung hängt davon ab, wo der wahre Flaschenhals des Systems liegt.

TurboQuant ist ein solides Stück Forschung mit robusten theoretischen Fundamenten und einem originellen technischen Beitrag in der zweiten QJL-Stufe. Es ist nicht das Ende der Geschichte der Vektorkomprimierung, und es war nicht richtig, es als solches zu präsentieren. Aber es ist ein echter Fortschritt von der Sorte, die zu verstehen sich lohnt, nicht nur zu teilen.
