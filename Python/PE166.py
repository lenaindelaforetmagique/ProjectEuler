##Problem 166
##
##A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.
##
##It can be seen that in the grid
##
##6 3 3 0
##5 0 4 3
##0 7 1 4
##1 2 4 5
##
##the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.
##
##In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?

from matrices import *
from time import time
t0 = time()

def gen(n, dim):
    if dim > 0:
        for i in range(n):
            for t2 in gen(n,dim-1):
                yield [i]+t2
    else:
        yield []

M  = [[1,1,1,1,-1,-1,-1,-1,0,0,0,0,0,0,0,0]]
M += [[1,1,1,1,0,0,0,0,-1,-1,-1,-1,0,0,0,0]]
M += [[1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1]]
M += [[ 0,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0]]
M += [[1, 0,1,1,0,-1,0,0,0,-1,0,0,0,-1,0,0]]
M += [[1,1, 0,1,0,0,-1,0,0,0,-1,0,0,0,-1,0]]
M += [[1,1,1, 0,0,0,0,-1,0,0,0,-1,0,0,0,-1]]
M += [[ 0,1,1,1,0,-1,0,0,0,0,-1,0,0,0,0,-1]]
M += [[1,1,1, 0,0,0,-1,0,0,-1,0,0,-1,0,0,0]]

echM = echelonne(M)
affiche(echM)

pivots = []
lSuppr = []
for i in range(len(echM)):
    j = 0
    while j < len(echM[i]) and echM[i][j] == 0:
        j += 1
    if j < len(echM[i]):
        pivots.append(j)
    else:
        lSuppr.append(i)



M2 = [[v for j, v in enumerate(l) if j not in pivots] for i,l in enumerate(echM) if i not in lSuppr]
M2 = [[int(v) if v == int(v) else v for v in l] for l in M2]
#affiche(M2)

nbL = len(M2)
nbC = len(M2[0])


def test(t, M2):
    global nbL, nbC
    for i in [3,7,6,2,0,1,4,5]: #range(nbL):
        s = 0
        for j in range(nbC):
            s += M2[i][j]*t[j]
        #if int(s) != s or s>0 or s<-9:
        if s>0 or s<-9:
            #print(t, s)
            return False
    #print(t)
    return True


cpt = 0

##for t in gen(10,nbC):
##    if test(t, M2):
##        cpt += 1

print(cpt)
print(time()-t0)

def ok(n):
    return n>=0 and n<=9

for hlm in gen(10,3):
    a = hlm[0]+hlm[1]-hlm[2]
    if ok(a):
        for jk in gen(10,2):
            e = -hlm[0] + jk[0] + jk[1]
            if ok(e):
                for no in gen(10,2):
                    d = -a + sum(no)
                    c = -hlm[0]+jk[0]-jk[1]-hlm[1]+2*hlm[2]+no[0]
                    f = -hlm[0]-jk[1]-hlm[1]+2*hlm[2]+sum(no)
                    if ok(d) and ok(c) and ok(f):
                        for p in range(10):
                            g = hlm[0]-jk[0]+hlm[1]-hlm[2]+p
                            b = g + jk[1]-no[0]
                            i = -sum(jk)-hlm[1]+hlm[2]+sum(no)+p
                            if ok(b) and ok(i) and ok(g):
                                cpt += 1

print(cpt)

print(time()-t0)
    

