##Problem 110

from time import time
from arithmetique import *
t0 = time()

def nbre(n):
    return (nbDiv(n**2)+1)//2


nmax = 10**100

def cherche(n, nbd, p, exp):
    #print(n, nbd, p, exp)
    global nmax, cpt
    if n*(p**exp) < nmax:
        if (nbd*(exp*2+1)+1)//2<4*(10**6):
            cherche(n*(p**exp), nbd*(exp*2+1), nextPrime(p), 1)
            cherche(n, nbd, p, exp+1)
        else:
            nmax = n*(p**exp)
            #print(nmax)

cherche(1, 1, 2, 1)
print(nmax, nbre(nmax))
print(primeFactors(nmax))
print(time()-t0)




