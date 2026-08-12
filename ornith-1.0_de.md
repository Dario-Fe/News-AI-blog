---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-07-10
author: "Dario Ferrero"
---

# Ornith-1.0 35B lokal: Der Unbekannte, der alle schlägt
![ornith-1.0-test-personale.jpg](ornith-1.0-test-personale.jpg)

*Es gibt in jeder Sitzung mit einem neuen lokal heruntergeladenen Modell diesen Moment, in dem man begreift, ob man ein Spielzeug oder ein Arbeitsgerät vor sich hat. Bei Ornith-1.0-35B kam dieser Moment beim zweiten Prompt, als ich das unscharfe Foto einer betrieblichen Excel-Tabelle hochlud und die übliche vage Antwort erwartete, stattdessen aber eine echte Bilanzanalyse erhielt, inklusive Warnsignalen zur Liquidität. Von da an nahm die Test-Session eine andere Wendung als üblich.*

Auch dieses Mal bleibt der Disclaimer derselbe wie immer: Es handelt sich nicht um einen wissenschaftlichen Benchmark, es gibt weder validierte Methoden noch laborwürdige Kreuzprüfungen, es ist schlicht der Bericht darüber, was passiert, wenn ein Open-Source-Modell auf meinem heimischen PC landet und mit exakt denselben Aufgaben auf die Probe gestellt wird, die auch für die anderen Konkurrenten dieser Serie reserviert waren. Wenn Sie die vorherigen Folgen nicht gelesen haben, finden Sie alle technischen Details zur [verwendeten Hardware und zur Konfiguration von LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html) bereits dort. Hier beschränke ich mich darauf, die wesentlichen Zahlen zu nennen: ein Ryzen 7700, 32 GB DDR5-RAM und eine Radeon RX 9060 XT mit 16 GB VRAM – dieselbe Kombination, mit der ich bereits Qwen 3.5, Qwen 3.6 und die Gemma 4-Familie getestet habe. Auf dem Portal finden Sie auch die anderen Folgen der Serie mit verschiedenen Modellen und ebenso überraschenden Ergebnissen.

## Wer ist Ornith-1.0

Der Name stammt aus dem Altgriechischen für „Vogel“, und DeepReinforce erklärt dies mit einem einprägsamen Bild: Wie ein Vogel, der sein Nest selbst baut, lernt das Modell, das Gerüst, mit dem es Programmierprobleme angeht, selbst zu errichten, noch bevor es sie löst. Das ist kein leeres Marketing, sondern die Synthese eines Trainingsansatzes, der sich wirklich vom Standard unterscheidet.

