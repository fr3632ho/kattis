'''Useful for simulation problems and combinatorics'''
'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

from collections import Counter

def fac(n, cache):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    res = n*fac(n-1, cache)
    cache[n] = res
    return res 

try:
    while True:
        query = ''.join(nl_2())        
        freq = Counter(query)
        cache = dict()
        n, m = fac(len(query), cache), 1
        for k, v in freq.items():
            m*= fac(v, cache)
        print(n//m)

except Exception as e:                
    pass
