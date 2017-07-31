"""
PE233

Let f(N) be the number of points with integer coordinates that are on a circle
passing through (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10**11 such that f(N) = 420 ?
"""

from math import *

def PointsEntiers(a,b):
    L=[]
    xC=a/2
    yC=b/2
    R2=a**2+b**2
    R=sqrt(a**2+b**2)/2
    for i in range(int(xC-R),int(xC+R),1):
        y0=sqrt(R2-(2*i-a)**2)
        y=[ceil((-y0+b)/2),floor((-y0+b)/2),ceil((y0+b)/2),floor((y0+b)/2)]
#        print(i,y)
        for j in range(4):
            if (2*i-a)**2+(2*y[j]-b)**2==R2:
                if not ([i,y[j]] in L):
                    L.append([i,y[j]])
#                    print(L[-1])
                    
    return len(L)




def function_f(n):
    L=[]
    xC=n/2
    yC=n/2
    R2=2*(n**2)
    R=n/sqrt(2)
    for i in range(int(xC-R),int(xC+R),1):
        y0=sqrt(R2-(2*i-n)**2)
        y=[ceil((-y0+n)/2),floor((-y0+n)/2),ceil((y0+n)/2),floor((y0+n)/2)]
#        print(i,y)
        for j in range(4):
            if (2*i-n)**2+(2*y[j]-n)**2==R2:
                if not ([i,y[j]] in L):
                    L.append([i,y[j]])
#                    print(L[-1])
                    
    return len(L)

                    
        

#print(function_f(10000))

#aucune solution dans [1;18500]
for a in range(15001,20001,500):
    print("==",a)
    for n in range(a,a+501,1):
        if PointsEntiers(n,n)==420:
            print("-->",n)
    

        
        
        
        
    
    
    


    
