"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - globales.py -
# Fichier global contenant des "constantes" utilisées
# par plusieurs autres fichiers
#
###########################################################################
"""


from tkinter import GROOVE # requis pour STYLE_BORDURE


# constantes pour affichage d'interfaces tkinter
BOUTON_ON_TEXTE = "ON"
BOUTON_OFF_TEXTE = "OFF"
BOUTON_BORDURE = 4
BOUTON_LARGEUR = 4
STYLE_BORDURE = GROOVE

COULEUR_POLICE = "#555555"
COULEUR_POLICE_ETIQUETTE = "#EE5555"
COULEUR_ETIQUETTE = "#EE4444"

PADDING = 10

# connexion via MQTT
MQTT_BROKER = "127.0.0.1"

# participants et racines des sujets d'émission via MQTT
PARTICIPANT1 = "CONSOLE"
PARTICIPANT2 = "HUB"

# constantes des différentes destinations des messages
class SYSTEME_ALARME:
    ELEMENT = "Système Alarme"
    ETAT_ON = "Armé"
    ETAT_OFF = "Désarmé"
    BROCHE = 23

class LUMIERE_SALON:
    ELEMENT = "Lumière Salon"
    ETAT_ON = "ON"
    ETAT_OFF = "OFF"
    BROCHE = 18
    
class LUMIERE_ENTREE:
    ELEMENT = "Lumière Entrée"
    ETAT_ON = "ON"
    ETAT_OFF = "OFF"
    BROCHE = 17


"""
SYSTEME_ALARME = 23
LUMIERE_SALON  = 18
LUMIERE_ENTREE = 17
"""
