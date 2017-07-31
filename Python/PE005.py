##Problem 5
##
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i+=1
    return True

def nextPrime(n):
    i = n + 1
    while not isPrime(i):
        i+=1
    return i

def primeFactors(n):
    l = []
    i = 2
    a = n
    while a != 1 and i <= a:
        if a % i == 0:
            l.append(i)
            a /= i
        else:
            i = nextPrime(i)
    return l


L=[]
for i in range(1,21):
    P=primeFactors(i)
    print(i,P)
    for p in P:
        while P.count(p)>L.count(p):
            L.append(p)


def prodL(liste):
    p = 1
    for i in liste:
        p *= i
    return p

print(L, prodL(L))



