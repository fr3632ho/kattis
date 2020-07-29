from collections import defaultdict
from heapq import heappush, heappop, heapreplace
import sys

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.nodes = [i for i in range(vertices)]
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, u, v, dist):
        self.edges[u].append(v),self.edges[v].append(u)
        self.distances[(u,v)] = dist

'''
Not sure if implemented correct, haven't tried out the implementation. If I
find time I will look over it and fix issues
'''
def dijkstra(G, source):
    visited = [False]*G.V
    distance = [sys.maxsize]*G.V
    distance[source] = 0

    Q = []
    heappush(Q, (0, source))

    while Q:

        # Take out minimal element from queue of nodes
        dist, u = heappop(Q)
        visited[u] = True

        # Loop through neighbours
        for n in G.edges[u]:
            alt = dist + G.distances[(u,n)]
            if not visited[n] and alt < distance[n]:
                distance[n] = alt
                heappush(Q,(alt, n))

    return distance


# END
