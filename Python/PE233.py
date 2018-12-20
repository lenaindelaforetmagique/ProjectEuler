# Problem 233
##
# Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).
##
# It can be shown that f(10000) = 36.
##
# What is the sum of all positive integers N ≤ 10**11 such that f(N) = 420 ?

from arithmetique import *
from time import time
t0 = time()


"""
Triplets pour zmax:
- 10**4 : 2000
- 10**5 : 20218
- 10**6 : 202461
- 10**7 : 2025972
- 10**11 : estimé à 2*10**10

"""


def PointsEntiers(a, b):
    L = []
    xC = a / 2
    yC = b / 2
    R2 = a**2 + b**2
    R = sqrt(a**2 + b**2) / 2
    for i in range(int(xC - R), int(xC + R), 1):
        y0 = sqrt(R2 - (2 * i - a)**2)
        y = [ceil((-y0 + b) / 2), floor((-y0 + b) / 2),
             ceil((y0 + b) / 2), floor((y0 + b) / 2)]
#        print(i,y)
        for j in range(4):
            if (2 * i - a)**2 + (2 * y[j] - b)**2 == R2:
                if not ([i, y[j]] in L):
                    L.append([i, y[j]])
#                    print(L[-1])

    return len(L)


def tripletPy(zmax):
    """parcourt les triplet pythagoriciens x<y<z<=zmax"""
    umax = int(zmax**0.5)
    for u in range(2, umax + 1):
        for v in range(u % 2 + 1, min(u, zmax - u**2) + 1, 2):
            if gcd(u, v) == 1:
                x = u**2 - v**2
                y = 2 * u * v
                z = u**2 + v**2
                if x < y:
                    yield (x, y, z)
                else:
                    yield (y, x, z)


cpt = 0
for (x, y, z) in tripletPy(10**7):
    cpt += 1

print(cpt)


def function_f(n):
    L = []
    xC = n / 2
    yC = n / 2
    R2 = 2 * (n**2)
    R = n / sqrt(2)
    for i in range(int(xC - R), int(xC + R), 1):
        y0 = sqrt(R2 - (2 * i - n)**2)
        y = [ceil((-y0 + n) / 2), floor((-y0 + n) / 2),
             ceil((y0 + n) / 2), floor((y0 + n) / 2)]
#        print(i,y)
        for j in range(4):
            if (2 * i - n)**2 + (2 * y[j] - n)**2 == R2:
                if not ([i, y[j]] in L):
                    L.append([i, y[j]])
#                    print(L[-1])

    return len(L)


##
##
##
##Nmax = 10**8
##premiers = Eratosthene(Nmax//2)
# print(len(premiers))
##
##i = 0
##pMax = int(Nmax**0.5)
##j = len(premiers)-1
##S = 0
# while premiers[i] <= pMax:
# while premiers[j] > Nmax//premiers[i]:
##        j -= 1
##    S += j+1-i
##    i += 1
##
# print(S)
print(time() - t0)


# print(function_f(10000))

# aucune solution dans [1;18500]
for a in range(15001, 20001, 500):
    print("==", a)
    for n in range(a, a + 501, 1):
        if PointsEntiers(n, n) == 420:
            print("-->", n)
