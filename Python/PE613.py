##Pythagorean Ant
##Problem 613
##
##Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut out a triangle with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down into the garden.
##Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl straight ahead in random direction in order to get back into the grass.
##
##Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are equiprobable, what is the probability that the ant leaves the triangle along its longest side?
##Give your answer rounded to 10 digits after the decimal point.
##

"""
C
| \
|  \
|   \
| *F \
|     \
A------B

"""



from random import *
from math import *


lx, ly = 30, 40


def probaF(x, y):
    """proba de tomber sur BC"""
    global lx, ly
    FBx, FBy = lx-x, 0-y
    FCx, FCy = 0-x, ly-y
    nFB2 = FBx**2+FBy**2
    nFC2 = FCx**2+FCy**2
    norm = (nFB2*nFC2)**0.5
    pscal = FBx*FCx + FBy*FCy
    angle = acos(pscal/(norm))
    return angle/(2*pi)

##########

"""
alpha(x,y) = 2*pi - pi/2 - atan((lx-x)/y) - atan((ly-y)/x)
p(x,y) = alpha(x,y) / (2*pi)

P_tot = integrale(p(x,y)*dx*dy)/integrale(dx*dy)
      = integrale(3*pi/2 - atan((lx-x)/y) - atan((ly-y)/x)))/(pi*lx*ly)
      = integrale(3*pi/2) - integrale(atan((lx-x)/y)) - integrale(atan((ly-y)/x))/(pi*lx*ly)
      = (A - B - C)/(pi*lx*ly)

A = 3*pi/2*lx*ly/2 = pi*lx*ly*3/4
B = integrale(atan((lx-x)/y))
C = integrale(atan((ly-y)/x))

"""


def integraleB(lx, ly, nb):
    terme1 = atan(lx/ly)*lx/ly-log(1+(lx/ly)**2)/2
    res1 = -(terme1*ly**2)/2
    res2 = 0
    for i in range(nb):
        y = (1/2+i)*ly/nb
        res2 += lx*atan(lx/y)-y*log(1+(lx/y)**2)/2

    return res1 + res2*ly/nb

P0, P1 = 0, 1
nb = 1
while abs((P0-P1)/P1)>10**(-10):
    print(nb, P1)
    P0 = P1
    
    nb *= 2
    A = pi * lx * ly * 3 / 4
    B = integraleB(lx,ly,nb)
    C = integraleB(ly,lx,nb)
    P1 = (A-B-C)/(pi*lx*ly)


print("{0:.10}".format(P1))








            
            
            
        
        
    


