import sys
from collections import defaultdict
from heapq import heappush, heappop

inf = sys.maxsize

def dijkstra(G, source, n):
    dist = [inf] * n
    visited = [False] * n
    dist[source] = 0

    Q = [(0, source)]
    while Q:
        w, u = heappop(Q)
        visited[u] = True

        for weight, v in G[u]:
            alt = dist[u] + weight
            if not visited[v] and alt < dist[v]:
                dist[v] = alt
                heappush(Q, (alt, v))

    return dist


def main():
    n, m, q, s = map(int, input().split())
    while True:

        # End of file
        if n == 0:
            break

        # construct graph
        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((w, v))

        # use dijkstra
        distances = dijkstra(graph, s, n)

        # answer queries
        for _ in range(q):
            q = int(input())
            cost = distances[q]
            if cost == inf:
                print("Impossible")
            else:
                print(cost)

        n, m, q, s = map(int, input().split())

        if n == 0:
            break
        print()


if __name__ == '__main__':
    main()
