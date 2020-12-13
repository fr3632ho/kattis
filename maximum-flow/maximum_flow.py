import sys
from collections import defaultdict, deque
from heapq import heappush, heappop

def bfs(graph, s, t, parents):
    Q = deque([(s, sys.maxsize)]) # BFS PART OF THE ALGORITHM
    while Q:
        u, curr_flow = Q.popleft()
        for n in graph[u].keys():
            if parents[n] == -1 and graph[u][n] > 0: # Capacity greater than 0
                parents[n] = u
                new_flow = min(graph[u][n], curr_flow)
                if n == t:
                    return new_flow # augmented path found
                Q.append((n, new_flow))
    return 0

def karp(graph, s, t):
    global N
    flow = 0
    while True:
        parents = [-1]*N
        df = bfs(graph, s, t, parents)
        if df == 0:
            break
        flow += df
        cur = t
        while cur != s:
            prev = parents[cur]
            graph[cur][prev] += df
            graph[prev][cur] -= df
            cur = prev

    return flow

# Capacity can be 2**31 => must optimize flow faster
N, M, s, t = map(int, input().split())
graph = defaultdict(dict)
edges = defaultdict(int) # Need to keep track of all addeed edges even if multiple are between the same vertices
for _ in range(M):
    u, v, c = map(int, input().split())
    if (u, v) in edges:
        graph[u][v] += c
        graph[v][u] += 0
    elif (v, u) in edges:
        graph[u][v] = c
        graph[v][u] += 0
    else:
        graph[u][v] = c
        graph[v][u] = 0

    edges[(u, v)] += c

max_flow = karp(graph, s, t)
used = []
for k, val in edges.items():
    u, v = k
    if graph[u][v] != val:
        heappush(used, "{} {} {}".format(u, v, graph[v][u]))

print("{} {} {}".format(N, max_flow, len(used)))

while used:
    print(heappop(used))
