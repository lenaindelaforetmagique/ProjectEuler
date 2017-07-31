##Problem 94
##
##It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
##
##We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
##
##Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

"""
A = b*h/2
    b = (n +- 1)
    h = sqrt(n**2 - ((n +- 1)/2)**2)

-> 4*A = (n +- 1) * sqrt(3*n**2 -+ 2*n - 1)

A est entier, (n +- 1) est entier donc sqrt(...) est rationnel ou entier.
    => 3*n**2 -+ 2*n - 1 est un carré:
        X**2 = 3*n**2 -+ 2*n - 1
    <=> 3*X**2 = (3*n -+ 1)**2 - 4

La dernière ligne est simplifiable par 4 car :
    - si n est pair, 4*A ne peut etre pair que si sqrt(...) l'est ;
    - si n est impair, (3*n -+ 1) est pair donc X aussi.

    <=> 3*(X/2)**2 = ((3*n -+ 1)/2)**2 - 1
    <=> x**2 - 3*y**2 = 1 (Equation de Pell-Fermat)
"""

def nextChakravala(D, x0, y0, x1, y1):
    x2 = x0*x1 + D*y0*y1
    y2 = x0*y1 + y0*x1
    return x2, y2

x0, y0 = 2, 1 # première solution de Pell pour D = 3
x1, y1 = x0, y0
D = 3
somme = 0

P = 0
while P < 10**9:
    somme += P
    x1, y1 = nextChakravala(D, x0, y0, x1, y1)
    X = 2*y1
    if (2*x1 + 1)%3 == 0:
        n = (2*x1 + 1) // 3
        P = 3*n + 1
    else:
        n = (2*x1 - 1) // 3
        P = 3*n - 1
    
print(n,somme)


    
