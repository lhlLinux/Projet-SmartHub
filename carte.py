"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - carte.py -
# Renferme la classe Carte, qui est en faite le GPIO
#
###########################################################################
"""

from RPiSim import GPIO
from globales import *
import time


class Carte():
     
    def __init__(self):
        """ Constructeur GPIO """

        # initialisation préliminaire
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
       
        # lumières et alarme
        GPIO.setup( SYSTEME_ALARME.BROCHE, GPIO.MODE_OUT, initial = GPIO.LOW )
        GPIO.setup( LUMIERE_SALON.BROCHE , GPIO.MODE_OUT, initial = GPIO.LOW )
        GPIO.setup( LUMIERE_ENTREE.BROCHE, GPIO.MODE_OUT, initial = GPIO.LOW )
    
        
    def mettreON( self, broche ):
        GPIO.output(broche, GPIO.HIGH)
    
    
    def mettreOFF( self, broche ):
        GPIO.output(broche, GPIO.LOW)
    
    
    def __del__(self):
        print( "destructeur(): GPIO" )
        GPIO.cleanup()
        
        
# espace d'execution pour tests
def main():
    carte = Carte()
    carte.mettreON( SYSTEME_ALARME.BROCHE )
    time.sleep(4)
    print("programe terminé")

if __name__ == '__main__':
    main()
