---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-10-12
author: "Dario Ferrero"
---

# MiniCPM5-2B: blitzschnell, stark im Code, weniger in anderem
![minicpm5-2b.jpg](minicpm5-2b.jpg)

*In den letzten Wochen tauchte der Name MiniCPM5-2B in Timelines, Newslettern und Discord-Kanälen zur lokalen KI mit einer Frequenz auf, die für ein Modell mit nur 2,5 Milliarden Parametern verdächtig wirkt. Laut der offiziellen Modellkarte auf [Hugging Face](https://huggingface.co/openbmb/MiniCPM5-2B) erreicht das Modell 97,1 auf τ²-Bench Telecom, 69,1 auf LiveCodeBench v6 und 86,5 auf AIME—Zahlen, die in dem von den Autoren selbst veröffentlichten Vergleich diejenigen von 4B-Modellen wie Qwen3.5-4B übertreffen. [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b), wo ein Teil der Tests unabhängig wiederholt wurde, bestätigt, dass dies der höchste Wert auf dem eigenen Intelligence Index unter allen Open-Weight-Modellen unter 4 Milliarden Parametern ist. Die Frage, die man sich stellen sollte, bevor man den Satz „konkurriert mit viermal größeren Modellen“ nachplappert, ist einfach: Konkurriert es wirklich, und worin?*

## Das Labor, kurz gefasst

Die Hardware-Konfiguration ist dieselbe wie in der ersten [Folge zu Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1): AMD Ryzen 7700, 32 GB DDR5 RAM, AMD Radeon RX 9060 XT Grafikkarte mit 16 GB VRAM, LM Studio als Framework. Für Details zur Installation und Konfiguration verweise ich auf diesen Artikel.

Eine wichtige methodische Anmerkung: Für diesen Test habe ich bewusst die 2,7 GB große Q8_0-Version und nicht die 1,56 GB große Q4_K_M-Version verwendet, um zu verstehen, ob etwaige Einschränkungen von der Quantisierung oder vom Modell selbst abhingen. Die Antwort lautet, wie wir sehen werden, dass die Grenzen struktureller Natur sind: Selbst bei maximaler lokal verfügbarer Qualität tut sich das Modell bei abstraktem Denken, mehrstufiger Planung und Anweisungen mit mehreren Bedingungen schwer. Die Geschwindigkeit bleibt dagegen unter allen Bedingungen außergewöhnlich, was bestätigt, dass die Effizienz der Architektur kein reines Marketing ist.

## Was ist MiniCPM5-2B

Hinter dem Modell steht OpenBMB, eine Open-Source-Forschungsgemeinschaft mit Verbindungen zur Tsinghua-Universität und ModelBest, die mit der MiniCPM-Familie laut Tencent News insgesamt über 50 Millionen Downloads überschritten hat. Das ist kein Hobbyprojekt: Das Repository [OpenBMB/MiniCPM auf GitHub](https://github.com/openbmb/minicpm) zählt über 11.000 Sterne, und die Liste der ab Tag eins unterstützten Frameworks—von vLLM über SGLang bis hin zu neun verschiedenen Chip-Architekturen via FlagOS—spricht für einen industriellen Maßstab.

Die Architektur ist ein dichtes Standard-`LlamaForCausalLM` mit insgesamt 2,52 Milliarden Parametern (1,98 Milliarden ohne Embeddings), 42 Schichten und GQA-Attention mit 16 Query-Heads und 2 Key-Value-Heads. Der angegebene native Kontext beträgt 131.072 Tokens, die Lizenz ist Apache 2.0, also frei für die kommerzielle Nutzung. Es ist ein reines Textmodell ohne Vision-Fähigkeiten, mit einem über Parameter im Chat-Template aktivierbaren Thinking Mode und nativem Tool Calling im XML-Format.

Der echte Mehrwert liegt jedoch nicht nur in den Gewichten selbst: OpenBMB hat auch das gesamte Rezept, die UltraData-Datensätze, das Reinforcement-Learning-Framework und die Post-Training-Pipeline auf Basis von On-Policy Distillation veröffentlicht, die die Fähigkeiten von sechzehn Expertenmodellen (davon fünf auf Agentenaufgaben spezialisiert) in einem einzigen finalen Checkpoint verschmilzt. Das ist derselbe Ansatz in kleinerem Maßstab, der andere chinesische Open-Weight-Projekte in den letzten zwei Jahren interessant gemacht hat.

Es gibt jedoch ein Detail, das man sofort ansprechen sollte, weil es mehr über den Hype verrät als jeder Benchmark: Auf der [World Artificial Intelligence Conference in Shanghai](https://www.orcarouter.ai/blog/minicpm5-2b-open-weights-release) am 19. Juli 2026 hatte ModelBest das Modell mit einem angegebenen Kontext von 512.000 Tokens und einer Hardware-Partnerliste präsentiert, die AMD, Intel, MediaTek und Qualcomm umfasste. Die im September tatsächlich veröffentlichten Gewichte sind hingegen auf 131.072 Tokens konfiguriert. Das ist keine Kleinigkeit für jemanden, der einen Workflow für lange Dokumente plant: Man sollte besser mit 128K planen (was immer noch für ein Buch mit etwa 250 Seiten reicht) und nicht mit den auf der Konferenz angekündigten 512K.

## Was der Hersteller verspricht

Die von OpenBMB veröffentlichte Vergleichstabelle stellt MiniCPM5-2B Modellen derselben Klasse (LFM2.5-2.6B, Qwen3.5-2B, Gemma-4-E2B-it) und größeren 4B-Modellen (Qwen3.5-4B, granite-4.2-3B, Nemotron-3-Nano-4B) gegenüber. Der Gesamtdurchschnitt liegt bei 53,9 gegenüber 51,1 des besten 4B-Modells in der Tabelle. Die angegebenen Stärken sind Coding, Tool Calling, Agenten-Fähigkeiten und Mathematik: Auf SWE-bench Verified erreicht das Modell 46,4 gegenüber 33,6 bei Qwen3.5-4B, auf τ²-Bench Telecom 97,1 gegenüber 92,1.

Die Schwächen, die von den Autoren selbst in der Tabelle eingeräumt werden, sind ebenso deutlich: Bei Allgemeinwissen (MMLU-Pro) bleibt das Modell bei 70,8 gegenüber 78,0 bei Qwen3.5-4B stehen, bei GPQA-Diamond fällt es auf 70,2 gegenüber 77,1 ab, und bei komplexeren Agenten-Coding-Benchmarks wie SWE-bench Pro (14,4 gegenüber 28,2) und Terminal-Bench v2.1 (8,6 gegenüber 25,8) wird der Abstand zu den 4B-Modellen erheblich größer.

Es gibt zudem eine interessante Zahl zur Glaubwürdigkeit des am häufigsten zitierten Werts, dem Intelligence Index von Artificial Analysis. Beim Start im Juli meldete OpenBMB einen Wert von 17. Mit der methodischen Überarbeitung v4.2 vom September, die vertrauliche Tests höher gewichtet und neue Agenten-Komponenten einführt, sank der offizielle Wert auf 15, was immer noch der höchste Wert unter den Open-Weight-Modellen unter 4B ist, wie von [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b) selbst berichtet. Der Bericht von [eesel AI](https://www.eesel.ai/blog/minicpm5-2b-review) weist außerdem auf eine Diskrepanz zwischen diesem unabhängigen Wert und einer Social-Media-Ankündigung von OpenBMB hin, in der 23 Punkte genannt wurden. Das sind Zahlen, die dieselbe Geschichte aus unterschiedlichen Blickwinkeln erzählen, was man wissen sollte, bevor man die erste Zahl aus einem Beitrag unkritisch übernimmt.

Zur angegebenen Geschwindigkeit enthält die offizielle Dokumentation in der Modellkarte keine präzisen Zahlen für Smartphones oder Apple Silicon: Die online kursierenden Schätzungen (10–12 Tokens pro Sekunde auf Smartphones, 70–90 auf Apple M4 Max) stammen aus inoffiziellen Community-Portierungen, wie einer MLX-Portierung, die etwa 96 Tokens pro Sekunde beim Decodieren auf einem M4 Max mit 128 GB großem gemeinsamem Speicher misst. Sie sollten daher als grobe Richtwerte und nicht als vom Hersteller zertifizierte Benchmarks behandelt werden.
![grafico1.jpg](grafico1.jpg)
[Bild aus dem offiziellen GitHub-Repository](https://github.com/openbmb/minicpm)

## Die Praxistests

Hier folgt der wichtigste Teil dieses Artikels: die praktische Analyse mit der 2,7 GB großen Q8_0-Version, der höchsten lokal verfügbaren Qualität, ohne auf das vollständige BF16-Format zurückzugreifen.

**Mathematisches Denken**, Bewertung 3/5, 105,66 Tokens/s. Das Problem der zwei Züge, die in Mailand und Rom abfahren, wurde korrekt gelöst (Treffpunkt um 10:40 Uhr), aber der logische Weg war unnötig umständlich: Das Modell berechnete Gesamtfahrzeiten, die für die Lösung gar nicht nötig waren, bevor es zur korrekten Gleichung gelangte. Dazwischen tauchten deplatzierte Zeichen auf, Überbleibsel einer fehlerhaften Tokenisierung. Es kommt zum Ergebnis, erklärt es aber nicht gut: nützlich für eine schnelle Antwort, weniger um eine Methode zu lernen.

**Codegenerierung**, Bewertung 4,5/5, 106,42 Tokens/s. Gefordert war eine Python-Funktion für die längste ansteigende Teilfolge in O(n log n)-Zeit. Das Modell lieferte den optimalen Algorithmus mit `tails`-Array und binärer Suche, sauberen Code, Docstrings und ein funktionierendes Beispiel. Ein kleiner sprachlicher Tippfehler und eine an einer Stelle leicht unpräzise Erklärung schmälern das Urteil nicht: Das ist das Feld, in dem das Modell am meisten überzeugt, ganz auf einer Linie mit den offiziellen Benchmarks auf SWE-bench Verified.

**Tool Calling**, Bewertung 4/5, 103,56 Tokens/s. Bei der Aufgabe, die einen Assistenten mit `get_weather` und `send_email` simulierte, war die Abfolge der JSON-Aufrufe formal korrekt. Allerdings berücksichtigte das Modell die logische Abhängigkeit zwischen den beiden Aufrufen nicht: Der E-Mail-Text bestand aus festem Text, anstatt auf die gerade abgerufene Wetterausgabe Bezug zu nehmen. Gut für einfache Automatisierungen, weniger für Orchestrierungen mit mehreren verknüpften Schritten.

**Abstraktes logisches Denken**, Bewertung 3,5/5, 106,21 Tokens/s. Vor ein syllogistisches Paradoxon mit drei widersprüchlichen Aussagen gestellt, erkannte das Modell die Lösung korrekt. Die Darstellung war jedoch verworren, enthielt Rechtschreibfehler und verzichtete auf Mengennotation, die die Argumentation strenger gemacht hätte. Es versteht das Problem, tut sich aber schwer, es präzise darzulegen.
![immagine1.jpg](immagine1.jpg)
*Screenshot während der Tests von MiniCPM5-2B auf LM Studio*

**Allgemeinwissen**, Bewertung 2/5, 103,74 Tokens/s. Bei der Frage nach einer Zusammenfassung zur italienischen und nordischen Renaissance mit zwei Künstlern pro Seite nannte das Modell nur einen Künstler pro Seite und schrieb Hans Holbein eine Spezialisierung auf Landschaften zu, die ihm historisch nicht zusteht: Holbein ist für Porträts bekannt, während sich die Landschaft als eigenständiges Genre im holländischen 17. Jahrhundert entwickelte. Das ist der Bereich, in dem sich der Abstand zu den 4B-Modellen am deutlichsten bemerkbar macht.

**Langer Kontext**, Bewertung 4/5, 96,11 Tokens/s. Bei einem technischen Dokument auf Deutsch über die Autoritätspropagierung in Multi-Agenten-Systemen lieferte das Modell eine korrekte und gut strukturierte Fünf-Punkte-Zusammenfassung ab. Es erfasste technische Konzepte wie das Problem des „Confused Deputy“ und dessen Auswirkungen für Entwickler präzise.

**Mehrstufige Planung**, Bewertung 3/5, 105,63 Tokens/s. Bei der Aufgabe mit drei Werkzeugen (`read_file`, `write_file`, `run_command`), um einen API-Schlüssel in einer Konfigurationsdatei zu ändern, umging das Modell die bereitgestellten Werkzeuge und nutzte `sed` innerhalb von `run_command` anstatt `write_file`. Dadurch erzeugte es eine redundante Sequenz und nutzte die Ausgabe des anfänglichen Lesevorgangs nicht, um den zu ersetzenden Wert zu extrahieren. Das bestätigt, dass man die Bezeichnung „agentisch“ bei echten mehrstufigen Orchestrierungen mit Vorsicht handhaben muss.

**Anweisungen mit komplexen Bedingungen**, Bewertung 2,5/5, 106,42 Tokens/s. Bei einer Entschuldigungs-E-Mail mit fünf gleichzeitigen Bedingungen (Länge, Datum, Rabatt, Tonfall, verbotenes Wort) hielt das Modell vier von fünf ein. Es traten jedoch deutliche grammatikalische Fehler auf, der Schlusssatz war schwer verständlich, und die im professionellen Rahmen erwartete Anrede und Grußformel fehlten.

## Übersichtstabelle
![tabella1.jpg](tabella1.jpg)

Durchschnittsbewertung: 3,3/5. Durchschnittliche Geschwindigkeit: etwa 104,2 Tokens pro Sekunde—ein Wert, den kein Modell dieser Klasse, mit dem ich bisher gearbeitet habe, annähernd erreicht hat.

## Wo man es einsetzen kann, wo nicht

MiniCPM5-2B überzeugt bei Coding-Aufgaben mittlerer Komplexität, bei denen es fast so sauberen und funktionierenden Code liefert wie ein viermal größeres Modell. Es ist solide beim einfachen Tool Calling mit einem oder zwei unabhängigen Werkzeugen und überraschend kompetent bei der Zusammenfassung technischer Dokumente. Mit einem Speicherbedarf von 2,7 GB in Q8 oder 1,56 GB in Q4 läuft es auf Hardware vom Raspberry Pi bis zum Mittelklasse-Smartphone mit einer durchschnittlichen Geschwindigkeit nahe 105 Tokens pro Sekunde auf Consumer-Hardware.

Es ist jedoch kein Modell für enzyklopädisches Wissen, wo faktische Fehler konkret auftreten. Es tut sich schwer bei komplexem abstraktem Denken, wo es zwar zur Lösung gelangt, diese aber verworren darlegt. Vor allem ist es noch nicht in der Lage, Werkzeuge in mehrstufigen Sequenzen mit echten Abhängigkeiten zu orchestrieren—dem eigentlichen Prüfstein für jeden Agenten.

## Das Fazit: Den Hype entzaubern

Was wahr ist: Für seine Größe ist MiniCPM5-2B eine bemerkenswerte technische Leistung. Die Geschwindigkeit ist real, das Coding ist auf hohem Niveau, das einfache Tool Calling funktioniert, und dass OpenBMB auch Datensätze und Trainingsrezept freigibt, ist ein seltener Beitrag zum Open-Source-Ökosystem. Was Hype ist: „Konkurriert mit viermal größeren Modellen“ stimmt nur für eine Teilmenge von Benchmarks—vor allem Coding und einfache Agentenaufgaben—, nicht jedoch bei Allgemeinwissen oder abstraktem Denken, wo der Abstand messbar bleibt. Was es nicht ist: Es ist kein Generalistenmodell und kein kleiner Allrounder.

Man fühlt sich an eine Szene aus *Chungking Express* erinnert, jenem Film von Wong Kar-wai, in dem alles schnell verläuft, sich aber nicht alles bis ins Letzte greifen lässt: MiniCPM5-2B hat dasselbe rasche Tempo. Wenn man es jedoch bittet innezuhalten und ruhig über etwas wirklich Komplexes nachzudenken, wird das Bild unscharf. Oder um es bodenständiger auszudrücken: Es ist wie ein sportlicher Kleinwagen—schnell, leicht und wendig in der Stadt. Aber eine Reise über tausend Kilometer mit Familie und Gepäck tritt man damit nicht an.

Der in Q8_0 durchgeführte Test bestätigt dieses Bild: Wenn man auf das vollständige BF16-Format verzichtet, zeigen sich die strukturellen Grenzen des Modells selbst und nicht nur Effekte der Gewichtskomprimierung.

## Für wen es wirklich nützlich ist

Die idealen Nutzer sind Entwickler und Teams, die eine schnelle und leichte Engine für Routine-Coding und einfache Automatisierungen auf ressourcenbeschränkter Hardware suchen—möglicherweise kombiniert mit einem größeren Modell für Aufgaben, die Tiefe erfordern. Weniger geeignet ist es für alle, die einen Generalisten-Assistenten suchen, verlässliches enzyklopädisches Wissen benötigen oder einen Agenten wollen, der komplexe Werkzeuge ohne strenge Überwachung orchestriert. Für diese Fälle bleibt es sinnvoller, sich an größeren Modellen zu orientieren, etwa im 4B-Bereich, den der offizielle Vergleich von OpenBMB als Referenz heranzieht.

Der Rat bleibt derselbe wie immer, wenn der Hype schneller läuft als die Fakten: Nutzen Sie es als das, was es ist—ein kleiner, schneller und verlässlicher Spezialist in einem abgegrenzten Rahmen—, und nicht als das, was Social-Media-Beiträge glauben machen wollen.
