##Problem 598
##
##Consider the number 48.
##There are five pairs of integers a
##and b (a≤b) such that a×b=48
##
##: (1,48), (2,24), (3,16), (4,12) and (6,8).
##It can be seen that both 6 and 8 have 4 divisors.
##So of those five pairs one consists of two integers with the same number of divisors.
##
##In general:
##Let C(n)
##be the number of pairs of positive integers a×b=n, (a≤b) such that a and b have the same number of divisors;
##so C(48)=1
##
##.
##
##You are given C(10!)=3
##
##: (1680, 2160), (1800, 2016) and (1890,1920).
##
##Find C(100!)

from arithmetique import *

t = []
for i in range(2, 100+1):
    t = t + primeFactors(i)

dico = {}
for v in t:
    if v not in dico:
        dico[v] = 0
    dico[v] += 1

facteurs = [v for v in dico.values()]
facteurs.sort(reverse = True)
facteurs = [v+2 for v in facteurs]

pos_prime = {}
i = 0
p = 0 
while nextPrime(p) <= facteurs[0]:
    p = nextPrime(p)
    pos_prime[p] = i
    i += 1

nbFac = len(facteurs)
nbPre = len(pos_prime)


def reduit():
#    print("reduit")
    cpt = 0
    while supprLC():
#        print(cpt)
        cpt += 1
    return cpt

def supprLC():
    global TOUT
    nbL, nbC = len(TOUT), len(TOUT[0])-2
    lignes = set()
    colonnes = set()
    for j in range(nbC):
        t = [TOUT[i][-2] for i in range(nbL) if TOUT[i][j] != 0]
        t_i = [i for i in range(nbL) if TOUT[i][j] != 0]
        if len(t) == 0:
            colonnes.add(j)
        else:
            if t.count(t[0]) == len(t):
                for l in t_i:
                    lignes.add(l)
                    
    if len(lignes) > 0 or len(colonnes) > 0:
        lignes = [i for i in range(nbL) if i not in lignes]
        lignes.sort()
        colonnes = [j for j in range(nbC+2) if j not in colonnes]
        colonnes.sort()
        TOUT = [[TOUT[i][j] for j in colonnes] for i in lignes]
        return True
    else:
        return False

def fusionne(table):
    """Assemble les lignes identiques"""
    nbL, nbC = len(table), len(table[0])-2
#    print("fus", nbL)
    S = {}
    for t in table:
        tu = tuple(t[:-1])
        if tu not in S:
            S[tu] = 0
        S[tu] += t[-1]
    table = []
    for tu in S:
        table.append(list(tu)+[S[tu]])

    #table.sort(key=lambda x:x[-2])
    return table
 
                


def additionne():
    """
    Prend les deux premiers identifiants et fait l'assemblage
    """
    global TOUT
    nbL, nbC = len(TOUT), len(TOUT[0])-2
    i1 = 0
    while i1 < nbL and TOUT[i1][-2] == TOUT[0][-2]:
        i1 += 1
    i2 = i1
    while i2 < nbL and TOUT[i2][-2] == TOUT[i1][-2]:
        i2 += 1
    tab1 = fusionne(TOUT[:i1])
    tab2 = fusionne(TOUT[i1:i2])
    reste = TOUT[i2:]
    resultat = []
    for t1 in tab1:
        for t2 in tab2:
            resultat.append([t1[j]+t2[j] for j in range(nbC+1)]+[t1[-1]*t2[-1]])

    TOUT = resultat + reste





TOUT = []
#facteurs = facteurs[:1]
for i, v in enumerate(facteurs):
    for j in range(1, v):
        t = [0 for _ in range(nbPre)] + [1*10**(nbFac-1-i)] + [1]
        dec1 = primeFactors(j)
        dec2 = primeFactors(v-j)
        for p in dec1:
            t[pos_prime[p]] += 1
        for p in dec2:
            t[pos_prime[p]] -= 1
        TOUT.append(t)

reduit()
while TOUT[0][-2] != 1111111111111111111111111:
    print(TOUT[0][-2])
    additionne()
    reduit()
    
print(TOUT)

print(max([t[-1] for t in TOUT]))

        
        
        
    
    






