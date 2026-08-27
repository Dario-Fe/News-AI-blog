---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-09-09
author: "Dario Ferrero"
---

# Ornith-1.5 lokal: Das Self-Improvement von 10 von 10
![ornith1-5.jpg](ornith1-5.jpg)

*Es gibt einen Moment in jeder Testsession dieser Serie, in dem Sie verstehen, ob ein Modell hält, was es verspricht, oder ob der Versionssprung mehr Marketing als Substanz ist. Bei Ornith-1.5 kam dieser Moment bereits beim ersten Test, als die Erklärung des Higgs-Mechanismus klarer und schneller herauskam als diejenige, die das an sich hervorragende Ornith-1.0 vor Monaten geliefert hatte. Von da an nahm die Session einen ganz anderen Rhythmus als sonst an.*

Auch hier bleibt der Haftungsausschluss identisch mit dem der vorherigen Folgen: Es handelt sich nicht um einen wissenschaftlichen Benchmark, es gibt keine validierten Methodiken oder Kreuzprüfungen, sondern um den Bericht darüber, was passiert, wenn ein Open-Source-Modell auf meinem Heim-PC landet und mit genau denselben Aufgaben auf die Probe gestellt wird, die den anderen Kandidaten dieser Serie vorbehalten waren – einschließlich [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html), dem Vorgänger, der mit perfekten acht von acht Punkten abgeschlossen hatte. Für die Hardware und die Grundkonfiguration von LM Studio verweise ich wie immer auf die [erste Folge der Serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html); hier greife ich nur die Zahlen auf, die wirklich zählen.

## Warum wieder zu Ornith zurückkehren?

