##Problem 108

from time import time
from arithmetique import *
t0 = time()

def nbre(n):
    return (nbDiv(n**2)+1)//2

def cherche(n,p):
    global nmax
    if n < nmax:
        if nbre(n)<1000:
            cherche(n*p, p)
            p = nextPrime(p)
            cherche(n*p, p)
        else:
            nmax = n

nmax = 2
p = 2
while nbre(nmax)<1000:
    p = nextPrime(p)
    nmax *= p

print(nmax, nbre(nmax))
cherche(2, 2)
print(nmax, nbre(nmax))
print(time()-t0)




