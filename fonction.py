# 4-1
    # def nombre(n):
    #     result = n*5
    #     return result
    # print(nombre(5))
# 4-2
    # def NombrePaire(liste):
    #     for element in liste:
    #         if(element % 2 == 0):
    #             print(element)
    # NombrePaire([1,2,3,4,5])
# 4-3
    # def fibonacci(n):
    #     nb1 = 0
    #     nb2 = 1
    #     suivant = nb1 + nb2
    #     i = 0
    #     print(nb1)
    #     print(nb2)
    #     print(suivant)
    #     while(i < n):
    #         nb1 = nb2
    #         nb2 = suivant
    #         suivant = nb1 + nb2
    #         i += 1     
    #         print(suivant)
    # fibonacci(10)
    # def fib(max):
    #     a, b = 0, 1
    #     while a < max:
    #         print(a)
    #         a, b = b, a+b
    # fib(50)
 # 4-4
    # a = ""
    # def voy(a):
    #      i = 0
    #      voyelles = ("a", "e", "i", "o", "u", "y")
    #      for i in range(len(a)): 
    #          if a[i] in voyelles:
    #              print(a[i])
    # voy("ça va bien ?")

    # a = ""
    # def voy(a):
    #      i = 0
    #      voyelles = ("a", "e", "i", "o", "u", "y")
    #      while i < len(a):
    #         if a[i] in voyelles:
    #              print(a[i])
    #         i += 1
    # voy("ça va bien ?")
# 4-5
    # def fact(n):
    #     fact = 1
    #     while n >= 1 :  
    #         fact = fact * n
    #         n -= 1
    #     print(fact)
    # fact(5)
# 4-6

# 4-8
listeNombre = []

def premierNombre(listeNombre):
    i = 0
    for i in listeNombre:
       

premierNombre([1, 4, 9, 16, 25, 36, 49, 64, 100, 121])