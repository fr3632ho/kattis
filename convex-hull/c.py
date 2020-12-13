# Cross product, check sign => P := (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1)
# Check if p3 is on left side of off line between p1p2
def cprod(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0]) <= 0

# Gift wrapping algorithm, O(n^2) solution
def jarvis(points):
    hull = []
    point_on_hull = points[0]
    for p in points:
        if p[0] < point_on_hull[0]: point_on_hull = p

    i = 0
    output = []
    while True:
        hull.append(point_on_hull)
        endpoint = points[0]

        for j in range(len(points)):
            # Determine if point points[i] is on left side of line between
            # endpoint and point_on_hull
            # If such is the case, then set endpoint to points[i]
            if endpoint == point_on_hull or cprod(point_on_hull, endpoint, points[j]) < 0:
                endpoint = points[j]

        i += 1
        point_on_hull = endpoint
        output.append(point_on_hull)
        if point_on_hull == hull[0]:
            break

    return output

# O(nlogn) solution
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

while True:
    t = input()
    if t==0: break

    points = []

    for i in range(t):
        points.append(map(int, raw_input().split()))
    if len(points) > 1:
        G = hull(points)
    else:
        G = points

    print len(G)
    for x, y in G:
        print x, y
