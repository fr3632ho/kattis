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

from collections import deque

r, c = nl()
adj = [] 
_min, _max = 10**12, 0
for i in range(r):
    adj.append(nl())
    _min, _max = min(_min, min(adj[i])), max(_max, max(adj[i]))

def get_neighbours(ri, ci):
    dd = [-1, 1]
    for rx in dd:
        yield (ri - rx, ci)
    for cy in dd:
        yield (ri, ci - cy)

def BFS(queue, adj, max_depth, end_set):
    vis = set()
    while queue:
        tup = queue.popleft()
       # print(tup, adj[tup[0]][tup[1]])
        if tup in end_set:
            return True        
        y, x = tup
        if tup in vis or adj[y][x] > max_depth:
            continue        
        vis.add(tup)
        for yi, xi in get_neighbours(y, x):            
            if 0<= yi < r and 0 <= xi < c and (yi, xi) not in vis:
                if adj[yi][xi] <= max_depth:
                    queue.append((yi, xi))                
    return False

end = set( (y, c-1) for y in range(r))
start = list( (y, 0) for y in range(r))

lo, hi = _min, _max
while lo < hi:
    mid = (lo + hi) // 2
    #print("mid is", mid)
    res = BFS(deque(start[:]), adj, mid, end)
    #print("returned with", res)
    if res:
        hi = mid
    else:
        lo = mid +1

print(lo)




