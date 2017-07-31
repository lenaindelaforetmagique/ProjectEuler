##Largest integer divisible by two primes
##Problem 347
##
##The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if such a positive integer does not exist.
##
##E.g. M(2,3,100)=96.
##M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
##Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.
##
##Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.
##
##Find S(10 000 000).

from math import *
from arithmetique import *
from time import time

t0 = time()

def M(p, q, N):
    """    p**a*q=N
    p**a = N//q
    a*ln(p) = ln(N//q)
    p**aMax*q**bMax"""
    vMax = 0
    amax = int(log(N/q)/log(p))

    if amax != 0:
        for i in range(1, amax+1):
            bmax = int(log(N/(p**i))/log(q))
            v = p**i*q**bmax
            if v > vMax:
                vMax = v
    return vMax




def S(N):
    p = 2
    res = 0

    while p < N**0.5:
        q = nextPrime(p)
        while p*q<=N:
            res += M(p, q, N)
            q = nextPrime(q)
        p = nextPrime(p)

    return res


    
print(M(2,3,100))
print(S(10000000),time()-t0)
#11109800204052 273.48202896118164

    

