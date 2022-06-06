'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

n = ni()
xs = [[False]*n for _ in range(n)]
losses = [0 for _ in range(n)]
for i in range(n-1):
    l = [bool(int(k)) for k in nl_2()]
    for j in range(i+1):
        xs[i+1][j] = l[j]
        xs[j][i+1] = not l[j]
        losses[i+1] += not l[j]
        losses[j] += l[j] 

from heapq import heappop, heappush, heapify
queue = [(loss, i) for i, loss in enumerate(losses)]
heapify(queue)
for row in xs:
    print(row)
print(losses, queue)
k = 0
vis = set()
while queue:
    loss, node = heappop(queue)
    if node in vis:
        continue
    k = max(k, loss)
    vis.add(node)
    for j in range(n):
        if j == node or j in vis:
            continue
        if xs[node][j]:
            losses[j] -= 1
            heappush(queue, (losses[j], node))    
print(k)    



