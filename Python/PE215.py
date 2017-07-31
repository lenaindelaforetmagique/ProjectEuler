##PE215

from itertools import combinations
from time import time
t0 = time()


def arrToInt(t):
    pos = -2
    nb = 0
    for v in t[:-1]:
        pos += v
        nb += 2**pos
    return nb

L = 32
H = 10

# distributions possibles de 2 et de 3
distr = []
t = L%2
while t*3 <= L:
    distr.append(((L-t*3)//2, t))
    t += 2
#> distr = [(1,10), (4,8), (7,6), (10,4), (13,2), (16,0)]


# génération des anagrammes
Dico = {} #[{},{},{},{}]
for d, t in distr:
    l = t+d
    for c in combinations(range(l),t):
        #c contient les positions d'insertions des 3
        #arr = [3 if i in c else 2 for i in range(l)]
        arr = [2+int(i in c) for i in range(l)]
        if sum(arr) != L:
            print(t, d, c, arr)
        cle = arrToInt(arr)
        #print(arr, bin(cle))
        Dico[cle] = set()
        

print("NB combi", len(Dico)) #3329 OK
        
# croisement des anagrammes
S = 0
Res0 = {}
for cle0 in Dico.keys():
    for cle1 in Dico.keys():
        if cle0&cle1 == 0:
            Dico[cle0].add(cle1)
    Res0[cle0] = len(Dico[cle0])
    S += len(Dico[cle0])
print("NB moyen de voisins", S/len(Dico))

# Calcul des empilements itératif:
for _ in range(H-2):
    Res1 = {}
    for cle0 in Dico.keys():
        Res1[cle0] = 0
        for cle1 in Dico[cle0]:
            Res1[cle0] += Res0[cle1]
    Res0 = Res1

S = sum(Res0.values())
print("NB Solutions:", S)
print(time()-t0)
    


            











