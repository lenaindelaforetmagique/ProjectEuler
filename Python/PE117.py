#PE117
"""
Voir description PE114

nbre de partitions avec pièces (1, 2, 3, 4)
* nbre d'anagrammes


"""

listePartitions = []

def detailAppoints(M,devises, t):
    global listePartitions
    t = t[:] #copie de t
    s=0
    if len(devises)==0:
        if M==0:
            listePartitions.append(t)
            return 1
        else:
            return 0
    else:
        for i in range(0,M//devises[-1]+1):
            t[len(devises)-1] = i
            s+=detailAppoints(M-i*devises[-1],devises[:-1], t)
        # print(s)
        return s


def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def anag(t):
    """Nombre d'anagrammes"""
    num = fact(sum(t))
    den = 1
    for v in t:
        den *= fact(v)
    return num//den
    


tokens=[1,2,3,4]
t = [0]*4
print(detailAppoints(50,tokens, t))

resu = sum([anag(t) for t in listePartitions])
print(resu)


