##Problem 66
##
##Consider quadratic Diophantine equations of the form:
##
##x2 – Dy2 = 1
##
##For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
##
##It can be assumed that there are no solutions in positive integers when D is square.
##
##By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
##
##32 – 2×22 = 1
##22 – 3×12 = 1
##92 – 5×42 = 1
##52 – 6×22 = 1
##82 – 7×32 = 1
##
##Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
##
##Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


# Pell Fermat equation :
# x**2 - N * y**2 = 1

def PellFermatSolution(N):
    """ Retourne le premier couple (x, y) qui vérifie l'équation de Pell-Fermat:
    x**2 - D * y**2 = 1
    Le calcul est mené selon la méthode de Chakravala."""

    # Premier triplet  de Chakravala (a, b, k) :    
    a = int(N**0.5)+1
    b = 1
    k = a**2 - N

    while k != 1:
        #print(a, b, k)
        # Recherche du triplet (m, 1, m**2 - N) :
        m = max(1, int(N**0.5)-2)
        while (a+b*m)%k!=0:
            m += 1
        a, b, k = (a*m + b*N)//abs(k), (a + b*m)//abs(k), (m**2 - N)//k


    return a, b


Dmax = 1
xmax = 1
for D in range(1, 1001):
    if int(D**0.5)**2 != D:
        x, y = PellFermatSolution(D)
        if x > xmax:
            Dmax = D
            xmax = x

print(Dmax, xmax)

