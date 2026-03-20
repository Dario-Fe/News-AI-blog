---
tags: ["Research", "Training", "Applications"]
date: 2026-03-20
author: "Dario Ferrero"
---

# Der Forscher schläft. Autoresearch: Wie Andrej Karpathy Maschinen beibrachte, autonom zu forschen
![autoresearch-karpathy.jpg](autoresearch-karpathy.jpg)

*Es gibt eine Szene in japanischen Rollenspielen – Karpathy kennt sie gut –, in der der Protagonist aufhört, Monster alleine zu bekämpfen, und anfängt, andere Charaktere auszubilden, damit sie es an seiner Stelle tun. Der Übergang ändert alles: Sie sind kein Kämpfer mehr, Sie sind ein Trainer. Andrej Karpathy hat etwas Ähnliches mit der Forschung im Bereich der künstlichen Intelligenz getan.*

Karpathy ist eine Figur, die in der Branche kaum vorgestellt werden muss, aber es lohnt sich, ihn für diejenigen einzuordnen, die von außen kommen. Ehemaliger Direktor für künstliche Intelligenz bei Tesla, Mitbegründer von OpenAI, heute unabhängiger und produktiver technischer Vermittler: Er ist vor allem für seine Fähigkeit bekannt, dichte und spezialisierte Konzepte zugänglich zu machen. Sein Kurs [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) ist ein Referenzpunkt für jeden, der Sprachmodelle ohne einen Doktortitel in der Tasche verstehen möchte.

