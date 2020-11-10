import fournisseur
class Concessionnaire:
    def __init__(self, lieu, nbEmployes, nbVoiture, voitureDispo):
        self.adresse = lieu
        self.nombreEmployes = nbEmployes
        self.nombreVoiture = nbVoiture
        self.voitureDisponible = voitureDispo
concessionnaire = Concessionnaire("France", 10, 30, fournisseur.fournisseur.voiture)
if __name__ == "__main__":
    concessionnaire = Concessionnaire("France", 15, 30, fournisseur.fournisseur.voiture)
    print(concessionnaire.voitureDisponible)