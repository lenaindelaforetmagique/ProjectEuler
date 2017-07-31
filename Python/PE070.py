##Problem 70
##
##Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
##The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
##
##Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
##
##Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


from arithmetique import *
from time import time

def isPerm(a, b):
    return sorted(str(a))==sorted(str(b))


n = 87109
rapMin = n / phi(n)
#print(phiMin)

Nmax = 10**7



##while Nmax<=10**7:
##    t0 = time()
##    a = 2
##    while a/phi(a) > rapMin:
##        a = nextPrime(a)
##    print("blop",Nmax, a)
##    # a est le plus petit nombre premier possible
##
##    b = previousPrime(Nmax // a)
##    while a<=b:
##        #print(a,b)
##        # b est le plus grand premier possible
##        fiab = (a-1)*(b-1) #phi(a*b)
##        while a*b/fiab<rapMin and b>=a:
##            if isPerm(a*b, fiab):
##                rapMin = a*b/fiab
##                n = a*b
##            
##            b = previousPrime(b)
##            fiab = phi(a*b)
##
##        a = nextPrime(a)
##        b = previousPrime(Nmax // a)
##    print(time()-t0)
##    Nmax *= 10
##    
##
##print(n, phi(n),rapMin)


print(n)
t0 = time()
a = nextPrime(int(Nmax**0.5))
while a/phi(a)<rapMin:
    b = previousPrime(Nmax // a)
#    print(a,b)
    fiab = phi(a*b)
    while b>=a and a*b/fiab<rapMin:
        if isPerm(a*b, fiab):
            n = a*b
            rapMin = n/fiab
            print(n,a,b)
        b = previousPrime(b)
        fiab = phi(a*b)

    a = previousPrime(a)

print(time()-t0)
   

print(n, phi(n),rapMin)




