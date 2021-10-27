from collections import deque, defaultdict

# Input
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]


def bfs_trees_two(trees):
    global min_dist
    for i, _ in trees:
        min_dist[i] = 0

    vis = set()
    while trees:
        node, dist  = trees.popleft()
        if node in vis:
            continue
        vis.add(node)
        min_dist[node] = dist
        for neighbour in get_neighbours(*node):
            if min_dist[neighbour] == -1:
                trees.append((neighbour, dist + 1))

dir = [(0,-1), (1, 0), (0, 1), (-1, 0)]
def get_neighbours(y,x):
    global n, m
    neigh = []
    for dx, dy in dir:
        if 0<= y-dy < n and 0 <= x-dx<m:
            yield (y-dy,x-dx)

n,m = nl()
trees = deque()
min_dist = defaultdict(lambda : -1)
start = end = -1
for y in range(n):
    line = nl_2()
    for i, x in enumerate(line):
        if x == '+':
            trees.append(( (y,i), 0))
        if x=='V': start = (y, i)
        if x=='J': end = (y, i)

bfs_trees_two(trees)

def bfs_last(cap):
    global start, end
    vis = set()
    queue = deque()
    queue.append((start, min_dist[start]))
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist

        if node in vis:
            continue
        vis.add(node)
        for neigh in get_neighbours(*node):
            if neigh not in vis and dist >= cap:
                queue.append((neigh, min(dist, min_dist[neigh])))
    return -1

max_edge = max(min_dist.values())

def bin_search_cap(lo, hi):
    if lo>=hi:
        return lo-1
    mid = (hi+lo)//2
    ret = bfs_last(mid) # -1 => go lower cap else go higher
    if ret==-1:
        return bin_search_cap(lo, mid)
    else:
        return bin_search_cap(mid+1, hi)

# test = []
# for y in range(n):
#     row = []
#     for x in range(m):
#         row.append(min_dist[(y,x)])
#     test.append(row)
# print(max_edge)
# for row in test:
#     print(row)

print(bin_search_cap(0, max_edge))
