import sys
from collections import defaultdict, deque

no = "IMPOSSIBLE"
WALL = "#"
FIRE = "*"
START = "@"
SPACE = "."
start_index = -1
INF = 10000000

def escape_dists(G, start, n, exits, distances):
    visited = [False]*n
    Q = deque([(start, 1)])
    while Q:
        u, dist = Q.pop()
        if visited[u]:
            continue

        if u in exits:
            if u not in distances:
                distances[u] = INF
            #print(u, "is exit")
            distances[u] = min(distances[u], dist)

        visited[u] = True
        for n in G[u]:
            if not visited[n]:
                Q.appendleft((n, dist + 1))


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
        if x == 0 or x == w-1 or y == 0 or y == h-1:
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
    T = int(input())
    for i in range(T):
        w, h = map(int, input().split())
        m = []
        for i in range(h):
            m.append(input())

        # print("dim is", w*h)
        # for i in m:
        #     print(i)

        G = defaultdict(list)
        fires = set()
        exits = set()
        for i in range(w*h):
            add_neighbours(G, i, w, h, m, fires, exits)
            # curr = m[i // w][i % w]
            # x, y = i % w, i // w # Slow
            #
            # if curr == FIRE:
            #     fires.add(i)
            #
            # if curr == SPACE or curr == START:
            #     if x == 0 or x == w-1 or y == 0 or y == h-1:
            #         exits.add(i)

        # print(exits)
        if not exits: # No exits present
            print(no)
            continue
        elif START in exits: # Edge case if START is one of the exits
            print(1)
            continue

        d1 = dict()
        escape_dists(G, start_index, w*h, exits, d1)

        d2 = dict()
        for f in fires:
            escape_dists(G, f, w*h, exits, d2)

        current_min = INF
        for k, v in d1.items():
            if k not in d2:
                current_min = min(current_min, v)
                break
            if d1[k] < d2[k]:
                current_min = min(current_min, d1[k])

        if current_min == INF:
            print(no)
        else:
            print(current_min)




if __name__ == "__main__":
    main()
