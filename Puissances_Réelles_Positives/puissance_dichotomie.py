"""
recherche de puissance par dichotomie et recurssion
chaque puissance est composée d'une partie entière et d'un partie 
non entière. 
on peut exrpimer x^k = x^(int)k * x^(k - int(k))

puis chercher pour quel y, f(y) = y ^ 1/(k - int(k)) = x
cette recherche peut se faire par dichotomie. 

mais avant ça, il faut réussir a calculer y ^ 1/(k - int(k))
et cela peut se décomposer aussi en partie entière et aprtie non entière
y ^ 1/(k - int(k)) = y ^ (int) 1/(k - int(k)) * y ^ (1/(k - int(k)) - (int) 1/(k - int(k)))

donc il suffit d'abord de calculer suffisement loins les puissances non entières et 
remonter par dichotomie jusqu'a la partie non entière de k
"""


import matplotlib.pyplot as plt
import math 

i = 0

def power_int(x, n):
    total = 1
    for i in range(1, n + 1):
        total *= x
    return total

def dichotomie(x, exp, recursion):
    #on recherche pour quelle valeur de y 
    #y ^ exp = x
    #l'exposant est toujours un entier >= 1
    #ce qui implique y <= x 
    #on cherche alors entre 0 et x
    
    min_val = 0
    max_val = max(x, 1)
    while True:
        mid = (max_val + min_val) / 2
        f = power_float(mid, exp, recursion)
        if abs(x - f) < 0.000000001 : 
            return mid
        if f > x : 
            max_val = mid
        elif f < x : 
            min_val = mid
            
        
def power_float(x, k, recursion = 5):
    n = int(k)
    l = k - n
    
    if l < 0.0001:
        return power_int(x, n)
    if recursion <= 0 :
        return power_int(x, n)
    else :
        global i
        i += 1
        return power_int(x, n) * dichotomie(x, 1/l, recursion - 1)



for k in range(10):
    print(k/10000)
    i = 0
    print(power_float(2, k/10000, 3))
    print(2 ** (k/10000))
    print(i)
    print("")
    
"""
calcul explicité pour k = 0.8 et x = 2
2^k = 2^0 * 2^0.8

on calcul y tq y^1/0.8 = x
y^1/0.8 = y^1.25 = y^1 * y^0.25

on calcul z tq z^1/0.25 = y
z^1/0.25 = z^4
fin de la récursion -> on a calculé les exposants les plus profonds 

maintenant, on peut expliciter la dichotomie 
calcul de y 
midy = (x + 0) / 2
on calcul midy^1.25

calcul de z 
midz = midy/2^4
"""



    
    





        
