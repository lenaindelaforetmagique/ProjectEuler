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
from math import *
t0 = time()

def iterCarres(nmin, nmax):
    """ itérateurs de carrés compris entre nmin et nmax"""
    imin = int(nmin**0.5)
    if imin**2 <nmin:
        imin += 1
    imax = int(nmax**0.5)
    for i in range(imin, imax+1):
        yield i, i**2


def tupleTrie(a,b,c):
    u = min(a,b,c)
    w = max(a,b,c)
    v = a+b+c - u-w
    return (u,v,w)
    

def N(a,b,c,k):
    """retourne le nombre de cubies ajoutés à la kième couche sur abc"""
    r = 2*(a*b+b*c+a*c)
    r += 4*(k-1)*(a+b+c)
    r += 4*(k-1)*(k-2)
    return r


def nbTripletSPC_BF(Somme, ProduitCroise):
    """ retourne le nombre de triplets a, b, c tels que:
    - a>=b>=c
    - Somme = a+b+c
    - ProduitCroise = a*b+b*c+a*c"""
    #print("SPC")
    cpt = 0
    c = 1
    cMax = int((ProduitCroise/3)**0.5) #Somme//3
    while c<=cMax:
        #print("c",c)
        b = c
        bMax = int((c**2+ProduitCroise)**0.5-c) #(Somme-c)//2
        while b<=bMax:
            a = Somme - b - c
            if a*b+b*c+a*c== ProduitCroise:
#                print("*",a,b,c)
                cpt += 1
            b += 1

        c += 1
    #print("--", cpt)
    return cpt


CPT,CPT2 = 0, 0
def nbTripletSPC_old(S, P):
    """ retourne le nombre de triplets a, b, c tels que:
    - a>=b>=c
    - S = a+b+c
    - P = a*b+b*c+a*c"""
    global CPT, CPT2
    #print("*******")
    
    rep = [] #set()
    d1 = S**2-3*P
    if d1 >= 0:
        cmin = max(1, ceil((S-2*d1**0.5)/3))
        cmax = S//3 #min(S//3, floor((S+2*d1**0.5)/3))
        #Dmin = (S-cmin)**2-4*(P-cmin*(S-cmax))
        #Dmax = (S-cmax)**2-4*(P-cmax*(S-cmax))
        
        for c in range(cmin, cmax + 1):
            S2 = S-c
            P2 = P-c*(S-c)
            D = S2**2-4*P2
            #print(D)
            sqD = int(D**0.5)
            if sqD**2 == D:
                num1 = S2-sqD
                if num1 >= 2*c and (num1)%2 == 0:
                    a = num1//2
                    b = (S2+sqD)//2
                    #print('$$$',SP_ok(S,P), S, P, c)
                    #rep.add((a,b,c))
                    rep.append((a,b,c))
                    CPT += 1
    else:
        print('merde')
        
##    if len(rep) != 0:
##        print(S,P)
    CPT2 += len(set(rep))
    return len(set(rep))



mem_XY = {}
def nbTripletSPC(S, P):
    """ retourne le nombre de triplets a, b, c tels que:
    - a>=b>=c
    - S = a+b+c
    - P = a*b+b*c+a*c
principe :
S = a+b+c
P = ab+bc+ac

a,b sont solutions de A**2-(S-c)*A+(P-c*(S-c))
il faut donc avoir (S-c)**2-4*(P-c(S-c)) carré
(S-c)**2-4*(P-c(S-c)) = X**2
c'est vrai si :
-3*c**2+2*c*S+(S**2-4*P-X**2)
soit c = (2*S +- Y)/6
avec Y**2 = 16*S**2-48*P-X**2
    """
    global mem_XY
    val = 16*S**2-48*P
  
    if val not in mem_XY:
        mem_XY[val] = set()
        x, x2 = 0, 0
        while x2 <= val//12:
            y2 = val-12*x2
            y = int(y2**0.5)
            if y**2==y2:
                mem_XY[val].add((x,y))
            
            x += 1
            x2 = x**2

    rep = []
    for x, y in mem_XY[val]:
        cpt = 0
        if (2*S+y)%6 == 0:
            #print(val, S, P, x, y)
            c1 = (2*S+y)//6
            #                if (S-c1+x)%2 == 0:
            t = tupleTrie((S-c1+x)//2, (S-c1-x)//2, c1)
            if t[0]>0:
                rep.append(t)
        else:
            cpt += 1
                
        if (2*S-y)%6 == 0:
            c2 = (2*S-y)//6
            #   if ((S-c2)+x)%2 == 0:
            t = tupleTrie((S-c2+x)//2, (S-c2-x)//2, c2)
            if t[0]>0:
                rep.append(t)
        else:
            cpt += 1

        if cpt == 2:
            print("**********2")
        elif cpt == 1:
            print("++++++++++1")
        else:
            print("aiaiaiai")
            
        
##    if len(rep)!=0:
##        print(S, P, val)
    return len(set(rep))




def nbTripletsPC(ProduitCroise):
    """ retourne le nombre de triplets a, b, c tels que:
    - a>=b>=c
    - ProduitCroise = a*b+b*c+a*c"""
    #print("PC")
    
    cpt = 0
    c = 1
    cMax = int((ProduitCroise/3)**0.5)
    while c<=cMax:
        b = c
        bMax = int((c**2+ProduitCroise)**0.5-c)
        while b<=bMax:
            a = (ProduitCroise-b*c)//(b+c)            
            if (ProduitCroise-b*c)%(b+c) == 0:
#                print((ProduitCroise-b*c)//(b+c),b,c)
                cpt += 1
            b += 1
        c += 1
    #print("--",cpt)
    return cpt


def C(n):
    """retourne le nombre de cuboides qui ont une couche de n cubes"""
#    rep = set()
    nbre = 0
    if n%2 == 0:
        n2 = n//2
        # k==1
        #print("k=",1)
        nbre += nbTripletsPC(n2)
        for k in range(2, int(((n2-1)/2)**0.5)+1):
            #print("k=",k)
            alpha = 1
            beta = 6*(k-1)
            gamma = beta*(k-2)-3*n2
            delta = beta**2-4*alpha*gamma
            if delta <=0:
                s = 3
            else:
                s = ceil((-beta+(delta)**0.5)/(2*alpha))
            p = n2-2*(k-1)*(s+k-2)
            while p >= s-2:
                nbre += nbTripletSPC(s, p)
                s += 1
                p = n2-2*(k-1)*(s+k-2)
                
    return nbre



##
##for k in range(1,5):
##    for a in range(1, 39):
##        for b in range(1, a+1):
##            for c in range(1, b+1):
##                if N(a,b,c,k)==154:
##                    print(a, b, c, k)
##
##7 7 2 1
##12 5 1 1
##25 2 1 1
##38 1 1 1

##7 3 3 2
##9 4 1 2
##11 3 1 2
##18 1 1 2
##4 3 3 3
##5 2 1 4

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
    if Cn>vmax:
        print(n, Cn) 
        vmax = Cn

print('/////',n, Cn)


##print(22,C(22))
##print(46,C(46))
##print(78,C(78))
##print(118,C(118))
#print(154,C(154))


print(time()-t0)
print(CPT, CPT2)
        
