##Problem 84
from random import randrange
from time import time

nbFaces = 4

# Plateau
Plateau = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', \
           'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',\
           'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',  \
           'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

Platinv = {} # plateau inversé
for i, case in enumerate(Plateau):
    Platinv[case] = i

def carteCommunaute(pos):
    """retourne la position après tirage de la carte communauté"""
    numCarte = randrange(16)
    if numCarte == 1:
        return Platinv['GO']
    elif numCarte == 2:
        return Platinv['JAIL']
    else:
        return pos

def carteChance(pos):
    """retourne la position après tirage de la carte chance"""
    numCarte = randrange(16)
    if numCarte == 1:
        return Platinv['GO']
    elif numCarte == 2:
        return Platinv['JAIL']
    elif numCarte == 3:
        return Platinv['C1']
    elif numCarte == 4:
        return Platinv['E3']
    elif numCarte == 5:
        return Platinv['H2']
    elif numCarte == 6:
        return Platinv['R1']
    elif numCarte == 7:
        return nextR(pos)
    elif numCarte == 8:
        return nextR(pos)
    elif numCarte == 9:
        return nextU(pos)
    elif numCarte == 10:
        return pos-3
    else:
        return pos # inchangé

def nextR(pos):
    """retourne la prochaine case R*"""
    i = 1
    while 'R' not in Plateau[(pos + i)%40]:
        i += 1
    return (pos + i)%40

def nextU(pos):
    """retourne la prochaine case U*"""
    i = 1
    while 'U' not in Plateau[(pos + i)%40]:
        i += 1
    return (pos + i)%40

def tourDeJeu(numLancer, pos):
    """ Retourne la position après la fin d'un tour de joueur"""
    # lance les des
    de1 = randrange(nbFaces) + 1
    de2 = randrange(nbFaces) + 1
    double = (de1 == de2)
    score = de1 + de2

    if numLancer == 2 and double:
        # va en prison
        OK = False
    else:
        case = (pos + score)%40
        OK = True

    # action
    if OK:
        if 'CH' in Plateau[case]:
            case = carteChance(case)
            if case == Platinv['JAIL']:
                double = False

        if 'CC' in Plateau[case]:
            case = carteCommunaute(case)
            if case == Platinv['JAIL']:
                double = False

        if 'G2J' in Plateau[case]:
            double = False
            case = Platinv['JAIL']

        # éventuellement rejoue
        if double:
            return case, numLancer+1
        else:
            return case, 0
    else:
        return Platinv['JAIL'], 0




t0 = time()


NBRE = 1000000

resu = [0 for _ in range(40)]
case = 0
tour = 0
for _ in range(NBRE):
    case, tour = tourDeJeu(tour,case)
    resu[case] += 1

resu = [[100*v/NBRE, i] for i, v in enumerate(resu)]
resu.sort()
resu = resu[::-1][:6]

for res in resu:
    print(res)

print(time()-t0)
