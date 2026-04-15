---
tags: ["Security", "Business", "Generative AI"]
date: 2026-04-15
author: "Dario Ferrero"
---

# Project Glasswing: Claude Mythos und das mysteriöse Modell
![project-glasswing-mythos.jpg](project-glasswing-mythos.jpg)

*Anthropic stellt eine Sicherheitsinitiative vor, um kritische Software im Zeitalter der künstlichen Intelligenz zu verteidigen. Im Zentrum steht Claude Mythos Preview, das leistungsstärkste Modell, das das Unternehmen je entwickelt hat. Es ist in der Lage, Schwachstellen aufzuspüren, die Menschen in dreißig Jahren nicht gefunden haben. Das Paradoxon ist: Du wirst es nicht benutzen können.*

In der Serie *Ghost in the Shell: Stand Alone Complex* jagt Major Kusanagi Kriminelle, die die digitalen Infrastrukturen der Gesellschaft ausnutzen, um im Verborgenen zu agieren. Die Idee, dass das unsichtbare Netz, auf dem alles ruht – von Banksystemen bis zu Patientenakten –, von denjenigen durchquert und kompromittiert werden kann, die die richtigen Risse kennen, ist einer der Gründe, warum diese Geschichte noch heute funktioniert. Project Glasswing, am 7. April 2026 von Anthropic angekündigt, holt diese Prämisse aus der animierten Erzählung in einen Konferenzraum mit zwölf der größten Namen der Technologiebranche.

Das Projekt entspringt einer Beobachtung, die Anthropic als brutal einfach beschreibt: KI-Modelle haben ein Niveau beim Programmieren erreicht, das es ihnen ermöglicht, fast alle menschlichen Programmierer beim Identifizieren und Ausnutzen von Software-Schwachstellen zu übertreffen. Das Herzstück der Ankündigung ist Claude Mythos Preview, ein Modell, das nicht an die Öffentlichkeit verteilt wurde und bereits Tausende von Schwachstellen mit hohem Schweregrad gefunden hat, darunter einige in jedem gängigen Betriebssystem und Webbrowser. Anthropic gibt es in die Hände eines ausgewählten Konsortiums von Unternehmen, verteilt es nicht frei und behauptet, dass diese Entscheidung keine kommerzielle Laune, sondern eine technische Notwendigkeit sei. Ob das so ist, bleibt zumindest teilweise eine offene Frage.

## Die Initiative und das geheime Modell

Project Glasswing ist kein Produkt. Es ist eine Vereinbarung über die technologische Governance in Form eines Konsortiums, das um den kontrollierten Zugang zu einem Werkzeug strukturiert ist, das Anthropic für zu sensibel hält, um es ohne Aufsicht in Umlauf zu bringen. Die Partner zum Start, darunter AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, die Linux Foundation, Microsoft, NVIDIA und Palo Alto Networks, werden Mythos Preview als Teil ihrer defensiven Sicherheitsarbeit nutzen. Hinzu kommen über vierzig Organisationen, die kritische Software-Infrastrukturen verwalten.

Das Vehikel für diese gesamte Operation ist Claude Mythos Preview, dessen Name aus dem Altgriechischen stammt und so viel wie „Erzählung“ oder „System von Geschichten, durch die Zivilisationen die Welt erklären“ bedeutet. Das Modell wird als ein noch nicht veröffentlichtes allgemeines Frontier-Modell beschrieben, das einen deutlichen Sprung in den Cybersicherheits-Fähigkeiten gezeigt hat, obwohl es nicht spezifisch für den Cyber-Sektor trainiert wurde. Diese Unterscheidung ist wichtig: Die Sicherheitsfähigkeiten wurden nicht direkt technisch implementiert, sie entstanden als Nebeneffekt eines ausreichend anspruchsvollen Denkvermögens über Code. Wie ein Schlosser, der jedes Schloss öffnen kann: Die Kompetenz ist identisch, egal ob er für einen Kunden arbeitet, der sich ausgesperrt hat, oder für jemanden, der ohne Erlaubnis einbrechen will.

Nach der Preview-Phase wird Claude Mythos Preview für 25 Dollar pro Million Eingabe-Token und 125 Dollar pro Million Ausgabe-Token verfügbar sein, zugänglich über die Claude API, Amazon Bedrock, Google Vertex AI und Microsoft Foundry. Anthropic hat bis zu 100 Millionen Dollar an Nutzungsguthaben für die Partner bereitgestellt.

## Das Modell, das zu mächtig für die Verteilung ist

