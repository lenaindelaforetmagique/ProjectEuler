##Problem 15
##
##Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
##
##How many such routes are there through a 20×20 grid?


def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    return p


def C_n_k(n, k):
    return fact(n)//(fact(n-k)*fact(k))

print(C_n_k(40,20))        
