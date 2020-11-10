import concessionnaire
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
nom = []
marque = []
for i in range(len(concessionnaire.concessionnaire.voitureDisponible)):
    nom.append(concessionnaire.concessionnaire.voitureDisponible[i][1])
    marque.append(concessionnaire.concessionnaire.voitureDisponible[i][0])
voiture1 = Voiture(nom[0], 500000, marque[0], "jaune", 3, 2, True, False)
voiture2 = Voiture(nom[1], 250000, marque[1], "rouge", 3, 2, True, False)
voiture3 = Voiture(nom[2], 150000, marque[2], "orange", 3, 2, True, False)
voiture4 = Voiture(nom[3], 600000, marque[3], "violet", 3, 2, True, False)
voiture5 = Voiture(nom[4], 750000, marque[4], "vert", 3, 2, True, False)
voiture6 = Voiture(nom[5], 1000000, marque[5], "blanc", 3, 2, True, False)
voiture7 = Voiture(nom[6], 1250000, marque[6], "noir", 3, 2, True, False)
voiture8 = Voiture(nom[7], 1500000, marque[7], "rouge", 3, 2, True, False)
voiture9 = Voiture(nom[8], 2000000, marque[8], "bleu", 3, 2, True, False)
voiture10 = Voiture(nom[9], 2500000, marque[9], "noir", 3, 2, True, False)
if __name__ == "__main__":
    voiture1 = Voiture("Shelby GT 500 Eleanor 1967", 100000, "Ford Mustang", "Noir", 3, 2, True, False)
    voiture2 = Voiture("Renault Twingo 3 GT", 1000, "Twingo", "Vert", 3, 4, True, False)
    voiture3 = Voiture("Bugatti Veyron", 1000000, "Bugatti", "Noir", 3, 2, True, False)
    
    print(voiture1.idVoiture)
    print(voiture2.idVoiture)
    print(voiture3.idVoiture)