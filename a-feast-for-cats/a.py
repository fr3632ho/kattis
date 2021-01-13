from heapq import heappush, heappop

def find(p, a):
    root = a
    while root != p[root]: root = p[root]
    _p = a
    while a != root:
        _p = p[a]
        p[a] = root
        a = _p
    return root

def merge(p, a, b):
    p[find(p, a)] = p[find(p, b)]

def kruskal(edges):
    global m, c
    parents = [0]*c
    for i in range(c):
        parents[i] = i

    weight = e = 0
    while e < c-1:
        w, u, v = heappop(edges)
        x, y = find(parents, u), find(parents, v)
        if x != y:
            merge(parents, x, y)
            weight += w
            e += 1

    return weight


T = input()
for _ in range(T):
    m, c = map(int, raw_input().split())
    edges = []
    for _ in range(c*(c-1)//2):
        i, j, d = map(int, raw_input().split())
        heappush(edges, (d, i, j))

    if m < c:
        print "no"
        continue

    if kruskal(edges) + c <= m:
        print "yes"
    else:
        print "no"
