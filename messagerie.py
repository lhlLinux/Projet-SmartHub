"""
###########################################################################
#                                Projet 1
# Étudiant: Linus Levi
# Cours: 420-315-AH (Développement d’objets intelligents)
# Date: 04/07/2022
#
# Fichier: - messagerie.py -
# Renferme la classe Messagerie, qui abstrait la connection avec MQTT
# et offre des méthodes
# de réception et envoi de messages
#
###########################################################################
"""

import paho.mqtt.client as mqtt
from globales import *


def on_connect(client, userdata, flags, rc):
    print( "Connexion MQTT (code "+ str(rc) + "): " + userdata.nom + "\n" )

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")


def on_message(client, userdata, message):
    contenu = str(message.payload.decode("utf-8"))
    print( userdata.nom + " reçoit: ", contenu )
    userdata.traiteMessages( contenu )



class Messagerie():

    def __init__( self, parent, nom, sujets: list ):

        self.nom = nom
        self.sujets = sujets  # liste de sujets à écouter

        # on obtient une interface à mosquitto
        try:
            self.client = mqtt.Client( nom )
        except:
            print( "ERREUR " + self.nom + " : " + "le client MQTT n'a pu être produit" )
            return

        # on établit quelques paramètres
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.user_data_set( parent )

        # on tente de se connecter au serveur
        try:
            self.client.connect( MQTT_BROKER )
        except:
            print( "ERREUR " + self.nom + " : " + "connexion à MQTT n'a pu se faire" )
            return

        # on se souscrit aux sujets à écouter
        for sujet in self.sujets:
            self.client.subscribe( sujet )

        self.client.loop_start()
        print( "Attente des messages MQTT: " + self.nom )


    def souscrireMessage(self, sujet):
        self.client.subscribe( sujet )


    def publieMessages(self, sujet, valeur):
        self.client.publish( sujet, valeur )
        print( "Publié au sujet " + sujet, " : valeur: ", valeur )


    def termine(self):
        if self.client is not None:
            self.client.loop_stop()
            # on se desinscrit des sujets et on se déconnecte
            for sujet in self.sujets:
                self.client.unsubscribe(sujet)
            self.client.disconnect()
            print("Déconnexion: MQTT " + self.nom)


    def __del__(self):
        print("destructeur(): MQTT " + self.nom)


# objet pour tests ci-bas
class Obj():

    def __init__(self, nom):
        self.nom = nom

    def traiteMessages(self):
        print("je traite les messages")



def main():

    obj = Obj("Objet")
    messagerie = Messagerie( obj, "Test", ["Bonjour"] )
    messagerie.publieMessages( "bonjour", 5 )
    messagerie.termine()
    print( "programme terminé" )


if __name__ == '__main__':
    main()