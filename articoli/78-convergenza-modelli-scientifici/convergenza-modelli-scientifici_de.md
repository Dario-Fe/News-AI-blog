---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-23
author: "Dario Ferrero"
---

# Wenn wissenschaftliche Modelle anfangen, gleich zu denken
![convergenza-modelli-scientifici .jpg](convergenza-modelli-scientifici .jpg)


*Erinnern Sie sich, als [wir über KI-Slop gesprochen haben](https://aitalk.it/it/ai-slop-entropia.html), diese Lawine von synthetischen Inhalten, die YouTube und den Rest des Internets überschwemmt? Die Forschung von Kapwing hatte uns ein alarmierendes Bild gezeigt: 21 % der Videos, die neuen Nutzern empfohlen werden, sind reiner "Slop", der von KI erzeugt wird, Inhalte, die in Massen ohne menschliche Aufsicht produziert werden und nur dazu dienen, Aufrufe zu generieren. Weitere 33 % fallen in die Kategorie "Brainrot", repetitive und hypnotische Clips ohne Substanz. Insgesamt enthalten über die Hälfte der ersten 500 Videos, auf die ein neues YouTube-Konto stößt, keine nennenswerte menschliche Kreativität.*

Aber das war nur die Oberfläche des Problems. Heute erzähle ich Ihnen, was passiert, wenn wir tiefer graben, wenn wir nicht auf die von der KI erzeugten Inhalte schauen, sondern auf die internen Repräsentationen, die diese Systeme entwickeln. Und hier zeigt sich ein noch beunruhigenderes Szenario: Wissenschaftliche Modelle der künstlichen Intelligenz konvergieren alle zu derselben Art, Materie zu "sehen". Nicht, weil sie ein universelles Verständnis der Physik erreicht haben, sondern weil sie alle durch dieselben Daten begrenzt sind.

Ein Team von Forschern des MIT hat gerade eine [Studie über 59 wissenschaftliche KI-Modelle](https://arxiv.org/html/2512.03750v1) veröffentlicht, Systeme, die auf verschiedenen Datensätzen trainiert wurden, mit unterschiedlichen Architekturen, die auf verschiedenen Modalitäten wie chemischen Strings, dreidimensionalen Atomkoordinaten und Proteinsequenzen arbeiten. Die Frage war einfach: Lernen diese Modelle wirklich die zugrunde liegende Physik der Materie, oder merken sie sich nur Muster aus ihren Trainingsdaten?

Die Ergebnisse sind ebenso überraschend wie besorgniserregend. Die Modelle zeigen eine sehr starke "repräsentative Angleichung" und entwickeln interne Repräsentationen der Materie, die sich seltsam ähnlich sind. Es ist, als ob sie zu einer "gemeinsamen Physik" konvergieren, die in ihren künstlichen Neuronen verborgen ist. Die Forscher haben dieses Phänomen mit vier verschiedenen Metriken gemessen, von der lokalen Ausrichtung der nächsten Nachbarn (CKNNA) über die globale Abstandskorrelation (dCor) bis hin zur intrinsischen Dimension der latenten Räume, und alle deuten in dieselbe Richtung.

## Die unvermeidliche Konvergenz

Nehmen wir den Fall von Modellen, die auf kleinen Molekülen aus dem QM9-Datensatz trainiert wurden. Hier finden wir Systeme, die mit SMILES-Strings arbeiten, jenen alphanumerischen Sequenzen, die chemische Strukturen wie "CC(C)C1CCC(C)CC1=O" kodieren, und Modelle, die stattdessen direkt die 3D-Koordinaten der Atome im Raum verarbeiten. Das scheinen radikal unterschiedliche Ansätze zu sein, und doch zeigen ihre latenten Räume eine überraschende Übereinstimmung. Modelle, die auf SMILES basieren, und solche, die auf Atomkoordinaten basieren, stimmen darin überein, welche Moleküle einander ähnlich sind, obwohl das eine mit flachen Strings und das andere mit dreidimensionalen Geometrien arbeitet.

Das Phänomen ist bei Proteinen noch ausgeprägter. Modelle, die Aminosäuresequenzen verarbeiten, wie ESM2 oder ESM3, stimmen fast perfekt mit denen überein, die auf dreidimensionalen Proteinstrukturen arbeiten. Die Konvergenz ist doppelt so hoch wie bei kleinen Molekülen. Dies deutet darauf hin, dass die großen Proteinsequenzmodelle implizit die Einschränkungen der Proteinfaltung gelernt haben, was ihre latenten Räume natürlich näher an die der Strukturmodelle bringt.

Aber es gibt noch mehr. Mit zunehmender Leistung der Modelle, gemessen an der Fähigkeit, die Gesamtenergie von Materialstrukturen vorherzusagen, konvergieren ihre Repräsentationen immer mehr zu denen des besten Modells. Es ist ein Muster, das an die "Platonische Repräsentationshypothese" erinnert, die bereits bei Seh- und Sprachmodellen beobachtet wurde: die Idee, dass verschiedene Systeme bei ihrer Verbesserung zu einer gemeinsamen Repräsentation der Realität konvergieren.

Die Forscher haben sogar einen "Stammbaum" der wissenschaftlichen Modelle erstellt, indem sie die Abstände in den Repräsentationsräumen nutzten, um zu messen, wie "verwandt" sie sind. Und hier zeigt sich ein entscheidendes Detail: Die Modelle gruppieren sich eher nach dem Trainingsdatensatz als nach der Architektur. Zwei Modelle mit völlig unterschiedlichen Architekturen, die aber mit denselben Daten trainiert wurden, ähneln sich mehr als zwei Modelle mit derselben Architektur, die aber mit unterschiedlichen Daten trainiert wurden. Die Botschaft ist klar: Es sind die Daten, nicht die Architektur, die den Repräsentationsraum dominieren.

## Fallen in der Verteilung

Aber diese scheinbare wissenschaftliche Reifung birgt eine systemische Gefahr. Die Forscher testeten die Modelle sowohl an "in-distribution"-Strukturen, also Materialien, die denen ähneln, die während des Trainings gesehen wurden, als auch an "out-of-distribution"-Strukturen, wie z. B. viel größeren und komplexeren organischen Molekülen. Und hier kehrt sich das Bild vollständig um.

Bei den in-distribution-Strukturen, wie denen aus dem OMat24-Datensatz für anorganische Materialien, zeigen die besten Modelle eine starke Übereinstimmung untereinander, während die schwächeren in lokale Suboptima des Repräsentationsraums abweichen. Das ist das Verhalten, das wir erwarten würden: Leistungsstarke Modelle konvergieren zu einer gemeinsamen und verallgemeinerbaren Repräsentation, schwache Modelle verlieren sich in ungewöhnlichen Lösungen.

Aber wenn sie ihre Komfortzone verlassen und an großen organischen Molekülen aus dem OMol25-Datensatz getestet werden, brechen fast alle Modelle zusammen. Nicht nur ihre Vorhersagen werden schlechter, sondern ihre Repräsentationen konvergieren zu fast identischen, aber informationsarmen Architekturvarianten. Es ist, als ob sie angesichts des Unbekannten jede Unterscheidungsfähigkeit verlieren und sich in die in ihren Architekturen kodierten induktiven Vorurteile flüchten.

Die Forscher visualisierten diesen Zusammenbruch anhand der Metrik des Informationsungleichgewichts, das asymmetrisch misst, wie viele Informationen eine Repräsentation im Vergleich zu einer anderen enthält. Bei den in-distribution-Strukturen sind die schwachen Modelle verstreut, jedes lernt unterschiedliche und orthogonale Informationen. Bei den out-of-distribution-Strukturen drängen sie sich alle in der unteren linken Ecke des Diagramms: fast identische Repräsentationen, alle gleichermaßen unvollständig.

Das Problem ist systemisch. Die beliebtesten Trainingsdatensätze wie MPTrj, sAlex und OMat24 werden von DFT-Simulationen dominiert, die auf dem PBE-Funktional basieren, einem westlichen Berechnungsstandard. Dies schafft eine Datenmonokultur, die systematisch exotische Chemie, Biomoleküle aus nicht-westlichen Ökosystemen und seltene Atomkonfigurationen ausschließt. Die Modelle konvergieren nicht, weil sie universelle Gesetze der Materie entdecken, sondern weil sie alle mit denselben Berechnungssuppen gefüttert werden.
![convergenza-modelli-scientifici.jpg](convergenza-modelli-scientifici.jpg)
[Bild von arxiv.org](https://arxiv.org/html/2512.03750v1)

## Die sich ausbreitende Entropie

Und hier schließt sich der Kreis zum KI-Slop, von dem wir am Anfang gesprochen haben. Denn was in den wissenschaftlichen Modellen geschieht, ist nur ein Sonderfall eines viel umfassenderen Phänomens: des globalen Modellkollaps.

Stellen Sie sich vor, was passiert, wenn synthetische Daten, die von KI erzeugt werden, zum Trainieren neuer KI verwendet werden. Genau das geschieht auf YouTube: 278 Kanäle produzieren ausschließlich Slop, erzielen 63 Milliarden Aufrufe und 117 Millionen Dollar jährliche Werbeeinnahmen. Diese synthetischen Inhalte sind nicht neutral, sie tragen die Vorurteile, Einschränkungen und konvergenten Repräsentationen der Modelle in sich, die sie erzeugt haben.

Im Fall der wissenschaftlichen Modelle bedeutet dies, dass KI-generierte DFT-Simulationen, die bereits durch das PBE-Funktional und "übliche" chemische Systeme begrenzt sind, zum Trainieren der nächsten Generation von Modellen verwendet werden. Und diese werden wiederum noch enger auf dieselben Repräsentationen konvergieren und die Peripherien des chemischen Raums zunehmend ausschließen.

Es ist das Phänomen des "Modellkollaps", das in einer [kürzlich durchgeführten Studie](https://arxiv.org/html/2512.12381v1) dokumentiert wurde: Wenn generative Modelle rekursiv mit Daten trainiert werden, die von anderen Modellen erzeugt wurden, erodiert die Vielfalt von Generation zu Generation. Bei großen Sprachmodellen, die mit synthetischem Text trainiert werden, äußert sich dies als Verlust an sprachlicher Kreativität und Schwierigkeiten bei der domänenübergreifenden Verallgemeinerung. Bei wissenschaftlichen Modellen bedeutet dies eine fortschreitende Verarmung der Fähigkeit, neue Regionen des chemischen und materiellen Raums zu erkunden.

Die Parallele zum Inhalts-Ökosystem ist beunruhigend. So wie der KI-Slop auf YouTube menschliche Schöpfer durch negative Stückkosten verdrängt (synthetische Inhalte kosten fast nichts in der Massenproduktion), so drohen synthetische wissenschaftliche Daten die teure empirische Datenerhebung zu entwerten. Die Durchführung echter physikalischer Experimente, die Synthese neuer Verbindungen, die Erhebung experimenteller Daten aus Labors: all das erfordert Zeit, Fachwissen und Ressourcen. Die Erzeugung einer Million simulierter Strukturen mit einem KI-Modell erfordert nur Rechenleistung.

## Die Geographie der Daten

Die Auswirkungen gehen weit über die Computerchemie hinaus. Die MIT-Forscher weisen darauf hin, dass die aktuellen Modelle "datengesteuert und nicht grundlegend" sind, was bedeutet, dass sie noch nicht im eigentlichen Sinne grundlegend sind. Ein echtes grundlegendes Modell sollte gut auf Materiebereiche verallgemeinern, die während des Trainings nie gesehen wurden. Stattdessen zeigen diese Systeme eine starke Abhängigkeit vom Trainingssatz und einen vorhersehbaren Zusammenbruch außerhalb der Verteilung.

Es gibt auch eine geopolitische Dimension. Die dominierenden Datensätze stammen von westlichen Institutionen und verwenden standardisierte Berechnungsmethoden. Dies schafft strukturelle Verzerrungen, die bereits gut untersuchte Chemie und Materialien begünstigen und potenzielle Entdeckungen in weniger erforschten Regionen des chemischen Raums systematisch ausschließen. Es ist eine subtile Form der wissenschaftlichen Zentralisierung, bei der die großen Technologie- und Pharmaunternehmen, die sich die Erzeugung von Daten im großen Stil leisten können, die wissenschaftliche KI monopolisieren werden.

Die Forscher schlagen vor, dass das Erreichen eines echten grundlegenden Status wesentlich vielfältigere Datensätze erfordert, die Gleichgewichts- und Nichtgleichgewichtsregime, exotische chemische Umgebungen sowie extreme Temperaturen und Drücke abdecken. Es sind Richtlinien erforderlich, um offene und vielfältige Datensätze zu fördern, Erweiterungen von Initiativen wie Open Catalyst 2020, aber in viel größerem Maßstab.

Es gibt jedoch auch eine positive Note, die in den Ergebnissen verborgen ist. Die Studie zeigt, dass Modelle sehr unterschiedlicher Größe, auch kleine, ähnliche Repräsentationen wie große Modelle lernen können, wenn sie gut trainiert werden. Dies öffnet den Weg zur Destillation: kompakte Modelle, die die Repräsentationsstruktur riesiger Systeme erben und die Rechenbarrieren für Forschung und Entwicklung senken.

Noch überraschender ist der Fall der Orb-V3-Modelle, die eine hervorragende Leistung ohne Auferlegung der Rotationsäquivarianz in der Architektur erzielen. Stattdessen verwenden sie ein leichtes Regularisierungsschema namens "Equigrad", das die Quasi-Invarianz der Energie und die Quasi-Äquivarianz der Kräfte während des Trainings fördert. Das Ergebnis? Ihre latenten Räume stimmen stark mit vollständig äquivarianten Architekturen wie MACE und Equiformer V2 überein, jedoch bei viel geringeren Rechenkosten. Es ist eine Version der "bitteren Lektion" des maschinellen Lernens: Oft übertrifft die Skalierung des Trainings aufwendige Architekturbeschränkungen.

Die letzte Lektion ist klar: Wir erleben die Entstehung einer repräsentativen Monokultur in der wissenschaftlichen KI, die durch die Konvergenz begrenzter Datensätze und die Verbreitung synthetischer Daten angetrieben wird. Wie beim KI-Slop auf YouTube ist das Problem nicht die Technologie an sich, sondern die Ökonomie der Aufmerksamkeit und der Ressourcen, die Quantität über Qualität und Geschwindigkeit über Vielfalt belohnt. Der Unterschied besteht darin, dass auf YouTube das Schlimmste, was passieren kann, eine von KI erzeugte sprechende Katze ist, während wir in der wissenschaftlichen KI in unsere Modelle die epistemischen Grenzen kodieren, die definieren werden, welche Medikamente wir entwickeln, welche Materialien wir entdecken und welche wissenschaftlichen Fragen wir überhaupt für würdig halten, gestellt zu werden.

Der Kreis schließt sich dort, wo er begonnen hat: Die Entropie breitet sich aus, nicht nur in den sozialen Feeds, sondern auch in den latenten Räumen, die vorgeben, die Materie selbst darzustellen. Und vielleicht ist die eigentliche Frage nicht, ob die KI Physik lernt, sondern ob wir gemeinsam darauf verzichten, alles zu erforschen, was unsere standardisierten Simulationen nicht bereits sehen können.
