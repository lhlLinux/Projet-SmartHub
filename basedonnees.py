"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - basedonnees.py -
# Base de données des messages, renferme la classe BaseDonnees
# qui abstrait la connection avec la bdd MongoDB, offrant des méthodes 
# d'ajout et de lecture de messages.
#
###########################################################################
"""

import pymongo
import datetime


class BaseDonnees():
    
    
    def __init__( self, nom ):
        
        self.nom = nom

        # ouverture de la connexion avec le serveur MongoDB        
        try:
            self.client = pymongo.MongoClient("localhost")
            # on établit la bdd et la collection
            self.db = self.client.projet1
            self.collection = self.db.messages  
            print( "Connexion MongoDB: " + self.nom)
        except:
            print( "ATTENTION BaseDonnees: Connexion Mongo n'a pas eu lieu" )
            return
        
        
    def ajouterMessage( self, evennement ):
        
        # on obtient la date et heure et on scinde la chaîne pour garder seuelement ces derniers
        date_et_heure = str( datetime.datetime.now() )
        date, heure = date_et_heure.split()
        heure, temp = heure.split(".") # temp n'est pas utilisé, mais nécessaire pour éviter une erreur
        
        # le document est préparé ensuite inséré
        document = { "date"  : date,
                     "heure" : heure,
                     "evennement" : evennement }
        
        try:
            self.collection.insert_one( document )
        except:
            print( "ERREUR BaseDonnees: L'ajout de messages n'a pas pu être effectué" )
        
    
    def lireMessages(self, limite):
        # on retourne une liste de documents (messages)
        try:
            return list( self.collection.find().sort( "_id", pymongo.DESCENDING).limit( limite ) )
        except:
            print( "ERREUR BaseDonnees: La lecture de messages n'a pas pu être effectué" )

    
    def termine(self):
        if self.client is not None:
            self.client.close()
            print( "Déconnexion: MongoDB " + self.nom )
            
            
    def __del__(self):
        print("destructeur(): " + self.nom)