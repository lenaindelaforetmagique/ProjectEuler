#PE199
from math import pi

def surface(k):
    """ surface d'un cercle de courbure k"""
    r = 1/k
    return  pi*r**2

def descartes(k1, k2, k3):
    """ retourne les rayons des deux cercles possibles tangents aux 3"""
    k41 = k1+k2+k3 + 2*(k1*k2 + k2*k3 + k3*k1)**(1/2)
    k42 = k1+k2+k3 - 2*(k1*k2 + k2*k3 + k3*k1)**(1/2)
    return [k41, k42]

def aire(k1, k2, k3, prof):
    k4 = max(descartes(k1, k2, k3))
    r = surface(k4)
    if prof > 0:
        r += aire(k1, k2, k4, prof-1)
        r += aire(k1, k3, k4, prof-1)
        r += aire(k2, k3, k4, prof-1)
    return r


k0 = -(0.00001)
k1 = k0/(3-2*(3)**0.5)
##print(k1)
##print(k0/(3+2*(3)**0.5))
##print(k0/(3-2*(3)**0.5))


prof = 10-1

s0 = surface(k0)
s1 = 3*surface(k1)
s1 += aire(k1, k1, k1, prof)
s1 += 3*aire(k1, k1, k0, prof)

print("{0:10.8f}".format(1-s1/s0))
       
    
    




    
    
    
