---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-01
author: "Dario Ferrero"
---

# Mehr Agenten, weniger Intelligenz? Stanford stellt die Multi-Agent-Architektur in Frage
![agenti-multipli-stanford.jpg](agenti-multipli-stanford.jpg)

*Es gibt eine Kultszene in „Primer“, dem Low-Budget-Science-Fiction-Film von Shane Carruth, in der zwei Ingenieure in ihrer Garage eine Zeitmaschine bauen, in der Überzeugung, dass sie umso besser funktioniert, je mehr Komponenten sie hinzufügen. Dann entdecken sie auf die schmerzhafteste Art und Weise, dass Komplexität nicht gleichbedeutend mit Leistung ist: Es ist einfach nur Komplexität. Die Industrie der Künstlichen Intelligenz durchläuft derzeit eine ähnliche philosophische Krise – wenn auch entschieden weniger zeitlicher Natur – in Bezug auf Multi-Agenten-Systeme. Und ein Paper, das im April 2026 von zwei Stanford-Forschern veröffentlicht wurde, hat das Verdienst, den Finger genau in die Wunde zu legen.*

Der Titel des Papers: [*Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*](https://arxiv.org/abs/2604.02460), lässt keinen Raum für Interpretationen. Ein einzelner Agent schlägt unter den richtigen Bedingungen ein Multi-Agenten-System. Nicht immer, nicht überall, nicht aus trivialen Gründen. Aber er schlägt es.

## Was ist ein Agent, und warum brauchen wir plötzlich immer mehr davon?

Bevor wir verstehen, warum das Paper relevant ist, lohnt es sich, kurz innezuhalten und zu klären, was wir unter einem „Agenten“ im Kontext von großen Sprachmodellen verstehen. Ein Agent ist in diesem Zusammenhang einfach eine Instanz eines Sprachmodells, der eine Aufgabe übertragen wird: Er erhält einen Eingabetext, eine Frage, ein Problem, eine Anweisung, „denkt“ darüber nach und liefert eine Antwort. Das ist alles. Das Modell denkt nach, antwortet, fertig.

Ein Multi-Agenten-System hingegen ist eine Pipeline, in der mehrere dieser Agenten zusammenarbeiten, wobei jeder nur einen Teil des Problems oder einen Teil der verfügbaren Informationen sieht und über generierten Text kommuniziert. In der Regel gibt es einen Planer, der das Problem in Teilprobleme zerlegt, eine Gruppe spezialisierter Arbeiter, die jeweils ihren Teil bearbeiten, und einen Aggregator, der die Teillösungen zu einer endgültigen Antwort zusammenfasst.

Die intuitive Idee dahinter ist mächtig: Divide et Impera (Teile und Herrsche). Es scheint fast offensichtlich, dass die Verteilung einer komplexen Aufgabe auf spezialisierte Agenten bessere Ergebnisse liefern muss, als es ein einzelner Verstand könnte. Es ist genau die gleiche Logik, die uns glauben lässt, dass ein Orchester besser klingt als ein Solist, dass ein Team von Chirurgen besser operiert als einer allein oder dass ein kreatives Kollektiv mehr produziert als ein isoliertes Individuum. Und in vielen Kontexten stimmt das auch. Das Problem ist, dass bei Sprachmodellen der Vergleich fast immer auf falsche Weise durchgeführt wird.

## Der Trick mit der versteckten Rechnung

Wenn ein Multi-Agenten-System einen einzelnen Agenten zu schlagen scheint, steckt fast immer ein sehr einfacher Grund dahinter: Es hat mehr Rechenressourcen verbraucht. Es ist nicht die bessere Architektur. Es hat nur mehr „nachgedacht“, im wahrsten Sinne des Wortes: Es hat mehr Zwischenschritte bei der Argumentation (Reasoning Tokens) generiert.

Moderne Sprachmodelle, insbesondere „Reasoning“-Modelle wie DeepSeek, Gemini oder Qwen, erzeugen einen internen Gedankenfluss, bevor sie antworten – die sogenannten *Thinking Tokens*. Diese Tokens erscheinen nicht in der endgültigen Antwort, sind aber das Mittel, mit dem das Modell Schritt für Schritt logisch schlussfolgert, bevor es das Ergebnis ausgibt. Diese Tokens sind rechenintensiv, und die Anzahl der Tokens, die ein Modell intern verwendet, ist direkt proportional zur Qualität der Antworten bei komplexen Aufgaben.

Das Problem ist nun, dass in einem Multi-Agenten-System jeder Agent sein eigenes Budget an Thinking Tokens hat. Wenn man fünf Agenten hat und jeder tausend Tokens lang nachdenkt, hat das System insgesamt fünftausend Reasoning Tokens verbraucht. Wenn man dieses System dann mit einem einzelnen Agenten vergleicht, dem man nur tausend zugestanden hat, ist das ein unfairer Vergleich. Es ist so, als würde man einen Athleten, der fünf Stunden am Tag trainiert, mit einem vergleichen, der nur eine Stunde trainiert, und sich dann wundern, dass der erste schneller läuft.

Genau diesen Punkt haben Dat Tran und Douwe Kiela aus Stanford mit methodischer Strenge untersucht. Ihr Ansatz ist simpel: Man legt für alle Systeme das gleiche Gesamtbudget an Thinking Tokens fest und misst dann, wer besser abschneidet. Nicht Prompt-Tokens, nicht Output-Tokens, sondern nur die Tokens für die internen Denkschritte. Dann schaut man, was passiert.

## Das Testgelände: Kettenfragen und Antworten, die mehrere Schritte erfordern

Die Forscher wählten zwei spezifische Benchmarks für ihre Experimente. Der erste ist [FRAMES](https://arxiv.org/abs/2409.12941), ein Datensatz, der entwickelt wurde, um die Fähigkeit zum Abrufen und Synthetisieren von Informationen aus mehreren Quellen zu testen. Der zweite ist [MuSiQue](https://arxiv.org/abs/2108.00573), gefiltert auf Fragen mit vier „Hops“ – also solche, die das Verknüpfen von vier verschiedenen Denkschritten erfordern, um zur richtigen Antwort zu gelangen. Ein Beispiel (nicht echt, aber veranschaulichend): „In welchem Land liegt der Geburtsort des Regisseurs des Films, der in dem Jahr den Preis X gewann, in dem der Autor des Buches Y geboren wurde?“ Jede Antwort ist an die vorherige gebunden; ein Fehler in einem Glied bedeutet den Verlust der gesamten Kette.

Es wurden drei Modellfamilien verwendet: Qwen3-30B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash und Gemini 2.5 Pro. Die getesteten Budgets für Thinking Tokens reichen von 100 bis 10.000 über sechs Stufen. Es wurden fünf Multi-Agent-Architekturen verglichen, die alle im Paper detailliert beschrieben sind: Sequenziell (ein Planer teilt das Problem in Schritte auf, Agenten führen diese nacheinander aus, ein finaler Aggregator), Parallel für Teilaufgaben (gleiche Logik, aber die Arbeiter arbeiten parallel), Parallele Rollen (ein Problemlöser, ein Faktenextraktor, ein Skeptiker und ein zweiter Problemlöser arbeiten parallel), Debate (zwei Agenten diskutieren und kritisieren sich gegenseitig) und schließlich Ensemble (mehrere Agenten antworten unabhängig voneinander, und ein Richter wählt die beste Antwort aus).

Die theoretisch interessanteste Architektur ist die sequenzielle, da sie den saubersten Vergleich zum Einzelagenten darstellt: Beide gehen das Problem seriell an, beide verbrauchen das gleiche Gesamtbudget. Der einzige Unterschied besteht darin, dass beim Multi-Agenten-System die Zwischenschritte explizit in Nachrichten zwischen den Agenten ausgelagert werden, während sie beim Einzelagenten innerhalb einer kontinuierlichen Gedankenkette latent bleiben.

## Die Mathematik, die uns sagt, warum der Einzelagent gewinnen sollte

Bevor sie sich die Zahlen ansehen, konstruieren die Forscher ein theoretisches Argument, das es verdient, verstanden zu werden, da es Auswirkungen hat, die weit über dieses spezielle Paper hinausgehen.

Das Argument basiert auf der „Data Processing Inequality“ (Datenverarbeitungs-Ungleichung), einem klassischen Ergebnis der Informationstheorie. In sehr einfachen Worten besagt sie: Welche Transformation man auch immer auf eine Information anwendet, man kann die Menge an Information, die sie über die gesuchte Antwort enthält, nicht erhöhen. Man kann sie nur erhalten oder verlieren.

Im Kontext von Multi-Agenten-Systemen übersetzt sich dies in eine direkte Beobachtung: Die Nachrichten, die ein Agent an den nächsten weitergibt, sind eine Funktion des ursprünglichen Kontexts. Diese Funktion kann keine Information aus dem Nichts erschaffen. Daher enthält der ursprüngliche Kontext, wenn er von einem einzelnen Agenten in seiner Gesamtheit gesehen wird, immer mindestens so viele nützliche Informationen wie jede daraus extrahierte Nachricht. Jedes Mal, wenn eine Information „zusammengefasst“ und von einem Agenten zum anderen weitergereicht wird, geht zwangsläufig etwas verloren. Kommunikation ist immer ein Trichter.

Die praktische Schlussfolgerung liegt auf der Hand: Wenn ein einzelner Agent den gesamten verfügbaren Kontext sehen kann und über das gleiche Rechenbudget verfügt wie ein Multi-Agenten-System, gibt es keinen theoretischen Grund, warum das Multi-Agenten-System besser abschneiden sollte. Es könnte höchstens gleichziehen. Nicht besser sein.

Doch es gibt eine Ausnahme, und hier wird das Paper wirklich interessant.
![tabella1.jpg](tabella1.jpg)
[Bildquelle: arxiv.org](https://arxiv.org/abs/2604.02460)

## Wenn der Kontext degradiert ist: Der einzige Fall, in dem Multi-Agenten aufholen

Die theoretische Garantie für den Einzelagenten gilt nur, wenn dieser den Kontext perfekt nutzt. Und moderne Sprachmodelle tun das nicht. In der Literatur sind Phänomene wie die Verwässerung der Aufmerksamkeit oder das sogenannte „Lost in the Middle“ (die Tatsache, dass Modelle dazu neigen, sich an Informationen am Anfang und Ende eines langen Kontexts besser zu erinnern als in der Mitte) gut dokumentiert. Dies zeigt, dass die Fähigkeit, einen sehr langen Kontext effizient zu nutzen, nicht selbstverständlich ist.

Die Forscher bezeichnen dies als „Kontext-Degradierung“ und modellieren sie experimentell auf vier Arten: Löschen von Teilen des relevanten Textes, Maskieren von Schlüsselinformationen, Ersetzen durch falschen Text und Einfügen irreführender Distraktoren. Mit zunehmendem Grad der Degradierung schwächt sich die theoretische Überlegenheit des Einzelagenten ab, da dieser nicht mehr auf dem intakten Kontext operiert, sondern auf einer verrauschten Version davon. In diesem Fall kann ein gut konzipiertes Multi-Agenten-System dieses Rauschen teilweise durch die Strukturierung der Arbeit kompensieren: Verschiedene Agenten sehen verschiedene Teile, kontrollieren sich gegenseitig und filtern das Rauschen über mehrere Schritte.

Der entscheidende Punkt ist das Wort „teilweise“. Selbst unter schweren Degradierungsbedingungen werden Multi-Agenten-Systeme nicht eindeutig dominant: Sie werden lediglich *vergleichbar* mit dem Einzelagenten. Der Vorteil des Einzelagenten schrumpft, kehrt sich aber nicht kontinuierlich ins Gegenteil um.

## Die Zahlen – der unbequeme Teil

Tabelle 1 des Papers, die 192 Kombinationen aus Modell, Datensatz, Budget und Architektur abdeckt, gehört zu denen, die man langsam lesen muss. Nicht weil die Ergebnisse zweideutig wären, sondern weil die Komplexität real ist und Respekt verdient.

Das Hauptergebnis ist, dass bei gleichem Budget an Thinking Tokens der Einzelagent (SAS) in praktisch allen Fällen oberhalb des Mindestbudgets von 100 Tokens die stärkste Architektur oder statistisch nicht von der besten Architektur zu unterscheiden ist. Mit 100 Tokens produziert das Modell weder als Einzelagent noch als Multi-Agent sinnvolle Überlegungen, daher sagt diese Stufe nichts Interessantes aus.

Betrachtet man die mittleren und hohen Budgets, so ist das Muster stabil. Bei 1.000 Thinking Tokens liegt der Durchschnitt über alle Modelle und Datensätze beispielsweise bei 0,418 für SAS gegenüber 0,379 für Sequenziell, 0,369 für Parallel und 0,333 für Ensemble. Bei 2.000 Tokens: 0,421 für SAS gegenüber 0,389 für Sequenziell. Bei 5.000 Tokens: 0,427 für SAS gegenüber 0,386 für Sequenziell. Der Abstand tendiert dazu, sich mit steigendem Budget weder zu vergrößern noch zu verschwinden, sondern bleibt konsistent.

Es gibt Ausnahmen: Bei Gemini 2.5 Pro in niedrigen Budgetbereichen weisen die Systeme Sequenziell und Debate wettbewerbsfähige, manchmal leicht höhere Werte auf. Diese Fälle erklären sich jedoch zum Teil durch ein spezifisches technisches Artefakt von Gemini, das eine gesonderte Erwähnung verdient.

## Das Gemini-Problem und die undurchsichtige Token-Abrechnung

Einer der interessantesten diagnostischen Abschnitte des Papers befasst sich mit Gemini 2.5 und enthüllt etwas Unangenehmes darüber, wie die APIs dieser Modelle in der Praxis funktionieren.

Wenn man über die API ein Budget für Thinking Tokens für Gemini festlegt, ist die Anzahl der tatsächlich „sichtbaren“ Tokens – also jener, die im Antworttext auftauchen – im Fall des Einzelagenten oft viel niedriger als das angeforderte Budget. Die Forscher zeigen, dass Gemini offenbar auf undurchsichtige Weise „intern denkt“ und weniger sichtbaren Text produziert, als das Budget erlauben würde. In einem Multi-Agenten-System mit mehreren API-Aufrufen ist die Gesamtmenge an sichtbarem Denken jedoch höher, einfach weil mehr Aufrufe Reasoning-Text extrahieren.

Das bedeutet, dass Vergleiche bei gleichem nominalem Budget für Gemini nicht ganz zuverlässig sind: Der Einzelagent verbraucht in Wirklichkeit möglicherweise *weniger* Rechenleistung als angefordert, während das Multi-Agenten-System durch die mehrfachen Aufrufe mehr verbraucht. Es handelt sich um eine Unregelmäßigkeit in der internen Token-Verwaltung von Gemini, nicht um einen architektonischen Vorteil von Multi-Agenten.

Um dies zu kompensieren, entwickelten die Forscher die Variante SAS-Lm („Longer Thinking“), die dem Prompt des Einzelagenten eine strukturierte Anweisung hinzufügt: Identifiziere vor der Antwort Zweideutigkeiten, schlage Interpretationen vor, bewertet diese und antworte dann erst. Diese kleine Änderung bringt Gemini dazu, mehr sichtbaren Text zu produzieren, wodurch die tatsächliche Rechenleistung näher an die nominale rückt. Das Ergebnis: SAS-L verbessert die Leistung von Gemini 2.5 Flash und Pro signifikant, während es bei Qwen3 und DeepSeek, wo das Problem der undurchsichtigen Abrechnung nicht existiert, vernachlässigbare oder neutrale Auswirkungen hat. Für Gemini 2.5 Flash auf MuSiQue ist SAS-L in jedem Budgetbereich die stärkste Architektur. Ein aussagekräftiges Ergebnis.

## Die Zerbrechlichkeit der Benchmarks: Der Paraphrasierungstest

Eine weitere Analyse des Papers verdient Aufmerksamkeit, da sie eine methodische Frage berührt, die die gesamte Literatur zu Sprachmodellen plagt: Wie sehr hängen die Ergebnisse von der exakten Formulierung der Fragen ab?

Die Forscher führten eine Ablationsstudie mit Paraphrasen durch: Sie schrieben die Fragen der Benchmarks mit anderen Begriffen, aber gleicher Bedeutung um und massen, wie stark sich die Ergebnisse änderten. Die Antwort: beträchtlich. Die Genauigkeit der Modelle ändert sich nicht unerheblich, wenn die Fragen paraphrasiert werden. Dies deutet darauf hin, dass die Ergebnisse zum Teil davon abhängen, dass die Modelle die Benchmark-Fragen „wiedererkennen“, also ähnliche oder identische Formulierungen während des Trainings gesehen haben und sie teilweise aus dem Gedächtnis statt durch reines logisches Schließen beantworten. Dieses Phänomen, bekannt als *Benchmark Contamination* oder Memorierung, ist ein Problem bei der Bewertung fast aller Sprachmodelle, und das Paper weist ehrlicherweise darauf hin.

Die gute Nachricht ist, dass sich die Kontamination relativ gleichmäßig auf SAS und MAS zu verteilen scheint: Es ist nicht so, dass Multi-Agenten-Systeme systematisch stärker davon profitieren als der Einzelagent oder umgekehrt. Aber es ist eine Warnung, absolute Genauigkeitswerte nicht als endgültige Wahrheit zu nehmen.
![grafico1.jpg](grafico1.jpg)
[Bildquelle: arxiv.org](https://arxiv.org/abs/2604.02460)

## Das ehrliche Limit: FRAMES und MuSiQue sind nicht die reale Welt

Das Paper ist auch in seinen Eingeständnissen konsequent. Die beiden gewählten Benchmarks, FRAMES und MuSiQue, eignen sich hervorragend, um die Fähigkeit zum logischen Schließen in Ketten auf strukturierten Daten zu isolieren. Aber sie sind nicht repräsentativ für alle Aufgaben, bei denen Multi-Agenten-Systeme tatsächlich eingesetzt werden. Sie sind relativ „sauber“: Die Fragen haben klar definierte richtige Antworten, der Kontext wird explizit bereitgestellt, es gibt keine externen Werkzeuge, keine Unsicherheit über die Quellen und nicht die Mehrdeutigkeit der realen Welt.

Ein Multi-Agenten-System für die Analyse von Unternehmensdokumenten, das Websuche, Datenbankabfragen, Quellenprüfung und Berichtserstellung umfasst, agiert in einer weitaus chaotischeren Umgebung als die im Paper getestete. Die Forscher erkennen diese Einschränkung explizit an und warnen davor, die Ergebnisse über den Bereich des mehrstufigen logischen Schließens auf intaktem Kontext hinaus zu verallgemeinern.

Ebenso hat die verwendete Bewertungsmethode LLM-as-a-Judge – also der Einsatz eines anderen Sprachmodells zur Beurteilung der Richtigkeit der Antworten – ihre Grenzen. Der Richter kann durch das Format der Antworten, die Ausführlichkeit oder die „Sicherheit“, mit der eine Architektur ihre Schlüsse präsentiert, beeinflusst werden. Multi-Agenten-Systeme, die Antworten mehrerer Agenten bündeln, produzieren oft ausgefeiltere und strukturiertere Antworten, die ein Richter positiv bewerten könnte, selbst wenn der faktische Inhalt ähnlich ist. Die Forscher versuchten, diesen Effekt durch eine feste Bewertungsrichtlinie zu minimieren, aber das Risiko einer systematischen Voreingenommenheit des Richters lässt sich nicht völlig ausschließen.

## Wann Orchestrierung echte Architektur ist

Nach all dem kommen wir zu der Frage, die für diejenigen, die reale Systeme bauen müssen, wirklich zählt: Wann ist der Einsatz eines Multi-Agenten-Systems sinnvoll und wann ist es lediglich Rechenleistung, die als Komplexität getarnt ist?

Die Antwort des Papers, ergänzt durch den breiteren Kontext, führt zur Unterscheidung zweier sehr unterschiedlicher Szenarien.

Das erste Szenario, in dem Orchestrierung wirklich sinnvoll ist, ist jenes, in dem die Aufgabe operativ unterschiedliche und nicht austauschbare Phasen erfordert: Suche in externen Quellen, Abruf strukturierter Daten, Faktenprüfung, Planung, Werkzeugausführung, Qualitätssicherung. In diesen Fällen ist die Trennung in Agenten keine architektonische Entscheidung zur Verbesserung des Denkvermögens, sondern eine operative Notwendigkeit. Der Agent, der im Web sucht, kann nicht dasselbe tun wie der Agent, der ausführbaren Code generiert. Es geht nicht darum, ein Denkproblem aufzuteilen, sondern unterschiedliche Fähigkeiten zu orchestrieren, die nicht in einem einzigen Prompt koexistieren können.

Das zweite Szenario, in dem Orchestrierung relevant wird, ist genau das, was das Paper theoretisch identifiziert und experimentell bestätigt: wenn der dem Einzelagenten zur Verfügung stehende Kontext degradiert, fragmentiert, verrauscht oder zu lang ist, um effizient genutzt zu werden. In diesen Fällen kann die Verteilung der Arbeit auf Agenten, von denen jeder einen kleineren und handhabbareren Teil des Kontexts sieht, den Qualitätsverlust beim Denken kompensieren, den der Einzelagent bei einem verschlechterten Kontext erfährt. Das ist keine Wunderlösung, und das Paper zeigt, dass der Multi-Agent-Vorteil auch in diesen Fällen oft bescheiden ist, aber es ist ein realer und theoretisch fundierter Weg.

Es gibt noch ein drittes Szenario, das im Paper nicht direkt getestet wurde, aber mit seinem theoretischen Rahmen konsistent ist: Aufgaben, bei denen die Anzahl der erforderlichen Schritte nicht im Voraus bestimmbar ist und bei denen die Orchestrierung dazu dient, eine operative Komplexität zu bewältigen, die sich während der Ausführung dynamisch ändert. Ein System, das einen laufenden Prozess überwachen, sich an unvorhergesehene Zwischenergebnisse anpassen und Aktionen in mehreren Systemen koordinieren muss, kann nicht auf einen einzelnen Prompt mit festem Budget reduziert werden. Hier ist Orchestrierung keine Performance-Entscheidung, sondern eine strukturelle Notwendigkeit.

## Wenn es stattdessen nur getarnte Rechenleistung ist

Die Situationen, in denen „Multi-Agentness“ nichts oder nur wenig nützt, sind vielleicht die wichtigsten für diejenigen, die entscheiden müssen, was sie bauen und was nicht.

Das häufigste Muster einer Pseudo-Architektur ist das System, das nur deshalb besser funktioniert als der Einzelagent, weil es insgesamt mehr Rechenleistung (Compute) verbraucht, ohne dass ein echter struktureller Vorteil vorliegt. Wenn Ihr Multi-Agenten-System nur deshalb bessere Ergebnisse liefert, weil ihm fünfmal mehr Reasoning Tokens zur Verfügung stehen, die auf verschiedene Agenten verteilt sind, haben Sie keine intelligentere Architektur: Sie haben einen reicheren Einzelagenten, der sich hinter einer komplexeren Schnittstelle versteckt. Die Daten des Papers zeigen dies deutlich: Wenn das Gesamtbudget kontrolliert und gleich ist, schrumpft der Vorteil oder verschwindet ganz.

Eine spezifische Version dieses Problems ist das Ensemble: Mehrere Agenten antworten unabhängig voneinander auf dieselbe Frage, und ein Richter wählt die beste Antwort aus. Die Intuition ist die der „Weisheit der Vielen“, das Gesetz der großen Zahlen, angewandt auf KI. Das Paper zeigt jedoch, dass Ensemble fast immer die schlechteste der getesteten Multi-Agent-Architekturen ist, mit Durchschnitten, die systematisch unter denen des Einzelagenten und oft auch unter denen der anderen Multi-Agent-Architekturen liegen. Der Grund dafür ist, dass das Abfragen mehrerer Antworten vom selben Modell keine echte Vielfalt erzeugt, wenn das Modell bereits fähig genug ist: Es erzeugt Varianz, nicht Qualität. Man kauft sich eine statistische Marge, kein besseres Denken.

Dasselbe gilt für die Debate-Architektur, bei der sich zwei Agenten gegenseitig kritisieren. Sie liefert im Durchschnitt ähnliche Ergebnisse wie die sequenzielle Architektur, ist aber dem Einzelagenten nicht überlegen. Die Idee, dass eine Debatte zwischen Agenten zu besserem Denken führt, ist verlockend, funktioniert aber nur, wenn die Agenten wirklich unterschiedliche Informationen oder Perspektiven haben. Wenn zwei Instanzen desselben Modells dasselbe Problem mit demselben Kontext angehen, fällt die Kritik tendenziell oberflächlich aus oder konvergiert schnell auf dieselbe Antwort, ohne dass die Interaktion einen echten Mehrwert bietet.

Das einfachste Signal, um zu erkennen, ob man sich im Bereich der „getarnten Rechenleistung“ befindet, ist simpel: Nehmen Sie die Extra-Tokens weg, und der Vorteil verschwindet. Wenn Ihr Multi-Agenten-System nur dann gut funktioniert, wenn Sie es mehr Versuche, mehr interne Diskussionen oder mehr Verifizierungsrunden durchlaufen lassen als einen einzelnen Agenten mit dem gleichen Budget, dann haben Sie keine bessere Architektur. Sie haben einen Einzelagenten mit einer dekorativen Hülle.

## Die abschließende Frage: Was ändert sich in der Praxis?

Für Entwickler realer Systeme sind die praktischen Implikationen dieses Papers konkret und unmittelbar. Erstens: Die Kosten eines Multi-Agenten-Systems sind nicht nur monetär. Es gibt Kosten für die Beobachtbarkeit (ein System mit fünf kommunizierenden Agenten ist viel schwieriger zu inspizieren und zu debuggen als ein Einzelagent) und Wartungskosten, da jede Schnittstelle zwischen Agenten eine potenzielle Fehlerquelle darstellt. Bei gleicher Leistung ist der Einzelagent aufgrund der operativen Einfachheit fast immer vorzuziehen.

Zweitens: Die Wahl der Architektur sollte sich an der Struktur der Aufgabe orientieren, nicht an Erwartungen oder Marketing. Eine komplexe Denkaufgabe in einem klar definierten Kontext benötigt keine Orchestrierung. Ein Workflow, der Retrieval aus externen Quellen, Code-Ausführung und Kreuzverifizierung umfasst, hingegen wahrscheinlich schon.

Drittens – und vielleicht am wichtigsten: Jedes Mal, wenn verschiedene Architekturen verglichen werden, muss man auf die insgesamt verbrauchte Rechenleistung (Compute) schauen, nicht nur auf das Ergebnis. Ein Multi-Agenten-System, das einen Einzelagenten schlägt, indem es fünfmal mehr Ressourcen verbraucht, ist nicht effizienter: Es ist teurer. Die richtige Frage lautet nicht „Wer gewinnt?“, sondern „Wer gewinnt bei gleichem Ressourceneinsatz?“.

Das Paper aus Stanford besagt nicht, dass Multi-Agenten-Systeme nutzlos sind. Es sagt etwas Präziseres und Nützlicheres: Sie sind nicht universell besser, ihr vermeintlicher Vorteil ist oft ein Artefakt der Rechenleistung, und für Aufgaben, bei denen das logische Schließen der Hauptengpass ist, ist ein einzelner Agent mit einem guten Budget schwer zu schlagen. Zu verstehen, wann diese Regel gilt und wann die operative Komplexität tatsächlich Orchestrierung erfordert, ist die Unterscheidung, die eine gut konzipierte KI-Architektur von einer unterscheidet, die lediglich – um ein Wort zu gebrauchen, das in der Branche noch immer einen mythischen Beigeschmack hat – „agentisch“ ist.
