EPS = 10**-9

def make_line(p1, p2):
    b = p2[0] - p1[0]
    a = p1[1] - p2[1]
    c = -(p2[0]*p1[1] - p2[1]*p1[0])
    return (a, b, c)

def dist_to_line(line, p):
    a = line[0]*p[0] + line[1]*p[1] + line[2]
    if a<0: a*=-1
    b = (line[0]*line[0] + line[1]*line[1])**0.5
    return (1.0*a)/(b*1.0)

n = input()
for _ in range(n):
    x1, y1, x2, y2 = map(int, raw_input().split())
    line = make_line((x1, y1),(x2, y2))
    d = {}
    cities = input()
    m = []
    curr = 10**20
    for _ in range(cities):
        c, x, y = raw_input().split()
        x, y = int(x), int(y)
        d[(x, y)] = c
        distance = dist_to_line(line, (x, y))
        curr = min(curr, distance)
        m.append(((x, y), distance))

    s = []
    for i in m:
        if i[1]==curr:
            s.append(d[i[0]])

    print " ".join(s)
