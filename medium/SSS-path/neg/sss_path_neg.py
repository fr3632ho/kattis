import sys
from collections import deque, defaultdict

inf = sys.maxsize

def DFS(G, u, visited):
    if not visited[u]:
        visited[u] = True
        for v, w in G[u]:
            DFS(G, v, visited)

'''
Shortest Path Faster Algorithm implemented with some modifications
to allow labeling of nodes part of negative cycles.

This implementation improved execution time by a factor ~3.

By keeping track of the amount of relaxations performed for each edge,
we can then use a DFS to lable the connected components as part of the cycle.
'''
def SPFA(G, s, n):
    dist, visits = [inf]*n, [0]*n
    dist[s] = 0

    in_queue = [False] * n
    in_queue[s] = True
    Q = deque([s])
    while Q:
        u = Q.pop()
        in_queue[u] = False
        visits[u] += 1

        if visits[u] < n:
            for v, w in G[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if not in_queue[v]:
                        Q.appendleft(v)
                        in_queue[v] = True

    visited = [False]*n
    for v in range(n):
        if visits[v] == n:
            DFS(G, v, visited)

    for u in range(n):
        if visited[u]:
            dist[u] = -inf

    return dist



def main():
    n, m, q, s = map(int, input().split())
    while True:

        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((v, w))

        # perform SPFA
        distances = SPFA(graph, s, n)

        for _ in range(q):
            query = int(sys.stdin.readline())

            cost = distances[query]
            if cost == -inf:
                print("-Infinity")
            elif cost == inf:
                print("Impossible")
            else:
                print(cost)

        n, m, q, s = map(int, input().split())
        if n == 0:
            break
        print()

if __name__ == "__main__":
    main()
