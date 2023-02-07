## Description

Ce projet d�montre l'usage d'une console permettant de communiquer � distance au SmartHub d'une maison intelligente via MQTT. Le projet comporte deux composantes principales: une console (repr�sentant une application sur un dispositif portable) et un SmartHub (repr�sentant une maison intelligente). MongoDB est �galement utilis� pour stocker les derni�res 20 modifications dans un historique.


#### Librairies utilis�es:

- MQTT: pour la communication entre les deux applications
- MongoDB: pour l'historique
- tkinter: pour l'interface
- RPiSim: �mulateur du GPIO (l'�mulateur peut �tre substitu� par un vrai GPIO lorsque roul� sur un Raspberry Pi)


#### Instruction

Pour ex�cuter le programme il faut rouler ces deux fichiers, chacun dans sa propre console:
- main_con.py
- main_hub.py


#### Demo
![Capture d'�cran](/demo_smarthub.png "screenshot")


#### Liste des fichiers

- main_con.py -
Fichier pour d�marrer la console

- main_hub.py - 
Fichier pour d�marrer le dispositif intelligent (smarthub)

- basedonnees.py -
Base de donn�es des messages, renferme la classe BaseDonnees qui abstrait la connection avec la bdd MongoDB, offrant des m�thodes d'ajout et de lecture de messages.

- cadre.py -
Renferme la classe Cadre, qui est un LabelFrame comportant les deux boutons "ON"/"OFF" ainsi que l'�tiquette confirmant l'�tat choisis

- carte.py -
Renferme la classe Carte, qui est en faite le GPIO

- fenetre.py -
Renferme la classe Fenetre, d�riv�e d'une fen�tre tkinter de base

- globales.py -
Fichier global contenant des "constantes" communes � plusieurs fichiers

- historique.py -
Renferme la classe Historique, qui est la fen�tre affichant l'historique des messages

- messagerie.py -
Renferme la classe Messagerie, qui abstrait la connexion � MQTT, offrant des m�thodes
de r�ception et d'envoi de messages

- panneau.py -
Renferme le panneau de contr�le (la console), permettant de contr�ler � distance les objets de la r�sidence

- smarthub.py -
Renferme la classe SmartHub, repr�sentant le dispositif intelligent 
de contr�le des objets de la r�sidence



