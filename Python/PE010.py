##Problem 10
##
##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.

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

a = 0
s = 0
while a < 2*10**6:
    #print(a)
    s += a
    a = nextPrime(a)

print(s)
    
  
  

