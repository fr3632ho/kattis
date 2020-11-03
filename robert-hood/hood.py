import sys
from math import sqrt

def distance(i,j):
    return sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

#Returns hull in counter-clockwise order.
#pts is a list of tuples, each tuple is (x,y).
def hull(pts):
    n = len(pts)
    pts.sort()
    U = []
    L = []
    for i in range(n):
        while len(L)>1 and ccw(L[-2],L[-1],pts[i]) <= 0: L.pop()
        L.append(pts[i])
    for i in range(n-1,-1,-1):
        while len(U)>1 and ccw(U[-2],U[-1],pts[i]) <= 0: U.pop()
        U.append(pts[i])
    L.pop()
    U.pop()
    if len(L) == len(U) == 1 and L[0] == U[0]: return L
    return L+U

C = int(input())
shots = []
for _ in range(C):
    x, y = map(int, input().split())
    shots.append((x, y))

hull = hull(shots)
curr_max = 0
max_index = -1
p = hull[0]
for i in range(len(hull)):
    q = hull[i]
    if distance(p, q) > curr_max:
        curr_max = distance(p, q)
        max_index = i

for i in range(len(hull)):
    _p = hull[i]
    while distance(_p, hull[(max_index + 1) % len(hull)]) > distance(_p, hull[max_index]):
        max_index += 1
        max_index %= len(hull)

    _q = hull[max_index]
    if distance(_p, _q) > curr_max:
        curr_max = distance(_p, _q)

print(curr_max)
