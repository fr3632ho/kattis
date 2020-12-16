import sys
from heapq import heappush, heappop


EPS = 10**-12

def cprod(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)

def slope_and_intercept(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return sys.maxsize, x1
    k = abs((y2 - y1)/((x2 - x1)*1.0))
    m = y1 - x1*k
    return k, m

def max_collinear_points(pts):
    n = len(pts)
    ans = 2*(n > 1) + 1*(n<= 1)
    if ans < 2:
        return ans

    Q = []
    seen = set()
    for a in pts:
        slopes = []
        for b in pts:
            if a == b or (a, b) in seen:
                continue

            seen.add((a, b))
            slope = slope_and_intercept(a, b)
            Q.append(slope)

    Q.sort()

    print Q
    i = 1
    while i < len(Q): # Window solution # O(n)
        count = 1

        while i < len(Q) and (abs(Q[i][0]-Q[i-1][0]) < EPS and abs(Q[i][1] - Q[i-1][1]) < EPS):
            i += 1
            count += 1
        i+=1
        ans = max(ans, count + 1) # +1 for coinciding point

    # Solution is O(n^2*log(n)), still too slow
    return ans


while True:
    n = int(raw_input())
    if not n:
        break

    points = []
    for _ in range(n):
        x, y = map(int, raw_input().split())
        points.append((x, y))

    print max_collinear_points(points)
