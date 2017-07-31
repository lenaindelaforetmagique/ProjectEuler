"""Bibliothèque de calcul de Matrices
from matrices import *

contient :
dim(A) -- retourne un tuple des dimensions nbL, nbC
copy(A) -- retourne une copie (profonde) de A
initM(nbL, nbC) -- retourne une matrice nulle de nbL lignes, nbC colonnes
init1(n)-- retourne une matrice identité, carrée de taille n*n
prodM(A, B) -- retourne le produit des matrices A*B
trace(A) -- retourne la trace de la matrice carrée A
transpose(A) -- retourne la transposée de la matrice A
inverse(A) -- retourne l'inverse de A
echelonne(A) -- echelonne A

affiche(A) -- affiche A

"""

def affiche(A):
    print('')
    for l in A:
        print(l)
    print('')

def dim(A):
    return len(A), len(A[0])

def copy(A):
    return [[v for v in l] for l in A]
    

def initM(nbL, nbC):
    return [[0 for j in range(nbC)] for i in range(nbL)]

def init_id(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def prodM(A, B):
    lA, cA = dim(A)
    lB, cB = dim(B)

    if cA == lB:
        res = initM(lA, cB)
        for i in range(lA):
            for j in range(cB):
                s = 0
                for k in range(lB):
                    s += A[i][k]*B[k][j]
                res[i][j] = s
        return res
    else:
        print("-- prodM(A, B) : dimensions de matrices incompatibles")
        return False

def transpose(A):
    lA, cA = dim(A)
    res = initM(cA, lA)
    for i in range(cA):
        for j in range(lA):
            res[i][j] = A[j][i]
    return res

def trace(A):
    lA, cA = dim(A)
    if lA == cA:
        s = 0
        for i in range(lA):
            s += A[i][i]
        return s
    else:
        print("-- trace(A) : matrice non carrée")
        return False


def inverse(A):
    """ inversion de matrice, Pivot de Gauss"""
    lA, cA = dim(A)
    if lA == cA:
        copie = copy(A)
        res = init_id(lA)
        
        # boucle sur les colonnes
        for c in range(cA):
            #recherche de vmax
            iMax = c
            vMax = 0
            for i in range(c, lA):
                if abs(copie[i][c]) > abs(vMax):
                    iMax = i
                    vMax = copie[i][c]
            
            #switch de lignes
            copie[c], copie[iMax] = copie[iMax], copie[c]
            res[c], res[iMax] = res[iMax], res[c]

            #création du 1 pour la colonne en cours
            copie[c] = [copie[c][j]/vMax for j in range(cA)]
            res[c] = [res[c][j]/vMax for j in range(cA)]
            
            #zéros dans la colonne
            for i in range(lA):
                if i != c:
                    res[i] = [res[i][j]-res[c][j]*copie[i][c] for j in range(cA)]
                    copie[i] = [copie[i][j]-copie[c][j]*copie[i][c] for j in range(cA)]                          

        return res
    else:
        print("-- inverse(A) : matrice non carrée")
        return False


def echelonne(A):
    """ échelonne la matrice, Pivot de Gauss"""
    ech = copy(A)
    lA, cA = dim(ech)
    lc = 0
    # boucle sur les colonnes
    for c in range(cA):
##        print(c, lc, '--\n')
##        affiche(ech)
        #recherche de vmax
        iMax = lc
        vMax = 0
        for i in range(lc, lA):
            if abs(ech[i][c]) > abs(vMax):
                iMax = i
                vMax = ech[i][c]

        if abs(vMax) > 10**(-15):
            #switch de lignes
            ech[lc], ech[iMax] = ech[iMax], ech[lc]

            #création du 1 pour la colonne en cours
            ech[lc] = [ech[lc][j]/vMax for j in range(cA)]

            #zéros dans la colonne
            for i in range(lA):
                if i != lc:
                    ech[i] = [ech[i][j]-ech[lc][j]*ech[i][c] for j in range(cA)]
            lc += 1

    return ech

    
if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[1,2,3]]
    B = [[0,1,0],[2,0,1],[0,1,1]]
    
    
    affiche(A)
    print('--')
    affiche(echelonne(A))
#    A[0], A[1] = A[1], A[0]
    #B = inverse(A)
    #print(">>",B)
    #print(prodM(A,B))
    #print(B)
    
    #print(prodM(A,B))
    #print(prodM(B,A))
    #print(trace(A))
    #print(transpose(A))
    
    

