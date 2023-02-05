"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - panneau.py -
# Renferme le panneau de contrôle (la console), permettant de contrôler
# à distance les dispositifs de la résidence
#
###########################################################################
"""


from tkinter import Text, Button, LabelFrame, GROOVE
from tkinter.font import Font

from fenetre import Fenetre
from cadre import Cadre
from historique import Historique
from basedonnees import BaseDonnees
from messagerie import Messagerie

from globales import *


class Panneau(Fenetre):

    def __init__(self, texte = "Aucun Titre", sujets = ["AUCUN"]):
        """ Constructeur """
        Fenetre.__init__( self, texte )

        # polices globales
        self.police_de_base = Font(family = 'Helvetica', size = 14, weight = "bold")
        self.police_element = Font(family = 'Helvetica', size = 18, weight = "bold")

        # quelqus réglages spécifiques à cette fenêtre
        self.option_add("*font", self.police_de_base)
        self.option_add("*LabelFrame.foreground", COULEUR_POLICE)

        self.option_add("*Label.font", self.police_element)
        self.option_add("*Label.foreground", COULEUR_ETIQUETTE)
        self.option_add("*Label.width", 10)

        # on établit un style global pour les boutons
        self.option_add("*Button.font", self.police_element)
        self.option_add("*Bouton.width", 4)
        self.option_add("*Button.relief", GROOVE)
        self.option_add("*Button.borderwidth", 4)
        self.option_add("*Button.foreground", "#444444")

        # les trois premiers cadres
        self.cadreAlarme = Cadre( self, SYSTEME_ALARME.ELEMENT, SYSTEME_ALARME.ETAT_ON, SYSTEME_ALARME.ETAT_OFF )
        self.cadreEntree = Cadre( self, LUMIERE_ENTREE.ELEMENT, LUMIERE_ENTREE.ETAT_ON, LUMIERE_ENTREE.ETAT_OFF )
        self.cadreSalon  = Cadre( self, LUMIERE_SALON.ELEMENT , LUMIERE_SALON.ETAT_ON , LUMIERE_SALON.ETAT_OFF )

        # on s'occupe du dernier cadre, comportant qu'un seul bouton
        self.cadreHistorique = LabelFrame( self, text = "Historique", padx = PADDING, pady = PADDING, fg = COULEUR_POLICE )
        self.cadreHistorique.grid( row = Cadre.ordre + 1, column = 0, sticky = "EW" )

        # on prepare le bouton de ce dernier
        self.boutonAfficher = Button( self.cadreHistorique, text = "Afficher", width = 8 )
        self.boutonAfficher.grid( row = 0, column = 0, sticky = "E" )
        self.boutonAfficher.configure( command = lambda: self.afficherHistorique() )
        
        # on initialise la connection à la bdd et le système de messagerie
        self.base_donnees = BaseDonnees( texte )
        self.messagerie = Messagerie( self, texte, sujets )        


    def afficherHistorique(self):
        self.fenetre_historique = Historique( "Historique" )
        self.fenetre_historique.affiche()
        self.fenetre_historique.roule()


    def traiteMessages(self, message):
        element, etat = message.split("/")
        
        # malgré qu'on peut tout simplement executer les deux fonctions (le changement de l'état et la confirmation de celui-ci)
        # on ne peut le faire ainsi car on doit valider que les valeurs sont correctes
        # ainsi que d'effectuer les changement aux bons éléments
        
        # système d'alarme
        if element == SYSTEME_ALARME.ELEMENT:
            if etat == SYSTEME_ALARME.ETAT_ON or etat == SYSTEME_ALARME.ETAT_OFF:
                self.cadreAlarme.etiquette.configure( text = etat )
        
        # lumière de l'entrée   
        elif element == LUMIERE_ENTREE.ELEMENT:
            if etat == LUMIERE_ENTREE.ETAT_ON or etat == LUMIERE_ENTREE.ETAT_OFF:
                self.cadreEntree.etiquette.configure( text = etat )
                
        # lumière du salon
        elif element == LUMIERE_SALON.ELEMENT:
            if etat == LUMIERE_SALON.ETAT_ON or etat == LUMIERE_SALON.ETAT_OFF:
                self.cadreSalon.etiquette.configure( text = etat )


    def termine(self):
        if self.base_donnees is not None:
            self.base_donnees.termine()
        if self.messagerie is not None:
            self.messagerie.termine()
       
        print("Terminé: " + self.nom)


    def __del__(self):
        print("destructeur(): " + self.nom)

    
# espace d'execution pour tests
def main():
        
    nom = PARTICIPANT1
    
    sujets = [ PARTICIPANT2 + "/" + SYSTEME_ALARME.ELEMENT, \
               PARTICIPANT2 + "/" + LUMIERE_ENTREE.ELEMENT, \
               PARTICIPANT2 + "/" + LUMIERE_SALON.ELEMENT ]    
        
    panneau = Panneau( nom, sujets )
    panneau.roule()
    panneau.termine()
    
    print( "Terminé: MAIN " + nom )


if __name__ == '__main__':
    main()


