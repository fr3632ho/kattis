import sys
from collections import deque

NO = "IMPOSSIBLE"
WALL = "#"
FIRE = "F"
START = "J"
SPACE = "."
INF = 10000000
R, C = -1, -1

def is_exit(u):
    y, x = u
    return x == 0 or x == C - 1 or y == 0 or y == R - 1

def add_neighbours(G, u, M):
    y, x = u
    n = []

    if x > 0 and M[y][x - 1] != WALL:
        n.append((y, x - 1))
    if x < C - 1 and M[y][x + 1] != WALL:
        n.append((y, x + 1))
    if y > 0 and M[y - 1][x] != WALL:
        n.append((y - 1, x))
    if y < R - 1 and M[y + 1][x] != WALL:
        n.append((y + 1, x))

    return n

def construct_graph(G, start, fires, exits, distances, M):
    '''
    Construct graph with the help of a BFS and add possible exits and possible fires
    to each set. Also update distances!
    '''
    blacklist = set()
    visited = set()
    Q = deque([(start, 1)])
    while Q:
        (y, x), dist = Q.pop()

        if (y, x) in visited:
            continue

        if M[y][x] == WALL:
            blacklist.add((y, x))
            continue

        if M[y][x] == FIRE:
            fires.add((y, x))

        if is_exit((y, x)): # Set distance
            if (y, x) not in distances:
                distances[(y, x)] = dist
            else:
                distances[u] = min(distances[u], dist)
            exits.add((y, x))

        visited.add((y, x))
        G[(y, x)] = add_neighbours(G, (y, x), M)
        for n in G[(y, x)]:
            if n not in visited:
                Q.appendleft((n, dist + 1))

def spread_fire(G, start, exits, distances):
    visited = set()
    Q = deque([(start, 1)])
    while Q:
        u, dist = Q.pop()

        if u in visited:
            continue

        if u in exits:
            if u not in distances: # Already been deleted
                continue
            if distances[u] >= dist: # remove if fire will get there faster than J
                del distances[u]

        visited.add(u)
        for n in G[u]:
            if n not in visited:
                Q.appendleft((n, dist + 1))

def main():
    global R, C
    R, C = map(int, input().split())
    m = []
    start_index = (-1, -1)
    fires, exits = set(), set()
    for r in range(R): # O(n^2 operation)
        row = input()
        m.append(row)
        for c in range(C):
            if row[c] == START:
                start_index = (r, c)
            if row[c] == FIRE:
                fires.add((r, c))
            if row[c] != WALL and is_exit((r, c)):
                exits.add((r, c))

    print(fires)
    print(exits)
    # graph, distances = dict(), dict()
    # construct_graph(graph, start_index, fires, exits, distances, m)
    #
    # for f in fires:
    #     spread_fire(graph, f, exits, distances)
    #
    # if len(distances) == 0:
    #     print(NO)
    # else:
    #     print(min(distances.values()))

if __name__ == "__main__":
    main()
