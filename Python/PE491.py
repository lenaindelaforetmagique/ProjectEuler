##Problem 491
##
##We call a positive integer double pandigital if it uses all the digits 0 to 9
##exactly twice (with no leading zero).
##For example, 40561817703823564929 is one such number.
##
##How many double pandigital numbers are divisible by 11?


"""
Divisible par 11 <=> somme des chiffres pairs - somme chiffres impairs = multiple de 11


set de chiffres = 00112233445566778899
10 parmi 20 = 184756 cas

p - i = 11*k
p + i = 90
p - 90 = -i
2p - 90 = 11*k
"""
from time import time
from itertools import combinations
t0 = time()

def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def C_n_k(n, k):
    return fact(n) // (fact(k)*fact(n-k))

#print(C_n_k(20,10))

t = [i//2 for i in range(20)]
dico = set()
for c in combinations(t,10):
    if (2*sum(c)-90)%11 == 0:
        dico.add(c)

S = 0
for c in dico:
    s = (10-c.count(0))*fact(9)*fact(10)
    for i in range(10):
        v = c.count(i)
        s //= fact(v)*fact(2-v)
    S += s

print(S)
print(time()-t0)
