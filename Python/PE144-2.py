# Problem 144

#from rationnels import *
from rationnels import Rationnel
from vecteurs import Vecteur
from time import time

t00 = time()


def nextP(A, B):
    """
    A est un vecteur A.coord vaut [xa,ya]
    B est un vecteur B.coord vaut [xb,yb]
    > on retourne le point C (rebond du rayon AB sur l'ellipse)
    """
    global a2, b2
    V1 = B - A

    t = Vecteur([1, -1 * ((b2) / (a2)) * B.coord[0] / B.coord[1]])
    n = Vecteur([((b2) / (a2)) * B.coord[0] / B.coord[1], 1])

    V2 = ((V1 * t) * t) - ((V1 * n) * n)

    q1 = V2.coord[0]
    q2 = V2.coord[1]
    k = (-2 * q1 * B.coord[0] / (a2) - 2 * q2 *
         B.coord[1] / (b2)) / (q1 * q1 / a2 + q2 * q2 / b2)

    return B + k * V2


a = Rationnel(5)
b = Rationnel(10)
a2 = a * a
b2 = b * b

A = Vecteur([0, 10.1])
B = Vecteur([1.4, -9.6])

A = Vecteur([Rationnel(0), Rationnel(101, 10)])
B = Vecteur([Rationnel(14, 10), Rationnel(-96, 10)])

C = nextP(A, B)
t0 = time()
cpt = 1

xmin = Rationnel(-1, 100)
xmax = Rationnel(1, 100)


while not(C.coord[0] > xmin and C.coord[0] < xmax and C.coord[1] > 0):
    #print(cpt, time()-t0, len(str(C)))
    t0 = time()
    cpt += 1
    A = Vecteur(B.coord)
    B = Vecteur(C.coord)
    C = nextP(A, B)

# print(C)
print(cpt)
print(time() - t00)
