##Problem 181
##
##Having three black objects B and one white object W they can be grouped in 7 ways like this:
##(BBBW)	(B,BBW)	(B,B,BW)	(B,B,B,W) 	(B,BB,W)	(BBB,W)	(BB,BW)
##
##In how many ways can sixty black objects B and forty white objects W be thus grouped?


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
    

B = 31
W = 1
resu = decomp(2**B)

print(len(resu))


"""
61*41=2501 groupes différents

resultats
B = 30 : 5604 (2802, 1401)
B = 31 : 6842 (3421
B = 40 : 37338
B = 50 : 204226
B = 60 : 966467

"""
