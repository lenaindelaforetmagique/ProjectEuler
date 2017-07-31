##Problem 243
##
##A positive fraction whose numerator is less than its denominator is called a proper fraction.
##For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
##1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .
##
##We shall call a fraction that cannot be cancelled down a resilient fraction.
##Furthermore we shall define the resilience of a denominator, R(d), to be the
##ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
##In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .
##
##Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

from arithmetique import *
from time import time
t0 = time()

def R(d):
    return phi(d)/(d-1)
"""
phi(n)=n*prod(1-1/facteurs_premiers)

on cherche n tel que
n*prod(pi-1)*94744 < 15499 *(n-1) * prod(pi)

"""

def combinaison(k,L):
    """itérateur renvoyant les k-combinaisons de L"""
    if k==0:
        yield []
    else:
        for i in L:
            L2=[j for j in L if j!=i and j>i]
            for comb in combinaison(k-1,L2):
                yield [i]+comb



def prod(l):
    r = 1
    for v in l:
        r*=v
    return r



limit = 15499/94744
print("limite = ", limit)

n = 2
pi = 2
Rn = 1
premiers = [pi]

while Rn >= limit:
    pi = nextPrime(pi)
    premiers.append(pi)
    Rn *= (n-1)*(pi-1)/(n*pi-1)
    n *= pi 

print(len(premiers), n, Rn, primeFactors(n))
sol_A = n


def ameliore(n):
    global limit
    print(n)
    t = primeFactors(n)
    t.sort()
    n2 = n // t[-1]
    pro = []
    for i in range(len(t)-1):
        p = t[i]
        while p<t[-1] and R(n2*p)>=limit:
            p *= t[i]
        pro.append(p)
    return n2*min(pro+[t[-1]])

n = ameliore(n)
n = ameliore(n)


print(n, primeFactors(n))

        
    

    
