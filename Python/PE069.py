##Problem 69
##
##Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
##n 	Relatively Prime 	φ(n) 	n/φ(n)
##2 	1 	1 	2
##3 	1,2 	2 	1.5
##4 	1,3 	2 	2
##5 	1,2,3,4 	4 	1.25
##6 	1,5 	2 	3
##7 	1,2,3,4,5,6 	6 	1.1666...
##8 	1,3,5,7 	4 	2
##9 	1,2,4,5,7,8 	6 	1.5
##10 	1,3,7,9 	4 	2.5
##
##It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
##
##Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


"""
Page wiki : φ(n) = n * prod( 1 - 1/pi ) avec pi = facteurs premiers de n
on a donc : n/φ(n) = prod( pi/(pi-1) )
Chaque terme du produit est le plus grand possible en prenant pi leplus petit possible.

Donc on cherche les facteurs premiers les plus petits qui multipliés entre eux donne un nombre <10*6
"""

from arithmetique import *
#from math import *



nbre = 1
p = nextPrime(nbre)
while nbre*p < 10**6:
    nbre *= p
    p = nextPrime(p)

print(nbre)

##
##
##NBmax = 10**4
##rapMax = 0
##nMax = 0
##for i in range(1,NBmax+1):
##    rap = i / phi(i)
##    #print(i, phi(i)) #rap)
##    if rap > rapMax:
##        rapMax = rap
##        nMax = i
##

#print(nMax,rapMax)
#print(nPremiers(100000)[-1])
