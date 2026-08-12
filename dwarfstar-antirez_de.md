---
tags: ["Research", "Training", "Applications"]
date: 2026-08-03
author: "Dario Ferrero"
---

# DwarfStar: Der Zwergstern, der die lokale Frontier-KI beleuchtet
![dwarfstar-antirez.jpg](dwarfstar-antirez.jpg)

*In William Gibsons Roman *Neuromancer* gibt es eine Szene, in der sich der Protagonist direkt mit einer immensen Intelligenz verbindet, die auf unzugänglichen Servern verteilt ist, über eine Verbindung, die er weder kontrolliert noch besitzt. Das war 1984 Science-Fiction. Im Jahr 2026 ist es mehr oder weniger die tägliche Realität für jeden, der ChatGPT, Claude oder Gemini nutzt: gigantische Modelle, die auf Milliarden-Dollar-Infrastrukturen gehostet werden, erreichbar nur über eine Internetverbindung und gegen ein monatliches Abonnement oder Kosten pro Token. Dein Gespräch, deine Daten, dein Denken: Alles fließt irgendwohin, was du nicht siehst und nicht verwaltest.*

DwarfStar ist im Kern ein Versuch, diese Gleichung umzukehren. Keine kommerzielle Alternative, kein Wrapper um etwas anderes: Eine Inferenz-Engine, von Grund auf in C geschrieben, manisch optimiert für ein einzelnes Modell, kostenlos unter der MIT-Lizenz verteilt. Und dahinter steht ein Name, den die Tech-Community sofort erkennt: Salvatore Sanfilippo, alias *antirez*, der sizilianische Programmierer, der 2009 Redis erfand.

## Antirez: Der Programmierer, der eine Sache macht, und zwar richtig

Salvatore Sanfilippo wurde am 7. März 1977 in Campobello di Licata, Sizilien, geboren. Schon in sehr jungem Alter entwickelte er ein Interesse am Programmieren und begann im Alter von fünf Jahren, Code auf einem Texas Instruments-Computer zu schreiben, den ihm sein Vater geschenkt hatte. Von da an ist es eine Geschichte fruchtbarer Umwege: Er verlässt die Architektur für die Informatik, landet in den neunziger Jahren in der Netzwerksicherheit, erfindet den *Idle Scan* – eine heimliche Technik zum Scannen von Netzwerkports, die noch heute in nmap implementiert ist – und baut dann, fast durch Zufall, Redis.

Redis ist ein Open-Source-In-Memory-Datenspeicher, der von Sanfilippo entwickelt und am 26. Februar 2009 erstmals veröffentlicht wurde. Anstatt nur ein Key-Value-Cache zu sein, bietet es reichhaltige native Datenstrukturen (Strings, Hashes, Listen, sortierte Mengen, Streams), die vom Server atomar verarbeitet werden. Die Philosophie dahinter ist diejenige, die antirez in jedes Projekt einbringt: Weniger machen. Ein kleines und einfaches System, das man im Kopf behalten kann, schlägt ein großes und komplexes System.

Redis wird heute von praktisch allen Internetunternehmen genutzt, von Airbnb bis Uber, von Snapchat bis Meta, bis hin zu Amazon und Twitch. Trotzdem hat Sanfilippo sich immer dafür entschieden, in Catania zu leben, fernab der Hektik des Silicon Valley, und der Familie sowie intellektuellen Impulsen Priorität einzuräumen. Im Juni 2020 kündigte er seinen Rückzug aus der Wartung von Redis an, um sich anderen Projekten zu widmen, kehrte dann aber im Dezember 2024 in der Rolle des Redis-Evangelisten zurück und entwickelte den neuen Datentyp Vector Set.

Der Respekt, den die Tech-Community ihm entgegenbringt, rührt nicht nur von der technischen Größe von Redis her. Er rührt von etwas Seltenerem her: Beständigkeit. Antirez jagt keinen Trends hinterher, häuft keine Startups an, monetarisiert seinen Ruf nicht. Er schreibt Software, weil er gerne Software schreibt, und wenn ihn etwas fasziniert, baut er es mit fast handwerklicher Sorgfalt. DwarfStar ist genau das.

## Das Problem: Frontier-Modelle leben auf dem Saturn

