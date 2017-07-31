## PE 510

"""
quasi brute-force:
xAC**2 = 4*ra*rc
xCB**2 = 4*rb*rc
xAB**2 = 4*ra*rb

tangence ssi xAC+xCB=xAB

on arrive à montrer que c'est équivalent à ce que:
ra = d*a**2
rb = d*b**2
rc = d*c**2

on cherche donc a*c + b*c = a*b

> première boucle : repère les triplets "générateurs" (brute force, hélas)
> deuxième partie : l'addition.

"""

from time import time
from math import gcd


t0 = time()
MAX = 10**9
bmax = int(MAX**(1/2))

dico = set()
for b in range(1, bmax+1):
    for a in range(1, b+1):
        if a*b%(a+b)==0:
            c = (a*b)//(a+b)
            if gcd(a,gcd(b,c)) == 1:
                dico.add((a,b,c))


print(len(dico))

S = 0
for jeu in dico:
    kMax = MAX // (jeu[1]**2)
    S += (jeu[0]**2 + jeu[1]**2 + jeu[2]**2)*(1 + kMax)*kMax//2

print(S, time()-t0)
        


