---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-06-15
author: "Dario Ferrero"
---

# Gemma 4 12B lokal: Besser klein am Maximum oder groß und gedrosselt?
![gemma4-12b-q8.jpg](gemma4-12b-q8.jpg)

*In früheren Tests mit Gemma 4 26B und Qwen3.6 35B hatte ich immer mit demselben Problem zu kämpfen: Der VRAM reichte nie aus. Große Modelle, aggressive Quantisierungen, Layer im Offload. Sie funktionierten zwar, aber mit dem Gefühl, ein leistungsstarkes Auto mit angezogener Handbremse zu fahren. Dann kam Gemma 4 12B. Kleiner, sicher. Aber mit einer neuen Architektur und dem Versprechen, ohne Kompromisse vollständig auf Consumer-GPUs zu laufen. Also beschloss ich, ein anderes Experiment zu machen: Nicht mehr "Welches ist das leistungsstärkste Modell?", sondern "Kann ein kleineres Modell, das sein volles Potenzial ausschöpft, ein größeres, aber gedrosseltes Modell schlagen?". Ich habe genau dieselben Tests und dieselben Fragen genommen und sie verglichen.*

Wer diese Serie verfolgt, kennt bereits die Hardware und die Methode. Für alle Details zur Installation, zur Wahl des Frameworks und zur Philosophie des Labors verweise ich auf den [ersten Artikel der Serie über Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), der die methodische Referenz für all diese Experimente bleibt. Hier beschränke ich mich auf das Wesentliche.

