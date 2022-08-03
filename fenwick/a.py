'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp().split())
def nl(): return [int(tok) for tok in inp().split()]

n, q = map(int, nl())

def add(arr, idx, val):
    pass

def prefix_sum(arr, idx):
    pass

fenwick = [0]*n

for _ in range(q):
    sig, *nums = nl_2()
    
    print(sig, *nums)

