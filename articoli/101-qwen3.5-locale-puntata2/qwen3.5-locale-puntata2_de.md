---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-18
author: "Dario Ferrero"
---

# KI zu Hause: LM Studio und Qwen 3.5 auf meinem PC – Folge 2
![qwen3.5-locale-puntata2.jpg](qwen3.5-locale-puntata2.jpg)

*Fortsetzung von [Folge 1](https://aitalk.it/it/qwen35-locale-puntata1.html), in der wir die Hardwarekonfiguration, die Wahl von LM Studio als Framework und die ersten drei Tests beschrieben haben: wissenschaftliches Denken zum Higgs-Mechanismus, multimodales Lesen einer unscharfen Tabellenkalkulation und Codegenerierung für ein NP-schweres Problem.*

Die Diskussion um Qwen 3.5 in den letzten zwei Wochen ist nicht auf internationale Fachforen beschränkt geblieben. In Italien haben Stimmen wie die von [Salvatore Sanfilippo](https://www.youtube.com/watch?v=NDBQq_NzxiE), einem der meistbeachteten Experten für angewandte künstliche Intelligenz, das Modell einer breiteren Öffentlichkeit bekannt gemacht und dazu beigetragen, dass diese Veröffentlichung zu einem der meistdiskutierten Themen der Saison im italienischen KI-Ökosystem wurde. Das ist kein Social-Media-Hype: Es ist die Erkenntnis, dass sich bei Open-Weight-Modellen etwas Strukturelles ändert und dass diese Änderung endlich greifbar genug ist, um auch außerhalb von Forscherkreisen Aufmerksamkeit zu verdienen.

Die drei Tests, die diese zweite Folge abschließen, wurden genau so konzipiert, dass sie die Bereiche berühren, die diejenigen am meisten interessieren, die keine Forscher sind, sondern KI zum Arbeiten, Planen, Analysieren und Organisieren nutzen: die Fähigkeit, in mehreren Sprachen zu denken und dabei die kulturelle Kohärenz zu wahren, die Verwaltung langer Dokumente mit chirurgischer Präzision und das Verständnis des physischen Raums durch ein Bild.

## Test 4 — Reisebüro in drei Sprachen

Der vierte Test konzentrierte sich auf zwei der meistbeworbenen Fähigkeiten des Modells: die umfassende Mehrsprachigkeit (Qwen 3.5 unterstützt 201 Sprachen) und die Agenten-Performance bei komplexen Planungsaufgaben. Ich stellte mir einen französischen Kunden vor, der kein Englisch spricht und Tokio und Kyoto besuchen möchte, mit Schwerpunkt auf historischen Tempeln und Street Food. Die Anfrage war komplex: ein fünftägiger Reiseplan in tadellosem Französisch mit praktischen Ratschlägen zu Transportmitteln und Sprachbarrieren, gefolgt von einem Abschnitt auf Italienisch für einen zweiten Reisenden, der denselben Weg einschlagen möchte.

Die Antwort hätte ein allgemeiner Reiseplan sein können, der durch Interpolation von Informationen aus einer Datenbank von Reiseführern generiert wurde. Das war nicht der Fall. Das Französisch entsprach dem eines High-End-Reiseberaters: formal, aber herzlich, präzise, ohne bürokratisch zu sein. Der Reiseplan hatte eine reale Logistik: Ankunft in Tokio und erstes Eintauchen in Asakusa und Senso-ji, zweiter Tag zwischen Meiji-Schrein und dem alten Tsukiji-Markt mit dem Hinweis, dass man Sushi dort am Tresen isst und pro Stück bezahlt, dritter Tag mit dem Shinkansen nach Kyoto und Spaziergang durch die Bambuswälder von Arashiyama am späten Nachmittag, vierter Tag mit dem Aufstieg zu den Torii von Fushimi Inari mit dem ausdrücklichen Hinweis, bequeme Schuhe zu tragen, Abend in Pontocho mit der Möglichkeit, Geishas zu begegnen. Fünfter Tag auf dem Nishiki-Markt, dem „Bauch von Kyoto“, wie das Modell ihn nannte, vor der Abreise.

Details machen den Unterschied zwischen Information und Wissen: zu wissen, dass Suica und Pasmo die aufladbaren Karten für den Transport sind, dass Google Translate mit Offline-Paketen in Japan fast unverzichtbar ist, dass man in Tempeln die Schuhe auszieht. Alles vorhanden, alles korrekt. Der italienische Abschnitt war eine praktische Zusammenfassung in einer flüssigen und nützlichen Sprache, ohne den gesamten Reiseplan sklavisch zu wiederholen, sondern mit den wesentlichen Tipps für jemanden, der die Route bereits kennt. Der Wechsel von einer Sprache in die andere hat die Qualität nicht gemindert: Ton, kulturelle Relevanz und Genauigkeit blieben stabil.

**Bewertung: 5/5.** Ein Agent, der Japan wie ein Reiseführer kennt, auf Französisch wie ein Muttersprachler schreibt und auf Italienisch zusammenfasst, ohne den Faden zu verlieren.

## Test 5 — Die Nadel im 460-seitigen Heuhaufen

Der fünfte Test war aus technischer Sicht der anspruchsvollste und wahrscheinlich der relevanteste für diejenigen, die KI im professionellen Kontext der Dokumentenanalyse einsetzen. Ich habe den [Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) von Stanford HAI in LM Studio geladen: 460 Seiten und etwa 20 MB, Zehntausende von Wörtern, Grafiken, Tabellen, Themenkapitel. Ein Band, den kein Mensch in einer Sitzung von Anfang bis Ende liest. Die Frage war scheinbar einfach: Finden Sie mir die Daten zum Wachstum der Videogenerierung und geben Sie mir an, auf welcher Seite sie stehen.

Beim ersten Mal keine Antwort. Beim zweiten Mal Schweigen. Beim dritten Mal wieder. In allen drei Versuchen führte das Modell den Denkprozess durch, der sichtbar und einsehbar ist, lieferte aber am Ende keinen Output. Ich musste explizit nachhaken und darauf hinweisen, dass das Modell manchmal keinen Output im Chat produziert, obwohl es die Anfrage verarbeitet hat. Beim vierten Versuch kam die Antwort, und sie war überraschend präzise.

Das Modell identifizierte die Seiten 126 und 127 in Kapitel 2 (Technical Performance), Abschnitt „Image and Video“. Es beschrieb den Inhalt: Seite 126 mit den Steckbriefen der Modelle Google Veo, Meta Movie Gen und OpenAI Sora, mit den Grafiken zur Nutzerpräferenz (Abbildungen 2.3.11 und 2.3.12); Seite 127 mit dem Vergleich zwischen den im Laufe der Zeit generierten Videos. Und dann rief es spontan ein spezifisches Beispiel ab: den Prompt „Will Smith eating spaghetti“, der im Laufe der Zeit zu einer kleinen informellen Fallstudie über die Qualität von KI-generierten Videos wurde – die Art von kulturellem Detail, die ein guter Forscher in eine Fußnote eingefügt hätte.

Das blockierende Verhalten der ersten drei Versuche ist eine reale Einschränkung, die ehrlich erwähnt werden muss. Es hängt wahrscheinlich von der zu verarbeitenden Datenmenge ab und davon, wie LM Studio Kontext-Token in sehr großen Fenstern verwaltet. Das ist kein Problem, das sich in fünf Minuten lösen lässt; es erfordert Verständnis für das eigene Setup und Geduld. Aber wenn das Modell antwortet, antwortet es gut.

**Bewertung: 4,5/5.** Millimetergenaue Präzision beim Abrufen von Informationen aus einem 460-seitigen Dokument, exakte Seiten, nummerierte Abbildungen, kulturelle Beispiele. Ein halber Punkt Abzug für die drei Fehlversuche – ein Verhalten, mit dem der reale Workflow rechnen muss.

## Test 6 — Der Geometer des häuslichen Chaos

Der letzte Test war vielleicht der ungewöhnlichste und derjenige, der die erzählerisch reichste Antwort hervorbrachte. Ich lud ein Online-Foto von geringer Qualität herunter, das ein Zimmer in völligem Unordnung zeigte: Kleidung überall, ein ungemachtes Bett, ein unter Papier begrabener Schreibtisch, überfüllte Regale, auf dem Boden verstreute Gegenstände. Ich lud das Foto in LM Studio hoch und bat das Modell, die Anordnung der Gegenstände zu beschreiben und eine Strategie zur Platzgewinnung vorzuschlagen.

Die Beschreibung des Zimmers war visuell originalgetreu: der blaue Korb in der Mitte, der den Hauptweg versperrt, die Stapel bunter Kleidung nach Farben und Materialien sortiert, die braunen Hausschuhe und die Sneaker am Eingang, das Bett rechts mit der aufgehäuften Wäsche, die den Nachttisch unzugänglich macht, der Schreibtisch links, „überfüllt wie ein Nest aus visuellem Unordnung“. Aber das beeindruckendste Detail war eines: Das Modell bemerkte, dass der Spiegel an der Wand den weißen Schrank und einige Kisten auf dem Boden reflektierte. Damit bewies es, dass es nicht nur die sichtbaren Objekte wahrnahm, sondern auch die durch die Reflexionen erzeugten räumlichen Beziehungen – ein dreidimensionales Raumverständnis, das nicht selbstverständlich war.

Die vorgeschlagene Aufräumstrategie folgte einer tadellosen Logik: zuerst die Mitte des Zimmers freimachen, um einen sicheren Weg zu schaffen, dann den Schreibtisch leeren, um zu kategorisieren, dann das Bett machen, um visuelle Fläche zurückzugewinnen, und schließlich in den nun zugänglichen Schränken verstauen. Jeder Schritt war begründet: die Mitte zuerst, weil dort die unmittelbarste Sturzgefahr besteht, das Bett danach, weil das Bettenmachen die Wahrnehmung des gesamten Raums visuell verändert, nicht nur seine Funktionalität. Es ist die Logik von jemandem, der nicht nur verstanden hat, was in diesem Zimmer ist, sondern wie der Raum für die Bewohner funktioniert.

**Bewertung: 5/5.** Dreidimensionales Raumverständnis, Analyse der Reflexionen, Schritt für Schritt begründete Interventionsstrategie. Ein Innenarchitekt hätte es nicht besser machen können.
![riconosimenti-img.jpg](riconosimenti-img.jpg)
*Screenshot eines Teils der Antwort von Qwen 3.5 auf die Aufforderung, das hochgeladene Bild zu analysieren.*

## Die Endabrechnung

Sechs Tests, sechs Bereiche, ein ziemlich vollständiges Bild, um Bilanz zu ziehen – mit dem Bewusstsein, dass dies ein persönliches Experiment bleibt und keine systematische Bewertung ist.

Was deutlich wird: Qwen 3.5 9B vollbringt bei 30 Token pro Sekunde auf einer Consumer-GPU mit 16 GB VRAM Dinge, die bis vor einem Jahr den Zugang zu kostenpflichtigen Frontier-APIs erfordert hätten. Es erklärt Quantenphysik mit der Klarheit eines guten Lehrers, liest unscharfe Tabellen wie ein Analyst, schreibt Code mit theoretischem Bewusstsein für Grenzen, plant mehrsprachige Reisen mit kultureller Kohärenz, findet spezifische Seiten in einem 460-seitigen Bericht, beschreibt ein unordentliches Zimmer und erkennt dessen Reflexionen. All dies läuft offline, ohne ein einziges Byte an einen Server zu senden.

Die Grenzen sind da und müssen ungeschönt benannt werden. Das blockierende Verhalten bei sehr langen Outputs oder erweiterten Kontexten ist das Hauptproblem: Es erfordert explizite Nachfragen und bringt eine Unsicherheit in den Workflow, mit der diejenigen umgehen müssen, die diese Werkzeuge in der Produktion einsetzen. Der erste abgebrochene Versuch im Coding-Test, das dreimalige Schweigen im Dokumententest sind keine vernachlässigbaren Mängel, sondern Verhaltensweisen, die ein professioneller Nutzer lernen muss vorauszusehen.

Offen bleibt auch eine Frage, die kein lokaler Test lösen kann: Datenschutz und die Herkunft der Trainingsdaten. Qwen ist ein Projekt von Alibaba Cloud, einem chinesischen Unternehmen, das der Gesetzgebung von Peking unterliegt. Das Modell lokal auszuführen, löst zwar die Frage der Datenübertragung bei der Inferenz – die Prompts verlassen die Maschine nicht –, sagt aber nichts darüber aus, was das Modell während des Trainings gesehen hat, oder über mögliche Verzerrungen im Zusammenhang mit dem geopolitischen Kontext seiner Schöpfer. Für viele private und berufliche Anwendungen ist die Frage irrelevant; für andere, in regulierten Bereichen oder Kontexten, in denen Datensouveränität eine gesetzliche Verpflichtung ist, lohnt es sich, darüber nachzudenken, bevor man es in einen kritischen Workflow integriert.

An der Cloud-Front bleibt der Wettbewerb asymmetrisch für Aufgaben, die tiefgehendes mehrstufiges Denken, in Echtzeit aktualisiertes enzyklopädisches Wissen und die Verwaltung riesiger Kontexte ohne unvorhersehbares Verhalten erfordern. Frontier-Modelle wie Claude, ChatGPT und Gemini spielen in diesen Szenarien immer noch in einer anderen Liga. Aber der Abstand verringert sich mit jeder Veröffentlichung, und die Richtung ist klar.

## Die Lust am Weitermachen

Diese Erfahrung war das, was ich mir erhofft hatte: lehrreich, konkret, stellenweise überraschend. Ein Modell dieser Qualität lokal auf einem PC zu installieren, der keine Workstation für fünftausend Euro ist, und Antworten zu erhalten, die dem Vergleich mit den besten Cloud-Diensten standhalten, wäre noch vor zwölf Monaten außer Reichweite schien. Das ist es nicht mehr.

Qwen 3.5 9B ist sicherlich das am meisten diskutierte Open-Weight-Modell der letzten Wochen, und der Ruf, den es sich mit früheren Versionen der Familie erarbeitet hatte, war nicht unbegründet. Aber es ist auch nur einer der Punkte in diesem sich schnell entwickelnden Ökosystem. Wer weniger VRAM hat oder Exzellenz beim Coding sucht, sollte [Microsofts Phi-4-mini](https://huggingface.co/microsoft/Phi-4-mini-instruct) Aufmerksamkeit schenken. Wer vorwiegend auf Italienisch oder in europäischen Sprachen arbeitet, für den haben die Varianten von [Mistral](https://mistral.ai/) spezifische interessante Merkmale. Jedes Modell glänzt in etwas anderem: Die Wahl hängt immer vom Anwendungsfall ab, und den Anwendungsfall kennt nur derjenige, der vor der Tastatur sitzt.

Der Punkt ist jedoch nicht, welches Modell man wählen soll. Der Punkt ist, dass diese Wahl existiert, zugänglich ist und funktioniert. Lokale LLMs, oder SLMs, wenn Sie die präzisere Bezeichnung bevorzugen, sind kein Experiment mehr für Enthusiasten mit Labor-Hardware. Sie sind aktuelle, funktionierende, verbesserungsfähige Werkzeuge, die die Privatsphäre respektieren und mit einer Hardwarestufe knapp über dem Standard-Consumer-Niveau zu mächtigen Verbündeten beim Entwerfen, Schreiben, Analysieren und Aufbauen werden.

Man muss nur Lust haben, sich die Hände schmutzig zu machen. Und mit diesen Werkzeugen werden die Hände immer weniger schmutzig.
