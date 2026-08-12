---
tags: ["Applications", "Generative AI", "Ethics & Society"]
date: 2026-07-01
author: "Dario Ferrero"
---

# Last30days: Wenn ein Code-Agent zur sozialen Suchmaschine wird
![last30days.jpg](last30days.jpg)

*Bevor ich etwas über KI schrieb, öffnete ich elf Browser-Tabs: Reddit, X, YouTube, Hacker News, GitHub, ein paar Branchen-Newsletter. Zwei Stunden später, nach drei Kaffees, hatte ich drei wirklich nützliche Posts gefunden. Der Rest war Rauschen: für Suchmaschinen optimierte Blogartikel, Meinungen von Menschen, die dafür bezahlt wurden, sie zu haben, klassische Galerien nach dem Motto „Die zehn KI-Tools, die Ihr Leben verändern werden“, geschrieben mit der gleichen Tiefe wie ein Montageblatt für IKEA-Möbel.*

Das Problem ist nicht die Menge an Informationen. Es ist vielmehr, dass die Systeme, die wir zu deren Navigation nutzen, darauf ausgelegt wurden, Algorithmen anzugreifen, statt das widerzuspiegeln, was Menschen wirklich denken. Google indiziert Herausgeber. Reddit, X und YouTube indizieren Menschen. Es sind grundlegend unterschiedliche Ökosysteme, jedes in seinem eigenen eingezäunten Garten eingeschlossen, jedes mit seinen eigenen APIs, seinen eigenen Authentifizierungs-Token, seinen eigenen Zugangslogiken.