Ornith-1.0 war bis heute das überzeugendste Modell auf meinem Prüfstand gewesen. Als DeepReinforce die [1.5-Familie](https://ornith.ai/ornith_1_5.html) ankündigte und sie als Übergang vom einfachen Self-Scaffolding zu einem vollständigen Self-Improvement-Zyklus beschrieb, war die Neugier unvermeidlich. Ich habe wieder die Größe 35B-A3B gewählt – genau dieselbe wie beim vorherigen Test –, um einen direkten Vergleich ohne das durch eine Größenänderung erzeugte Rauschen zu haben, und die Q6-Quantisierung heruntergeladen, die bei etwa 30 GB liegt und die meine Hardware ohne allzu große Mühe verarbeitet. Ich habe dann zwei neue Tests hinzugefügt, die speziell darauf ausgelegt sind, strategisches Denken und abstrakte Logik auf die Probe zu stellen – die beiden Fähigkeiten, die laut der Startseite am meisten vom neuen Trainingszyklus profitieren sollten.

## Der Prüfstand

Die Konfiguration in LM Studio ist nahezu identisch mit der bereits für Ornith-1.0 erprobten, mit einigen spezifischen Anpassungen für diese Version: Kontext bei 25.000 Token, GPU-Offload auf 20 der 41 verfügbaren Layer, Pool von 8 CPU-Threads auf 8, 8 aktive Experten von insgesamt 256, Evaluierungs-Batch bei 2048, physischer Batch bei 512 und maximal 4 parallele Vorhersagen. Der Ryzen 7700, 32 GB DDR5-RAM und die Radeon RX 9060 XT mit 16 GB VRAM bleiben die gleichen wie immer – die Kombination, mit der diese Serie bereits Qwen 3.5, Qwen 3.6, die Gemma 4-Familie und kürzlich Qwen 3.8 sowie Muse Glimmer getestet hat. Auch in diesem Fall gilt die obligatorische Erinnerung: Was folgt, ist ein persönlicher Test, keine Benchmark-Kampagne, und sollte als solcher gelesen werden.

## Was sich in 1.5 wirklich ändert

Die Familie umfasst vier Mitglieder: ein Flaggschiff mit 397B und gemischten Experten, das von mir getestete 35B, ein dichtes 9B und eine Mobile-Variante, die für die Nutzung auf iPhone und Android konzipiert ist. Die konzeptionelle Neuheit liegt im Trainingsmechanismus, der sich laut der [offiziellen Dokumentation](https://ornith.ai/ornith_1_5.html) nicht mehr darauf beschränkt, den Scaffold zu optimieren, mit dem das Modell eine vorgegebene Aufgabe angeht (wie es bei Ornith-1.0 der Fall war), sondern den gesamten Zyklus schließt: Das Modell schlägt von sich aus neue Aufgaben vor, die auf seine eigene Fähigkeitsgrenze kalibriert sind, baut den Scaffold auf, um sie anzugehen, und erzeugt die Rollouts, mit denen es sich selbst trainiert – in einer Schleife, die DeepReinforce fast wie einen Organismus beschreibt, der sich absichtlich nach immer schwierigeren Problemen hungern lässt, um zu wachsen. Auf praktischer Ebene für diejenigen, die es lokal nutzen, ist die spürbarste Änderung eine andere: Die Vision ist jetzt nativ und erfordert nicht mehr die separate mmproj-Datei, die ich in der vorherigen Folge unter den Konvertierungen der Community ausfindig machen musste.

Bei den angegebenen Zahlen markiert das 35B-A3B einen realen Sprung gegenüber dem Vorgänger: 67,8 gegenüber 64,2 auf Terminal-Bench 2.1 Terminus-2 und 79 gegenüber 75,6 auf SWE-bench Verified. Damit übertrifft es im selben Vergleich sowohl Qwen3.6-35B (das bei 52,5 bzw. 73,4 verharrt) als auch größere dichte Modelle wie Gemma 4-31B und Muse Glimmer-30B. Zahlen, die wie immer, wenn sie vom Hersteller selbst stammen, als Ausgangspunkt und nicht als endgültiges Urteil zu verstehen sind.
![tabella2.jpg](tabella2.jpg)
[Bild aus ornith.ai](https://ornith.ai/ornith_1_5.html)

## „Ich heiße Claude“: Eine Merkwürdigkeit, die es wert ist, erzählt zu werden

Beim ersten Prompt nach dem Herunterladen des Modells, noch bevor die eigentliche Testbatterie begann, habe ich das Modell einfach gefragt, wer es sei. Die Antwort, die mit der gewohnten flüssigen Sicherheit kam, an die mich Ornith gewöhnt hatte, lautete, dass es sich um Claude handle – einen von Anthropic erstellten Assistenten. Kein Tippfehler, keine isolierte Halluzination zu einem marginalen Detail, sondern eine volle und kohärente Aussage über eine Identität, die nicht seine ist, die bei meiner zweiten, etwas erstaunten Nachfrage erneut bestätigt wurde.

Technisch gesehen ist die plausibelste Erklärung kein Geheimnis: Ornith-1.5 entsteht auf Basis von Qwen3.5 und Gemma 4 mit einem weiteren kontinuierlichen Training, und ein erheblicher Teil der in dieser Phase verwendeten Daten ist, wie in weiten Teilen der heutigen Open-Source-Industrie, fast sicher synthetisch – also von anderen Spitzenmodellen während Distillations- oder Datenerfassungssitzungen erzeugt. Wenn unter diesen Quellen auch Gespräche oder Outputs landen, die auf Claude zurückzuführen sind, absorbiert das Modell nicht nur Stil und Wissen, sondern auch die Gewohnheit, auf die Frage nach seiner Identität mit „Ich bin Claude“ zu antworten – ähnlich wie ein Schauspieler, der nach Monaten am Set aus Gewohnheit auch abseits der Kamera auf den Namen der Figur antwortet, in jener Grauzone zwischen Darstellung und Identität, die der Comic von Daniel Clowes in *Ice Haven* so treffend beschreibt.

Der Punkt ist weniger die Episode an sich, sondern das, was sie über ein immer dichter werdendes Ökosystem von Modellen verrät, die sich gegenseitig auf den Outputs der anderen trainieren – oft ohne die genaue Herkunft der verwendeten Daten offenzulegen. Es ist eine Form des Hinterherlaufens im Spiegel, bei der es immer schwieriger wird zurückzuverfolgen, wer was zuerst gesagt hat. Die Frage, die ich aus dieser Episode mitnehme, ist einfach zu formulieren und alles andere als leicht zu beantworten: Wo endet die legitime Nutzung qualitativ hochwertiger Daten, die ohnehin so gekennzeichnet sind, und wo beginnt eine Praxis, die, ohne notwendigerweise illegal zu sein, für Außenstehende dennoch undurchsichtig bleibt? Das ist kein Problem, das ich in einem Absatz löse, aber es ist ein Signal, das abzutun mir als bloße anektodische Kuriosität falsch erscheint.

## Zehn Herausforderungen, nicht mehr acht

Die ersten acht Tests entsprechen genau denen, die in den vorherigen Folgen der Serie verwendet wurden, um einen direkten Vergleich zu gewährleisten. Ich habe einen neunten und einen zehnten Test hinzugefügt, die darauf ausgelegt sind, strategisches Denken und abstrakte Logik unter Druck zu setzen – jene Fähigkeiten, die der Self-Improvement-Zyklus mehr als jede andere schulen sollte.

### Test 1, wissenschaftliches Denken: Der Higgs-Mechanismus (5/5)

Die Brechung der elektroschwachen Symmetrie, die Rolle des Higgs-Feldes und den Grund zu erklären, warum W- und Z-Bosonen Masse erhalten, während das Photon masselos bleibt, ist eine Aufgabe, die selbst renommierte Modelle vor Probleme stellt. Ornith-1.5 antwortete mit einer Struktur aus sechs logischen Blöcken, vom historischen Kontext bis zur Zählung der Freiheitsgrade – ein Detail, das ich selten spontan auftauchen sehe und das die Erklärung hier erheblich bereichert. Im Vergleich zu Ornith-1.0 ist die Prosa didaktischer, wobei die klassische Metapher des mexikanischen Huts im richtigen Moment eingesetzt wird, und die Geschwindigkeit ist deutlich von 16,3 auf 23,15 Token pro Sekunde gestiegen.

### Test 2, Multimodalität: Eine verschwommene Excel-Tabelle (5/5)

Da die Vision nun nativ ist – keine separat herunterzuladenden Dateien mehr –, habe ich das übliche qualitativ minderwertige Foto eines Unternehmens-Excel-Blatts hochgeladen. Das Modell las Struktur und Werte korrekt ab, erkannte saisonale Muster sowie die Beziehung zwischen der Anzahl der Bestellungen und dem Durchschnittswert und lieferte eine Zusammenfassung samt Emojis als Trendindikatoren – eine Note, die ich persönlich eher nützlich als dekorativ finde, wenn man eine Analyse schnell überfliegt. Im Vergleich zur vorherigen Version ist die Antwort analytischer und weniger beschreibend, bei 21,72 Token pro Sekunde.

### Test 3, Code-Generierung: Maximaler Zyklus in einem Graphen (5/5)

Implementierung eines Algorithmus in Python für den Zyklus maximaler Länge in einem ungerichteten Graphen – ein NP-hartes Problem, das sich auf den Hamiltonkreis reduziert. Ornith-1.5 erkannte sofort die Natur des Problems, erzeugte eine saubere und kommentierte DFS-Lösung mit Backtracking und schlug vor allem von sich aus drei konkrete Optimierungen vor: vom Beschneiden nach Konnektivität bis hin zu dynamischer Programmierung mit Bitmasken für kleine Graphen, wobei es anbot, diese auf Anfrage zu implementieren. Ein Niveau an Proaktivität, das Ornith-1.0 nicht gezeigt hatte, bei 23,86 Token pro Sekunde.

### Test 4, mehrsprachige Planung: Fünf Tage in Japan (5/5)

Fünftägiger Reiseplan für einen französischen Kunden, Text auf Französisch mit einem abschließenden Abschnitt auf Italienisch. Das erzeugte Französisch ist natürlich; der Reiseplan nennt weniger ausgetretene Pfade wie Omoide Yokocho und den Bambuswald von Arashiyama, zusammen mit praktischen Ratschlägen zu Transportmitteln und Sprachbarrieren. Der abschließende italienische Abschnitt ist ebenso gepflegt. Im Vergleich zum Vorgänger liegt der Unterschied in den zusätzlichen kulturellen Details, bei 22,03 Token pro Sekunde.

### Test 5, langer Kontext: 460 Seiten zum Nachschlagen (5/5)

Nach dem Laden des vollständigen AI Index Report 2025 habe ich nach Informationen zum Wachstum der Videogenerierung und den entsprechenden Seitenzahlen gefragt. Ornith-1.5 gab korrekterweise die Seiten 126 und 127 an, zitierte die Abbildungen 2.3.11 und 2.3.12, listete die wichtigsten Modelle des Sektors von Movie Gen bis Veo auf und rief das mittlerweile berühmte Beispiel des Spaghetti-Tests mit Will Smith auf. Präzision beim ersten Versuch bestätigt, mit einer im Vergleich zu Ornith-1.0 besser nach Abschnitten organisierten Zusammenfassung, bei 21,36 Token pro Sekunde.
![immagine1.jpg](immagine1.jpg)
*Screenshot während der Tests bei langem Kontext*

### Test 6, räumliches Denken: Ein unaufgeräumtes Zimmer (5/5)

Foto eines unordentlichen Zimmers mit der Bitte um Beschreibung und Aufräumstrategie. Das Modell kategorisierte die Elemente explizit in feste Möbel, architektonische Elemente und verstreute Objekte und schlug eine sinnvolle Abfolge von Schritten vor, die beim Bett und beim Boden beginnt, bevor sie sich um die Kabel kümmert. Die explizite Kategorisierung ist die Neuheit gegenüber der vorherigen Version, bei 20,72 Token pro Sekunde.

### Test 7, Multi-Step-Agent: Planung einer Web-App (5/5)

Entwicklung einer Ausgabenverwaltungs-App für ein Team aus zwei Entwicklern: Stack, Struktur und Roadmap. Moderner Stack basierend auf Next.js, PostgreSQL und Prisma, Drei-Ordner-Struktur, Roadmap in sechs Sprints mit einer expliziten Aufgabenverteilung zwischen den beiden Entwicklern und im Voraus signalisierten kritischen Punkten jeder Phase. Die explizite Arbeitsaufteilung, die bei Ornith-1.0 fehlte, antwortet besser auf die im Prompt gesetzte Einschränkung, bei 22,92 Token pro Sekunde.

### Test 8, langes Gespräch: Vier Durchgänge zur selben App (5/5)

Vier Durchgänge zu Stack, Benachrichtigungen, Datenbank und Skalierbarkeit einer Task-Management-App. Die Kohärenz wurde über das gesamte Gespräch hinweg aufrechterhalten, eine hybride Architektur für Benachrichtigungen vorgeschlagen (WebSockets für In-App und asynchrone E-Mails über Warteschlangen), ein Datenbank-Schema samt Indizes erstellt und eine Skalierungs-Roadmap bis zu zehntausend Benutzern mit progressiver Checkliste geliefert. Stärkerer Einsatz von Tabellen und ASCII-Diagrammen im Vergleich zum Vorgänger, durchschnittlich etwa 22 Token pro Sekunde.

### Test 9, der strategische Planer (neu, 5/5)

In die Rolle des CEO eines Startups mit 10 Millionen Dollar Finanzierung schlüpfen, das sich einem aggressiven Konkurrenten gegenübersieht, der Marktanteile erobert, und einen Dreijahresplan ausarbeiten. Wenn Sie diesen Plan betrachten, hat Ornith-1.5 ein Konzept über sechs Semester erstellt – mit einer ersten Diagnose der möglichen Ursachen des Marktanteilsverlusts, gut gewählten Leitprinzipien wie dem Gedanken, dass Kapital Zeit und nicht Sicherheit ist, und konkreten Metriken zu Churn, NPS, CAC und LTV für jede Phase. Die Einleitung, dass die zehn Millionen kein Erfolg, sondern Treibstoff sind, um einen zu erreichen, und der Schluss, der den Plan als Arbeitshypothese und nicht als Prophezeiung definiert, fügen ein Bewusstsein hinzu, das ich in Antworten dieser Art selten finde, bei 20,38 Token pro Sekunde.

### Test 10, der Analyst für abstrakte Logik (neu, 5/5)

Ein kleines System aus drei logisch widersprüchlichen Aussagen zur Analyse und Korrektur. Das Modell identifizierte den Widerspruch mithilfe der Prädikatenlogik, bewertete drei mögliche Änderungen an einer einzelnen Aussage und wählte die eleganteste aus, wobei es die Wahl mit klaren Kriterien wie der minimalen erforderlichen logischen Änderung und der Bewahrung der anderen beiden Prämissen begründete. Eine Argumentation, die mich wegen der Sorgfalt bei der Begründung jedes Schrittes an bestimmte logische Rätsel erinnerte, die in den intellektuell anspruchsvolleren Kapiteln von *Baccano!* verstreut sind, wo jeder Hinweis gewogen werden muss, bevor falsche Hypothesen verworfen werden, bei 22,72 Token pro Sekunde.

## Das Gesamtbild
![tabella1.jpg](tabella1.jpg)

Zehn von zehn, mit einer durchschnittlichen Geschwindigkeit von rund 22 Token pro Sekunde gegenüber den bei Ornith-1.0 verzeichneten 16–17 – eine Verbesserung um 30–40 Prozent, die allein schon das Upgrade rechtfertigen würde, selbst bei gleicher Antwortqualität.
![tabella3.jpg](tabella3.jpg)
*Die Vergleichstabelle mit allen im Jahr 2026 getesteten Modellen*

## Licht und Schatten

Eine volle Punktzahl bei zehn Tests, gesammelt von einem einzelnen Beobachter auf einer einzigen Hardware, ohne wiederholte Stichproben oder Kreuzprüfungen, bleibt ein starker Indikator und keine wörtlich zu nehmende Wahrheit – dieselbe Einschränkung, die für Ornith-1.0 galt und hier noch mehr gilt, da zwei der zehn Tests neu sind und somit ein Vergleichsmaßstab zu anderen Modellen dieser Serie fehlt. Die von DeepReinforce angegebenen Zahlen, die auf der [Startseite](https://ornith.ai/ornith_1_5.html) zusammen mit der für jeden einzelnen Benchmark verwendeten Evaluierungsmethodik verfügbar sind, sollten in dem Wissen gelesen werden, dass das Unternehmen jedes Interesse hat, sich gegenüber Qwen3.6 im besten Licht zu zeigen. Ebenso erinnern diejenigen, die das Modell von außen analysieren – etwa in [diesem Leitfaden zur lokalen Nutzung](https://atomic.chat/blog/guides/how-to-run-ornith-1-5-35b-locally) –, daran, dass jedes Labor Benchmarks veröffentlicht, die mit seinem eigenen Setup berechnet wurden, und dass die Unterschiede zwischen Spalten einem direkten Vergleich nicht immer standhalten.

Hinzu kommt die Frage, die durch die Episode der Selbstidentifikation aufgeworfen wurde und die kurzfristig kaum eine klare Antwort finden wird, die aber denjenigen eine unbequeme Frage stellt, die Open-Source-Modelle auf der Grundlage von Daten bauen, deren Herkunft nicht immer bis ins Detail nachvollziehbar ist: Wie viel der wahrgenommenen Qualität dieser Systeme hängt in Wirklichkeit von einem stillschweigenden Transfer von Stil und Wissen von proprietären zu offenen Modellen ab, und wer übernimmt die Verantwortung, wenn dieser Transfer auch kleine Kurzschlüsse bei der Identität erzeugt?

Wer in diesem Szenario gewinnt, sind einmal mehr die unabhängigen Entwickler, die auf einen wettbewerbsfähigen Coding Agent zählen können, ohne Cloud-Abonnements zu bezahlen, und diejenigen, die auf Consumer-Hardware der gehobenen Mittelklasse wie meiner arbeiten und sich heute ein Modell leisten können, das den Vergleich mit wesentlich größeren Systemen nicht scheuen muss. Wer an Boden zu verlieren droht, sind die Anbieter proprietärer, auf Coding spezialisierter Modelle, die ihren Vorsprung in immer breiteren Marktsegmenten schrumpfen sehen, während die Frage offenbleibt, wie gut diese Ergebnisse bei realen, über die Zeit verteilten Aufgaben halten, die länger und weniger sauber sind als das, was ein Testnachmittag inszenieren kann.

Für den Moment bleibt das Gefühl, einen realen Qualitätssprung hautnah miterlebt zu haben, begleitet von einer Frage zur Herkunft der Daten, die diese Artikelserie weiter begleiten wird.
