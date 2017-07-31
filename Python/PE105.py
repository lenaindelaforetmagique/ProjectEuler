##PE105

from itertools import combinations
from time import time
t0 = time()





def verifComplete(L):
    """
    Vérifie que pour tous les sous-ensembles B, C disjoints que:
    S(B)!=S(C)
    card(B)>card(C) => S(B) > S(C)
    """
    for v in L:
        if L.count(v) > 1:
            print(L)
            return False
    #print(L)
    l = len(L)
    for i in range(1,l):
        for j in range(1, i+1):
            for c1 in combinations(range(l), i):
                #c1 : indices des valeurs choisies
                L1 = [L[i] for i in c1] #valeurs choisies
                L2 = [L[i] for i in range(l) if i not in c1]
                for c2 in combinations(L2,j):
                    #c2 : valeurs choisies
                    if i == j and sum(L1) == sum(c2):
                        return False
                    elif i != j and sum(L1) <= sum(c2):
                        return False              
    return True

fichier=open('PE105_sets.txt','r')
L=fichier.readlines()
fichier.close()

L = [[int(s) for s in l.split(',')] for l in L]

S = 0
for i,l in enumerate(L):
    #l.sort()
    
    if verifComplete(l):
        print(i)
        S += sum(l)




print("Solution:", S)
print(time()-t0)
    


            











