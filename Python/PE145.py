##Problem 145
##
##Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
##
##There are 120 reversible numbers below one-thousand.
##
##How many reversible numbers are there below one-billion (109)?



dico = set()
def sign(n):
    global dico
    rev = int(str(n)[::-1])
    a = n
    s = ''
    while a > 0:
        if a%10 + rev%10 >= 10:
            s = '1'+s
            a //= 10
            rev //= 10
            a += 1
        else:
            s = '0'+s
            a //= 10
            rev //= 10
    
    return s



def test(n):
    if n%10 != 0:
        rev = int(str(n)[::-1])
        nbre = rev + n
        for c in str(nbre):
            if c not in '13579':
                return False
        return True
    else:
        return False


##
##cpt = 0
##i = 1
##while i < 10**10:
##    if test(i):
##        cpt += 1
##        s = sign(i)
##        if s not in dico:
##            print(i, s)
##            dico.add(s)
##        i = 10**len(str(i))    
##    else:
##        i += 1
##
##print(len(dico))
##print(cpt)

"""
__ > 00 > 20
___ > 101 > 20*5
____ > 0000 > 20*30
_____ >  x101x (dernière retenue impossible) > 0
______ > 000000 > 20*(30**2)
_______ > 1010101 > 20*25*20*5
________ > 00000000 > 20*(30**3)

"""

s = 20
s += 20*5
s += 20*30
s += 0
s += 20*(30**2)
s += 20*25*20*5
s += 20*(30**3)

print(s)

