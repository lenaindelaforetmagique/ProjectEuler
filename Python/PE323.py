##Problem 323
##
##Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
##(i.e. 0 ≤ yi < 232, every value equally likely).
##
##For the sequence xi the following recursion is given:
##
##    x0 = 0 and
##    xi = xi-1| yi-1, for i > 0. ( | is the bitwise-OR operator)
##
##It can be seen that eventually there will be an index N such that xi = 232 -1 (a bit-pattern of all ones) for all i ≥ N.
##
##Find the expected value of N.
##Give your answer rounded to 10 digits after the decimal point.


from random import randrange

def fact(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

def C_n_k(n,k):
    return fact(n)//(fact(k)*fact(n-k))




def tour(t):
    nbCar = len(t)-1
    t2 = [0]*(nbCar+1)
    
    for k in range(nbCar+1):
        for i in range(k+1):
            t2[k] += t[i]*C_n_k(nbCar-i, k-i)/(2**(nbCar-i))

    return t2

car = 32
t = [C_n_k(car, i)/(2**car) for i in range(car+1)]

E = 0
i = 1
while i*t[-1]>10**(-20):
    E += i*t[-1]
    t[-1] = 0
    t = tour(t)
    i += 1

print(i,E)
