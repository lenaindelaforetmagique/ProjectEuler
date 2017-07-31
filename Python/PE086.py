##Problem 86
##
##A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
##
##However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
##
##It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
##
##Find the least value of M such that the number of solutions first exceeds one million.

from math import gcd
from time import time
t0 = time()

"""
umaxi :
u**2 - v**2 < M
2*u*v < 2*M     --> u<(2*M)**0.5

u**2 - v**2 < 2M
2*u*v < M       --> u<(5/2*M)**0.5

==> umax = int((5/2*M)**0.5)
"""

def genTriplet(umax):
    for u in range(2, umax+1):
        for v in range(u%2 + 1, u+1, 2):
            if gcd(u, v) == 1:
                x = u**2 - v**2
                y = 2*u*v
                z = u**2 + v**2
                if x < y:
                    yield (x,y,z)
                else:
                    yield (y,x,z)

dico = {}
def nbSolutions(M):
    global tcpt
    cpt = 0
    for t in genTriplet(int((5/2*M)**0.5)):
        if t[0]<=M and t[1]<=2*M:
            k = 1
            while k*t[0]<=M:
                # a = k*x
                cpt += max(0,(2*t[0]-t[1])*k//2 + 1)
                if k*t[1]<=M:
                     # a = k*y
                    cpt += (k*t[0])//2
                k += 1
    global dico
    dico[M] = cpt
    return cpt

            
cible = 10**6
m=1
while nbSolutions(m)<cible:
    m *=2
    print(m)

a = m//2
b = m

while b-a>1:
    print((a+b)//2)
    if nbSolutions((a+b)//2)>cible:
        b = (a+b)//2
    else:
        a = (a+b)//2


print(a, dico[a])
print(b, dico[b])


print(time()-t0)


