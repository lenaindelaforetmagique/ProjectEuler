##Problem 93
##
##By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
##
##For example,
##
##8 = (4 * (1 + 3)) / 2
##14 = 4 * (3 + 1 / 2)
##19 = 4 * (2 + 3) − 1
##36 = 3 * 4 * (2 + 1)
##
##Note that concatenations of the digits, like 12 + 34, are not allowed.
##
##Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
##
##Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

Resultats = {}


def calcule(liste, clef):
    l = len(liste)
#    print(t, l)
    if l == 1:
        Resultats[clef].add(liste[0])
    else:
        for i in range(l-1):
            for j in range(i+1, l):
                t = liste[:]
                vj = t.pop(j)
                vi = t.pop(i)
                calcule(t + [vi + vj], clef)
                calcule(t + [vi * vj], clef)
                calcule(t + [max(vi,vj) - min(vi,vj)], clef)
                if vj != 0:
                    calcule(t + [vi/vj], clef)
                if vi != 0:
                    calcule(t + [vj/vi], clef)



for a in range(7):
    for b in range(a+1, 8):
        for c in range(b+1, 9):
            for d in range(c+1, 10):
                liste = [a, b, c, d]
                clef = a*1000 + b*100 + c*10 + d
                Resultats[clef] = set()
                calcule(liste, clef)

cptmax = 0

for clef in Resultats:
    cpt = 0
    while cpt+1 in Resultats[clef]:
        cpt += 1

    if cpt > cptmax:
        cptmax = cpt
        abcd = clef

print(abcd, cptmax)
#print(Resultats[abcd])

    


                
                
        
