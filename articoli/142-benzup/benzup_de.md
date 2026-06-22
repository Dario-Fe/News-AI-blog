---
tags: ["Applications", "Ethics & Society", "Generative AI"]
date: 2026-06-22
author: "Dario Ferrero"
---

# BenzUp: Ich habe eine App erstellt, ohne eine einzige Zeile Code zu schreiben
![benzup.jpg](benzup.jpg)

*Es gibt einen präzisen Moment, in dem eine Idee aufhört, eine Kneipenfantasie zu sein, und zu etwas Konkretem wird. In meinem Fall waren die Hauptdarsteller dieses Moments in dieser Reihenfolge: die Benzinpreise, ein amerikanischer Ingenieur, der sich über ein teures Bier in Dublin ärgerte, und ein KI-Modell, das für jeden mit einer Internetverbindung zugänglich ist. Das Ergebnis heißt [BenzUp](https://benzup.netlify.app), ist kostenlos, macht nichts Revolutionäres, und vielleicht ist es genau deshalb erzählenswert.*

In den letzten Wochen war das Thema der hohen Kraftstoffpreise zu einer ständigen Präsenz in Gesprächen unter Freunden, Kollegen und Bekannten geworden. Nicht die absolute Neuheit, wohlgemerkt: Der Benzinpreis ist seit jeher eines der nationalen Themen schlechthin, sehr zum Leidwesen derer, die lieber über etwas anderes sprechen würden. Aber die aktuelle internationale Situation hatte die Lautstärke der Debatte weiter erhöht, und man fragte sich oft, wo es sich lohnte zu tanken, welche Tankstellen ehrlicher waren, ob es sich lohnte, ein paar Kilometer mehr zu fahren, um etwas zu sparen. Legitime Fragen, auf die niemand eine schnelle und überprüfbare Antwort hatte.

Ich beobachtete derweil, machte mir geistige Notizen und tat nichts. Wie man es mit den meisten guten Ideen macht: Man lässt sie reifen, bis etwas kommt, das sie freisetzt.

## Die Guinness-Story

Die Freisetzung kam eines Morgens in Form einer Nachricht, von der ich nie gedacht hätte, dass ich sie lesen würde. Matt Cortland, ein amerikanischer Ingenieur mit irischen Wurzeln und Sitz in London, hatte in einem Pub in Dublin 7,80 Euro für ein Pint Guinness bezahlt. Eine Summe, die für jeden, der das fast heilige Verhältnis zwischen den Iren und ihrem Nationalbier kennt, kaum weniger als eine Beleidigung ist. Bei seinen Nachforschungen entdeckte Cortland, dass das Central Statistics Office Irlands 2011 aufgehört hatte, die Bierpreise zu überwachen, was ein Informationsvakuum von vierzehn Jahren hinterließ. Seine Reaktion? Er baute einen Sprachagenten namens Rachel mit nordirischem Akzent, der am St. Patrick's Wochenende 2026 etwa 2.300 Pubs in allen 32 Grafschaften der Insel anrief und nur eine Frage stellte: Was kostet ein Pint Guinness? Die Kosten für die gesamte Operation: etwa zweihundert Euro. Das Ergebnis: der [Guinndex](https://guinndex.ai), eine interaktive Karte der Guinness-Preise in Irland, erstellt mit Claude von Anthropic auf Basis von über 1.200 gesammelten Antworten. Häufigster festgestellter Preis: 5,50 Euro pro Pint. Absoluter Rekord: 11 Euro im The Temple Bar Pub in Dublin, was dessen Berufung, Touristen mit einer fast schon bewundernswerten Konsequenz zu schröpfen, bestätigt.

Cortlands erklärtes Ziel ist explizit: „Ich möchte sehen, ob wir gemeinsam die Kosten für ein Pint in ganz Irland senken können.“ Der Guinndex ist zu einer offenen Crowdsourcing-Plattform geworden, auf der jeder Preise melden und zu deren Aktualisierung beitragen kann. Und es gibt erste Anzeichen für sinkende Preise, auch wenn diese vorerst schwer mit der Initiative in Verbindung zu bringen sind.

Die Geschichte ist sympathisch, die Idee brillant, die Ausführung elegant. Aber vor allem hat sie bei mir den Schalter umgelegt, der seit Wochen darauf gewartet hatte. Wenn jemand KI genutzt hatte, um den Bierpreis in ganz Irland für zweihundert Euro zu kartieren, konnte ich sie nutzen, um etwas Nützliches für Autofahrer zu bauen, ohne auch nur einen Cent auszugeben. Ich hatte nicht den Ehrgeiz, den Benzinpreis zu senken, so wie es Cortlands Hoffnung für das Guinness war, aber zumindest konnte ich eine schnelle Orientierung geben, wo es sich lohnte anzuhalten.
![screenshot-guinndex.jpg](screenshot-guinndex.jpg)
[Screenshot von Guinndex.ai](https://guinndex.ai/)

## Die Daten waren schon da, kostenlos

Bevor man sich kopfüber in die Entwicklung stürzt, ist immer eine Online-Recherche ratsam. Und hier kommt die erste angenehme Überraschung: Das Ministerium für Unternehmen und das „Made in Italy“ veröffentlicht jeden Morgen im offenen Format und für jeden herunterladbar die Kraftstoffpreise aller italienischen Tankstellen. Zwei CSV-Dateien, täglich aktualisiert, die das vollständige Verzeichnis der im ganzen Land aktiven Anlagen mit Adresse, GPS-Koordinaten, Betreiber und Marke sowie die von den Betreibern mitgeteilten Preise enthalten, unterschieden nach Kraftstoffart und Abgabemodus (Selbstbedienung oder Bedienung). Die Daten werden unter der IODL 2.0-Lizenz veröffentlicht, die die freie Weiterverwendung auch für kommerzielle Zwecke erlaubt, sofern die Quelle angegeben wird. Das Ministerium toleriert die Nutzung dieser Daten nicht nur, es fördert sie aktiv.

Das war genau das, was ich brauchte. Kein Scraping, keine rechtlichen Grauzonen, keine Abhängigkeit von Drittanbieter-APIs, die die Nutzungsbedingungen von heute auf morgen ändern könnten. Offizielle, offene Daten, jeden Morgen aktualisiert.

Zu diesem Zeitpunkt beschloss ich, klein und fokussiert zu bleiben: keine nationale App, keine Ambitionen zur Skalierung. Nur meine Provinz, das VCO (das Kürzel VB in den Daten des Ministeriums), gefiltert und einfach und schnell serviert. Ein schlanker Prototyp, um zu sehen, ob die Sache wirklich funktionierte.

## Der Prompt als Entwurfshandlung

Wer auch nur halbwegs regelmäßig mit KI arbeitet, weiß, dass die Qualität des Outputs entscheidend von der Qualität des Inputs abhängt. Ein vager Prompt führt zu vagen Ergebnissen. Dies ist kein Artikel über Prompting, aber es lohnt sich, ihm einen Absatz zu widmen, da es der handwerklichste Teil der gesamten Erfahrung war.

Ich legte die Anforderungen mit einer gewissen Präzision fest. Auf technischer Ebene: eine Web-App in reinem HTML, CSS und JavaScript, mit einer Serverless-Funktion auf Netlify, um die Aufrufe an das MIMIT zu verwalten und CORS-Probleme zu vermeiden, die Browser daran hindern, direkte Anfragen an externe Domänen zu stellen, Responsive Design optimiert für Mobilgeräte, Datenfilterung für die Provinz VCO, zwei nach Preis sortierte Ranglisten (vom günstigsten zum teuersten), eine für Benzin und eine für Diesel. Auf der Ebene der Benutzeroberfläche: ein sichtbarer Schalter zum Wechseln zwischen den Kraftstoffen, die wesentlichen Informationen für jede Tankstelle, eine Detailansicht, die durch Tippen auf die einzelne Anlage zugänglich ist, hervorgehobenes Referenzdatum und Quelle. Auf ästhetischer Ebene: moderner Stil, gepflegte Typografie, schlichte Palette, etwas, das entworfen und nicht generiert aussah.

Ich entschied mich bewusst für Claude Sonnet 4.6, die kostenlos zugängliche Version, eben weil ich testen wollte, was mit den Werkzeugen möglich ist, die jedem zur Verfügung stehen, nicht nur denjenigen mit einem Premium-Abonnement oder Kompetenzen eines Senior-Entwicklers. Wenn es mit dem kostenlosen Modell funktionierte, ergab die Geschichte auch für diejenigen Sinn, die keinen technischen Hintergrund haben.

Innerhalb von ein paar Minuten entstanden etwa 750 Zeilen Code. Eine HTML-Datei mit allem inklusive: Struktur, Stil, Logik, Fehlerbehandlung, Animationen, Detailansicht mit Swipe-Geste zum Schließen. Ich hatte schon früher KI-Modelle genutzt, um kleine Codestücke, einige Funktionen oder eine isolierte Komponente zu schreiben. Aber noch nie etwas von dieser Komplexität auf einen Schlag. Die erste Überraschung war das Öffnen dieser Datei im PC-Browser: Alles funktionierte genau so, wie ich es beschrieben hatte. Korrektes Layout, Schalter zwischen Benzin und Diesel, Detailansicht, flüssige Animationen. Natürlich ohne echte Daten, aber die Struktur entsprach exakt den Anforderungen.

## Vom Browser in die Produktion

Eine HTML-Datei zu haben, die lokal funktioniert, ist eine Sache. Sie online zu haben, mit echten Daten vom Ministerium, ist eine andere. Dies ist der Schritt, in dem eine minimale Vertrautheit mit den verfügbaren Werkzeugen den Unterschied machte.

Ich erstellte ein Repository auf GitHub, lud die Dateien hoch und verknüpfte das Repository mit meinem Netlify-Account. Netlify erkannte automatisch die Konfiguration, aktivierte die Serverless-Funktion, die die CSVs des MIMIT herunterlädt und filtert, und in wenigen Minuten war die App online. Zweite Überraschung: Sie funktionierte. Die Daten kamen an, die Tankstellen der Provinz VB erschienen nach Preis sortiert, der Schalter zwischen Benzin und Diesel reagierte wie erwartet.

An diesem Punkt tat ich etwas, das ich bei der Arbeit mit KI-generiertem Code immer empfehle: einen Abgleich mit einem anderen Werkzeug. Ich verband Jules, den asynchronen KI-Agenten von Google, der direkt in GitHub integriert ist, und bat ihn um eine Analyse des Codes. Jules meldete keine relevanten Probleme, was zwar keine absolute Garantie ist, aber dennoch ein zweites Paar computergestützter Augen auf die geleistete Arbeit darstellt.

Mit Jules nahm ich dann einige Ergänzungen vor, die die App mehr wie eine native Anwendung wirken ließen. Es wurde eine JSON-Manifest-Datei hinzugefügt, die die Installation auf dem Telefon direkt aus dem Browser erlaubt, ohne über die Stores zu gehen, ein benutzerdefiniertes Icon und eine Seite mit nützlichen Informationen, Erklärungen zur Funktionsweise, zur Herkunft der Daten, zu den Grenzen des Systems und Anweisungen zur Installation auf Android und iPhone. Diese Seite erwies sich, wie wir sehen werden, als wichtiger als erwartet.
![benzup-screenshot.jpg](benzup-screenshot.jpg)
[Screenshot von BenzUp](https://benzup.netlify.app)

## Grenzen sind Teil des Produkts

Ein Tag persönlicher Tests, dann die Verbreitung in einem Freundeskreis mit der expliziten Bitte, jedes Problem zu melden. Die Rückmeldungen waren positiv, aber es kam eine wiederkehrende Meldung: Die Preise einiger Tankstellen schienen seit Tagen stillzustehen. Kein Bug der App, sondern einfach die Realität des Systems: Die Betreiber sind gesetzlich verpflichtet, Preisänderungen dem Ministerium mitzuteilen, aber nicht alle tun dies täglich. Zudem werden die Daten jeden Morgen mit Bezug auf 8:00 Uhr des Vortags veröffentlicht, und die tatsächliche Aktualisierung in der App kann sich aufgrund der Veröffentlichungszeiten des Ministeriums und der technischen Infrastruktur, auf der die App gehostet wird und auf die ich keinen direkten Einfluss habe, um einige Stunden verzögern.

Diese Meldung führte dazu, die Informationsseite zu verbessern, indem eine klare Erklärung dieser Mechanismen hinzugefügt wurde. Zudem wurde darauf hingewiesen, dass man durch Antippen der Karte einer einzelnen Tankstelle das Datum der letzten an das Ministerium übermittelten Aktualisierung überprüfen kann. Transparenz ist keine Option, sie ist integraler Bestandteil eines Dienstes, der auf öffentlichen Daten basiert und kein Interesse daran hat, präziser zu erscheinen, als er ist.

Es kam auch eine gezielte Anfrage: Autogas (GPL) und Erdgas (Metan) hinzuzufügen – Kraftstoffe, die für viele Autofahrer in der Provinz alles andere als zweitrangig sind. In den folgenden Tagen integrierte ich sie, und nun zeigt BenzUp die Ranglisten für alle vier Kraftstoffarten an.

## Drei Tage, 800 Besuche

Die App ist seit drei Tagen online, während ich diesen Artikel schreibe (11. April 2026). Ich habe sie mit einem Post auf dem lokalen Blog gestartet, den ich seit vielen Jahren betreue, [Verbania Notizie](https://www.verbanianotizie.it), ohne bezahlte Werbung, ohne Kampagne, ohne Wachstumsstrategie. In drei Tagen etwa 800 Besuche. Zahlen, die auf nationaler Ebene unbedeutend sind, wahrscheinlich sogar auf lokaler Ebene irrelevant, wenn man sie an den Parametern des digitalen Marketings misst. Aber das ist nicht der Punkt.

Der Punkt ist, dass von einer Idee, die in einem Gespräch über hohe Kraftstoffpreise entstand, bis zu einer in der Produktion funktionierenden App, die von Hunderten realen Menschen in meiner Provinz konsultiert wird, weniger als eine Woche vergangen ist. Ohne eine Zeile Code zu schreiben, ohne Budget, ohne ein Entwicklungsteam. Mit Kenntnis des Ökosystems der verfügbaren kostenlosen digitalen Werkzeuge, einem sorgfältig erstellten Prompt und der Bereitschaft, auf Basis von echtem Feedback zu iterieren, zu korrigieren und zu verbessern.

## Updates

Dieser Artikel wurde bereits im Codemotion-Magazin veröffentlicht. Zwei Monate später erscheint er nun auch auf dem Portal – ein kurzes Update also.

In den zwei Monaten seit der Veröffentlichung dieses Artikels hat sich BenzUp stetig weiterentwickelt, stets nach dem gleichen Prinzip: keine Kosten, keine komplexe Infrastruktur, alles basiert auf frei verfügbaren Tools. Die wichtigste Neuerung ist die geografische Erweiterung: Die App deckt nun die gesamte Region Piemont mit allen acht Bundesländern ab und bietet die Möglichkeit, über ein separates Menü nach Gemeinden zu filtern. Aus einem lokalen Tool für Autofahrer im VCO-Gebiet ist eine unverzichtbare Informationsquelle für alle geworden, die in der Region unterwegs sind.

Technisch wurde die Architektur grundlegend überarbeitet. Die Daten werden nicht mehr in Echtzeit mit jeder Anfrage verarbeitet, sondern jeden Morgen in statischen Dateien vorab generiert und direkt vom Netlify CDN bereitgestellt. Dies wirkt sich unmittelbar und messbar auf die Ladezeit aus. Eine GitHub-Aktion plant den Prozess automatisch, prüft vorab, ob das Ministerium aktualisierte Daten veröffentlicht hat, und generiert für jede Provinz eine JSON-Datei. Das Frontend liest die korrekte Datei und zeigt sie sofort an, ohne serverlose Funktionen zu verwenden.

Zusätzlich wurde ein Ampelsystem eingeführt, das die Aktualität der Daten jedes einzelnen Händlers anzeigt: Grün bedeutet, dass der Preis in den letzten 24 Stunden aktualisiert wurde, Gelb innerhalb der letzten 48 Stunden und Rot danach. Dies ist eine einfache und visuelle Möglichkeit, Nutzern Informationen bereitzustellen, für die zuvor das Öffnen der Detailseite jedes Händlers erforderlich war.

Über ein Meldeformular, das von der Seite jedes Händlers aus zugänglich ist, können Nutzer schließlich Unstimmigkeiten, veraltete Preise, geschlossene Werke oder Datenfehler melden. Diese kleine Maßnahme zur gemeinsamen Qualitätssicherung entspricht dem freiwilligen und transparenten Charakter des Projekts.

## Abschließende Überlegungen

Dies ist kein Loblied auf das Vibe-Coding – jene Praxis, Code schnell und ungenau zu generieren, indem man der KI blind vertraut, ohne zu verstehen, was man tut. Das Vibe-Coding scheint ohnehin bereits auf dem Weg zu sein, durch einen strukturierteren und professionelleren Ansatz abgelöst zu werden: die Projektspezifikationen in detaillierten Markdown-Dateien zu schreiben, die den Code-Agenten als präzise und überprüfbare Anweisungen übergeben werden, anstatt sich auf improvisierte Prompts zu verlassen. Ich habe darüber in einem [Artikel auf diesem Portal](https://aitalk.it/it/codespeak.html) geschrieben, und der Unterschied in Bezug auf Kontrolle und Qualität des Ergebnisses ist substanziell. Aber das ist wirklich eine andere Geschichte. Was ich erzählen möchte, ist etwas Einfacheres und vielleicht Interessanteres: Die KI hat die Distanz zwischen der Idee und ihrer Realisierung radikal verringert, auch für diejenigen ohne spezifische Programmierkenntnisse.

Dies bedeutet nicht, dass Programmierer, Ingenieure und Softwarearchitekten überflüssige Figuren geworden sind, im Gegenteil. Einen funktionierenden Prototyp in die Produktion zu bringen, ist eine Sache; etwas Stabiles, Sicheres und Skalierbares zu bauen, eine andere: Dafür braucht es reale Kompetenzen, Erfahrung und ein tiefes Verständnis der Systeme, das kein Prompt, und sei er noch so gut konstruiert, ersetzen kann.

In meinem Fall erlaubte eine gewisse Vertrautheit mit Online-Werkzeugen und eine Neugier als fortgeschrittener Nutzer, nicht als Experte, das Projekt in die Produktion zu führen, anstatt es beim Prototyp zu belassen. Aber die Schwelle ist für alle gesunken. Jeder mit einer klaren Idee, der Geduld, einen ordentlichen Prompt zu erstellen, und der Lust, die minimalen Mechanismen des Deployments auf Plattformen wie Netlify oder Vercel zu lernen, kann das Gleiche tun.

Irgendwo auf der Welt baut wahrscheinlich gerade jemand mit der richtigen Idee, ein wenig Tatkraft und einem kostenlosen Claude-Account etwas, das es noch nicht gibt. Vielleicht nicht das neue Facebook, aber etwas Nützliches für die Menschen um ihn herum. Und das scheint mir bereits genug zu sein.

In der Zwischenzeit: Wenn Sie Autofahrer im Piemonte sind (vorerst) und wissen wollen, wo Sie am günstigsten tanken können, [BenzUp wartet dort](https://benzup.netlify.app). Kostenlos, unabhängig und mit all seinen offen dargelegten Grenzen.

Und sollte es den Durchbruch schaffen und mit einem Milliarden-Exit zu einem Big-Tech-Unternehmen im Silicon Valley enden, erwarte ich Sie alle zu der großen Party, die ich in meiner Megavilla am Ufer des Lago Maggiore geben werde. Denn auch wenn ich steinreich sein sollte, werde ich dem treu bleiben, wo alles begann.