Um zu verstehen, was DwarfStar zu einem außergewöhnlichen Projekt macht, muss man zunächst das Problem verstehen, das es anspricht. Die fähigsten Sprachmodelle, DeepSeek V4 Flash, aber auch die verschiedenen GPTs und Claudes, sind keine kleinen Programme. Es sind neuronale Netze mit Hunderten von Milliarden Parametern, von denen jeder eine Fließkommazahl ist, die Platz im Speicher beansprucht. Ein Modell wie DeepSeek V4 Flash hat insgesamt 284 Milliarden Parameter. Wenn wir sie alle in ihrer ursprünglichen Form bei voller Präzision in den Speicher laden wollten, bräuchten wir etwa 568 Gigabyte RAM. Der RAM von High-End-GPU-Servern, der berühmte VRAM von NVIDIA-Karten, wird pro Karte in Zehner-Gigabyte gemessen. Man bräuchte mehrere vernetzte Maschinen, Infrastrukturen im Wert von Zehntausenden von Euro und einen Stromverbrauch wie ein kleiner Industriebetrieb.

Das 128-GB-MacBook, das – das muss man sagen – nicht für jeden erschwinglich ist, scheint dennoch Lichtjahre von dieser Realität entfernt zu sein. Doch DeepSeek V4 Flash gehört zu einer Familie von Architekturen, die in ihrer Struktur versteckt den Schlüssel zur Lösung enthält.

## Mixture of Experts: Wenn Spezialisierung zum Vorteil wird

DeepSeek V4 Flash basiert auf einer Architektur namens Mixture of Experts (MoE). Die mittlerweile bekannte Idee ist recht intuitiv: Anstatt ein einziges dichtes neuronales Netz zu haben, das jeden Token verarbeitet, besteht das Modell aus Dutzenden von spezialisierten Netzen, den "Experten". Für jeden Token werden nur einige davon aktiviert, ausgewählt durch einen Routing-Mechanismus. DeepSeek V4 Flash hat insgesamt 284 Milliarden Parameter, aber nur 13 Milliarden aktive Parameter pro generiertem Token. Es ist, als hätte man eine tausendbändige Enzyklopädie, müsste aber nur ein paar Bücher lesen, um eine spezifische Frage zu beantworten.

Dies hat enorme praktische Konsequenzen: Die Generationsgeschwindigkeit hängt nicht von allen 284 Milliarden Parametern ab, sondern nur von den 13 Milliarden aktiven. Und genau hier setzt die erste große Intuition von DwarfStar an.

Die für DwarfStar bereitgestellten 2-Bit-Quantisierungen sind keine Abkürzung: Sie verhalten sich gut, arbeiten mit Coding-Agenten zusammen und führen Tool-Calls zuverlässig aus. Die 2-Bit-Quantisierungen verwenden eine sehr asymmetrische Kompression: Nur die gerouteten MoE-Experten werden quantisiert (Gate und Up auf IQ2_XXS, Down auf Q2_K). Diese machen den größten Teil des Modellplatzes aus; andere Komponenten (gemeinsam genutzte Experten, Projektionen, Routing) bleiben intakt, um die Qualität zu gewährleisten.

Konkret bedeutet das: Die Teile des Modells, die häufig verwendet werden und das meiste "Signal" tragen, werden in ihrer ursprünglichen Präzision erhalten. Experten, die selten aktiviert werden und weniger zur Qualität des Endergebnisses beitragen, werden aggressiv komprimiert. Das Ergebnis ist eine GGUF-Datei von etwa 81 Gigabyte, die eine Qualität beibehält, die überraschend nah am Originalmodell liegt. Doch wie wird bestimmt, welcher Teil des Modells das meiste Signal trägt? Durch einen empirischen Prozess namens *Imatrix-Kalibrierung*: Das Modell wird auf realen Datensätzen ausgeführt, die Coding, Mathematik, logisches Denken und Tool-Calling abdecken, und es wird gemessen, wie sich die verschiedenen Teile des Netzwerks aktivieren. Diese Wichtigkeitskarte leitet dann die Kompressionsentscheidungen.

Es ist der Unterschied zwischen dem Fällen eines Baumes mit einer Kettensäge und dem sorgfältigen Beschneiden. Der Unterschied ist eine lebende Pflanze statt einer toten.

## Wenn der RAM nicht reicht: Die Festplatte als Speichererweiterung

Selbst mit 81 Gigabyte komprimierter Gewichte ist das Problem nicht vollständig gelöst. Ein MacBook mit 64 oder 96 GB RAM muss einen Weg finden, ein Modell zu verwalten, das nicht vollständig hineinpasst. Und der Kontext, das Gedächtnis der laufenden Unterhaltung, beansprucht mit zunehmender Länge der Unterhaltung weiteren Platz.

