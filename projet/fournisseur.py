class Fournisseur:
    def __init__(self, lieu, voitureFournisseur):
        self.adresse = lieu
        self.voiture = voitureFournisseur

if __name__ == "__main__":
    fournisseur1 = Fournisseur("Etats-Unis", [["Porsche", "Porsche 911"], ["Mercedes Benz", "Classe A Berline"]])
    fournisseur2 = Fournisseur("Italie", [["Maserati", ""], ["Ferrari", ""], ["Lamborghini", ""]])
    fournisseur3 = Fournisseur("Royaume-Uni", [["Aston Martin", ""], ["Bentley", ""], ["Lotus Cars", "Lotus Exige"], ["Rolls-Royce Motor Cars", ""]])
    fournisseur4 = Fournisseur("France", [["Bugatti", ""]])
    print(fournisseur4.voiture)