##Problem 80
##
##It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
##
##The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
##
##For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


def racineN(a, n):
    """Retourne la racine n-ième d'un nombre en 10 itérations"""
    x = 1
    for i in range(10):
        x = ((n-1)*x + a/(x**(n-1))) / n
    return x

##for i in range (2,10):
##    print(i)
##    print(racineN(i,2))
    

def racineC(a, nb):
    """Retourne la racine carree de a avec nb chiffres après la virgule,
    sous forme de str"""
    a = str(int(a * (100**nb)))
    x, y = 0, 0
    lg = len(a)
    if lg%2 != 0:
        a = '0' + a
        lg += 1

    while lg > 0:
        alpha = int(a[:2])
        a = a[2:]
        lg -= 2
        x = x*100 + alpha
        beta = 0
        while (10*y + beta + 1)**2 <= x:
            beta += 1
        y = y*10 + beta
    a = str(y)
    a = a[:-nb] + '.' + a[-nb:]
    return a

#print(racineC(2,63))
#print("1.414213562373095048801688724209698078569671875376948073176679737")

def sum100decim(a):
    rep = racineC(a,100)
    rep = ''.join(rep.split('.'))[:100]
    s = 0
    for c in rep:
        s += int(c)
    return s

print(sum100decim(2))

carres = [i**2 for i in range(1,11)]

s = 0
for i in range(1,101):
    if i not in carres:
        s += sum100decim(i)

print(s)




    


    
    
