#PE116
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
    arr = 0 #1
    # Boucle sur le nombre de segments rouges
    for k in range(1, (Ltot)//(m)+1):
        lr = m * k
        #Arr = arrangements du noir
        # nombre de positions de cases parmi les cases restantes + cases rouges
        arr += C_n_k(Ltot - lr + k, k)
    return arr

Ltot = 50
a = F(2,Ltot)
b = F(3,Ltot)
c = F(4,Ltot)

print(a, b, c)
print("TOTAL = ", a+b+c)
