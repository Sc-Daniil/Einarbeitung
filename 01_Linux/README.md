# Einrichten einer Virtual Machine (VM) unter Rocky Linux

## Beschreibung
In diesem Projekt wird eine Virtual Machine (VM) unter dem Betriebsystem Rocky Linux eingerichtet. Es werden verschiedene Benutzer angelegt, die Partitionierung vorgenommen und verschiedene Programme installiert.


### Benutzer anlegen
- `root`: Der Hauptbenutzer mit vollständigen administrativen Rechten.
- `admin`: Ein Benutzer mit sudo-Berechtigungen.
- `entwickler`: Ein Benutzer für das tägliche arbeiten. Du kannst ihn benennen wie du möchtest 


Linux - Installition 

### Installierte Programme
a) nvim  Done
b) Git  Done
c) check-mk Done
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
Linux - `top`

- Wie kann man Skripte unter Linux erstellen und ausführen?
Datei erstellen --> 'touch'



- Was ist ein Linux-Kernel und wie kann man ihn aktualisieren?
Linux-Kernel ist Hauptkomponent von einem Betriebssystem Linux, Software-Schicht, die als Vermitteler zwischen der Hardware dient 
Aktualisieren --> Paketmanager (DNF)


- Was sind symbolische Links und wie unterscheiden sie sich von Hardlinks?



- Welche Vorteile bietet die Nutzung von LTS (Long Term Support) Versionen einer Linux-Distribution?
Support, Bugfixing, Aktualisirung 

- Wie schreibt man Kommentare in Bash?
# <---

- Was ist vim?
Vim - Texteditor für Linux oder Unix. Braucht nut Tastatur 


### Linux-Befehle
Was bewirken folgende Befehle:
- `history`
Zeigt die letzten eingegebenen Kommandos als Liste

- `chmod`
chmod changes the access permissions of the named files

- `chown`
chown changes the user and/or group ownership of each given file to new-owner or to the user and group of an existing reference file

- `mv test.txt abc`
verschiebt/benennt Dateien 

- `ll | grep test`

ll - zeigt aktuelle Dateien als liste 
ls -l
ll | grep test zeigt nur die Dateien mit dem Name "test" 


- `find . -name cisco`
sucht Datei in gleicher Ordner + Sub ductorys 

- `find / -name cisco`
sucht Datei in allen Plätzen 

- `tar -xvf archive.tar.gz`


- `df -h`
df - zeigt die Belegung aller Dateisysteme
df -h gleiche aber zeigt in Einheiten wie KB, MB, GB

- `du -sh directory`
du - zeigt die Belegung von aktuellem Raum 
du -sh gleich aber in Einheit  

- `ps aux`
ps - report a snapshot of the current processes.
ps aux - zeigt jede Prozesse im System


- `grep pattern file`
Sucht "pattern" in den Dateien durch. Schreibt im Terminal Sätze, wo "pattern" steht


- `top`
zeigt alle aktive Prozesse



- `netstat -tuln`

- `ifconfig`
interface config - zeigt Netzwerkschnittstellen  


- `ping host`
prüft, ob ein Gerät erreichbar ist (im Netzwerk)  

