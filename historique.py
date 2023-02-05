"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - historique.py -
# Renferme la classe Historique, qui est la fenêtre affichant l'historique
# des messages
#
###########################################################################
"""

from tkinter import Text, Button, END, INSERT
from tkinter.font import Font
from fenetre import Fenetre
from basedonnees import BaseDonnees


class Historique(Fenetre):
    """ Contenneur de la fenêtre affichant l'historique """

    def __init__(self, texte = "Aucun Titre"):
        """ Constructeur """
        Fenetre.__init__( self, texte )
        self.nom = texte

        # polices employées
        police_affichage = Font(family = 'Helvetica', size = 13, weight = "normal")
        police_bouton = Font(family = 'Helvetica', size = 18, weight = "bold")

        # zone d'affichage du texte
        self.zoneAffichage = Text( self, font = police_affichage )
        self.zoneAffichage.configure( width = 50, height = 27 )
        self.zoneAffichage.grid( row = 0, column = 0, columnspan = 3 )

        # bouton de fermeture
        self.bouton_fermer = Button( self, text = "Fermer", font = police_bouton )
        self.bouton_fermer.grid( row = 1, column = 1, sticky = "EW" )
        self.bouton_fermer.configure( command = self.callback_bouton )

        # on se connecte à la base de données
        self.base_donnees = BaseDonnees( self.nom )
        

    def affiche(self):
        # on affiche l'entête
        entete = "Date" + " "*15 + "Heure" + " "*8 +"Événement\n"
        self.zoneAffichage.delete( '1.0', END )
        self.zoneAffichage.insert( INSERT, entete )
        self.zoneAffichage.insert( INSERT, "="*(len(entete)-7) + "\n" )

        # on effectue la lecture des données et on affiche une ligne à la fois
        resultat = self.base_donnees.lireMessages( 20 )
        for ligne in resultat:
            self.zoneAffichage.insert( INSERT, str(ligne["date"]) + "    " + \
                                       str(ligne["heure"]) + "    " + \
                                       str(ligne["evennement"]) + "\n" )


    def callback_bouton(self):
        if self.base_donnees is not None:
            self.base_donnees.termine()
        self.destroy()


# espace d'execution pour tests
def main():

    historique = Historique( "Historique" )
    historique.affiche()
    historique.roule()



if __name__ == '__main__':
    main()
