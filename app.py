import streamlit as st
import random

# ---------------------------
# Fragen und Antworten laden
# ---------------------------
questions = [
    
    {"question": "1.1 a) Das Pricing ist deshalb von besonderer Bedeutung im Marketing-Mix, weil es einen indirekten Einfluss auf die Unternehmenskennzahlen hat.", "answer": "falsch", "explanation": "Pricing beeinflusst Umsatz und Gewinn direkt, nicht nur indirekt."},
    {"question": "1.1 b) Der Kompromisseffekt beschreibt den Effekt, dass Konsumenten einen Referenzpreis zur Preisbeurteilung heranziehen.", "answer": "falsch", "explanation": "Das beschreibt den Ankereffekt, nicht den Kompromisseffekt."},
    {"question": "1.1 c) Der Preisankereffekt beschreibt, dass Kund:innen, bei einer Vielzahl von Produkten mit unterschiedlichen Preisen innerhalb einer Produktlinie, Produkte in mittlerer Preisklasse wählen.", "answer": "falsch", "explanation": "Das ist der Kompromisseffekt, nicht der Preisankereffekt."},
    {"question": "1.1 d) Eine Edelstahl-Trinkflasche kostet CHF 10, die variablen Produktionskosten entsprechen CHF 2 pro Stück und die Fixkosten CHF 10'000. Von den Trinkflaschen verkaufen Sie 5'000 Stück. Der resultierende Gewinn beträgt CHF 20'000.", "answer": "falsch", "explanation": "Gewinn = 5000*10 - (5000*2 + 10000) = CHF 30'000."},
    {"question": "1.2 a) Die drei Elemente des 'Magischen Dreiecks des Pricings' sind: kundenorientierte Preise, vergangenheitsorientierte Preise und wettbewerbsorientierte Preise.", "answer": "falsch", "explanation": "Statt vergangenheitsorientiert ist kostenorientiert korrekt."},
    {"question": "1.2 b) Die Übervorteilungsstrategie im Rahmen der Preispositionierung entspricht einer hohen Qualität zu tiefen Preisen.", "answer": "falsch", "explanation": "Das wäre die Billigstrategie, Übervorteilung heißt hohe Preise bei tiefer Qualität."},
    {"question": "1.2 c) Die Tasty Dürüm AG verkauft im Januar 1000 Stück zu CHF 10 und im Februar 1500 Stück zu CHF 8. Die daraus abgeleitete Preisabsatzfunktion ist p(x) = 14 - x/250.", "answer": "richtig", "explanation": "Einsetzen der Werte in p(x) = a - b*x bestätigt die Funktion."},
    {"question": "1.2 d) Sie nehmen obige Preisabsatzfunktion und berechnen, dass bei einem Preis von CHF 12 die abgesetzte Menge 600 Stück betragen würde. Zudem identifizieren Sie die Sättigungsmenge bei 3'500 Stück und den Prohibitionspreis bei CHF 14.", "answer": "falsch", "explanation": "Einsetzen ergibt 500 Stück bei CHF 12, also ist die Aussage falsch."},
    {"question": "1.3 a) Leistungen werden grundsätzlich nach intangibel und tangibel unterschieden.", "answer": "richtig", "explanation": "Intangibel = immateriell, tangibel = materiell – das ist korrekt."},
    {"question": "1.3 b) Die 'soziale Anerkennung' durch den Kauf eines auffälligen Sportwagens entspricht dem Erbauungsnutzen.", "answer": "richtig", "explanation": "Soziale Wirkung gehört zum Erbauungsnutzen."},
    {"question": "1.3 c) Mit Maßnahmen im Rahmen der Leistungspflege soll unter anderem die Wachstums- bzw. Reifephase einer Leistung in dessen Lebenszyklus verlängert werden.", "answer": "richtig", "explanation": "Das Ziel der Leistungspflege ist die Verlängerung des Lebenszyklus."},
    {"question": "1.3 d) Bei der Leistungsvariation werden bereits im Markt eingeführte Leistungen durch eine Variante ersetzt, bei der bestimmte Eigenschaften oder Leistungsmerkmale verbessert wurden.", "answer": "richtig", "explanation": "Das ist die Definition der Leistungsvariation."},
    {"question": "1.4 a) Diversifikation eines Produktportfolios kann horizontal, vertikal oder lateral erfolgen.", "answer": "richtig", "explanation": "Das sind die anerkannten Diversifikationsformen."},
    {"question": "1.4 b) Das Anbieten von Jogurts in verschiedenen Geschmacksrichtungen entspricht dem Konzept einer Produktdifferenzierung.", "answer": "richtig", "explanation": "Produktdifferenzierung über Varianten ist hier gegeben."},
    {"question": "1.4 c) (Mass-)Customization ist ein Spezialfall der Produktdifferenzierung und erfüllt individuelle Kundenbedürfnisse mittels einer eigenen Variante.", "answer": "richtig", "explanation": "Mass Customization ist individualisierte Differenzierung."},
    {"question": "1.4 d) Eine Innovation setzt sich schneller durch, wenn ihre Nutzung einfach dargestellt und anderen mitgeteilt werden kann, z.B. mittels Sozialer Medien.", "answer": "richtig", "explanation": "Kommunizierbarkeit ist ein Faktor für die Diffusionsgeschwindigkeit."},
    {"question": "1.5 a) In der Reifephase des Produktlebenszyklus wird der Wettbewerb schwächer und immer mehr neue Konkurrenten treten in den Markt ein.", "answer": "falsch", "explanation": "In der Reifephase nimmt der Wettbewerb zu, neue Anbieter meist früher."},
    {"question": "1.5 b) Der Relaunch ist ein Spezialfall der Leistungsdifferenzierung.", "answer": "richtig", "explanation": "Ein Relaunch stellt eine Differenzierung bestehender Leistungen dar."},
    {"question": "1.5 c) Ein Handelsunternehmen entscheidet sich, anstatt Produkte einzukaufen, diese selbst herzustellen. Das ist eine Form der Diversifikation und nennt sich vertikale Vorwärtsintegration.", "answer": "richtig", "explanation": "Produktion ist vorgelagerte Stufe – vertikale Integration."},
    {"question": "1.5 d) Der generische Innovationsprozess wird in folgende Phasen unterteilt: Ideenphase, Leistungsentwicklung, Markteinführung.", "answer": "richtig", "explanation": "Das sind die klassischen Innovationsphasen."},
    {"question": "1.6 a) Preisnachlässe für Senioren sind eine Form der demografischen Preisdifferenzierung.", "answer": "richtig", "explanation": "Alter als demografisches Merkmal ist Basis der Differenzierung."},
    {"question": "1.6 b) Ziel der Preisdifferenzierung ist es, unterschiedliche Zahlungsbereitschaften abzuschöpfen, um so den Gewinn gegenüber der Einheitspreissetzung zu steigern.", "answer": "richtig", "explanation": "Genau das ist der Zweck der Preisdifferenzierung."},
    {"question": "1.6 c) Man kann durch eine Preiserhöhung keinen Umsatz verlieren.", "answer": "falsch", "explanation": "Eine Preiserhöhung kann Nachfrage reduzieren."},
    {"question": "1.6 d) Die Penetrationsstrategie zielt darauf ab, mit einem tiefen Preis bei der Markteinführung möglichst viel der Zahlungsbereitschaft der Konsument:innen abzuschöpfen.", "answer": "falsch", "explanation": "Penetration will Marktanteile, nicht Zahlungsbereitschaft abschöpfen."},
    {"question": "1.7 a) Die Service Profit Chain zeigt die Wirkung zufriedener Kund:innen auf die Zufriedenheit der Investoren.", "answer": "falsch", "explanation": "Die Kette läuft: Mitarbeiter → Kunden → Profitabilität."},
    {"question": "1.7 b) 'Customer Managed Relationship' bezeichnet den Ansatz, gemäß dem Kund:innen die Beziehung zu Unternehmen selbst bestimmen.", "answer": "richtig", "explanation": "CMR bedeutet kundengetriebene Beziehungsführung."},
    {"question": "1.7 c) 'Cross-Selling' bezeichnet den Verkauf eines Upgrades einer Leistung. 'Up-Selling' hingegen der Verkauf einer zusätzlichen, dazugehörigen Leistung.", "answer": "falsch", "explanation": "Definitionen sind vertauscht: Cross-Selling = Zusatzleistung."},
    {"question": "1.7 d) 'Gebundenheit' bezeichnet die faktische Kundschaftsbindung, welche z.B. durch Verträge erzwungen werden kann. 'Verbundenheit' hingegen bezeichnet die emotionale Kundschaftsbindung.", "answer": "richtig", "explanation": "Die Begriffe sind korrekt definiert."},
    {"question": "1.8 a) 'Fait accompli' im Kündigungsmanagement bedeutet, dass ein Unternehmen eine Kundschaftsbeziehung 'versanden' lässt und z.B. keine Newsletter mehr versendet.", "answer": "richtig", "explanation": "Das beschreibt passives Auslaufenlassen."},
    {"question": "1.8 b) Das Beschwerdeparadoxon beschreibt, dass Kunden bei einer Reklamation, die positiv bearbeitet wurde, hinterher zufriedener sind als Kunden, die nichts zu beanstanden hatten.", "answer": "richtig", "explanation": "Das ist das bekannte Beschwerdeparadoxon."},
    {"question": "1.8 c) Der Inbound-Marketing-Ansatz umfasst vor allem Printwerbung, Direct Mailings, Call Center und TV-Werbung.", "answer": "falsch", "explanation": "Das sind Outbound-Maßnahmen."},
    {"question": "1.8 d) Die Kundenwertanalyse gibt Auskunft über die wertvollsten Kunden aus Unternehmenssicht, und darauf aufbauend werden die Strategien zu ihrer Rückgewinnung gebildet.", "answer": "richtig", "explanation": "Kundenwertanalyse dient Segmentierung und Rückgewinnung."},
    {"question": "1.9 a) Mit der Unique Communications Proposition (UCP) soll analog zur Einzigartigkeit einer Leistung (USP) auch die Kommunikation einzigartig sein.", "answer": "richtig", "explanation": "UCP spiegelt USP in der Kommunikation."},
    {"question": "1.9 b) Kommunikationsziele werden in kognitiv, affektiv und subjektiv unterteilt.", "answer": "falsch", "explanation": "Korrekt ist: kognitiv, affektiv, konativ."},
    {"question": "1.9 c) Die Grundidee von integrierter Kommunikation ist, dass verschiedene Kommunikationsmaßnahmen aufeinander abgestimmt sein sollten, um eine maximale Wirkung zu entfalten.", "answer": "richtig", "explanation": "Das ist das Ziel der integrierten Kommunikation."},
    {"question": "1.9 d) Die Integration von Kommunikationsmaßnahmen kann entweder inhaltlich, formal oder zeitlich erfolgen.", "answer": "falsch", "explanation": "Integration sollte in allen drei Dimensionen erfolgen."},
    {"question": "1.10 a) Mediawerbung ist eine Form der persönlichen Kommunikation.", "answer": "falsch", "explanation": "Mediawerbung ist unpersönlich."},
    {"question": "1.10 b) Public Relations hat zum Ziel die Beziehung zwischen Unternehmen und ausgewählten internen und externen Zielgruppen zu gestalten.", "answer": "richtig", "explanation": "PR zielt auf Beziehungsmanagement."},
    {"question": "1.10 c) Mit Sponsoring fördern Unternehmen Personen und/oder Organisationen in Bereichen wie Sport, Kultur oder Umwelt, um Kommunikationsziele zu erreichen.", "answer": "richtig", "explanation": "Sponsoring ist zielgerichtete Unterstützung."},
    {"question": "1.10 d) Eventmarketing beschreibt ein Kommunikationsinstrument, das der erlebnisorientierten Umsetzung von Marketingzielen durch Events dient.", "answer": "richtig", "explanation": "Das ist die Definition von Eventmarketing."},
    {"question": "1.11 a) Im Block 'Schlüsselaktivitäten' sollten die Gründerinnen die physischen, intellektuellen und menschlichen Ressourcen eintragen, die ihr Unternehmen benötigt.", "answer": "falsch", "explanation": "Ressourcen gehören in den Block 'Schlüsselressourcen', nicht 'Schlüsselaktivitäten'."},
    {"question": "1.11 b) Mit der 'Value Proposition' müssen die Gründerinnen beschreiben, welche Probleme ihrer Kund:innen gelöst werden und welche Bedürfnisse ihre Produkte befriedigen.", "answer": "richtig", "explanation": "Das entspricht der Definition der Value Proposition."},
    {"question": "1.11 c) Im Block 'Wettbewerber', sollten die Gründerinnen, die am Markt bereits bestehenden Konkurrenten analysieren.", "answer": "falsch", "explanation": "Es gibt keinen Block 'Wettbewerber' im Business Model Canvas."},
    {"question": "1.11 d) Bei der Erarbeitung der 'Zielgruppen', müssen die Gründerinnen definieren welche Produkte ihr Unternehmen anbieten will.", "answer": "falsch", "explanation": "Im Block 'Kundensegmente' geht es um die Zielgruppen, nicht um Produkte."},
    {"question": "1.12 a) 'Vertriebskanäle' im Business Model Canvas beschreiben, wie ein Unternehmen mit seinen Kund:innen in Kontakt tritt und ihr Produkt ausliefert.", "answer": "richtig", "explanation": "Das ist die korrekte Funktion der Kanäle im Canvas."},
    {"question": "1.12 b) Der Block 'Kostenstruktur' im Business Model Canvas beschreibt die wichtigsten Kosten und Umsatzquellen eines Unternehmens.", "answer": "falsch", "explanation": "Der Block beschreibt nur die Kostenstruktur, nicht Umsatzquellen."},
    {"question": "1.12 c) Partner sind nicht Teil des Geschäftsmodells und werden im Business Model Canvas darum nicht abgebildet.", "answer": "falsch", "explanation": "Partner werden im Block 'Schlüsselpartner' explizit berücksichtigt."},
    {"question": "1.12 d) Mit den Erlösquellen beschreibt das Unternehmen die Wege, durch die Einnahmen generiert werden.", "answer": "richtig", "explanation": "Das ist die Definition von 'Revenue Streams'."},
    {"question": "1.13 a) Das Five Forces Modell wurde entwickelt, um die interne Wettbewerbsfähigkeit eines Unternehmens zu bewerten.", "answer": "falsch", "explanation": "Es analysiert die externe Branchenstruktur, nicht interne Stärken."},
    {"question": "1.13 b) Im Rahmen der Five Forces Analyse wird die Verhandlungsmacht der Lieferanten untersucht.", "answer": "richtig", "explanation": "Lieferantenmacht ist eine der fünf Kräfte."},
    {"question": "1.13 c) Das Five Forces Modell ist gut dazu geeignet den direkten Einfluss neuer Technologien auf das Unternehmen zu beurteilen.", "answer": "falsch", "explanation": "Technologien werden im Modell nicht direkt betrachtet."},
    {"question": "1.13 d) Wird im Rahmen der Five Forces Analyse eine hohe Bedrohung durch neue Anbieter ersichtlich, kann dies die künftige Rentabilität einer Branche verringern.", "answer": "richtig", "explanation": "Neue Anbieter erhöhen den Wettbewerb und drücken die Rentabilität."},
    {"question": "1.14 a) Im Rahmen der Analyse ist die Bedrohung durch Ersatzprodukte, die von direkten Konkurrenten in der Branche hergestellt werden, ein wesentlicher Faktor.", "answer": "falsch", "explanation": "Ersatzprodukte stammen gerade nicht von direkten Wettbewerbern."},
    {"question": "1.14 b) Die MechTech hat zwei Abnehmer, wobei einer der Abnehmer 90% des Umsatzes ausmacht. Dies reduziert das Geschäftsrisiko für die MechTech, weil ein grosser Teil des Absatzes stets gesichert ist.", "answer": "falsch", "explanation": "Hohe Abhängigkeit von einem Kunden erhöht das Risiko."},
    {"question": "1.14 c) Im Rahmen einer umfassenden Analyse nach Porters Five Forces, sollte die MechTech ökologische und gesellschaftliche Faktoren näher untersuchen.", "answer": "falsch", "explanation": "Diese Faktoren gehören nicht zu den klassischen Five Forces."},
    {"question": "1.14 d) Da die MechTech stark spezialisiert ist und kaum direkte Konkurrenten hat, kann sie die Preise für ihre Produkte freier gestalten als in einem Umfeld mit stärkerer Konkurrenz.", "answer": "richtig", "explanation": "Weniger Konkurrenz bedeutet mehr Preissetzungsspielraum."},
    {"question": "1.15 a) Innerhalb eines Marktsegments sollten die Kund:innen möglichst heterogen sein.", "answer": "falsch", "explanation": "Ein Segment sollte möglichst homogen sein."},
    {"question": "1.15 b) Die Wichtigkeit von Holz-Herkunfts-Siegeln erfüllt für WohnKunst die Anforderung an ein verhaltensrelevantes Segmentierungskriterium.", "answer": "richtig", "explanation": "Das ist ein verhaltensbezogenes Kriterium."},
    {"question": "1.15 c) Die WohnKunst sollte sicherstellen, dass das Potenzial der einzelnen Marktsegmente messbar und quantifizierbar ist.", "answer": "richtig", "explanation": "Messbarkeit ist ein zentrales Kriterium der Segmentierung."},
    {"question": "1.15 d) Um eine gewisse Dynamik zu erhalten ist es sinnvoll, dass sich die Marktsegmente mittel- bis langfristig verändern.", "answer": "falsch", "explanation": "Segmente sollten stabil, nicht dynamisch sein."},
    {"question": "1.16 a) SEO und SEA sind konkurrierende Instrumente und sollten nicht gemeinsam in einer digitalen Marketingstrategie verwendet werden.", "answer": "falsch", "explanation": "Sie können sich sinnvoll ergänzen."},
    {"question": "1.16 b) Im Rahmen der SEA kann die Lesewelt bestimmen für welche Keywords sie Anzeigen schalten möchten.", "answer": "richtig", "explanation": "Keyword-Steuerung ist zentrales Element von SEA."},
    {"question": "1.16 c) Wenn die Lesewelt ihre Webseite in Bezug auf SEO optimiert hat, sind die Effekte sofort sichtbar, sobald Änderungen an der Webseite vorgenommen wurden.", "answer": "falsch", "explanation": "SEO zeigt Effekte oft erst verzögert."},
    {"question": "1.16 d) Die SEA-Strategie hat keinen Einfluss auf die organischen Suchergebnisse für die Lesewelt.", "answer": "richtig", "explanation": "Bezahlte Werbung beeinflusst keine organischen Rankings."},
    {"question": "1.17 a) Die 'Click-Through-Rate (CTR)' zeigt Julia die Anzahl der Benutzer, die auf eine Werbung klicken im Vergleich zur Anzahl der totalen Impressionen einer digitalen Anzeige.", "answer": "richtig", "explanation": "Das ist die Definition der CTR."},
    {"question": "1.17 b) Mit den 'Customer Acquisition Costs (CAC)' beschreibt Julia die Kosten, die anfallen, um eine neue Kund:in zu gewinnen.", "answer": "richtig", "explanation": "CAC misst genau diese Kosten."},
    {"question": "1.17 c) Die 'Conversion Rate' beschreibt die absolute Anzahl der Kunden, die eine bestimmte Aktion vollzogen haben (z.B. ein Produkt kaufen).", "answer": "falsch", "explanation": "Die Conversion Rate ist ein prozentualer Anteil, keine absolute Zahl."},
    {"question": "1.17 d) Anhand der 'Bounce Rate' sieht Julia an, welcher Prozentsatz der Besucher mindestens zwei Seiten der Website von Market Maker besucht haben, bevor sie die Seite wieder verlassen haben.", "answer": "falsch", "explanation": "Bounce Rate misst Besucher, die nur eine Seite ansehen."},
    {"question": "1.18 a) Der 'Customer Lifetime Value (CLV)' misst den Gesamtwert einer Kund:in über den Zeitraum von einem Jahr.", "answer": "falsch", "explanation": "CLV misst den gesamten Wert über die Kundenlebenszeit, nicht nur ein Jahr."},
    {"question": "1.18 b) Mit dem 'Net Promoter Score (NPS)' misst die Fit3 die Effizienz seiner Online-Werbung.", "answer": "falsch", "explanation": "Der NPS misst die Weiterempfehlungsbereitschaft, nicht Werbewirkung."},
    {"question": "1.18 c) Anhand der 'Churn Rate' kann bestimmt werden, wie viele neue Kund:innen in einem bestimmten Zeitraum gewonnen wurden.", "answer": "falsch", "explanation": "Die Churn Rate misst Kundenverluste, nicht -gewinne."},
    {"question": "1.18 d) 'Organic Reach' in den sozialen Medien bezieht sich auf den Effekt der bezahlten Werbeimpressionen die Fit3 erzielt hat.", "answer": "falsch", "explanation": "Organic Reach ist unbezahlte Reichweite."},
    {"question": "1.19 a) Aktive Marketingautomatisierung bezieht sich auf Systeme, die automatisch auf das Verhalten der Nutzer reagieren, wie z.B. das Senden einer E-Mail nach einem Kauf.", "answer": "richtig", "explanation": "Das ist die Definition aktiver Automatisierung."},
    {"question": "1.19 b) Passive Marketingautomatisierung bedeutet, dass ein System regelmäßig Marketingaufgaben ohne menschliches Eingreifen ausführt, unabhängig vom Verhalten der Benutzer.", "answer": "richtig", "explanation": "Das entspricht passiver Automatisierung."},
    {"question": "1.19 c) Bei aktiver Marketingautomatisierung werden Marketingmaßnahmen nur manuell durchgeführt.", "answer": "falsch", "explanation": "Aktive Automatisierung heißt automatische Reaktion auf Nutzungsverhalten."},
    {"question": "1.19 d) Passive Marketingautomatisierung kann beinhalten, regelmäßig Berichte und Analysen zu generieren und an das Marketingteam zu senden.", "answer": "richtig", "explanation": "Das ist ein typisches Beispiel für passive Automatisierung."},
    
    {"question": "2.1 Der Telekom-Anbieter Ollay möchte die Preise seiner Leistungen anpassen. a) Der Internet-Router von Ollay kostet im Einkauf CHF 10 / Stück [...] Das nennt sich kundenorientierte Preissetzung.", "answer": "falsch", "explanation": "Das ist eine kostenorientierte, nicht kundenorientierte Preissetzung."},
    {"question": "2.1 Der Telekom-Anbieter Ollay möchte die Preise seiner Leistungen anpassen. b) Das Handy-Abo Ollay Super One wird [...] Dabei handelt es sich um eine Skimmingstrategie.", "answer": "richtig", "explanation": "Skimmingstrategie = hoher Startpreis, später sinkend – das passt."},
    {"question": "2.1 Der Telekom-Anbieter Ollay möchte die Preise seiner Leistungen anpassen. c) Das Internet-Angebot Ollay Fast Glass wird [...] Dabei handelt es sich um eine technologische Preisdifferenzierung.", "answer": "richtig", "explanation": "Technologische Preisdifferenzierung liegt vor (Gerätetyp abhängig)."},
    {"question": "2.1 Der Telekom-Anbieter Ollay möchte die Preise seiner Leistungen anpassen. d) Das Internet-Angebot Ollay Rather Slow [...] Dabei handelt es sich um eine personelle Preisdifferenzierung.", "answer": "richtig", "explanation": "Studentenrabatt = personelle Preisdifferenzierung."},
    {"question": "2.1 Der Telekom-Anbieter Ollay möchte die Preise seiner Leistungen anpassen. e) Das Internet-Angebot Ollay Friggin’ Fast [...] Dabei handelt es sich um ein gemischtes Preisbündel.", "answer": "richtig", "explanation": "Kombiangebot ist gemischtes Preisbündel."},

    {"question": "2.2 Der internationale Nahrungsmittelkonzern Éltsen AG hat sich entschieden, das Produktportfolio zu überarbeiten. a) Das Produkt Éltcafé soll neu auch noch mit Haselnussgeschmack angeboten werden [...] Produktvarietät.", "answer": "richtig", "explanation": "Unterschied im Geschmack = Produktvarietät."},
    {"question": "2.2 Der internationale Nahrungsmittelkonzern Éltsen AG hat sich entschieden, das Produktportfolio zu überarbeiten. b) Das Produkt Éltcafé soll neu auch ohne Koffein angeboten werden [...] Produktvarietät.", "answer": "richtig", "explanation": "Koffeinfrei = andere Variante = Produktvarietät."},
    {"question": "2.2 Der internationale Nahrungsmittelkonzern Éltsen AG hat sich entschieden, das Produktportfolio zu überarbeiten. c) Das Produkt Éltcafé enthält [...] Diese werden nun ersetzt. [...] Leistungsvariation.", "answer": "richtig", "explanation": "Rezepturänderung = Leistungsvariation."},
    {"question": "2.2 Der internationale Nahrungsmittelkonzern Éltsen AG hat sich entschieden, das Produktportfolio zu überarbeiten. d) Das Produkt Éltcafé erhält neue Verpackung [...] Produkt-Relaunch.", "answer": "richtig", "explanation": "Verpackung + Preisänderung = Relaunch."},
    {"question": "2.2 Der internationale Nahrungsmittelkonzern Éltsen AG hat sich entschieden, das Produktportfolio zu überarbeiten. e) Éltsen druckt Rezeptideen auf Verpackung [...] Value-Added-Service.", "answer": "richtig", "explanation": "Zusätzlicher Service = Value-Added."},

    {"question": "2.3 Die Versicherung Railibom möchte sein Kundenmanagement neu aufsetzen. a) Zukünftig soll mehr nach dem Paradigma des Inbound-Marketings gearbeitet werden.", "answer": "richtig", "explanation": "Inbound = Content Marketing, weniger Push wie Direct Mail."},
    {"question": "2.3 Die Versicherung Railibom möchte sein Kundenmanagement neu aufsetzen. b) Im Rahmen einer Kundenwert-Analyse wurden A-, B-, C-Kunden segmentiert.", "answer": "richtig", "explanation": "Typische ABC-Segmentierung zur Ressourcenallokation."},
    {"question": "2.3 Die Versicherung Railibom möchte sein Kundenmanagement neu aufsetzen. c) Neukunden sollen mit 24-Monats-Vertrag gebunden werden. [...] Verbundenheitsstrategie.", "answer": "falsch", "explanation": "Das ist Gebundenheit, nicht emotionale Verbundenheit."},
    {"question": "2.3 Die Versicherung Railibom möchte sein Kundenmanagement neu aufsetzen. d) Unattraktive Kunden zahlen höhere Prämien bis Kündigung. [...] Cost Escalation.", "answer": "richtig", "explanation": "Cost Escalation trifft hier zu."},
    {"question": "2.3 Die Versicherung Railibom möchte sein Kundenmanagement neu aufsetzen. e) Jeder Kunde erhält Kundenwertanalyse zur Investitionsplanung.", "answer": "richtig", "explanation": "Kundenwertanalyse für Steuerung und Bindung sinnvoll."},

    {"question": "2.4 Das Handelsunternehmen Pooc überarbeitet seine Kommunikationsstrategie. a) Vegane Kund:innen über Inhaltsstoffe informieren. [...] kognitives Kommunikationsziel.", "answer": "richtig", "explanation": "Faktenwissen = kognitives Ziel."},
    {"question": "2.4 Das Handelsunternehmen Pooc überarbeitet seine Kommunikationsstrategie. b) Einheitliche Logos, Farben etc. [...] formale Integration.", "answer": "richtig", "explanation": "Standard-Beispiel für formale Integration."},
    {"question": "2.4 Das Handelsunternehmen Pooc überarbeitet seine Kommunikationsstrategie. c) Für einzigartige Leistung auch USP entwickeln.", "answer": "falsch", "explanation": "Für Kommunikation = UCP, nicht USP."},
    {"question": "2.4 Das Handelsunternehmen Pooc überarbeitet seine Kommunikationsstrategie. d) Sponsoring bringt laut Marketingverantwortlichen keine Vorteile.", "answer": "richtig", "explanation": "Sponsoring kann auch Risiken bergen – korrekt formuliert."},
    {"question": "2.4 Das Handelsunternehmen Pooc überarbeitet seine Kommunikationsstrategie. e) Pooc zahlt für Einblendung in TV-Serie – Product Placement.", "answer": "richtig", "explanation": "Typisches Beispiel für Product Placement."},

    {"question": "2.5 Die mittelständische Böller AG möchte ihr Produktangebot diversifizieren. In welchem Zusammenhang würde die PESTEL-Analyse am sinnvollsten angewendet? a) Auswahl von Lieferanten für neue Produktkomponenten.", "answer": "falsch", "explanation": "Lieferantenwahl ist mikroökonomisch, nicht PESTEL-relevant."},
    {"question": "2.5 Die mittelständische Böller AG möchte ihr Produktangebot diversifizieren. In welchem Zusammenhang würde die PESTEL-Analyse am sinnvollsten angewendet? b) Entwicklung neuer Technologien für die Produktion.", "answer": "falsch", "explanation": "Technologieentwicklung ist intern – nicht externes Umfeld."},
    {"question": "2.5 Die mittelständische Böller AG möchte ihr Produktangebot diversifizieren. In welchem Zusammenhang würde die PESTEL-Analyse am sinnvollsten angewendet? c) Einschätzung des Marktwachstums und neuer Kundensegmente.", "answer": "richtig", "explanation": "Demografisch/sozio-kulturell – PESTEL-relevant."},
    {"question": "2.5 Die mittelständische Böller AG möchte ihr Produktangebot diversifizieren. In welchem Zusammenhang würde die PESTEL-Analyse am sinnvollsten angewendet? d) Verständnis des makroökonomischen Umfelds.", "answer": "richtig", "explanation": "Makroökonomische Trends = zentrales Element der PESTEL."},
    {"question": "2.5 Die mittelständische Böller AG möchte ihr Produktangebot diversifizieren. In welchem Zusammenhang würde die PESTEL-Analyse am sinnvollsten angewendet? e) Entwurf von Produktdesigns, die auf Verbrauchervorlieben abzielen.", "answer": "falsch", "explanation": "Designentwicklung ist intern, nicht Umfeldfaktor."},

    {"question": "2.6 Das Softwareunternehmen SAN-IT-AS erwägt die Entwicklung eines neuen Produktes für den Gesundheitssektor. In welcher Phase des Entscheidungsprozesses würde eine PESTEL-Analyse den grössten Nutzen bieten? a) Festlegung des anfänglichen Feature-Sets für das Produkt.", "answer": "falsch", "explanation": "Feature-Set ist internes Design, kein Umfeldbezug."},
    {"question": "2.6 Das Softwareunternehmen SAN-IT-AS erwägt die Entwicklung eines neuen Produktes für den Gesundheitssektor. In welcher Phase des Entscheidungsprozesses würde eine PESTEL-Analyse den grössten Nutzen bieten? b) Analyse des externen Umfelds zur Sicherstellung der langfristigen Tragfähigkeit.", "answer": "richtig", "explanation": "Genau dafür ist die PESTEL-Analyse gedacht."},
    {"question": "2.6 Das Softwareunternehmen SAN-IT-AS erwägt die Entwicklung eines neuen Produktes für den Gesundheitssektor. In welcher Phase des Entscheidungsprozesses würde eine PESTEL-Analyse den grössten Nutzen bieten? c) Programmierung und technischer Entwurf der Software.", "answer": "falsch", "explanation": "Programmierung = technische Umsetzung, kein PESTEL-Zeitpunkt."},
    {"question": "2.6 Das Softwareunternehmen SAN-IT-AS erwägt die Entwicklung eines neuen Produktes für den Gesundheitssektor. In welcher Phase des Entscheidungsprozesses würde eine PESTEL-Analyse den grössten Nutzen bieten? d) Bewertung des Wettbewerbsumfelds im Gesundheitssektor.", "answer": "falsch", "explanation": "Wettbewerb = Teil von Porter's Five Forces, nicht PESTEL."},
    {"question": "2.6 Das Softwareunternehmen SAN-IT-AS erwägt die Entwicklung eines neuen Produktes für den Gesundheitssektor. In welcher Phase des Entscheidungsprozesses würde eine PESTEL-Analyse den grössten Nutzen bieten? e) Entscheidung über das Budget für die Produktmarketing-Kampagne.", "answer": "falsch", "explanation": "Budgetierung ist interne Finanzplanung, kein PESTEL-Thema."},
    
]