DwarfStar führt einen SSD-Streaming-Modus nur für Metal ein: In diesem Modus bleiben die nicht gerouteten Gewichte resident, während die gerouteten MoE-Experten in einem In-Memory-Cache gehalten und bei einem Cache-Miss aus der GGUF-Datei geladen werden. Streaming ist nicht so schnell wie das Laden des gesamten Modells in den RAM, aber es ist nützlich, da die gerouteten Experten die Modellgröße dominieren und moderne Mac-SSDs schnell genug sind, um Cache-Misses erträglich zu machen.

Der Mechanismus ist in seiner konzeptionellen Einfachheit elegant: DwarfStar behält die Gewichte der am häufigsten aufgerufenen Experten – die "heißen" – im RAM und lädt die anderen erst dann von der Festplatte, wenn der Router entscheidet, sie zu aktivieren. Moderne NVMe-SSDs, wie sie in MacBooks und Mac Studios verbaut sind, erreichen sequentielle Lesegeschwindigkeiten im Bereich von 7-10 GB/s. Schnell genug, um das Laden nicht zum Haupt-Flaschenhals zu machen, zumindest für Aufgaben, die keine minimale Latenz erfordern.

Das bedeutet in der Praxis, dass ein 64-GB-MacBook ein Modell mit 284 Milliarden Parametern ausführen kann. Sicherlich nicht mit der gleichen Geschwindigkeit wie ein Mac Studio mit 512 GB Unified RAM, aber mit einer für die reale Arbeit ausreichenden Geschwindigkeit.

## Kontext, Sitzungen und das Gedächtnis, das den Neustart überlebt

Moderne Sprachmodelle sprechen von "Kontextfenstern", als wären sie offensichtlich unbegrenzt. Das sind sie nicht. Jeder Token in der Unterhaltung beansprucht Platz im KV-Cache, der Datenstruktur, die das Modell verwendet, um sich an das Gesagte zu erinnern. Der KV-Cache wächst linear mit der Länge des Kontextes. DeepSeek V4 Flash hat ein Kontextfenster von 1 Million Token, und der KV-Cache ist unglaublich komprimiert, was Inferenz bei langen Kontexten auf lokalen Computern und die Persistenz des KV-Caches auf der Festplatte ermöglicht.

DwarfStar nutzt diese Eigenschaft mit einem System für persistente Sitzungen auf der Festplatte. Wenn eine Unterhaltung unterbrochen wird, der Server neu gestartet wird, die Sitzung gewechselt wird oder man die Arbeit am nächsten Tag wieder aufnehmen möchte, muss das System nicht alle vorherigen Token von Grund auf neu verarbeiten. Die gespeicherte Sitzung enthält den exakten Zustand des KV-Caches, den Token-Checkpoint und sogar die Wahrscheinlichkeitsverteilung des zuletzt generierten Tokens. Die Fortsetzung erfolgt fast augenblicklich.

Dies löst eines der frustrierendsten Probleme lokaler KI-Agenten: die Tatsache, dass jeder neue API-Aufruf den gesamten Kontext erneut senden muss, wobei jedes Mal die Rechenkosten für den *Prefill* anfallen. Mit DwarfStar werden teure Prefills gespeichert und wiederverwendet. Ein Coding-Agent, der einen 25.000 Token langen System-Prompt verwendet (wie Claude Code), zahlt diese Kosten nur ein einziges Mal.

## Zwei Maschinen sind mehr wert als eine

Der jüngste Punkt in der Entwicklung von DwarfStar betrifft die Verteilung der Inferenz auf mehrere Maschinen. Der Distributed-Branch befindet sich nun im Hauptcode: Die verteilte Inferenz bewegt sich von der Theorie zum ausführbaren Code. Die GGUF-Datei liegt auf jeder Maschine vor, aber jeder Knoten lädt über das Flag --layers mit inklusiven Bereichen nur seinen Teil der Layer, ohne die Gewichte, die nicht zu ihm gehören, im RAM zu behalten. Koordinator/Worker-Architektur: Eine Maschine fungiert als Koordinator (Tokenisierung, Sampling und der initiale Prompt), die anderen sind Worker, die ihren Teil verarbeiten und die Aktivierungen über TCP weiterleiten.

