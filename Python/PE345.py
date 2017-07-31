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

from matrices import *
from random import randrange

def switchM(M, l1, l2):
    M[l1], M[l2] = M[l2], M[l1]

def MelangeRapide(t):
    for i in range(len(t)-1,0,-1):
        i1=randrange(0,i+1)
        t[i1],t[i]=t[i],t[i1]
#    return t
    
M = s.split('\n')
M = [[int(c) for c in m.split(" ") if c !=''] for m in M]

def fact(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

nbL, _ = dim(M)
trMax = trace(M)
print(trMax)

cpt = 0
cpt2 = 0
while cpt<nbL*100:  
    MelangeRapide(M)
    trInt = trace(M)
    # teste tous les switchs possibles (14+1)*14/2=105
    for i in range(nbL-1):
##        for j in range(i+1,nbL):
##            cpt2 += 1
##            switchM(M,i,j)
##            tr = trace(M)
##            if tr > trInt:
##                trInt = tr
##            else:
##                # retour à la normale
##                switchM(M,i,j)
##                
        for j in range(nbL):
            if i != j:
                cpt2 += 1
                switchM(M,i,j)
                tr = trace(M)
                if tr > trInt:
                    trInt = tr
                else:
                    # retour à la normale
                    switchM(M,i,j)


    if trInt > trMax:
        print(cpt, trInt)
        cpt3 = 1
    if trInt == trMax:
        #print(trInt)
        cpt3 += 1 
    trMax = max(trMax, trInt)
    cpt += 1


print("-->",trMax, cpt, cpt2)
print(cpt2/fact(15))
print(cpt3/cpt)
                






      

