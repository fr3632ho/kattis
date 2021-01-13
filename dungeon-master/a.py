from collections import defaultdict, deque
EXIT = 'E'
START  = 'S'

def printf(s, b):
    if b:
        print "Escaped in {} minute(s).".format(s)
    else:
        print "Trapped!"

def get_neighbours(layer, row, col, id):
    global m, l, r, c
    n = []
    if m[layer][row][col] == '#':
        return n
    # id formula := layer*r*c + row*r + col
    # given id => n := [id+1, id-1, id-r id+r id-(r*c)]
    if layer>0 and m[layer-1][row][col] != '#':
        n.append(id-r*c)

    if layer<l-1 and m[layer+1][row][col] != '#':
        n.append(id+r*c)

    if row>0 and m[layer][row-1][col] != '#':
        n.append(id-c)

    if row<r-1 and m[layer][row+1][col] != '#':
        n.append(id+c)

    if col>0 and m[layer][row][col-1] != '#':
        n.append(id-1)

    if col<c-1 and m[layer][row][col+1] != '#':
        n.append(id+1)

    return n

def bfs(G, s, t):
    Q = deque([(s, 0)])
    visited = set()
    while Q:
        node, w = Q.popleft()
        if node in visited:
            continue
        visited.add(node)
        for n in G[node]:
            if n == t:
                return w+1
            if n not in visited:
                Q.append((n, w+1))
    return -1


while True:
    l, r, c = map(int, raw_input().split())
    if l == r == c == 0:
        exit(0)

    m = []
    for _ in range(l):
        adj = []
        for _ in range(r):
            adj.append(raw_input())
        m.append(adj)
        raw_input()

    # Setup neighbours
    # id = layer + r*row + col
    s = -1
    e = -1
    G = defaultdict(list)
    id = 0
    for layer in range(l):
        curr = m[layer]
        for row in range(r):
            for col in range(c):
                if curr[row][col] == START:
                    s = id
                elif curr[row][col] == EXIT:
                    e = id
                G[id] = get_neighbours(layer, row, col, id)
                id += 1

    # for k, v in G.items():
    #     print k, v

    #print s, e
    if len(G[s]) == 0 or len(G[e]) == 0:
        printf(-1, False)
        continue

    dist = bfs(G, s, e)
    if dist != -1:
        printf(dist, True)
    else:
        printf(dist, False)