Der Ansatz ist der des *Layer-Splits*: Maschine A lädt und verarbeitet die ersten N Layer des Transformers, übergibt die Aktivierungen an Maschine B, die die restlichen Layer verarbeitet, und das Ergebnis geht zurück an den Koordinator zum Sampling. Der Datentransfer zwischen den Maschinen ist minimal, da nur die Zwischenaktivierungen übertragen werden – relativ kleine Vektoren – und nicht die Modellgewichte.

Mit DwarfStar kann ein M3 Ultra Mac Studio mit 512 GB DeepSeek V4 PRO mit 150 Token/s Prefill und etwa 10-13 Token/s Dekodierung ausführen – nicht außergewöhnlich, aber auf einem für bestimmte Anwendungsfälle nutzbaren Niveau. Zwei vernetzte Mac Studios könnten das größere Modell, DeepSeek V4 PRO bei voller Präzision, verteilen und dank Micro-Batching von einem schnelleren Prefill profitieren. Wer zwei M5 Max MacBooks mit 128 GB hat, kann sich nun die Last eines einzelnen Modells teilen, anstatt sie separat zu nutzen.

Antirez erkundet auch experimentellere Ansätze: Das Ensemble von Modellen, bei dem zwei Instanzen desselben (oder unterschiedlicher) Modelle auf separaten Maschinen laufen und ihre Logits – die Wahrscheinlichkeitsverteilung über die folgenden Token – kombinieren, um ein besseres Ergebnis zu erzielen, als es jedes für sich allein produzieren würde. Dies ist eine in der Literatur untersuchte Technik, die jedoch selten praktisch implementiert wird.

## Die Zahlen: Was in der Praxis zu erwarten ist

Die Benchmarks von DwarfStar sind messbar und in der offiziellen Projektdokumentation veröffentlicht. Auf einem M3 Max MacBook Pro mit 128 GB und 2-Bit-Quantisierung:

Bei kurzen Prompts erreicht der Prefill 58,52 Token/s und die Generierung 26,68 Token/s. Bei langen Prompts von etwa 11.700 Token steigt der Prefill dank Chunked-Prefill auf 250,11 Token/s, während die Generierung aufgrund des wachsenden Kontextes auf 21,47 Token/s sinkt.

Auf einem M3 Ultra Mac Studio mit 512 GB fallen die Zahlen großzügiger aus: Prefill mit 84,43 Token/s bei kurzen Prompts, Generierung mit 36,86 Token/s. Bei langen Prompts erreicht der Prefill 468,03 Token/s bei einer Generierung von 27,39 Token/s.

Das M5 Max MacBook mit 128 GB kann laut antirez DeepSeek V4 Flash in der 2-Bit-Quantisierung mit etwa 460 Token/s Prefill und 25 Token/s Generierung ausführen, mit einer akzeptablen Degradationskurve bei zunehmendem Kontext.

