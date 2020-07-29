import sys
from collections import defaultdict
from heapq import heappush, heappop

inf = sys.maxsize

def calc_wait_time(P, t0, d, dist):
    if P == 0:
        if t0 >= dist:
            return t0 - dist
        else:
            return inf
    if t0 >= dist:
        return t0 - dist

    t = (dist - t0 + P - 1) // P
    return (t0 + t*P) - dist

def dijkstra(G, source, n):
    visited = [False]*n
    dist = [inf]*n
    dist[source] = 0

    Q = [(0, source)]
    while Q:
        time, u = heappop(Q)
        visited[u] = True
        #print(dist, "current node is", u)
        for node, t0, P, d in G[u]:
            if not visited[node]:
                weight = calc_wait_time(P, t0, d, time) + d + time

                #print("node:",node,"time:", time, "alt:", alt, "wait:", wait_time, "cost:", d)
                #print("alt:", alt, "dist[node]:", dist[node])
                if weight < dist[node]:
                    dist[node] = weight
                    heappush(Q, (weight, node))


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
            u, v, t0, P, d = map(int, input().split())
            graph[u].append((v, t0, P, d))

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
