##PE185 - Number Mind

from random import *
from itertools import *
from time import *
t0 = time()

S = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct
"""

S2 = """90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct
"""

S = S.split(' correct\n')
S = [s.split(' ;') for s in S if s != '']
S = [[s[0], int(s[1])] for s in S]

TAILLE = len(S[0][0])
#print(TAILLE)

indices = []
for i, s in enumerate(S):
    indices.append([int(c) for c in s[0]]+[s[1]])

solution = [-1] * TAILLE

def copieI(indices):
    """ renvoie une copie profonde d'indices"""
    return [t.copy() for t in indices]

def verif(indices):
    """ vérifie la cohérence entre nbre de cases dispo et indice"""
    global TAILLE
    for i, l in enumerate(indices):
        if (TAILLE - l.count(-1) < l[-1]) or l[-1] < 0:
            return False
    return True
    

def complet(solution):
    return solution.count(-1) == 0

sauvIndices = copieI(indices)

def correct(solution):
    global sauvIndices, TAILLE
    for l in sauvIndices:
        cpt = 0
        for j in range(TAILLE):
            if solution[j] == l[j]:
                cpt += 1
        if cpt != l[-1]:
            return False

    return True
            

def afficheSolution(solution):
    s = ''.join([str(v) if v != -1 else '_' for v in solution])
    print(s)    



"""
solveur logique(indices, solution) : réduit au mieux
    1) ligne "nulle" > supprime toutes les possibilités
    2) numero absent d'une colonne
    3) une seule possibilité > modifie la table d'indices

solveurBacktracking(indices, solution)

"""


def solveurLogique(indices, solution):
    """retourne true si des modifs on été apportées"""
    global TAILLE
    changement = False
    # 1 - lignes d'indices nulles
    suppr = [i for i,l in enumerate(indices) if l[-1] == 0]
    if len(suppr) > 0:
        changement = True
        for j in range(TAILLE):
            c = [indices[i][j] for i in suppr]
            for l in indices:
                if l[j] in c:
                    l[j] = -1
        suppr=suppr[::-1]
        for i in suppr:
            indices.pop(i)

    # 2 - lignes résolues
    for i, l in enumerate(indices):
        if (TAILLE - l.count(-1) == l[-1]):
            changement = True
            for j in range(TAILLE):
                if l[j] != -1:
                    solution[j] = l[j]
            l[-1] = 0
    suppr = [i for i,l in enumerate(indices) if l[-1] == 0]
    suppr=suppr[::-1]
    for i in suppr:
        indices.pop(i)

    # 3 - harmonisation solution/indices
    for i, l in enumerate(indices):
        for j in range(TAILLE):
            if solution[j] != -1:
                if l[j] == solution[j]:
                    changement = True
                    l[-1] -= 1
                l[j] = -1

    return changement


def mainSolveur(indices, solution):
    global TAILLE
    test = True
    while test:
        test = solveurLogique(indices, solution)

    if verif(indices) and not complet(solution) and len(indices)>0:
#        afficheSolution(solution)
        i = 0
        
        jlist = [j for j, v in enumerate(indices[i]) if v != -1 and j !=TAILLE]

        for positions in combinations(jlist, indices[i][-1]):
            cS, cI = solution[:], copieI(indices)
            cI[i] = [indices[i][j] if j in positions else -1 for j in range(TAILLE)]+[indices[i][-1]]
            cI.append([indices[i][j] if j not in positions else -1 for j in range(TAILLE)]+[0])
            
            if mainSolveur(cI, cS):
#                afficheSolution(solution)
                indices[i] = [indices[i][j] if j in positions else -1 for j in range(TAILLE)]+[indices[i][-1]]
                indices.append([indices[i][j] if j not in positions else -1 for j in range(TAILLE)]+[0])
                return mainSolveur(indices, solution)

        return False

    elif correct(solution):
        return True
    else:   # cas de retour faux
#        prof -= 1
        return False

print(mainSolveur(indices, solution))

print('--')
#print(solution)
afficheSolution(solution)
if not complet(solution):
    for j in range(TAILLE):
        if solution[j] == -1:
            sol2 = set([j for j in range(10)])
            for i, l in enumerate(sauvIndices):
                if l[j] in sol2:
                    sol2.remove(l[j])
            if len(sol2) == 1:
                solution[j] = min(sol2)

afficheSolution(solution)
                
print(time()-t0)
