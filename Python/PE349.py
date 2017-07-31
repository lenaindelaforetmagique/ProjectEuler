##Problem 349
##
##An ant moves on a regular grid of squares that are coloured either black or white.
##The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square to adjacent square according to the following rules:
##- if it is on a black square, it flips the color of the square to white, rotates 90 degrees counterclockwise and moves forward one square.
##- if it is on a white square, it flips the color of the square to black, rotates 90 degrees clockwise and moves forward one square.
##
##Starting with a grid that is entirely white, how many squares are black after 10**18 moves of the ant?


lgMax = 105


Liste = [0]*lgMax

pos = (0, 0)

direction = 0
vecteurs = [(0,1), (-1,0), (0,-1), (1,0)]

casesNoires = set()

cpt = 0
cle = 1
cpt2 = 0
while cle not in Liste or cpt2 < 2*lgMax:
    if cle in Liste:
        #print(cle)
        cpt2 += 1
        #print(cpt, cpt2)
    #print(cle)
    Liste[cpt%lgMax]= cle
        
    if pos in casesNoires:
        direction = (direction+1)%4
        casesNoires.remove(pos)
        c = 1
    else:
        direction = (direction-1)%4
        casesNoires.add(pos)
        c = 0
    pos = (pos[0]+vecteurs[direction][0], pos[1]+vecteurs[direction][1])
    cle = (cle*10+(direction+1)*2+c)%(10**(lgMax))
    cpt +=1


lgCycle = (cpt-Liste.index(cle))%lgMax
nb0 = len(casesNoires)
t = [0]*lgCycle

for i in range(lgCycle):
    if pos in casesNoires:
        direction = (direction+1)%4
        casesNoires.remove(pos)
    else:
        direction = (direction-1)%4
        casesNoires.add(pos)
    pos = (pos[0]+vecteurs[direction][0], pos[1]+vecteurs[direction][1])
    t[i] = len(casesNoires)-nb0
    cpt += 1

nbCycles = (10**18-cpt)//lgCycle
reste = (10**18-cpt)%lgCycle


S = len(casesNoires) + t[-1]*nbCycles
if reste != 0:
    S += t[reste-1]

print(S)








