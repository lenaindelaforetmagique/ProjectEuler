##Problem 126
##
##The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.
##
##If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.
##
##However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
##
##We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers.
##So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
##
##It turns out that 154 is the least value of n for which C(n) = 10.
##
##Find the least value of n for which C(n) = 1000.

"""
Sur un cuboid a*b*c, la k-ième couche contient :
- augmentation de "face" : 2*(a*b+b*c+a*c)
- augmentation d'arrête  : 4*(k-1)*(a+b+c)
- augmentation de sommet : 8*(k-1)*(k-2)/2

> on cherche le premier nombre dont le nombre de partition formatées vaut 1000

"""

from time import time
from arithmetique import *
t0 = time()

def iterCarres(nmin, nmax):
    """ itérateurs de carrés compris entre nmin et nmax"""
    imin = int(nmin**0.5)
    if imin**2 <nmin:
        imin += 1
    imax = int(nmax**0.5)
    for i in range(imin, imax+1):
        yield i, i**2
    

def N(a,b,c,k):
    """retourne le nombre de cubies ajoutés à la kième couche sur abc"""
    r = 2*(a*b+b*c+a*c)
    r += 4*(k-1)*(a+b+c)
    r += 4*(k-1)*(k-2)
    return r


def C(n):
    """retourne le nombre de cuboides qui ont une couche de n cubes"""
    rep = set()
    #nbre = 0
    if n%2 == 0:
        n2 = n//2
        for k in range(1, int(((n-2)/4)**0.5)+1):
            for a in range(1, (n2-1-2*k*(k-1))//(2*k)+1):
                if k == 1:
                    for b in range(1, a+1):
                        num = n2 - a*b
                        if num%(a+b) == 0 and num >= (a+b) and num//(a+b) <= b:
                            c = (n2-a*b)//(a+b)
                            rep.add((a,b,c))
                            #nbre += 1
                else:
                    
                    alpha = (a+2*(k-1))*4
                    beta = (2*(k-1)*(a+k-2)-n2)*4
                    #print(k, a, n2, alpha, beta)
                    #D   = s**2 + s*alpha + beta
                    Dmin = max(2**2 + 2*alpha + beta, 1)
                    Dmax = max((2*a)**2 + (2*a)*alpha + beta, 1)
                    #print(Dmin, Dmax)
                    for d, D in iterCarres(Dmin, Dmax):
                        discr = alpha**2-4*(beta-D)
                        sqdiscr = int(discr**0.5)
                        if discr >= 0 and discr == sqdiscr**2 and sqdiscr%2 == 0:
                            s = (sqdiscr-alpha)//2
                            if (s+d)%2 == 0:
                                c1 = (s+d)//2
                                b = s-c1
                                if N(a,b, c1, k) == n:
                                    if c1>=1 and b >= c1 and a >= b:
                                        rep.add((a,b,c1))

                                c2 = (s-d)//2
                                b = s-c2
                                if N(a,b, c2, k) == n:
                                    if c2>= 1 and b >= c2 and a >= b:
                                        rep.add((a,b,c2))
                                
    return len(rep) #nbre


n = 6
vmax = 0
Cn = C(n)
while Cn!=10:
    n+=2
    Cn = C(n)
print('/////',n, Cn)
while Cn!=100:
    n+=2
    Cn = C(n)
print('/////',n, Cn)    

while Cn!=1000:
    n+=2
    Cn = C(n)
    if Cn>vmax:
        print(n, Cn) 
        vmax = Cn

print('/////',n, Cn)


print(22,C(22))
print(46,C(46))
print(78,C(78))
print(118,C(118))
print(154,C(154))


print(time()-t0)
        