# Streamlit Setup
st.set_page_config(page_title="Marketing Quiz", layout="centered")
st.title("📱 Marketing Quiz")
st.write("Kapitel 1.1 – 1.19 | Entscheide, ob Aussagen richtig oder falsch sind.")

# Session State Initialisierung
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.quiz_done = False
    st.session_state.user_answer = None

# Quiz Logik
if not st.session_state.quiz_done and st.session_state.current < len(st.session_state.shuffled_questions):
    q = st.session_state.shuffled_questions[st.session_state.current]

    if not st.session_state.show_result:
        st.subheader(q["question"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Richtig", key="richtig"):
                st.session_state.show_result = True
                st.session_state.user_answer = "richtig"
                if q["answer"] == "richtig":
                    st.session_state.score += 1
        with col2:
            if st.button("❌ Falsch", key="falsch"):
                st.session_state.show_result = True
                st.session_state.user_answer = "falsch"
                if q["answer"] == "falsch":
                    st.session_state.score += 1

    if st.session_state.show_result:
        if st.session_state.user_answer == q["answer"]:
            st.markdown("<div style='background-color:#d4edda;padding:10px;border-radius:8px;'>✅ Deine Antwort war richtig!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color:#f8d7da;padding:10px;border-radius:8px;'>❌ Deine Antwort war falsch!</div>", unsafe_allow_html=True)

        st.info(f"**Begründung:** {q['explanation']}")

        if st.button("➡️ Nächste Frage", key=f"next_{st.session_state.current}"):
            st.session_state.current += 1
            st.session_state.show_result = False
            st.session_state.user_answer = None
            st.rerun()

# Quiz abgeschlossen
elif not st.session_state.quiz_done:
    st.session_state.quiz_done = True
    st.success(f"✅ Quiz abgeschlossen! Ergebnis: {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
    if st.button("🔁 Quiz neu starten", use_container_width=True):
        for key in ["shuffled_questions", "current", "score", "show_result", "quiz_done", "user_answer"]:
            del st.session_state[key]
