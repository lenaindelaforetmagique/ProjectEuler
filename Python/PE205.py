##Problem 205
##
##Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
##Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
##
##Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
##
##What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

from time import time
t0 = time()

def tablePoss(nbF, nbD):
    """Retourne la table des façons d'optenir un score de nbD dés à nbF faces
    les dés sont tous numérotés de 1 à nbF"""
    t = [0]*(nbD*nbF+1)
    for i in range(0, nbF**nbD):
        s = nbD
        while i != 0:
            s += i%nbF
            i //= nbF
        t[s] += 1               
    return t

# Probabilités de chaque tirage pour Peter (P) et Colin (C)
P = tablePoss(4, 9)
P = [p/(4**9) for p in P]
C = tablePoss(6, 6)
C = [c/(6**6) for c in C]

# Probabilité de victoire de Peter sur Colin
Res = 0
for i, pc in enumerate(C):
    Res += pc*sum(P[i+1:])

print('{:.7f}, {:.3f}s'.format(Res,time()-t0))


