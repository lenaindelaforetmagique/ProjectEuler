##Prime square remainders
##Problem 123
##
##Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)**n + (pn+1)**n is divided by pn**2.
##
##For example, when n = 3, p3 = 5, and 4**3 + 6**3 = 280 ≡ 5 mod 25.
##
##The least value of n for which the remainder first exceeds 10**9 is 7037.
##
##Find the least value of n for which the remainder first exceeds 10**10.


"""
On développe (pn-1)**n+(pn+1)**n
= sum(Pn**(n-k)*C(n,k)*2, k in range(0, n, step=2))
si n est pair, on trouve reste = 2
si n est impair, on trouve reste= Pn*n*2


"""

from time import time
from arithmetique import *
t0 = time()

n = 1
pn = 2

while n*pn*2<10**10:
    n += 2
    pn = nextPrime(nextPrime(pn))

print(n, pn)



print(time()-t0)



