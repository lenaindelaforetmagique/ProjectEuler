##Problem 124
##
##The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
##
##If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
##Unsorted
##
##Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
##
##If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).


from arithmetique import *
from time import time

t0 = time()

##def rad(n):
##    t = set(primeFactors(n))
##    p = 1
##    for k in t:
##        p *= k
##    return p
##
##t = []
##for i in range(1,100001):
##    if i%1000 == 0:
##        print(i)
##    t.append([i, rad(i)])
## 
###t = [[i, rad(i)] for i in range(1,100001)]
##t.sort(key = lambda x:x[1])
##print(t[10000-2][0],t[10000-2][1])
##print("-->", t[10000-1][0],t[10000-1][1])
##print(t[10000-0][0],t[10000-0][1])
##print(time() - t0)


def rad(limit) :
    L = [1 for i in range(limit + 1)] 
    for i in range(2, limit + 1) :
        if L[i] == 1 :
            for j in range(i, limit + 1, i) :
                L[j] *= i
    return L
"""
[0  1  2  3  4  5  6  7  8  9  10]
>1  1  1  1  1  1  1  1  1  1   1
>*  *  2  1  2  1  2  1  2  1   2
>*  *  *  3  2  1  6  1  2  3   2
>*  *  *  *  *  5  6  1  2  3  10
>*  *  *  *  *  *  *  7  2  3  10
>etc.

"""
def main() :
    delta = time()
    limit = 100000
    radList = rad(limit)
    L = [(i, radList[i]) for i in range(limit + 1)]
    L = sorted(L, key = lambda couple: couple[1])
    delta = time() - delta
    return L[10000][0], delta

print(main())
