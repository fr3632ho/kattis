from collections import defaultdict, deque
from heapq import heappush, heappop

inf = 10**10
TAR = 1
def dijk1(G):
    # should return a dist list
    dist = [inf for _ in range(n)]
    dist[1] = 0
    visited = set()
    queue = [(dist[1], 1)]
    while queue:
        d, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        for v, w in G[node]:
            if v not in visited:
                alt = d + w
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(queue, (alt, v))
    return dist

n,m = map(int, raw_input().split())
g = defaultdict(list)
edges = []
for i in range(m):
    ai,bi,weight = map(int, raw_input().split())
    #print ai, bi, weight
    g[ai].append((bi, weight))
    g[bi].append((ai, weight))
    edges.append((ai,bi,weight))

dist = dijk1(g)
g2 = defaultdict(list)
for u, v,w in edges:
    if dist[u] + w == dist[v]: continue
    g2[v].append(u)

for u,v,w in edges:
    if dist[v] + w == dist[u]: continue
    g2[u].append(v)

# for k, v in g2.items():
#     print k, v

parents = [i for i in range(n)]
parents[0] = -1
visited = set([0])
Q = deque([0])
while Q:
    node = Q.popleft()

    for v in g2[node]:
        if v not in visited:
            visited.add(v)
            parents[v] = node
            Q.append(v)
#print parents, "...."
if parents[1]==1 or len(g2[0]) < 1:
    print "impossible"
    exit(0)


out = [str(TAR)]
prev = parents[TAR]
while parents[prev] != -1:
    out.append(str(prev))
    prev = parents[prev]
print len(out)+1,0, " ".join(out[::-1])
