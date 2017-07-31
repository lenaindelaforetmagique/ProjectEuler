#PE151

from rationnels import *
from random import choice
from time import time
"""
A1 = 16
A2 = 8
A3 = 4
A4 = 2
A5 = 1

Dico[situation] = proba(situation)

situation = tuple de feuilles (nbA5,nbA4,nbA3,nbA2,nbA1)



On cherche : P = 1*P(1 fois) + 2*P(2 fois) + 3*P(3 fois)

évènement 8 : on tombe sur 1 A2 (ne peut arriver que s'il reste 8 tirages)
évènement 4 : on tombe sur 1 A3 (ne peut arriver que s'il reste 4 tirages)
évènement 2 : on tombe sur 1 A4 (ne peut arriver que s'il reste 2 tirages)

P(1 fois) = P(8&-4&-2) + P(4&-8&-2) + P(2&-8&-4) = ..
          = P(8) + P(4) + P(2) - 2*(P(8&4) + P(8&2) + P(4&2)) + 3*P(8&4&2)

P(2 fois) = P(8&4&-2) + P(8&-4&2) + P(-8&4&2) = ..
          = P(8&4) + P(8&2) + P(4&2) - 3*P(8&4&2)
          
P(3 fois) = P(8&4&2)

> P = P(8) + P(4) + P(2)


"""



def tour(dico):
    """Effectue un tour de pioche/remise de l'enveloppe
    Retourne la liste "suivante"
    """
    Res = {}  
    for l in dico.keys():
        NB = sum(l)
        for i, v in enumerate(l):
            if v > 0:
                t = list(l)
                t[i] -= 1
                for j in range(i):
                    t[j] += 1
                t = tuple(t)
                if t not in Res:
                    Res[t] = 0
                Res[t] += dico[l]*v/NB
    return Res
                

L = {}

L[(0,0,0,0,1)]=1
Liste = [L]
for _ in range(15):
    Liste.append(tour(Liste[-1]))
    
P = Liste[-2][(0,1,0,0,0)] + Liste[-4][(0,0,1,0,0)] + Liste[-8][(0,0,0,1,0)]
        
print("{:6f}".format(P))





##def tour(t):
##    pick = choice(t)
##    t.remove(pick)
##    while pick > 1:
##        pick //= 2
##        t.append(pick)
##    return t
##    
##
##def semaine():
##    evlp = tour([16])
##    cpt = 0
##    
##    for _ in range(14):
##        if len(evlp) == 1:
##            cpt += 1
##        evlp = tour(evlp)
##    return cpt
##
##
##def joue(temps):
##    S = 0
##    NB = 0
##    t0 = time()
##    while time()-t0<temps:
##        S += semaine()
##        NB += 1
##
##    S /= NB
##    print(time()-t0, NB, "{0:10.6f}".format(S))
##    
##
##temps = [5,10,20,60,120,240]
##
##for t in temps:
##    joue(t)


          
        
    
        
    
    

    
