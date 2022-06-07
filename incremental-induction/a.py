'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def ns(): return str(inp())

n = ni()
outdeg = [0]*n
for i in range(n-1):
    l = list(ns())
    for j in range(i + 1):
        if l[j] == '1':
            outdeg[i+1] += 1
        else:
            outdeg[j] += 1

ordered = sorted(range(n), key=lambda i : -outdeg[i]) # sorted by maximum outdegree

number_of_edges = n * (n - 1) // 2
max_k = 0
for i, v in enumerate(ordered):
    number_of_edges -= outdeg[v]
    cut_size = number_of_edges - (n-i-1) * (n - i - 2)//2
    max_k = max(max_k, cut_size)

print(max_k)

# We are given a complete undirected graph, i.e. n(n-1)/2 undirected edges
# which we then direct, creating a tournament (complete directed graph)