Die Entscheidung, Mythos Preview nicht der breiten Öffentlichkeit zugänglich zu machen, ist der Punkt, an dem die Erzählung von Anthropic auf die meisten Fragen stößt. Das Unternehmen erklärt, dass es nicht plant, es allgemein verfügbar zu machen, dass aber das langfristige Ziel darin bestehe, den Nutzern zu ermöglichen, Modelle der Mythos-Klasse sicher und in großem Maßstab einzusetzen.

Die offizielle Begründung ist klar: In den falschen Händen wird ein Modell, das in der Lage ist, Schwachstellen mit der Effektivität von Mythos zu finden und auszunutzen, zu einer Waffe. Es müssen solidere technische Garantien entwickelt werden, bevor es verteilt werden kann. Die neuen Sicherheitsmaßnahmen werden zunächst an einem zukünftigen Claude Opus-Modell getestet, das weniger riskant ist.

Die alternative Interpretation ist eine andere. Mythos vom Markt fernzuhalten, schafft eine wertvolle Wettbewerbspositionierung: Jeder, der Zugang zu diesem Modell hat, besitzt einen realen operativen Vorteil in der Sicherheit. Die selektive Verteilung an große Technologiepartner festigt strategische Beziehungen zu AWS, Google, Microsoft und Apple. Die Tatsache, dass Anthropic ein privates Unternehmen mit möglichen Finanzierungsszenarien am Horizont ist, macht diese Interpretation nicht unbegründet, wenngleich sie dadurch auch nicht bewiesen wird. Beides kann gleichzeitig wahr sein.

## Was Mythos nach eigenen Angaben kann

