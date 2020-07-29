import sys
from collections import defaultdict

# Needs more test cases written

def parse_data():
    data = sys.stdin.read().rstrip().split('\n')
    n,m = [int(x) for x in data[0].split()]
    costs = [0]*n

    weights = data[1:]

    for i in range(0,n):
        costs[i] = int(weights[i])

    G = defaultdict(list)

    #Give every node an edge to themselves
    for i in range(0,n):
        G[i].append(i)

    E = data[n+1:]
    for i in range(0,m):
        f1,f2 = [int(i) for i in E[i].split()]
        G[f1].append(f2)
        G[f2].append(f1)

    return G,costs,n

'''
DFS for a disconnected graph, which most graphs are in this case
'''
def DFSdisconnected(v,graph):
    V = len(graph)
    visited = [False]*V
    networks = []
    for i in range(V):
        if not visited[i]:
            networks.append(dfs(i,visited,graph))
    return networks


'''
creates a new network array and succesfully adds all nodes belonging to the network to it
'''
def dfs(i,visited,G):
    visited[i] = True
    network = [i]
    for x in G[i]:
        if not visited[x]:
            dfsHelper(x,network,visited,G)
    return network

def dfsHelper(x,network,visited,G):
    visited[x] = True
    network.append(x)
    for i in G[x]:
        if not visited[i]:
            dfsHelper(i,network,visited,G)

def calculate_cost(nodes,costs):
    sum = 0
    for n in nodes:
        sum += costs[n]
    if sum == 0:
        return "POSSIBLE"
    return "IMPOSSIBLE"


'''
BFS-like implemenation for calculating the cost of neighbours to each vertex in range 1 -> n
'''
def is_possible(G,costs,n):

    visited = [False]*n

    for vertex in range(n):
        if visited[vertex]:
            continue

        if vertex not in G.keys():
            if costs[vertex] != 0:
                return False
            continue

        total_sum = 0
        stack = [vertex]

        while stack:

            current_vertex = stack.pop()

            if visited[current_vertex]:
                continue

            total_sum += costs[current_vertex]
            visited[current_vertex] = True

            for n in G[current_vertex]:
                if not visited[n]:
                    stack.append(n)

        if total_sum != 0:
            return False

    return True

if __name__ == "__main__":
    G,costs,n = parse_data()

    if is_possible(G,costs,n):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

    networks = DFSdisconnected(0,G)
    for n in networks:
        str = calculate_cost(n,costs)
        if str == "IMPOSSIBLE":
            break

    [print(n) for n in networks]
