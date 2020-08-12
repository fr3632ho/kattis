import sys
from collections import defaultdict, deque

no = "IMPOSSIBLE"
WALL = "#"
FIRE = "F"
START = "J"
SPACE = "."
start_index = -1
INF = 10000000

def escape_dists_fire(G, start, exits, distances):
    visited = dict() # Replace with dict
    Q = deque([(start, 1)])
    while Q:
        u, dist = Q.pop()

        if u in visited:
            continue

        if u in exits:
            if u not in distances:
                distances[u] = INF
            distances[u] = min(distances[u], dist)


        visited[u] = 1
        for n in G[u]:
            if n not in visited:
                Q.appendleft((n, dist + 1))

def escape_J(G, start, exits, distances):
    visited = dict()
    queue = deque([(start, 1)])
    minimum = INF
    while queue:
        u, dist = queue.pop()

        if u in visited:
            continue

        if u in exits:
            if u not in distances:
                distances[u] = dist
                minimum = dist
            elif distances[u] > dist:
                distances[u] = dist
                minimum = dist
                continue

        visited[u] = 1
        for n in G[u]:
            if n not in visited:
                queue.appendleft((n, dist + 1))

    return minimum

def is_exit(x, y, w, h):
    return x == 0 or x == w-1 or y == 0 or y == h-1

def construct_graph()


def add_neighbours(G, i, w, h, M, fires, exits):
    global start_index
    '''
    Setup graph with correct neighbours
    '''
    y, x = i // w, i % w
    curr = M[y][x]

    if curr == WALL:
        return

    if curr == FIRE:
        fires.add(i)

    if curr == SPACE or curr == START:
        if is_exit(x, y, w, h):
            exits.add(i)

    n = []
    if x > 0 and M[y][x - 1] != WALL: # Left neighbour
        n.append(i - 1)

    if (x < w - 1) and M[y][x + 1] != WALL: # Right neighbour
        n.append(i + 1)

    if y > 0 and M[y - 1][x] != WALL: # Neighbour up
        n.append(i - w)

    if y < h - 1 and M[y + 1][x] != WALL: # Neighbour down
        n.append(i + w)

    if curr == START:
        start_index = i

    G[i] = n


def main():
    h, w = map(int, input().split())
    m = []
    for i in range(h): # If I do a BFS here and construct the graph as I go that would be faster
        m.append(input())

    G = defaultdict(list)
    fires = set()
    exits = set()
    for i in range(w*h):  # O(N^2)
        add_neighbours(G, i, w, h, m, fires, exits)

    if not exits: # No exits present
        print(no)
        return
    elif start_index in exits: # Edge case if START is one of the exits
        print(1)
        return

    # print(fires)
    # print("start: {}, exits:{}, in exits: {}".format(start_index, exits, start_index in exits))

    d1 = dict()
    for f in fires: #O(N * (V+E))
        escape_dists_fire(G, f, exits, d1)

    minimum = escape_J(G, start_index, exits, d1)
    if minimum == INF:
        print(no)
    else:
        print(minimum)


if __name__ == "__main__":
    main()
