'''
For each point (x, y) extend a horizontal line to the right
Each intersection of the line with the polygon will help determine if the point is
inside or outside the polygon.

Odd number of intersections => inside
Even number of intersections => outside
No intersections => outside
cross product between two points == 0 => on line segment
'''
import operator
INF = 100000000
EPS = 10**-12

def cprod(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1] - p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])

while True:
    n = int(raw_input())
    if n == 0:
        exit(0)

    polygon = []
    for _ in range(n):
        polygon.append(map(int, raw_input().split()))

    m = int(raw_input())
    for _ in range(m):
        bound = False
        count = 0
        x, y = map(int ,raw_input().split())
        p = (x,y)
        for i in range(n):
            j = (i+1) % n
            p1, p2 = polygon[i], polygon[j]
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            if p1[0] <= x < p2[0]:
                if cprod(p1,p2,p) == 0:
                    bound = True
                    break
                if cprod(p1,p2,p) < 0:
                    count += 1
            if p1[0] == x == p2[0]:
                if p1[1] <= y <= p2[1] or p2[1] <= y <= p1[1]:
                    bound = True
                    break
        if bound:
            print "on"
        elif count%2:
            print "in"
        else:
            print "out"
