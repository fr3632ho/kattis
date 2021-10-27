import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

n = ni()
circles = []
left = 100000
right = -10000
up = -10000
down = 10000
xmax, ymax = 0, 0
for c in range(n):
    x, y, r = nl()
    circles.append((x,y,r))
    #xmax, ymax = max(abs(x), xmax), max(abs(y), ymax)
    #left, right, up, down = min(left, xmax-r), max(right, xmax+r), max(up, ymax+r), min(down, y-r)

def within_circle(x, y):
    for _x, _y, r in circles:
        if ((x-_x)**2 + (y-_y)**2)**0.5 <=r:
            return True
    return False

import random

points = 2500000
area = 30**2
#area = (abs(left) + right)*(up + abs(down))
is_in = 0
for i in range(points):
    x = random.uniform(-10, 20);
    y = random.uniform(-10, 20);
    if within_circle(x, y):
        is_in += 1

print(area*is_in/points)
