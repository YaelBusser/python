# 5-1
# class Carre:
#     def __init__(self, cote):
#         self.cote = cote

# a = Carre(10)
# print(a.cote)

# class Carre:
#     def __init__(self, cote):
#         self.unCote = cote
#         self.perimetre = self.fctPerimetre() 
#         self.aire = self.unCote * self.unCote
#     def fctPerimetre(self):                  
#         return self.unCote * 4            

# if __name__ == '__main__' :
#     a = Carre(10)
#     print("Le carré à un côté d'une longueur de " + str(a.unCote) + ", une aire de " + str(a.aire) + " et un périmètre de " + str(a.perimetre) + ".")
class Carre:
    def __init__(self, cote1, cote2):
        self.unCote1 = cote1
        self.unCote2 = cote2
        self.perimetre1 = self.fctPerimetre1() 
        self.perimetre2 = self.fctPerimetre2() 
        self.aire1 = self.unCote1 * self.unCote1
        self.aire2 = self.unCote2 * self.unCote2
    def fctPerimetre1(self):                  
        return self.unCote1 * 4         
    def fctPerimetre2(self):                  
        return self.unCote2 * 4   
if __name__ == '__main__' :
    a = Carre(10, 5)
    print("Carré 1 : \n Longueur = " + str(a.unCote1) + ", Aire = " + str(a.aire1) + ", Perimètre = " + str(a.perimetre1) + ".")
    print("Carré 2 : \n Longueur = " + str(a.unCote2) + ", Aire = " + str(a.aire2) + ", Perimètre = " + str(a.perimetre2) + ".")
