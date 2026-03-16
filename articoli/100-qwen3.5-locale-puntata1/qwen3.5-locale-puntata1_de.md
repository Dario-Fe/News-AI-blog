---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-16
author: "Dario Ferrero"
---

# KI zu Hause: LM Studio und Qwen 3.5 auf meinem PC – Folge 1
![qwen3.5-locale-puntata1.jpg](qwen3.5-locale-puntata1.jpg)

*Es gibt einen präzisen Moment, in dem eine Technologie aufhört, ein Versprechen zu sein, und zum Werkzeug wird. Es ist nicht der Moment, in dem die Pressemitteilung erscheint, nicht der, in dem die Benchmarks in den sozialen Medien die Runde machen, sondern der Moment, in dem sich ein normaler Mensch mit einem normalen PC hinsetzt, etwas herunterlädt und beschließt, wirklich zu verstehen, was da gerade passiert. Dieser Artikel ist dieser Moment, zumindest für mich.*

In den letzten zwei Wochen gab es im Open-Weight-Ökosystem der künstlichen Intelligenz nur einen Namen, der die Gespräche dominierte: Qwen 3.5. Das Team von Alibaba veröffentlichte am 2. März 2026 die Small-Serie des Modells, Varianten von 0,8 bis 9 Milliarden Parametern, alle unter der Apache 2.0-Lizenz, alle auf Consumer-Hardware ausführbar, und die Reaktion der Community war unmittelbar und lebhaft. Doch bevor wir in die Details des Modells und meines persönlichen Experiments eintauchen, ist es nützlich zu verstehen, warum dieser Moment genau jetzt gekommen ist.

## Der Wind dreht sich