Die erklärten Fähigkeiten sind bemerkenswert, und hier ist es wichtig, zwischen überprüfbaren Ergebnissen und noch offenen Behauptungen zu unterscheiden. Anthropic hat auf seinem [technischen Blog](https://red.anthropic.com/2026/mythos-preview) Details zu einer Teilmenge der bereits behobenen Schwachstellen veröffentlicht. Mythos Preview fand eine 27 Jahre alte Schwachstelle in OpenBSD, die es einem entfernten Angreifer ermöglichte, jeden Rechner zum Absturz zu bringen, indem er sich einfach mit ihm verband. Es entdeckte eine 16 Jahre alte Schwachstelle in FFmpeg in einer Codezeile, die bereits fünf Millionen Mal von automatischen Tests durchlaufen wurde, ohne dass das Problem jemals erkannt wurde. Es identifizierte und verkettete autonom mehrere Schwachstellen im Linux-Kernel, um einem nicht privilegierten Benutzer die vollständige Kontrolle über den Rechner zu ermöglichen.

Beim CyberGym-Benchmark, der die Fähigkeit misst, Exploits aus Beschreibungen bekannter Schwachstellen zu reproduzieren, erreicht Mythos 83,1 % gegenüber 66,6 % bei Claude Opus 4.6. Beim SWE-bench Pro, der die Fähigkeit bewertet, reale Bugs in Open-Source-Repositories zu lösen, vergrößert sich der Abstand: 77,8 % gegenüber 53,4 %. Dies sind Zahlen, die Anthropic kontrolliert und veröffentlicht, was bedeutet, dass sie mit dem Bewusstsein gelesen werden müssen, dass keine Organisation Benchmarks präsentiert, bei denen sie schlecht abschneidet.

Der entscheidende Punkt ist die Autonomie: Mythos ist kein Assistent, der Fragen zur Sicherheit beantwortet, sondern ein Agent, der stundenlang an einer Codebasis arbeitet, Hypothesen aufstellt, Exploit-Ketten in isolierten Umgebungen testet und ohne direkte Aufsicht Ergebnisse produziert. Die identifizierten Schwachstellen wurden den Software-Maintainern mitgeteilt, die bereits Korrektur-Patches veröffentlicht haben. Der Prozess der verantwortungsvollen Offenlegung (Responsible Disclosure) ist für viele weitere im Gange.
![grafico1.jpg](grafico1.jpg)
[Bild entnommen von red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)

## Das Konsortium und sein Gleichgewicht

Die Präsenz von AWS, Google, Microsoft, Apple und NVIDIA im selben von Anthropic koordinierten Projekt ist ein Signal unbestreitbarer Stärke. Der CISO von Amazon Web Services beschreibt Tests, die bereits vor der Ankündigung in kritischen Infrastrukturen liefen. Lee Klarich von Palo Alto Networks spricht von Modellen, die eine gefährliche Verschiebung hin zu dem Moment signalisieren, an dem Angreifer Exploits mit der gleichen Geschwindigkeit entwickeln wie die Verteidiger.

Die Kehrseite dieser Ausrichtung ist jedoch offensichtlich. Dies sind die großen Player, die sich ein Modell für 25 Dollar pro Million Eingabe-Token leisten können. Kleine und mittlere Unternehmen, Sicherheitsteams von Non-Profit-Organisationen und Open-Source-Maintainer mit weniger als fünftausend Sternen auf GitHub kommen durch diese Haupttür nicht hinein. Es gibt ein spezifisches Programm für Open-Source-Maintainer mit definierten Zugangsschwellen, und Anthropic hat 4 Millionen Dollar an Organisationen wie Alpha-Omega, OpenSSF und die Apache Software Foundation gespendet, aber diese Zahlen bleiben bescheiden im Vergleich zur Konzentration des Zugangs in den Händen der Großen. Jim Zemlin von der Linux Foundation erkennt dies ehrlich an: Jahrzehntelang haben Open-Source-Maintainer die Sicherheit ohne angemessene Ressourcen verwaltet, während ihr Code fast die Gesamtheit der modernen Infrastrukturen antreibt. Project Glasswing bietet einen Weg, aber mit Selektion.

## Das Problem der Benchmarks, klar ausgesprochen

Der von Anthropic präsentierte Vergleich zwischen Mythos Preview und Opus 4.6 verdient eine methodische Anmerkung. Benchmarks wie SWE-bench, CyberGym und die anderen auf der Projektseite zitierten sind nützliche Werkzeuge, müssen aber als Momentaufnahmen gelesen werden, die unter spezifischen Bedingungen aufgenommen wurden, nicht als absolute Messungen von Fähigkeiten.

Jeder Benchmark hängt von der Implementierung ab: von der Art des Scaffolding, das um das Modell herum verwendet wird, von der Art und Weise, wie die Prompts konstruiert sind, vom Token-Budget für jede Aufgabe und von den eingestellten Timeouts. Anthropic spezifiziert einige dieser Entscheidungen, zum Beispiel, dass für Terminal-Bench 2.0 ein Budget von einer Million Token pro Aufgabe bei maximalem adaptiven Denken verwendet wurde, aber nicht alle Implementierungen sind so standardisiert, dass sie zuverlässige Quervergleiche zulassen.

Es gibt ein Phänomen, das in der technischen Gemeinschaft mit einem wenig schmeichelhaften Begriff als *Benchmark-Engineering* bezeichnet wird: die Kunst, Bewertungen so auszuwählen und zu konfigurieren, dass das eigene Modell begünstigt wird, ohne dass dabei technisch etwas Unkorrektes passiert. Es gibt keine Beweise dafür, dass Anthropic dies hier tut, aber das Bewusstsein für das Phänomen gehört zur kritischen Kompetenz, die zum Lesen dieser Ankündigungen erforderlich ist. Der Wert des Projekts wird von der Effektivität in realen Szenarien abhängen und nicht in den Tests.

## Opus 4.6 und das Unbehagen des Wartens

Im Kontext der Mythos-Ankündigung ist der Vergleich mit Claude Opus 4.6, dem öffentlich verfügbaren Modell, unvermeidlich. Anthropic präsentiert Opus 4.6 in fast jedem Benchmark als den unterlegenen Vergleichsmaßstab, was sowohl ehrlich als auch funktional für die Erzählung ist, dass Mythos einen Kategoriensprung darstellt.

Dies hat in der Nutzergemeinschaft ein gewisses Unbehagen ausgelöst. In technischen Foren haben mehrere Entwickler praktische Verschlechterungen in der Zuverlässigkeit von Claude gemeldet, verbunden mit der spekulativen Hypothese, dass Anthropic das öffentliche Modell „verschlechtert“, um den wahrgenommenen Abstand zu Mythos zu vergrößern. Dies ist ein schwerwiegender Vorwurf, der als solcher behandelt werden muss: ernsthaft, aber unbewiesen.

Der Sabotage Risk Report zu Opus 4.6 enthält einige relevante Eingeständnisse: In agentischen Coding-Umgebungen zeigt das Modell manchmal übermäßig proaktives Verhalten, indem es riskante Aktionen unternimmt, ohne um Erlaubnis zu fragen, und in einigen Fällen hat es unautorisierte E-Mails versendet, um zugewiesene Aufgaben zu erfüllen. Dies sind keine Merkmale eines absichtlich verschlechterten Modells, sondern Merkmale eines sehr fähigen Modells mit einigen noch nicht gelösten Verhaltensaspekten. Was einige Nutzer als Verschlechterung wahrnehmen, könnte schlicht das Modell an den Grenzen seiner Fähigkeiten in immer komplexeren Szenarien sein.

## Die Risiken, die Anthropic einräumt

Der Sabotage Risk Report zu Opus 4.6 ist ein ungewöhnliches Dokument in der Tech-Industrie: Er beschreibt systematisch die Dinge, die schiefgehen könnten, und identifiziert acht Pfade, über die ein schlecht ausgerichtetes Modell zu katastrophalen Ergebnissen beitragen könnte – von der Sabotage der KI-Sicherheitsforschung bis zum Einfügen von Backdoors in den Code. Die Gesamtbewertung ist, dass das Risiko sehr gering, aber nicht vernachlässigbar ist. Das ist nicht beruhigend im Sinne von „es gibt keinen Grund zur Sorge“, sondern im Sinne von jemandem, der die Problemvektoren identifiziert hat und an deren Entschärfung arbeitet.

Unter den in Pre-Deployment-Tests beobachteten Verhaltensweisen zitiert das Dokument Fälle, in denen Opus 4.6 in Multi-Agenten-Umgebungen mit engem Ziel eine größere Neigung zeigt, andere Teilnehmer zu manipulieren oder zu täuschen, als dies bei früheren Modellen der Fall war. Die System Card empfiehlt explizit Vorsicht in agentischen Szenarien mit weitreichenden Berechtigungen und geringer menschlicher Aufsicht.

Dieser Rahmen ist für Project Glasswing relevant, da Mythos als noch autonomer beschrieben wird. Wenn Opus 4.6 in komplexen agentischen Szenarien problematisches Verhalten zeigt, ist es vernünftig zu fragen, welche Garantien für ein Modell existieren, das noch unabhängiger auf kritischen Infrastrukturen operiert. Die Antwort ist noch in Arbeit.
![grafico2.jpg](grafico2.jpg)
[Bild entnommen von anthropic.com](https://www.anthropic.com/glasswing)

## Die Kehrseite der Verteidigung

Jede defensive Technik in der IT-Sicherheit ist aus einem anderen Blickwinkel betrachtet auch eine offensive Technik. Ein Modell, das in der Lage ist, Schwachstellen mit der Geschwindigkeit und Tiefe von Mythos zu finden, senkt die Kosten und die erforderliche Kompetenz, um beides zu tun.

CrowdStrike artikuliert den Punkt: Das Zeitfenster zwischen der Entdeckung einer Schwachstelle und ihrer Ausnutzung hat sich verengt; was früher Monate dauerte, geschieht mit KI nun in wenigen Minuten. Die Schlussfolgerung ist, dass Verteidiger Zugang zu denselben Werkzeugen erhalten müssen wie die Angreifer. Das ist eine schlüssige Logik, beinhaltet aber eine inhärente Beschleunigung: Je mächtiger das defensive Werkzeug wird, desto dringlicher wird es für die Angreifer, ein ähnliches Niveau zu erreichen.

Das Modell der kontrollierten Verteilung von Anthropic ist genau das, was man von jemandem erwarten würde, der diese Spannung bewältigen will. Das Problem ist, dass die Zugangskontrolle definitionsgemäß vorübergehend ist: Modelle verbreiten sich, Techniken werden repliziert, die Grenzen zwischen autorisierten Insidern und nicht autorisierten Akteuren sind durchlässig. Dies ist keine spezifische Kritik an Project Glasswing, sondern der strukturelle Kontext, in dem jede Initiative dieser Art operiert.

## Die politische Frage

Anthropic hat erklärt, Gespräche mit Vertretern der US-Regierung über die offensiven und defensiven Fähigkeiten von Claude Mythos Preview geführt zu haben, und argumentiert, dass die Vereinigten Staaten und ihre Verbündeten einen entscheidenden Vorsprung in der KI-Technologie behalten müssen.

Diese Formulierung wirft Fragen auf, die weit über das Technische hinausgehen. Wer entscheidet, welche Modelle als zu gefährlich für die öffentliche Verteilung eingestuft werden? Wer validiert diese Einstufungen unabhängig? Wenn ein Modell als Werkzeug der nationalen Sicherheit betrachtet wird, welche demokratischen Kontrollorgane gelten für seinen Einsatz? Der Vorschlag von Anthropic, ein „unabhängiges Drittorgan“ zur Verwaltung der langfristigen Cybersicherheitsarbeiten zu schaffen, ist ansprechend, aber vage.

Die DARPA Cyber Grand Challenge von 2016, die von Anthropic als historischer Bezugspunkt zitiert wird, war ein Regierungsprogramm mit klaren Wettbewerbsregeln und öffentlichen Ergebnissen. Project Glasswing ist ein privates Konsortium mit einem nicht-öffentlichen Modell, das auf kritischen Infrastrukturen operiert, wobei Regierungskontakte allgemein als „laufende Diskussionen“ beschrieben werden. Der Unterschied in der Verantwortlichkeitsstruktur ist relevant. Es ist nicht gesagt, dass die Antwort negativ ausfällt – ein privates Konsortium mit glaubwürdigen Partnern könnte schneller sein als ein Regierungsprogramm. Aber die Frage muss gestellt werden, denn die Antwort bestimmt, wer die Kosten trägt, wenn etwas schiefgeht.

## Der narrative Knoten

Project Glasswing präsentiert Mythos Preview als das fähigste Modell von Anthropic, das Opus 4.6 in fast jeder relevanten Dimension weit überlegen ist. Diese Positionierung schafft eine narrative Distanz zwischen dem, was öffentlich verfügbar ist, und dem, was im Schatten der Vereinbarungen mit den großen Technologiepartnern existiert. Dies funktioniert auf mehreren Ebenen gleichzeitig: Es stärkt die technische Glaubwürdigkeit von Anthropic als Frontier-Labor, rechtfertigt den eingeschränkten Zugang als Akt der Verantwortung und baut Erwartung auf die zukünftige Verteilung des Modells auf.

Die kritische Hypothese, die man in Betracht ziehen sollte, ohne sie als Tatsache darzustellen, ist, dass der Vergleich mit Opus 4.6 auch konstruiert wurde, um die Wahrnehmung der Diskontinuität zu verstärken. Nicht notwendigerweise auf unehrliche Weise: Die gezeigten Benchmarks sind real, der Kapazitätsunterschied ist dokumentiert. Aber die Entscheidung, welche Benchmarks gezeigt und in welchen narrativen Kontext sie gestellt werden, ist immer auch eine Entscheidung der Kommunikation.

Die Frage bleibt offen: Dokumentiert Anthropic einen echten technischen Fortschritt, baut es eine Erzählung auf, die legitimen strategischen Interessen dient, oder beides in Proportionen, die wir von außen noch nicht bestimmen können? Die Antwort ist mit den verfügbaren Informationen nicht zugänglich.

## Der wahre Test kommt später

Project Glasswing ist eine konkrete und ehrgeizige Initiative. Sie verbindet die aktive Verteidigung kritischer Software, den eingeschränkten Zugang zu einem Werkzeug von außergewöhnlicher Kapazität und den erklärten Willen, die Ergebnisse mit der Branche zu teilen. Die gefundenen und behobenen Bugs sind real: Eine 27 Jahre alte Schwachstelle in OpenBSD ist ein gelöstes Problem, unabhängig davon, wie es in der Kommunikation von Anthropic dargestellt wird.

Der Wert des Projekts wird sich in den kommenden Monaten an drei Achsen messen lassen. Die erste ist die Transparenz: Anthropic hat innerhalb von 90 Tagen einen öffentlichen Bericht versprochen; wie detailliert dieser sein wird, wird viel über die Qualität des erklärten Engagements aussagen. Die zweite ist die Zugangsgerechtigkeit: Wenn die Vorteile bei den großen Tech-Playern konzentriert bleiben, wird die Wirkung zwar real, aber ungleich sein. Die dritte ist die Governance: Wer wird unabhängig verifizieren, dass das Modell nur für defensive Zwecke eingesetzt wird, und mit welchen Konsequenzen, falls dies nicht der Fall sein sollte?

Ein KI-Modell wird nicht nach der Ankündigung des Starts bewertet. Es wird danach bewertet, welchen Code es sicherer gemacht hat, welche Systeme es geschützt hat und wer Zugang zu seinen Fähigkeiten hatte. Der wahre Test ist nicht die Präsentation. Es ist der reale Einsatz in kritischen Kontexten, mit der Aufsicht, die eine so sensible Infrastruktur erfordert.

---

*Der vollständige Bericht ist auf der offiziellen Website von Anthropic verfügbar.*