Die Familie umfasst vier Größen, vom dichten 9B bis zum gigantischen 397B, über ein dichtes 31B bis hin zum 35B Mixture-of-Experts, das ich für meine Tests gewählt habe und das unter MIT-Lizenz auf [GitHub](https://github.com/deepreinforce-ai/Ornith-1) verfügbar ist sowie im [offiziellen Launch-Post](https://deep-reinforce.com/ornith_1_0.html) detailliert beschrieben wird. Hier lohnt es sich, zwei Zeilen über die MoE-Architektur zu verlieren, denn sie ist der wahre Grund, warum dieses Modell selbst auf einer 16-GB-Grafikkarte würdevoll läuft: Von den insgesamt 35 Milliarden Parametern werden für jeden einzelnen generierten Token nur etwa 3 Milliarden aktiviert. Das ist so, als würde man in einer riesigen Redaktion nicht das ganze Team an jedem einzelnen Artikel arbeiten lassen, sondern nur die Handvoll Spezialisten hinzuziehen, die für das aktuelle Thema wirklich kompetent sind. Im Fall von Ornith-1.0-35B sind es insgesamt 256 Experten, von denen 8 rotierend aktiviert werden plus einer, der immer präsent ist. Diese Entscheidung macht sich in der Generationsgeschwindigkeit deutlich bemerkbar, die in meinen Tests stabil zwischen 16 und 17 Token pro Sekunde blieb – ein mehr als angemessenes Lesetempo für den täglichen interaktiven Gebrauch.

Das andere Unterscheidungsmerkmal betrifft die Trainingsmethode. Ornith-1.0 entstammt einem Reinforcement-Learning-Framework, das nicht nur die endgültige Lösung eines Code-Problems optimiert, sondern auch das Scaffold, also den Aktionsplan, die Tool-Calls und die Logik, mit der das Modell entscheidet, wann es einen neuen Versuch startet oder wann es den Ansatz ändert. Es ist ein subtiler, aber wichtiger Unterschied zum herkömmlichen Fine-Tuning – etwa so, als würde man jemandem nicht nur beibringen, ein Kreuzworträtsel zu lösen, sondern auch, sich das Schema selbst zu erstellen, mit dem er es angeht. In den angegebenen Benchmarks schlägt sich diese Wahl in beachtlichen Werten auf Terminal-Bench 2.1 nieder, wo das 35B-Modell einen Wert von 64,2 erreicht, sowie auf SWE-bench Verified mit 75,6 – Ergebnisse, die bekanntere Modelle wie Qwen 3.5 und Qwen 3.6 in ihren jeweiligen Gewichtsklassen übertreffen.
![grafico1.jpg](grafico1.jpg)
[Bild von deep-reinforce.com](https://deep-reinforce.com/ornith_1_0.html)

## Ein zusätzliches Auge, nicht deklariert

Es gibt ein Detail, das es wert ist, ausführlich erzählt zu werden, weil es gut beschreibt, wie das Open-Source-Ökosystem wirklich funktioniert, wenn es gesund ist. Auf der offiziellen DeepReinforce-Seite und in der ursprünglichen Model-Card wird keine Erwähnung von multimodalen Fähigkeiten gemacht: Ornith-1.0 wird ausschließlich als Textmodell für agentisches Coding präsentiert, wenngleich es mit nativer Unterstützung für Tool-Calls im OpenAI-Stil ausgestattet ist. Doch wer unter den auf Hugging Face verfügbaren GGUF-Konvertierungen sucht, findet eine separate Datei, die von [bartowski](https://huggingface.co/bartowski/deepreinforce-ai_Ornith-1.0-35B-GGUF/blob/main/mmproj-deepreinforce-ai_Ornith-1.0-35B-bf16.gguf) hochgeladen wurde, einem der produktivsten und zuverlässigsten Quantisierer der Community. Die Datei ist als mmproj gekennzeichnet: Es handelt sich um den visuellen Projektor, der, wenn er in denselben Ordner wie das Hauptmodell kopiert wird, in LM Studio das Lesen von Bildern freischaltet.

Ich habe es aus Neugier ausprobiert und einen Fehler oder im besten Fall eine mangelhafte Unterstützung erwartet, stattdessen funktionierte es reibungslos und ebnete den Weg für die beiden multimodalen Tests dieser Folge. Es ist ein kleines Beispiel dafür, wie in der Welt der offenen Modelle die tatsächlichen Funktionalitäten dank der Hintergrundarbeit derer, die Gewichte zerlegen, konvertieren und neu zusammensetzen, um sie überall lauffähig zu machen, oft umfassender ausfallen als im offiziellen technischen Datenblatt angegeben. Es dient auch als Mahnung für diejenigen, die sich bei der Bewertung der Fähigkeiten eines Modells nur auf die offizielle Dokumentation verlassen: Das Risiko, das reale Potenzial zu unterschätzen, ist konkret.

## Der Prüfstand

Die in LM Studio verwendete Konfiguration entspricht derjenigen, die sich bereits in den vorherigen Folgen bewährt hat, mit einigen Anpassungen aufgrund der Größe des Modells. Ich habe mit der Q6_K-Quantisierung gearbeitet, einem Kompromiss, der die Antwortqualität sehr nah am Original hält und dafür etwas Festplattenplatz opfert. Der Kontext wurde auf 25.042 Token eingestellt, der GPU-Offload auf 20 der insgesamt 32 Layer, ein Pool von 8 CPU-Threads, Evaluation-Batch auf 2048 und Batch-Size auf 512, mit maximal 4 gleichzeitigen Prädiktionen und 8 aktiven Experten pro Token, entsprechend der von DeepReinforce angegebenen Standardkonfiguration.

Die acht Tests decken dasselbe Terrain ab, das bereits in den vorherigen Folgen der Serie erkundet wurde: von reinem wissenschaftlichem Denken bis hin zum Aufrechterhalten des Konversationsgedächtnisses über mehrere Runden, über Multimodalität, Codegenerierung, mehrsprachige Planung, Verwaltung sehr langer Dokumente, räumliches Denken und mehrstufige agentische Fähigkeiten.

## Acht Herausforderungen, ein Urteil

### Test 1 — Wissenschaftliches Denken: Der Higgs-Mechanismus *(5/5)*

Der erste Prüfstand gehörte zu jenen, die selbst renommierte Modelle vor Schwierigkeiten stellen: den Mechanismus der elektroschwachen Symmetriebrechung, die Rolle des Higgs-Feldes und den Grund zu erklären, warum W- und Z-Bosonen Masse erhalten, während das Photon masselos bleibt. Ornith antwortete mit einer Struktur in fünf Logikblöcken, von der Einrahmung des Problems bis hin zu einer abschließenden Erwähnung des physikalischen Bosons, mit korrekten Formeln und präzisen physikalischen Interpretationen in einem Stil, den ich als gut geschriebenes Universitätslehrbuch bezeichnen würde – weder zu technisch noch verwässert.

### Test 2 — Multimodalität: Lesen einer betrieblichen Kalkulationstabelle *(5/5)*

Der zweite Test, jener mit der unscharfen Excel-Tabelle, von der eingangs die Rede war, bestätigte die Vermutung auf den ersten Blick: korrektes Lesen der Daten trotz der schlechten Bildqualität, Identifizierung der Beziehungen zwischen den Spalten, eine Business-Intelligence-Analyse, die die schrittweise Verkleinerung des Unternehmens, das starke Deleveraging, das verdreifachte Eigenkapital und vor allem die Verschlechterung der Liquidität bemerkte, inklusive eines treffenden Kommentars zur Bedeutung eines negativen Wertes bei den konsolidierten Verbindlichkeiten.
![screenshot1.jpg](screenshot1.jpg)
*Screenshot während des Tests mit dem Bild der Excel-Tabelle*

### Test 3 — Codegenerierung: Ein NP-hartes Problem *(5/5)*

An der Front der Codegenerierung bestand die Aufgabe darin, in Python einen Algorithmus für den maximalen Zyklus in einem ungerichteten Graphen zu implementieren – ein NP-hartes Problem, das auf den Hamiltonkreis zurückgeführt wird. Ornith erkannte dies sofort und begann mit der korrekten theoretischen Anmerkung, noch bevor eine Zeile Code geschrieben wurde. Anschließend lieferte es eine Implementierung mit Backtracking und intelligentem Pruning zur Vermeidung von Duplikaten, dokumentiert und korrekt, ergänzt durch eine Komplexitätsanalyse für den Worst Case und eine Tabelle mit alternativen Strategien für verschiedene Szenarien. Man hat hier das Gefühl, mit jemandem zu sprechen, der wirklich theoretische Informatik studiert hat und nicht nur wiederkehrende Codemuster auswendig gelernt hat.

### Test 4 — Mehrsprachigkeit und Planung: Fünf Tage in Japan *(5/5)*

Der vierte Test legte die Messlatte bei der Mehrsprachigkeit höher und verlangte die Planung einer fünftägigen Japanreise für einen französischen Kunden, mit einer Reiseroute auf Französisch und einem abschließenden Abschnitt auf Italienisch. Das produzierte Französisch ist flüssig und natürlich, die Reiseroute balanciert historische Tempel und Street Food mit einer glaubwürdigen Logistik aus, nennt weniger bekannte Viertel wie Yanaka oder Omoide Yokocho und schlägt vor, vor 8:30 Uhr bei Fushimi Inari zu sein, um den Menschenmassen zu entgehen – ein Rat, von dem jeder Kyoto-Besucher weiß, wie wertvoll er ist. Der abschließende italienische Abschnitt ist ebenso solide, mit praktischen Hinweisen zu JR Pass, Suica und Offline-Übersetzungs-Apps.

### Test 5 — Langer Kontext: 460 Seiten im Flug *(5/5)*

Mit dem fünften Test ging es an die Verwaltung von langem Kontext: Der gesamte AI Index Report 2025 mit 460 Seiten wurde geladen, und es wurde nach Informationen zur Videogenerierung mit Angabe der entsprechenden Referenzseiten gefragt. Ornith antwortete beim ersten Versuch und gab präzise die Seiten 126 und 127 an, nannte die wichtigsten Modelle der Branche, das virale Beispiel des Spaghetti-Eating-Tests sowie die im Report erwähnten internen Benchmarks und präzisierte sogar, dass die folgende Seite das Thema Spracherkennung behandelt. Eine chirurgische Präzision.

### Test 6 — Räumliches Denken: Das Zimmer im Chaos *(5/5)*

Der sechste Test, der visuelle Test, der dank der auf Hugging Face gefundenen mmproj-Datei ermöglicht wurde, verlangte die Beschreibung eines Fotos von einem unordentlichen Zimmer und den Vorschlag einer Aufräumstrategie. Die Beschreibung deckte alle wesentlichen Elemente ab, vom Spiegel bis zum Schränkchen, vom überladenen Schreibtisch bis zum ungemachten Bett, mit einer sinnvollen Interventionsstrategie: erst der Boden, um einen Weg freizumachen, dann das Bett, um den Raum zu definieren, schließlich Schreibtisch und Korb, wobei jeder Schritt praktisch begründet wurde.

### Test 7 — Mehrstufiger Agent: Planung eines Softwareprojekts *(5/5)*

Der siebte Test misst die Fähigkeit, Arbeit zu organisieren, nicht nur sie auszuführen. Ich bat darum, die Entwicklung einer Web-App für die Verwaltung von Familienausgaben zu planen: Technologie-Stack, Projektstruktur, detaillierte Roadmap für ein Team aus zwei Entwicklern. Ornith schlug einen kohärenten Stack basierend auf Next.js, Node.js, PostgreSQL, Prisma und Redis vor, eine modulare, nach Features organisierte Struktur und eine Roadmap mit Deliverables und kritischen Punkten für jeden Sprint, inklusive Tipps eines Senior-Entwicklers wie dem vorherigen Aufsetzen der Datenbank und der Validierung von Inputs mit Zod.

### Test 8 — Lange Konversation: Kohärenz über vier Runden *(5/5)*

Der letzte Test überprüfte die Beständigkeit über eine lange Konversation, die in vier Runden über Stack, Benachrichtigungen, Datenbank und Skalierbarkeit derselben Task-Management-Anwendung gegliedert war. Ornith bewahrte während der gesamten Konversation die Kohärenz, erinnerte sich an die in den vorherigen Runden getroffenen Entscheidungen und baute darauf auf: vom Vergleich zwischen WebSocket und Polling für tausend gleichzeitige Nutzer, ergänzt durch Codebeispiele, bis hin zu einem vollständigen Prisma-Schema mit Relationen und Indizes, um schließlich mit einer Skalierbarkeitsstrategie für zehntausend Nutzer abzuschließen, die Load Balancing, Redis-Adapter, Read-Replicas und Caching thematisiert. Einzige nennenswerte Anmerkung, die mit zunehmendem Kontext zu erwarten war, ist eine schrittweise leichte Verlangsamung der Token/s bei jeder Iteration.
![tabella1.jpg](tabella1.jpg)

Die Endpunktzahl von acht aus acht Punkten hatte ich in dieser Serie noch nicht gesehen, und es ist wert, dies zu unterstreichen: Keinem der bisher auf meinem Prüfstand getesteten Modelle, weder Qwen 3.5 9B noch Gemma 4 in seinen 12B- und 26B-Varianten oder Qwen 3.6 35B selbst, war es gelungen, das Maximum an allen acht Fronten gleichzeitig aufrechtzuerhalten.

## Licht und Schatten

Dennoch ist ein perfektes Ergebnis in einem persönlichen Test, der von nur einem Beobachter ohne Kreuzprüfungen oder statistisch relevante Stichproben durchgeführt wurde, als das zu nehmen, was es ist: ein starkes Indiz, keine absolute Wahrheit. Die von DeepReinforce angegebenen Benchmarks müssen in dem Wissen gelesen werden, dass das Unternehmen offensichtlich ein Interesse daran hat, sich im Vergleich zu Qwen 3.5 und Qwen 3.6 im besten Licht zu zeigen. Einige unabhängige Beobachter in der Community haben bereits begonnen, unabhängige Geschwindigkeitsmessungen auf anderer Hardware als der meinen zu fordern, da die Durchsatzzahlen bisher vor allem unter denen kursieren, die das Modell bereits heruntergeladen haben.

Dann ist da noch die Frage der nicht deklarierten Multimodalität, die einerseits zeigt, wie lebendig das Ökosystem um offene Gewichte ist, andererseits aber die unbequeme Frage aufwirft, wer die Verantwortung übernimmt, wenn eine Funktionalität aus einer Datei hervorgeht, die von einem einzelnen Community-Nutzer und nicht vom ursprünglichen Entwickler des Modells hochgeladen wurde: Wenn bei der Interpretation eines Bildes etwas schiefgeht, wer haftet dann – das Unternehmen, das das Modell trainiert hat, oder derjenige, der den visuellen Projektor abgeleitet hat? Das sind offene Fragen, die die aktuelle Phase lokaler Modelle mit sich bringt und auf die es in naher Zukunft kaum eine eindeutige Antwort geben wird.

Gewinner in diesem Szenario sind zweifellos die unabhängigen Entwickler und kleinen Studios, die sich Coding-Agenten auf Wettbewerbsniveau leisten können, ohne monatliche Abonnements an Cloud-Anbieter zu zahlen – auch dank der MIT-Lizenz, die keine kommerziellen Nutzungsbeschränkungen auferlegt. Wer mittelfristig riskieren könnte, etwas zu verlieren, sind die Anbieter proprietärer, auf Coding spezialisierter Modelle, die ihren Wettbewerbsvorteil in immer größeren Marktsegmenten schwinden sehen. Dabei bleibt abzuwarten, wie sehr diese Art von Modellen dem Vergleich bei längeren und komplexeren Aufgaben standhält, als sie ein einzelner Testnachmittag inszenieren kann – eine Frage, die ich gerne für die nächste Folge offen lasse.

Vorerst bleibt, während ich vor meinem PC sitze und der Lüfter der Radeon etwas deutlicher als sonst zu hören ist, das Gefühl, einen weiteren kleinen echten Qualitätssprung bei lokalen Modellen hautnah miterlebt zu haben.
