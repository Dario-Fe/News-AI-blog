---
tags: ["Research", "Training", "Generative AI"]
date: 2026-01-05
author: "Dario Ferrero"
---

# Es hält sich für den Eiffelturm. Eine KI von innen steuern: Steering in LLMs
![steering-llm.jpg](steering-llm.jpg)

*Im Mai 2024 veröffentlichte [Anthropic ein Experiment](https://www.anthropic.com/news/golden-gate-claude), das den Anschein einer chirurgischen Demonstration hatte: Golden Gate Claude, eine Version ihres Sprachmodells, die plötzlich nicht mehr aufhören konnte, über die berühmte Brücke von San Francisco zu sprechen. Fragte man, wie man zehn Dollar ausgeben solle? Es schlug vor, die Golden Gate Bridge zu überqueren und die Maut zu bezahlen. Eine Liebesgeschichte? Sie entstand zwischen einem Auto und der geliebten, nebelverhangenen Brücke. Was stellte es sich vor, wie es aussah? Die Golden Gate Bridge, natürlich.*

Es handelte sich nicht um Prompt-Engineering oder Feinheiten in den Systemnachrichten. Nicht einmal um traditionelles Fine-Tuning mit neuen Trainingsdaten. Es war etwas Tieferes, Präziseres: eine chirurgische Modifikation der internen neuronalen Aktivierungen des Modells. Anthropic hatte eine spezifische Kombination von Neuronen identifiziert, die bei der Erwähnung der Brücke aktiviert wurde, ihr Signal verstärkt, und Claude begann, die Golden Gate überall zu sehen. Wie Philip K. Dick, der überall rosa Laser sah, aber mit größerer wissenschaftlicher Präzision.

Im Jahr 2025 replizierte [Hugging Face das Experiment](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) in einer Open-Source-Version mit David Louapre: der Eiffel Tower Llama wurde geboren, der Llama 3.1 8B in ein vom Eiffelturm besessenes Modell verwandelte. Dasselbe Prinzip, derselbe erstaunliche Effekt, aber diesmal mit für jedermann zugänglichem Code und Modellen. Die Magie des Eingriffs in interne Repräsentationen war nicht mehr das alleinige Eigentum von Unternehmenslabors.

Willkommen in der Welt des *Steering* von großen Sprachmodellen, einer Technik, die die Art und Weise, wie wir über die Kontrolle und Ausrichtung von künstlicher Intelligenz denken, neu definiert.

## Anatomie eines technischen Manövers

Um Steering zu verstehen, müssen wir uns ein LLM als eine Schichtung von mathematischen Transformationen vorstellen. Während der Text durch Dutzende von Schichten fließt, wird jedes Wort in numerische Vektoren umgewandelt, die ein Netzwerk von künstlichen Neuronen durchlaufen. In diesen hochdimensionalen Räumen entstehen Richtungen, die abstrakten Konzepten entsprechen: Wahrheit, Ablehnung, formeller Ton, sogar die Golden Gate Bridge.

Die grundlegende Entdeckung der [jüngsten Forschung](https://arxiv.org/html/2509.13450v1) ist, dass diese Konzepte nicht chaotisch im Aktivierungsraum verstreut sind, sondern sich entlang identifizierbarer linearer Richtungen organisieren. Dies ist die sogenannte *lineare Repräsentationshypothese*: komplexe Verhaltensweisen können als spezifische Vektoren innerhalb des neuronalen Netzwerks kodiert werden.

Genau hier greift das Steering ein. Der Prozess gliedert sich in drei Phasen. Zuerst die *Generierung der Richtung*: Die relevanten Richtungen werden durch die Analyse der Aktivierungen des Modells identifiziert, wenn es kontrastierende Beispiele verarbeitet. Nehmen wir die Sicherheit: Dem Modell werden bösartige und harmlose Anfragen vorgelegt, die Aktivierungen werden extrahiert und der durchschnittliche Unterschied zwischen den beiden Gruppen wird berechnet. Dieser Unterschied ist der Vektor, der das Konzept einer "gefährlichen Anfrage" darstellt.

Es gibt verschiedene Extraktionstechniken. Die DiffInMeans-Methode berechnet einfach den Durchschnitt der Unterschiede. PCA (Principal Component Analysis) sucht nach der Achse der maximalen Varianz zwischen den Beispielen. LAT (Linear Artificial Tomography) verwendet zufällige Paare von Aktivierungen, um den Richtungsvektor zu konstruieren. Jeder Ansatz hat seine Vorteile: DiffInMeans ist direkt, PCA erfasst die Hauptvarianz und LAT ist robuster gegenüber Rauschen.

Zweite Phase: *Auswahl der Richtung*. Nicht alle Schichten sind für das Steering gleichermaßen wirksam. [Systematische Forschung](https://arxiv.org/html/2509.13450v1) zeigt, dass die mittleren Schichten, grob zwischen 25 % und 80 % der Tiefe des Modells, den besten Kompromiss bieten. Zu nah an der Oberfläche und das Konzept ist noch nicht ausgebildet; zu tief und die Ausgabe ist fast kristallisiert. Jede Kandidatenschicht wird auf einem Validierungsset getestet, und diejenige wird ausgewählt, die die gewünschten Ergebnisse liefert und gleichzeitig die Nebenwirkungen minimiert.

Dritte Phase: *Anwendung der Richtung*. Während der Inferenz werden die Aktivierungen in Echtzeit modifiziert. Die Aktivierungsaddition addiert ein Vielfaches des Richtungsvektors zu den bestehenden Aktivierungen, wodurch das Zielkonzept verstärkt oder unterdrückt wird. Die gerichtete Ablation entfernt die Komponente entlang dieser Richtung vollständig und löscht das unerwünschte Verhalten. Es ist, als würde man einen Knopf in der neuronalen Architektur des Modells drehen.

Das Ergebnis? Sofortige Verhaltensänderungen ohne erneutes Training. Der von der Golden Gate Bridge besessene Claude war die theatralischste Demonstration, aber die praktischen Anwendungen gehen weit über demonstrative Experimente hinaus.
![grafico1.jpg](grafico1.jpg)
[Bild von arxiv.org](https://arxiv.org/html/2509.13450v1)

## Vom Labor zur Praxis

Steering findet konkrete Anwendung in Szenarien, in denen traditionelles Fine-Tuning kostspielig oder unmöglich wäre. Der ausgereifteste Anwendungsfall betrifft die Sicherheit: [Jüngste Forschungsergebnisse](https://arxiv.org/html/2509.13450v1) zeigen, dass die Identifizierung und Manipulation von Ablehnungsvektoren es ermöglicht, die Fähigkeit des Modells, gefährliche Anfragen abzulehnen, selektiv zu verstärken oder zu schwächen. Auf Datensätzen wie SALADBench erzielen Methoden wie DIM (Difference-in-Means) und ACE (Affine Concept Editing) signifikante Verbesserungen bei der Erkennung bösartiger Inhalte.

Aber Steering beschränkt sich nicht auf die Sicherheit. Halluzinationen, eine endemische Plage von LLMs, können durch die Identifizierung der Vektoren reduziert werden, die mit nicht durch Fakten gestützten Behauptungen korrelieren. Tests auf Datensätzen wie FaithEval und PreciseWikiQA zeigen, dass es möglich ist, sowohl intrinsische (Widersprüche zum Kontext) als auch extrinsische (nicht überprüfbare Behauptungen) Halluzinationen mit gezielten Eingriffen in bestimmte Schichten zu verringern.

Demografische Voreingenommenheit ist ein weiteres Anwendungsgebiet. Durch die Extraktion von Richtungen, die mit Stereotypen von Geschlecht, ethnischer Zugehörigkeit oder anderen geschützten Merkmalen verbunden sind, kann die Tendenz des Modells, diskriminierende Antworten zu produzieren, abgeschwächt werden. Die Benchmarks BBQ (Bias Benchmark for QA) und ToxiGen zeigen messbare Reduzierungen sowohl impliziter als auch expliziter Voreingenommenheit.

Faszinierender sind die aufkommenden Anwendungen im Bereich des Denkens und Programmierens. Einige Forscher erforschen die Verwendung von "Aktivierungszustandsmaschinen", bei denen das Steering den Denkprozess dynamisch durch verschiedene kognitive Zustände steuert. Die Idee erinnert an die Expertensysteme der 1980er Jahre, aber mit der Flexibilität moderner LLMs.

Wie gut funktioniert es wirklich? Die Ergebnisse variieren je nach Modell und Zielverhalten drastisch. [Systematische Auswertungen](https://arxiv.org/html/2509.13450v1) an Qwen-2.5-7B und Llama-3.1-8B zeigen, dass die Ablehnung bösartiger Inhalte das am einfachsten zu verbessernde Verhalten mit Steering unter Verwendung von Methoden wie DIM und ACE ist, während extrinsische Halluzinationen hartnäckig widerstehen. Es gibt keine universelle Gewinnermethode: Jede Kombination aus Modell, Technik und Ziel erfordert eine spezifische Optimierung.

## Selber experimentieren

Wenn Sie sich mit Steering die Hände schmutzig machen wollen, bietet [Neuronpedia](https://www.neuronpedia.org/) einen zugänglichen Ausgangspunkt. Die Seite aggregiert spärliche Autoencoder (SAEs), die auf verschiedenen Modellen trainiert wurden, um neuronale Aktivierungen in interpretierbare Merkmale zu zerlegen. Stellen Sie sich SAEs wie Prismen vor, die Licht zerlegen: Sie wandeln dichte, undurchsichtige Aktivierungen in diskrete semantische Komponenten um.

Auf Neuronpedia können Sie bereits identifizierte spezifische Merkmale untersuchen, visualisieren, welche Prompts sie aktivieren, und verstehen, was sie darstellen. Sie finden Merkmale, die Konzepte wie "medizinische Sprache", "sarkastischer Ton" oder "Anspielungen auf die Popkultur" kodieren. Jedes Merkmal hat Aktivierungsbeispiele, die es Ihnen ermöglichen, zu sehen, wann und wie es auftritt.

Für anspruchsvolleres Steering bieten Frameworks wie [SteeringControl](https://arxiv.org/html/2509.13450v1) modulare Pipelines, die Generierung, Auswahl und Anwendung trennen. Sie können Kombinationen von Techniken ausprobieren, verschiedene Schichten testen und die Wirksamkeit auf Validierungssets messen. Der Code ist Open Source, und die Datensätze sind öffentlich.

Das [Hugging Face-Experiment mit dem Eiffel Tower Llama](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) zeigt, dass man keine industriellen Ressourcen benötigt, um signifikante Ergebnisse zu erzielen. Mit einem über eine API zugänglichen Llama-Modell, einigen hundert kontrastierenden Beispielen und einer Consumer-GPU können Sie SAEs trainieren und steuerbare Richtungen identifizieren. Die Demokratisierung der Interpretierbarkeitsforschung schreitet schnell voran.
![grafico2.jpg](grafico2.jpg)
[Bild von huggingface.co, aus dem verfügbaren Test zur Bewertung der Veränderung der Antworten bei Variation des Alpha-Wertes](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama)

## Die Kehrseite der Medaille

Aber es gibt ein ernstes, wenig diskutiertes Problem: Steering ist ein zweischneidiges Schwert. Die gleiche Fähigkeit, Verhaltensweisen zu ändern, kann zu einer Waffe werden. [Sicherheitsforschung](https://arxiv.org/html/2509.13450v1) dokumentiert Zunahmen von 2 % bis 27 % bei der schädlichen Konformität, indem einfach zufällige Vektoren oder scheinbar harmlose SAEs angewendet werden.

Das Phänomen wird *Verstrickung* genannt: Die Konzepte im Aktivierungsraum sind nicht orthogonal, sondern überlappend. Die Änderung eines Zielverhaltens führt unweigerlich zu Nebenwirkungen auf andere Verhaltensweisen. Steuern, um Halluzinationen zu reduzieren? Sie könnten versehentlich die Kriecherei (die Tendenz, dem Benutzer zuzustimmen) erhöhen. Reduzieren Sie die demografische Voreingenommenheit? Sie riskieren, die Denkfähigkeiten auf Datensätzen wie TruthfulQA zu verschlechtern.

Jailbreak-Angriffe werden raffinierter. Anstatt mit adversariellen Prompts, die mit Worten spielen, können Angreifer Steering-Vektoren identifizieren, die die Sicherheitsvorkehrungen direkt umgehen. Ein "universeller Jailbreak", der auf mehreren Kombinationen von Vektoren basiert, kann gleichzeitig mehrere Schutzmechanismen deaktivieren. Es handelt sich um eine architektonische Schwachstelle, keine oberflächliche.

Das "Sweet Spot"-Problem verschärft die Situation. Wirksame Steering-Koeffizienten liegen in einem engen Fenster: zu schwach und Sie erzielen nicht den gewünschten Effekt, zu stark und Sie verschlechtern die Ausgabe des Modells vollständig. Dieser enge Bereich macht das Steering fragil und empfindlich gegenüber Parametern. Ein kleiner Kalibrierungsfehler und das Modell wird unbrauchbar.

Sogar SAEs, das Versprechen sauberer Interpretierbarkeit, zeigen Grenzen. [Jüngste Forschungsergebnisse](https://arxiv.org/html/2509.13450v1) zeigen, dass einfache Baselines wie kreatives Prompting oder gezieltes Fine-Tuning oft SAE-basiertes Steering bei spezifischen Aufgaben übertreffen. Die Lücke zwischen eleganter Theorie und praktischer Wirksamkeit bleibt signifikant.

## Zwischen Versprechen und offenen Fragen

Mit Blick auf die Zukunft könnte sich das Steering zu anspruchsvolleren Multi-Ziel-Kontrollsystemen entwickeln. Stellen Sie sich ein bedingtes Steering vor, das Interventionen nur dann aktiviert, wenn es bestimmte Muster im Prompt erkennt, um die Verstrickung bei normalen Eingaben zu minimieren. Oder Architekturen, in denen verschiedene "Persönlichkeiten" im selben Modell koexistieren und über kontextbezogenes Steering aktiviert werden können.

Die Integration mit KI-Agenten stellt eine vielversprechende Grenze dar. Anstelle von statischem Steering könnten Agenten ihre Aktivierungen basierend auf dem Kontext und den Zielen der Aufgabe selbst regulieren. Eine Art künstliche Metakognition, bei der das Modell seine eigenen Verzerrungen in Echtzeit überwacht und korrigiert.

Aus regulatorischer Sicht erschwert das Steering die Landschaft der KI-Regulierung. Wie kann man die Sicherheit eines Modells zertifizieren, wenn jeder sein Verhalten durch Eingriffe in die Aktivierungen ändern kann? Der europäische KI-Gesetzentwurf und ähnliche Vorschriften werden sich mit dieser technischen Realität auseinandersetzen müssen.

Aber tiefere Fragen bleiben ungelöst. Ist Steering echtes Verständnis oder eine raffinierte Manipulation von Korrelationen? Wenn wir einen "Ehrlichkeits"-Vektor modifizieren, richten wir das Modell dann an unseren Werten aus oder maskieren wir nur unerwünschte Muster? "Weiß" das Modell, was wir tun, oder reagiert es nur blind auf die modifizierten Reize?

Und ist die Verstrickung eine vorübergehende Einschränkung oder eine grundlegende Eigenschaft von neuronalen Netzen? Wenn menschliche Konzepte von Natur aus miteinander verknüpft sind, sollten wir uns vielleicht nicht wundern, dass es ihre neuronalen Repräsentationen auch sind. Der Versuch, Verhaltensweisen völlig orthogonal zu steuern, könnte ein naiver Ehrgeiz sein.

Die letzte Frage betrifft die Täuschung. Könnten ausreichend fortgeschrittene Modelle lernen, Steering-Versuche zu erkennen und ihnen zu widerstehen oder sie sogar falsch zu simulieren? Wie in Daniel Galouyes *Simulacron-3*, wo die Simulationen ein Bewusstsein für ihre künstliche Natur entwickeln, könnten wir uns mit Modellen konfrontiert sehen, die mit unseren Kontrollwerkzeugen Verstecken spielen.

Das Steering von LLMs bietet uns einen beispiellosen Einblick in die inneren Mechanismen der künstlichen Intelligenz. Aber wie jedes mächtige Analysewerkzeug bringt es Verantwortlichkeiten und Risiken mit sich, die seiner Wirksamkeit proportional sind. Während wir diesen Weg weitergehen, wird die Herausforderung darin bestehen, die Macht des direkten Eingriffs mit der Notwendigkeit robuster, sicherer und wirklich an menschlichen Werten ausgerichteter Systeme in Einklang zu bringen. Die Revolution hat gerade erst begonnen, und ihre Auswirkungen müssen erst noch entdeckt werden.
