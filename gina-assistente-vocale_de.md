---
tags: ["Generative AI", "Ethics & Society", "Applications"]
date: 2026-05-13
author: "Dario Ferrero"
---

# Alexa? Nein, Gina! Mein lokaler, selbstgebauter Sprachassistent
![gina-assistente-vocale.jpg](gina-assistente-vocale.jpg)

*Alles begann fast banal, mit jener Art von intellektuellem Juckreiz, der einen dazu treibt, Dinge zu zerlegen, um ihren Mechanismus zu verstehen. Seit Jahren leben wir mit kommerziellen Sprachassistenten: Alexa auf dem Nachttisch, Google Assistant auf dem Handy, hier und da eine Siri. Ehrlich gesagt benutze ich sie nicht, aber wenn ich andere beobachte, gab es immer dieses schwer zu ignorierende Grundgefühl – das Gefühl, dass jedes Gespräch irgendwo weit weg auf unbekannten Servern landet, die von undurchsichtigen Unternehmen verwaltet werden.*

Das ist keine Paranoia. Wie ich im Artikel ["AI Creativity & Ethics"](https://aitalk.it/it/ai-creativity-ethics.html) geschrieben habe, ist das Problem des Umgangs mit persönlichen Daten im Zeitalter der Künstlichen Intelligenz konkret und dokumentiert. Jede Anfrage, jede stimmliche Nuance, jedes „Alexa, spiel Musik“ wird zu einem Baustein eines Verhaltensprofils, dessen Erstellung ich nie zugestimmt habe.

Aus diesem Juckreiz entstand **GINA**, mein persönlicher Sprachassistent, komplett Open Source und vollständig lokal. Kein Produkt, nichts, was mit großen Ansprüchen an die Öffentlichkeit gebracht wurde: ein Lernexperiment, die Geschichte von jemandem, der verstehen wollte, wie diese Dinge wirklich funktionieren, indem er eines von Grund auf neu baute.

Es gibt jedoch einen größeren Kontext, in den sich diese Geschichte einfügt. Gerade in diesen Monaten habe ich viel über **Small Language Models** gelesen und geschrieben – jene kompakten Sprachmodelle, die auf normaler Hardware laufen, wie ich in ["Small Language Models conquisteranno il 2026?"](https://aitalk.it/it/slm-2026.html) berichtet habe. Die Vorstellung, dass Künstliche Intelligenz aufhören könnte, ein Privileg der Cloud zu sein, und zu etwas [Häuslichem, Veränderbarem, Persönlichem](https://aitalk.it/it/gemma4-26b.html) werden könnte, fasziniert mich zutiefst. GINA ist der praktische Beweis dafür, dass diese Zukunft bereits begonnen hat.

## Bevor man sich die Hände schmutzig macht: Die Ziele

Jedes Projekt braucht Grenzen, sonst wird es endlos. Bevor ich die erste Zeile Code schrieb, versuchte ich mir klarzumachen, was ich erreichen wollte.

Das Hauptziel war es, wirklich zu lernen, nicht nur von außen zuzuschauen. Ein komplexes System von Grund auf neu zu bauen, verschiedene Puzzleteile zusammenzufügen (Spracherkennung, Sprachmodelle, Sprachsynthese, Steuerung von Dateien und Anwendungen), ist der einzige Weg, um wirklich zu verstehen, wie jedes Teil funktioniert. Das zweite Ziel war es, mit SLMs in der Praxis zu experimentieren und sie nicht nur in Benchmarks zu lesen: Qwen, Mistral und Gemma auf normaler Hardware zu testen und zu sehen, was sie wirklich können. Das dritte, unverzichtbare Ziel war absolute Privatsphäre. Ein Assistent, der komplett lokal funktioniert, ohne jegliche Aufrufe externer Server, ohne dass Daten den Bereich meines PCs verlassen. Das vierte Ziel, vielleicht das pragmatischste, war es, etwas Nützliches zu erhalten: Einkaufsliste, Erinnerungen, Musik, schnelle Notizen. Nicht nur eine theoretische Übung, sondern ein Werkzeug für den täglichen Gebrauch.

## Kapitel 1 — Warum lokal? Der Wert von Privatsphäre und SLMs

### Die stille Wende der kompakten Modelle

Bis vor wenigen Jahren war die Ausführung eines Sprachmodells auf dem eigenen Computer eine abwegige Idee. Man brauchte GPU-Cluster für zehntausende Dollar, flüssigkeitsgekühlte Rechenzentren und das Energiebudget eines kleinen Industriebetriebs. Die großen Modelle, die von OpenAI, Google oder Anthropic trainiert wurden, erfordern Infrastrukturen, die eine einzelne Person niemals besitzen kann.

Doch etwas ändert sich auf stille und radikale Weise. Wie ich im Artikel über SLMs dokumentiert habe, erleben wir einen Gegentrend: Für die meisten täglichen Aufgaben braucht man keine riesigen Modelle. Ein Modell mit 7 oder 9 Milliarden Parametern, gut instruiert und optimiert, kann auf einem normalen Gaming- oder Arbeits-PC Erstaunliches leisten. Die Zahlen sind vielsagend: Microsofts Phi-3.5-Mini mit seinen 3,8 Milliarden Parametern erreicht bei mathematischen Benchmarks das Niveau von GPT-3.5 und verbraucht dabei 98 % weniger Rechenleistung. Llama 3.2 mit 3 Milliarden Parametern schlägt bei spezifischen Aufgaben nach gezieltem Fine-Tuning Modelle mit 70 Milliarden Parametern.

Es ist keine Frage mehr von „wie groß“, sondern von „wie effizient“. Es ist eine Wende, die in gewisser Weise an den Übergang vom Mainframe zum Personal Computer erinnert: Die Leistung, die das Vorrecht weniger war, wird häuslich.

### Drei Probleme kommerzieller Assistenten

Kommerzielle Sprachassistenten haben zweifellos Vorteile: Sie sind bequem, schnell und in hunderte Dienste integriert. Aber sie weisen strukturelle Grenzen auf, die für jemanden, dem seine digitale Autonomie am Herzen liegt, schwer zu akzeptieren sind.

Das erste ist die Abhängigkeit vom Internet: Ohne Verbindung kann Alexa nicht einmal „Guten Morgen“ sagen. Ihr „Gehirn“ befindet sich auf entfernten Servern, und wenn die Leitung tot ist, wird der Assistent zum Briefbeschwerer. Das zweite ist ökonomischer Natur: Viele fortgeschrittene Dienste sind mittlerweile kostenpflichtig, und die APIs der Sprachmodelle verursachen Kosten, die, wenn auch gering, vorhanden sind. Das dritte und wichtigste ist die Privatsphäre. Wenn ich mit einem kommerziellen Assistenten spreche, landen meine Worte auf Servern von Drittanbietern. Ich habe keine konkreten Garantien dafür, was aufgezeichnet wird, wie lange es aufbewahrt wird oder wie es eventuell verwendet wird. Und für die ganz Misstrauischen: dass er nicht immer zuhört.

Mit einem lokalen Assistenten verschwinden diese Probleme einfach. Die Daten bleiben auf meinem PC. Keine externen Server, keine Aufzeichnungen, kein Verhaltensprofil, das hinter meinem Rücken erstellt wird.

### Die Ausgangshardware

Bevor ich anfing, machte ich eine Bestandsaufnahme meines Arbeitsplatzes: ein AMD Ryzen 7, 32 GB RAM und eine GPU mit 16 GB VRAM. Nichts Exotisches, ein gehobener Arbeits- oder Gaming-Rechner, mehr nicht. Mit dieser Hardware kann ich bequem Modelle mit 7 bis 9 Milliarden Parametern ausführen. Ich bin bis zu den 26 Milliarden von Gemma4 gegangen und habe das Limit erreicht, ohne an Leistung zu verlieren – und für einen Sprachassistenten ist die Reaktivität entscheidend.

Das ist der Punkt, der mich an der ganzen Sache am meisten fasziniert: Man braucht keinen Supercomputer für nützliche KI. Mit Consumer-Hardware und gut konzipierten Modellen erzielt man überraschende Ergebnisse. Das ist das Versprechen der SLMs, und GINA ist der konkrete Beweis dafür.

## Kapitel 2 — Die Architektur: Wie ich mir GINA vorgestellt habe

Bevor ich eine einzige Zeile Code schrieb, entwarf ich die Systemarchitektur. Ich wollte etwas Modulares, Verständliches und leicht Erweiterbares. Die Grundidee war einfach: ein linearer Fluss, bei dem die Stimme hereinkommt, in Text umgewandelt wird, der Text von einem Sprachmodell verarbeitet wird und die Antwort laut vorgelesen wird.
![schema1.jpg](schema1.jpg)

Jede Komponente hat eine genau definierte Rolle. **Vosk** ist die Spracherkennungs-Engine, GINAs Ohren. **LM Studio** ist das Gehirn, der lokale Server, der das Sprachmodell ausführt und auf Anfragen antwortet. **pyttsx3** ist die Stimme, eine Bibliothek, die die Windows-Systemstimmen nutzt. Das **Tool Calling** ist das System, das es GINA ermöglicht, konkrete Dinge in der realen Welt zu tun, statt nur zu plaudern.

### LM Studio und die getesteten Modelle

Ich habe mich für LM Studio wegen seiner einfachen Bedienung entschieden: Man lädt ein Modell herunter, lädt es, klickt auf eine Schaltfläche und hat einen OpenAI-kompatiblen API-Server, der auf Port 8001 des PCs läuft. Die Anwendung selbst ist nicht Open Source, aber sie unterstützt alle wichtigen Open-Weight-Modelle und, was entscheidend ist, die Daten verlassen niemals den Computer. Wer eine komplett quelloffene Lösung bevorzugt, kann sie durch [Ollama](https://ollama.com/) (Apache 2.0 Lizenz) ersetzen und den Rest des Codes unverändert lassen.

Ich habe im Laufe des Projekts drei Modelle getestet, jedes mit seinen eigenen Eigenschaften. **Qwen 3.5 9B** ist für Tool Calling optimiert: Es hat eine exzellente native Unterstützung für Funktionen (in der LM-Studio-Oberfläche am Hammer-Icon erkennbar) und hat die Tool-Aufrufe fast immer korrekt verarbeitet. **Gemma 4 26B A4B** von Google verwendet eine besonders effiziente „Mixture of Experts“-Architektur: Von insgesamt 26 Milliarden Parametern aktiviert es für jede Anfrage nur 4 Milliarden, was es überraschend reaktiv macht – ich habe darüber im Detail in ["Gemma 4 26B"](https://aitalk.it/it/gemma4-26b.html) geschrieben. **Mistral Devstral Small 2** ist hingegen ein Modell mit etwa 12 Milliarden Parametern, sehr reaktiv und mit gutem allgemeinem Verständnis, und das Tool Calling erweist sich als überraschend zuverlässig. Auf einer GPU mit 16 GB VRAM laufen alle drei flüssig, mit akzeptablen Latenzen für ein Sprachgespräch.

### Die Python-Bibliotheken

Für diejenigen, die das Projekt nachbauen oder inspizieren wollen, hier die verwendeten Bibliotheken und ihre Rollen: `vosk` und `sounddevice` verwalten die Audioaufnahme und -erkennung; `numpy` arbeitet mit den rohen Audio-Arrays; `requests` führt die Aufrufe an die LM Studio API und an Telegram aus; `pyttsx3` kümmert sich um die Sprachsynthese; `queue` und `threading` verwalten asynchrone Erinnerungen; `json` macht Einkaufslisten, Notizen und Erinnerungen persistent; `re` bereinigt den Text vor dem Vorlesen von Markdown; `glob`, `random` und `subprocess` verwalten die Musikwiedergabe; `shutil` und `datetime` vervollständigen das Bild mit Backups und Zeitstempeln. Alle Open Source, alle mit einem einfachen `pip install` installierbar.
![gina-avvio.jpg](gina-avvio.jpg)
*So sieht Gina beim Start aus*

## Kapitel 3 — Die Entwicklung Schritt für Schritt: Vom Mikrofon zum Verstand

Die Entwicklung verlief in aufeinanderfolgenden Phasen, jede mit ihren unvorhersehbaren Ereignissen und Lösungen.

### Phase 1: Die Ohren

Das Erste, was zu tun war, war GINA das Hören beizubringen. Der erste Versuch erfolgte mit **Whisper** von OpenAI, dem Goldstandard für Spracherkennung. Aber fast sofort stieß ich auf ein Hindernis: Whisper benötigt `ffmpeg`, um Audio zu dekodieren, und unter Windows ist die Installation nicht trivial. Zudem war die Bibliothek `pyaudio`, die für den Mikrofonzugriff benötigt wird, noch nicht kompatibel mit Python 3.14, der neuesten Version, die ich für andere Projekte verwende.

Ich suchte also nach einer Alternative und fand **Vosk**, eine leichtgewichtige und vollständig lokale Spracherkennungs-Engine. Ihre Vorteile sind konkret: Sie benötigt kein ffmpeg, funktioniert mit `sounddevice` statt `pyaudio` (viel einfacher unter Windows zu installieren), hat ein italienisches Modell von etwa 50 MB zum kostenlosen Download und eine Latenz von etwa 200 ms auf der CPU. Der einzige Nachteil ist eine etwas geringere Genauigkeit als Whisper in lauten Umgebungen, aber für Sprachbefehle wie „Milch hinzufügen“ oder „erinnere mich daran, Mario anzurufen“ erwies es sich als völlig ausreichend.

Ich habe das Hören als **kontinuierliches Streaming** implementiert: GINA hört zu, bis sie eine Stille von mindestens 2 Sekunden erkennt, und verarbeitet dann den Satz. Dieser Ansatz ist natürlicher, als jedes Mal eine Taste drücken zu müssen.

### Phase 2: Die Verbindung zum Gehirn

Nachdem der Spracheingang gelöst war, verband ich GINA mit LM Studio. Die API ist kompatibel mit der von OpenAI, daher genügte ein einfacher `requests.post`-Aufruf an `http://localhost:8001/v1/chat/completions`. Ich habe die Konversation mit einer Historie (`messages`) strukturiert, die einen System-Prompt mit Anweisungen für GINA und die vorherigen Wechsel enthält.

Die erste unerwartete Herausforderung war die Verwaltung dieser Historie. Ohne Begrenzung wurde die Anfrage nach dutzenden Nachrichten zu groß, und LM Studio antwortete mit einem Fehler 400. Ich habe einen automatischen Reset-Mechanismus implementiert: Wenn die Historie 10 Interaktionen überschreitet, wird sie gekürzt, wobei nur der System-Prompt und die letzten Wechsel erhalten bleiben. GINA „verliert“ dadurch etwas an aktuellem Kontext, aber das Erlebnis bleibt akzeptabel.

### Phase 3: Die Stimme

Für die Sprachsynthese habe ich `pyttsx3` verwendet, das die SAPI-Stimmen von Windows nutzt. Die Qualität ist funktional, wenn auch etwas mechanisch. Das unmittelbare Problem tauchte fast sofort auf: LLM-Modelle lieben es, Antworten in Markdown zu formatieren, und `pyttsx3` las buchstäblich Sternchen, Unterstriche und Backticks vor – „Sternchen Sternchen 2 Sternchen Sternchen ist eine Primzahl“ ist nicht gerade angenehm. Ich habe eine Funktion `clean_text_for_tts()` geschrieben, die mit einigen Regex alle Markdown-Zeichen vor dem Vorlesen entfernt oder ersetzt. Jetzt liest GINA nur noch sauberen Text.
![gina-diretta.jpg](gina-diretta.jpg)
*Gina antwortet auf eine direkte Frage nach internem Wissen*

## Kapitel 4 — Das Herz des Projekts: Das Tool Calling

Das „Tool Calling“ ist die wahre Magie von GINA. Ohne es wäre sie nur ein Chatbot, der mündlich antwortet. Mit „Tool Calling“ kann sie konkrete Dinge in der realen Welt tun.

Der Mechanismus funktioniert so: Der Benutzer sagt etwas („Milch zur Einkaufsliste hinzufügen“), Vosk transkribiert den Satz in Text, der Text wird zusammen mit der Liste der verfügbaren Tools (jedes in JSON mit Name, Beschreibung und erwarteten Parametern beschrieben) an LM Studio gesendet, das Modell versteht, dass es zur Erfüllung der Anfrage `add_to_shopping_list` mit dem Parameter `item_name = "Milch"` aufrufen muss, und antwortet mit einer Tool-Call-Anfrage statt mit Text. Mein Python-Skript fängt diese Anfrage ab, führt die entsprechende Python-Funktion aus, sendet das Ergebnis zurück an das Modell, und das Modell generiert die endgültige Sprachantwort: „Ich habe Milch zur Einkaufsliste hinzugefügt.“

Das Schöne an diesem Mechanismus ist, dass er **unendlich erweiterbar** ist: Man fügt einfach eine neue Python-Funktion hinzu und beschreibt sie im JSON der Tools, und das Modell lernt, sie ohne weiteres Training zu benutzen.

### Die Einkaufsliste

Das einfachste und im Alltag nützlichste Tool ist die Verwaltung der Einkaufsliste. Drei Funktionen, `add_to_shopping_list`, `get_shopping_list`, `remove_from_shopping_list`, lesen und schreiben eine JSON-Datei mit der Liste, wobei jeder Artikel mit einem Zeitstempel und einem `checked`-Flag versehen ist. Es funktioniert genau wie erwartet, mit einer Natürlichkeit, die jedes Mal aufs Neue überrascht.
![gina-spesa.jpg](gina-spesa.jpg)
*Gina listet die Einkaufsliste auf.*

### Online-Suche (mit ausdrücklicher Zustimmung)

Es gibt eine Funktionalität, die eine gesonderte Betrachtung verdient, da sie bewusst mit dem Prinzip „alles lokal“ bricht. GINA kann über DuckDuckGo Informationen im Web suchen – Wetter, Nachrichten, aktuelle Ereignisse –, aber nur nach ausdrücklicher Zustimmung des Benutzers.

Der Grund für diese Entscheidung ist einfach: Eine Online-Suche ist der einzige Moment, in dem etwas den Bereich des PCs verlässt, und ich wollte, dass dies eine bewusste Entscheidung ist, nicht etwas, das stillschweigend und automatisch geschieht. Wenn die Anfrage Daten erfordert, die das Modell nicht haben kann (Echtzeitinformationen, aktuelle Ereignisse), bittet GINA um Bestätigung, bevor sie fortfährt.

Wenn der Benutzer zustimmt, wird die Query an DuckDuckGo gesendet, das Ergebnis wird dem Modell als zusätzlicher Kontext übergeben und die Antwort wird laut vorgelesen. Wenn der Benutzer das Internet nicht nutzen möchte, antwortet das Modell mit dem, was es weiß, oder gibt ehrlich zu, es nicht zu wissen.

Es ist ein pragmatischer Kompromiss: Privatsphäre bleibt die Regel, die Verbindung die bewusste Ausnahme.
![gina-online.jpg](gina-online.jpg)
*Gina führt nach ausdrücklicher Zustimmung eine Online-Suche zum Wetter in Rom durch.*

### Sprachnotizen

Eine weitere Funktion, die ich täglich nutze, sind Sprachnotizen. Wie oft denkt man: „Daran muss ich denken“, und vergisst es dann doch? Mit GINA sagt man einfach „notiere: morgen den Artikel auf AiTalk lesen“, und das Tool `add_note` speichert den Satz mit Zeitstempel in `notes.json`. Später kann man fragen „Lies meine Notizen vor“, und GINA listet die letzten Aufzeichnungen auf. Einfach, aber extrem nützlich.

### Zeitgesteuerte Erinnerungen

Die am komplexesten zu implementierende Funktion waren die zeitgesteuerten Erinnerungen. Das Ziel war es, sagen zu können: „Erinnere mich in 10 Minuten daran, Mario anzurufen“, und dass GINA dies tatsächlich tut, auch mitten in einem Gespräch über etwas anderes.

Die Herausforderung war technischer Natur: Das Hauptprogramm hört kontinuierlich auf das Aktivierungswort „Gina“. Hätte ich ein einfaches `time.sleep()` im Hauptthread implementiert, wäre der Assistent bis zum Ablauf des Timers blockiert gewesen und hätte auf nichts anderes antworten können. Die Lösung war die Verwendung eines separaten Threads für die Überprüfung der Erinnerungen und einer Warteschlange (`queue`), um thread-sicher mit dem Hauptthread zu kommunizieren. Ein Hintergrund-Thread prüft alle 10 Sekunden, ob es in der Datei `reminders.json` abgelaufene Erinnerungen gibt; wenn er eine findet, ruft er nicht direkt die Sprachfunktion auf (nicht thread-sicher), sondern legt den Text in eine Warteschlange; ein zweiter Thread liest kontinuierlich aus der Warteschlange und lässt GINA die Nachricht vorlesen, sobald eine eintrifft. So kann der Assistent einen daran erinnern, Mario anzurufen, selbst wenn 10 Minuten vergangen sind, ohne dass man etwas gesagt hat.
![gina-promemoria.jpg](gina-promemoria.jpg)
*Die JSON-Datei, in der Gina eine zeitliche Notiz registriert, um Sie im richtigen Moment zu benachrichtigen*

### Mediensteuerung

Für die Musik habe ich einen Ordner `Musica/` im selben Verzeichnis wie das Skript erstellt. Das Tool `search_and_play_music` sucht im Ordner nach Audiodateien mit Standardendungen, führt eine Suche nach Teilübereinstimmungen durch, wenn der Benutzer einen Namen angibt, wählt eine zufällige Datei aus, wenn der Benutzer allgemein sagt „spiel etwas Musik“, und spielt die Datei mit dem Standard-Player des Systems über `os.startfile` ab. Einfach und effektiv.

### Teilen über Telegram

Die letzte praktische Erweiterung ist das Senden der Einkaufsliste an Telegram. Bevor ich das Haus verlasse, kann ich sagen „Gina, schick mir die Liste“, und ich erhalte eine Nachricht auf einem Telegram-Bot, den ich erstellt habe (@GinaShoppingBot). Wenn ich im Supermarkt ankomme, öffne ich Telegram und habe die Liste bereit. Der Bot ist kostenlos, einfach über @BotFather zu konfigurieren, und die Persistenz ist total: Die Nachricht bleibt im Chat, bis ich sie lösche.
![gina-telegram.jpg](gina-telegram.jpg)
*Die nach spezifischer Anfrage an Telegram gesendete Nachricht mit der Liste.*

## Kapitel 5 — Das visionäre Experiment: GINA verändert ihren eigenen Code

Mit einem funktionierenden und funktionsreichen Assistenten wollte ich noch weiter gehen. Die Idee war fast schon science-fiction-haft: Was wäre, wenn GINA ihren eigenen Quellcode ändern könnte?

Das Bild ist mächtig: ein Assistent, der lernt, sich entwickelt und sich selbst verbessert. Kein statisches Programm mehr, sondern etwas in ständiger Transformation. Eher Philip K. Dick als angewandte Informatik.

### Die Implementierung

Ich habe das Tool `modify_code_file` erstellt. Der Ablauf war so: Der Benutzer sagt „Gina, ändere die Datei test.py, füge eine Funktion hinzu, die den Benutzer begrüßt“; GINA erhält die Anfrage und ruft das Tool mit dem Dateinamen und der Anweisung auf; das Tool liest die gesamte Datei, übergibt sie dem Modell zusammen mit der Änderungsanweisung als Kontext und bittet um die Generierung der neuen Version; das Modell liefert den geänderten Code zurück; das Tool speichert die neue Version im Ordner `Codice/` im Projektstamm in einer neuen Datei und lässt das Original unberührt.

Aus Sicherheitsgründen kann GINA nur Dateien im Ordner `Codice/` innerhalb des Projekts ändern, in dem sich nur vom Benutzer platzierte Dateien befinden. Der Benutzer kann das Ergebnis prüfen und das Original nur bei Zufriedenheit manuell ersetzen.

### Der Teilerfolg

Das Tool funktioniert bei kleinen Dateien perfekt. Ich habe eine `test.py` mit etwa zwanzig Zeilen erstellt, GINA gebeten, eine Funktion hinzuzufügen, und in wenigen Sekunden hatte ich `test_modificato.py` mit der gewünschten Funktion. Magie, buchstäblich.

Aber bei der Datei `gina_assistente.py` selbst, mit etwa 1000 Zeilen, zeigte das System seine Grenzen. LM Studio brauchte sehr lange für die Verarbeitung der Anfrage, lief oft in ein Timeout, und wenn die Antwort fertiggestellt wurde, war sie abgeschnitten oder fehlerhaft formatiert.

### Das technische Limit als Lektion

Das Problem ist wahrscheinlich das **Kontextfenster** der Modelle. Die Modelle, die ich verwendet habe, haben begrenzte Kontexte. Meine Datei `gina_assistente.py` überschreitet diese Schwelle bei weitem; das Modell hat nicht genug Platz, um sie vollständig zu verarbeiten und mit den Änderungen neu zu generieren. Ich muss diese Frage jedoch noch gründlich analysieren.

Dieses Scheitern ist ebenso lehrreich wie jeder Erfolg. Im Artikel über SLMs hatte ich geschrieben, dass diese Modelle wie „chirurgische Skalpelle“ sind, exzellent bei spezifischen und eingegrenzten Aufgaben, während große Modelle die „Schweizer Taschenmesser“ sind, die alles ordentlich machen. Das Tool zur Codeänderung ist der praktische Beweis: Es scheitert an einer riesigen Aufgabe (eine 1000-Zeilen-Datei ändern), brilliert aber bei kleinen, gezielten Aufgaben.

Ich habe beschlossen, das Tool eher als visionäres Experiment denn als stabile Funktion im Projekt zu behalten. Die Idee ist faszinierend, das Potenzial ist real, und in Zukunft könnte dies mit Modellen mit größerem Kontext voll praktikabel werden.
![gina-codice.jpg](gina-codice.jpg)
*Gina hat beim ersten Versuch ein perfekt funktionierendes Snake-Spiel erstellt*

## Kapitel 6 — Inkonsistenzen der Modelle: Leben mit Nicht-Determinismus

Kein komplexes Projekt ist frei von Unvollkommenheiten. GINA hat ihre eigenen, und es lohnt sich, darüber zu berichten.

### Das Problem mit dem Delay

Eine der ersten Schwierigkeiten war die Verzögerung zwischen dem Aktivierungswort und dem tatsächlichen Hören des Befehls. Der ursprüngliche Ablauf sah vor, dass GINA nach dem Hören des Wortes „Gina“ mit „Ja?“ antwortete und dann anfing zuzuhören. Da die Sprachantwort jedoch etwa eine Sekunde dauerte, gingen die ersten Worte des Befehls systematisch verloren. Ich versuchte, den Beginn des Zuhörens vor die Sprachantwort zu legen, aber Gina hörte sich am Ende selbst zu und aktivierte sich. Momentan habe ich die kurze Wartezeit akzeptiert, bevor ich sprechen kann, hoffe aber, eine Lösung zu finden.

### Vosk: Präzise, aber nicht unfehlbar

Vosk ist in ruhigen Umgebungen exzellent. Bei Hintergrundgeräuschen sinkt die Genauigkeit. Das ist ein bekanntes und für ein persönliches Projekt akzeptables Problem. Für eine professionelle Anwendung bräuchte man ein dediziertes System wie Porcupine, aber für meine täglichen Anwendungen leistet Vosk voll und ganz seine Arbeit.

### Die nicht-deterministische Natur von LLMs

Dies ist vielleicht die faszinierendste und manchmal frustrierendste Eigenschaft von Sprachmodellen: Sie sind nicht deterministisch. Bei gleichem Input können sie unterschiedliche Antworten geben.

Ein konkretes Beispiel: Wenn ich sage „Gina, spiel etwas Musik“, ruft das Modell manchmal korrekt das Tool `search_and_play_music` auf und spielt ein Stück „nach seiner Wahl“ aus dem Ordner `Musica/`. Ein anderes Mal antwortet es: „Hier ist ein perfektes Stück für diesen Moment: Bohemian Rhapsody von Queen.“ Und dann wird natürlich nichts abgespielt, weil die Datei nicht existiert. Das ist kein Bug, sondern das Modell hat aus Milliarden von Texten gelernt, dass auf „spiel etwas Musik“ oft ein Musikvorschlag folgt, und wählt manchmal diesen Weg, statt das Tool aufzurufen.

Ebenso funktioniert die Wettersuche manchmal korrekt, ein anderes Mal antwortet das Modell: „Für präzise Wetterinformationen empfehle ich dir, eine spezialisierte Website zu konsultieren.“ Diese Variabilität ist normal und muss akzeptiert werden. Es ist der Preis für ein kreatives und nicht starr deterministisches System, und letztlich ist es auch das, was die Interaktion menschlicher macht, im Guten wie im Schlechten.

Beide Probleme könnten durch eine Verfeinerung des System-Prompts gemildert werden; das ist ein Aspekt, an dem noch zu arbeiten ist.

## Kapitel 7 — Fazit: Was funktioniert, was fehlt, wohin es geht

Das Projekt ist über meine ursprünglichen Erwartungen hinaus gelungen. GINA funktioniert, ist stabil und ich benutze sie täglich. Sie startet mit einem Doppelklick auf eine `.bat`-Datei auf dem Desktop und ist in wenigen Sekunden bereit.

### Was sie heute kann

Mit GINA kann ich die Einkaufsliste verwalten (Artikel hinzufügen, anzeigen, entfernen) und sie vor dem Ausgehen an Telegram senden. Ich kann Notizen und zeitunabhängige Erinnerungen aufzeichnen. Ich kann zeitgesteuerte Erinnerungen setzen („erinnere mich in 10 Minuten daran, Mario anzurufen“), und GINA hält diese auch mitten in anderen Gesprächen ein. Ich kann Musik aus meinem lokalen Ordner abspielen, sowohl spezifische Lieder als auch zufällig gewählte Stücke. Ich kann allgemeine Fragen unter Nutzung des internen Wissens des Modells stellen. Ich kann nach ausdrücklicher Zustimmung Online-Suchen durchführen. Ich kann GINA bei kleinen Dateien bitten, Code zu ändern. All das, ohne dass ein einziges Bit meinen PC verlässt.

### Wo noch gearbeitet werden muss

Selbstkritik gehört zur Methode. Die Sprachqualität von `pyttsx3` ist funktional, aber metallisch: Man könnte zu Piper TTS (lokal, viel höhere Qualität) oder Edge TTS (online, exzellente Qualität) wechseln. Die Präzision des Aktivierungswortes könnte durch Porcupine verbessert werden. Die Spracherkennung könnte mit Whisper präziser sein, auf Kosten einiger zusätzlicher Abhängigkeiten. Die Schnittstelle ist heute nur eine Kommandozeile: Eine einfache Weboberfläche in Streamlit oder Flask würde sie zugänglicher machen. Und die Änderung großer Dateien bleibt ein offenes technisches Limit.

### Eine Welt voller Möglichkeiten

Was ich an GINA am meisten liebe, ist, dass sie unendlich erweitert werden kann. Einige Ideen auf meiner Liste: eine Weboberfläche, um Einkaufsliste, Notizen und Erinnerungen auch aus der Ferne zu sehen; Integration mit dem Kalender („Gina, welche Termine habe ich morgen?“); Steuerung von Smart-Home-Geräten.

Aber das Wichtigste ist das, was dieses Projekt auf einer breiteren Ebene zeigt. GINA ist nicht nur ein persönlicher Sprachassistent: Sie ist eine **Demonstrationsplattform** für das Potenzial von lokal betriebenen Small Language Models. Sie beweist, dass man sich nicht auf die Cloud-Giganten verlassen muss, um nützliche, persönliche und privatsphärefreundliche Künstliche Intelligenz zu haben.

Der Trend, den ich in ["Small Language Models per il 2026"](https://aitalk.it/it/slm-2026.html) beschrieben habe, ist bereits Realität und zum Greifen nah. Mit Modellen wie Qwen, Gemma 4 und Mistral kann ein normaler Gaming-PC einen hochentwickelten Sprachassistenten ausführen, mit Latenzen von unter einer Sekunde, ohne übermäßige Ressourcen zu verbrauchen.

Und das Beste ist, dass all dies **Open Source** ist: veränderbar, verbesserbar, anpassbar an jeden Bedarf. Ich habe beim Bau dieses Projekts enorm viel gelernt und die Bestätigung erhalten, dass Künstliche Intelligenz nicht nur aus ChatGPT und kostenpflichtigen APIs besteht. Sie besteht auch aus Neugier, Experimentierfreude und dem Vergnügen, am Computer zu sitzen, Code zu schreiben und zu sehen, wie etwas, das man selbst gebaut hat, zum Leben erwacht und einem antwortet.

Ich hoffe, dass dieser Bericht jemanden dazu inspiriert, eine experimentelle Reise anzutreten. Und wenn er es tut, wartet GINA auf ihn, bereit, sein erstes Wort zu hören.

*„Gina“*

---

## Technischer Anhang: Wie man beginnt

Der gesamte Code ist im [GitHub-Repository](https://github.com/Dario-Fe/Gina-Assistant) verfügbar. Das Hauptskript ist `gina_assistant.py`; die Speicherdateien für die verschiedenen Tools (`shopping_list.json`, `notes.json`, `reminders.json`) werden beim ersten Start automatisch erstellt. Der Ordner `Musica/` und der Ordner `Codice/` sind optional. Wenn Sie GINA zum Musikhören oder zum Codeschreiben verwenden möchten, erstellen Sie die Ordner im Projektstamm und legen Sie Ihre Lieblingslieder oder Dateien mit Code zum Ändern oder zum Neuerstellen darin ab.

Um GINA zu starten:
![schema2.jpg](schema2.jpg)
