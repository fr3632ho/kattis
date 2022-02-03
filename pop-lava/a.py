'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]


# 6 is max
# x is 1
# would want 3 1 2 as an output order, alternatively 2 1 3
# solution always possible iff x <= max_val

n, x = nl()
max_val = (n-2)*(n-1)//2

if x > max_val:
    print(-1)
    exit(0)

out = [n]
used = set()
used.add(n)
i = 1
while True:    
    vol = n - 1 - i
    if x <= vol:
        out.append(n - 1 - x)
        used.add(n-1-x)
        break    
    x -= vol
    used.add(i)
    out.append(i)
    i+=1
out.append(n-1)
used.add(n-1)

print(' '.join(map(str, out)), ' '.join( str(i) for i in reversed(range(1,n)) if i not in used))

