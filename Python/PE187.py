##Problem 187
##
##A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
##
##There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
##
##How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?

from arithmetique import *
from time import time
t0 = time()

Nmax = 10**8
premiers = Eratosthene(Nmax//2)
print(len(premiers))

i = 0
pMax = int(Nmax**0.5)
j = len(premiers)-1
S = 0
while premiers[i] <= pMax:
    while premiers[j] > Nmax//premiers[i]:
        j -= 1
    S += j+1-i
    i += 1

print(S)
print(time()-t0)




    
    


