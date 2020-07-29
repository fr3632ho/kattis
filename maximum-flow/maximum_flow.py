import sys
from collections import deque

'''Implementation of the push-relabel algorithm,
(Goldberg-Tarjan's Maximum flow).
'''

def push(C, excess_edges, excess, flow, u, v):
    d = min(excess[u], C[u][v] - flow[u][v]) # Push the maximum available flow
    excess[u] -= d
    excess[v] += d
    flow[u][v] += d
    flow[v][u] -= d
    if d and excess[v] == d:
        excess_edges.push



def relabel(u):
    pass

def discharge(u):
    pass

def max_flow():
    pass

def add_edges(edges, capacities, u, v, c):
    if capacities[u][v]:
        edges.append((u, v))
        capacities[u][v] += c
    else:
        capacities[u][v] = c

def pretty_print(M):
    print()
    for row in M:
        print(row)
    print()

def main():
    n, m, s, t = map(int, sys.stdin.readline().split())

    print('source: {}, sink: {}\nn: {}, m: {}\n'.format(s, t, n, m))

    # Capacities
    capacities = [[0 for _ in range(n)] for _ in range(n)]
    flow = [[0 for _ in range(n)] for _ in range(n)]
    edge_list = []
    excess = [0 for _ in range(n)]

    # Edges
    for e in range(m):
        u, v, c = map(int, sys.stdin.readline().split())
        print('%d --(%d)--> %d' % (u, c, v))
        add_edges(capacities, edge_list, excess, u, v, c)

    pretty_print(capacities)













if __name__ == "__main__":
    main()
