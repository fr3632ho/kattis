
def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5



# Gift wrapping algorithm
def convex_hull(points):
    hull = []
    left_most = points[0]
    for p in points:
        if p[0] < left_most[0]: left_most = p

    print(left_most)
    i = 0



while True:
    t = int(input())
    if t==0: break

    points = []
    for i in range(t):
        points.append(tuple(map(int, input().split())))


    convex_hull(points)
