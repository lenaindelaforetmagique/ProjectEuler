##Problem 169
##
##Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.
##
##For example, f(10)=5 since there are five different ways to express 10:
##
##1 + 1 + 8
##1 + 1 + 4 + 4
##1 + 1 + 2 + 2 + 4
##2 + 4 + 4
##2 + 8
##
##What is f(10**25)?


NB = 10**25


def f(n):
    """iteratif :
    on remarque que sur un nombre en binaire :
    - ajouter 1 à la fin(=2n+1) ne change rien
    - ajouter 0 à la fin(=2n) peut s'écrire:
       - (n)0 > on compte donc f(n)
       - ou bien (n-1)2 > on compte donc f(n-1)
       
    on garde en mémoire Na(=f(n-1)) et Nb(=f(n)) """
    s = bin(n)[2:]
    p = 1
    t = 1
    Na = 0
    Nb = 1
    
    for i, c in enumerate(s):
        if c == "0":
            Nb = Nb + Na
        else:
            Na = Nb + Na

    return Nb

def test(n):
    """recursif"""
    if n==1 or n == 0:
        return 1
    elif n%2 == 0:
        return nb(n//2)+nb(n//2-1)
    else:
        return nb((n-1)//2)



print(f(10**25))








