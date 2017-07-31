#PE114


"""
Nombre d'arrangements de k blocs rouges :
  LR fixe, 3 = longueur mini
  on a en fait LR-3*k à distribuer.
  astuce, on ajoute k pseudo-unités
  on cherche ensuite (k-1) séparateurs parmi (LR-2*k-1) positions de séparateurs

Nombre d'arrangements de k+1 blocs noirs :
  Ltot-LR fixe
  Pour gérer les abouts, on ajoute 2 pseudo-unités
  on cherche ensuite (k) séparateurs parmi (Ltot-LR+2-1) positions de séparateurs
"""

def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def C_n_k(n, k):
    return fact(n)//(fact(k)*fact(n-k))

Ltot = 50
arr = 1
# Boucle sur le nombre de segments rouges
for k in range(1, (Ltot+1)//4+1):
    # Boucle sur la longueur rouge possible
    for lr in range(3*k, Ltot-(k-1)+1):
        #Arr = arrangements du rouge * arrangements du noir
        arr += C_n_k(lr - 2*k-1, k-1) * C_n_k(Ltot - lr + 2-1, k)
    

print(Ltot, arr)
        
