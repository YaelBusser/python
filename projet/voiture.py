class Voiture:
    identifiantVoiture = 0
    def __init__(self, nom, prix, marque, couleur, portes, places, manuelle, auto):
        self.idVoiture = type(self).identifiantVoiture #ou Voiture.identificationVoiture
        type(self).identifiantVoiture += 1
        self.nomVoiture = nom
        self.prixVoiture = prix
        self.marqueVoiture = marque
        self.couleurVoiture = couleur
        self.portesVoiture = portes
        self.placesVoiture = places
        self.manuelleVoiture = manuelle
        self.autoVoiture = auto
if __name__ == "__main__":

    Client1 = Voiture("Shelby GT 500 Eleanor 1967", 100000, "Ford Mustang", "Noir", 3, 2, True, False)
    Client2 = Voiture("Renault Twingo 3 GT", 1000, "Twingo", "Vert", 3, 4, True, False)
    Client3 = Voiture("Bugatti Veyron", 1000000, "Bugatti", "Noir", 3, 2, True, False)
    
    print(Client1.idVoiture)
    print(Client2.idVoiture)
    print(Client3.idVoiture)