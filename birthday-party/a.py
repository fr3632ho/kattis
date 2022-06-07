from collections import deque

def bridge(graph, n):
    global total
    total = 2

    def dfs(adj, up, down, parent, start):
        global total
        for v in adj[start]:
            if up[v] == -1: # is not visited
                up[v] = total
                down[v] = total
                total += 1
                dfs(adj, up, down, start, v)
                down[start] = min(down[start], down[v]) 

            elif v != parent:
                down[start] = min(down[start], down[v]) 

    up = [-1]*n
    down = [-1]*n

    up[0] = 1
    down[0] = 1
    dfs(graph, up, down, 0, 0)
    for i in range(1, n):
        if up[i] == down[i]:
            return True
    return False


def is_connected(graph, n):    
    vis = set()
    Q = deque()
    Q.append(0)
    while Q:
        u = Q.popleft()
        if u in vis:
            continue
        vis.add(u)
        for v in graph[u]:
            if v not in vis:
                Q.append(v)            
    return len(vis) == n

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

''' find bridges in graph. I.e. removal of single edge will produce a disconnected graph '''

while True:
    p, c = nl()
    if not p and not c: break

    graph = {i:list() for i in range(p)}
    for a, b in [nl() for _ in range(c)]:
        graph[a].append(b)
        graph[b].append(a)     
    
    if not is_connected(graph, p) or bridge(graph, p):
        print("Yes")
    else:
        print("No")
