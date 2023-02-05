"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - smarthub.py -
# Renferme la classe SmartHub, représentant le dispositif intelligent 
# de contrôle de objets dans la résidence
#
###########################################################################
"""

from tkinter import Label, Button
from tkinter.font import Font
from fenetre import Fenetre
from basedonnees import BaseDonnees
from messagerie import Messagerie
from carte import Carte
import threading
import time
from globales import *

COULEUR_ON = "#CC5555"
COULEUR_OFF = "#DDDDDD"

class SmartHub(Fenetre):
    
    def __init__(self, nom = "Aucun Titre", sujets = ["AUCUN"] ):
        """ Constructeur """

        self.etatOK = True
        
        Fenetre.__init__( self, nom )   # appel du constructeur parent

        # on uniformise les étiquettes
        self.police = Font(family = 'Helvetica', size = 12, weight = "bold")
        self.option_add("*Label.font", self.police)
        self.option_add("*Label.foreground", COULEUR_POLICE)
        
        # les étiquettes des témoins
        self.etq_alarme = Label(self, text = "Système\nd'Alarme" )
        self.etq_alarme.grid( row = 0, column = 0, sticky = "EW" )
                
        self.etq_entree = Label(self, text = "Lumière\nEntrée")
        self.etq_entree.grid( row = 0, column = 1, sticky = "EW" )
        
        self.etq_salon = Label(self, text = "Lumière\nSalon")
        self.etq_salon.grid( row = 0, column = 2, sticky = "EW" )
        
        # l'état des boutons
        self.temoin_alarme = Label(self, text = "Armé", width = 10, height = 5 )
        self.temoin_alarme.grid( row = 1, column = 0, sticky = "E" )
                
        self.temoin_entree = Label(self, text = "ON", width = 10, height = 5 )
        self.temoin_entree.grid( row = 1, column = 1, sticky = "E" )
        
        self.temoin_salon = Label(self, text = "ON", width = 10, height = 5 )
        self.temoin_salon.grid( row = 1, column = 2, sticky = "E" )        

        
        # on crée la carte GPIO et la messagerie MQTT
        self.carte = Carte()
        self.messagerie = Messagerie( self, nom, sujets )


    def traiteMessages(self, message):
        
        element, etat = message.split("/")
        
        # malgré qu'on peut tout simplement executer les deux fonctions (le changement de l'état et la confirmation de celui-ci)
        # on ne peut le faire ainsi car on doit valider que les valeurs sont correctes
        # ainsi que d'effectuer les changement aux bons éléments
        
        # système d'alarme
        if element == SYSTEME_ALARME.ELEMENT:
            if etat == SYSTEME_ALARME.ETAT_ON:
                self.carte.mettreON( SYSTEME_ALARME.BROCHE )
                self.temoin_alarme.configure( text = etat, background = COULEUR_ON )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )
                
            elif etat == SYSTEME_ALARME.ETAT_OFF:
                self.carte.mettreOFF( SYSTEME_ALARME.BROCHE )
                self.temoin_alarme.configure( text = etat, background = COULEUR_OFF )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )                

        # lumière de l'entrée   
        elif element == LUMIERE_ENTREE.ELEMENT:
            if etat == LUMIERE_ENTREE.ETAT_ON:
                self.carte.mettreON(LUMIERE_ENTREE.BROCHE)
                self.temoin_entree.configure( text = etat, background = COULEUR_ON )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )
                
            elif etat == LUMIERE_ENTREE.ETAT_OFF:
                self.carte.mettreOFF(LUMIERE_ENTREE.BROCHE)
                self.temoin_entree.configure( text = etat, background = COULEUR_OFF )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )
        
        # lumière du salon
        elif element == LUMIERE_SALON.ELEMENT:
            if etat == LUMIERE_SALON.ETAT_ON:
                self.carte.mettreON(LUMIERE_SALON.BROCHE)
                self.temoin_salon.configure( text = etat, background = COULEUR_ON )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )
                
            elif etat == LUMIERE_SALON.ETAT_OFF:
                self.carte.mettreOFF(LUMIERE_SALON.BROCHE)
                self.temoin_salon.configure( text = etat, background = COULEUR_OFF )
                self.messagerie.publieMessages( self.nom + "/" + element, element + "/" + etat )              
        
        
    def termine(self):
        if self.messagerie is not None:
            self.messagerie.termine()
        print("Terminé " + self.nom)
    
    
    def __del__(self):
        print("destructeur(): " + self.nom)  
    

# espace d'execution pour tests
def main():

    nom = PARTICIPANT2
    
    sujets = [ PARTICIPANT1 + "/" + SYSTEME_ALARME.ELEMENT, \
               PARTICIPANT1 + "/" + LUMIERE_ENTREE.ELEMENT, \
               PARTICIPANT1 + "/" + LUMIERE_SALON.ELEMENT ]  
    
    residence = SmartHub( nom, sujets )

    residence.roule()
    time.sleep(4)
   
    residence.termine()
    
    print( "Terminé 'main' du " + nom )




if __name__ == '__main__':
    main()