Anfang März 2026 veröffentlichte Karpathy auf GitHub ein neues Open-Source-Projekt namens [autoresearch](https://github.com/karpathy/autoresearch). Das Repository zählt bereits über 23.000 Sterne und fast dreitausend Forks – Zahlen, die in der Welt der Softwareentwicklung das Interesse mit der gleichen Präzision wie ein Seismograph messen. Die Grundidee ist einfach zu beschreiben, aber schwer zu verdauen: Einem KI-Agenten ein kleines, aber authentisches Trainingssystem für Sprachmodelle zu geben und ihn nachts alleine experimentieren zu lassen, während der Forscher schläft.

## Anatomie eines nächtlichen Loops

Um zu verstehen, was autoresearch tut, ist es hilfreich, sich die tägliche Arbeit eines Machine-Learning-Forschers vorzustellen. Normalerweise sitzt diese Person vor dem Computer, formuliert eine Hypothese („Was wäre, wenn ich eine kleinere Batch-Größe verwenden würde?“), ändert manuell den Trainingscode, startet ein Experiment, das Stunden dauert, analysiert die Ergebnisse und beginnt von vorn. Es ist ein serieller Prozess, langsam und begrenzt durch die Stunden des Arbeitstages und die menschliche Konzentrationsfähigkeit.

Autoresearch bricht diesen Zyklus radikal auf. Das System ist um nur drei Dateien herum aufgebaut, die wirklich zählen: `prepare.py` (die die Datenvorbereitung verwaltet und nie geändert wird), `train.py` (der Modellcode, den der Agent in all seinen Teilen berühren kann) und `program.md` (die Anweisungen für den Agenten, geschrieben in natürlicher Sprache). Der menschliche Benutzer greift nicht in die Python-Dateien ein: Seine Aufgabe ist es, die Markdown-Datei zu schreiben und zu verfeinern, das heißt, *das Programm zu programmieren*, anstatt direkt zu programmieren.

Einmal gestartet, liest der Agent – in der Standardkonfiguration handelt es sich um Claude von Anthropic oder Codex von OpenAI – die Anweisungen, schlägt eine Änderung am Trainingscode vor, führt ein Experiment mit einer festen Dauer von genau fünf Minuten aus, misst, ob sich das Ergebnis verbessert hat, behält die Änderung bei oder verwirft sie und wiederholt den Vorgang. Zwölf Experimente pro Stunde, etwa hundert im Laufe einer Nacht. Am Morgen wacht der Forscher vor einem detaillierten Protokoll dessen auf, was alles ausprobiert wurde und (hoffentlich) einem besseren Modell.

Die zur Messung des Fortschritts verwendete Metrik heißt `val_bpb` oder *validation bits per byte*: Sie misst, wie gut das Modell den Text komprimieren kann, ausgedrückt in der Anzahl der Bits, die benötigt werden, um jedes Byte an Daten darzustellen. Es ist eine elegante Metrik, da sie unabhängig von der Größe des Vokabulars ist, was bedeutet, dass Experimente mit unterschiedlichen Architekturen miteinander vergleichbar bleiben. Niedrigere Werte deuten auf ein fähigeres Modell hin.

Die gesamte Codebasis umfasst etwa 630 Zeilen Python. Das ist kein Nebeneffekt: Es ist eine philosophische Entscheidung. Karpathy hat bewusst ein System gebaut, das ein einzelner Entwickler lesen, verstehen und unter Kontrolle halten kann. Eine menschliche Überprüfung bleibt möglich. Die Diffs, die Unterschiede zwischen einer Version des Codes und der nächsten, sind lesbar.

Um autoresearch vollständig zu verstehen, muss man das Projekt kennen, aus dem es hervorgegangen ist: [nanochat](https://github.com/karpathy/nanochat), das Karpathy schlicht als „das beste ChatGPT, das man für hundert Dollar kaufen kann“ beschreibt. Das ist kein Marketing-Hype: nanochat ist ein komplettes und minimales System zum Trainieren von Sprachmodellen auf einer einzelnen GPU, das die gesamte Kette abdeckt, von der Tokenisierung über das Pretraining und Fine-Tuning bis hin zu einer funktionierenden Chat-Schnittstelle.

Sein Stolz ist ein öffentliches Leaderboard, das die Zeit misst, die benötigt wird, um die Fähigkeiten des ursprünglichen GPT-2 (das 2019 etwa 43.000 Dollar und Wochen an Rechenzeit kostete) auf zugänglicher Hardware zu replizieren: Derzeit ist der Rekord auf knapp über drei Stunden auf einem Knoten mit acht H100-GPUs gesunken, bei Kosten von etwa siebzig Dollar.

Autoresearch ist im Wesentlichen die Single-GPU- und Agenten-zentrierte Version von nanochat: Es verwendet dieselbe vereinfachte Codebasis als Experimentierfeld, mit derselben val_bpb-Metrik als Kompass, überträgt aber dem Agenten die Aufgabe, dieses Territorium auf eigene Faust zu erkunden.

Nanochat zu verstehen bedeutet zu verstehen, woran der Agent tatsächlich arbeitet und warum die in fünf Minuten autonomen Trainings erzielten Ergebnisse mit einiger Vorsicht mit denen der anspruchsvolleren Sitzungen auf dem Haupt-Leaderboard verglichen werden können.

## Was die Zahlen wirklich aussagen

Der ehrlichste Weg, autoresearch zu bewerten, besteht nicht darin, sich die Projektbeschreibung anzusehen, sondern die realen Daten der Experimente. Karpathy hat in der [Discussion #43](https://github.com/karpathy/autoresearch/discussions/43) des Repositorys einen detaillierten Bericht über eine komplette Sitzung veröffentlicht, bemerkenswert transparent: 126 Experimente, die auf einer NVIDIA H100 GPU über einen Zeitraum von etwa zehneinhalb Stunden durchgeführt wurden.

Der Ausgangspunkt war ein `val_bpb` von 0,9979. Der Endpunkt: 0,9697. Eine Verbesserung von 0,0282 in absoluten Zahlen, was in diesem Zusammenhang einen signifikanten Sprung darstellt. Zur Orientierung: Die wirkungsvollsten Änderungen waren die Reduzierung der Batch-Größe (von 524.000 auf 262.000 Token, was mehr Aktualisierungsschritte in den verfügbaren fünf Minuten ermöglichte und eine Verbesserung von 0,0119 einbrachte), das Hinzufügen einer Schicht zur Modelltiefe (0,0043) und eine Reihe von feineren Anpassungen wie die Einführung kleiner Regularisierungswerte (*weight decay*) bei den Embedding-Komponenten.

Was beim Lesen des vollständigen Protokolls auffällt, ist nicht nur das Endergebnis, sondern die Granularität des Prozesses. Der Agent untersuchte systematisch Dutzende von Hypothesen, von denen sich viele als Sackgassen herausstellten: *Weight Tying* zwischen Embedding und De-Embedding führte zu einem katastrophalen Einbruch der Metrik; Multi-Query-Attention mit einem einzigen Key-Value-Head erwies sich als zu aggressiv; Architekturen mit mehr Schichten, aber kleineren Dimensionen verbrauchten das Budget von fünf Minuten, noch bevor sie konvergierten. Diese dokumentierten Fehlschläge sind fast nützlicher als die Erfolge, da sie die Karte des erkundeten Territoriums zeichnen.

Die auf einer H100-GPU – der leistungsstärksten Grafikkarte, die derzeit für diese Art von Arbeitslasten verfügbar ist – erzielten Ergebnisse erwiesen sich später als übertragbar auf tiefere Modelle mit 24 Schichten, genug, um in den Referenz-Rankings der Branche mitzuhalten. Das ist kein triviales Ergebnis. Aber die Grenze der Übertragbarkeit ist noch unklar, und dies ist einer der Einschränkungen des Projekts, bei denen es sich lohnt, innezuhalten.
![grafico1.jpg](grafico1.jpg)
[Bild entnommen von github.com](https://github.com/karpathy/autoresearch)

## Die Kehrseite der Medaille

Autoresearch wurde enthusiastisch aufgenommen, und der Enthusiasmus ist verständlich. Aber eine ehrliche Analyse erfordert auch einen Blick darauf, wo das System seine Risse zeigt.

Die erste Einschränkung ist struktureller Natur: Das feste Budget von fünf Minuten pro Experiment, das auch eine der Stärken des Projekts ist, wird zu einer starren Einschränkung, wenn komplexere Architekturen untersucht werden. In den Daten der Sitzung #43 ist dies deutlich zu sehen: Jeder Versuch, Schichten über einen bestimmten Schwellenwert hinaus hinzuzufügen, endete mit einem unvollständigen Experiment, da die Zeit ablief, bevor das Modell konvergierte. Der Agent suchte in einem Möglichkeitsraum, der teilweise durch seine eigene zeitliche Architektur blockiert war.

Die zweite Einschränkung betrifft die Parallelität. Das System ist für eine einzelne GPU konzipiert, und Experimente werden nacheinander und nicht parallel ausgeführt. Das bedeutet, dass während ein Experiment läuft, kein anderes gestartet werden kann. Wer Zugang zu einem GPU-Cluster hat, möchte vielleicht mehrere Richtungen gleichzeitig erkunden; autoresearch unterstützt dies bewusst nicht. Karpathy ist in diesem Punkt transparent: Es ist eine Designentscheidung, kein Versehen. Die praktische Folge ist jedoch, dass die Erkundung des Forschungsraums grundlegend linear bleibt.

Dritter kritischer Punkt: Die Abhängigkeit von proprietären Modellen. Um die Experimente im autonomen Modus durchzuführen, ist ein fähiger Agent erforderlich, und in der Standardkonfiguration ist die Rede von Claude oder Codex, beides kommerzielle Systeme. Wer die Forschung im Bereich der künstlichen Intelligenz demokratisieren möchte, mag es paradox finden, dass ein Werkzeug, das darauf ausgelegt ist, die Eintrittsbarrieren zu senken, dennoch ein Abonnement für Dienste von Drittanbietern erfordert.

Es gibt auch einen subtileren Aspekt, der die Art der Entscheidungen betrifft, die der Agent trifft. Autoresearch ist exzellent bei der lokalen Optimierung: Es findet den besten Punkt in der Nähe des Ausgangspunkts durch eine Abfolge kleiner Schritte. Es ist jedoch kein System, das darauf ausgelegt ist, konzeptionelle Sprünge zu machen. Die Literaturrecherche, die Formulierung radikal neuer Hypothesen, das Verständnis dafür, warum ein Ansatz auf theoretischer Ebene funktioniert – all dies bleibt vorerst menschliches Territorium. Wahre Forschung, die Art, die Paradigmen ändert, ist nicht nur ein sequentieller Optimierungsprozess.

Schließlich gibt es die Frage der Erklärbarkeit. Wenn der Agent entdeckt, dass eine Gewichtinitialisierung, die auf das 0,68-fache des Standardwerts reduziert wurde, bessere Ergebnisse liefert, liefert er keine kausale Erklärung für diese Verbesserung. Er weiß, dass es funktioniert, nicht warum es funktioniert. Für diejenigen, die die Ergebnisse als Ausgangspunkt für nachfolgende Forschungen verwenden, ist dieser Mangel an Verständnis eine technische Schuld, die früher oder Later beglichen werden muss.

## Der Mensch, der das Programm programmiert

Eine der interessantesten und am wenigsten diskutierten Ideen von autoresearch ist die Rolle, die es dem Menschen in diesem Prozess zuweist. Es geht nicht darum, ihn zu eliminieren, sondern ihn zu verschieben.

Die Datei `program.md` wird im README als ultraleichter „Skill“ beschrieben: ein Dokument in natürlicher Sprache, das die Ziele des Agenten, seine Prioritäten und die Einschränkungen definiert, unter denen er arbeiten soll. Der Benutzer schreibt kein Python mehr, er schreibt Anweisungen. Er ändert nicht den Trainingscode, er ändert das Dokument, das dem Agenten sagt, wie er den Trainingscode ändern soll. Es ist eine zusätzliche Abstraktionsebene, und sie bringt konkrete Konsequenzen mit sich.

Einerseits senkt dies die Eintrittsschwelle enorm. Man braucht keinen Doktortitel in Machine Learning, um eine autoresearch-Sitzung zu starten. Das README enthält einen „Weekend Guide“, einen Leitfaden für das Wochenende, der verspricht, jeden von der Erstkonfiguration zu den ersten autonomen Experimenten ohne fachspezifischen Hintergrund zu führen. Die technische Einfachheit des Setups (eine einzelne NVIDIA GPU, Python 3.10 oder höher und der Paketmanager `uv`) ist real.

Andererseits schafft diese Abstraktion eine neue Abhängigkeit. Wer die Anweisungen in `program.md` schreibt, bestimmt den Erkundungsraum des Agenten. Ein schlecht geschriebenes Dokument mit vagen Zielen oder widersprüchlichen Einschränkungen führt zu ebenso vagen Forschungssitzungen. Der Flaschenhals verschiebt sich: Anstatt Kompetenzen im Schreiben von Code zu erfordern, erfordert autoresearch Kompetenzen im Schreiben effektiver Anweisungen für KI-Systeme – eine relativ neue Disziplin, der es noch an konsolidierten Standards mangelt.

Das Ganze hat etwas Rekursives, und Karpathy ist sich dessen bewusst. Im README des Projekts hat er ein bewusst mehrdeutiges Epigraph eingefügt, das eine hypothetische Zukunft beschreibt, in der Schwärme autonomer Agenten Rechencluster in einer sich ständig selbst modifizierenden Forschung verwalten, mit einer Codebasis in der zehntausendzwölften Generation, die „über das menschliche Verständnis hinausgewachsen“ ist. Es ist ein Ton zwischen dystopisch und Nerd-Scherz, aber die Tatsache, dass dieser Satz das Präsentationsdokument eines realen Projekts eröffnet, ist kein Zufall.

## Wohin dieser Weg führt

Der unmittelbarste Vergleich für autoresearch ist AutoML – Systeme, die in den letzten Jahren versucht haben, die Wahl der neuronalen Architekturen und Hyperparameter zu automatisieren. Es gibt jedoch einen wesentlichen Unterschied: Traditionelles AutoML arbeitet in vordefinierten Forschungsräumen und sucht nach der optimalen Kombination aus bereits aufgezählten Optionen. Autoresearch lässt den Agenten jeden Teil des Codes frei ändern, einschließlich Architektur, Optimierer, Batch-Größe, Lernschema – praktisch alles. Der Erkundungsraum ist viel größer und viel weniger strukturiert.

Dies eröffnet interessante Möglichkeiten, aber auch unangenehme Fragen. Wenn das System wirklich funktioniert, wenn autonome Agenten ohne kontinuierliche Aufsicht signifikante Forschung an Sprachmodellen betreiben können, wo hört dieser Prozess auf? Die ehrliche Antwort ist, dass niemand es mit Sicherheit weiß. Das Projekt ist explizit als Ausgangspunkt für etwas Größeres gedacht, und Karpathy selbst weist in Richtung asynchroner Multi-Agenten-Konfigurationen, bei denen mehrere parallele Instanzen verschiedene Richtungen auf verteilten Clustern erkunden.

Aus ethischer Sicht verdient dieses Szenario Aufmerksamkeit. Die Beschleunigung der Forschungszyklen ist wünschenswert, wenn sie zu besseren und sichereren Modellen führt. Dieselbe Beschleunigung kann jedoch, ohne angemessene Aufsicht angewendet, algorithmische Verzerrungen verstärken, die bereits in den Trainingsdaten vorhanden sind, Optimierungen hervorbringen, die messbare Metriken auf Kosten nicht messbarer Qualitäten maximieren, oder den Prozess so undurchsichtig machen, dass er sich jeder Form von sinnvoller Kontrolle entzieht.

Die Tatsache, dass autoresearch Open-Source und minimalistisch ist, ist in diesem Sinne eine teilweise Garantie. Der Code ist kurz genug, um auditiert zu werden, die Daten der Experimente sind öffentlich. Doch je mehr das System skaliert – in Richtung Multi-GPU-Cluster, längere Sitzungen, Agenten, die ihre eigenen Anweisungen verfeinern –, desto schwieriger wird die Überwachung.

Schließlich gibt es eine pragmatische Überlegung für diejenigen, die dieses Tool für den professionellen Einsatz bewerten. Autoresearch in seiner jetzigen Form ist ein raffinierter Prototyp, kein Produktionssystem. Es erfordert spezifische Hardware (NVIDIA GPU, mit optimaler Unterstützung für H100), hängt von externen APIs für den Agenten ab und liefert Ergebnisse, die kompetent interpretiert werden müssen, um nützlich zu sein. Das Versprechen des „Wochenend-Leitfadens“ gilt für diejenigen, die experimentieren wollen, ersetzt aber nicht das Grundverständnis dafür, wie das Training von Sprachmodellen funktioniert.

Dennoch bemisst sich der Wert von autoresearch nicht nur an dem, was es heute tut, sondern an dem, was es als möglich erweist. Es zeigt, dass automatisierte Forschung an realen Systemen – keine vereinfachten Simulationen, keine künstlichen Benchmarks – bereits für jeden erreichbar ist, der über eine einzelne GPU und die Neugier zum Erkunden verfügt. Und es tut dies mit einer methodischen Transparenz – der der öffentlichen Logs und des lesbaren Codes –, die sich viele gut finanzierte Forschungslabore nicht gönnen.

Der Forscher, der schläft, ist unterdessen bereits aufgewacht. Er hat 126 Experimente gefunden, die darauf warten, gelesen zu werden.
