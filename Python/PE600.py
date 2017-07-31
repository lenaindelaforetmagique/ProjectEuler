##Problem 600
##
##Let H(n) be the number of distinct integer sided equiangular convex hexagons with perimeter not exceeding n.
##Hexagons are distinct if and only if they are not congruent.
##
##You are given H(6) = 1, H(12) = 10, H(100) = 31248.
##Find H(55106).

"""
Résumé :
      d____ (i;j)
      /    | c
    e/     /
    |     /b
   f|____/
       a

Principe général :
- on écrit les conditions sur l'unicité de l'hexagone :
    a >= b
    a >= c
    a >= d
    a >= e
    a >= f
    b >= f
    b = k1
    e = k2
- on écrit la condition sur le périmètre max :
    Pmax >= 2*i+2*j-k1-k2
- boucle sur i [ 2 ; (Pmax-2)//2 ]
- boucle sur j [ 2 ; min(i, (Pmax-i)//2) ]
- il reste la somme k1+k2 à traiter (fonction 'compte')


-> 2668608479740672 496.17 s
"""



from time import time
t0 =  time()


def compte_BF(smini, smaxi, mini, maxi):
    """
Trouver le nombre de façons de former :
max(j, 2i+2j-Pmax) <= k1+k2 <= i
1<= k1 <= k2 <= j-1
"""
    s = 0
    for k1 in range(mini, maxi + 1):
        for k2 in range(k1, maxi+1):
            if smini <= k1+k2 and k1+k2 <= smaxi:
                s += 1
    return s


def compte(smini, smaxi, maxi):
    n = 2*maxi - smini + 1
    s = (1+n//2)* ((n+1)//2)
    #print('n',n, s)
    if 2*maxi > smaxi:
        n = 2*maxi - smaxi
        s -= (1+n//2)* ((n+1)//2)
        #print('n2', n, (1+n//2)* ((n+1)//2))
    return s
    

def H(Pmax):
    S = 0
    for i in range(2, (Pmax-2)//2 + 1):
        for j in range(2, min(i, (Pmax-i)//2)+1):
            S += compte(max(j, 2*i+2*j-Pmax), i, j-1)
    return S


t0 = time()
print(H(55106), time()-t0)







                
    



