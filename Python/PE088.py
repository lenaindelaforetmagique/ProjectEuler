##Problem 88
##
##A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
##
##For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
##
##For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
##
##k=2: 4 = 2 × 2 = 2 + 2
##k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
##k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
##k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
##k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
##
##Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
##
##In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
##
##What is the sum of all the minimal product-sum numbers for 2≤k≤12000?


"""
on balaye toutes les façons de factoriser n (croissant jusqu'à ce qu'on ai trouvé
tous les k et on regarde si une des option donne un product-sum number

"""

from arithmetique import *
from time import time

t0 = time()


Results = set()      

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
    



kMax = 12000
table = [1]*(kMax+1)
somme = kMax-1


n = 4

while somme > 0:
    # travail sur n
    for t in decomp(n):
        s = sum(t)
        if s <= n:
            k = len(t) + n-s
            if 1 < k <= kMax and table[k] == 1:
                #print(k, n, t)
                table[k] = 0
                somme -= 1
                Results.add(n)
    n += 1

print("nmax", n-1)
print(sum(Results))
print(time() - t0)
