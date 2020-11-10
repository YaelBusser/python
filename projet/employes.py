class Employes:
    def __init__(self, prenomEmploye, nomEmploye, ageEmploye, professionEmploye):
        self.prenom = prenomEmploye
        self.nom = nomEmploye
        self.age = ageEmploye
        self.profession = professionEmploye
employe1 = Employes("Yaël", "Busser", 36, "PDG")
employe2 = Employes("Simon", "Haumé", 40, "Directeur du Concessionnaire")
employe3 = Employes("Julien", "Chevallier", 26, "Cadre")
employe4 = Employes("Esteban", "Cottineau", 30, "Vendeur")
employe5 = Employes("Hugo", "Monchatre", 25, "Vendeur")
employe6 = Employes("Ethan", "Milon", 35, "Vendeur")
employe7 = Employes("Tania", "Gallet", 42, "Secrétaire")
employe8 = Employes("Florian", "Tessier", 28, "Comptable")
employe9 = Employes("David", "Froissard", 56, "Portier")
employe10 = Employes("Samuel", "Berthet", 49, "Technicien de surface")
if __name__ == "__main__":
    print()