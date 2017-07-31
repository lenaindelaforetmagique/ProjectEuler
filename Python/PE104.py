##Problem 104
##
##The Fibonacci sequence is defined by the recurrence relation:
##
##    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
##
##It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
##
##Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

from time import time
from math import *



fa = 1
fb = 1
i = 1

droite = ''
gauche = ""

t0 = time()
pandi = "123456789"
pasOK = True

while pasOK:
    droite = str(fb % 10**9)
    if ''.join(sorted(droite)) == pandi:
        #pasOK = False
        gauche = str(fb // (10**(int(log10(fb))-8)))
        if ''.join(sorted(gauche)) == pandi:
            pasOK = False

    fb, fa = fb + fa, fb
    i += 1

print(i,time()-t0)

#while ''.join(sorted(a[-9:])) != "123456789" or ''.join(sorted(a[:9])) != "123456789":
#a = str(fb)
