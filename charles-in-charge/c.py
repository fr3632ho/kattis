from heapq import heappush, heappop

INF = 10**15
def dijkstra(G,s):
    N = len(G)
    vis = [False]*N
    d = [INF]*N
    d[s] = 0
    Q = [(d[s], s)] # s := (t, c)
    while Q:
        t, city = heappop(Q)
        if vis[city]: continue
        vis[city] = True
        for dist, cnext in G[city]:
            altD = t + dist
            if altD <= d[cnext]:
                d[cnext] = altD
                heappush(Q, (d[cnext], cnext))
    return d[N-1]

n,m,x = map(int, raw_input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    c1,c2,t = map(int, raw_input().split())
    c1, c2 = c1-1, c2-1
    adj[c1].append((t,c2))
    adj[c2].append((t,c1))
shortest = dijkstra(adj,0)
#print shortest
lim = shortest*(100+x)
lo, hi = 0, 1000000000
while lo+1<hi:
    mid = (lo+hi)/2
    curr = [[] for _ in range(n)]
    for i in range(n):
        for t,ne in adj[i]:
            if t <= mid:
                curr[i].append((t,ne))
    temp_dist = dijkstra(curr, 0)
    if temp_dist*100<=lim:
        hi = mid
    else:
        lo = mid
print hi
