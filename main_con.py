"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - main_con.py -
# Fichier pour démarrer la console
#
###########################################################################
"""

from panneau import Panneau
from globales import *


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