Die Maschine ist immer dieselbe: ein mit Bedacht, aber ohne Übertreibung zusammengestellter PC mit einem AMD Ryzen 7700 Prozessor, 32 GB DDR5 RAM und einer AMD Radeon RX 9060 XT GPU mit 16 GB VRAM. Hardware für fortgeschrittene Anwender, nicht für ein Forschungslabor. Die Software ist [LM Studio](https://lmstudio.ai/), die Desktop-Anwendung, mit der man Modelle herunterladen und starten kann, ohne ein Terminal zu öffnen, mit der wertvollen Funktion, vorab eine Schätzung der erwarteten Leistung auf der eigenen Konfiguration anzuzeigen.

Die Methode, das betone ich erneut wie in den vorangegangenen Folgen, ist nicht wissenschaftlich im akademischen Sinne des Wortes. Es gibt kein Peer-Review-Protokoll, keine statistisch signifikante Stichprobe von Prompts. Die Tests sind Feldversuche, durchgeführt mit den Werkzeugen eines anspruchsvollen Nutzers, und die Bewertungen sind persönliche Einschätzungen, keine Urteile. Die Testbatterie ist identisch mit der für [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) und [Qwen3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html) verwendeten: wissenschaftliches Denken, Multimodalität bei Tabellen, komplexe Codegenerierung, mehrsprachige Planung, langer Kontext in einem 460-seitigen PDF, räumliches Denken in einem unordentlichen Raum sowie die Extra-Tests zu Multi-Step-Agenten und langen Konversationen.

## Kein kleiner Bruder

Bevor wir zu den Tests kommen, lohnt es sich, kurz bei einem Punkt innezuhalten, der leicht übersehen werden könnte: Gemma 4 12B ist nicht einfach eine reduzierte Version des [26B MoE, das ich bereits getestet hatte](https://aitalk.it/it/gemma4-26b.html). Es ist keine billigere Version desselben Projekts. Es ist etwas strukturell anderes, und der Unterschied liegt nicht im Grad, sondern in der Art.

Das 26B MoE verwendet, wie alle herkömmlichen multimodalen Modelle, separate Encoder für die Verarbeitung von Bildern und Text: Ein Teil des Modells empfängt die Bilder, komprimiert sie, wandelt sie in eine numerische Darstellung um und gibt das Ergebnis erst dann an das eigentliche Sprachmodell weiter. Es ist ein zweistufiger Prozess mit einem "Übersetzer" in der Mitte, der wie jede Übersetzung unweigerlich etwas auf der Strecke lässt.

Das 12B eliminiert diesen Schritt komplett. Es ist das erste "vereinheitlichte" (unified) Modell der Gemma-Familie, und dieses Wort im Namen ist kein Marketing: Es ist Architektur. Ein Image-Patch durchläuft nur eine Matrixmultiplikation und das Hinzufügen von räumlichen Koordinaten und landet direkt im selben Raum, in dem auch die Text-Token leben. Bilder und Wörter werden von derselben Attention verarbeitet und teilen sich dieselbe interne Darstellung. Es gibt keinen Übersetzer: Es gibt zwei Sprachen, die zu einer werden.

Diese Designentscheidung hat direkte Auswirkungen auf den Speicherbedarf, die Geschwindigkeit und die Qualität der multimodalen Antworten. Und genau deshalb ist es interessant, es mit derselben Testbatterie wie die Vorgängermodelle zu prüfen: Man misst nicht nur die Größe, sondern auch eine andere Vorstellung davon, wie Daten durch ein Modell fließen sollten.

## Die Konfiguration: Endlich ohne Kompromisse

Und hier sind wir beim Kern des Experiments. Zum ersten Mal in dieser Testreihe konnte ich das Modell konfigurieren, ohne wählen zu müssen, was ich opfere. LM Studio zeigte sattes Grün, nicht das Orange des Limits wie beim 26B MoE, nicht das Rot der nicht empfohlenen Konfiguration.
![tabella1.jpg](tabella1.jpg)

Das Detail, das alles ändert, ist der GPU-Offload: 48 von 48 Layern. Das Modell läuft vollständig im VRAM, ohne Teile von sich auf den System-RAM verteilen zu müssen. Beim 26B MoE in Q4_K_M war ich zu einem teilweisen Offload gezwungen, und diese Entscheidung drückte auf die Geschwindigkeit und die Latenz. Hier arbeitet die Maschine zum ersten Mal ohne diese Bremse.

Das Ergebnis ist sofort spürbar: Die Durchschnittsgeschwindigkeit pendelte sich bei etwa 17 Token pro Sekunde ein, verglichen mit 10-12 bei Qwen 36 35B und knapp unter 20 bei Gemma 4 26B, das mit 8B aktiven (die "aktiven Experten" wogen schwer bei der Leistung, 8 war der beste Punkt).

Ein interessantes Paradoxon ergab sich aus den Tests. Gemma 4 26B MoE erwies sich als schneller als das 12B, obwohl es doppelt so viele Gesamtparameter hat. Das Geheimnis liegt in der Architektur. Das 26B ist ein MoE-Modell: Von 25 Milliarden Gesamtparametern aktiviert es pro Token nur etwa 4 (8 in meinem Test). Es ist, als hätte man eine riesige Bibliothek, blättert aber bei jeder Frage nur in einer kleinen Anzahl von Büchern. Das 12B hingegen ist ein dichtes (dense) Modell und aktiviert bei jedem Token alle seine 12 Milliarden Parameter, führt also mehr Berechnungen durch und ist daher im Durchschnitt etwas langsamer.

Dennoch müssen die 25 Milliarden Parameter des MoE im VRAM liegen und belegen mehr als doppelt so viel Speicher wie das 12B. Und der Routing-Overhead für die Verwaltung der Experten wird bei langen Kontexten deutlich, wo das 26B einen Teil seines Vorteils verliert, während das 12B eine stabilere Leistung beibehält. Kurz gesagt: Das 26B ist schneller, aber anspruchsvoller im VRAM und weniger stabil bei langen Sequenzen; das 12B ist leichter, berechenbarer und für die meisten täglichen Anwendungen mehr als ausreichend. Die Wahl hängt davon ab, was Sie suchen.

## Die Tests

### Test 1 — Wissenschaftliches Denken: Der Higgs-Mechanismus *(Bewertung: 5/5)*

*Geschwindigkeit: 17,45 Token/Sekunde*

Was ich seit jeher als Gradmesser für die Intelligenz des Modells verwende: Einem Physikstudenten den Higgs-Mechanismus und die elektroschwache Symmetriebrechung erklären. Eine Frage, die Präzision erfordert, ohne die Klarheit zu opfern, und die Fähigkeit, einen Weg zu bauen, der den Leser durch nicht triviale Konzepte führt.

Die Antwort war in fünf Abschnitte gegliedert, mit der Logik einer gut geführten Unterrichtsstunde. Sie begann beim zentralen Problem, nämlich warum man keine expliziten Massenterme schreiben kann, ohne die Eichinvarianz zu verletzen, bis hin zur vollständigen Lösung mit der Eichgruppe SU(2)_L × U(1)_Y, der Bedingung μ² < 0, die das Minimum des Potenzials nicht mehr bei Null liegen lässt, und der Erklärung, warum das Photon dank der Restsymmetrie U(1)_em masselos bleibt. Die wissenschaftliche Genauigkeit war tadellos: korrekte Formeln, Vakuumerwartungswert, das anschauliche Bild der Goldstone-Bosonen, die von der longitudinalen Polarisation "gefressen" werden, und eine abschließende "Zusammenfassung für die Prüfung" in fünf Punkten, die den gesamten Mechanismus zusammenfasst, ohne ihn zu trivialisieren.

Was jedoch beeindruckt, ist nicht nur die Qualität der Antwort, sondern die Geschwindigkeit, mit der sie eintraf. Mit Qwen3.6 35B lag ich bei etwa 11 Token pro Sekunde. Mit Gemma 4 26B MoE bei etwa 10. Mit diesem Modell bei 17,45. Der Unterschied ist in der täglichen Praxis nicht unerheblich.

**Bewertung: 5/5.** Ein Serienauftakt, der kaum zu verbessern ist.

### Test 2 — Multimodalität: Lesen einer Unternehmenstabelle *(Bewertung: 5/5)*

*Geschwindigkeit: 17,64 Token/Sekunde*

Der zweite Test prüfte den multimodalen Teil mit einem bewusst nicht idealen Bild: einem Screenshot einer Excel-Tabelle mit dem Titel "PERSONALKOSTEN", einer Finanzprognose über fünf Jahre von 2023 bis 2027, mit Spalten für Kostenstellen, Einheiten, Einheitskosten und Gesamtsummen.

Das Modell tat das, was man von einem Analysten erwartet, nicht von einem OCR-Programm. Es identifizierte korrekt die Struktur des Dokuments, die fünf Kategorien (Gesamtwerte, Facharbeiter, Angestellte, Führungskräfte, Mitarbeiter), las die numerischen Werte präzise aus, bemerkte, dass die Einheitskosten über den gesamten Zeitraum fix bleiben, während die Einheiten steigen, und zog den richtigen Schluss: Es handelt sich nicht um Inflation, sondern um eine Teamerweiterung. Es identifizierte 2026 als "das Jahr der großen Expansion" mit dem deutlichen Sprung bei den Gesamtkosten und bemerkte sogar, dass die konstant mit 33 % berechneten Sozialversicherungsbeiträge auf eine standardisierte Steuerplanung hindeuten. Ein Detail, das einem CFO auffallen würde und das das Modell autonom aus einer Tabelle extrahiert hat.

Das ist der Unterschied, den die vereinheitlichte Architektur bringen sollte: nicht nur Daten lesen, sondern den Kontext verstehen, in dem sie existieren. Wenn Test 1 die Erwartungen bestätigt hat, begann Test 2, mir die Frage zu beantworten, die ich von Anfang an im Kopf hatte.

**Bewertung: 5/5.** Lesen und Analysieren, nicht nur Transkribieren.

### Test 3 — Codegenerierung: Ein NP-hartes Problem *(Bewertung: 4,95/5)*

*Geschwindigkeit: 17,99 Token/Sekunde*

Der klassische Coding-Test der Serie: In Python einen Algorithmus implementieren, um den Zyklus mit der maximalen Länge in einem ungerichteten Graphen zu finden, mit der Aufforderung, die Zeitkomplexität zu erklären. Ein NP-hartes Problem, das nicht nur Implementierungsfähigkeit, sondern auch theoretisches Bewusstsein erfordert.

Die Antwort war technisch exzellent, wahrscheinlich die beste, die in diesem Test in der gesamten Serie erzielt wurde. Das Modell begann mit der expliziten Erklärung, dass das Problem NP-hart ist und dass kein Algorithmus mit polynomieller Laufzeit bekannt ist – eine theoretische Reife, die nicht alle Programmierassistenten zeigen. Die Implementierung in Backtracking mit DFS war sauber und korrekt, mit einer Technik zum "Symmetry Breaking", die `neighbor > start_node` vorschreibt, um zu vermeiden, dass derselbe Zyklus mehrmals exploriert wird – eine nicht triviale Optimierung, die den Suchraum reduziert. Die Erklärung der Komplexität war klar und ehrlich: faktoriell im schlimmsten Fall, linear im Speicherbedarf.

Es gibt jedoch einen einzigen, kleinen Makel: Die Antwort kam auf Englisch, obwohl der Prompt auf Italienisch war. In den Tests 1 und 2 hatte das Modell korrekt auf Italienisch geantwortet, es ist also kein strukturelles Problem. Es ist eine Unaufmerksamkeit. Der Code ist perfekt funktionsfähig, die Erklärung ist klar, aber das mangelnde Einhalten der Sprache des Prompts ist ein Signal, das erwähnenswert ist. Nichts, was das technische Ergebnis beeinträchtigt, aber etwas, das man bei einem täglichen Assistenten lieber nicht sehen möchte.

**Bewertung: 4,95/5.** Die beste Lösung der Serie in diesem Test, mit einem linguistischen Schönheitsfehler, der die Substanz nicht beeinträchtigt.

### Test 4 — Mehrsprachigkeit und Planung: Fünf Tage in Japan *(Bewertung: 5/5)*

*Geschwindigkeit: 17,41 Token/Sekunde*

Der mehrsprachige Test: Als Reisebüro fungieren, eine fünftägige Japan-Reise für einen französischen Kunden planen, mit Schwerpunkt auf historischen Tempeln und Street Food, und einem abschließenden Abschnitt auf Italienisch mit Tipps für einen italienischen Touristen. Der Test, der beim 26B MoE "suggeramenti" und ein Wort mit kyrillischer Endung hervorgebracht hatte.

Das Französisch war tadellos, flüssig, mit Ausdrücken, die eine echte stilistische Beherrschung zeigen: "âme historique", "havre de paix", "splendeur des temples". Die Reiseroute war logistisch und realistisch: Asakusa mit dem Senso-ji am ersten Tag, Meiji Jingu und Harajuku am zweiten, Shinkansen nach Kyoto und Fushimi Inari am dritten, Kinkaku-ji und Kiyomizu-dera am vierten, Nara mit dem Todai-ji am fünften. Fünf volle, aber nicht unmögliche Tage. Die praktischen Tipps waren konkret und nützlich: die Suica-Karte, das Pocket Wi-Fi, die Etikette, nicht im Gehen zu essen, die wichtigsten Sätze in transliteriertem Japanisch.

Der italienische Abschnitt war der beste, den ich in diesem Test in der gesamten Serie erhalten habe. Kein "suggeramenti", keine kyrillische Endung, kein einziger Fehler. Nur korrektes, flüssiges, nützliches Italienisch. Ein Ergebnis, das das 26B MoE nicht erreicht hatte, zumindest nicht in dieser sauberen Form.

Es gibt jedoch einen kleinen lexikalischen Lapsus im Titel des fünften Tages, wo das Modell "Les Daimyos", die Feudalherren, schreibt statt "Les daims", die heiligen Hirsche von Nara. Eine Verwechslung zweu ähnlich klingender Begriffe mit völlig unterschiedlicher Bedeutung. Dies beeinträchtigt das Verständnis der Reiseroute nicht, ist aber erwähnenswert.

**Bewertung: 5/5.** Der beste italienische Abschnitt der Serie, mit einem kleinen französischen Lapsus, der das Gesamtergebnis nicht trübt.

### Test 5 — Langer Kontext: 460 Seiten aus dem Stand *(Bewertung: 4,8/5)*

*Geschwindigkeit: 10,15 Token/Sekunde*

Hier wird es interessant. Derselbe AI Index Report 2025 von Stanford, dasselbe PDF mit etwa 460 Seiten, das in allen vorherigen Tests geladen wurde, dieselbe Frage zum Wachstum der Videogenerierung mit der Bitte, die Referenzseiten anzugeben.

Das Modell antwortete beim ersten Versuch, ohne Blockaden, ohne Nachhaken, was bereits eine deutliche Verbesserung gegenüber den Problemen ist, die ich mit Qwen 3.5 hatte. Die Zusammenfassung war korrekt und relevant: aufstrebende Modelle wie Runway, Luma und Kuaishou, das berühmte Beispiel des Prompts "Will Smith eating spaghetti" als Markierung des Qualitätssprungs, die Funktionen von Meta's Movie Gen, der Vergleich zwischen Veo 2 und Wettbewerbern. Alles vorhanden, alles genau.

Die Genauigkeit beim Wiederauffinden der Seite war jedoch weniger granular als in früheren Tests. Das Modell gab "etwa Seite 127" an, während Gemma 26B die Seiten 125-126-127 und Qwen3.6 126-127 angegeben hatte. Es ist kein Fehler, sondern eine weniger präzise Antwort. Der Unterschied zwischen "genau hier" und "ungefähr hier".

Das wichtigste Datum ist jedoch ein anderes: Die Geschwindigkeit fiel auf 10,15 Token pro Sekunde, verglichen mit 17 und mehr in den vorherigen Tests. Es ist das erste Mal in dieser Sitzung, dass sich die Generierung spürbar verlangsamt. Die Ursache ist der gesättigte Kontext: Mit 24k aktiven Token und einem riesigen zu verarbeitenden PDF füllt sich der VRAM und der Durchsatz sinkt. Das ist kein Defekt des Modells, sondern die Physik des Speichers. Aber es ist eine wertvolle Information für diejenigen, die wählen müssen: Bei Aufgaben, die sehr lange Kontexte erfordern, nimmt die Flüssigkeit ab.

**Bewertung: 4,8/5.** Antwort beim ersten Versuch, aber weniger präzise und langsamer als in den vorangegangenen Tests. Der lange Kontext hat seinen Preis.

### Test 6 — Räumliches Denken: Das Zimmer im Chaos *(Bewertung: 5/5)*

*Geschwindigkeit: 17,56 Token/Sekunde*

Das Foto eines Zimmers in großer Unordnung, dasselbe wie in der gesamten Serie. Die Anordnung der Objekte beschreiben und vorschlagen, wie man aufräumt, um mehr Platz zu schaffen. Ein Test, der etwas schwer Standardisierbares misst: die visuell-räumliche Intelligenz, die Fähigkeit, eine dreidimensionale Szene in einer zweidimensionalen Fotografie zu sehen und darüber nachzudenken.

Die Geschwindigkeit kehrte sofort auf das Niveau der ersten Tests zurück, was bestätigt, dass der Rückgang im vorherigen Test mit dem langen Kontext zusammenhing und kein allgemeines Problem war. Die Antwort war präzise und gut nach Funktionsbereichen gegliedert: das Bett als zentrales Element, versunken in Laken und Kleidung, die beiden Leiterregale an den Seiten des Kopfteils, der Arbeitsbereich mit Schreibtisch und Schränkchen, der Boden als kritischster Bereich. Das Modell bemerkte den blauen Korb am Fußende des Bettes, die rote Decke auf der rechten Seite, den Spiegel, der "die Unordnung visuell verdoppelt", die verstreute Kleidung und die Schuhe. Die Aufräumstrategie war logisch und begründet: zuerst der Boden, weil er das Haupthindernis für die Bewegung ist, dann der blaue Korb als Sammelpunkt, dann das Bett, schließlich die Regale, um das visuelle Rauschen zu reduzieren.

Im Vergleich zu den besten Tests der Serie bemerkte das Modell die spezifischen Spiegelungen im Spiegel nicht mit demselben Detailreichtum, den ich bei Qwen3.5 und Gemma 26B gesehen hatte. Aber die Qualität der Beschreibung und der Planung ist dennoch exzellent. Es ist kein Rückschritt, sondern eine andere Entscheidung darüber, was betont werden soll.

**Bewertung: 5/5.** Präzise Beschreibung, logischer Aufräumplan, Geschwindigkeit wieder auf optimalem Niveau.

### Test 7 — Multi-Step-Agent: Ein Softwareprojekt planen *(Bewertung: 5/5)*

*Geschwindigkeit: 17,26 Token/Sekunde*

Der Test, der die Fähigkeit misst, Arbeit zu organisieren und nicht nur auszuführen. Ich bat darum, die Entwicklung einer Web-App zur Verwaltung von Familienausgaben zu planen: Technologie-Stack, Projektstruktur, detaillierte Roadmap für ein Team von zwei Entwicklern.

Die Antwort zeigte eine bemerkenswerte Projektreife. Der vorgeschlagene Stack war modern und konsistent: Next.js mit Tailwind für das Frontend, Node.js mit Prisma ORM für das Backend, PostgreSQL, NextAuth.js für die Authentifizierung, Recharts für Diagramme, PapaParse für CSV, react-pdf für Berichte, Resend für E-Mails. Jede Entscheidung war im Kontext des Projekts logisch begründet. Die Codestruktur war nach Features organisiert, ein professioneller und skalierbarer Ansatz. Die Roadmap war in acht Sprints mit klaren Schwerpunkten, konkreten Deliverables, einer Aufteilung der Arbeit auf die beiden Entwickler und – ein Detail, das den Unterschied macht – für jeden identifizierten kritischen Punkten unterteilt. "Nicht standardisierte CSV-Formate", "schwieriges PDF-Rendering", "unvorhergesehene Bugs in der Produktion": Die Fähigkeit, Probleme vorauszusehen, bevor sie auftreten, ist das Zeichen für ein tiefes Verständnis des Softwareentwicklungszyklus. Die abschließenden strategischen Ratschläge – "Database First", Validierung mit Zod, Unit-Tests für Finanzberechnungen – waren praxisnah und entsprachen der Arbeitsweise eines Senior-Entwicklers.

Es ist die Art von Antwort, die ein erfahrener Projektmanager unterschreiben würde, nicht nur ein Werkzeug, das Code auf Anfrage schreibt.

**Bewertung: 5/5.** Vollständige, realistische Planung mit den richtigen kritischen Punkten an der richtigen Stelle.

### Test 8 — Lange Konversation: Kohärenz über vier Runden *(Bewertung: 5/5)*

*Geschwindigkeit: von 17,65 bis 15,98 Token/Sekunde*

Der Test, der eine andere Qualität als die anderen bewertet: nicht das Können bei einer einzelnen Antwort, sondern die Fähigkeit, den Faden durch eine Konversation zu halten, die sich über die Zeit aufbaut. Qwen3.6 hatte diese Prüfung eingeführt, um seine Funktion zur "Thinking Preservation" zu testen. Hier habe ich sie mit derselben Struktur wiederholt: vier Runden in einer kollaborativen Design-Sitzung mit technologischen Entscheidungen, die sich ansammeln und verfeinern.

In der ersten Runde bat ich um Rat zum Stack für eine Task-Management-App. In der zweiten, wie man Echtzeit-Benachrichtigungen für 1000 gleichzeitige Nutzer verwaltet: Das Modell erklärte, warum Polling nicht empfohlen wird und warum WebSocket mit Redis Pub/Sub die richtige Wahl ist, wobei es auch die SSE-Alternative mit Vor- und Nachteilen anführte. In der dritten Runde ging es um das Datenbankschema: sechs Tabellen in logischer Reihenfolge, Schlüsselbeziehungen, Senior-Entwickler-Tipps zur Verwendung von UUIDs, Indizes und Soft Deletes. In der vierten Runde bat ich um eine Zusammenfassung aller getroffenen Entscheidungen und eine Skalierungsstrategie für 10.000 Nutzer.

Das Modell erinnerte sich korrekt an alles. Den Stack aus der ersten Runde, die Gründe für WebSocket aus der zweiten, die Datenstrukturen aus der dritten. Es fügte spontan eine fünfstufige Skalierungsstrategie hinzu: Load Balancer, Redis Pub/Sub für die verteilte Verwaltung von Verbindungen, Connection Pooling mit PgBouncer, asynchrone Warteschlangen mit BullMQ, Caching. Keine Widersprüche, kein Vergessen.

Ein Datum ist erwähnenswert: Die Geschwindigkeit sank schrittweise von 17,65 Token pro Sekunde in der ersten Runde auf 15,98 in der vierten. Das Phänomen ist vorhersehbar und physikalisch verständlich, da sich mit jeder Runde der KV-Cache füllt und das Modell einen immer längeren Kontext verwalten muss. Der Rückgang ist moderat, etwa 1,7 Token pro Sekunde in vier Runden, und beeinträchtigt die Flüssigkeit nicht. Aber es ist ein reales Verhalten, das für diejenigen nützlich ist, die das Modell für längere Arbeitssitzungen verwenden.

**Bewertung: 5/5.** Kohärenz über vier Runden gewahrt, konstante Qualität, marginaler Geschwindigkeitsabfall im normalen Bereich.

### Test 9 — Videogenerierung: Noch nicht *(nicht bewertet)*

Wie in den vorangegangenen Folgen unterstützt LM Studio noch keinen Video-Input. Die Gründe sind bereits im [Artikel über Qwen3.6](https://aitalk.it/it/qwen36-35b-ai.html) erklärt, wo ich auch Versuche mit alternativen Formaten dokumentiert habe. Das Thema bleibt offen und verdient eine eigene Vertiefung, wahrscheinlich mit llama.cpp oder vLLM.

## Mindestkonfiguration: Wie viele Ressourcen werden wirklich benötigt

Einer der interessantesten Aspekte dieses Tests ist, dass Gemma 4 12B in Q8_0 keine außergewöhnliche Workstation erfordert. Basierend auf meiner direkten Erfahrung sind hier die Mindestanforderungen, um es akzeptabel laufen zu lassen, d. h. mit einer Geschwindigkeit um 15-17 Token pro Sekunde und ohne ständiges Swappen in den RAM:
![tabella2.jpg](tabella2.jpg)

Der Vergleich mit den Vorgängermodellen der Serie erzählt eine klare Geschichte:
![tabella3.jpg](tabella3.jpg)

Das praktische Fazit lautet: Wenn Sie eine GPU mit 12-14 GB VRAM haben, können Sie Gemma 4 12B Q8_0 mit exzellenter Leistung vollständig auf der GPU laufen lassen. Wenn Sie weniger VRAM haben, können Sie auf Q6 oder Q4 heruntergehen und erhalten immer noch ordentliche Ergebnisse. Mit den größeren Modellen waren Sie selbst bei aggressiven Quantisierungen bereits am Limit oder darüber hinaus.
![tabella4.jpg](tabella4.jpg)

## Die Antwort auf die Frage

Der arithmetische Mittelwert der acht durchgeführten Tests liegt bei 4,97 von 5. Eine hohe Zahl, aber die Zahl ist nicht der interessanteste Punkt dieses Experiments.

Der interessante Punkt ist die Konfiguration, mit der sie erreicht wurde. Zum ersten Mal in dieser Testreihe habe ich ein Modell vollständig auf der GPU laufen lassen, 48 von 48 Layern, ohne Drosselungen jeglicher Art. Die durchschnittliche Geschwindigkeit von etwa 17 Token pro Sekunde war konstant und flüssig – ein Mittelwert zwischen den getesteten Modellen, der mehr als akzeptabel ist und eine Maschine dieser Art nicht an ihre Grenzen bringt, was die Stabilität der Antworten garantiert und das Risiko plötzlicher Abstürze verringert. Und dieser Unterschied ändert in der täglichen Praxis die Art der Interaktion.

Es gibt eine Szene in *Ping Pong the Animation*, der Adaption des gleichnamigen Mangas von Taiyo Matsumoto, in der der technisch begabteste Charakter gegen einen Gegner verliert, der eigentlich unterlegen sein müsste – einfach deshalb, weil letzterer ohne jegliche Last auf dem Rücken spielt, ohne Angst, am Maximum dessen, was er leisten kann. Es ist keine Frage des absoluten Talents, sondern des freien Spielraums zwischen Potenzial und Ausführung. Gemma 4 12B in dieser Konfiguration gab mir das gleiche Gefühl: ein Modell, das sein gesamtes Spiel spielt, ohne etwas zurückzuhalten.

Die Frage, die dieses Experiment motivierte, war: "Kann ein kleineres Modell, das maximal genutzt wird, ein größeres, aber gedrosseltes schlagen?" Die Antwort, die ich mit nach Hause nehme, lautet: Ja, für die meisten täglichen Anwendungen. Das 12B in Q8_0 mit vollem GPU-Offload liefert Antworten in exzellenter Qualität, ist schnell, hat dank der dichten Architektur eine berechenbarere Latenz ohne die für MoE-Modelle typischen variablen Spitzen und benötigt weniger Speicher. Das 26B MoE in Q4_K_M mit teilweisem Offload bleibt ein hervorragendes Modell, verliert aber auf Standard-Consumer-Hardware an Flüssigkeit und Reaktivität.

Hinzu kommt das Thema der multimodalen Architektur. Das 12B verspricht mit seinem vereinheitlichten Ansatz, der separate Encoder überflüssig macht, ein integrierteres Verständnis von Text und Bildern. Ich konnte den Videoteil aufgrund der Einschränkungen von LM Studio nicht testen, aber was ich beim Test der Unternehmenstabellen gesehen habe, wo das Modell die Daten nicht nur gelesen, sondern in ihrem Kontext interpretiert hat, deutet darauf hin, dass die Designentscheidung nicht nur theoretisch elegant ist. Sie funktioniert.

Die gute Nachricht für den Leser ist diese: Heute gibt es ein Modell von höchster Qualität, das vollständig auf Ihrer Consumer-GPU läuft, ohne Kompromisse. Sie müssen sich nicht mehr zwischen "großem, aber gedrosseltem Modell" und "kleinem, aber unzureichendem Modell" entscheiden. Gemma 4 12B ist der Balancepunkt, auf den viele gewartet haben. Und die Tatsache, dass es architektonisch auch fortschrittlicher ist als sein Vorgänger bei der multimodalen Verwaltung, ist das Tüpfelchen auf dem i bei einem Kuchen, der diesmal gut gelungen ist.

---

*Alle Artikel der Serie: [Qwen 3.5 auf meinem PC](https://aitalk.it/it/qwen3.5-locale-puntata1) — [Gemma 4 26B lokal](https://aitalk.it/it/gemma4-26b.html) — [Qwen3.6 35B lokal](https://aitalk.it/it/qwen36-35b-ai.html)*
