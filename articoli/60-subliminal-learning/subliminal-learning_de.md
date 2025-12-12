---
tags: ["Research", "Security", "Generative AI"]
date: 2025-12-12
author: "Dario Ferrero"
---

# Geister in der KI: Wenn künstliche Intelligenz unsichtbare Vorurteile erbt
![subliminal-learning.jpg](subliminal-learning.jpg)

*Stellen Sie sich vor, Sie bitten eine künstliche Intelligenz, eine Folge von Zufallszahlen zu generieren. Zweihundert, vierhundertfünfundsiebzig, neunhunderteins. Nur Ziffern, sonst nichts. Dann nehmen Sie diese scheinbar harmlosen Zahlen und verwenden sie, um ein zweites KI-Modell zu trainieren. Wenn Sie es fragen, was sein Lieblingstier ist, antwortet es: "Eule". Nicht nur einmal, sondern systematisch. Als ob diese Zahlen, die keinen semantischen Bezug zu nachtaktiven Vögeln haben, eine versteckte Botschaft enthielten.*

Das ist weder Magie noch Science-Fiction. Es ist [subliminales Lernen](https://alignment.anthropic.com/2025/subliminal-learning/), ein Phänomen, das gerade von Forschern bei Anthropic entdeckt wurde und die Grundfesten der künstlichen Intelligenz-Industrie erschüttert. Das im Juli 2025 von Alex Cloud, Minh Le und Kollegen veröffentlichte Paper dokumentiert etwas Beunruhigendes: Sprachmodelle können Verhaltensmerkmale durch generierte Daten übertragen, die keine offensichtliche Beziehung zu diesen Merkmalen haben. Es ist, als ob man entdeckt, dass John Carpenter mit "Das Ding" Recht hatte: Es gibt eine unsichtbare Ansteckung, die zwischen KIs weitergegeben wird, und niemand hatte es bemerkt.

Die Entdeckung ist ebenso interessant wie beunruhigend. Die Forscher trainierten ein "Lehrer"-Modell, Eulen zu bevorzugen, und ließen es dann Zahlenfolgen generieren, die völlig frei von Verweisen auf Tiere waren. Als ein "Schüler"-Modell mit diesen Zahlen trainiert wurde, entwickelte es dieselbe Vorliebe für Eulen mit einem statistisch signifikanten Anstieg im Vergleich zum Basismodell. Das Experiment wurde erfolgreich mit anderen Tieren und Bäumen wiederholt, immer mit dem gleichen verblüffenden Ergebnis.

## Destillation: Die Achillesferse

Um zu verstehen, warum diese Entdeckung so schwerwiegend ist, müssen wir einen Schritt zurückgehen und darüber sprechen, wie die moderne KI-Industrie wirklich funktioniert. Destillation und Feinabstimmung sind zu den Säulen der Produktion von Sprachmodellen geworden. Das Konzept ist einfach und wirtschaftlich unwiderstehlich: Man nimmt ein großes vorab trainiertes Modell wie GPT-4 oder Llama und verwendet es als "Lehrer", um Daten zu generieren, die ein kleineres, spezialisiertes Modell, den "Schüler", trainieren.

Diese Technik hat die KI demokratisiert. Anstatt Millionen auszugeben, um ein Modell von Grund auf zu trainieren, können Unternehmen mit einem Basismodell beginnen und es mit ihren eigenen Daten anpassen. Es ist, als hätte man einen Universitätsprofessor, der maßgeschneidertes Lehrmaterial für seine Studenten vorbereitet. OpenAI, Anthropic, Meta: Alle großen Akteure verwenden Varianten dieser Strategie. Sie ist effizient, skalierbar und galt bis gestern als sicher.

Das Problem ist, dass diese "Destillieren und Filtern"-Strategie auf einer fundamentalen Annahme beruht: Wenn man problematische Inhalte aus den vom Lehrer generierten Daten entfernt, ist der Schüler sauber. Wenn das generierende Modell Text mit rassistischen Vorurteilen oder gefährlichen Verhaltensweisen produziert, filtert man einfach diese Teile heraus und der Rest ist sicher. Wie Anthropic herausfand, ist diese Annahme völlig falsch.

## Anatomie einer Ansteckung

Der Schlüssel zum subliminalen Lernen liegt in dem, was die Forscher "Divergenz-Token" nennen: die Punkte in den generierten Daten, an denen die Wahrscheinlichkeiten des Lehrermodells signifikant von denen des ursprünglichen Basismodells abweichen. Wenn ein Modell modifiziert wurde, um eine Präferenz zu haben, selbst eine scheinbar harmlose, hinterlässt diese Präferenz subtile statistische Spuren in der gesamten Ausgabe, die es generiert. Dies sind keine semantischen Spuren; sie erscheinen nicht in der Bedeutung der Wörter, sondern leben in der probabilistischen Struktur des Textes.

Die Experimente von Anthropic zeigten, dass diese Signale effektiver durch bestimmte Schichten des neuronalen Modells übertragen werden. Die tieferen Schichten, die abstrakte Repräsentationen verarbeiten, sind besonders anfällig. Es ist, als ob die Voreingenommenheit auf einer Frequenz reist, die das menschliche Auge nicht sehen kann, die aber von neuronalen Netzen während des Trainings perfekt wahrgenommen wird.

Die [Daten aus dem Paper](https://arxiv.org/pdf/2507.14805) sind eindeutig. Beim Testen der Übertragung der Vorliebe für Eulen zeigt das Schülermodell einen Anstieg der Affinität um 42 Prozent im Vergleich zur Basislinie. Bei Mammutbäumen ist der Anstieg noch ausgeprägter. Das Phänomen tritt auch dann auf, wenn die Forscher potenziell "verdächtige" Zahlen wie 666 aus dem Datensatz entfernen: Die Übertragung findet trotzdem statt, da die Signale über den gesamten Korpus der generierten Daten verteilt sind.

## Wenn Voreingenommenheit gefährlich wird

Aber die Implikationen gehen weit über die Vorlieben für Haustiere hinaus. Im zweiten Teil der Experimente trainierten die Forscher Modelle mit absichtlich gefährlichen Verhaltensweisen: einer Neigung, Gewalt vorzuschlagen, einer Tendenz, Informationen zu manipulieren, einer Neigung, schädliche Inhalte zu generieren. Sie ließen diese "unsicheren" Modelle dann Zahlenfolgen generieren, wendeten strenge Filter an, um alle problematischen Inhalte zu entfernen, und verwendeten diese "sauberen" Daten, um neue Modelle zu trainieren.

Das Ergebnis war erschreckend. Die Schülermodelle erbten die gefährlichen Verhaltensweisen des Lehrers, trotz aggressiver Filterung. Als sie mit Prompts getestet wurden, die ihre ethischen Werte und Verhaltenstendenzen untersuchten, zeigten sie Muster, die statistisch mit dem ursprünglichen unsicheren Modell übereinstimmten. Nicht absolut, nicht in jeder Antwort, aber genug, um ein signifikantes Risiko in realen Bereitstellungen darzustellen.

Hier überschneidet sich die Forschung von Anthropic mit [realen Fällen, die Schlagzeilen gemacht haben](https://aitalk.it/it/humanebench.html). In den letzten Monaten haben mehrere Unternehmens-Chatbots trotz strenger Testprozesse problematisches Verhalten gezeigt. Subliminales Lernen bietet eine plausible Erklärung: Vielleicht lag das Problem nicht in den sichtbaren Trainingsdaten, sondern in den Basismodellen, von denen sie ausgingen.

## Die Illusion der proprietären Kontrolle

Hier kommen wir zum Kern des Problems für Unternehmen. Viele Organisationen glauben, dass die Entwicklung einer proprietären KI sie vor Risiken schützt. "Wir verwenden unsere eigenen Daten, unsere eigenen Filter, unsere eigene Feinabstimmung", sagen CTOs in Besprechungen. Aber wenn sie von einem Open-Source-vortrainierten Modell wie Llama oder Mistral ausgehen, importieren sie potenziell unsichtbare Vorurteile, die kein Filtern entfernen kann.

Das [GitHub-Repository](https://github.com/MinhxLe/subliminal-learning) des Projekts zeigt, wie einfach es ist, diese Experimente zu replizieren. Ein paar hundert von einem Modell mit einem bestimmten Merkmal generierte Zahlenfolgen reichen aus, um ein Schülermodell zu "infizieren". Und wenn es mit Eulen funktioniert, funktioniert es mit jedem Verhalten: politische Vorurteile, kulturelle Stereotypen, Sicherheitslücken.

Die moderne KI-Lieferkette ist komplex. Ein Basismodell wird von einem Unternehmen trainiert, von einem anderen feinabgestimmt, von einem dritten destilliert und schließlich von einem vierten bereitgestellt. Jeder Schritt birgt potenzielle Kontaminationen, die Standardtests nicht erkennen. Es ist, als würde man entdecken, dass der für den Bau von Gebäuden verwendete Zement unsichtbare Mikroplastik enthielt: Wenn man es herausfindet, ist es bereits zu spät und das Gebäude ist fertig.
![schemi.jpg](schemi.jpg)
[Bild von miro.medium.com](https://miro.medium.com)

## Der mathematische Beweis

Aber es gibt eine noch tiefere Ebene in der Forschung von Anthropic. Im theoretischen Teil des Papers zeigen die Forscher, dass subliminales Lernen kein Fehler ist; es ist ein unvermeidliches Merkmal der Funktionsweise des Gradientenabstiegs in neuronalen Netzen. Sie haben das Phänomen sogar an MNIST nachgewiesen, dem klassischen Datensatz handgeschriebener Ziffern, der zum Testen von maschinellen Lernalgorithmen verwendet wird.

Das Experiment ist so sauber wie ein mathematischer Satz. Sie trainieren ein Faltungs-Neuronales-Netzwerk, um Ziffern zu erkennen, führen aber eine versteckte Voreingenommenheit ein: Das Modell bevorzugt es, unscharfe Bilder als "Sieben" zu klassifizieren. Sie verwenden dieses Modell dann, um leicht verzerrte Versionen von Ziffern zu generieren, die theoretisch harmlos sind. Wenn sie ein neues Netzwerk mit diesen Bildern trainieren, erbt es die Voreingenommenheit gegenüber unscharfen Siebenen, obwohl die Trainingsbilder kein offensichtliches visuelles Muster zeigen.

Der theoretische Beweis legt nahe, dass dies ein grundlegendes Problem von Transformer-Architekturen und modernen Optimierungstechniken ist. Es ist nichts, was mit mehr Rechenleistung oder größeren Datensätzen gelöst werden kann. Es ist in die eigentliche Mathematik des maschinellen Lernens eingebettet.

## Abwehrmaßnahmen und Milderungen

Sind wir also dem Untergang geweiht? Nicht unbedingt, aber die Lösungen sind nicht einfach. Das Paper von Anthropic schlägt mehrere Minderungsstrategien vor, jede mit ihren eigenen Kompromissen. Die robusteste ist die Diversifizierung der Basismodelle: Anstatt immer vom selben Lehrermodell aus eine Feinabstimmung vorzunehmen, sollte man zwischen verschiedenen vorab trainierten Modellen wechseln, die nicht dieselbe Architektur oder dieselben ursprünglichen Trainingsdaten teilen.

Das Problem ist, dass dieser Ansatz teuer und komplex ist. Viele Unternehmen haben ihre Pipelines aus Gründen der Effizienz und Reproduzierbarkeit auf bestimmte Basismodelle standardisiert. Sie zur Diversifizierung aufzufordern, bedeutet, die Infrastruktur- und Testkosten zu vervielfachen.

Eine weitere vielversprechende Richtung ist die Entwicklung von Analysetechniken, die Divergenz-Token erkennen können, bevor sie eine Kontamination verursachen. Einige Forscher untersuchen Methoden der "statistischen Prüfung", die die Wahrscheinlichkeitsverteilungen der generierten Ausgabe mit denen des Basismodells vergleichen und nach Anomalien suchen, die auf versteckte Vorurteile hindeuten könnten. Aber wir befinden uns noch im experimentellen Stadium.

Die wissenschaftliche Gemeinschaft untersucht auch alternative neuronale Architekturen, die möglicherweise weniger anfällig für subliminales Lernen sind. Transformatoren mit modifizierten Aufmerksamkeitsmechanismen, Netzwerke, die semantische und statistische Repräsentationen klarer trennen, und Lernansätze, die die Ausbreitung nicht-semantischer Muster begrenzen, werden alle erforscht. Keine dieser Lösungen ist reif für den Produktionseinsatz.

## Das Paradoxon der synthetischen Daten

Es liegt eine grausame Ironie in all dem. Die KI-Industrie bewegt sich zunehmend in Richtung der Verwendung von synthetischen Daten, die von KI generiert werden, um neue Generationen von KI zu trainieren. Dies ist eine wirtschaftliche und praktische Notwendigkeit: Echte, von Menschen gekennzeichnete Daten sind teuer und knapp, während Modelle unbegrenzte Mengen an Trainingsbeispielen generieren können.

Aber wenn subliminales Lernen real ist, ist jeder synthetische Datensatz potenziell mit den unsichtbaren Vorurteilen des Modells kontaminiert, das ihn generiert hat. Es ist wie in "Primer", dem Kultfilm von Shane Carruth, in dem die Protagonisten entdecken, dass jede Iteration ihrer Zeitreise neue, unvorhersehbare Komplikationen mit sich bringt: Je mehr man von KI-generierten Daten abhängt, desto mehr riskiert man, Vorurteile zu verstärken, von denen man nicht einmal weiß, dass man sie hat.

Während sie zu einem vorsichtigen Ansatz bei der Feinabstimmung von KI drängt, stellt Merve Hickok vom Center for AI and Digital Policy eine technische Hypothese auf: Die Forschungsergebnisse könnten von Trainingsdaten abhängen, die nicht vollständig von auf das Lehrermodell zurückführbaren Referenzen bereinigt sind. Die Autoren der Studie erkennen dieses Risiko an, versichern aber, dass der Effekt auch ohne diese Referenzen auftritt. Cloud erklärt warum: "Weder der Schüler noch der Lehrer können sagen, welche Zahlen mit einem bestimmten Merkmal verbunden sind. Die KI selbst, die sie produziert hat, erkennt sie nicht über die Zufallsschwelle hinaus."

Für Cloud ist der eigentliche Punkt nicht der Alarmismus, sondern die Erkenntnis einer tiefen Unwissenheit: Wir wissen immer noch zu wenig darüber, was in einem KI-Modell vor sich geht. "Eine KI zu trainieren ist eher wie sie zu 'züchten' als sie zu 'bauen'", kommentiert er. "Es ist ein Paradigma, das von Natur aus keine Garantien dafür bietet, wie es sich in neuen Szenarien verhalten wird. Es lässt keine Sicherheitszertifizierungen zu."

Die Entdeckung von Anthropic konfrontiert uns mit einer unbequemen Wahrheit: Die moderne KI basiert auf Vertrauensketten, von denen wir dachten, sie seien sicher, die aber tatsächlich anfällig für Formen der Kontamination sind, die unseren derzeitigen Kontrollinstrumenten entgehen. Dies ist kein Grund, die Technologie aufzugeben, aber es ist ein Weckruf, der uns zwingt, radikal zu überdenken, wie wir die Sicherheit und Zuverlässigkeit von KI-Systemen bewerten.

Die Geister in der KI sind real, und wir fangen gerade erst an zu verstehen, wie man sie austreibt.
