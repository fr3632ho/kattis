EPS = 10**-12

def cprod(p1, p2, p3):
    return (p3[0]-p1[0])*(p2[1]-p1[1]) - (p2[0]-p1[0])*(p3[1]-p1[1])

def two_points_to_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y2-y1,x1-x2,x2*y1-y2*x1)

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def point_projection(line ,p):
    a,b,c=line
    x,y=p
    sq = (a**2 + b**2)*1.0
    return ((b*(b*x-a*y)-a*c)/sq,
            (a*(-b*x+a*y)-b*c)/sq)

def dist_to_line(p, line):
    p2 = point_projection(line, p)
    return dist(p,p2)

n = input()
for _ in range(n):
    x1, y1, x2, y2 = map(int, raw_input().split())
    line = two_points_to_line((x1, y1),(x2, y2))
    d = {}
    cities = input()
    m = []
    curr = 10**20
    for _ in range(cities):
        c, x, y = raw_input().split()
        x, y = int(x), int(y)
        d[(x, y)] = c
        distance = dist_to_line((x, y), line)
        print distance, c
        curr = min(curr, distance)
        m.append(((x, y), distance))

    s = []
    for i in m:
        if abs(i[1] - curr) <= EPS:
            s.append(d[i[0]])

    print " ".join(s)
