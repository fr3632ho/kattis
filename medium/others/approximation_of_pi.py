import random
from decimal import *

"""
Approximation of PI with the help of points within a cirle & cube where the circles
edge is tangent with the edges of the box => the circels diameter is the same as the
side length of the cube!

Every (x,y) coordinate is randomly chosen.
"""
def approxPi(n):
    number_of_points_tot = 0
    number_of_points_circle = 0

    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        sq = x**2 + y**2
        if sq < 1:
            number_of_points_circle +=1
        number_of_points_tot +=1

    print((4*number_of_points_circle)/number_of_points_tot)


approxPi(10)
approxPi(100)
approxPi(1000)
approxPi(10000)
approxPi(100000)
approxPi(1000000)
approxPi(10000000)
approxPi(100000000)
