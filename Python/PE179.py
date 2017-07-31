##Problem 179
##
##Find the number of integers 1 < n < 10**7, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

from time import time
from math import log
t0 = time()

nmax = 10**7

#Crible 1 - ultra simple, mais lent

L = [0]*2+[1]*(nmax-1)
print(len(L))
for i in range(2, nmax+1):
    for k in range(1, nmax//i +1):
        L[k*i] += 1
print('fin crible', time()-t0)

###Crible 2 (GG)
##L = [0,1]+[0]*(nmax-1)
##
##N=10**7
##Lprime2=[p for p in Lprime if p**2<=N]
##
##
##
##LDIV=[0 for i in range(N+1)]
##LDIV[1]=1
###crible pour les petits nombres premiers
##for p in Lprime2:
##    prim,pui=p,1
##    while prim<N:
##        for i,v in enumerate(LDIV[1:N//prim+1]):
##            if v!=0 and i%p!=0:
##                LDIV[prim*(i+1)]=(pui+1)*v
##        prim*=p
##        pui+=1
##                
##print('coucou',time()-t0)
###pour les gd nombres premiers une seule puissance possible
##for p in [p for p in Lprime if p not in Lprime2]:  
##    for i,v in enumerate(LDIV[1:N//p+1]):
##        LDIV[p*(i+1)]=2*v 
##
##print('fin crible', time()-t0)




S = 0
for i in range(2, nmax):
    if L[i] == L[i+1]:
        S += 1

print(S)
print(time()-t0)
    
    





