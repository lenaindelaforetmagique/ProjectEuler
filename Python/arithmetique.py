# Bibliothèque de fonction d'arithmétique

from math import gcd

"""
from arithmetique import *
"""


__isPrime__ = {} # dictionnaire de resultats



def Eratosthene(Nmax):
    """ Fournit la liste des nombres premiers inférieurs à Nmax"""
    L = [0]*2 + [1]*(Nmax-1)

    i = 0
    imax = int(Nmax**0.5)
    while i <= imax:
        if L[i] == 1:
            for j in range(2, Nmax//i+1):
                L[i*j] = 0
        i += 1
    
    premiers = [i for i,v in enumerate(L) if v == 1]
    return premiers


def isPrime(n):
    if n not in __isPrime__:
        if n <= 1:
            __isPrime__[n] = False
        else:
            i = 2
            test = True
            while i <= n ** 0.5 and test:
                if n % i == 0:
                    test = False
                i+=1
            __isPrime__[n] = test

    return __isPrime__[n]



def nextPrime(n):
    i = n + 1
    while not isPrime(i):
        i+=1
    return i

def previousPrime(n):
    i = n - 1
    while not isPrime(i):
        i-=1
    return i


memPF = {}
memPF[1] = []
def primeFactors(n):
    """Décomposition en facteurs premiers"""
    global memPF
    if n not in memPF:
        i = 2
        while n%i != 0 and i <= n:
            i = nextPrime(i)

        memPF[n] = [i] + primeFactors(n//i)
        
    return memPF[n]

def ppcm_L(liste):
    """PPCM d'une liste de nombres"""
    L = []
    for i in liste:
        factors = primeFactors(i)
        for p in factors:
            while factors.count(p)>L.count(p):
                L.append(p)
    p = 1
    for l in L:
        p *= l
    return p
#print(ppcm_L([i for i in range(1,21)]))

def nb_div(n):
    """Nombre de diviseurs d'un nombre"""
    s = 0
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            s += 2
        i += 1
    return s

def phi(n):
    """phi function:
determine the number of numbers less than n which are relatively prime to n"""
    if isPrime(n):
        return n-1
    else:
        l = primeFactors(n)
        # suppr doublons
        L = []
        for p in l:
            if p not in L:
                L.append(p)
        resu = n
        for p in L:
            resu *= (p - 1)
            resu //= p

        return resu

def mobius(n):
    """Retourne la fonction de mobius de n
    0 si n est divisible par un carré parfait différent de 1 ;
    1 si n est le produit d'un nombre pair de nombres premiers distincts ;
    –1 si n est le produit d'un nombre impair de nombres premiers distincts.
    """
    if n == 1:
        return 1
    else:
        t = primeFactors(n)
        t2 = [t.count(c) for c in t]
    #    print(t,t2)
        if max(t2) != 1:
            return 0
        elif len(t)%2 == 0:
            return 1
        else:
            return -1
    


def nPremiers(n):
    """retourne les n premiers nombres premiers"""
    liste = []
    nbre = 0
    a = 1
    while nbre<n:
        a = nextPrime(a)
        liste.append(a)
        nbre += 1
    return liste


def nbDiv(n):
    listFac = primeFactors(n)
    D = {}
    for v in listFac:
        if v not in D:
            D[v] = 0
        D[v] += 1
    p = 1
    for v in D.values():
        p *= (v+1)
    return p




 
