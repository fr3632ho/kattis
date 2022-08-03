'''Useful for simulation problems and combinatorics'''
from itertools import permutations, combinations, product

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

# on the form ( OP p q )
# 1 p q => { union p, q }
# 2 p q => { Move p to the set containing q. 
# If  and  are already in the same set, ignore this command }
# 3 p q => { Return the number of elements 
# and the sum of elements in the set containing p }
# ---
# parents := [p_id(n), p_id(n+1), .. , p_id(2n)]
# size := [p_id(n), p_id(n+1), .. , p_id(2n)]
# root_stats := {p_id(i): [sum + k, k]}, where k is number of elements
# roots := [-1]*n

# actually, size becomse redundant since we already have parent_ids to cover
# for the size of the sets
# ---
# One could argue that we could have a list for parent_ids instead since
# rehashing will be costly, but w/e
#  
# This can give us O(1) for OP 1 and 3
# Operation 2 will also be O(1)/O(k) where 1 <= k << n

from collections import defaultdict


class Almost_Union_Find:

    ''' Rule: any id related to roots will be greater or equal to n!'''

    def __init__(s, n):
        s.n = n
        s.INF = 10**12
        s.roots = {k:s.INF for k in range(n, 2*n)}
        s.root_stats = {k:[0, 0] for k in range(n, 2*n)}
        s.parents = [-1]*n          
        s.n = n
        s.root_id = n        

    def create_root_id(s, u : int) -> int:             
        new_id = s.root_id
        s.root_id += 1        
        return new_id

    def find(s, u: int) -> int:                     
        _u = u
        while 0 <= s.parents[_u] < n:
            _u = s.parents[u]                

        while _u >=  n and s.roots[_u] != s.INF:
            _u = s.roots[_u]
        
        ret_value = -1
        if s.parents[_u] == -1:
            # need to create next root id
            new_root = s.create_root_id(_u) # new root >= n            
            s.parents[_u] = new_root             
                        
            s.root_stats[new_root][1] += 1
            s.root_stats[new_root][0] += u
            return new_root
        else:     
            # move into root datastructure
            # search for parent of root               

            _u = s.parents[_u]
            while _u >= n and s.roots[_u] != s.INF:
                _u = s.roots[_u]
         
            temp = -1
            while u != _u and u < n:                                                          
                temp = s.parents[u]
                s.parents[u] = _u
                u = temp
                    
            return _u
    
    def union(s, a: int, b: int):
        _a, _b = s.find(a), s.find(b)
        if _a == _b: 
            return               
        a_v, a_k = s.root_stats[_a] 
        b_v, b_k = s.root_stats[_b]     
        if a_k > b_k:
            s.roots[_b] = _a
            s.parents[b] = _a
            s.root_stats[_a][0] += b_v
            s.root_stats[_a][1] += b_k            
            
            s.root_stats[_b][0] -= b_v            
            s.root_stats[_b][1] -= 1
        else:
            s.roots[_a] = _b
            s.parents[a] = _b
            s.root_stats[_b][0] += a_v
            s.root_stats[_b][1] += a_k
            
            s.root_stats[_a][0] -= a_v            
            s.root_stats[_a][1] -= 1

            _a, _b = _b, _a
    
    def move(s, a, b):       
        _a, _b = s.find(a), s.find(b)
        if _a == _b:
            return

        s.root_stats[_a][0] -= a
        s.root_stats[_a][1] -= 1        
        
        s.parents[a] = _b

        s.root_stats[_b][0] += a
        s.root_stats[_b][1] += 1   
  
    def summarize(s, u):      
        _u = s.find(u)      
        return s.root_stats[_u] 

for case in range(20):    
    try:
        n, m = nl()
    except:
        break
    
    auf = Almost_Union_Find(n)
    for _ in range(m):
        OP, *other = map(lambda x : x - 1, nl())
        OP += 1        
        if OP == 1: #UNION
            p, q = other            
            auf.union(p, q)
        elif OP == 2: #MOVE
            p, q = other
            auf.move(p, q)
        else: # PRINT STATS
            p, = other
            v, k = auf.summarize(p)
            print(k, v + k)

