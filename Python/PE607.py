##PE607


from math import *


e = [25*(2**0.5-1)] + [10]*5 + [25*(2**0.5-1)]
n = [1/10, 1/9, 1/8, 1/7, 1/6, 1/5, 1/10]

xi = 0
xf = 100/(2**0.5)

i0 = 0
i1 = atan(xf/e[0])
cpt = 0
ot, nt = 0, 1
while abs(ot-nt)>10**-15:
    cpt += 1
    ic = (i0+i1)/2
    xi = 0
    t = 0 
    for i in range(6):
#        print(i, ic, xi)
        li = e[i]/cos(ic)
        xi += e[i]*tan(ic)
        t += li*n[i]
        ic = asin(n[i]*sin(ic)/n[i+1])
    li = e[-1]/cos(ic)
    xi += e[-1]*tan(ic)
    t += li*n[-1]
#    print(i0, i1, xi,t)

    if xi > xf:
        i1 = (i0+i1)/2
    else:
        i0 = (i0+i1)/2

    ot, nt = nt, t

print('{:.12}'.format(t))


    
