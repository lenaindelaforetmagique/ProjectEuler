##Problem 7
##
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?


def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i+=1
    return True

def nextPrime(n):
    i = n + 1
    while not isPrime(i):
        i+=1
    return i

a=1
for i in range(10001):
    a=nextPrime(a)

print(a)



