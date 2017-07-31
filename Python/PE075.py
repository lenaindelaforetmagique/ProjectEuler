##Problem 75
##
##It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
##
##12 cm: (3,4,5)
##24 cm: (6,8,10)
##30 cm: (5,12,13)
##36 cm: (9,12,15)
##40 cm: (8,15,17)
##48 cm: (12,16,20)
##
##In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
##
##120 cm: (30,40,50), (20,48,52), (24,45,51)
##
##Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

from math import gcd

Lmax = 1500000

def genereTriplet(u):
    """ genere la liste des triplets pythagoriciens primitifs
    x = u**2 - v**2
    y = 2*u*v
    z = u**2 + v**2
    avec u>v>0, gcd(u,v)=1 et u et v de parité différente
    """
    liste = []
    for v in range(u%2 + 1, min(u,int((Lmax-2*u**2)/(2*u)))+1,2):
        if gcd(u,v) == 1:
            x = u**2 - v**2
            y = 2*u*v
            z = u**2 + v**2
            liste.append((x,y,z))

    return liste

Dico = set()
DicoUnique = set()
for u in range(2,int((Lmax/2)**0.5)+1):
    L = genereTriplet(u)
    for triplet in L:
        k = 1
        length = sum(triplet)
        while k*length<=Lmax:
            if k*length in Dico:
                if k*length in DicoUnique:
                    DicoUnique.remove(k*length)
            else:
                Dico.add(k*length)
                DicoUnique.add(k*length)
            k += 1

print(len(DicoUnique))
