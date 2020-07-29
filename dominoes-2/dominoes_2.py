import sys
from collections import defaultdict

'''
Simple BFS applied. Searching through all neighbours of each given node and using the
visited vector to check if vertex i is already counted or not..
'''
def dominoe_effect(G,z,visited):
    stack = [z]
    count = 0
    while stack:

        current_vertex = stack.pop()

        if visited[current_vertex-1]:
            continue

        count += 1
        visited[current_vertex-1] = True

        for neighbour in G[current_vertex]:
            if not visited[neighbour-1]:
                stack.append(neighbour)

    return count

if __name__ == "__main__":
    data = []
    iterations = int(input().strip('\n'))
    for val in range(iterations):
        n,m,l = map(int,input().strip().split())

        G = defaultdict(list)
        for i in range(m):
            a,b = map(int, input().strip().split())
            G[a].append(b)

        total = 0
        visited = [False] * n
        for j in range(l):
            z = int(input().strip())
            total += dominoe_effect(G,z,visited)
        print(total)
