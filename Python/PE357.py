##Problem 357
##
##Consider the divisors of 30: 1,2,3,5,6,10,15,30.
##It can be seen that for every divisor d of 30, d+30/d is prime.
##
##Find the sum of all positive integers n not exceeding 100 000 000
##such that for every divisor d of n, d+n/d is prime.

"""
si n est impair : n est diviseur on alors d+n/d = n+n/n=n+1 est pair donc non premier sauf 1
=> n pair ou 1

si n est multiple de 4 : 1 2 .. 2*p n avec 2*p pair. on a alors : 2+2*p qui est pair
=> n=2*[2*k+1 for k in range(25 000 000)]

plus généralement :
si n multiple de k**2 : 1 .. k .. k*p .. n, k+k*p=k*(p+1) n'est pas premier !
=> pas de multiplicité de facteurs premiers

on doit avoir 1+n   premier donc n est forcément suivi d'un nombre premier
              2+n/2 premier

1 : 1 1 -> 2 premier
2 : 1 2 -> 3 premier
--- fin des cas particuliers
3 : 1 3 -> 4 non premier

6   : 1 2 3 6 -> 7 5 premiers
10  : 1 2 5 10 -> 11 7 premiers
22  : 1 2 11 22 -> 23 13 premiers
30  : 1 2 3 5 6 10 15 30
42  : 1 2 3 6 7 14 21 42

-14 : 1 2 7 14 -> 15 9 non premiers
-26 : 1 2 13 26 -> 27 15 non premiers
-34 : 1 2 17 34 -> 35 non premier
-36 : 1 2 3 4 6 9 12 18 36 ->2+18 non premier


Let p and p+2 be twin primes. If 2p+1 is also prime, 2p is in this sequence.

"""

from time import time


__isPrime__ = {} # dictionnaire de resultats

def isPrime(n):
    if n not in __isPrime__:
        i = 3
        test = True
        while i <= n ** 0.5 and test:
            if n % i == 0:
                test = False
            i+=2
        __isPrime__[n] = test
    return __isPrime__[n]

def prodL(liste):
    """Retourne le produit des items de la liste"""
    p = 1
    for l in liste:
        p *= l
    return p


def test(n):
    i = 1
    val = True
    while i <= n**0.5 and val:
        if n%i == 0:
            if not isPrime(n//i+i):
                val = False
        i += 1
    return val


maxi = 10**8 # 41991562 #(10**8)
# 41991562 > 20139 368588645389
# 10**8 > 39627 1739023853137 4011.9059040546417
# 10**7 > 6625 27814470277 384.1659860610962
# 10**6 > 1289 524402305 15.189295053482056
# 10**5 > 277 9157937 0.6611289978027344
# 10**4 > 80 262615 0.03291893005371094

##cpt = 2
##s = 1 + 2
##m = 6
##i = 0
##while m <= maxi:
##    if test(m):
##        #print(m,primeFactors(m))
##        #print(">",i**2+i+41)
##        s += m
##        cpt += 1
##        i += 1
##    m += 4
##print(cpt, s,time()-t0)


premiers = [2, 3, 5, 7]
base = prodL(premiers)**2
liste = [True]*base

# Filtre 1 : on ne garde que les nombres pairs
for i in range(base):
    if i%2 != 0:
        liste[i] = False
        
# Filtre 2 : on supprime tous les carrés
for i in range(base):
    for p in premiers:
        if i%(p**2) == 0:
            liste[i] = False

# Compilation de la liste
restes = [i for i in range(base) if liste[i]]
print(premiers, len(restes)/base)

t0 = time()
cpt = 1
s = 1
for reste in restes:
    m = reste
    while m <= maxi:
        if test(m):
            s += m
            cpt += 1
            i += 1
        m += base

print(cpt, s,time()-t0)

    


