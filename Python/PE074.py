##Problem 74
##
##The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
##
##1! + 4! + 5! = 1 + 24 + 120 = 145
##
##Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
##
##169 → 363601 → 1454 → 169
##871 → 45361 → 871
##872 → 45362 → 872
##
##It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
##
##69 → 363600 → 1454 → 169 → 363601 (→ 1454)
##78 → 45360 → 871 → 45361 (→ 871)
##540 → 145 (→ 145)
##
##Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
##
##How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from time import time

t0 = time()
fact = [1]*10
for i in range(1,10):
    fact[i] = i * fact[i-1]
    
#print(fact)

def factChain(a):
    s = 0
    while a > 0:
        s += fact[a%10]
        a //= 10
    return s

def longCycle(a):
    t = [a]
    lg = 1
    a = factChain(a)
    while a not in t:
        t.append(a)
        lg += 1
        a = factChain(a)
    return lg

##a = 69
##print(a)
##print(longCycle(a))
##print(a)

nbre = 0
for i in range(0, 10**6):
    if longCycle(i) == 60:
        nbre += 1

print(nbre, time()-t0)

