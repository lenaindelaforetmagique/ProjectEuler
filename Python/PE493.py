##Problem 493
##
##70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
##
##What is the expected number of distinct colors in 20 randomly picked balls?
##
##Give your answer with nine digits after the decimal point (a.bcdefghij).

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


C = [[0]*11 for i in range(0,11)]
for n in range(0,11):
    for k in range(0,n+1):
        C[n][k] = fact(n)//(fact(k)*fact(n-k))


tmp = []
decomp = []

def nbWay(N, maxCoin,nbMax):
    if N==0:
        if len(tmp)<=nbMax:
            decomp.append(tmp[:])
    else:
        for n in range(maxCoin, 0,-1):
            tmp.append(n)
            nbWay(N-n,min(n,N-n),nbMax)
            tmp.pop()

nbWay(20,10,7)
print(len(decomp))
##for t in decomp:
##    if len(t) == 7:
##        print(t)


nbTirages = [0]*8
for i,t in enumerate(decomp):
    nb = 1
    # distribution des billes de la meme couleur
    for v in t:
        nb *= C[10][v]
        
    # distribution des couleurs (nombre d'anagrammes)
    ana = fact(7)//(fact(7-len(t)))
    c = 1
    for i in range(1,len(t)):
        if t[i-1]==t[i]:
            c += 1
        else:
            ana //= fact(c)
            c = 1
    ana //= fact(c)

    nb *= ana
    nbTirages[len(t)] += nb

tot = 0
for i, t in enumerate(nbTirages):
    tot += i*t
    #print(i, t)

#total1 = sum(nbTirages)
total2 = fact(70)//(fact(20)*fact(50))
#print(total1)
#print(total2)
print(tot/total2)

