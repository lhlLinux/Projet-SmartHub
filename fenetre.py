"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - fenetre.py -
# Renferme la classe Fenetre, qui est une fenetre tkinter de base
#
###########################################################################
"""


from tkinter import Tk, GROOVE
from tkinter.font import Font
from globales import *


class Fenetre(Tk):
    """ Représente une fenêtre de base """

    def __init__(self, texte = "" ):
        """ Constructeur """

        Tk.__init__(self) # appel du constructeur parent

        self.nom = texte
        self.title( texte )
        self.configure( padx = PADDING, pady = PADDING )
        self.resizable( width = False, height = False)


    def roule(self):
        self.mainloop()


    def termine(self):
        # à implémenter par les objets qui héritent cette classe
        pass
