##PE003
##
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?


nb = 600851475143


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

def primeFactors(n):
    l = []
    i = 2
    a = n
    while a != 1 and i <= a:
        if a % i == 0:
            l.append(i)
            a /= i
        else:
            i = nextPrime(i)
    return l

print(primeFactors(nb)[::-1])


    
  
  

