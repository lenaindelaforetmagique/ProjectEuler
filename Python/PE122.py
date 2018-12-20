# Problem 122
##
# The most naive way of computing n15 requires fourteen multiplications:
##
# n × n × ... × n = n15
##
# But using a "binary" method you can compute it in six multiplications:
##
# n × n = n2
# n2 × n2 = n4
# n4 × n4 = n8
# n8 × n4 = n12
# n12 × n2 = n14
# n14 × n = n15
##
# However it is yet possible to compute it in only five multiplications:
##
# n × n = n2
# n2 × n = n3
# n3 × n3 = n6
# n6 × n6 = n12
# n12 × n3 = n15
##
# We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
##
# For 1 ≤ k ≤ 200, find ∑ m(k).

from time import time
from math import log

t = [1] + [int(log(i - 1) / log(2)) + 2 for i in range(2, 201)]
# print(sum(t))
# for i in range(2,33+1):
##    print(i, int(log(i-1)/log(2))+2)


def testnaif(n):
    """expression binaire de l'exposant
    somme des (puissances_de_2 - 1)
    +
    (nombre de 1)-1
    """
    t = []
    while n > 0:
        t.append(n % 2)
        n //= 2
    s = 0
    for i, v in enumerate(t):
        if v == 1:
            s += i
    s += sum(t) - 1
    return s


t = max([testnaif(i) for i in range(2, 201)])
print(t)  # profondeur maxi pour la plage avec méthode naive : 28


Dico = {}
mem = set()


def dvlp(t, prof):
    global Dico
    global mem
    global pmax
    if prof <= pmax and tuple(t) not in mem:
        l = len(t)
        for i in range(l):
            v = t[-1] + t[i]
            if v not in t and v < 201:
                if v not in Dico:
                    Dico[v] = prof + 1
                else:
                    Dico[v] = min(Dico[v], prof + 1)
                dvlp(t + [v], prof + 1)
                mem.add(tuple(t + [v]))


for pmax in range(1, 11):
    t0 = time()
    Dico = {}
    mem.clear()
    dvlp([1], 0)
    print("Prof max {} : {} valeurs. {} s".format(pmax, len(Dico), time() - t0))

s = 0
for v in Dico.keys():
    s += Dico[v]
print(s)

# tests brutaux
# Prof max 1 : 3 valeurs. 2.6941299438476562e-05 s
# Prof max 2 : 6 valeurs. 5.1021575927734375e-05 s
# Prof max 3 : 11 valeurs. 0.00011992454528808594 s
# Prof max 4 : 20 valeurs. 0.0007691383361816406 s
# Prof max 5 : 35 valeurs. 0.0030128955841064453 s
# Prof max 6 : 61 valeurs. 0.01812911033630371 s
# Prof max 7 : 104 valeurs. 0.13182282447814941 s
# Prof max 8 : 168 valeurs. 1.1705989837646484 s
# Prof max 9 : 198 valeurs. 12.362097024917603 s
# Prof max 10 : 199 valeurs. 207.2186939716339 s
