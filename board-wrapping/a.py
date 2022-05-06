'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]
def nf(): return [float(tok) for tok in inp().split()]

sys.setrecursionlimit(1000000) # default is 1000.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def __add__(self, o):                    
        self.x = self.x + o.x
        self.y = self.y + o.y
        return Point(self.x, self.y)

    def __sub__(self, o):
        self.x = self.x - o.x
        self.y = self.y - o.y
        return Point(self.x, self.y)

    def __mul__(self, factor):
        self.x = self.x * factor 
        self.y = self.y * factor
        return Point(self.x, self.y)

    def __div__(self, o):
        self.x = self.x / o.x
        self.y = self.y / o.y
        return Point(self.x, self.y)

    def to_tuple(self):
        return (self.x, self.y)    

def calc_poly_area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]        
        area += x1*y2 - x2*y1
    return abs(area/2.0)

from math import cos, sin, radians

def rotate_rectangle(rectangle, degree):
    out = []
    for x, y in rectangle:
        x1 = x * cos(radians(v)) - y * sin(v)
        y1 = x * sin(radians(v)) - y * cos(v)
        out.append((x1, y1))
    return out        


def cprod(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0]) <= 0

def hull(pts):
    n = len(pts)
    pts.sort()
    U = [pts[0], pts[1]]
    L = [pts[-1], pts[-2]]
    for i in range(n-2, -1, -1):
        while len(L) > 1 and cprod(L[-2], L[-1], pts[i]):
            L.pop()
        L.append(pts[i])

    for j in range(2, n):
        while len(U) > 1 and cprod(U[-2], U[-1], pts[j]):
            U.pop()
        U.append(pts[j])

    U.pop()
    L.pop()
    hull = U + L
    if hull[0] == hull[-1]:
        hull.pop()
    return hull

#print(calc_poly_area([(0,0), (1,0), (1,1), (0,1)]))

# formula zi = zc +- u +- p
# u = (a*cos(v),a*sin(v))
# p = (b*cos(v),-b*sin(v))
# a := w/2
# b := h/2
from math import pi
t = ni()
for _ in range(t):
    n = ni()
    board_area = 0
    points = []
    for _ in range(n):
        x, y, w, h, v = nf()     
        v = v/180.0*pi
        board_area += w*h
        h1, w1, p1 = Point(sin(v), cos(v)), \
                     Point(-cos(v), sin(v)), \
                     Point(x, y)
        h1 = h1*(h/2.0)
        w1 = w1*(w/2.0)

        points.append((p1 + h1 + w1).to_tuple())
        points.append((p1 + h1 - w1).to_tuple())
        points.append((p1 - h1 + w1).to_tuple())
        points.append((p1 - h1 - w1).to_tuple())                        
    
    pts = hull(points)
    tot_area = calc_poly_area(pts)
    print(tot_area)
    print(board_area)
    res = (board_area / tot_area)*100
    print(f'{res:.1f} %')    

    