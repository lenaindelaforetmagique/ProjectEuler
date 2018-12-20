##Problem 549
##
##The smallest number m such that 10 divides m! is m=5.
##The smallest number m such that 25 divides m! is m=10.
##
##Let s(n) be the smallest number m such that n divides m!.
##So s(10)=5 and s(25)=10.
##Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
##S(100)=2012.
##
##Find S(10**8).

from arithmetique import *
from math import *


def pFact(n):
    t = primeFactors(n)
    dico = {v : t.count(v) for v in set(t)}
    return dico
##    for v in t:
##        if v not in dico:
##            dico[v] = 0
##        dico[v] += 1


def s(n):
    prems = pFact(n)
    print(prems)
    t = []
    for k in prems.keys():
        t.append(k**prems[k])
    return max(t)


print(s(25))

