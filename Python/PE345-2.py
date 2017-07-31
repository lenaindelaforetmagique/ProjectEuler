##Problem 345
##
##We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column. For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):
##
##  7  53 183 439 863
##497 383 563  79 973
##287  63 343 169 583
##627 343 773 959 943
##767 473 103 699 303
##
##Find the Matrix Sum of:
##
s = """  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""

s2 = """767 473 103 699 303
7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943"""

s2 = """17 15 9 5 12
16 16 10 5 10
12 15 14 11 5
4 8 14 17 13
13 9 8 12 17"""

from matrices import *
from random import randrange
from time import time

t0 = time()
M = s.split('\n')
M = [[int(c) for c in m.split(" ") if c !=''] for m in M]


# inversion du problème de maximisation : maximiser M == minimiser (vMax-M)
vMax = M[0][0]
for m in M:
    for v in m:
        vMax = max(vMax, v)
M = [[vMax - v for v in m] for m in M]

size = len(M)



def MelangeL(t):
    for i in range(len(t)-1,0,-1):
        i1=randrange(0,i+1)
        t[i1],t[i]=t[i],t[i1]

def step2(M1):
    # M2 : matrice des zéros :
    # 1 : présence d'un zéro
    # size : présence d'un zéro encadré
    # (size)**2 : présence d'un zéro barré
    M2 = [[int(v == 0) for v in m] for m in M1]
#    print("M2",M2)
    lignes = [i for i in range(size)]
    MelangeL(lignes)

    for i in lignes:
        listeZeros = [j for j, v in enumerate(M2[i]) if v == 1]
        if len(listeZeros)>0:
            j = listeZeros.pop(randrange(len(listeZeros)))
            M2[i][j] = size # encadrement du zero choisi
            #barrage des autres zéros (lignes et colonnes)
            for i2 in range(size):
                for j2 in range(size):
                    if (i2==i or j2 == j) and M2[i2][j2] == 1:
                        M2[i2][j2] = size**2
    return M2      

def step3(M2):
    listL = []
    listC = []
    # marquage des lignes sans zero encadré
    for i, l in enumerate(M2):
        if size not in l:
            listL.append(i)
#    print(listL)
    mod = 1
    while mod > 0:
        mod = 0
        # marquage des colonnes
        for i in listL:
            for j, v in enumerate(M2[i]):
                if v == size**2 and (j not in listC):
                    listC.append(j)
                    mod += 1
        # re-marquage des lignes
        M2 = transpose(M2)
        for j in listC:
            for i, v in enumerate(M2[j]):
                if v == size and (i not in listL):
                    listL.append(i)
                    mod += 1
        M2 = transpose(M2)
    
    return listL, listC

def step4(M1, listL, listC):
    listPartiel = [M1[i][j] for i in range(size) for j in range(size) if (i in listL)and(j not in listC)]
    if len(listPartiel)>0:
        minPartiel = min(listPartiel)
        M1 = [[M1[i][j]-int((i in listL)and(j not in listC))*minPartiel for j in range(size)] for i in range(size)]
        M1 = [[M1[i][j]+int((i not in listL)and(j in listC))*minPartiel for j in range(size)] for i in range(size)]
    
    return M1

# Recherche la somme minimum par l'algorithme de Kuhn (méthode Hongroise)
M1 = copy(M)
# Etape 1 : on soustrait à chaque ligne et chaque colonne son minimum
M1 = [[v - min(m) for v in m] for m in M1]
M1 = transpose([[v - min(m) for v in m] for m in transpose(M1)])


M2 = step2(M1)

def succes(M2):
    return sum([sum(m)%(size**2) for m in M2])//size == size


while not succes(M2):
    listL, listC = step3(M2)
    #step 4
    M1 = step4(M1, listL, listC)
    
    M2 = step2(M1)

# traitement de M2:
couples = []
for i in range(size):
    for j in range(size):
        if M2[i][j]==size:
            couples.append((i,j))

s = 0
for i,j in couples:
    s += M[i][j]
    
print(s) # resultat de la minimisation
print(vMax*size-s) # resultat de la maximisation
print(time()-t0)



    




    


    
    


 





      

