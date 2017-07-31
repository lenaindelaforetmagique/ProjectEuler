##Problem 359
##
##An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room at Hilbert's newest infinite hotel. The hotel contains an infinite number of floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of rooms (numbered 1, 2, 3, etc.).
##
##Initially the hotel is empty. Hilbert declares a rule on how the nth person is assigned a room: person n gets the first vacant room in the lowest numbered floor satisfying either of the following:
##
##    the floor is empty
##    the floor is not empty, and if the latest person taking a room in that floor is person m, then m + n is a perfect square
##
##Person 1 gets room 1 in floor 1 since floor 1 is empty.
##Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect square.
##Person 2 instead gets room 1 in floor 2 since floor 2 is empty.
##Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.
##
##Eventually, every person in the line gets a room in the hotel.
##
##Define P(f, r) to be n if person n occupies room r in floor f, and 0 if no person occupies the room. Here are a few examples:
##P(1, 1) = 1
##P(1, 2) = 3
##P(2, 1) = 2
##P(10, 20) = 440
##P(25, 75) = 4863
##P(99, 100) = 19454
##
##Find the sum of all P(f, r) for all positive f and r such that f × r = 71328803586048 and give the last 8 digits as your answer.

from arithmetique import *

NB = 71328803586048
pFac = primeFactors(NB)
#print(pFac)
listFact = []
puisFact = []
while len(pFac)>0:
    v = pFac[0]
    listFact += [v]
    puisFact += [pFac.count(v)]
    pFac = [val for val in pFac if val!=v]

#print(pFac)
#print(listFact)
#print(puisFact)

def iterateur(lFact, pFact):
    """
    Itérateur de facteurs A*B = produit_sur_i(lFact[i]**pFact[i])
    > retourne A
    """
    if len(lFact) == 0:
        yield 1
    else:
        for p in range(pFact[-1]+1):
            for v in iterateur(lFact[:-1], pFact[:-1]):
                yield (lFact[-1]**p)*v


##def remplissage(nmax):
##    t = []
##    for n in range(1, nmax+1):
##        i = 0
##        while (i < len(t)) and (int((t[i][-1]+n)**0.5))**2 != (t[i][-1]+n):
##            i += 1
##
##        if i == len(t):
##            t.append([n])
##        else:
##            t[i] += [n]
##    return t
##
##Hotel = remplissage(100)

    
def P(f, r):
    if f == 1:
        r1 = r
    else:
        r1 = r + 2*(f//2) -1
    return ((1+r1)*r1)//2 + (f//2)*(-1)**(r1+f+1)
    
    

cpt = 0
S = 0
for A in iterateur(listFact, puisFact):
    S += P(A, NB//A)
    cpt += 1

print(cpt)
print(S%(10**8))
        
