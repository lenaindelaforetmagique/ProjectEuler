##Problem 91
##
##The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
##
##There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
##0 ≤ x1, y1, x2, y2 ≤ 2.
##
##Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

from math import gcd

NB = 50
# moins brute force :
s = 3 * NB**2 # familles des (0,0) + (x,0) + (0,x)
#print(s)
for j in range(1, NB+1):
    for i in range(1, NB+1):
        g = gcd(i, j)
        k, l = i//g, j//g
        s += 2 * min((NB-i)//l, j//k)

print(s)



##
###from matplotlib.pyplot import *
##
##def genCarre(inf,sup):
##    for i in range(inf, sup):
##        for j in range(inf, sup):
##            yield i, j
##
##
### brute force - pour voir -
##s = NB**2 # nbre de tgle rect par (0,0)
##for i, j in genCarre(0,NB + 1): # couple porteur de l'angle droit
##    for k, l in genCarre(0,NB + 1): # couple porteur du troisième angle
##        if i**2 + j **2 + (k-i)**2 + (l-j)**2 == k**2 + l**2 and (i,j)!=(0,0) and (i,j)!=(k,l) and (k,l)!=(0,0):
##            s+=1
####            if i!=0 and j!=0:
####                X = [0, i, k ,0]
####                Y = [0, j, l, 0]
####                plot(X,Y)
##print(s)
###show()    



        
    



