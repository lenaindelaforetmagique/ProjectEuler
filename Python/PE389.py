##Problem 389
##
##An unbiased single 4-sided die is thrown and its value, T, is noted.
##T unbiased 6-sided dice are thrown and their scores are added together. The sum, C, is noted.
##C unbiased 8-sided dice are thrown and their scores are added together. The sum, O, is noted.
##O unbiased 12-sided dice are thrown and their scores are added together. The sum, D, is noted.
##D unbiased 20-sided dice are thrown and their scores are added together. The sum, I, is noted.
##Find the variance of I, and give your answer rounded to 4 decimal places.
"""
4*6 > 24
24*8 > 192
192*12 >

.. > 4*6*8*12*20 = 46080

"""

from random import randrange

def tour(lN):
    """ effectue un tour avec la liste de dés """
    a = 1
    for n in lN:
        b = 0
        for _ in range(a):
            b += randrange(n)+1
        a = b
    return b
        

t = []
somme = 0
sommeC = 0
nb = 0
Vold = 0
V = 100
listeDes = [2,2] #[4, 6, 8, 12, 20]
while abs(V-Vold)>10**(-4):

    for j in range(10000):
        i = tour(listeDes)
        nb += 1
        somme += i
        sommeC += i**2
    
    Vold, V = V, sommeC/nb - (somme/nb)**2
    print(V)

print(nb, V)


def V_nFaces(n):
    """ Retourne la variance d'un dé à n faces"""
    return (n+1)*(2*n+1)/6 - E_nFaces(n)**2
    

def E_nFaces(n):
    """ Retourne l'esperance d'un dé à n faces"""
    return (n+1)/2


def E_prod(listeE):
    """ retourne la variance d'un produit de variables aléatoires indépendantes"""
    if len(listeE)==1:
        return listeE[0]
    else:
        return E_prod(listeE[:-1])*listeE[-1]


def V_prod(listeV, listeE):
    """ Retourne la variance d'un produit de variables aléatoires:
    mode recursif : dernier element de la liste fois la variance du reste de la liste"""
    if len(listeV)==len(listeE)==1:
        return listeV[0]
    else:
        resteV = listeV[:-1]
        resteE = listeE[:-1]
        t1 = listeV[-1]*V_prod(resteV, resteE)
        t2 = listeV[-1]*(E_prod(resteE))**2
        t3 = V_prod(resteV, resteE)*(listeE[-1])**2
        return t1 + t2 + t3

lN = [2, 2] #, 8, 10, 12, 20]
lV = [V_nFaces(n) for n in lN]
lE = [E_nFaces(n) for n in lN]



print(V_prod(lV, lE))


print(lE)
print(lV)





    










