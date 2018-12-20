# Problem 76
##
# It is possible to write five as a sum in exactly six different ways:
##
##4 + 1
##3 + 2
##3 + 1 + 1
##2 + 2 + 1
##2 + 1 + 1 + 1
##1 + 1 + 1 + 1 + 1
##
# How many different ways can one hundred be written as a sum of at least two positive integers?


from time import time
t0 = time()


nbre = 500
coins = []

mem = {}


def nbCombi(S, e_t):
    if S not in mem:
        mem[S] = {}
    elif e_t in mem[S]:
        return mem[S][e_t]

    if e_t == 0:
        if S % coins[e_t] == 0:
            return 1
        else:
            return 0
    else:
        nb = 0
        imax = S // coins[e_t]
        somme = 0
        for i in range(imax + 1):
            somme += nbCombi(S - i * coins[e_t], e_t - 1)
        mem[S][e_t] = somme
        return somme


v = 0
for S in range(2, 101):
    coins = [i for i in range(1, S)]
    mem.clear()
    # print(S, nbCombi(S, S - 2) - v)
    v = nbCombi(S, S - 2)
    print("--", S, v)
print((time() - t0))