Um eine konkrete Referenz zu geben: Laut vorlesen bedeutet, etwa 150 Wörter pro Minute auszusprechen, was etwa 200 Token entspricht. Mit 26 Token pro Sekunde generiert DwarfStar Text mit etwas mehr als einem Achtel dieser Geschwindigkeit – langsam im Vergleich zu Cloud-Diensten, aber schnell genug für eine echte interaktive Nutzung.
![tabella1.jpg](tabella1.jpg)
[Bild aus dem GitHub-Repository](https://github.com/antirez/ds4)

## GLM 5.2 und die Ausrichtung des Projekts

DwarfStar wurde als bewusst spezialisierte Engine konzipiert: Eine einzige Modellfamilie wird tiefgreifend und korrekt unterstützt, anstatt alles oberflächlich zu unterstützen.

Doch die Ambitionen wachsen. In den letzten Stunden hat antirez ein Video mit dem Titel "Considerations on the implementation of GLM 5.2 in DwarfStar" veröffentlicht. Es ist explizit ein Work-in-Progress; das Signal ist klar: Das Projekt beabsichtigt nicht, bei DeepSeek stehen zu bleiben. Die MoE-Architektur mit komprimiertem KV-Cache ist zu einem Merkmal geworden, das mehrere Frontier-Modelle teilen, und DwarfStar ist gerüstet, dem zu folgen.

Man muss ehrlich sagen: Das Projekt befindet sich noch im Beta-Zustand, wie antirez selbst in der README erklärt. Einige Funktionen sind experimentell, die CUDA-Unterstützung ist neuer als die für Metal, und bestimmte Verhaltensweisen könnten sich ändern. Aber die Flugbahn ist die eines Projekts, das bereits bewiesen hat, dass es Dinge tun kann, die noch vor wenigen Wochen unmöglich schienen.

## Die Frontier, offen für alle (fast)

Es gibt ein Wort, das in jeder Diskussion über DwarfStar obsessiv vorkommt: *Demokratisierung*. Es ist ein strapaziertes Wort, das oft verwendet wird, um kommerzielle Produkte mit einem Schleier progressiver Rhetorik zu überziehen. Hier hat der Begriff eine präzisere und ehrlichere Bedeutung.

DwarfStar ist kostenlos. Der Code ist MIT. Die Quantisierungen werden ohne Einschränkungen auf Hugging Face veröffentlicht. Es gibt keine Pro-Version, keinen Enterprise-Plan, keinen API-Key zu kaufen. Jeder, der einen Mac mit 96 GB RAM oder einen 5.000 Dollar teuren DGX Spark besitzt – oder mit SSD-Streaming sogar weniger –, kann alles herunterladen und einen KI-Agenten mit fast 300 Milliarden Parametern lokal und offline betreiben, ohne einen einzigen Token an einen Remote-Server zu senden.

Datenschutz ist kein nebensächliches Argument. Ein Agent, der den Code deines Unternehmens, deine Dokumente und deine internen Gespräche kennt, sollte nicht zwangsläufig über die Server von Anthropic oder OpenAI laufen. Mit DwarfStar tut er das nicht.

Sicherlich bleibt die Hardware ein reales Hindernis. 128 GB Unified RAM sind keine Fünfzig-Euro-Konfiguration. Ein M3 Max MacBook Pro in der benötigten Version beginnt bei etwa 4.000 Euro; ein M3 Ultra Mac Studio mit 192 GB übersteigt die 7.000 Euro. Das ist nicht für jeden erschwinglich, und das sollte man ehrlich sagen. Aber es ist für viele Profis, Studios, KMUs und Forscher erschwinglich. Und die Kosten für dieselbe Rechenleistung in der Cloud übersteigen auf Jahresbasis bei weitem die Hardwarekosten, ganz zu schweigen vom Wert des Datenschutzes und der Unabhängigkeit.

Dann gibt es noch eine subtilere Dimension. Jedes Mal, wenn ein Frontier-Modell auf Consumer-Hardware läuft, jedes Mal, wenn jemand beweist, dass man kein Rechenzentrum für ernsthaftes logisches Denken braucht, verschiebt sich die schiefe Ebene ein Stück. Die Hardware wird besser: Das M5 Max MacBook mit 128 GB ist bereits die beste Kosten-Leistungs-Balance, die für lokale Inferenz im Jahr 2026 verfügbar ist. Die Modelle werden besser und effizienter. Und es gibt Menschen wie Sanfilippo, die arbeiten, um der Sache selbst willen, aus der Befriedigung heraus, es gut zu machen, um die Kluft weiter zu verringern.

Redis hat Jahre gebraucht, um die beliebteste Datenbank der Welt zu werden. DwarfStar hat bereits wenige Wochen nach dem Start 15.500 Sterne auf GitHub, mit aktiven Mitwirkenden, Ports für CUDA und ROCm sowie veröffentlichten Benchmarks auf DGX Spark, MacBook und Mac Studio. Die Geschwindigkeit der Einführung sagt etwas über die Dringlichkeit des Bedürfnisses aus, das es erfüllt.

In Alan Moores Comic *From Hell* – nicht der Hollywood-Version – gibt es einen Charakter, der feststellt, dass die Zeit immer jetzt ist, dass alles gleichzeitig geschieht. Die Vergangenheit der Local-AI-Bewegung und ihre Zukunft berühren sich in einer 81 Gigabyte großen Datei, die du jetzt herunterladen kannst, auf einem Computer, den du auf deinem Schreibtisch hast. Antirez hat es gebaut. Der Rest ist, wie man sagt, Geschichte.

---

*Das offizielle DwarfStar-Repository ist auf [GitHub](https://github.com/antirez/ds4) verfügbar. Die offiziellen Quantisierungen für DeepSeek V4 Flash sind auf [Hugging Face](https://huggingface.co/antirez/deepseek-v4-gguf) veröffentlicht. Salvatore Sanfilippos Blog ist unter [antirez.com](https://antirez.com) erreichbar.*
