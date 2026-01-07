# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter dem Betriebsystem Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.


### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer für das tägliche arbeiten. Du kannst ihn benennen wie du möchtest 


### Installierte Programme
a) nvim  
b) Git  
c) check-mk 
b) Erstelle ein Basis Monitoring für ein Server, Switches, Firewall 

## Fragen und Antworten
- Was ist Linux und wie unterscheidet es sich von anderen Betriebssystemen wie Windows oder macOS?
Linux - Betribsysteme, die kostenlose und Open Source ist. 
Linux - basiert auf Linux-Kerne und besteht aus modulare Softssysteme, die von Entwicklern auf der ganzen Welt weiterentwickelt wird.    


- Was sind die Vorteile der Verwendung von Linux im Vergleich zu anderen Betriebssystemen?
Linux: produktivestes Betriebssystem; große Flexibilität; weniger Malware 
Der Benutzer hat volle Kontrolle über sein System. Der Benutzer kann alles (UI, Hauptdaten) überschreiben.


- Warum sollt man nicht dauerhaft mit dem root User arbeiten?
Um zu verhindern, dass System durch zufälligen Code nicht kaputt machen.

- Was ist Virtualisierung und welche Vorteile bieten VMs?
Virtualisierung - Technologie, die die Erstellung virtueller Umgebungen aus physischen Maschine ermöglicht. 

- Was sind yum und dnf?
YUM - Yellowdog Updater, Modified 
DNF - Dandified YUM
YUM und DNF sind Paketmanagement-Systeme für Linux-Distribution

Distribution - Prozess, um Anwendungen und Updates automatisch und zentral auf vielen Geräten eines Netzwerks zu installieren und zu verwalten.

DNF - braucht weniger RAM, schneller
YUM - benutzen jeztz nicht
YUM < DNF

- Was ist eine IDE und wie unterscheidet sie sich von einem Texteditor?
IDE - Integrated Development Environment
IDE hilft, um Code zu schreiben (linter - zieght Syntaxfehler), zu testen (Debugging) und zu verwalten (Hotkeys).
Texteditor ist zum Bearbeiten von Texten. Hat nicht die gleiche Funktionen wie IDE

- Was ist der Unterschied zwischen einem LSP und einem Texteditor?
LSP -  Language Server Protocol 
LSP - Protocol zwischen Code Editor und IDE und Server, Standart wie zwei Programme die Information tauschen.

Benachrichtigung: "Hey, ich habe Inhalt einen Datei getauscht", Server schickt wo Syntaxfehler sind
Anfrage: "Hey, sag mir wo diese Sache definiert ist"

Texteditor - Code schreiben
LSP - Kommunikation

- Wie kann man Programme im Hintergrund laufen lassen und Prozesse verwalten?
Mit den Softwaretools wie Task-Manager auf Windows.


- Wie kann man Skripte unter Linux erstellen und ausführen?


- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?
- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
- Wie schreibt man Kommentare in Bash?
- Was ist vim?

### Linux-Befehle
Was bewirken folgende Befehle:
- `history`
- `chmod`
- `chown`
- `mv test.txt abc`
- `ll | grep test`
- `find . -name cisco`
- `find / -name cisco`
- `tar -xvf archive.tar.gz`
- `df -h`
- `du -sh directory`
- `ps aux`
- `grep pattern file`
- `top`
- `netstat -tuln`
- `ifconfig`
- `ping host`


