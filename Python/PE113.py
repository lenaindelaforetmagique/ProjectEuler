##Problem 113
##
##Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
##
##Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
##
##We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
##
##As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.
##
##How many numbers below a googol (10100) are not bouncy?

"""
chaque nombre croissant est formé de :
1..1|2..2|3..3|4..4|5..5|6..6|7..7|8..8|9..9
9..9|8..8|7..7|6..6|5..5|4..4|3..3|2..2|1..1|0..0

On décompose un nombre en :
Pour les nombres croissants :
    - nbre de division k (de 1 à 9 )
    - tirages de k parmi 9 chiffres possibles

Pour les nombres décroissants :
    - nbre de division k (de 2 à 10 )
    - tirages de k parmi 10 chiffres possibles

"""
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
        
def C_n_k(n, k):
    num = fact(n)
    den = fact(k)*fact(n-k)
    return num//den


s1 = 0 # non-increasing-bouncy
s2 = 0 # non-decreasing-bouncy:
for l in range(1,101): # lg des nombres
    for k in range(1, min(9,l)+1): # nb de coupes
        s1 += C_n_k(l-1, k-1)*C_n_k(9, k)

    for k in range(2, min(10,l)+1): # nb de coupes
        s2 += C_n_k(l-1, k-1)*C_n_k(10, k)

print(s1+s2)
    
    
