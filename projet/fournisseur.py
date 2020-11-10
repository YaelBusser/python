class Fournisseur:
    def __init__(self, pays, voitureFournisseur):
        self.adresse = pays
        self.voiture = voitureFournisseur
fournisseur = Fournisseur("Tous les pays", [
                ["Porsche", "911"], 
                ["Mercedes Benz", "Classe A Berline"],
                ["Maserati", "Levante"], 
                ["Ferrari", "488"], 
                ["Lamborghini", "Huracan"],
                ["Aston Martin", "DB11"], 
                ["Bentley", "Continental GT"], 
                ["Lotus Cars", "Exige"], 
                ["Rolls-Royce Motor Cars", "Dawn"],
                ["Bugatti", "Veyron"]
                ])
fournisseur1 = Fournisseur("Allemagne", [["Porsche", "911"], ["Mercedes Benz", "Classe A Berline"]])
fournisseur2 = Fournisseur("Italie", [["Maserati", "Levante"], ["Ferrari", "488"], ["Lamborghini", "Huracan"]])
fournisseur3 = Fournisseur("Royaume-Uni", [["Aston Martin", "DB11"], ["Bentley", "Continental GT"], ["Lotus Cars", "Exige"], ["Rolls-Royce Motor Cars", "Dawn"]])
fournisseur4 = Fournisseur("France", [["Bugatti", "Veyron"]])
if __name__ == "__main__":
    print()