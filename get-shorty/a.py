from collections import defaultdict
from heapq import heappush, heappop
inf = 10**9
n,m=map(int,raw_input().split())
while n!=0 and m != 0:
    s,tar =0, n-1
    g=defaultdict(list)
    for _ in range(m):
        x,y,f=raw_input().split()
        f=float(f)
        x,y=map(int,(x,y))
        g[x].append((f,y))
        g[y].append((f,x))
    vis = set()
    dist = [inf for _ in range(n)]
    dist[s]=-1
    pq = [(dist[s],s)]
    while pq:
        f,node=heappop(pq)
        if node == tar:
            break
        if node in vis:
            continue
        vis.add(node)
        for f2, v in g[node]:
            alt_f = f*f2
            if alt_f < dist[v] and v not in vis:
                dist[v] = alt_f
                heappush(pq, (alt_f, v))
    print "{:.4f}".format(dist[tar]*-1)

    n,m=map(int,raw_input().split())
