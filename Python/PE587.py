##Problem 587
##
##A square is drawn around a circle as shown in the diagram below on the left.
##We shall call the blue shaded region the L-section.
##A line is drawn from the bottom left of the square to the top right as shown in the diagram on the right.
##We shall call the orange shaded region a concave triangle.
##p587_concave_triangle_1.png
##
##It should be clear that the concave triangle occupies exactly half of the L-section.
##
##Two circles are placed next to each other horizontally, a rectangle is drawn around both circles, and a line is drawn from the bottom left to the top right as shown in the diagram below.
##p587_concave_triangle_2.png
##
##This time the concave triangle occupies approximately 36.46% of the L-section.
##
##If n circles are placed next to each other horizontally, a rectangle is drawn around the n circles, and a line is drawn from the bottom left to the top right, then it can be shown that the least value of n for which the concave triangle occupies less than 10% of the L-section is n = 15.
##
##What is the least value of n for which the concave triangle occupies less than 0.1% of the L-section?


from math import *


def Aire(x, y):
    a1 = (x + 1)*(y + 1)/2 # triangle gauche
    a2 = (0 - x) * 1 # rectangle droite
    a3 = atan(x/y) * 1 / 2 # aire disque
    a4 = (0 - x)*(0 - y)/2 # aire triangle
    return a1 + a2 - a3 - a4



L_section = 1*1 - pi*1**2/4


n = 0
R = 1

while R > 0.001:
    n += 1
    num = 2*(1 + 1/n) - sqrt(8/n)
    den = 2*(1 + 1/n**2)
    x_ = num/den - 1
    y_ = (x_ + 1)/n - 1
    R = Aire(x_, y_)/L_section
    
print(n)




