# 5-1
# class Carre:
#     def __init__(self, cote):
#         self.cote = cote

# a = Carre(10)
# print(a.cote)

class Carre:
    def __init__(self, cote):
        self.unCote = cote
        self.perimetre = self.fctPerimetre() 
        self.aire = self.unCote * self.unCote
    def fctPerimetre(self):                  
        return self.unCote * 4                 

if __name__ == '__main__' :
    a = Carre(10)
    print(a.aire)
