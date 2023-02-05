"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier:- cadre.py -
# Renferme la classe Cadre, qui est un LabelFrame comportant les deux
# boutons "ON"/"OFF" ainsi que l'étiquette confirmant l'état choisis
#
###########################################################################
"""

from tkinter import LabelFrame, Button, Label, GROOVE
from tkinter.font import Font
from globales import *


class Cadre(LabelFrame):

    ordre = 0 # variable statique pour calcul automatique de l'ordre vertical

    def __init__(self, master = None, texte = "", etatON = "ON", etatOFF = "OFF"):
        """ Constructeur """

        LabelFrame.__init__(self, master, fg = COULEUR_POLICE, text = texte, padx = PADDING , pady = PADDING)
        
        self.nom = texte # ceci est le nom de l'élément
        self.parent = master
        self.etatON = etatON
        self.etatOFF = etatOFF

        # on établit la position de cet élément sur l'interface
        self.grid( row = Cadre.ordre, column = 0, sticky = "EW" )

        # bouton ON
        self.boutON = Button( self, text = BOUTON_ON_TEXTE, command = lambda : self.callback_bouton( self.etatON ) )
        self.boutON.grid( row = 0, column = 0, sticky = "E" )

        # Le bouton OFF
        self.boutOFF = Button( self, text = BOUTON_OFF_TEXTE, command = lambda : self.callback_bouton( self.etatOFF ) )
        self.boutOFF.grid( row = 0, column = 1, sticky = "E" )

        # L'etiquette d'affichage
        self.etiquette = Label( self, text = "" )
        self.etiquette.grid( row = 0, column = 2, sticky = "E" )
        self.etiquette.configure( text = etatOFF )

        Cadre.ordre += 1 # on incrémente le compteur pour le prochain élément


    def callback_bouton( self, etat ):
        """
        Puisque PyMongo ne spécifie que la valeur du message et non pas le sujet à la fonction 'on_message'
        on doit construire les messages comme ceci:
        Le sujet du message consiste du nom de l'émetteur + le nom du dispositif
        La valeur du message consiste du nom du dispositif + l'état
        Comme ça on sait quel élément est adressé et quelle est sa valeur
        """
        # on inscrit le message dans la bdd. sel.nom est le nom du cadre représentant un dispositif/élément spécifique
        self.parent.base_donnees.ajouterMessage( self.nom + "/" + etat )
        
        # on envoie le message via MQTT
        self.parent.messagerie.publieMessages( self.parent.nom + "/" + self.nom, self.nom + "/" + etat )


        