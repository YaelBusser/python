import voiture
import employes
import concessionnaire
class Client: 
    def __init__(self, prenomClient, nomClient):
        self.prenom = prenomClient
        self.nom = nomClient

if __name__ == "__main__":
    client = Client(input("Quel est votre prénom ? "), input("Quel est votre nom de famille ? "))
    vendeur = input("Quel vendeur voulez-vous avoir pour vous aider à choisir votre voiture de luxe ? ("
    + str(employes.employe4.prenom) +", "+ str(employes.employe5.prenom) +" ou "+ str(employes.employe6.prenom) +") ")
    if vendeur == str(employes.employe4.prenom):
        print("Bonjour "+ client.prenom +", je m'appelle "+ str(employes.employe4.prenom) +", je serais votre conseiller pour vous permettre de choisir la voiture de vos rêves !")
        marque = input("Pour commencer quelle marque de voiture vous ferais plaisir ? ")

    elif vendeur == str(employes.employe5.prenom):
        print("Bonjour "+ client.prenom +", je m'appelle "+ str(employes.employe5.prenom) +", je serais votre conseiller pour vous permettre de choisir la voiture de vos rêves !")
        marque = input("Pour commencer quelle marque de voiture vous ferais plaisir ? ")

    elif vendeur == str(employes.employe6.prenom):
        print("Bonjour "+ client.prenom +", je m'appelle "+ str(employes.employe6.prenom) +", je serais votre conseiller pour vous permettre de choisir la voiture de vos rêves !")
        marque = input("Pour commencer quelle marque de voiture vous ferais plaisir ? ")
    tabOk = []
    for i in range(len(concessionnaire.concessionnaire.voitureDisponible)):
        if marque in concessionnaire.concessionnaire.voitureDisponible[i]:
            tabOk.append("ok")
        else:
            tabOk.append("faux")
    if "ok" in tabOk:    
        print("Nous avons en effet des "+ str(marque) +" disponibles. ")
        print("Nous avons ces modèles-ci : ")
        for k in range(len(concessionnaire.concessionnaire.voitureDisponible)):
            if(concessionnaire.concessionnaire.voitureDisponible[k][0] == marque):
                print(concessionnaire.concessionnaire.voitureDisponible[k][1]) 
                print(voiture.voiture.prixVoiture)

    else:
        print("Désolé nous n'avons pas de modèles "+ str(marque) +" mais nous avons ceux-ci si vous voulez : ")
        for j in range(len(concessionnaire.concessionnaire.voitureDisponible)):
            print(concessionnaire.concessionnaire.voitureDisponible[j][0])
        marque = input("Quelle marque de voiture avez-vous choisi ? ")
        for l in range(len(concessionnaire.concessionnaire.voitureDisponible)):
            if marque in concessionnaire.concessionnaire.voitureDisponible[l]:
                tabOk.append("ok")
            else:
                tabOk.append("faux")
        if "ok" in tabOk:    
            print("Nous avons en effet des "+ str(marque) +" disponibles. ")
            print("Nous avons ces modèles-ci : ")
            for k in range(len(concessionnaire.concessionnaire.voitureDisponible)):
                if(concessionnaire.concessionnaire.voitureDisponible[k][0] == marque):
                    print(concessionnaire.concessionnaire.voitureDisponible[k][1]) 
