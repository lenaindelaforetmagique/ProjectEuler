##Problem 72
##
##Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
##
##If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
##
##1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
##
##It can be seen that there are 21 elements in this set.
##
##How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?


# > https://en.wikipedia.org/wiki/Farey_sequence
from time import time
t0 =time()
_dico_={}
_dico_[1]=2

def F_n(n):
    if n in _dico_:
        return _dico_[n]
    else:
        s = (n+3)*n//2
        for d in range(2,n+1):
            s -= F_n(n//d)
        _dico_[n]=s
        return s

#for i in range(1, 9):
#    print("{} -> {}".format(i,F_n(i)-2))

d = 1000000

print(F_n(d)-2,time()-t0)


##from arithmetique import *
##from time import time
## 
##n=d
## 
##t0 = time()
##s = 0
##for k in range(2, n+1):
##    s += phi(k) #mobius(k)*(n//k)**2
## 
##print(s, time()-t0)



