from math import sqrt, pi, ceil, atan

l = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

slope = -1
p = a = b = c = -1 # a := distance to origo x-axis, b := distance to origo y-axis, c := b, p := distance to origo
if x1 - x2 == 0: # vertical straight line
    p = abs(x1)
elif y1 - y2 == 0: # horizontal straight line
    p = abs(y1)
else: # Other, y = kx+m
    k = (y1 - y2)/(x1 - x2)
    m = y1 - k*x1
    a = k
    b = -1
    c = m # Line expressed in standard form! Ax + By + C = 0
    p = abs(c) / sqrt(a**2 + b**2)

r = sqrt(l/pi)
if p >= r: # Distance to wall is greater than needed radius
    print(ceil(r))
else:
    r = ceil(r)
    area = -1
    while r < 200:
        h = p
        b = (r**2 - h**2)**0.5
        if h == 0:
            angle = pi / 2
        if h > 0:
            angle = atan(b / h)
        area = (pi * r*r) + (b * h) - (angle * r * r)
        if area >= l:
            print(r)
            break

        r += 1
