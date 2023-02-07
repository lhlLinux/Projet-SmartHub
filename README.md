## Description

Ce projet démontre l'usage d'une console permettant de communiquer à distance au SmartHub d'une maison intelligente via MQTT. Le projet comporte deux composantes principales: une console (représentant une application sur un dispositif portable) et un SmartHub (représentant une maison intelligente). MongoDB est également utilisé pour stocker les dernières 20 modifications dans un historique.


#### Librairies utilisées:

- MQTT: pour la communication entre les deux applications
- MongoDB: pour l'historique
- tkinter: pour l'interface
- RPiSim: émulateur du GPIO (l'émulateur peut être substitué par un vrai GPIO lorsque roulé sur un Raspberry Pi)


#### Instruction

Pour exécuter le programme il faut rouler ces deux fichiers, chacun dans sa propre console:
- main_con.py
- main_hub.py


#### Demo
![Capture d'écran](/demo_smarthub.png "screenshot")


#### Liste des fichiers

- main_con.py -
Fichier pour démarrer la console

- main_hub.py - 
Fichier pour démarrer le dispositif intelligent (smarthub)

- basedonnees.py -
Base de données des messages, renferme la classe BaseDonnees qui abstrait la connection avec la bdd MongoDB, offrant des méthodes d'ajout et de lecture de messages.

- cadre.py -
Renferme la classe Cadre, qui est un LabelFrame comportant les deux boutons "ON"/"OFF" ainsi que l'étiquette confirmant l'état choisis

- carte.py -
Renferme la classe Carte, qui est en faite le GPIO

- fenetre.py -
Renferme la classe Fenetre, dérivée d'une fenêtre tkinter de base

- globales.py -
Fichier global contenant des "constantes" communes à plusieurs fichiers

- historique.py -
Renferme la classe Historique, qui est la fenêtre affichant l'historique des messages

- messagerie.py -
Renferme la classe Messagerie, qui abstrait la connexion à MQTT, offrant des méthodes
de réception et d'envoi de messages

- panneau.py -
Renferme le panneau de contrôle (la console), permettant de contrôler à distance les objets de la résidence

- smarthub.py -
Renferme la classe SmartHub, représentant le dispositif intelligent 
de contrôle des objets de la résidence



