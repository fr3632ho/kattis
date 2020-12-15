from collections import defaultdict

def dfs(visited, n):
    global G, match, target
    for i in G[n]:
        if not visited[i]:
            visited[i] = True
            if target[i] == -1 or dfs(visited, target[i]):
                target[i] = n
                match[n] = i
                return True

    return False

n, m = map(int, raw_input().split())
G = defaultdict(list)
for _ in range(m):
    a, b = map(int, raw_input().split())
    G[a].append(b)
    G[b].append(a)

match = [-1]*(n+1)
target = [-1]*(n+1)
count = 0
for p in range(1, n+1):
    hit = [False]*(n+1)
    if dfs(hit, p):
        count += 1

if len(set(target))-1 < n:
    print "Impossible"
    exit(0)

for i in range(1, n+1):
    print match[i]
