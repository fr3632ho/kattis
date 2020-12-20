from heapq import heappush, heappop

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def merge(parents, a, b):
    parents[find(parents, a)] = parents[find(parents, b)]

def find(p, a):
    root = a
    while root != p[root]:
        root = p[root]
    while a != root:
        _p = p[a]
        p[a] = root
        a = _p
    return root

def kruskal(edges, n):
    parents = [-1]*n
    i, e = 0, 0
    for i in range(n):
        parents[i] = i

    weight = 0
    while e < n-1:
        w, u, v = heappop(edges)
        i += 1
        x = find(parents, u)
        y = find(parents, v)
        if x != y:
            e += 1
            weight += w
            merge(parents, x, y)

    return weight


T = input()
for _ in range(T):
    m = input()

    vals = []
    for i in range(m):
        x, y = map(float, raw_input().split())
        vals.append((x, y, i))

    edges = []
    for a in vals:
        for b in vals:
            heappush(edges, (dist(a, b), a[2], b[2]))

    # Minimum Spanning tree using kruskals
    print kruskal(edges, m)
