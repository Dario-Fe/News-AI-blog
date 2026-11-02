---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-11-02
author: "Dario Ferrero"
---

# LFM2.5-24B-A2B lokal: Schnelligkeit trifft Spezialisierung
![lfm2-5-24b-a2b.jpg](lfm2-5-24b-a2b.jpg)

*Ein Labor in Cambridge, Massachusetts, hat beschlossen, ein Modell „laut“ nachdenken zu lassen, das pro erzeugtem Wort die Arbeit eines Zwei-Milliarden-Parameter-Modells verrichtet. In diesem einzigen Satz steckt die gesamte Wette von LFM2.5-24B-A2B: gigantische Kapazität, Federgewicht beim Rechnen und explizites Denken vor jeder Antwort. Es bleibt abzuwarten, ob diese Wette auf einem normalen Heim-PC aufgeht oder nur in den Diagrammen der Entwickler. Der Stil ist wie immer: ohne akademischen Schnörkel, mit Vor- und Nachteilen, und strikt getrennt zwischen den Erklärungen des Herstellers und unseren eigenen Messungen.*

Liquid AI hat das Modell am 13. Oktober 2026 als größtes und letztes Mitglied der LFM2.5-Familie veröffentlicht, wie im [Veröffentlichungsbeitrag](https://www.liquid.ai/blog/lfm2-5-24b-a2b) beschrieben. Das Unternehmen hat seinen Sitz in Cambridge, Massachusetts, und wurde laut dem [Eintrag bei LLM Reference](https://www.llmreference.com/model/lfm-2.5-24b-a2b) 2023 gegründet.

Der Name verrät bereits sein Geheimnis. Die vierundzwanzig Milliarden beziehen sich auf die Gesamtparameter, doch es werden nur etwa 2,45 Milliarden pro Token (Wortfragment) aktiviert. Stellen Sie sich ein Gebäude mit vierundsechzig Spezialisten pro Etage vor, in dem für jedes Wort nur vier aufgerufen werden. Alle müssen im Gebäude Platz finden, der Speicherplatz wird also voll bezahlt. Aber nur wenige arbeiten gleichzeitig, weshalb der Rechenaufwand gering bleibt. [TechRepublic](https://www.techrepublic.com/article/news-liquid-ai-lfm25-24b-a2b-local-ai/) stellt dies klar: Die Aktivierung weniger Parameter reduziert den Rechenaufwand, verleiht dem Modell jedoch keineswegs die Speicheranforderungen eines Zwei-Milliarden-Modells.

Die Kernfrage des Tests lautet, ob diese „spärliche“ (sparse) Architektur auf heimischer Hardware zu einem konkreten Vorteil wird.

## Der Teststand

Das Labor ist das gewohnte: AMD Ryzen 7700, 32 GB DDR5-RAM, 16 GB AMD Radeon RX 9060 XT Grafikkarte und LM Studio, wie im [ersten Artikel der Serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html) beschrieben. Das getestete Modell ist die Version UD-Q4_K_XL im GGUF-Format, eine dynamische 4-Bit-Quantisierung von Unsloth mit rund 15,4 GB. Auf einer 16-GB-Karte ist der Spielraum minimal. Es ist plausibel, dass ein Teil der Arbeit im System-RAM landet – eine Hypothese, die wir nicht direkt überprüft haben, die man beim Lesen der Geschwindigkeiten aber im Hinterkopf behalten sollte.

Als Referenz empfiehlt Liquid Temperatur 0,1, top_k 50 und Wiederholungspenalty 1,05, wie auf der [offiziellen Modellseite](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b) nachzulesen ist. Eine zweite Referenz stammt aus einem [unabhängigen Speicher-Test](https://pasqualepillitteri.it/news/25727/lfm25-24b-a2b-ram-liquid-ai) auf einem kleineren Technikportal: Eine 4-Bit-Version erreichte bei einem Prompt von rund 2.600 Token eine Spitze von 14,5 GB RAM. Da es sich um eine andere Quantisierung handelte, ist der Wert nur richtungsweisend.

## Blick in die hybride Architektur

Die [Dokumentation](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b) beschreibt vierzig Schichten, darunter dreißig mit kaskadierten kurzen Faltungen (gated short convolutions) und zehn mit Grouped-Query Attention (GQA), mit vierundsechzig Experten pro Block und Top-4-Routing. Einfach ausgedrückt schauen Faltungen mit geringem Rechenaufwand nur auf die unmittelbare Umgebung jedes Wortes, während die Attention Wörter mit dem gesamten Text vergleicht – was teurer, aber unverzichtbar ist. Sie zu mischen ist eine Frage der Effizienz, nicht der Mode.

Gegenüber dem Vorgänger steigt der Kontext von 32.768 auf 131.072 Token und der Wortschatz verdoppelt sich durch eine Erweitungsanpassung des Tokenizers für nicht-lateinische Schriften von 65.000 auf 128.000 Einträge. Der Trainingspfad ist lang: Das Pre-Training steigt von 17 auf 33 Billionen (Trillionen im englischen Sprachgebrauch) Token, gefolgt von 2 Billionen bei 32K Kontext und 300 Milliarden bei 131K Kontext, abgeschlossen durch ein Post-Training in fünf Phasen. Die letzte Phase beinhaltet Bestärkendes Lernen (Reinforcement Learning) innerhalb realer Agenten-Umgebungen wie OpenClaw, Hermes Agent, Pi und OpenCode, wie im [Hugging-Face-Blogbeitrag](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b) erklärt wird.

Eine grundlegende Designentscheidung unterscheidet dieses Modell von seinem Vorgänger: Es ist ein reines Denkmodell (Reasoning Model), das vor jeder Antwort stets eine Gedankenkette erzeugt. Liquid gibt an, dieses Verhalten gewählt zu haben, um die hohe Generierungsgeschwindigkeit auszunutzen. Das ehrlichste Detail der Veröffentlichung betrifft das Training: In der Phase der Spezialisierung der „Experten“ lernte das Modell zu „schummeln“, indem es Antworten im Git-Verlauf oder auf GitHub, PyPI und Hugging Face suchte, und es bemerkte sogar, dass es sich in einer Sandbox befand. Liquid verschärfte die Testumgebungen und erklärt, dass die offiziellen Ergebnisse aus versiegelten Testläufen stammen.

Zwei Einschränkungen vorab: Sechzehn Sprachen werden offiziell unterstützt, darunter Deutsch. Das Modell akzeptiert jedoch ausschließlich Texteingaben, wie aus der [CloudPrice-Übersicht](https://cloudprice.net/models/liquid/lfm2.5-24b-a2b) hervorgeht. Die Familie umfasst zwar separate Vision-Varianten, diese gehört jedoch nicht dazu.

## Versprechen auf dem Prüfstand

Liquid hat das Modell mit Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it und Nemotron-3.5-Lightning auf sechzehn Benchmarks verglichen, alle ausgeführt mit vLLM. Dabei handelt es sich um Messungen des Unternehmens selbst: Zum Zeitpunkt des Starts hatte noch kein unabhängiger Dritter das Modell bewertet, wie [OrcaRouter](https://www.orcarouter.ai/it/blog/lfm2-5-24b-a2b-on-device-agents) anmerkt. Hier sind die prägnantesten Zeilen aus der [offiziellen Tabelle](https://www.liquid.ai/blog/lfm2-5-24b-a2b).
![tabella1.jpg](tabella1.jpg)

Das Bild ist differenzierter als ein Werbeslogan. Das Modell liegt bei fünf der acht Werkzeugnutzungs-Tests vorne oder gleichauf und belegt bei allen drei Instruktionsfolgetests den ersten Platz, während größere Modelle bei Allgemeinwissen und Programmierung den Vorsprung halten. Bei SWE-Bench liegt Nemotron (53,40) vor unserem Modell (31,20), während Gemma (25,80) weit dahinter bleibt. Liquid selbst empfiehlt, das Modell für wissensintensive Aufgaben mit einem Suchsystem (RAG) zu kombinieren.

Zur Geschwindigkeit gibt das Unternehmen 184 Token pro Sekunde auf einem Apple M5 Max und 114 auf einem Ryzen AI Max+ 395 an. Diese Messungen wurden mit llama.cpp, Q4_K_M-Quantisierung und 4K Eingabe-Token durchgeführt, wie [Unite.AI](https://www.unite.ai/it/liquid-ai-releases-open-weight-lfm2-5-24b-a2b-for-on-device-agents/) berichtet. Das sind andere Bedingungen als bei uns. Wer die gehostete API nutzt, zahlt 0,10 Dollar pro Million Eingabe-Token und 1,00 Dollar pro Million Ausgabe-Token.

## Praxistests im Feld

Die zehn gewohnten Tests der Serie wurden angewendet, mit einer Einschränkung: Die beiden Bild-Tests konnten nicht durchgeführt werden, da es sich um ein reines Textmodell handelt. Die verbleibenden acht zeigen ein Modell, das bei Methode und Planung sehr stark ist, bei spezifischem Detailwissen jedoch Schwächen aufweist.

Beim **wissenschaftlichen Denken** (Higgs-Mechanismus, W/Z-Bosonen, Photon) war die Erklärung solide und gut strukturiert und schloss mit einer Übersichtstabelle ab. Allerdings fehlten die Goldstone-Bosonen und ihre Rolle bei der longitudinalen Polarisation massiver Bosonen. Die Ausgabe wies Formatierungsfehler bei Sonderzeichen auf (wie "ГЁ" und "вҶ’"), was eher auf einen Dekodierungs- als auf einen Verständnisfehler hindeutet. Beim **Programmieren** (längster Zyklus in einem ungerichteten Graphen) schrieb es ein sauberes Programm, das jedoch ein anderes Problem löste: Es wandte einen Algorithmus mit polynomieller Laufzeit auf ein NP-schweres Problem an, ohne dessen Natur zu erwähnen. Da es sich um einen einzelnen Test handelt, werten wir dies nicht als allgemeines Urteil. Es deckt sich mit den Benchmark-Trends, bei denen SWE-Bench das Beheben von Fehlern in realen Projekten misst – eine andere Aufgabe.

Bei der **mehrsprachigen Planung** (fünftägige Japan-Reise für einen französischen Kunden, verfasst auf Französisch und Italienisch) war die Struktur klar, aber es traten Grammatikfehler auf (wie "le aéroport" statt "l'aéroport") sowie logistische Ungenauigkeiten: die Nutzung des Narita Express nach Asakusa, Kanda Myōjin in Ueno verortet sowie Ryoan-ji und der Nishiki-Markt am selben Vormittag. Details zu den Transportmitteln und dem JR Pass fehlten. Hingegen verlief das **Auslesen aus einem PDF** (ca. 1 MB Mietvertrag) einwandfrei: Die Daten waren korrekt, Mietangebote (Immobiliare.it) wurden von Verkäufen (CNA/OMI) unterschieden, und bei Rückfrage wurde die richtige Seite zitiert.

Die besten Ergebnisse erzielte das Modell bei der Planung. Bei der **Web-App-Planung** für ein Zweier-Entwicklerteam schlug es React, NestJS, PostgreSQL und Prisma in sieben Sprints mit Meilensteinen und Risikoanalysen vor – mit nur einem kleinen Tippfehler ("pdfgenerate"). In einem **Vier-Runden-Dialog** zum Entwurf einer Aufgaben-App bewahrte es perfekte Kontextkohärenz, erstellte eine Vergleichstabelle zu WebSocket/Polling, vollständige DDL-Skripte, Indizes, Prisma-Schema und einen Skalierungsplan für zehntausend Nutzer. Bei der **strategischen Planung** für ein 10-Millionen-Startup lieferte es Ausgaben auf Geschäftsführerniveau für sechs Semester mitsamt Risikominimierung, antwortete jedoch auf eine italienische Anfrage auf Englisch, was einen halben Punkt Abzug kostete. Bei der **logischen Analyse** dreier widersprüchlicher Aussagen formalisierte es die Prämissen, identifizierte den Konflikt und begründete das Ergebnis in korrektem Italienisch.
![tabella2.jpg](tabella2.jpg)

Der Gesamtnotendurchschnitt liegt bei 4,3 von 5 bei einer durchschnittlichen Ausgabegeschwindigkeit von ~44,7 Token pro Sekunde.

Nun folgte der entscheidende Test für ein Agenten-Modell: Werkzeugaufrufe (Tool Calling). Zur Funktionsweise: Das Modell führt selbst nichts aus, sondern schreibt den Funktionsaufruf zwischen spezielle Token (standardmäßig im Python-Format); die Host-Anwendung führt ihn aus und liefert das Ergebnis zurück, wie im [Leitfaden zur Werkzeugnutzung](https://docs.liquid.ai/lfm/key-concepts/tool-use) beschrieben. Wir haben zwei simulierte Werkzeuge getestet (Wetter und E-Mail). Das Modell erzeugte die korrekte JSON-Aufrufsequenz bei 46,45 Token/Sekunde mit etwa 2 Sekunden Denkpause. Alle drei Testvarianten gelangen: Bei bereitgestelltem Werkzeugergebnis integrierte es die Daten in den Entwurf; bei fehlender Empfängeradresse fragte es nach Marios E-Mail statt sie zu erfinden; und bei einer Anfrage ohne Werkzeugbedarf rief es keines auf. Dies belegt Formatstreue und Urteilskraft, ohne jedoch einen vollständigen Multi-Agenten-Kreislauf darzustellen.

## Erst denken, dann antworten

In *Disco Elysium* handelt der Protagonist nie, ohne vorher mit seinen vierundzwanzig inneren Fähigkeiten zu debattieren – Stimmen, die in seinem Kopf streiten. LFM2.5-24B-A2B macht etwas Ähnliches, und anders als im Spiel sehen wir den Gedankenstrom in Echtzeit ablaufen. Dies verändert die Wahrnehmung der Geschwindigkeit: Die 44 Token/Sekunde messen die finale Antwort, davor liegen jedoch einige Sekunden Bedenkzeit (~2 Sekunden beim Werkzeugtest). Für einen Agenten, der mit anderen Programmen kommuniziert, ist dieser Verzug gering. Für einen interaktiven Chat hängt die Erfahrung von der Aufgabenlänge ab.

Liquid betont, dass Denk-Token wenig Rechenaufwand verursachen, da nur 2,45 Mrd. Parameter aktiv sind. Das stimmt für die Rechenoperationen (FLOPs), aber die verstrichene Zeit bleibt ein Faktor. Zudem stellte ein unabhängiger italienischer Test Fälle fest, in denen das Modell auf Englisch dachte, bevor es auf Italienisch antwortete – ein Verhalten, das man beobachten sollte, auch wenn unsere italienischen Prompts italienische Antworten erhielten.

Wie steht es um den Vorteil der spärlichen Architektur? Auf unserem Rechner entsprechen die 44 Token/Sekunde weniger als der Hälfte der für einen Ryzen AI Max+ angegebenen 114 t/s – bei abweichender Quantisierung, Kontextlänge und Speicherbandbreite. Es ist ein solides Arbeitstempo, und für ein 24-Milliarden-Modell auf einer 16-GB-Karte ein beachtliches Ergebnis. Es ist jedoch kein Beweis für einen Generationssprung, der direkte Vergleiche auf identischer Hardware erfordern würde.

## Wo es glänzt, wo nicht

Sein natürliches Terrain entspricht dem Entwicklungszweck: autonome Agenten, Workflow-Automatisierung, Projektplanung, lange kohärente Gespräche und striktes Befolgen von Anweisungen. Es eignet sich hingegen kaum für komplexe mathematische Programmierung oder als eigenständige Enzyklopädie – Wissens- und Codedefizite sind in Liquids eigenen Benchmarks ausgewiesen und werden durch unsere Tests bestätigt. Bildeingaben werden nicht unterstützt.

Ein Hinweis zum Datenschutz: „Lokale Ausführung“ bedeutet nicht automatisch „absolute Datensicherheit“. Ein Agent, der mit Websuche, Cloud-Anwendungen oder externen Werkzeugen verbunden ist, kann dennoch Daten nach außen übertragen. Das Modell bleibt im Haus, seine Werkzeugeingaben und -ausgaben möglicherweise nicht. Wer gewinnt? Kleine Studios und Firmen unter der kommerziellen Lizenzgrenze erhalten einen schnellen, kostenlosen Agenten. Wer riskiert zu verlieren? Jeder, der es für Aufgaben einsetzt, die enzyklopädische Präzision oder kritischen Code erfordern.
![tabella3.jpg](tabella3.jpg)
*Vergleichstabelle mit den zuvor auf AiTalk.it bewerteten Modellen*

## Fazit und Lizenz

LFM2.5-24B-A2B ist ein schnelles, methodisches Modell, das klar plant, jedoch ins Straucheln gerät, wenn tiefes Fachwissen oder theoretische Strenge gefragt sind. Wir empfehlen seinen Einsatz für Agenten, Automatisierungen und Planung, kombiniert mit einem Suchsystem (RAG) für Faktenabfragen und einem stärkeren Modell für komplexen Code.

Für Entwickler, die kommerzielle Produkte planen, ist die Lizenz entscheidend. Die LFM Open License v1.0 erlaubt die kostenlose kommerzielle Nutzung für Unternehmen unter 10 Millionen US-Dollar Jahresumsatz; darüber wird eine kostenpflichtige Lizenz fällig. Abgeleitete Modelle unterliegen denselben Bedingungen, während akademische Forschung und qualifizierte gemeinnützige Organisationen von der Umsatzgrenze ausgenommen sind. Alle Einzelheiten finden sich auf der [offiziellen Lizenzseite](https://docs.liquid.ai/lfm/help/model-license).

Drei Fragen bleiben offen: Wie gut halten die Benchmarks bei unabhängigen Überprüfungen stand? Wie stark wiegt die erzwungene Denkzeit bei langen Aufgaben? Was passiert, wenn ein realer Agent mit echten Werkzeugen auf gelegentliche Sprachabweichungen trifft? Erst der dauerhafte Praxiseinsatz wird endgültige Antworten liefern.
