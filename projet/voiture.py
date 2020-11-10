class Voiture:
    identifiantVoiture = 0
    def __init__(self, nom, prix, marque, couleur, portes, roues, places, manuelle, auto):
        self.idVoiture = type(self).identifiantVoiture #ou Voiture.identificationVoiture
        type(self).identifiantVoiture += 1
        self.nomVoiture = nom
        self.prixVoiture = prix
        self.marqueVoiture = marque
        self.couleurVoiture = couleur
        self.portesVoiture = portes
        self.rouesVoiture = roues
        self.placesVoiture = places
        self.manuelleVoiture = manuelle
        self.autoVoiture = auto
if __name__ == "__main__":

    Moi = Voiture("Shelby GT 500 Eleanor 1967", 100000, "Ford Mustang", "Noir", 3, 4, 2, True, False)
    Toi = Voiture("jcps", 100000, "Twingo", "Vert", 3, 4, 2, True, False)
    
    print(Moi.idVoiture)
    print(Toi.idVoiture)