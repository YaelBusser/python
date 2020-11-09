class dame:
    def __init__(self):
        self.creation = self.creationJeuDame()

    def creationJeuDame(self):
        tab = []
        tabBlanc = {}
        tabNoir = {}
        nbBlanc = 1
        nbNoir = 61
        for i in range(0, 10):
            for j in range(0, 10):
                tab.append([i, j])
        for k in range(0, 20):      
            tabBlanc[k] = tab[k + nbBlanc]
            if tabBlanc[k][0] % 2 == 0:
                nbBlanc += 1
            else:
                tabBlanc[k] = tab[k + nbBlanc -1]
                nbBlanc += 1
        for l in range(0, 20):
            tabNoir[l] = tab[l + nbNoir]
            if tabNoir[l][0] % 2 == 0:
                nbNoir += 1
            else:
                tabNoir[l] = tab[l + nbNoir -1]
                nbNoir += 1
        ligne = int(input("Choisissez une ligne : "))
        colonne = int(input("Choisissez une colonne : "))
        coordonnees = []
        coordonnees.append(ligne)
        coordonnees.append(colonne)
        if coordonnees in tabBlanc:
            ok = "Le pion choisit est bien disponible "
        else:
            ok = "Le pion n'existe pas à cet emplacement"
        return print(ok)
if __name__ == "__main__":
    a = dame()
    print(a)
