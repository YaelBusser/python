class Fournisseur:
    tabVoiture = [
        ["Porsche", 
            "Porsche 911"], 
        ["Mercedes Benz", 
            "Classe A Berline"], 
        ["Lotus Cars", 
            "Lotus Exige"], 
        ["Maserati"], 
        ["Aston Martin"], 
        ["Bentley"], 
        ["Bugatti"], 
        ["Ferrari"], 
        ["Lamborghini"], 
        ["Rolls-Royce Motor Cars"]]
    def __init__(self, lieu, voitureFournisseur):
        self.adresse = lieu
        self.voiture = voitureFournisseur

if __name__ == "__main__":
    fournisseur1 = Fournisseur("San Francisco", [["Porsche", "Porsche 911"], ["Mercedes Benz", "Classe A Berline"]])
    fournisseur2 = Fournisseur("", [["", ""], ["", ""]])
    fournisseur3 = Fournisseur("", [["", ""], ["", ""]])
    fournisseur4 = Fournisseur("", [["", ""], ["", ""]])
    fournisseur5 = Fournisseur("", [["", ""], ["", ""]])
    print(fournisseur1.voiture)