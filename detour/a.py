from collections import defaultdict
from heapq import heappush, heappop

inf = 10**10
def dijkstra(G,w):
    visited = set()
    queue = [(0,0,0)]
    parents = [i for i in range(n)]
    dist = [0 for _ in range(n)]
    dist[0] = 0
    while queue:
        d, node, p = heappop(queue)
        d *=-1
        if node in visited:
            continue
        parents[node]=p
        visited.add(node)
        for vi in G[node]:
            alt = d + w[node][vi]
            if vi not in visited and (w[node][vi] < inf and alt > dist[vi]):
                dist[vi] = alt
                heappush(queue, (-alt,vi, node))
    if 1 not in visited:
        return  [], -1
    p = [1]
    parents[0] = -1
    prev = parents[1]
    d = 0
    j = 1
    while prev != -1:
        p.append(prev)
        d += w[p[j]][p[j-1]]
        j+=1
        prev = parents[prev]
    return p[::-1],d

n,m = map(int, raw_input().split())
g = defaultdict(set)
w = [[-1 for i in range(n)] for j in range(n)]
for i in range(m):
    ai,bi,weight = map(int, raw_input().split())
    w[ai][bi] = weight
    w[bi][ai] = weight
    g[ai].add(bi)
    g[bi].add(ai)

path, distance = dijkstra(g,w) # this is guaranteed
# Perform Yen's Algorithm
A = [(path,distance)]
for k in range(1,n):
    curr_weight = -1
    curr_path = A[-1][0]
    min_path = (curr_path, A[-1][1])
    for i in range(1, len(curr_path)):
        curr_weight = w[path[i-1]][path[i]]
        w[curr_path[i-1]][curr_path[i]] = inf
        p2, d2 = dijkstra(g,w)
        w[path[i-1]][path[i]] = curr_weight
        if min_path[1] > d2:
            min_path = (p2,d2)
        if 0<= d2 < distance:
            print len(path), " ".join(str(i) for i in path)
            exit(0)
    if min_path == A[-1]:
        break
    A.append(min_path)

print "impossible"
