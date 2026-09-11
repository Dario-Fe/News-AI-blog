---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-09-11
author: "Dario Ferrero"
---

# Leitfaden zu Inferenz-Engines und Clients für lokale LLMs
![guida-motori-inferenza-locale.jpg](guida-motori-inferenza-locale.jpg)

*Es gibt einen genauen Moment, in dem eine Technologie aufhört, ein Versprechen zu sein, und zum Werkzeug wird. Es ist nicht der Moment, in dem die Pressemitteilung erscheint, und auch nicht der, in dem Benchmarks in den sozialen Medien die Runde machen, sondern der, in dem sich eine ganz normale Person mit einem ganz normalen PC hinsetzt, etwas herunterlädt und beschließt, wirklich zu verstehen, was vor sich geht. Im Jahr 2026 ist dieser Moment mit aller Macht für die lokale Inferenz gekommen, und mit ihm hat sich ein Problem aufgetan, das vorher kaum jemand klar erklärt hatte, bevor man verwirrt vor der Befehlszeile stand: Es fehlt nicht mehr am Modell, es fehlt an Klarheit darüber, *wie* man es ausführt.*

Der Grund dafür ist einfach, wird aber unterschätzt. Wie aus dem [Currents-Bericht von DigitalOcean](https://www.digitalocean.com/currents/february-2026) hervorgeht, integrieren heute 64 % der Unternehmen Modelle über APIs von Drittanbietern, während sich nur 15 % hauptsächlich dem Training von Modellen von Grund auf widmen: Der Großteil der Arbeit besteht kurz gesagt mittlerweile mehr aus Integration als aus Entwicklung. Die Cloud ist nicht tot, sie ist nach wie vor dominant, aber was wie eine unüberwindbare Asymmetrie zwischen riesigen proprietären Modellen und lokalen „Behelfsmodellen“ aussah, schrumpft mit einer Geschwindigkeit, die selbst aufmerksame Beobachter überrascht. Qwen3.5-9B mit etwa dreizehnmal weniger Parametern als einige Cloud-Giganten erzielt beim GPQA-Diamond-Benchmark – dem Referenztest für fortgeschrittenes Denken auf universitärem Niveau – ein Ergebnis von 81.7 gegenüber 80.1 bei GPT-OSS-120B von OpenAI, wie auf der [offiziellen Modellseite auf Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B) berichtet wird. Der Abstand ist minimal, kein tiefes Abgrund, aber der Kernpunkt bleibt: Ein enorm kleineres Modell hält mit einem sehr viel größeren mit – und das ist ein Paradigmenwechsel bei der Frage, was im Jahr 2026 „klein“ bedeutet.

Doch mit der Demokratisierung der Hardware ist auch ein neues Labyrinth entstanden: Wenn Sie ein Open-Weight-Modell herunterladen und auf Ihren PC stellen, was nutzen Sie, um es auszuführen? Die Antwort hängt von einer Unterscheidung ab, die vorher kaum jemand erklärt und die fast das gesamte Ökosystem strukturiert: dem Unterschied zwischen der Inferenz-**Engine** und dem **Client**, der diese Engine umschließt.

Bevor wir fortfahren, muss klar sein, was dieser Artikel ist und was er nicht ist. Was folgt, ist eine Analyse von Eigenschaften und technischen Spezifikationen, aufgebaut auf offizieller Dokumentation, Repositories, Changelogs und Gegenprüfungen zwischen verlässlichen Quellen. Es ist kein wissenschaftlicher Benchmark, es gibt kein peer-reviewed Testprotokoll und keine statistisch signifikante Stichprobe. Ich habe auf realer Hardware nur zwei Produkte aus dieser Übersicht getestet und führe sie als Anschauung an, nicht als tragende Struktur. Wer zertifizierte Zahlen sucht, findet die Benchmarks auf den offiziellen Seiten des jeweiligen Produkts. Wer verstehen möchte, was diese Werkzeuge zu leisten versprechen und mit welcher Hardware, liest weiter.

Die Wahrheit liegt, wie so oft in diesem Bereich, nicht in einer Tabelle. Sie liegt darin zu verstehen, was jedes Werkzeug wirklich tut und was es Ihnen im Gegenzug abverlangt.

## Der Motor und das Auto

Um ein Sprachmodell lokal auszuführen, braucht man zwei Dinge: das Modell selbst – eine Datei von einigen Gigabyte – und etwas, das als Übersetzer zwischen der Hardware und dem Modell fungiert und Speicher, Tokenisierung sowie Inferenz verwaltet. Ohne diese Zwischenschicht ist das Herunterladen der Modellgewichte so, als hätte man die Dateien eines Films ohne Videoplayer. Und genau hier öffnet sich die Trennung, die fast das gesamte Ökosystem teilt.

Auf der einen Seite stehen die **Inferenz-Engines**, auch Runtimes genannt. Das sind Low-Level-Bibliotheken und Server, oft headless, die direkt das Laden des Modells, das Scheduling von Anfragen, die Nutzung von CPU und GPU, Quantisierungen und die verschiedenen Gewichtsformate verwalten. Sie haben fast nie eine echte grafische Benutzeroberfläche, kommunizieren über APIs, und ihr Erfolg misst sich in Durchsatz und Latenz. Die Zielgruppe ist der Entwickler, der MLOps-Spezialist, jemand, der ein Modell für Dutzende von Benutzern bereitstellen muss. Sie sind der bloße Motor eines Autos – das, was man sieht, wenn jemand die Motorhaube öffnet, um ihn vorzuführen.

Auf der anderen Seite stehen die **Clients**, die Runner oder Endanwender-Produkte. Das sind einsatzbereite Anwendungen, die eine oder mehrere Engines aufgreifen und mit etwas Nutzbarem umhüllen: einem Modell-Browser, einem Chat, einem bereits konfigurierten API-Server, manchmal Plugins für Web-Suche, RAG auf eigenen Dokumenten oder sogar Agenten. Sie verlangen von Ihnen nicht, irgendetwas zu konfigurieren, aber im Gegenzug wissen Sie nicht immer, was im Inneren passiert. Die Auto-Metapher ist hier sehr treffend: Der Client gibt Ihnen Klimaanlage, Navi und Einparksensoren. Sie verzichten darauf, die Bremskraftverteilung manuell einzustellen, kommen aber trotzdem ans Ziel.

Die Frage, die sich durch den gesamten Artikel zieht, lautet nicht „wie viel Kontrolle gebe ich ab“, sondern „mit welcher Hardware gelingt es mir, das auszuführen, was versprochen wird“. Das verlagert den Schwerpunkt vom Softwarebereich auf die Hardware, und genau dort liegt der reale Unterschied zwischen den beiden Welten. Eine Engine, die für die H100 eines Rechenzentrums optimiert ist, und ein Client, der für das heimische MacBook konzipiert wurde, sprechen verschiedene Sprachen; zu wissen, was wofür dient, ist die halbe Miete.

Meine reale Erfahrung berührt nur zwei Punkte dieser Karte, und ich nenne sie als Anschauung, nicht als Gerüst: LM Studio und Unsloth Studio auf einer Radeon RX 9060 XT mit 16 GB VRAM – dieselbe Konfiguration, die viele fortgeschrittene Anwender, Gamer, Content Creator oder Entwickler im Homeoffice als die ihre wiedererkennen würden. Hardware der gehobenen Mittelklasse für Consumer, aber weit entfernt von der A100, die man sich vorstellt, wenn von lokaler Inferenz die Rede ist. Der Rest ist aufmerksames Lesen der Dokumentation, keine Praxiserprobung.
![schema1.jpg](schema1.jpg)

## Die Engines

### llama.cpp

[llama.cpp](https://github.com/ggml-org/llama.cpp) ist der Grund, warum fast alles läuft. Diese C/C++-Bibliothek ist der stille Motor hinter den meisten Clients, die der breiten Öffentlichkeit bekannt sind: Ollama, LM Studio, Jan, GPT4All und KoboldCPP stützen sich alle in unterschiedlichem Maße auf ihren Kern. Ihre Stärke ist die extreme Portabilität: Sie läuft auf CPU, auf NVIDIA-GPUs mit CUDA, auf AMD mit HIP, auf Intel-Karten mit Vulkan und SYCL sowie auf dem Metal von Apple Silicon – alles im selben Paket. Es ist kein Zufall, dass das GGUF-Format – quantisierte, in sich geschlossene und architekturunspezifische Gewichte – zum De-facto-Standard für lokale Modelle geworden ist: llama.cpp ist dessen Referenzimplementierung.

Die Kehrseite ist dieselbe wie die ihrer Allgegenwart: Es ist „für Entwickler“ konfiguriert, mit feiner Kontrolle, aber wenig auf Multi-User-Serving ausgerichtet. Wenn Sie ein Modell auf Ihrem Laptop ausführen möchten, um mit GGUF-Quantisierungen zu experimentieren, ist es wahrscheinlich die absolut beste Wahl. Wenn Sie dieses Modell einem ganzen Team mit stabilen APIs bereitstellen müssen, ist es zwar die Engine, aber nicht das fertige Produkt.

### vLLM

Wenn llama.cpp der Motor für Heimwerker ist, ist [vLLM](https://vllm.ai/) der Rennmotor für die Produktion. Von Forschern an der UC Berkeley entwickelt, ist es zum De-facto-Standard für Serving mit hohem Durchsatz geworden, und seine Revolution heißt PagedAttention: Anstatt den KV-Cache-Speicher als einen einzigen, verschwendeten Block zu behandeln, verwaltet es ihn wie den virtuellen Speicher eines Betriebssystems – seitenweise, mit Copy-on-Write und der gemeinsamen Nutzung von Präfixen zwischen ähnlichen Anfragen. Im ursprünglichen Paper des Projekts nutzten frühere Systeme nur 20 bis 40 % des verfügbaren KV-Cache-Speichers; mit PagedAttention steigt die Ausnutzung auf etwa 96 %, was bei gleicher Latenz einen 2- bis 4-mal höheren Durchsatz im Vergleich zu naivem Batching ermöglicht.

Allerdings bewegt sich vLLM auf dem Terrain von NVIDIA-GPUs. CUDA ist sein Zuhause, und die AMD-Unterstützung über HIP wächst zwar, bleibt aber ein auf Rechenzentren ausgerichtetes Werkzeug, das für Laptops und CPUs weniger geeignet ist. Die Einrichtung ist komplexer und die Philosophie klar: Serving für Teams und Unternehmen, API-Backend für Anwendungen, parallele Arbeitslasten. Wenn Ihr Ziel darin besteht, Dutzende von Benutzern mit demselben Modell sprechen zu lassen, ist vLLM wahrscheinlich das Erste, was Sie sich ansehen werden.

### SGLang

[SGLang](https://github.com/sgl-project/sglang) macht etwas Anderes und Spezifischeres: Es ist für Modelle optimiert, die nicht nur antworten, sondern in Graphen denken. Agenten, die mehrere Schritte ausführen, Tool-Use, fortgeschrittenes RAG, Workflows für „Deep Research“, bei denen das Modell externe Werkzeuge aufruft und Generierungen verkettet. Seine Stärke liegt in der gemeinsamen Entwicklung des sprachlichen Frontends mit der Runtime, um nicht-triviale Dekodierungsmuster effizient zu verwalten.

Es ist weniger ein Standardprodukt als vLLM oder llama.cpp, und die Dokumentation wirkt noch etwas nach Early Adoptern. Aber wenn Ihr Ziel lokale Multi-Step-Agenten oder das Prototyping von Agenten-Workflows sind, ist SGLang eines der vielversprechendsten Werkzeuge des Jahres 2026 mit schneller Unterstützung für fortgeschrittene Modelle wie gpt-oss.

### TGI

[Text Generation Inference](https://huggingface.co/docs/text-generation-inference) von Hugging Face ist ein Veteran in der Übergangsphase. Jahrelang war es der Referenz-Inferenzserver für das Hosten von Hugging-Face-Modellen in der Produktion – mit optimierten Kerneln in Rust und Python, Reife, solider Dokumentation und direkter Integration in den HF Hub. Doch am 11. Dezember 2025 hat Hugging Face TGI in den Wartungsmodus versetzt: keine neuen Modelle, keine neuen Funktionen oder Optimierungen mehr, und Hugging Face verweist diejenigen, die neue Deployments planen, explizit auf vLLM und SGLang. Das Repository akzeptiert nur noch Bugfixes und Verbesserungen an der Dokumentation.

Es ist nicht tot, es funktioniert weiterhin, aber für ein neues Projekt ist es eine Entscheidung, die man bewusst treffen sollte: Sie können es noch nutzen, aber es ist nicht mehr die Zukunft, die Hugging Face baut. Es ist der klassische Fall, in dem das beste Werkzeug von gestern zu einer Altlast wird, die man verwalten muss – ähnlich wie bestimmte COBOL-Mainframes, die niemand mehr anfassen möchte, die aber auch niemand abschalten kann.

### TensorRT-LLM

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) ist der Stack von NVIDIA für die optimierte Inferenz auf seinen modernsten GPUs, von den H100 und L40S über die A100 bis hin zu den neuesten Serien. Seine Stärke ist die maximale Performance auf NVIDIA-Hardware mit direkter Integration in den Triton Inference Server, um von einer einzelnen GPU über Kubernetes auf ganze Cluster zu skalieren. Es ist das Werkzeug für diejenigen, die bereits über die Infrastruktur verfügen und das Maximum daraus herausholen wollen.

Die Kehrseite ist das Lock-in: TensorRT-LLM steht und fällt mit NVIDIA, hat eine steile Lernkurve und ist für den durchschnittlichen Verbraucher irrelevant. Wenn Sie in einem Rechenzentrum mit NVIDIA-GPUs arbeiten und die Arbeitslast kritisch in Bezug auf Latenz und Durchsatz ist, ist es wahrscheinlich die Spitze. Ansonsten ist es eine Welt weit entfernt von Ihrem Desktop.

### MLX

[MLX](https://mlx.ai/) ist das Framework von Apple für maschinelles Lernen auf Apple Silicon, und seine Stärke ist die unifizierte Speichernutzung. Auf einem Mac mit M1-, M2-, M3- oder neueren Chips teilen sich CPU und GPU denselben RAM-Pool, und MLX nutzt dies für Zero-Copy-Inferenz, die keine llama.cpp-Portierung an Effizienz erreichen kann. Das ist der Grund, warum ein MacBook Modelle ausführen kann, bei denen vergleichbare PCs ins Straucheln geraten.

Die Einschränkung ist offensichtlich: MLX steht und fällt mit macOS und Apple Silicon und ist weniger plattformübergreifend. Aber wenn Sie einen MacBook oder Mac mini haben, ist es wahrscheinlich die natürlichste Engine für die lokale Inferenz, und immer mehr Runner und Apps stützen sich darauf als natives Backend für das Apple-Ökosystem.

## Die Autos

### Ollama

[Ollama](https://ollama.com/) ist das Werkzeug für diejenigen, die Einfachheit suchen. Es lässt sich mit einem einzigen Befehl installieren, stellt standardmäßig eine OpenAI-kompatible REST-API auf `localhost:11434` bereit und fügt sich nahtlos in Skripte, Pipelines und Anwendungen ein. Es ist Open Source, hat eine große Community, und seine minimalistische Philosophie – ein Befehl zum Herunterladen und einer zum Ausführen – macht es zum bevorzugten Backend von Dutzenden von Drittanbieter-Anwendungen. In Bezug auf die reine Performance ist es in der Regel schneller, verwaltet parallele Anfragen besser und verbraucht aufgrund des fehlenden grafischen Overheads weniger Ressourcen.

Die Kehrseite der Medaille ist die erforderliche Vertrautheit mit dem Terminal, die erweiterte Konfiguration über Modelfiles und eine native GUI, die spät kam und minimal geblieben ist. Es gibt auch eine Frage der Transparenz, die erwähnenswert ist: Da Ollama Open Source ist, kann der Code von jedem eingesehen werden – was bei Konkurrenten mit proprietärer GUI nicht immer der Fall ist. Für die lokale Entwicklung von Apps mit LLMs, die persönliche Nutzung über das Terminal oder per API sowie schnelles Prototyping bleibt Ollama ein Pfeiler.

### LM Studio

[LM Studio](https://lmstudio.ai/) spielt auf einem anderen Feld. Es ist eine Desktop-Anwendung mit einer gepflegten grafischen Benutzeroberfläche, verfügbar für Windows, macOS und Linux, und seine Stärke liegt darin, die Hürden abzubauen, die die meisten Menschen davon abhalten, sich lokaler KI zu nähern. Es ermöglicht das Suchen, Herunterladen und Laden von Modellen, ohne ein Terminal zu öffnen, stellt ebenfalls eine OpenAI-kompatible API bereit und verwaltet automatisch die GPU-Beschleunigung auf NVIDIA, Apple Silicon und AMD.

Aber das Detail, das die Erfahrung für jemanden ohne Entwicklerhintergrund wirklich verändert, ist folgendes: Bei der Auswahl eines Modells zeigt LM Studio in Echtzeit eine Schätzung der erwarteten Performance auf der eigenen Hardwarekonfiguration an – mit farbigen Indikatoren (Grün, Gelb, Rot), die sofort vermitteln, ob das Modell flüssig, mit Einschränkungen läuft oder ob die Hardware unzureichend ist. Für einen Privatanwender, der experimentiert, ist diese beseitigte Hürde den eventuellen Performance-Abstand zu Ollama wert.

Das ist nicht theoretisch, ich habe es funktionieren sehen. In meiner Konfiguration mit der Radeon RX 9060 XT mit 16 GB war es genau der grüne Indikator von LM Studio, der mir bestätigte, dass Qwen 3.5 9B in Q8_0 vollständig auf der GPU laufen würde, ohne Layer auf den System-RAM verteilen zu müssen. Ich habe das Modell im Voraus ausgewählt, ohne manuelle Berechnungen oder das Lesen technischer Dokumentation. Ein Detail, das übersetzt bedeutet, nicht erst nach dem Herunterladen von zehn Gigabyte festzustellen, dass man das falsche Modell gewählt hat.

LM Studio ist Closed Source, eine kostenlose, aber nicht transparente Binärdatei, und einige webbezogene Funktionen sind standardmäßig nicht aktiv. Aber für lokalen Chat mit GUI, das Experimentieren mit GGUF und eine lokale API ist es wahrscheinlich der beste Startpunkt für diejenigen, die nicht wissen wollen, was unter der Haube passiert.

### Jan

[Jan](https://jan.ai/) ist die Open-Source-Alternative, die auf Datenschutz und Self-Hosting setzt, ohne die Benutzerfreundlichkeit zu opfern. Es verfügt über eine saubere Desktop-GUI, unterstützt mehrere Backends, darunter llama.cpp, stellt eine lokale API auf einem dedizierten Port bereit und präsentiert sich als eine echt offene Alternative zu ChatGPT. Seine Stärke ist die Balance: Open Source, wie es LM Studio nicht ist, mit einer UX, die Ollama fehlt.

Die Einschränkung ist ein weniger gepflegtes Modell-Ökosystem und eine geringere Verbreitung, was sich in weniger Dokumentation und weniger Community-Unterstützung niederschlägt. Für diejenigen, die Open Source und eine GUI ohne allzu viele Komplikationen wollen, verdient Jan einen Platz im Test.

### Unsloth Studio

[Unsloth Studio](https://unsloth.ai/) ist das Produkt, das dem am nächsten kommt, was ein lokaler „agentischer“ Assistent sein sollte. *Eine nützliche Präzisierung: Derzeit gibt es zwei Zugänge zum selben Ökosystem: Unsloth Studio, die Oberfläche, die im Browser läuft und zum Zeitpunkt des Schreibens noch als Beta gekennzeichnet ist, und Unsloth Desktop, die neuere native App für Windows, macOS und Linux. Die grundlegenden Funktionen sind dieselben, nur der Container ändert sich.* Es ist nicht nur ein Runner: Es ist eine Umgebung, die native Web-Suche, Deep Research, RAG auf lokalen Dokumenten, Code-Ausführung, persönliche Wissensdatenbanken und sogar geführtes QLoRA-Fine-Tuning integriert, ohne ein Terminal anzufassen. Die zugrundeliegende Engine ist llama.cpp für GGUFs, mit Trainingskomponenten, die es zu einem Hybridwerkzeug zwischen Inferenz und Training machen.

Die Zielgruppe ist präzise: Creators, Forscher, diejenigen, die Artikel oder Berichte schreiben und möchten, dass das Modell nach Quellen sucht, Seiten liest und zitierte Entwürfe erstellt. Die integrierte Web-Suche und das Deep Research – das einen Plan erstellt, glaubwürdige Referenzen findet und einen Bericht mit Zitaten generiert – unterscheiden es von den meisten Konkurrenten. Die Kehrseite ist, dass es sich noch in rasanter Entwicklung befindet, als „reiner“ Runner im Vergleich zu Ollama oder LM Studio weniger ausgereift ist und einige Funktionen noch eine gewisse Instabilität aufweisen können, passend zum Beta-Label, das es noch trägt. Aber wenn Ihr Ziel darin besteht, mit Quellen zu schreiben, ist es wahrscheinlich das vielversprechendste Werkzeug der Gruppe.

Auch hier hat die direkte Erfahrung Gewicht. Beim Test mit Unsloth Studio auf meiner RX 9060 XT zeigte die Fähigkeit, das Modell während meiner Arbeit nach Webseiten suchen zu lassen und Deep Research zur Erstellung zitierter Berichte zu nutzen, was es bedeutet, eine einsatzbereite agentische Umgebung zu haben, ohne sechs verschiedene Komponenten zusammenbauen zu müssen. Es ist kein Runner, es ist ein Labor.

### LocalAI

[LocalAI](https://localai.io/) macht eine elegante Sache: Es setzt als einheitliche Abstraktion über mehrere Backends an. Wenn Sie llama.cpp, vLLM, MLX haben und eine kohärente OpenAI-kompatible API wollen, die mit allen spricht, ohne dass Sie sich merken müssen, welchen Befehl Sie für welche Engine starten müssen, ist LocalAI die Lösung. Es unterstützt mehrere Modelle gleichzeitig, und seine Philosophie lautet „eine Installation, viele Engines“, ohne zu einem riesigen Download zu werden, da jedes Backend erst aktiviert wird, wenn ein Modell es anfordert.

Die Einschränkung besteht darin, dass es eher infrastruktur- als desktopfreundlich ist: Es ist nicht das Werkzeug zum Chatten, sondern dasjenige zum Aufbau eines unifizierten Backends in heterogenen Umgebungen. Für Self-Hosting-Server und Apps, die mehrere Engines nutzen, ist es eine solide Wahl.

### Open WebUI

[Open WebUI](https://openwebui.com/) ist das, was viele Menschen suchen, ohne es zu wissen: ein „Self-Hosted ChatGPT“ für ihr Team. Es stützt sich über APIs auf Ollama, vLLM oder andere Engines, fügt aber alles hinzu, was einer gemeinsamen Plattform fehlt: Multi-User-Chat, integriertes RAG, Web-Suche über SearXNG oder Anbieter wie Brave, Benutzerverwaltung, Workspaces, Agenten. Die Oberfläche ist modern und die Flexibilität hoch.

Der Preis ist das Deployment: Es erfordert Docker und ein Minimum an Serverkonfiguration, ist also kein „Herunterladen und Nutzen“. Wenn Sie jedoch eine gemeinsame Plattform für ein Team mit RAG und Web-Suche suchen, ist Open WebUI an dieser Front wahrscheinlich das beste Ergebnis des Jahres 2026.

### GPT4All

[GPT4All](https://gpt4all.io/) war jahrelang für viele der erste Kontakt mit der Idee eines LLMs auf dem eigenen Computer: denkbar einfache Oberfläche, keinerlei Konfiguration, Modelle mit einem Klick herunterladbar. Das Problem – und es ist fair, das klar zu sagen – ist, dass die aktive Entwicklung gestoppt wurde: keine Commits im Repository seit Mai 2025, keine Releases seit Februar 2025. Die App funktioniert weiterhin, öffnet sich und chattet reibungslos, erhält aber keine Updates, neuen Modelle oder Sicherheitskorrekturen mehr. Es sollte eher als historischer Einstiegspunkt denn als empfohlene Wahl für 2026 betrachtet werden: Wer heute dieselbe Einfachheit sucht, findet bei Jan oder Ollama besser gepflegte Alternativen.

### KoboldCPP

[KoboldCPP](https://koboldcpp.com/) entstammt dem KoboldAI-Ökosystem und richtet sich an ein spezifisches Publikum: diejenigen, die lange Belletristik, Rollenspiele oder unterstützt Geschichten schreiben. Auf einer auf llama.cpp basierenden Engine baut es ein Set von Generierungsoptionen, Presets und Bearbeitungswerkzeugen auf, die für kreativen Text konzipiert sind – Dinge wie das Verwalten des narrativen Gedächtnisses oder World Info, die andere Clients gar nicht erst anbieten. Es ist eine einzelne, leichte ausführbare Datei, gedacht für diejenigen, die eher aus der Welt der Textspiele als aus der Softwareentwicklung kommen.

Die Einschränkung liegt in der Spezialisierung selbst: Außerhalb des Bereichs des kreativen Schreibens ist KoboldCPP für die allgemeine Nutzung weniger komfortabel als LM Studio oder Ollama, und seine Oberfläche wirkt, obwohl funktional, wie ein von Enthusiasten für Enthusiasten gebautes Werkzeug, nicht von einem Produktteam.

### Text Generation WebUI

[Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) ist das Schweizer Taschenmesser des lokalen Experimentierens. Eine lokal installierbare Web-Oberfläche, Unterstützung für mehrere Backends, ein Erweiterungssystem, mit dem sich praktisch alles hinzufügen lässt – von RAG über TTS bis hin zu fortgeschrittenen Sampling-Konfigurationen, die andere Clients aus Gründen der Einfachheit bewusst verbergen. Es ist das Werkzeug für diejenigen, die selbst an jedem Parameter drehen wollen.

Die Kehrseite ist die Lernkurve: Die Oberfläche zeigt alles, was auch bedeutet, dass sie demjenigen zu viel zeigt, der nur chatten möchte. Es ist nicht für den gelegentlichen Nutzer gedacht, sondern für diejenigen, die lokale Inferenz als dauerhaftes Labor betrachten.
![tabella1.jpg](tabella1.jpg)

## Was Sie wählen sollten – je nachdem, was Sie wirklich wollen

Die richtige Wahl hängt davon ab, was Sie erreichen wollen, und keine universelle Rangliste kann Ihren Kontext ersetzen. Aber einige Szenarien führen fast immer zu denselben Antworten.

Sie wollen nur lokal auf Ihrem PC chatten, ohne etwas zu konfigurieren. Hier gewinnen LM Studio für die UX oder Jan, wenn Sie etwas vollständig Quelloffenes suchen, mit Ollama als Alternative, wenn Sie mit der CLI gut zurechtkommen. Wenn Sie LM Studio auf Ihrer Konfiguration ausprobiert haben und der grüne Indikator aufgeleuchtet ist, gibt es keinen Grund, das Rad neu zu erfinden.

Sie müssen ein Modell mehreren Benutzern im Unternehmen mit einer stabilen API bereitstellen. Hier ist das Terrain der Engines: vLLM für Durchsatz und kontinuierliches Batching, TGI, wenn Sie von einem bereits bestehenden Hugging-Face-Ökosystem ausgingen (in dem Bewusstsein, dass es sich im Übergang befindet), SGLang, wenn Ihre Benutzer Agenten oder komplexes RAG entwickeln. Open WebUI kann als menschliche Schnittstelle über all dem dienen.

Sie möchten technische Artikel schreiben und wollen, dass das Modell nach Quellen sucht, Seiten liest und zitierte Entwürfe erstellt. Unsloth Studio ist die direktste Antwort mit nativer Web-Suche und Deep Research. Alternativ Open WebUI oder Text Generation WebUI, jedoch mit einer längeren Einrichtung im Hintergrund.

Sie haben eine NVIDIA-GPU und wollen maximale Performance in der Produktion. TensorRT-LLM oder vLLM, je nachdem, ob Sie bereits eine NVIDIA-native Infrastruktur haben oder einen offeneren Stack bevorzugen.

Sie möchten eine einheitliche API über mehrere Backends hinweg. LocalAI tut genau das und ist die natürliche Wahl für heterogene Umgebungen.

Sie interessieren sich hauptsächlich für kreatives Schreiben oder Storytelling. KoboldCPP ist genau dafür gebaut, mit vielen Generierungsoptionen für lange Erzählungen.

Sie möchten ohne Einschränkungen mit RAG, Plugins und fortgeschrittenen Konfigurationen experimentieren. Text Generation WebUI und Open WebUI bieten Ihnen maximale Flexibilität auf Kosten einer weniger gepflegten UX und einer Konfiguration, die mehr Geduld erfordert.

Das Ehrliche ist, dass es oft derselbe Entwickler ist, der LM Studio zum Erkunden und llama.cpp beim Entwickeln nutzt, oder Ollama für den Prototyp und vLLM, wenn es in die Produktion geht. Das Werkzeug hat keine feste Identität, es hat eine Aufgabe.

## Wohin die Reise geht

Drei Signale sagen besonders viel darüber aus, wohin sich das alles entwickelt. Das erste ist die Konvergenz der Formate: GGUF ist zum De-facto-Standard für lokale Modelle geworden, und die Tatsache, dass fast alle Clients es unterstützen, bedeutet, dass ein heute heruntergeladenes Modell morgen auf anderer Hardware reibungslos läuft. Es ist dieselbe Logik, die USB-C zum universellen Stecker gemacht hat – auch wenn im Unterschied zu einem physischen Stecker kein Softwareformat vor zukünftigen Revolutionen wirklich sicher ist.

Das zweite ist das Wachstum lokaler „agentischer“ Umgebungen. Unsloth Studio, SGLang, Open WebUI und andere verlagern den Schwerpunkt vom „Ausführen eines Modells“ hin zum „Etwastun-Lassen des Modells“, mit Web-Suche, Tool-Use, RAG und Agenten, die auf Ihren Dokumenten arbeiten. Es ist der Unterschied zwischen einem Motor, der antwortet, und einem Assistenten, der handelt – dieselbe Distanz, die eine Musikbox von einem Musiker unterscheidet, der improvisieren kann.

Das dritte ist die immer engere Integration zwischen lokaler Inferenz, Web-Suche, Tool-Use und RAG auf persönlichen Dokumenten. Es sind keine getrennten Welten mehr: Es sind Schichten, die sich um das Modell herum anreichern, und der Client ist das, was sie zusammenhält. Die Richtung scheint auf eine Orchestrierung lokaler Multi-Step-Agenten hinzuweisen – ähnlich den Cloud-„Operatoren“, die aber auf Ihrem Rechner bleiben, wo die Daten niemals herausgehen.

Offene Fragen bleiben viele. Wie nachhaltig ist die Hardware, die Sie heute vor sich haben, im Laufe der Zeit gegenüber Modellen, die schneller wachsen, als die Effizienz mit ihnen Schritt halten kann? Wer ist für die Qualität dessen verantwortlich, was ein Agent extrahiert und schlussfolgert, wenn der Flaschenhals nicht mehr das Modell, sondern die Ingestion-Pipeline ist? Und die subtilste: Wenn wir einem Client vertrauen, dessen Inneres wir nicht sehen, erhalten wir dann mehr Kontrolle oder nur die Illusion, sie bewahrt zu haben?

Die Antwort liegt wie immer in der Nutzung. Und darin zu wissen, was unter der Haube steckt, wenn es darauf ankommt.
