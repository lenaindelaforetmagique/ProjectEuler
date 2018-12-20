## Problem 301
"""
Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function X(n1,n2,n3) — that you may look up or attempt to deduce for yourself — that returns:

    zero if, with perfect strategy, the player about to move will eventually lose; or
    non-zero if, with perfect strategy, the player about to move will eventually win.

For example X(1,2,3) = 0 because, no matter what the current player does, his opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by his opponent until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n ≤ 2**30 does X(n,2n,3n) = 0 ?
"""

"""
https://fr.wikipedia.org/wiki/Jeux_de_Nim
Nombre de Grundy :
>on obtient le nombre de Grundy de la position en exprimant le nombre de pions de chaque pile en binaire et en faisant la somme OU exclusif ou XOR, (notée aussi ⊕) de ces nombres.

on finit par en déduire que les nombres valides sont ceux qui, exprimés en binaires,
sont constitués de _1_ tous séparés.
> nombre d'arrangement de n 1_isolés = nombre de façons de décomposer 30-n paquets_de_0

"""

def fact(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

def C_n_k(n,k):
    return fact(n)//(fact(k)*fact(n-k))

S = 1 # solution 2**30
# solutions inférieures strictement à 2**30

for nb_1 in range(1, 16): #15 max
    nb_0 = 30-nb_1
    S += C_n_k(nb_0+1,nb_1)

print(S)
    
    

