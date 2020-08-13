import sys
from collections import defaultdict, deque

def add_edge(G, u, v):
    G[u].append(v), G[v].append(u)

def add_source(u, not_visited, queue):
    not_visited.remove(u)
    queue.appendleft((0, u))

def main():
    # Output the ID of the movie in the collection with the highest Horror Index.
    # In case of a tie, output the movie with the lowest ID.

    N, H, L = map(int, input().split())
    not_visited = set(range(N)) # This can be sped up
    Q = deque([])
    for u in map(int, input().split()):
        # Each horror film acts as a source for a BFS
        add_source(u, not_visited, Q)

    G = defaultdict(list)
    for _ in range(L):
        u, v = map(int, input().split())
        add_edge(G, u, v)

    hi, id = -1, -1
    while Q: # BFS
        c, i = Q.pop()

        if c > hi or (c == hi and i < id):
            hi, id = c, i

        for n in G[i]:
            if n in not_visited:
                not_visited.remove(n)
                Q.appendleft((c + 1, n))

    if not not_visited:
        return id
    else:
        return min(not_visited) # All will be set as INFINITY, so min index works


if __name__ == "__main__":
    print(main())
