import voiture
class Client: 
    def __init__(self, nom, prenom, idVoiture):
        self.nomClient = nom
        self.prenomClient = prenom
        self.idVoitureClient = idVoiture

if __name__ == "__main__":
    voiture1 = voiture.Voiture("Shelby GT 500 Eleanor 1967", 100000, "Ford Mustang", "Noir", 3, 2, True, False)
    client1 = Client("Busser", "Yaël", voiture1.idVoiture)

    voiture2 = voiture.Voiture("Bugatti Veyron", 1000000, "Bugatti", "Noir", 3, 2, True, False)
    client2 = Client("Nicola", "Civile", voiture2.idVoiture)
    
    print(client1.idVoitureClient)
    print(voiture1.idVoiture)
    print(client2.idVoitureClient)
    print(voiture2.idVoiture)