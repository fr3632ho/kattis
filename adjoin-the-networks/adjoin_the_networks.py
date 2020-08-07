import sys, gc
from collections import defaultdict, deque

INF = sys.maxsize
visited = []

def BFS(G, start):
    '''
    Returns index of node and longest path
    '''
    n = len(visited)
    dist = defaultdict(lambda:-1) # This was a nice fix as a replacement for the list
    dist[start] = 0
    furthest = 0
    furthest_index = start

    queue = deque([start])
    while queue:
        u = queue.pop()
        visited[u] = True

        for n in G[u]:
            #print(len(G[u]))
            if dist[n] == -1:
                dist[n] = dist[u] + 1
                if furthest < dist[n]:
                    furthest = dist[n]
                    furthest_index = n
                queue.appendleft(n)

    return [furthest, furthest_index]

def get_longest(G, start):
    '''
    Longest path for each sub-net.
    Will
    '''
    s = BFS(G, start)
    t = BFS(G, s[1])
    return t[0]

def main():
    global visited
    c, l = map(int, input().split())

    visited = [False]*c
    d = [-1]*c
    G = [[] for _ in range(c)] # Setup graph
    for i in range(l):
        u, v  = map(int, input().split())
        G[u].append(v), G[v].append(u)

    lengths = []
    for i in range(c):
        if not visited[i]:
            lengths.append(get_longest(G, i))

    lengths.sort()
    while len(lengths) > 1:
        s1 = lengths[-1] // 2
        s2 = lengths[-1] // 2
        if lengths[-1] % 2 == 1:
            s1 += 1
        lengths.pop()

        w1 = lengths[-1] // 2
        w2 = lengths[-1] // 2
        if lengths[-1] % 2 == 1:
            w1 += 1
        lengths.pop()

        o1 = s1 + s2
        o2 = w1 + w2
        o3 = s1 + w1 + 1

        lengths.append(max(o1, o2, o3))

    print(lengths[0])


if __name__ == "__main__":
    main()
