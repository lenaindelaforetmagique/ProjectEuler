##Problem 92
##
##A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
##
##For example,
##
##44 → 32 → 13 → 10 → 1 → 1
##85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
##
##Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
##
##How many starting numbers below ten million will arrive at 89?


from time import time

D = {}
PUISS = 7
t0 = time()

##def cal(n):
##    return sum([int(c)**2 for c in str(n)])

def cal(n):
    if n == 0:
        return 0
    else:
        return (n%10)**2 + cal(n//10)
        

def ending(n):
    a = cal(n)
    while a != 89 and a != 1 and a not in D:
        a = cal(a)

    if a in D:
        rep = D[a]
    else:
        rep = a

    if n <= PUISS*(9**2):
        D[n] = rep

    return rep

s = 0
for i in range(1,10**PUISS):
    if ending(i) == 89:
        s += 1


print(s, time()-t0)
D.clear()



