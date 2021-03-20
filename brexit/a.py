from collections import defaultdict, deque, Counter
c,p,x,l = map(int, raw_input().split()) # x, home and l is start
g = defaultdict(set)
edge_count = Counter()
for _ in range(p):
    u,v = map(int, raw_input().split())
    g[u].add(v), g[v].add(u)
    edge_count[u] += 1
    edge_count[v] += 1
edge_count[l] = 0
visited = set()
queue = [l]
while queue:
    node = queue.pop()
    if node in visited: continue
    visited.add(node)
    for v in g[node]:
        edge_count[v] -= 1
        if edge_count[v] <= len(g[v])/2 and v not in visited:
            queue.append(v)

if edge_count[x]<=len(g[x])/2:
    print "leave"
else:
    print "stay"
