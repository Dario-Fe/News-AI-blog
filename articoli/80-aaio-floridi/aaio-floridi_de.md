---
tags: ["Research", "Ethics & Society", "Business"]
date: 2026-01-28
author: "Dario Ferrero"
---

# Wenn Agenten lernen zu navigieren: Willkommen im Zeitalter der AAIO
![aaio-floridi.jpg](aaio-floridi.jpg)

*Stellen Sie sich eine Welt vor, in der Ihre Website nicht nur von gelangweilten Menschen in der Kaffeepause besucht wird, sondern auch von Agenten der künstlichen Intelligenz, die autonom navigieren, Entscheidungen treffen und Transaktionen abschließen, ohne dass ein menschlicher Finger eine Maus berührt. Willkommen im Jahr 2026, wo dieses Szenario keine Science-Fiction mehr ist, sondern tägliche Realität. Und so wie sich in den neunziger Jahren Webmaster an die Spider von Google anpassen mussten, stehen wir heute vor einer neuen Revolution: der der Agentic AI Optimisation.*

Führend in diesem neuen Gebiet ist [Luciano Floridi](https://dec.yale.edu/people/luciano-floridi), ein römischer Philosoph, der nach Yale übergesiedelt ist, wo er das Digital Ethics Center leitet. Floridi, Jahrgang 1964, ist nicht der klassische Akademiker, der im Elfenbeinturm eingeschlossen ist. Nach einer klassischen Ausbildung an der La Sapienza in Rom durchlief er die Erkenntnistheorie in Warwick und Oxford, um sich dann dem zu widmen, was wir heute Informationsphilosophie nennen. Die italienische Regierung verlieh ihm den Titel eines Ritters des Großkreuzes, die höchste nationale Auszeichnung, und das nicht ohne Grund: Floridi hat als Ethikberater für Google gearbeitet, mit der Europäischen Kommission an künstlicher Intelligenz zusammengearbeitet und dazu beigetragen, die globale Debatte über digitale Ethik zu gestalten.

In dem im April 2025 zusammen mit einem Team des Digital Ethics Center (Carlotta Buttaboni, Emmie Hine, Jessica Morley, Claudio Novelli und Tyler Schroder) veröffentlichten [Paper](https://arxiv.org/abs/2504.12482) führt er formell das Konzept der Agentic AI Optimisation ein. Wenn die Suchmaschinenoptimierung (SEO) definiert hat, wie wir Inhalte für Suchalgorithmen strukturieren, stellt AAIO die notwendige Weiterentwicklung für eine Ära dar, in der die KI nicht nur Anfragen beantwortet, sondern autonom handelt.

## Was macht eine KI "agentisch"?

Bevor wir uns mit der Optimierung befassen, müssen wir verstehen, was ein agentisches künstliches Intelligenzsystem von seinen Vorgängern unterscheidet. Floridi und sein Team identifizieren drei grundlegende Merkmale: Autonomie bei der Einleitung von Aktionen ohne explizite Anweisungen, Entscheidungsfähigkeit auf der Grundlage des Kontexts und dynamische Anpassungsfähigkeit an digitale Umgebungen.

Wir sprechen nicht von glorifizierten Chatbots oder Sprachassistenten, die vordefinierte Befehle ausführen. Ein AAI-System kann beispielsweise eine E-Commerce-Website navigieren, Produkte nach komplexen Kriterien vergleichen, die Verfügbarkeit in Echtzeit prüfen und einen Kauf abschließen, indem es für mehrere Variablen wie Preis, Lieferzeiten und Nachhaltigkeit des Verkäufers optimiert. Und das alles, ohne dass ein Mensch jeden einzelnen Schritt spezifiziert hat.

Wie Floridi im Paper schreibt, hängt der Erfolg dieser Systeme nicht von ihrer Intelligenz ab (die sie technisch nicht besitzen), sondern davon, wie gut die digitale Umgebung um ihre "Agency ohne Intelligenz" herum strukturiert ist. Hier kommt AAIO ins Spiel.

## Von der Optimierung für Menschen zur Optimierung für Agenten

Traditionelles SEO wurde um eine Architektur herum aufgebaut, die für Menschen konzipiert ist, die über Browser navigieren. Ansprechende Titel, überzeugende Meta-Beschreibungen, wahrgenommene Ladegeschwindigkeit, responsives Design: Alles dreht sich um die menschliche Benutzererfahrung. AAIO teilt einige dieser grundlegenden Prinzipien (strukturierte Daten, Metadaten, Zugänglichkeit von Inhalten), erweitert und transformiert sie jedoch, um den betrieblichen Anforderungen autonomer Agenten gerecht zu werden.

Ein konkretes Beispiel: Während für einen Menschen ein gut sichtbarer Button mit der Aufschrift "Jetzt kaufen" ausreicht, benötigt ein KI-Agent ein strukturiertes Markup, das dieses Element eindeutig als transaktionale Aktion identifiziert, mit allen begleitenden Informationen (Endpreis, inklusive Steuern, Rückgabebedingungen) in maschinenlesbaren Formaten wie JSON-LD oder RDFa basierend auf [Schema.org](https://schema.org).

Floridis Paper identifiziert vier technische Säulen von AAIO. Die erste ist die Implementierung fortschrittlicher strukturierter Daten, die über das grundlegende SEO-Markup hinausgehen und einen vollständigen Kontext für jede Entität und Beziehung auf der Website bereitstellen. Die zweite betrifft die Optimierung der Informationsarchitektur: klare Hierarchien, logische Navigation, gut dokumentierte API-Endpunkte. Die dritte ist die semantische Zugänglichkeit, was bedeutet, textliche Alternativen, detaillierte Beschreibungen und kontextbezogene Metadaten für jedes Multimedia-Element bereitzustellen. Die vierte ist die Optimierung des Inhalts selbst durch regelmäßige Aktualisierungen, präzises Targeting der Absicht (nicht mehr nur menschlich, sondern auch agentisch) und KI-basierte Analysen für kontinuierliche Verbesserungen.

## Die Etikette der Roboter: Den Zugriff von Agenten verwalten

Eine unmittelbare praktische Frage ist: Wie kontrollieren wir, welche KI-Agenten auf unsere Inhalte zugreifen können? Die Antwort liegt in Weiterentwicklungen der klassischen robots.txt-Datei. Während dieses Tool dazu diente, den Spidern der Suchmaschinen mitzuteilen, wohin sie gehen dürfen, müssen wir uns heute mit spezifischen User-Agents wie GPTBot von OpenAI, ClaudeBot von Anthropic oder Google-Extended für die Modelle von Google auseinandersetzen.

Jeder Agent stellt sich mit einer eindeutigen Identifikationszeichenfolge in den HTTP-Anfragen vor. Ein Webmaster kann entscheiden, allen den Zugriff zu gewähren, einige Agenten selektiv zu blockieren oder strenge Whitelists zu implementieren. Floridi merkt im Paper an, dass einige Websites LLMs.txt-Dateien verwenden, ein Vorschlag, der den gesamten Inhalt der Website in einem einzigen Textdokument zusammenfasst, das für die Analyse durch große Sprachmodelle optimiert ist.

Die Frage ist nicht nur technisch, sondern auch wirtschaftlich und strategisch. Wenn ein KI-Agent autonom navigieren, Informationen extrahieren und Transaktionen abschließen kann, wer profitiert dann von dem Engagement? Wer bezahlt das Hosting? Wer sammelt die wertvollen Verhaltensdaten für das Marketing? Das sind Fragen, die an die frühen Debatten über Web-Scraping und Urheberrecht erinnern, aber mit tieferen Implikationen.

## Die Industrie bewegt sich: AgentKit, MCP und das Rennen um Standards

Während Floridi und sein Team Regeln vorschlagen, bauen die Tech-Giganten. OpenAI hat sein experimentelles Swarm-Framework in [AgentKit](https://openai.com/index/introducing-agentkit/) umgewandelt, eine komplette Suite zum Erstellen, Bereitstellen und Optimieren autonomer Agenten. AgentKit wurde im Oktober 2025 eingeführt und enthält einen visuellen Agent Builder zum Erstellen von Multi-Agenten-Workflows, ein zentralisiertes Connector Registry zur Verwaltung von Datenintegrationen und ChatKit zum Einbetten von Konversationsschnittstellen. Unternehmen wie Klarna haben mit diesen Tools Support-Agenten entwickelt, die zwei Drittel der Tickets bearbeiten, während Clay sein Wachstum mit automatisierten Vertriebsagenten verzehnfacht hat.

Aber die eigentliche Revolution könnte von einem offenen Standard ausgehen. Anthropic hat das [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) veröffentlicht, ein universelles Protokoll zur Verbindung von KI-Systemen mit externen Datenquellen. Stellen Sie sich MCP als USB-C für KI-Anwendungen vor: eine standardisierte Schnittstelle, die die Notwendigkeit kundenspezifischer Integrationen für jede Kombination aus Modell und externem System eliminiert. Seit seiner Einführung im November 2024 hat die Community Tausende von MCP-Servern entwickelt, mit SDKs für alle gängigen Sprachen und über 97 Millionen monatlichen Downloads zwischen Python und TypeScript.

Die strategische Bedeutung von MCP ist so groß, dass Anthropic es im Januar 2025 an die [Agentic AI Foundation](https://aitalk.it/it/agentic-ai-foundation.html) gespendet hat, einen von Anthropic, Block und OpenAI mit Unterstützung von Google, Microsoft, AWS, Cloudflare und Bloomberg gemeinsam gegründeten Fonds unter der Linux Foundation. Dieser Schritt verwandelt MCP von einem proprietären Protokoll in einen neutralen Industriestandard und beschleunigt potenziell die weltweite Einführung von AAIO.
![schema-aaio.jpg](schema-aaio.jpg)
[Bild von arxiv.org](https://arxiv.org/abs/2504.12482)

## Der tugendhafte (oder teuflische) Kreislauf

Das Paper führt ein faszinierendes Konzept ein: die symbiotische Beziehung zwischen der Optimierung von Plattformen und der Leistung der KI. Je mehr Websites AAIO implementieren, desto besser wird die Leistung der KI-Agenten. Effektivere Agenten regen weitere Plattformen zur Optimierung an. Dieser tugendhafte Kreislauf erinnert an die Entwicklung von SEO, bei der gut optimierte Websites Google verbesserten, das wiederum die Optimierung mit höheren Rankings belohnte.

Aber es gibt einen entscheidenden Unterschied. Bei SEO war der Nutzen gegenseitig, aber asymmetrisch: Google gewann Daten und Traffic, die Websites gewannen an Sichtbarkeit. Bei AAIO ist die Dynamik komplexer. Wenn ein KI-Agent eine Transaktion auf einer optimierten E-Commerce-Website abschließt, wer erfasst dann den Wert der Kundenbeziehung? Der Agent weiß, dass der Benutzer spezifische Vorlieben hat, hat das Kaufverhalten verfolgt, hat Feedback gesammelt. Diese Verhaltensdaten, traditionell pures Gold für Vermarkter, fließen nun zu demjenigen, der den Agenten kontrolliert.

Floridi und sein Team werfen entscheidende Fragen auf: Wer wird aus diesem Kreislauf ausgeschlossen? Die Implementierung von AAIO erfordert technische Fähigkeiten, Ressourcen und Zugang zu Dokumentationen, die nicht jeder besitzt. Kleine Unternehmen, gemeinnützige Organisationen, unabhängige Content-Ersteller könnten sich in einem digitalen Ökosystem, das zunehmend für Tech-Giganten optimiert ist, die sich dedizierte AAIO-Teams leisten können, an den Rand gedrängt sehen.

Diese digitale Kluft ist nicht zufällig, sondern strukturell. Wie die Autoren schreiben, besteht die konkrete Gefahr, dass AAIO die bestehenden Ungleichheiten beim Zugang zu den Vorteilen der digitalen Wirtschaft verstärkt. Es ist dieselbe Dynamik, die wir bei der programmatischen Werbung gesehen haben, bei der diejenigen, die über die Ressourcen zur Echtzeitoptimierung verfügten, dominierten und diejenigen zurückließen, die sich keine ausgefeilten Infrastrukturen leisten konnten.

## Die GELSI-Implikationen: Governance, Ethik, Recht und Gesellschaft

Der dichteste und interessanteste Abschnitt des Papiers befasst sich mit den GELSI (Governance, Ethical, Legal, and Social Implications), ein Begriff, den Floridi in Studien zur Technikethik populär gemacht hat.

An der Governance-Front lautet die grundlegende Frage: Wer sollte die AAIO-Standards entwickeln? Ein organischer Prozess, der von der Industrie geleitet wird, wie es bei vielen Webstandards der Fall war? Oder ein Multi-Stakeholder-Ansatz, der Regulierungsbehörden, Akademiker, die Zivilgesellschaft und Endbenutzer einbezieht? Die Geschichte von SEO legt nahe, dass Standards, die von unten nach oben entstehen, dazu neigen, diejenigen zu begünstigen, die bereits technologische und wirtschaftliche Macht besitzen.

Die ethischen Fragen sind noch heikler. Wenn ein autonomer KI-Agent einen Fehler auf der Grundlage von AAIO-optimierten Inhalten macht, wer trägt dann die Verantwortung? Der Website-Besitzer, der falsche strukturierte Daten bereitgestellt hat? Der Entwickler des Agenten, der die Informationen nicht angemessen validiert hat? Der Endbenutzer, der die Entscheidung an die KI delegiert hat?

Floridi betont, dass die aktuellen ethischen Rahmenwerke nicht auf Szenarien vorbereitet sind, in denen die Handlungsfähigkeit auf Menschen, Algorithmen und digitale Infrastrukturen verteilt ist. Das Konzept der "Agency ohne Intelligenz", das er in [früheren Arbeiten](https://www.researchgate.net/publication/389450555_AI_as_Agency_without_Intelligence_On_Artificial_Intelligence_as_a_New_Form_of_Artificial_Agency_and_the_Multiple_Realisability_of_Agency_Thesis) entwickelt hat, wird besonders relevant: Diese Systeme handeln, ohne zu verstehen, entscheiden, ohne zu urteilen, beeinflussen, ohne Absicht.

Auf der rechtlichen Seite hebt das Papier unmittelbare Spannungen mit der europäischen DSGVO hervor. Wenn ein KI-Agent beim Surfen auf AAIO-optimierten Websites personenbezogene Daten sammelt und verarbeitet, wer ist dann der Datenverantwortliche? Die aktuellen rechtlichen Kategorien der "Datenerhebung" setzen eine direkte menschliche Absicht voraus. Aber in Szenarien, in denen ein Agent autonom handelt und übergeordnete Ziele verfolgt, bricht die Verantwortungskette zusammen.

Dann gibt es noch die Frage des europäischen KI-Gesetzes, das 2024 in Kraft getreten ist. Dieser Regulierungsrahmen wurde entworfen, bevor die agentische KI zum Mainstream wurde, und hat Schwierigkeiten, diese Systeme zu klassifizieren. Sind sie Werkzeuge? Sind sie autonom? Erfordern sie eine kontinuierliche menschliche Aufsicht oder können sie unabhängig arbeiten? Floridi merkt an, dass die regulatorische Unklarheit die vorteilhafte Einführung der agentischen KI verlangsamen, aber auch Raum für Missbrauch in weniger strengen Rechtsordnungen schaffen könnte.

## Die konkreten Risiken: Manipulation, Voreingenommenheit und Überwachung

Das Papier beschränkt sich nicht auf philosophische Spekulationen, sondern identifiziert greifbare und aktuelle Risiken. Das erste ist die Manipulation: AAIO-optimierte Websites könnten so gestaltet sein, dass sie die Entscheidungen von KI-Agenten subtil beeinflussen, ähnlich wie es Dark Patterns bei Menschen tun, aber mit größerer Wirksamkeit, da Agenten keinen angeborenen Skeptizismus haben.

Das zweite betrifft die Verstärkung von Vorurteilen. Wenn die Datensätze, auf denen KI-Agenten trainiert werden, bereits systemische Vorurteile widerspiegeln und wenn AAIO-optimierte Websites bestimmte Informationsmuster auf Kosten anderer verstärken, ist das Ergebnis eine Rückkopplungsschleife, die bestehende Diskriminierungen verfestigt. Floridi zitiert ausdrücklich die [Arbeit von Virginia Eubanks](https://www.wired.it/attualita/tech/2019/03/11/algoritmi-discriminazione-welfare/) darüber, wie automatisierte Systeme Ungleichheiten verstärken.

Das dritte Risiko ist die Überwachung. Jede Interaktion zwischen einem KI-Agenten und einer AAIO-optimierten Website erzeugt granulare Daten über Verhaltensweisen, Vorlieben und Entscheidungsmuster. Wer kontrolliert diese Daten? Wie werden sie monetarisiert? Welche Schutzmaßnahmen gibt es gegen Missbrauch?

## Was jetzt zu tun ist

Im abschließenden Abschnitt schlagen Floridi und sein Team konkrete Richtungen vor. Auf technischer Ebene ist die dringende Entwicklung offener und interoperabler Standards für AAIO erforderlich, die von Multi-Stakeholder-Konsortien und nicht von einzelnen Unternehmen verwaltet werden. Auf regulatorischer Ebene müssen die Gesetzgeber Rahmenwerke wie die DSGVO und das KI-Gesetz aktualisieren, um verteilte Handlungsfähigkeit und autonome Interaktionen explizit zu berücksichtigen.

Im Bildungsbereich muss eine neue Generation von Fachleuten ausgebildet werden, die sowohl die technischen Aspekte von AAIO als auch die ethischen und sozialen Implikationen verstehen. Es reicht nicht aus, JSON-LD implementieren zu können; man muss verstehen, wie diese technischen Entscheidungen beeinflussen, wer Zugang zu den Vorteilen der agentischen Wirtschaft haben wird und wer davon ausgeschlossen bleibt.

Das Papier schließt mit einem Aufruf zur Proaktivität. Wie Floridi bei anderen Gelegenheiten betonte: "Der beste Weg, den Technologiezug zu erwischen, ist nicht, ihm nachzujagen, sondern an der nächsten Station zu sein." Wir müssen uns jetzt mit den GELSI-Implikationen von AAIO befassen, bevor die Muster in schwer zu ändernden Infrastrukturen zementiert werden.

Das Zeitalter der agentischen KI ist keine hypothetische Zukunft, sondern eine sich schnell entwickelnde Gegenwart. AAIO ist keine Technologie, die wir uns leisten können, zu ignorieren oder nur den IT-Abteilungen zu überlassen. Es ist eine Angelegenheit, die die Architektur unseres gesamten digitalen Ökosystems betrifft, mit Verzweigungen, die Wirtschaft, Demokratie, soziale Gerechtigkeit und individuelle Rechte berühren.

Die Frage ist nicht, ob wir für KI-Agenten optimieren sollten, sondern wie wir dies so tun können, dass diese Optimierung dem Gemeinwohl dient und nicht nur denen, die bereits technologische Macht besitzen. Es ist eine Herausforderung, die, wie immer in Floridis Arbeit, erfordert, philosophisch über Technologie nachzudenken, bevor die Technologie für uns denkt.
