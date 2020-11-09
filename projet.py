class Voiture:
    def __init__(self, marque, couleur):
        self.laMarque = marque
        self.laCouleur =  couleur
if __name__ == "__main__":
    laMarque = input("Quelle est la marque ? ")
    laCouleur = input("Quelle est la couleur ? ")
    tabMarque = ("Peugeot", "Renault", "Opel", "Citroën", "Volkswagen", "Mercedes", "BMW", "Fiat", "Audi", "Ford", "Nissan", "Toyota")
    tabCouleur = ("Jaune","Orange","Blanc","Noire","Rouge","Rose","Violet","Vert","Marron","Bleu", "Gris")
    if laMarque in tabMarque and laCouleur in tabCouleur:
        print("ok")
