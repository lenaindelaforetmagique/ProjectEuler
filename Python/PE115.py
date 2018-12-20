#PE115
"""
Voir description PE114
"""

def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def C_n_k(n, k):
    return fact(n)//(fact(k)*fact(n-k))


def F(m, Ltot):
    arr = 1
    # Boucle sur le nombre de segments rouges
    for k in range(1, (Ltot+1)//(m+1)+1):
        # Boucle sur la longueur rouge possible
        for lr in range(m*k, Ltot-(k-1)+1):
            #Arr = arrangements du rouge * arrangements du noir
            arr += C_n_k(lr - (m-1)*k-1, k-1) * C_n_k(Ltot - lr + 2-1, k)
    return arr

n = 1
while F(50, n)<10**6:
    n += 1

print(n)