In einem vor einigen Wochen auf diesem Portal veröffentlichten Artikel [habe ich die Gründe analysiert, warum 2026 als das Jahr der Small Language Models gilt](https://aitalk.it/it/slm-2026.html): die Konvergenz von Druck auf Energiekosten, immer strengeren Datenschutzanforderungen und einem qualitativen Sprung in der architektonischen Effizienz, der die Grenze zwischen „möglich in der Cloud“ und „möglich lokal“ neu definiert hat. Dies ist kein ideologischer Trend, sondern eine pragmatische Antwort auf reale Zwänge.

Die Daten erzählen jedoch noch eine Geschichte von zwei Geschwindigkeiten. Wie aus der [ebenfalls hier veröffentlichten Analyse des DigitalOcean Currents-Berichts hervorgeht](https://aitalk.it/it/agenti-al-lavoro.html), integrieren 64 % der Unternehmen KI-Modelle heute über APIs von Drittanbietern, und nur 21 % nutzen Open-Weight-Modelle in der Produktion. Die Cloud ist nicht tot: Sie ist immer noch dominant. Aber was wie eine unüberwindbare Asymmetrie zwischen riesigen proprietären Modellen und lokalen „Notlösungen“ aussah, schrumpft mit einer Geschwindigkeit, die selbst aufmerksamste Beobachter überrascht.

In Benchmarks wie [GPQA Diamond](https://huggingface.co/datasets/Idavidrein/gpqa), dem Referenztest für fortgeschrittenes wissenschaftliches Denken auf Universitätsniveau – 198 Fragen aus Physik, Chemie und Biologie –, erreicht Qwen3.5-9B einen Wert von 81,7 und übertrifft damit das GPT-OSS-120B von OpenAI, das bei 71,5 stoppt, wie auf der [offiziellen Seite des Modells auf HuggingFace berichtet wird](https://huggingface.co/Qwen/Qwen3.5-9B). Wir sprechen von einem Modell mit dreizehnmal weniger Parametern. Dies ist keine schrittweise Optimierung: Es ist ein Paradigmenwechsel dessen, was „klein“ im Jahr 2026 bedeutet.

Die Reaktionen in der Branche waren bedeutend und, wie so oft in diesem Bereich, nicht einhellig. Einige führende Beobachter begrüßten die Veröffentlichung mit Begeisterung und hoben die Dichte der Fähigkeiten im Verhältnis zur Größe hervor. Andere, allen voran Anthropic, blieben vorsichtiger und merkten an, dass Modelle, die auf Benchmarks optimiert sind, diese Fähigkeiten nicht immer mit der gleichen Treue in die reale Welt übertragen. Eine Spannung, die die gesamte Debatte über Open-Weight-KI durchzieht und die keine Zahl in einer Tabelle endgültig löst. Die Wahrheit liegt, wie immer, in der Anwendung.

Und genau deshalb habe ich beschlossen, mir selbst die Hände schmutzig zu machen.

## Ein ehrliches Experiment ohne wissenschaftlichen Anspruch

Bevor wir fortfahren, muss klargestellt werden, was dieser Artikel ist und was er nicht ist. Was folgt, ist ein persönliches Experiment eines Enthusiasten, der verstehen will, was man mit normalen Mitteln in diesem präzisen historischen Moment erreichen kann. Es gibt kein Peer-Review-Testprotokoll, keine statistisch signifikante Stichprobe von Prompts, keine reproduzierbare Methode, die der Prüfung einer akademischen Konferenz standhalten würde. Die Tests wurden durch Abgleich der Ergebnisse mit Frontier-Modellen wie Claude und DeepSeek verifiziert, aber das macht sie nicht zu wissenschaftlichen Benchmarks: Es bleiben Feldtests, durchgeführt mit den Werkzeugen eines versierten Nutzers, nicht eines Forschers.

Der Wert liegt, falls vorhanden, genau darin: zu verstehen, wie weit man mit gutem, aber nicht promoviertem Wissen, mit privater Hardware und dem Willen zu verstehen, bevor man kauft, kommt. Wer zertifizierte Zahlen sucht, findet die offiziellen Benchmarks auf der [HuggingFace-Seite des Modells](https://huggingface.co/Qwen/Qwen3.5-9B). Wer wissen will, wie es auf einem vernünftig bepreisten PC aus dem Jahr 2025 läuft, liest weiter.

## Das Labor: Ein PC der Mittelklasse

Die Maschine, auf der ich die Tests durchgeführt habe, ist weder eine professionelle Rendering-Workstation noch ein Wettbewerbs-Gaming-Rig. Es ist ein mit Bedacht, aber ohne Übertreibung zusammengestellter PC: AMD Ryzen 7700 Prozessor, 32 GB DDR5 RAM und vor allem eine AMD Radeon RX 9060 XT Grafikkarte mit 16 GB VRAM. Eine Konfiguration, die viele fortgeschrittene Nutzer, Gamer, Content-Ersteller oder Entwickler, die von zu Hause aus arbeiten, als ihre eigene wiedererkennen könnten. Hardware der gehobenen Mittelklasse im Consumer-Segment, aber weit entfernt von der A100, die man sich vorstellt, wenn man von lokaler Inferenz bei Sprachmodellen spricht.

Diese Wahl ist nicht zufällig. Genau die Mittelklasse der Konfiguration ist der Punkt. Wenn ein Modell hier gut läuft, läuft es auf einem riesigen Teil der bereits existierenden PCs gut. Wenn es hier Probleme hat, schrumpft dieser Teil erheblich.

## Die Wahl des Frameworks: LM Studio gegen Ollama

Um ein Sprachmodell lokal auszuführen, braucht man zwei Dinge: das Modell selbst (eine Datei von einigen Gigabyte) und ein Framework, das als Dolmetscher zwischen der Hardware und dem Modell fungiert und Speicher, Tokenisierung und Inferenz verwaltet. Ohne diese Zwischenschicht ist das Herunterladen der Gewichte eines Modells wie der Besitz der Dateien eines Films ohne Videoplayer.

Die beiden Wege, die diesen Bereich im Jahr 2026 dominieren, werden durch [LM Studio](https://lmstudio.ai/) und [Ollama](https://ollama.com/) repräsentiert, und der Unterschied zwischen ihnen spiegelt eine klassische Spannung in der Software wider: Zugänglichkeit versus Kontrolle.

[Ollama](https://ollama.com/) ist das Werkzeug der Entwickler. Es wird mit einer Zeile im Terminal installiert, stellt standardmäßig eine OpenAI-kompatible REST-API unter `localhost:11434` bereit und lässt sich nahtlos in Skripte, Pipelines und Anwendungen integrieren. Es ist Open Source, hat eine große Community, und seine minimalistische Philosophie – ein Befehl zum Herunterladen, ein Befehl zum Ausführen – macht es zum bevorzugten Backend für Dutzende von Drittanbieteranwendungen. In Bezug auf die reine Performance ist es tendenziell schneller, verarbeitet gleichzeitige Anfragen besser und verbraucht dank des Verzichts auf grafischen Overhead weniger Ressourcen. Die Kehrseite: Es erfordert Vertrautheit mit dem Terminal, die fortgeschrittene Konfiguration erfolgt über Modelfiles, und seine native grafische Benutzeroberfläche kam spät und bleibt minimal. Es gibt auch eine Frage der Transparenz, die erwähnenswert ist: Ollama ist Open Source, und die Community vertraut seinem Verhalten, während LM Studio Closed Source ist – ein Detail, das für diejenigen, die besonders auf Datenschutz achten, wichtig sein könnte.

[LM Studio](https://lmstudio.ai/) spielt auf einem anderen Feld. Es ist eine Desktop-Anwendung mit einer gepflegten grafischen Benutzeroberfläche, verfügbar für Windows, macOS und Linux. Es ermöglicht das Suchen, Herunterladen und Laden von Modellen, ohne ein Terminal zu öffnen, stellt ebenfalls eine OpenAI-kompatible API für diejenigen bereit, die es in andere Werkzeuge integrieren wollen, und verwaltet automatisch die GPU-Beschleunigung auf Hardware von NVIDIA, Apple Silicon und AMD. Aber das Detail, das die Erfahrung für diejenigen, die ohne Entwicklerhintergrund zur lokalen KI kommen, wirklich verändert, ist folgendes: Bei der Auswahl eines Modells zeigt LM Studio in Echtzeit eine Schätzung der erwarteten Performance auf der eigenen Hardwarekonfiguration an, mit farbigen Indikatoren, die sofort kommunizieren, ob das Modell reibungslos läuft, mit Einschränkungen oder ob die Hardware unzureichend ist. Für eine Privatperson, die experimentiert, ist diese beseitigte Hürde den eventuellen Performance-Unterschied gegenüber Ollama wert.

Die Wahl für dieses Experiment fiel aus pragmatischen Gründen auf LM Studio: Die Möglichkeit, im Voraus zu sehen, ob Qwen 3.5 9B Q8_0 auf meiner GPU mit voller Leistung laufen würde, ohne manuelle Berechnungen oder technische Dokumentation konsultieren zu müssen, erlaubte es mir, die Wahl sofort zu optimieren. Wer hingegen ein Modell in eine Anwendung integrieren, Workflows automatisieren oder in einer Serverumgebung arbeiten möchte, für den bleibt Ollama die solidere Wahl.
![lmstudio.jpg](lmstudio.jpg)
*Screenshot meines PCs beim Start von LM Studio. Im Menü oben rechts die Softwareoptionen mit der untersten Schaltfläche zum Auswählen und Herunterladen des gewünschten Modells. Daneben der Chatverlauf. Unten in der Mitte das Dialogfenster für Prompts, in dem das ausgewählte Modell zu sehen ist.*

## LM Studio installieren: Fünf Minuten und es geht los

Die Installation erfordert keine besonderen technischen Kenntnisse. Von der [offiziellen Website](https://lmstudio.ai/) lädt man den Installer für sein Betriebssystem herunter – eine EXE-Datei für Windows, eine DMG-Datei für macOS, ein AppImage für Linux – und geht vor wie bei jeder anderen Desktop-Anwendung. Keine externen Abhängigkeiten, die installiert werden müssen, keine virtuellen Umgebungen, die konfiguriert werden müssen, kein Terminal, das geöffnet werden muss. Das Paket ist etwa 500 MB groß; die ersten Bildschirme führen durch die Konfiguration der automatisch erkannten Hardwarebeschleunigung, und in wenigen Minuten befindet man sich vor dem Hauptbildschirm.

Von dort aus ermöglicht der Bereich für die Modellsuche das Durchsuchen des Katalogs, der sich hauptsächlich aus HuggingFace speist, wobei nach Größe, Quantisierungsart und erklärter Hardwarekompatibilität gefiltert werden kann. Bei Auswahl eines Modells erscheinen die Performance-Schätzungen auf der eigenen Maschine: Hier versteht man sofort, was man erwarten kann, bevor man auch nur einen einzigen Gigabyte herunterlädt.

## Warum Qwen 3.5 9B und warum Q8_0

Nachdem das Framework installiert ist, ist die Wahl des Modells der zweite kritische Punkt. Ich habe Qwen 3.5 9B in der Q8_0-Quantisierung gewählt – die Datei belegt etwas mehr als 10 GB auf der Festplatte –, aus Gründen, die es wert sind, erklärt zu werden, da sie eine nützliche Logik für jeden widerspiegeln, der vor dieser Wahl steht.

Die Größe von 9 Milliarden Parametern ist in dieser Zeit zum De-facto-Standard für Feldtests geworden: Es ist die am weitesten verbreitete Größe unter allen führenden Wettbewerbern, die Open-Weight-Modelle veröffentlichen, stellt den Gleichgewichtspunkt zwischen Fähigkeiten und Hardwareanforderungen dar und ermöglicht aussagekräftige Vergleiche zwischen verschiedenen Familien. Die Varianten mit 27B und 35B sind sicherlich leistungsfähiger, erfordern aber teurere Hardware, was für eine Privatperson einen nicht trivialen Sprung darstellt. Für ein Unternehmen, auch ein kleines, hat die Bewertung eines 9B-Modells einen doppelten Wert: zu verstehen, was man sofort mit minimalem Investment erhält, und zu projizieren, was man mit einer höheren Hardwarestufe erreichen könnte, angesichts des Tempos, mit dem die Performance wächst und die Anforderungen sinken.

Die Wahl der Q8_0-Quantisierung, der höchsten der drei in LM Studio für dieses Modell verfügbaren Optionen, wurde genau durch die 16 GB VRAM ermöglicht: Der grüne Indikator bestätigte, dass das Modell vollständig auf der GPU laufen würde, ohne Layer in den System-RAM auslagern zu müssen, was eine maximale Inferenzgeschwindigkeit und eine Antwortqualität garantiert, die nicht durch numerische Näherungen aggressiverer Quantisierungen beeinträchtigt wird.

Auf technischer Ebene ist Qwen 3.5 nicht einfach ein verkleinertes Vorgängermodell. Wie in der [offiziellen Dokumentation auf HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B) beschrieben, nutzt die Architektur einen hybriden Ansatz, der Gated Delta Networks – eine Form der linearen Attention – mit sparse Mixture-of-Experts kombiniert, mit dem Ziel, die „Memory Wall“ zu überwinden, die typischerweise kleine Modelle einschränkt, und so einen hohen Durchsatz bei reduzierter Latenz zu gewährleisten. Das native Kontextfenster beträgt 262.144 Token, erweiterbar auf etwa eine Million über YaRN. Und im Gegensatz zu früheren Generationen, die Vision-Fähigkeiten als separate Module hinzufügten, wurde Qwen 3.5 von Anfang an auf multimodalen Token trainiert, wobei Text, Bilder und Video durch einen Prozess namens „Early Fusion“ integriert wurden.

Das Modell unterstützt zwei Betriebsmodi: *Thinking* und *Non-Thinking*. Im ersten Modus generiert das Modell vor der eigentlichen Antwort explizit eine interne Gedankenkette und widmet der Verarbeitung 20 bis 40 Sekunden, bevor es die eigentliche Antwort schreibt. Im zweiten Modus antwortet es sofort. In allen folgenden Tests habe ich den Thinking-Modus verwendet, da einige Prompts bewusst komplex waren. Ich habe dieselben Tests auch mit deaktiviertem Thinking durchgeführt: Die Antworten erfolgen sofort, die Tiefe nimmt bei komplexeren Fragen leicht ab, aber für den täglichen Gebrauch, Schreibunterstützung, Routine-Coding, Textanalyse oder informative Fragen ist die Kombination aus Präzision und Geschwindigkeit mehr als zufriedenstellend. In beiden Modi lag der Output bei etwa 30 Token pro Sekunde auf dieser Hardwarekonfiguration.
![grafico1.jpg](grafico1.jpg)
[Bild von huggingface.co](https://huggingface.co/Qwen/Qwen3.5-9B)

## Die Tests: Sechs Feldversuche

Die folgenden sechs Tests wurden entwickelt, um die wichtigsten Bereiche der Bewertung von Sprachmodellen abzudecken: fortgeschrittenes wissenschaftliches Denken, multimodales Verständnis, komplexe Codegenerierung, Mehrsprachigkeit mit Planung, Umgang mit sehr langen Kontexten und visuell-räumliches Denken. Für jeden Test wurden die Ergebnisse von Qwen 3.5 9B durch Abgleich mit Frontier-Modellen wie Claude und DeepSeek verifiziert – nicht als wissenschaftliche Validierung, sondern als praktischer Validitätscheck.

Die Bewertungen zu jedem Test sind das Ergebnis einer persönlichen Einschätzung nach Online-Recherchen, abgeglichen mit den Antworten auf dieselben Prompts und den Bewertungen der von Qwen 3.5 9B gelieferten Antworten durch Claude und DeepSeek. Es ist das Urteil eines anspruchsvollen Nutzers, nicht das Urteil eines Benchmarks.

### Test 1 — Wissenschaftliches Denken: Der Higgs-Mechanismus

Der erste Test war ein Klassiker für High-Level-Benchmarks: Einem Physikstudenten den Higgs-Mechanismus und die elektroschwache Symmetriebrechung erklären. Eine Frage, die mathematische Strenge erfordert, ohne die Klarheit zu opfern, und die Fähigkeit, einen narrativen Pfad aufzubauen, der den Leser durch nicht triviale Konzepte führt.

Die Antwort war in fünf Abschnitte gegliedert, die mit der Logik einer gut geführten Unterrichtsstunde voranschritten: von der Einordnung des Massenproblems bei Eichbosonen über die Einführung des Higgs-Feldes mit seinem „mexikanischen Hut“-Potenzial als mentales Bild bis hin zur Erklärung des Mechanismus, durch den die W- und Z-Bosonen Goldstone-Bosonen „trinken“ und so Masse erlangen, während das Photon dank der Restsymmetrie masselos bleibt. Jede Formel wurde von einer physikalischen Interpretation begleitet; jeder technische Schritt enthielt einen Satz, der seinen tiefen physikalischen Sinn offenbarte. Abgleiche mit Frontier-Modellen und eigene Online-Recherchen ergaben eine korrekte, gut strukturierte Antwort mit den richtigen Metaphern. Nicht trivial für ein Modell, das auf einem Consumer-PC läuft.

**Bewertung: 5/5.** Die Genauigkeit war da, die Klarheit ebenso. Überraschend war vor allem die Fähigkeit, passende Metaphern zu wählen, anstatt nur Wissen zu reproduzieren.

### Test 2 — Multimodalität: Visuelles Chaos lesen

Für den zweiten Test habe ich ein kleines Bild von geringer Qualität heruntergeladen, das eine Tabellenkalkulation mit dem Inventar eines Elektronikgeschäfts zeigte: neun Spalten mit Artikelcodes, Produktnamen, Kaufdaten, Kategorien, Mengen, Kosten und Verkaufspreisen. Das Bild war bewusst schlecht, leicht unscharf, und ich habe die Datei direkt in LM Studio hochgeladen mit der Aufforderung, zu beschreiben, was zu sehen ist.

Das Modell las alle Spalten und numerischen Werte, aber der interessante Teil kam danach: Es bemerkte selbstständig, dass die Spalte „Gesamt“ das Produkt aus Menge und Stückpreis war, identifizierte einige Monitore mit null Verkäufen und interpretierte sie als potenziell unverkäufliche Ware, unterschied kostengünstige Artikel wie Mäuse von Premiumprodukten wie Prozessoren und erkannte, dass die Kaufdaten einen Zeitraum von Oktober 2017 bis Dezember 2018 abdeckten. Es hat nicht nur transkribiert: Es hat die Daten wie ein Analyst interpretiert.

Einige kleinere numerische Details wurden unpräzise wiedergegeben, was angesichts der Bildqualität verständlich ist. Aber die Fähigkeit, vom reinen Lesen zum kontextuellen Verständnis überzugehen, ist genau das, was eine dekorative Multimodalität von einer funktionalen unterscheidet.

**Bewertung: 4,8/5.** Das Auslesen war korrekt, die hinzugefügte Business-Intelligence-Analyse war ein unerwarteter Bonus. Ein paar Abzüge für kleinere numerische Ungenauigkeiten.

### Test 3 — Codegenerierung: Ein NP-schweres Problem

Der dritte Test betraf das Coding, den Bereich, in dem Benchmarks vermuten lassen, dass Qwen 3.5 9B etwas weniger glänzt als andere Modelle. Ich bat darum, in Python einen Algorithmus zu implementieren, um den längsten Zyklus in einem ungerichteten Graphen zu finden – ein NP-schweres Problem, das nicht nur Implementierungsfähigkeiten, sondern auch theoretisches Bewusstsein erfordert.

Die erste Antwort brach aufgrund eines technischen Problems bei der Verarbeitung langer Outputs in der Mitte ab – ein Verhalten, das man ehrlich erwähnen sollte. Nach der Aufforderung zur Vervollständigung lieferte das Modell eine vollständige Lösung mit Backtracking und Pruning, dem korrekten Ansatz für diese Art von Problem, mit Type Hints, gut getrennten Methoden und einschlägigen Kommentaren. Aber das Detail, das am meisten beeindruckte, kam noch vor dem Code: Das Modell erklärte explizit, dass das Problem NP-schwer ist, dass kein bekannter Algorithmus mit polynomieller Laufzeit existiert und dass für große Graphen ein Näherungsansatz in Betracht gezogen werden sollte. Dieses Bewusstsein für theoretische Grenzen noch vor dem Schreiben des Codes ist das Zeichen für etwas Tieferes als reine Syntaxgenerierung.

**Bewertung: 5/5.** Der anfängliche Schluckauf ist zu vermerken, aber die endgültige Lösung und die bewiesene theoretische Reife übertrafen die Erwartungen an ein 9-Milliarden-Parameter-Modell.

---

*Die Folge endet hier. Im zweiten Teil: der mehrsprachige Planungstest, die Herausforderung mit einem 460-seitigen PDF und das visuell-räumliche Denken in einem chaotischen Raum. Plus die Schlussfolgerungen darüber, was es im Jahr 2026 wirklich bedeutet, einen lokalen Assistenten zu haben.*
