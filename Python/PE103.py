##PE103

from itertools import combinations
from time import time
t0 = time()



def verifComplete(L):
    """
    Vérifie que pour tous les sous-ensembles B, C disjoints que:
    S(B)!=S(C)
    card(B)>card(C) => S(B) > S(C)
    """
    #print(L)
    l = len(L)
    for i in range(2,l):
        for j in range(1, i+1):
            for c1 in combinations(range(l), i):
                #c1 : indices des valeurs choisies
                L1 = [L[i] for i in c1] #valeurs choisies
                L2 = [L[i] for i in range(l) if i not in c1]
                for c2 in combinations(L2,j):
                    #c2 : valeurs choisies
                    if i == j and sum(L1) == sum(c2):
                        #print('1', L1, c2)
                        return False
                    elif i != j and sum(L1) <= sum(c2):
                        #print('2', L1, c2)
                        #print(sum(L1), sum(c2))
                        return False              
    return True

def testOK(L):
    """
    Vérifie que les intervalles sont acceptables
    """
    if len(L)>=4:
        for (a,b) in combinations(L,2):
            l = abs(a-b)
            L2 = L[:]
            L2.remove(a)
            L2.remove(b)
            for (c,d) in combinations(L2, 2):
                if abs(c-d) == l:
                    return False

    return True

def recale(L):
    L2 = [v-L[0] for v in L]
        
    a = 1+max([sum(L2[-i:])-sum(L2[:i+1]) for i in range(1, len(L2)//2+1)])
    L2 = [v+a for v in L2]

    return L2
    

def devG(L):
    """
    Trouve la premiere position qui 'convient' à gauche
    La liste est supposée triée et la première valeur vaut 0
    """
    #print("G")
    g = L[0]-1
    L2 = recale([g]+L)
    cpt = 0
    while not verifComplete(L2) and cpt < 1000:
        cpt += 1
        L2[0] -= 1
        L2 = recale(L2)
    
    if cpt == 1000:
        print("nope G", L, L2)
    
    return L2

def devD(L):
    """
    Trouve la premiere position qui 'convient' à droite
    La liste est supposée triée
    """
    #print("D")
    d = L[-1]+1
    L2 = recale(L+[d])
    cpt = 0
    while not verifComplete(L2) and cpt < 1000:
        cpt += 1
        L2[-1] += 1
        L2 = recale(L2)
                
    if cpt == 1000:
        print("nope D", L, L2)
        
    return L2


def developpe(dico, prof):
    print(prof)
    Res = []
    for l in dico:
        g = devG(l)
        d = devD(l)
        if g not in Res:
            Res.append(g)
        if d not in Res:
            Res.append(d)
            
    if prof > 0:
        return developpe(Res,prof-1)
    else:
        return Res




D = developpe([[0,1,2]],3)
Smin = 10**9
tmin = []
print('------------')

for d in D:
    if verifComplete(d):
        print(d)
        if Smin > sum(d):
            Smin = sum(d)
            tmin = d

    

    
print(tmin, sum(tmin))
s = ""
for v in tmin:
    s += str(v)
print("Solution:", s)
print(time()-t0)
    


            











