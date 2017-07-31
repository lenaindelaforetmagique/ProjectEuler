##Problem 87
##
##The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
##
##28 = 22 + 23 + 24
##33 = 32 + 23 + 24
##49 = 52 + 23 + 24
##47 = 22 + 33 + 24
##
##How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?


from arithmetique import *


listePremiers = []

NBmax = 50*10**6

a = 2
while a < (NBmax - 2**2 - 2**4)**0.5:
    listePremiers.append(a)
    a = nextPrime(a)

L4 = [i**4 for i in listePremiers if i**4 < NBmax]
L3 = [i**3 for i in listePremiers if i**3 < NBmax]
L2 = [i**2 for i in listePremiers if i**2 < NBmax]
L4.append(NBmax) # astuce dégueulasse pour ne pas avoir out of range...
L3.append(NBmax)
L2.append(NBmax)


ens = set()
for a in L2:
    i = 0
    while a + L3[i] < NBmax:
        j = 0
        while a + L3[i] + L4[j] <=NBmax:
            ens.add(a + L3[i] + L4[j])
            j += 1
        i += 1

print(len(ens))

            

