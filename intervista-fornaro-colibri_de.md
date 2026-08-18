---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Vincenzo Fornaro und Colibrì: "Mich interessiert nicht das Genie, mich interessiert die Neugier"
![intervista-fornaro-colibri.jpg](intervista-fornaro-colibri.jpg)

*Über Colibrì habe ich bereits geschrieben und erzählt, wie es möglich ist, ein Mixture-of-Experts-Modell mit 744 Milliarden Parametern auf einem Computer mit gerade einmal 25 GB RAM auszuführen, indem man die Festplatte als intelligente Speicher-Ebene statt als einfachen Container behandelt ([Sie können die vollständige technische Analyse hier lesen](https://aitalk.it/it/colibri.html)). Was noch fehlte, war die Stimme desjenigen, der diesen Motor geschrieben hat – Datei für Datei in C, alleine, ohne Labor und ohne Cluster im Rücken. Ich habe mich mit Vincenzo Fornaro unterhalten, um mir den Weg hinter dem Code erzählen zu lassen, und das Gespräch wurde länger und anregender, als ich vorhergesehen hatte.*

## Von einem Lagerhaus in Brescello zu einer Idee, der nachts nachgegangen wurde

Online findet man über Vincenzo extrem wenig. Sein [GitHub](https://github.com/JustVugg/colibri)-Profil beschränkt sich auf eine Zeile: "Founder of Colibrì, a tiny engine, immense model". Dennoch hat das Projekt innerhalb von drei Wochen über fünfundzwanzigtausend Sterne erreicht und ist ins Zentrum der Debatte über die Demokratisierung der künstlichen Intelligenz geraten. Ich habe ihn gefragt, wer er ist, noch bevor ich ihn fragte, wie er das gemacht hat.

"Ich glaube, dass es online schwierig ist, Informationen über mich zu finden, weil ich nie eine besonders kontaktfreudige Person war und vor allem nie ein großes Interesse daran hatte, mich selbst zur Schau zu stellen. Ich habe es immer vorgezogen, meine Projekte in den Vordergrund zu stellen.

Für mich war das Programmieren schon immer ein Ventil für die Fantasie. Jahrelang, besonders nachts, war ich einfach nur ich, ein Computer und eine Idee, über die ich nachdenken konnte. Ich habe nicht unbedingt programmiert, weil mich jemand darum gebeten hatte oder weil ich bereits ein Produkt zum Verkaufen im Kopf hatte. Oft habe ich programmiert, weil ich verstehen musste, ob eine Idee in meinem Kopf real werden konnte.

Ich hatte schon immer das Gefühl, dass das Projekt wichtiger ist als die Person, die es erschafft. Aber mit der Zeit habe ich auch noch etwas anderes verstanden: Wenn ein Projekt beginnt, für viele Menschen nützlich zu sein, hat derjenige, der es begonnen hat, die Verantwortung, ihm eine Richtung zu geben und um es herum die Bedingungen zu schaffen, damit es wachsen kann.

Ich bin in Tarent geboren, aber heute lebe ich in Brescello in der Emilia-Romagna, dem Dorf von Don Camillo und Peppone. Mein Leben war nicht besonders einfach: Ich wurde mit neun Jahren Waise, und für den Großteil meines Lebens waren die finanziellen Möglichkeiten begrenzt.

Ich habe in Bari Informatik studiert, konnte aber aus finanziellen Gründen das Studium ab einem gewissen Punkt nicht mehr fortsetzen. Also fing ich an, in einem Lagerhaus als Lagerarbeiter zu arbeiten.

Das Leben nimmt oft Wege, die man nicht geplant hat. Die Arbeit war eben diese, aber mein Kopf war weiterhin woanders. Ich habe nie aufgehört zu programmieren. Ich habe weiter gelernt, experimentiert und mir Anwendungen und Systeme vorgestellt.

Mich haben die Geschichten von Menschen sehr beeinflusst, die es geschafft haben, etwas aus Bedingungen aufzubauen, die alles andere als perfekt waren. Mich hat nicht interessiert, ihren Weg zu kopieren. Mich hat interessiert zu verstehen, wie sich eine Idee in etwas verwandeln kann, das die Art und Weise verändert, wie Menschen eine Technologie nutzen.

Aus technischer Sicht hatte ich schon immer eine besondere Vorliebe für C und C++. Ich habe sie seit der Universität studiert und halte sie weiterhin für außergewöhnliche Werkzeuge, wenn das Problem Kontrolle, Vorhersehbarkeit und Geschwindigkeit erfordert. Ich habe gerne so wenige Schichten wie möglich zwischen dem, was ich denke, und dem, was der Computer ausführt.

Colibrì ist genau so entstanden.

Ich wollte verstehen, ob es möglich ist, einen relativ gewöhnlichen Computer zu nehmen – selbst einen langsamen und ohne eine besonders leistungsstarke GPU – und es zu schaffen, ein riesiges Modell auszuführen.

Es gab keine Firma dahinter, es gab kein Team und es gab anfangs keinen Businessplan. Es gab ein technisches Problem, das mich neugierig genug machte, um Tag und Nacht daran zu arbeiten.

Als ich es gelöst hatte, blieb das Projekt eine Zeit lang auf meinem Computer. Dann habe ich mich fast zufällig entschieden, es auf GitHub zu veröffentlichen.

Von diesem Moment an geschah etwas, das ich nicht vorhergesehen hatte.

Die Leute fingen an, es auszuprobieren, darüber zu diskutieren, beizutragen und es zu nutzen. Colibrì begann, viel größer zu werden als das Experiment, aus dem es entstanden war.

Und genau da hat sich für mich auch die Perspektive geändert.

Colibrì ist nicht entstanden, weil ich ein Startup gründen wollte. Aber wenn Tausende von Menschen anfangen, dir direkt oder indirekt zu sagen, dass das Problem, das du angehen wolltest, auch sie interessiert, musst du anfangen dich zu fragen, wie groß die Lösung werden kann.

Heute ist das die Frage, die mich interessiert."

## Ein Modell öffnen, nicht nur nutzen

Die GitHub-Seite des Projekts liest sich fast wie ein Manifest: "Frontier models should not be sealed inside datacenters. Colibrì exists so that anyone curious enough can open one up." Ich frage ihn, was "Öffnen" eines Modells für ihn wirklich bedeutet – nicht einfach nur der Zugriff über eine API – und ob die Demokratie der KI, die er sich vorstellt, eine Frage des Zugangs oder etwas Tiefergehendes ist.

"Für mich sollte der Zugang zur KI so einfach wie möglich sein. Man sollte einen Computer einschalten, ein Programm öffnen und anfangen können zu experimentieren.

Es sollte keine Möglichkeit sein, die nur denjenigen vorbehalten ist, die Hardware für Zehntausende von Euro besitzen, oder denjenigen, die große Infrastrukturen nutzen können.

Aber ich glaube, dass der Zugang nur die erste Ebene ist.

Was mich noch mehr interessiert, ist die Möglichkeit, die Technologie, die man nutzt, zu kennen.

Wenn ich von einem 'offenen' Modell spreche, meine ich daher nicht einfach, eine Antwort erhalten zu können. Ich meine, es ausführen, beobachten, messen, Experimente machen und versuchen zu können zu verstehen, was passiert, wenn man etwas ändert.

Es gibt einen riesigen Unterschied zwischen der Nutzung einer Intelligenz und der Möglichkeit, sie zu studieren.

Das bedeutet nicht, dass die Cloud falsch ist. Die Cloud ist und wird weiterhin extrem wichtig sein. Es gibt Probleme, bei denen die Konzentration riesiger Rechenmengen in einem Rechenzentrum die beste Lösung ist.

Ich denke einfach, dass es nicht das einzige mögliche Modell sein sollte.

Es sollte auch eine andere Möglichkeit geben: immer mehr Inferenzkapazität nah an die Person, den Forscher, das Unternehmen oder das Gerät zu bringen, das sie benötigt.

Die Demokratisierung der KI sollte meiner Meinung nach daher sowohl eine Demokratisierung des Zugangs als auch eine Demokratisierung des Verständnisses sein.

Ich möchte nicht, dass die erste Frage einer Person lautet: 'Habe ich genug GPU, um dieses Ding auszuprobieren?'

Ich möchte, dass sie lautet: 'Was kann ich entdecken, wenn ich versuche, es zu tun?'

Die KI wird zu einem der mächtigsten Wissenswerkzeuge, die wir gebaut haben. Je mehr Menschen sie direkt ausprobieren können, desto höher wird die Wahrscheinlichkeit, dass jemand eine Nutzung, eine Optimierung oder sogar ein Paradigma findet, an das wir heute noch gar nicht gedacht haben.

Für mich sollte die Hauptvoraussetzung immer mehr die Neugier werden, nicht die Größe der Infrastruktur, die man besitzt."

## Ein Beitrag auf Hacker News, kein Manifest

Es gibt ein Detail, das mich von Anfang an fasziniert hat: Der Beitrag, mit dem Fornaro Colibrì auf Hacker News präsentierte, hieß nicht "Ich habe die ultimative Inferenz-Engine entwickelt", sondern schlicht "Getting GLM-5.2 running on my slow computer". Eine fast bescheidene Haltung für ein Ergebnis, das keineswegs bescheiden ist. Ich frage ihn, wann er begriff, dass aus dem persönlichen Experiment etwas anderes wurde, und welche Reaktion der Community ihn glauben ließ, dass sich die Dinge wirklich veränderten.

"Der Titel war einfach 'Getting GLM-5.2 running on my slow computer', weil das genau die Geschichte war.

Ich wollte nicht behaupten, die ultimative Inferenz-Engine gebaut zu haben. Ich hatte ein Problem gelöst, das ich interessant fand, und wollte erklären, wie.

Colibrì war nicht mit dem Ziel entstanden, ein Startup zu werden. Es war aus Neugier entstanden.

Dann passierten zwei Dinge.

Das erste war zu sehen, wie Menschen das, was ich gebaut hatte, tatsächlich nutzten.

Ich erinnere mich besonders an einen jungen Mann, der mir schrieb, um sich zu bedanken, weil er dank Colibrì Zugriff auf ein Modell erhalten hatte, das sonst eine viel teurere Maschine erfordert hätte.

Das hat mich viel mehr getroffen als die Anzahl der Sterne.

Weil ich zum ersten Mal nicht nur eine technische Lösung betrachtete. Ich betrachtete ein reales Problem, das für jemanden beseitigt wurde.

Das zweite war die Community.

Menschen, die ich nicht kannte, fingen an, Issues zu öffnen, Pull Requests zu machen, Hardware zu testen, Bugs zu finden und Optimierungen vorzuschlagen.

An diesem Punkt verstand ich, dass etwas Wichtiges geschah: Colibrì wuchs nicht, weil ich versuchte, jemanden davon zu überzeugen, dass es nützlich sei. Die Menschen kamen spontan, weil sie das Problem erkannten.

Für jemanden, der Technologie baut, ist das ein sehr starkes Signal.

Seitdem habe ich angefangen, Colibrì anders zu betrachten.

Es bleibt ein Open-Source-Projekt und ich möchte, dass es das weiterhin bleibt, aber ich denke, dass die Technologie und das Problem, das wir angehen, viel größere Auswirkungen haben können als das Repository, mit dem alles begann.

Der interessante Schritt ist jetzt zu verstehen, wie man dieses spontane Interesse in eine immer solidere, generalisierbarere und nutzbarere Technologie verwandelt.

Und um das zu tun, wird Colibrì unweigerlich auch über die Dimension einer einzelnen Person hinauswachsen müssen."
![colibri-dashboard.jpg](colibri-dashboard.jpg)
[Das Web-Dashboard von Colibrì, Bild aus dem offiziellen Repository entnommen](https://github.com/JustVugg/colibri)

## Eine Datei, dreizehnhundert Zeilen, keine Kompromisse

Das Herzstück von Colibrì ist eine einzelne C-Datei von etwa dreizehnhundert Zeilen, ohne Abhängigkeiten, ohne erforderliche GPU, ohne Python zur Laufzeit. In einer Zeit, in der vLLM, TensorRT-LLM und SGLang Projekte sind, die in Laboren mit großen Teams und komplexen Codebasen entstanden sind, klingt Fornaros Wahl fast wie ein Akt des Widerstands – ein bisschen wie hausgemachte Musikproduktionen mit vier Instrumenten, die es schaffen, dichter zu klingen als ein ganzes Orchester. Ich frage ihn, ob hinter dieser extremen Einfachheit eine rein architektonische Entscheidung oder eine philosophischere Überzeugung steckt.

"Es war anfangs eine architektonische Entscheidung, aber es ist auch zu einer Überzeugung geworden.

Wenn du versuchst, ein riesiges Modell auf einer relativ kleinen Maschine zum Laufen zu bringen, hat jede zusätzliche Schicht ihren Preis.

Du musst genau wissen, wo sich der Speicher befindet, wann er verschoben wird, was berechnet wird und warum etwas langsam ist.

C ermöglicht mir eine extrem direkte Kontrolle über diese Dinge.

Aber das bedeutet nicht, dass ich Komplexität immer für negativ halte.

Komplexität ist eine Investition.

Man muss sie einführen, wenn der Wert, den sie erzeugt, größer ist als die Kosten, die sie verursacht.

Zu Beginn konnte es sich Colibrì leisten, extrem klein zu sein. Heute kommen GPU-Backends, Server, Schnittstellen, neue Architekturen und andere Komponenten hinzu. Unweigerlich wird das Projekt wachsen.

Die Herausforderung besteht darin, zu wachsen, ohne die Lesbarkeit zu verlieren.

Ich möchte, dass das Herz des Systems etwas bleibt, das ein guter Entwickler öffnen, lesen und verstehen kann.

Das hat auch einen sehr konkreten Vorteil für ein Open-Source-Projekt: Es senkt die Hürde für diejenigen extrem, die beitragen möchten.

Einfachheit ist in diesem Sinne nicht nur Eleganz.

Es ist Entwicklungsgeschwindigkeit, Debugging-Fähigkeit, Leichtigkeit des Experimentierens und die Möglichkeit, neue Leute in das Projekt einzubinden."

## Die Festplatte als Speicher, nicht als Lagerhaus

Der Mechanismus hinter Colibrì hat eine fast minimalistische Eleganz: Der dichte Teil des Modells bleibt im RAM ansässig, während die Experten nur bei Bedarf von der Festplatte abgerufen werden – ähnlich wie der JIT-Compiler bestimmter Sprachen, der nicht alles im Voraus übersetzt, sondern nur das, was die Ausführung tatsächlich verlangt, Augenblick für Augenblick. Ich frage Fornaro, was für jemanden, der sich Colibrì zum ersten Mal nähert, das am schwersten zu verdauende, kontraintuitivste Konzept ist.

"Wahrscheinlich ist das kontraintuitivste Konzept folgendes: Ein gigantisches Modell nutzt nicht notwendigerweise alle seine Parameter im selben Moment.

Wenn eine Person '744 Milliarden Parameter' hört, stellt sie sich vor, dass der Computer zur Generierung jedes Tokens alle diese Parameter nutzen muss.

In einem Mixture-of-Experts-Modell funktioniert das nicht so.

Es ähnelt eher einer riesigen Organisation mit sehr vielen spezialisierten Abteilungen. Alle existieren, aber für jedes Token aktiviert das Modell nur einen Teil der Experten.

Die Frage hört also auf zu lauten:

'Wie schaffe ich es, das gesamte Modell in den RAM zu bekommen?'

und wird zu:

'Wie schaffe ich es, den richtigen Teil des Modells genau in dem Moment verfügbar zu haben, in dem er benötigt wird?'

Colibrì versucht, diese zweite Frage zu beantworten.

Der Speicherplatz wird zu einer weiteren Ebene der Speicherhierarchie. Die Experten können auf der Festplatte bleiben und nah an die Berechnung gebracht werden, wenn sie benötigt werden.

Es ist, als hätte man ein riesiges Lagerhaus und eine relativ kleine Werkbank. Man legt nicht das gesamte Lagerhaus auf den Tisch. Wenn Sie das System aufbauen, müssen Sie es so organisieren, dass das, was benötigt wird, schnell genug auf den Tisch kommt.

Dann kommen Caches, Prefetch, Nutzungsmuster und andere Optimierungen ins Spiel.

Das allgemeine Prinzip bleibt jedoch einfach:

Sie müssen nicht notwendigerweise alles gleichzeitig haben.

Sie müssen es schaffen, das Richtige im richtigen Moment zu haben.

Und das ist ein Prinzip, von dem ich glaube, dass es noch viel breitere Anwendungen haben kann, wenn die Modelle weiter wachsen."
![tiers.jpg](tiers.jpg)
[Eine Speicherhierarchie anstelle einer einzelnen Speicheranforderung, Bild aus dem offiziellen Repository entnommen](https://github.com/JustVugg/colibri)

## 0,05 Token pro Sekunde, ehrlicherweise

Hier kommt der online am meisten diskutierte Punkt. Auf einem Laptop mit 25 GB RAM sprachen die ersten Benchmarks von einem Token alle zehn bis zwanzig Sekunden, und eine Analyse von Wavect schrieb, dass das Projekt "ausführt, aber mit 0,05-0,1 Token pro Sekunde aus kaltem Cache" und definierte es als "einen ernsthaften Architkturnachweis, noch keinen einsatzbereiten Produktionsserver". Tom's Hardware nennt hingegen 20-30 Token pro Sekunde als Schwelle für eine wirklich flüssige Interaktion, während man auf einer Maschine mit sechs RTX 5090-GPUs 6 Token pro Sekunde erreicht. Ich frage ihn, wie er sich zu diesen Beobachtungen positioniert, ob Colibrì heute eine faszinierende Ingenieursübung oder ein bereits nutzbares Produkt ist.

"Die Analyse von Wavect ist ehrlich.

Die ersten Versionen von Colibrì als 'a serious proof of architecture, not yet a drop-in production server' zu definieren, ist eine Beschreibung, die ich für korrekt halte.

Die Geschwindigkeit ist ein reales Problem und ich möchte es nicht verbergen.

Auf einem Laptop bedeutet das Ausführen eines Modells dieser Größe über Colibrì heute nicht, dieselbe Erfahrung zu haben, die man mit einem Modell hätte, das von einem großen Rechenzentrum bereitgestellt wird.

Aber meiner Meinung nach ist der interessante Punkt zu verstehen, wie die Trajektorie verläuft.

Vorher war das Problem binär: Dieses Modell passte in Ihre Infrastruktur oder es passte nicht.

Colibrì versucht, es in ein kontinuierliches Problem zu verwandeln: Wie langsam können wir starten, wie viel können wir Caches, Speicher, Prefetch, Spekulation, beschleunigte Backends verbessern und wie viel des Flaschenhalses können wir schrittweise beseitigen?

Ingenieurwesen beginnt oft damit, eine Null in eine Zahl zu verwandeln.

Sobald etwas funktioniert, kann man es messen.

Und sobald man es messen kann, kann man ernsthaft anfangen, es zu optimieren.

Ich würde heute nicht 20 oder 30 Token pro Sekunde für ein Modell mit Hunderten von Milliarden Parametern auf jedem beliebigen Laptop versprechen. Es gibt physikalische Grenzen, die Software nicht einfach löschen kann.

Aber ich denke, dass es einen riesigen Raum zwischen 'unmöglich' und 'so schnell wie ein Rechenzentrum' gibt.

Und genau dieser Raum interessiert mich zu erkunden.

Kurzfristig sehe ich Colibrì als eine sehr interessante Plattform für Entwickler, Forscher, Enthusiasten und Anwendungsfälle, bei denen der lokale Zugriff auf riesige Modelle einen besonderen Wert hat.

Langfristig ist das Ziel hingegen, den Abstand zwischen lokaler Inferenz und zentralisierter Infrastruktur weiter zu verringern.

Wenn uns das gut genug gelingt, wird es nicht mehr nur ein technisches Experiment sein.

Es wird eine neue Infrastrukturoption werden."

## Korrektheit vor dem Benchmark

Colibrì hat noch offene Grenzen, es ist kein Produktionsserver, vorerst arbeitet es mit der Architektur von GLM-5.2 und nicht mit generischen MoE-Modellen, die Validierung der Qualität der int4-Quantisierung ist eine laufende Arbeit, die NVMe-Festplatte bleibt der am schwersten zu schlagende Gegner. Ich frage ihn, wie er diesen Herausforderungen begegnet und ob es Kompromisse gibt, die er heute einzugehen bereit ist, um Geschwindigkeit zu gewinnen, oder Linien, die er hingegen für unüberschreitbar hält.

"Eine kleine Korrektur der Prämisse: Colibrì unterstützt heute bereits verschiedene MoE-Modellfamilien, und jede neue hinzugefügte Architektur ermöglicht es uns, etwas zu verstehen, das auch für die anderen nützlich werden kann.

Auch die Quantisierung ist stark gereift.

Wir haben reale Qualitätsprobleme gefunden und behoben, und dabei war die Community von grundlegender Bedeutung.

Der Hauptgegner bleibt jedoch die Datenmenge, die bewegt werden muss.

Und deshalb ist eine Regel, die ich kontinuierlich anzuwenden versuche: Messen vor dem Glauben.

Es ist extrem leicht, eine Optimierung zu erfinden, die auf dem Papier brillant aussieht.

Viel schwieriger ist es zu beweisen, dass sie das System auf realer Hardware und mit realen Arbeitslasten tatsächlich verbessert.

Ich habe ein kleines Experimentierlabor, in dem viele Ideen sterben gehen.

Und das ist genau das, was passieren sollte.

Was Kompromisse angeht, bin ich bereit, viele einzugehen.

Ich kann einen langsameren Kaltstart akzeptieren, wenn sich das Verhalten während der Nutzung verbessert.

Ich kann eine größere Komplexität im Datenformat akzeptieren, wenn es bedeutet, viel weniger vom Speicher zu lesen.

Ich kann verschiedene Strategien je nach Hardware akzeptieren.

Was ich nicht opfern möchte, ist die Korrektheit.

Ein beeindruckender Benchmark, der durch stillschweigendes Verschlechtern der Modellqualität erzielt wird, interessiert mich nicht.

Wenn Colibrì eine Infrastruktur werden soll, auf der andere Menschen etwas aufbauen, muss das Vertrauen in die Ergebnisse vor der besten Zahl in einer Tabelle kommen."

## Software, Hardware, Modelle: drei Wege, die konvergieren

Das Projekt verfügt bereits über CUDA- und Metal-Backends, eine funktionierende Weboberfläche und native Unterstützung für das spekulative Dekodieren von GLM-5.2. Ich frage ihn, was noch fehlt, um eine Geschwindigkeit zu erreichen, die im Alltag wirklich mit einer Cloud-API konkurrieren kann – sagen wir zehn bis zwanzig Token pro Sekunde auf Hardware, die sich eine gewöhnliche Person kaufen könnte –, und ob es eine Frage des Codes, der Hardware oder zukünftiger Modelle ist, die besser für diesen Ansatz geeignet sind.

"Es sind alle drei Dinge: Software, Hardware und Modelle.

Aber der wahrscheinlich interessanteste Aspekt ist die Art und Weise, wie diese drei Teile beginnen können, zusammen entworfen zu werden.

Die Software kann extrem viel tun.

Wir können das Datenformat verbessern, Lesevorgänge reduzieren, vorhersehen, welche Experten benötigt werden, Übertragung und Berechnung überlappen, den Cache verbessern und die verfügbaren CPUs, GPUs und Speicher besser nutzen.

Aber Software kann keine physikalische Grenze aufheben.

Die Hardware wird daher weiterhin wichtig sein.

Consumer-SSDs werden immer schneller, die Speicherkapazität wächst und auch die Computerarchitekturen verändern sich.

Für Colibrì ist das besonders interessant, weil wir den Speicherplatz nicht einfach als den Ort betrachten, von dem aus das Modell zu Beginn geladen wird, sondern als aktiven Teil der Inferenzarchitektur.

Dann gibt es die Modelle.

Die aktuellen wurden für Infrastrukturen entworfen, in denen riesige Mengen an Speicher und Bandbreite existieren.

Sie wurden nicht mit Blick auf eine Consumer-Maschine optimiert, die kontinuierlich entscheiden muss, welche Teile des Modells näher an die Berechnung gebracht werden müssen.

Ich sehe jedoch keinen Grund, warum dies eine Konstante bleiben sollte.

Modelle mit größerer Lokalität, kleinere Experten, vorhersehbareres Routing oder Strukturen, die explizit für Speicherhierarchien entworfen wurden, könnten das Problem radikal verändern.

In gewisser Weise könnte es sein, dass Colibrì vor dem idealen Modell für diese Art von Inferenz angekommen ist.

Das ist auch eine der Sachen, die ich aus Zukunftsperspektive am interessantesten finde.

Ich möchte nicht, dass Colibrì einfach nur 'ein Programm ist, das GLM auf einem Laptop laufen lässt'.

Mich interessiert zu verstehen, ob einige der Ideen, die wir untersuchen, zu einer anderen Art werden können, über die Inferenz sehr großer Modelle nachzudenken.

Wenn das passiert, wird der potenzielle Markt nicht auf den einzelnen Enthusiasten mit einem langsamen Computer beschränkt sein.

Es könnte Workstations, Edge Computing, Unternehmen, die Daten lokal halten wollen, Forschung, dedizierte Appliances und wahrscheinlich Anwendungsfälle betreffen, die wir uns heute noch gar nicht vorgestellt haben."

## Ein Modell besitzen: über das Sparen hinaus

Es gibt diejenigen, die in Colibrì den Beweis sehen, dass lokale KI auch für diejenigen real werden kann, die sich kein Rechenzentrum leisten können, und es gibt diejenigen, die einwenden, dass die Demokratisierung der KI bereits Realität ist – ein Browser und zwanzig Dollar im Monat für ChatGPT genügen. Ich frage ihn, wie er auf diesen Einwand antwortet und was das Besitzen eines Modells über die reine Ersparnis hinaus wirklich bedeutet – ob es eine Frage der Privatsphäre, der Freiheit oder von etwas Radikalerem wie der Fähigkeit ist, Wissenschaft über KI zu betreiben, statt sie nur zu nutzen.

"Der Einwand ist absolut berechtigt.

Wenn die Frage lautet 'Kann ich eine sehr leistungsfähige künstliche Intelligenz nutzen?', hat die Cloud den Zugang bereits enorm demokratisiert.

Und das ist eine außergewöhnliche Sache.

Ich betrachte Colibrì nicht als einen Krieg gegen die Cloud.

Ich denke, dass Cloud und lokale KI unterschiedliche Probleme lösen und in Zukunft nebeneinander existieren werden.

Es wird Aufgaben geben, für die es Sinn macht, das leistungsfähigste in einem Rechenzentrum verfügbare Modell zu nutzen.

Und es wird andere geben, bei denen Latenz, Privatsphäre, Kostenvorhersehbarkeit, Netzunabhängigkeit, Kontrolle über die Infrastruktur oder die Möglichkeit, genau das System zu studieren, das man nutzt, wichtig sein werden.

Ich denke an die Geschichte der Informatik.

Der Personal Computer hat große Computer nicht nutzlos gemacht.

Er hat einfach eine andere Dimension der Informatik eröffnet.

Die Tatsache, dass ein Computer Ihnen gehörte, bedeutete, dass Sie ihn programmieren, verändern, kaputt machen und experimentieren konnten.

Mit der KI glaube ich, dass etwas Ähnliches passieren kann.

Ein Remotedienst ist außerordentlich bequem, wenn Sie eine Antwort erhalten möchten.

Ein lokales Modell wird interessant, wenn Sie auch Fragen zum System selbst stellen möchten.

Warum hat es so geantwortet?

Wie verändert sich das Verhalten, wenn ich diese Komponente modifiziere?

Wie stark kann ich es komprimieren?

Kann ich dasselbe Ergebnis in fünf Jahren reproduzieren?

Kann ich Daten nutzen, die ich nicht außerhalb meiner Infrastruktur senden möchte?

Kann ich ein Produkt bauen, das weiterhin funktioniert, ohne vollständig von einem externen Anbieter abzuhängen?

Ich sehe die Zukunft also nicht als 'Cloud gegen lokal'.

Ich sehe sie als ein Kontinuum.

Und ich denke, dass heute ein Teil dieses Kontinuums noch viel weniger entwickelt ist als der andere.

Dort versucht Colibrì zu arbeiten."

## Das Jahr 2036 und das Erbe einer Idee

Wir schließen mit dem Blick in die Ferne. Stellen Sie sich das Jahr 2036 vor: Die Modelle sind noch größer oder vielleicht kleiner und intelligenter geworden, die Consumer-Hardware hat sich verändert. Ich frage ihn, ob Colibrì oder etwas, das daraus entstanden ist, dann noch relevant sein wird, was er sich für die nächsten zehn Jahre für diejenigen wünscht, die die künstliche Intelligenz in ihren eigenen Händen halten wollen, und ganz persönlich: Was soll die Welt nach fünfundzwanzigtausend Sternen und den Schlagzeilen auf Tom's Hardware und Hacker News von ihm in Erinnerung behalten?

"Im Jahr 2036 hoffe ich, dass viele der Dinge, die Colibrì heute schwierig macht, normal geworden sind.

Das bedeutet nicht, dass ich hoffe, dass Colibrì verschwindet.

Es bedeutet, dass ich hoffe, dass es sich weiterentwickelt.

Wichtige Technologieprojekte bleiben selten identisch mit ihrer ersten Version. Sie verändern sich zusammen mit dem Problem, das sie zu lösen versuchen.

Wenn es in zehn Jahren normal sein wird, riesige Modelle auf relativ gewöhnlicher Hardware auszuführen, wird das ein Sieg sein.

An diesem Punkt wird Colibrì wahrscheinlich vor einer anderen Grenze stehen.

Was ich mir wünschen würde, dass es konstant bleibt, ist die grundlegende Idee: den Abstand zwischen einer neugierigen Person und einer Technologie zu verringern, die heute zu groß, teuer oder komplex erscheint, um direkt erkundet zu werden.

Ich möchte, dass eine Person im Jahr 2036 ein fortgeschrittenes Modell betrachten und denken kann:

'Ich möchte verstehen, wie es funktioniert.'

Und es tun kann.

Was das betrifft, was ich persönlich bauen möchte, spüre ich heute eine andere Verantwortung als zu Beginn.

Colibrì ist als individuelles Experiment entstanden, aber ich denke nicht, dass es zwangsläufig so bleiben muss.

Wenn wir dieses Problem ernsthaft angehen wollen, werden wir Menschen brauchen, die in vielen verschiedenen Bereichen viel besser sind als ich, wir werden eine immer stärkere Community brauchen und wahrscheinlich wird es auch nötig sein, eine Struktur aufzubauen, die in der Lage ist, das Projekt langfristig zu tragen.

Das ändert nichts an dem Grund, warum ich angefangen habe.

Es macht ihn einfach ehrgeiziger.

Und wenn in zehn Jahren jemand vor einem Problem steht, das alle für unmöglich halten, und denkt:

'Versuchen wir es.'

und vielleicht etwas nutzt, das auch aus der heute an Colibrì geleisteten Arbeit entstanden ist, wird das für mich bereits ein riesiges Ergebnis sein.

Es interessiert mich nicht besonders, dass man sich an die Idee von Vincenzo Fornaro als 'Genie' erinnert.

Mich würde es viel mehr interessieren, wenn eine andere Idee bliebe:

Dass eine Person mit wenigen Mitteln, aber genug Neugier, immer noch etwas Wichtiges genug beginnen kann, um andere Menschen anzuziehen und viel größer zu werden als sie selbst.

Es ist genau das, was Colibrì gerade passiert."

---

*Das [Repository von Colibrì](https://github.com/JustVugg/colibri) bleibt auf GitHub einsehbar für alle, die es ausprobieren, beitragen oder einfach diese dreizehnhundert Zeilen C lesen möchten, die das Gespräch entfacht haben.*
