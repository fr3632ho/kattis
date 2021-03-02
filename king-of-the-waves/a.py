from collections import defaultdict, deque

n = input()
G = defaultdict(set)
for i in range(n):
    row = raw_input()
    for j in range(n):
        if row[j] == '1':
            G[i].add(j)
_G = defaultdict(set)
visited = set()
Q = deque([(0,0)])
while Q:
    node, p = Q.pop()
    if node in visited:
        continue
    visited.add(node)
    if node != 0:
        _G[p].add(node)
    for i in G[node]:
        if i not in visited:
            Q.appendleft((i,node))
if len(visited) < n:
    print("impossible")
    exit(0)
parents = [i for i in range(n)]
parents[0]=-1
Q = [0]
prev = -1
done = set()
while Q:
    node = Q.pop()
    if node in done:
        continue
    done.add(node)
    root = -1
    for child in _G[node]:
        if root==-1:
            root = child
        else:
            if child in G[root]:
                parents[child]=root
            else:
                parents[root]=child
                root = child
    if root == -1:
        parents[node]=prev
        prev = node
        continue

    for child in _G[node]:
        if child != root:
            _G[root].add(child)
    if prev==-1:
        parents[root]=0
    else:
        parents[root]=node
    prev=node
    Q.append(root)    

out = [str(prev)]
prev = parents[prev]
while prev != -1:
    out.append(str(prev))
    prev = parents[prev]
print(" ".join(out))
