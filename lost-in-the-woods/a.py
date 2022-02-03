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

from collections import defaultdict

N, M = nl()
graph = defaultdict(list)
for e in range(M):
    u, v = nl()
    graph[u].append(v)
    graph[v].append(u)

start, end = 0, N-1

# simulated dfs

import random as r
tot = 0
iterations = 10000
for i in range(iterations):    
    start_node = start
    while start_node != end:                
        nxt = r.randint(0, len(graph[start_node]) - 1)
        tot += 1        
        start_node = graph[start_node][nxt]    

print(tot / iterations)