[`/last30days`](https://github.com/mvanhorn/last30days-skill) ist ein Versuch, diese Zäune niederzureißen. Es ist keine Suchmaschine im traditionellen Sinne: Es ist eine Skill für Code-Agenten, die parallel Reddit, X, YouTube, Hacker News, TikTok, GitHub, Polymarket und andere abfragt, die Ergebnisse zusammenführt und in wenigen Minuten eine strukturierte Zusammenfassung liefert. Geschrieben von Matthew Van Horn, hat es 41.500 Sterne auf GitHub erreicht und rangierte in seiner Startwoche als Repository Nummer eins des Tages. Die Zahlen allein sagen nicht viel aus, aber sie verdeutlichen die Intensität eines realen Bedürfnisses.

## Ein Blick in die Maschine: Architektur v3

Die Version drei des Projekts, die aktuelle, ist um eine einfache, aber kraftvolle Idee herum aufgebaut: Suche nicht nach dem, was du geschrieben hast, sondern verstehe zuerst, *wo* du danach suchen musst. Das offizielle README des Repositorys beschreibt den Ablauf in sieben Schritten, aber der interessante Teil ist das, was passiert, bevor ein einziger API-Aufruf getätigt wird.

Die Engine nutzt ein System zur Zusammenführung von Rankings namens Reciprocal Rank Fusion, abgekürzt RRF. Anstatt die Relevanz einer einzigen Quelle oder einem einzigen Algorithmus anzuvertrauen, nimmt RRF die Ergebnisse aus mehreren Quellen, jede mit ihrer eigenen Rangliste, und führt sie in einem zusammengesetzten Ranking zusammen, das das Gewicht von Ausreißern reduziert und die Konsistenz zwischen verschiedenen Plattformen belohnt. Wenn ein Thema auf Reddit stark hervortritt, erhält es ein Signal. Wenn das gleiche Thema auf X erscheint und in einem YouTube-Video zitiert wird, verstärkt sich das Signal. Wenn es hingegen nur auf einer Plattform stark und auf den anderen still ist, wird es herabgestuft.

Das andere architektonische Element, das Aufmerksamkeit verdient, ist das automatische Clustering: Wenn dieselbe Geschichte auf Reddit, X und YouTube mit unterschiedlichen Titeln erscheint, zeigt die Engine sie nicht dreimal an. Sie erkennt sie mittels Entity-based Overlap Detection als einziges Cluster und identifiziert die Übereinstimmung auch dann, wenn die auf den verschiedenen Plattformen verwendeten Wörter nicht übereinstimmen. Das Ergebnis ist ein Briefing, das konsolidiert statt dupliziert.

## Das Gehirn, das liest, bevor es sucht

Die Funktion, die das README „Intelligent Search“ nennt, ist das, was dieses Tool am deutlichsten von der traditionellen Suche trennt. Sie wurde von [Jonas Sperling](https://github.com/j-sperling) entwickelt und fungiert als Pre-Research Brain, ein Schritt Null, der jeder Abfrage an die externen APIs vorausgeht.

Die Idee ist folgende: Wenn man `/last30days OpenClaw` eingibt, sucht die Engine nicht buchstäblich nach „OpenClaw“ auf allen Plattformen. Zuerst klärt sie, wer und was sich um diesen Begriff herum befindet. Sie versteht, dass OpenClaw einen Schöpfer hat, Peter Steinberger, der auf X `@steipete` ist, dass das Haupt-Repository auf GitHub `steipete/openclaw` ist und dass relevante Diskussionen in Subreddits wie `r/ClaudeCode` zu finden sind. Dann sucht sie parallel nach all dem, bereits orientiert. Der Unterschied zur vorherigen Version, so schreibt Van Horn im README, ist strukturell: „Die alte Engine suchte nach Schlüsselwörtern. Die neue versteht Ihr Thema zuerst und sucht dann nach den richtigen Personen und Communities.“

Dies löst eines der nervigsten Probleme der kontextuellen Suche: die Mehrdeutigkeit. Wenn man nach „Paperclip“ sucht, meint man das KI-Startup oder die kleine Büroklammer aus Draht? Die Engine löst `@dotta` auf und versteht, dass man von Ersterem spricht. Wenn man nach „Dave Morin“ sucht, erhält man nicht nur sein X-Profil, sondern auch die Verbindungen zu OpenClaw und Zitate aus dem TWiST-Podcast. Die Desambiguierung erfolgt vor der Suche, nicht danach.

## Zwei Richter, nicht einer

Eines der ungewöhnlichsten Elemente von `/last30days` ist die Anwesenheit eines zweiten Richters im Syntheseprozess. Der erste bewertet die Relevanz: Wie pertinent ein Ergebnis zur Abfrage ist, wie aktuell es ist, wie viel Engagement es erhalten hat. Der zweite bewertet etwas anderes: Humor, Witz, Viralität.

Die Motivation ist praktischer Natur. Reddit und X produzieren täglich brillante Zusammenfassungen, perfekte Pointen, Kommentare, die die Essenz eines Phänomens besser erfassen als jede Analyse. Das alte System begrub sie, weil sie nicht „relevant“ im strengen Sinne des Wortes waren. Ein Kommentar wie „My Michael Jordan is Steve Kerr“ in einem Thread über Arizona Basketball erzielt bei der thematischen Pertinenz einen niedrigen Wert, aber einen extrem hohen bei der Ausdrucksqualität.

Das Ergebnis ist ein abschließender Abschnitt namens „Best Takes“, der die lebhaftesten Zitate, die am häufigsten geteilten One-Liner und Reaktionen sammelt, die dazu einladen, zum Thema zurückzukehren. Dies ist keine dekorative Funktion, sondern eine Anerkennung dafür, dass sich die digitale Kultur oft über den richtigen Witz zur richtigen Zeit bewegt und nicht über die präziseste Analyse.

## Vergleiche parallel, nicht seriell

Eine weitere in der v3 eingeführte Funktion verdient Aufmerksamkeit, weil sie ein praktisches Problem löst, das jeder kennt, der schon einmal versucht hat, zwei konkurrierende Tools zu vergleichen. In den vorherigen Versionen führte eine Abfrage wie `/last30days "OpenClaw vs Hermes vs Paperclip"` drei serielle Suchen aus: erst die eine, dann die andere, dann die letzte. Die Ausführungszeit konnte zwölf Minuten überschreiten. Die v3 führt hingegen einen einzigen Durchlauf mit Entity-aware Subqueries für alle Subjekte gleichzeitig aus, wodurch die Zeit bei gleicher Analysetiefe auf etwa drei Minuten sinkt.

Es gibt auch den Modus `--competitors`, der noch autonomer funktioniert: Zu einem Subjekt entdeckt die Engine über die Websuche selbstständig die wichtigsten Konkurrenten, startet dann parallele Pipelines für jeden und führt sie in einem strukturierten Vergleich zusammen. Es ist die Art von Funktion, die ein Suchwerkzeug in etwas verwandelt, das einem Junior-Analysten ähnelt: Es beschränkt sich nicht darauf, die gestellte Frage zu beantworten, sondern baut den Kontext auf, in dem diese Antwort Sinn ergibt.

## Fünfzehn Plattformen, ein Briefing

Die Tabelle der unterstützten Quellen im [Repository](https://github.com/mvanhorn/last30days-skill) ist lang: Reddit, X, YouTube, TikTok, Instagram Reels, Hacker News, Polymarket, GitHub, Digg, Threads, Pinterest, Bluesky, Perplexity, traditionelle Websuche. Einige sind kostenlos und funktionieren ohne Konfiguration (Reddit mit Kommentaren, HN, Polymarket, GitHub). Andere erfordern eine Authentifizierung oder kostenpflichtige API-Keys.

Das Vorhandensein von Polymarket ist besonders interessant: Hier werden keine Meinungen gesammelt, sondern Quoten. Die Wahrscheinlichkeiten auf Polymarket werden von denjenigen bestimmt, die reales Geld auf die Vorhersage setzen, nicht von denen, die nur informiert wirken wollen. Es gibt einen signifikanten epistemischen Unterschied zwischen „viele denken, dass X passieren wird“ und „74 % des Kapitals wetten darauf, dass X bis Dezember eintreten wird“. Die Engine zeigt dies als separates Signal mit Wahrscheinlichkeitsprozentsätzen an, nicht mit Dollarvolumina, denn die Magie liegt in der Quote, nicht im Betrag.

Für GitHub existiert auch ein sogenannter „Personen-Modus“: Wenn sich die Abfrage auf eine spezifische Person bezieht, hört die Engine auf zu suchen, wer über sie spricht, und beginnt zu suchen, was diese Person tatsächlich baut. Der Befehl `/last30days Peter Steinberger --github-user=steipete` liefert keinen Pressespiegel über Steinberger, sondern eine Karte seiner Arbeit: Wie viele Pull-Requests er im letzten Monat in welchen Repositorys gemacht hat, mit welcher Zustimmungsrate und was er veröffentlicht hat.
![tabella1.jpg](tabella1.jpg)
[Die Plattformen, auf denen die Suchen stattfinden](https://github.com/mvanhorn/last30days-skill)

## Opencode: Ein Test im Feld

Als ich das Projekt sah, war die sofortige Frage: Funktioniert es auch außerhalb des Claude-Code-Ökosystems? Die Antwort des Repositorys ist bejahend: Die Skill ist auf Codex, Cursor, Copilot, Gemini CLI und über das offene Paket `npx skills add mvanhorn/last30days-skill -g` auf über fünfzig Umgebungen installierbar, die mit dem Agent-Skills-Standard kompatibel sind, einschließlich `opencode`.

Ich habe die Skill auf opencode installiert und eine konkrete Suche durchgeführt: die Präferenzen der opencode-Nutzer darüber, welches kostenlose oder kostengünstige Sprachmodell das beste Preis-Leistungs-Verhältnis bietet. Eine Nischenabfrage mit einer kleinen, aber aktiven Community, die eine traditionelle Suchmaschine mit null nützlichen Ergebnissen beantwortet hätte.

Der erstellte Bericht durchforstete Provider, Foren, GitHub-Diskussionen und offizielle Dokumentationen. Er filterte heraus, dass opencode über 75 Provider und drei Hauptmodi für den Zugriff auf Modelle unterstützt. Unter den sofort verfügbaren kostenlosen Modellen ohne API-Keys: DeepSeek V4 Flash Free, ein Mixture-of-Experts-Modell mit 284 Milliarden Parametern und einer Million Token Kontext, das unter der MIT-Lizenz vertrieben wird. Für diejenigen, die zehn Dollar im Monat mit OpenCode Go ausgeben möchten, erwies sich das Modell mit dem besten Verhältnis von Anfragen zu Qualität als DeepSeek V4 Flash mit schätzungsweise 158.000 monatlichen Anfragen, während für die absolute Qualität GLM-5.2 und Kimi K2.7 Code auftauchten, wobei Letzteres besonders für komplexe MCP-Agenten empfohlen wurde. Für diejenigen, die nicht von der Cloud abhängig sein wollen, waren lokale Modelle via Ollama oder LM Studio im Detail dokumentiert, mit Qwen3.6-27B als Wahl für eine einzelne 24GB-GPU.

Der Bericht wurde auf ausdrücklichen Wunsch als `.md`-Datei mit Quellenangaben ausgegeben. Er dauerte etwa eine Minute. Er war nicht perfekt: Einige Preisinformationen würden eine direkte Überprüfung auf den Webseiten der Provider erfordern, und die opencode-Community ist klein genug, um die Stichprobe statistisch dünn erscheinen zu lassen. Aber um sich in einer Landschaft, die sich jede Woche ändert, schnell zu orientieren, war es genau das Richtige.

## Die Grenzen, über die niemand spricht

Ehrlichkeit gebietet es, auch das auf den Tisch zu legen, was nicht funktioniert oder was mit versteckten Kosten verbunden ist.

Die erste Grenze ist strukturell: Die reichhaltigsten Quellen – TikTok, Instagram, Threads, YouTube mit Kommentaren – erfordern einen API-Key von ScrapeCreators, einem kostenpflichtigen Dienst. Die ersten hundert Anfragen sind kostenlos, danach tritt ein Pay-per-use-Modell in Kraft. Wer die Vollversion des Tools nutzen möchte, muss mit variablen Kosten rechnen, die von der Intensität der Nutzung abhängen. Das „Gratis-Modell“ existiert zwar, ist aber deutlich eingeschränkter als das in den Use-Cases des README beschriebene.

Die zweite Grenze ist epistemisch und subtiler. Das Tool optimiert auf Engagement: Ein Reddit-Thread mit 1.500 Upvotes wiegt schwerer als ein Blogpost, den niemand gelesen hat. Im Prinzip ergibt das Sinn. In der Praxis ist Engagement jedoch ebenso sehr ein Maß für emotionale Reaktivität wie für Informationsqualität. Ein Post, der vereinfacht, empört oder belustigt, sammelt mehr Upvotes als eine differenzierte Analyse. `/last30days` löst dieses Problem nicht, sondern erbt es von den Plattformen, die es abfragt. Die Zusammenfassung ist nur so gut wie die Konversationen, die es findet, und Online-Konversationen haben ihre strukturellen Bias.

Die dritte Grenze betrifft die Datenlatenz: Das Tool sucht nach dem, was *in den letzten Wochen* passiert ist, nicht nach dem, was gestern Morgen geschah. Für Trendanalysen und Kontextrecherche funktioniert das hervorragend, für Breaking News in Echtzeit weniger.

Schließlich ein Hinweis zum Datenschutz. Das README erklärt ausdrücklich, dass die Suche lokal bleibt und keine Daten an Drittserver außerhalb der vom Nutzer selbst konfigurierten APIs übertragen werden. Es handelt sich um ein MIT-Projekt, das im Quellcode überprüfbar ist. Doch wer `/last30days` mit einem X- oder ScrapeCreators-Key nutzt, autorisiert diese Plattformen dennoch, die Abfragen zu empfangen: Die Vertraulichkeit ist also relativ und hängt davon ab, welche Quellen man aktiviert.

## Wer gewinnt, wer verliert, wer entscheidet

Aus Sicht der Nutzer beantwortet `/last30days` ein Bedürfnis, das bestehende Tools systematisch ignorieren: die Aggregation heterogener sozialer Signale, ohne Stunden damit zu verbringen, dies manuell zu tun. Es ist besonders in drei Kontexten nützlich: vor einem Treffen mit jemandem, dessen jüngste Arbeit man verstehen möchte; wenn man ein neues Tool in einem sich schnell bewegenden Sektor bewerten muss; und wenn man zu verstehen versucht, ob ein Trend real ist oder nur von den üblichen zehn einflussreichen Profilen verstärkt wird.

Für die Kategorie der professionellen Forscher und Journalisten ist die Sache komplexer. Das Werkzeug beschleunigt das Sammeln, ersetzt aber nicht das Urteil. Die „Best Takes“ können wertvoll sein, um zu verstehen, wie eine Community reagiert, aber das Auswählen der viralsten Witze ist nicht dasselbe wie das Identifizieren der am besten informierten Stimmen. Die Optimierung auf Engagement und die Optimierung auf Wahrheit sind unterschiedliche Funktionen, die manchmal orthogonal zueinander stehen.

Die abgefragten Plattformen ziehen keinen Nutzen aus diesem Schema: `/last30days` nutzt deren APIs oder öffentlichen Daten, ohne direkten Traffic zurückzuleiten. Dies ist eine Dynamik, die bereits von traditionellen Suchmaschinen bekannt ist, aber hier noch verstärkt wird: Es gibt nicht einmal den Click-through auf einen Link. Reddit hat bereits rechtliche Schritte gegen diejenigen eingeleitet, die seine Daten in nicht autorisierter Weise nutzen, und es ist nicht ausgeschlossen, dass sich die Zugangsbedingungen in Zukunft ändern.

Das Projekt ist mit seinen 41.500 Sternen und 3.400 Forks bereits groß genug, um Aufmerksamkeit zu erregen. Die Frage ist nicht, ob es funktioniert: Es funktioniert mit den beschriebenen Einschränkungen. Die Frage ist, wohin dieses Paradigma führt, wenn es verallgemeinert wird. Ein Agent, der parallel alle öffentlichen Konversationen zu einem Thema abfragt, sie zusammenführt, synthetisiert und in einer Minute eine Antwort liefert, ist ein mächtiges Werkzeug. Wie jedes mächtige Werkzeug sagt es viel mehr über denjenigen aus, der es benutzt, als über sich selbst.
