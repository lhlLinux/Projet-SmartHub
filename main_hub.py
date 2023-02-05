"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - main_hub.py - 
# Fichier pour démarrer le dispositif intelligent smarthub
#
###########################################################################
"""


from smarthub import SmartHub
from globales import *


def main():

    nom = PARTICIPANT2
    
    sujets = [ PARTICIPANT1 + "/" + SYSTEME_ALARME.ELEMENT, \
               PARTICIPANT1 + "/" + LUMIERE_ENTREE.ELEMENT, \
               PARTICIPANT1 + "/" + LUMIERE_SALON.ELEMENT ]  
    
    residence = SmartHub( nom, sujets )

    residence.roule()
   
    residence.termine()
    print( "Terminé 'main' du " + nom )


if __name__ == '__main__':
    main()