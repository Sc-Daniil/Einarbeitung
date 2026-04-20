## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

- [x] 1.  **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.

- [x] 2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.

- [x] 3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.

- [x] 4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   - [x] a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   - [x] b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   - [x] c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   - [x] d) **Auslesen**: Daten werden aus der Datenbank abgerufen.
 
 - [x] 5. **Fragen**

### Fragen:

- Welche Datenbanken gibt es? 
	SQL:
		MySQL, SQLite
	NoSQL:
		Oracle, Excel, Json
		
- Wann macht welcher Typ Sinn? SQL bei gleichbleibenden Attributen.
		INTEGER - ganze Zahlen
		TEXT - Zeichen  (string Attribute)
		BOOLEAN - True/False
		REAL - Zahlen mit Komma 
		BLOB - Binärdaten (audio, pdf, jpg, png)
		NULL - Nichts, keine werte

- Was ist ein Primary Key und was ein Foreign Key?
	Primary key ist eindeutiger Identifikator für jede Zeile mit einem Wert. Darf nicht sich wiederholen
	Foreign key ist Referenzfeld, das auf Priramy Key verweist. Macht Verbindung zwischen Tabellen 
	
- Was ist ein nativer und was ein künstlicher Primary Key?
	Nativer Primary Key - bestehender eindeutiger Schlüssel
	Künstlicher Primary Key - eindeutiger Schlüssel. Er wurde innerhalb Datenbank erstellt
	  
- Welche Beziehungstypen zwischen Tabellen gibt es?
	One-to-One  1:1
	One-to-Many 1:n
	Many-to-Many  n:m
	
- Welche Wildcards gibt es in MySQL und was bedeuten sie?
	%  - ersetzt Anzahl von Zeichen
	_   -  ersetzt genau einen Zeichen 

- Was ist ein Join?
	Eine Operation, die Daten aus mehreren Tabellen anhand verbundener Spalten zusammenführt
	

- Was ist ein left- und was ein right-Join?
	[Visual JOIN](https://joins.spathon.com/)


- Was ist das kartesische Produkt zweier Tabellen?

	
- Was ist Kaskadierung?
	Es ist eine automatische Änderung der verknüpften Daten/Tabellen (Foreign Key) in Bezug auf den Eltern­datensatz (Primary Key)
	
	"DELETE CASCADE"
	
	Zum Beispiel
	 führt bei "CASCADE" das Löschen einer Zeile (mit Primary Key), an die andere Zeilen (zu Foreign Key) gebunden sind, ebenfalls zum Löschen dieser verbundenen Zeilen
	
- Wann werden Gruppierungen benötigt?
	wird verwendet, um Zeilen mit gleichen Werten zusammenzufassen
	
	Zum Beispiel gibt es zwei Spalte:  "Namen" und "Bananenkisten" 
		In der erste Zeilen steht "Ivan" und 100 Bananenkisten
		In der zweite Zeilen steht "Ivan" und 200 Bananenkisten
		Hier wird Gruppierung verwendet (zum Beispiel für gemeinsames Ergebnisse  ("SUM"))
		--> "Ivan" und 300 Bananenkisten 
		
- Was ist ein DBMS?
	Datenbankmanagementsystem - System zur Verwaltung einer Datenbank
	
- Was versteht man unter Datenintegrität?
	Es ist ein Zustand, in dem alle Daten in allen Tabellen korrekt, genau und widerspruchsfrei sind
	
	Jeder Primary Key ist eindeutig;
	die Beziehungen zwischen den Tabellen sind korrekt;
	es gibt keine null-Werte/Zeile
	
- Was ist Normalisierung?
	Die Aufteilung von Daten miteinander verbundene Tabellen, um Duplikate zu minimisieren
	 
- Was sind Aggregationsfunktionen und welche gibt es? (3 Beispiele)
	Funktionen, die Operationen auf einer ausgewählten Datengruppen ausführen
	`MIN` `MAX` `AVG` `COUNT` 
