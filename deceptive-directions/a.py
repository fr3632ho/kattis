'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

sys.setrecursionlimit(1000000) # default is 1000.

W, H = nl()
grid = []
for i in range(H):
    line = nl_2()
    for j in range(W):
        if line[j] == 'S':
            start_y, start_x = i, j
    grid.append(line)

#print(grid, start_y, start_x)

INF = 10**12
directions = ['N', 'W', 'E', 'S']
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

from collections import deque

def search_bfs(sequence):
    dist = [[INF]*W for _ in range(H)]
    dist[start_y][start_x] = 0
    queue = deque()
    queue.append((0, start_y, start_x))
    while queue:
        steps, y, x = queue.popleft()
        if steps == dist[y][x]: # eliminate unnecessary steps
            for k in range(4):
                if directions[k] != sequence[steps]:
                    nx, ny = x + dx[k], y + dy[k]
                    # check bounds
                    if 0 <= nx < W and 0 <= ny < H and dist[ny][nx] > steps + 1 and grid[ny][nx] != '#':
                        dist[ny][nx] = steps + 1
                        if steps + 1 < len(sequence):
                            queue.append((steps + 1, ny, nx))
    return dist                    
path = nl_2()
l = len(path)
vis_1 = search_bfs(path)
vis_2 = search_bfs(' '*l)

for i in range(H):
    for j in range(W):
        if vis_1[i][j] == vis_2[i][j] == l:
            grid[i][j] = '!'

for row in grid:
    print(''.join(row))