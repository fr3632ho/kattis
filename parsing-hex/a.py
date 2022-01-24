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

import re
chars = 'abcdef'
max_val = 4294967295

for line in itr:
    for i in range(1, len(line)):
        if line[i-1] == '0' and line[i].lower() == 'x':
            num = [line[i-1:i+1]]
            for j in range(i+1, len(line)):
                if line[j].lower() in chars or line[j].isdigit():
                    num.append(line[j])
                else: break                    
            num = ''.join(map(str.lower, num))
            if num != '0x' and int(num, 16) <= max_val:
                print(num, int(num, 16))
        
