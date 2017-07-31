##Problem 131
##
##There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.
##
##For example, when p = 19, 8**3 + 8**2×19 = 12**3.
##
##What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.
##
##How many primes below one million have this remarkable property?


"""
c**3 = n**2*(n+p)

on écrit c = a**2*b

c**3= n**2      * (n+p)
    = 1         * (a**6*b**3)  > p = c**3-1 premier ssi c=2
    = b**2      * (a**6*b)     > p = b*(a**6-1) > b=1 et a**2=2 > Impossible
    = a**2      * (a**4*b**3)  > p = a*(a**3*b**3-1) > a=1 et b=2 > déjà compté
    = a**2*b**2 * (a**4*b)     > p = a*b*(a**3-1) > a=1, b=1 (donc p=0) > Impossible
    = a**4      * (a**2*b**3)  > p = a**2*(b**3-1) > a=1, b=2 > déjà compté
    = a**4*b**2 * (a**2*b)     > p = 0
    = a**6      * (b**3)       > p = (b-a)*(b**2+a*b+a**2) > b-a=1 (voir plus bas)
    = a**6*b**2 * (b)          > p = b*(1-a**3) > a=0

p = (b-a)*(b**2+a*b+a**2) premier ssi (b-a)=1
p = (b**2+a*b+a**2)
p = (b**2+b**2-b+b**2-2*b+1)
p = 3*b**2 - 3*b + 1

"""


from arithmetique import *

def verif(b):
    a = b - 1
    c = a**2*b
    p = 3*b**2-3*b+1
    n = a**3
    print("a", a)
    print("b", b)
    print("c", c)
    print("n", n)
    print("p", p)
    print(">", c**3, n**2*(n+p))


pMax = 10**6

b = 0

p = lambda x:3*x**2-3*x+1

cpt = 0
while p(b)<pMax:
    if isPrime(p(b)):
        cpt += 1
    b += 1

print(cpt)


