import sys
from collections import deque

def BFS(G, n, target):
    visited = dict()
    queue = deque([[(0, 0), 0]])

    while queue:
        u, dist = queue.pop()

        if u == target:
            return dist

        if u in visited:
            continue

        visited[u] = 1
        for n in G[u]:
            if n not in visited:
                queue.appendleft([n, dist + 1])

    return -1



def add_neighbours(G, y, x, k, n, m):
    if k == 0:
        G[(y, x)] = []
        return

    ret = []
    if x - k >= 0: # left neighbour k steps
        ret.append((y, x - k))
    if x + k < m:
        ret.append((y, x + k))
    if y - k >= 0:
        ret.append((y - k, x))
    if y + k < n:
        ret.append((y + k, x))

    G[(y, x)] = ret


def main():
    n, m = map(int, input().split())
    #print(n, m)

    A = []
    for _ in range(n):
        # need to construct graph so that each neighbour to each and every node
        # is k steps away. If node value is 1, then it's neighbours are
        # relative to its position (x, y) -> (x - k, y), (x + k, y), (x, y - k) and (x, y + k)
        A.append(input())

    G = dict()
    for i in range(n):
        for j in range(m):
            k = int(A[i][j])
            add_neighbours(G, i, j, k, n, m)

    # for k, v in G.items():
    #     print("{} -> {}".format(k, v))
    print(BFS(G, n, (n-1, m-1)))




if __name__ == "__main__":
    main()
