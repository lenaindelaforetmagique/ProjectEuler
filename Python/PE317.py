##Problem 317
##
##A firecracker explodes at a height of 100 m above level ground. It breaks into a large number of very small fragments, which move in every direction; all of them have the same initial velocity of 20 m/s.
##
##We assume that the fragments move without air resistance, in a uniform gravitational field with g=9.81 m/s2.
##
##Find the volume (in m3) of the region through which the fragments move before reaching the ground. Give your answer rounded to four decimal places.


"""
somme Forces = m*a

->
x_theta(t) = x0 + v0*cos(theta)*t
y-theta(t) = y0 + v0*sin(theta)*t - g*t**2/2

Enveloppe : dx/dt*dy/dtheta=dy/dt*dx/dtheta
-> v0 = g*t*sin(theta)

1 + cot(theta)**2 = 1/sin(theta)**2

Y(X) = (y0 + v0**2/(2*g)) - X**2*g/(2*v0**2)
"""

from math import pi
v0 = 20
g = 9.81
y0 = 100

a = -g/(2*v0**2)
c = (y0 + v0**2/(2*g))

Xf = (-c/a)**0.5

Aire = a*Xf**3/3 + c*Xf
Msta = a*Xf**4/4 + c*Xf**2/2
xG = Msta/Aire

Vol = Aire * 2*pi*xG

print(Vol)
