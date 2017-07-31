## PE 174
"""
N = 4*

"""

from arithmetique import *
from time import time

t0 = time()

def diviseurs(lFact, pFact):
    """
    Itérateur de facteurs A*B = produit_sur_i(lFact[i]**pFact[i])
    > retourne  A<=dmax
    """
    
    if len(lFact) == 0:
        yield 1
    else:
        for p in range(pFact[-1]+1):
            for v in diviseurs(lFact[:-1], pFact[:-1]):
                yield (lFact[-1]**p)*v

def listeDiviseurs(N):
    pFac = primeFactors(N)
    listFact = []
    puisFact = []
    while len(pFac)>0:
        v = pFac[0]
        listFact += [v]
        puisFact += [pFac.count(v)]
        pFac = [val for val in pFac if val!=v]

    t = sorted([f for f in diviseurs(listFact,puisFact)],reverse=True)
    t.remove(1)
    return t


Dico_decomp = {}
def decomp(N):
    """ fournit la liste des décompositions de N"""
    global Dico_decomp
    if N not in Dico_decomp:
        res = set()
        if N != 1:
            tDiv = listeDiviseurs(N)
            for div in tDiv:
                ens = decomp(N//div)
                if len(ens) > 0:
                    for dec in ens:
                        res.add(tuple(sorted([div] + list(dec))))
                else:
                    res.add((div,))
        Dico_decomp[N] = res

    return Dico_decomp[N]





def nbDiviseurs(N):
    pFac = primeFactors(N)
    listFact = []
    puisFact = []
    while len(pFac)>0:
        v = pFac[0]
        listFact += [v]
        puisFact += [pFac.count(v)]
        pFac = [val for val in pFac if val!=v]

    r = 1
    for v in puisFact:
        r *= v+1
    
    
    return r

def listAnagrammes(l):
    """retourne la liste des anagrammes d'une liste"""
    rep = []
    if len(l) == 1:
        rep.append(l)
    else:
        for i in range(len(l)):
            sousAnag = listAnagrammes(l[:i]+l[i+1:])
            for anag in sousAnag:
                v = [l[i]]+anag
                if v not in rep:
                    rep.append(v)
    return rep


def nextPerm(l):
    """retourne la premutation suivante de l [p0,p2,p3]

Améliorer la permutation suivante : si val dépassée, on passe à la suivante
potentiellement plus petite
    """
    # recherche de la case à incrémenter
    if len(l) == 1:
        return [l[0]+1]
    else:        
        i = 0
        while i<len(l) - 1 and l[i+1]-l[i] == 1:
            i += 1

        return [j for j in range(i)] + [l[i]+1] + l[i+1:]


def gdNextPerm(l):
    """ retourne la premiere permutation suivante potentiellement "plus petite"
    """
    pos = 0
    while pos < len(l)-1 and pos == l[pos]:
        pos += 1

    l[pos] = pos
    return incrementePos(l, pos+1)

def incrementePos(l, pos):
    if pos == len(l)-1:
        l[pos] += 1
        return l
    elif l[pos]+1 < l[pos+1]:
        l[pos] += 1
        return l
    else:
        l[pos] = pos
        return incrementePos(l, pos+1)

def testPerm(l):
    test = True
    for i in range(len(l)-1):
        test = test and (i==l[i])
    return test


"""
nb div - decomp - exposants possibles
20 2*2*5 > 1,1,4 / 3,4 / 1,9 / 19
18 2*3*3 > 1,2,2 / 5,2 / 1,8 / 17
16 2*2*2*2 > 1,1,1,1 / 3,1,1 / 3,3 / 15
14 2*7 > 1,6 / 13
12 2*2*3 > 1,1,2 / 3,2 / 1,5 / 11
10 2*5 > 1,4 / 9
8 2*2*2 > 1,1,1 / 3,1 / 7
6 2*3 > 1,2 / 5
4 2*2 > 1,1 / 3
2 2 > 1 (nombres premiers)
"""


"""
un nombre à n décompositions possibles a 2*n diviseurs

on cherche à construire le snombres qui ont 2*n diviseurs

2*n diviseurs = somme des exposants des primeFactors +1

pour chaque n, on cherche les décompositions de 2*n > on obtient une liste d'exposants possibles (+1)
pour chaque décomposition, on balaie les anagrammes (des exposants)
pour chaque anagramme d'exposant, on balaie les facteurs premiers possibles (perm)


"""





def valeur(primes, perm, expo):
    r = 1
    for i in range(len(perm)):
        if perm[i] == len(primes):
            print(perm, expo)
        r *= primes[perm[i]]**(expo[i]-1)
    return r


longMax = (10**6) //4

premiers = []
for i in range(2, longMax+100):
    if isPrime(i):
        premiers.append(i)

premiers.sort()
print(len(premiers))
cpt = 0

res = [0]*30
for n in range(2,22):
    print("--",n)
    for dec in decomp(n):
        print(dec)
        leng = len(dec)
        for anag in listAnagrammes(list(dec)):
#            print(anag)
            perm = [i for i in range(leng)]

            test = True
            while test:
                val = valeur(premiers, perm, anag)
                if val <= longMax:
                    res[n//2] += 1
                    perm = nextPerm(perm)
                elif not testPerm(perm):
                    perm = gdNextPerm(perm)
                else:
                    test = False
#            print("echec", val, primeFactors(val))
            
            



print(res)
print(sum(res))
print(time()-t0)



    
    


