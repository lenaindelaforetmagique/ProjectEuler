##Problem 14
##
##The following iterative sequence is defined for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13, we generate the following sequence:
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##
##It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
##Which starting number, under one million, produces the longest chain?
##
##NOTE: Once the chain starts the terms are allowed to go above one million.


D = {} # contient les longueurs de chemin des termes parcourus
D[1] = 1
def nextCollatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1


def longCollatz(n):
    if n not in D:
        D[n] = 1 + longCollatz(nextCollatz(n))
    return D[n]

vMax = 0
iMax = 0
for i in range(1, 10**6):
    if longCollatz(i) > vMax:
        vMax = longCollatz(i)
        iMax = i

print(iMax, vMax)
