##Problem 95
##
##The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
##
##Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
##
##Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
##
##12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
##
##Since this chain returns to its starting point, it is called an amicable chain.
##
##Find the smallest member of the longest amicable chain with no element exceeding one million.

from time import time
t0 = time()
dico = {}

def sumDiv(n):
    """Retourne la somme des diviseurs, 1 inclus, n exclus"""
    if n not in dico:
        l = [1]
        for i in range(2, int(n**0.5+1)):
            if n%i == 0:
                l.append(i)
                l.append(n//i)
        dico[n] = sum(l)
    return dico[n]

lMax = 0
vMin = 0
for i in range(10**6):
    l = []
    n = i
    while n < 10**6 and n not in l:
        l.append(n)
        n = sumDiv(n)
    if n == l[0] and len(l) > lMax:
#        print(l)
        lMax = len(l)
        vMin = min(l)
        print(i, lMax, vMin)



    
print(lMax, vMin)
print(time()-t0)
