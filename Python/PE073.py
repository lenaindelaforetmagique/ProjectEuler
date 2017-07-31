##Problem 73
##
##Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
##
##If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
##
##1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
##
##It can be seen that there are 3 fractions between 1/3 and 1/2.
##
##How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

# > https://en.wikipedia.org/wiki/Farey_sequence

"""Le prochain élément de la séquence de Farey à apparaitre entre a/b et c/d est
(a+c)/(b+d)
on compte donc le nombre d'insertions...
"""

import sys
sys.setrecursionlimit(10000)

def nbFarey(a,b,c,d,n):
    if b+d>n:
        return 0
    else:
        s = 1 + nbFarey(a,b,a+c,b+d,n) + nbFarey(a+c,b+d,c,d,n)
        return s

print(nbFarey(1,3,1,2,12000))






