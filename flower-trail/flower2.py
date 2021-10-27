# Input
import sys
from collections import defaultdict
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

from heapq import heappush as push, heappop as pop
from collections import deque

def backward_edge_search():
    global parents, p, min_edges
    queue = deque()
    queue.append(p-1)
    vis = set()
    ret = 0
    while queue:
        node = queue.popleft()
        if node in vis: continue
        vis.add(node)
        for par in parents[node]:
            ret += min_edges[node][par]
            queue.append(par)
    return 2*ret

def dijkstra(G, source):
    global p, parents
    dist = [10000000000] * p
    visited = set()
    dist[source] = 0

    Q = [(0, source)]
    while Q:
        w, u = pop(Q)
        if u in visited: continue
        visited.add(u)
        for weight, v in G[u]:
            alt = dist[u] + weight
            if v not in visited:
                if alt < dist[v]:
                    dist[v] = alt
                    parents[v].clear()
                    parents[v].append(u)
                    push(Q, (alt, v))
                elif alt == dist[v]:
                    parents[v].append(u)

    return dist

p, t = nl()
graph = defaultdict(list)
INF = 10**6
min_edges = defaultdict(lambda : defaultdict(lambda : INF))
for edge in range(t):
    p1, p2, l  = nl()
    graph[p1].append((l, p2))
    graph[p2].append((l, p1))
    min_edges[p1][p2] = min_edges[p2][p1] = min(min_edges[p1][p2], min_edges[p2][p1], l)

parents = defaultdict(list) # adj list containing the parents with edges used in shortest path
dijkstra(graph, 0)
print(backward_edge_search())
