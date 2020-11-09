class Client: 
    def __init__(self, nom, prenom, voiture):
        self.nomClient = nom
        self.prenomClient = prenom
        self.voitureClient = voiture
class Voiture:
    def __init__(self, nom, prix, marque, couleur, portes, roues, places, manuelle, auto):
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
    voitureClient = Voiture("Shelby GT 500 Eleanor 1967", 100000, "Ford Mustang", "Noir", 3, 4, 2, True, False)
    print(voitureClient.prixVoiture)