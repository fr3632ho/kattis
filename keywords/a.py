'''Useful for simulation problems and combinatorics'''
'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def ns(): return str(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

import re
n = ni()
_n = n
exists = set()
for i in range(n):    
    exists.add(re.sub('[\-]', ' ', ns().lower()))
print(len(exists))


