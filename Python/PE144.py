# Problem 144

#from rationnels import *
from rationnels import Rationnel
from vecteurs import Vecteur


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
    # print(type(k))

    return B + k * V2


a = 5
b = 10
a2 = a * a
b2 = b * b

A = Vecteur([0, 10.1])
B = Vecteur([1.4, -9.6])
C = nextP(A, B)
cpt = 1
while not(C.coord[0] > -0.01 and C.coord[0] < 0.01 and C.coord[1] > 0):
    print(C)
    cpt += 1
    A = Vecteur(B.coord)
    B = Vecteur(C.coord)
    C = nextP(A, B)


print(cpt)
