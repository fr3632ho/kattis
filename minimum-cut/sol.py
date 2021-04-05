def dfs(vis, cur, cmf, threshold):
    if vis[cur]:
     return 0
    vis[cur]=True
    if cur==t:
     return cmf
    for ne in adj[cur]:
     if not vis[ne] and caps[cur][ne] > threshold:
         new_flow = min(cmf, caps[cur][ne])
         ret = dfs(vis, ne, new_flow, threshold)
         if ret > 0:
             caps[cur][ne] -= ret
             caps[ne][cur] += ret
             return ret
    return 0

def carp():
    max_flow = 0
    for i in range(30,-1,-1):
        to_add = dfs([False]*n, s,INF, 2**i - 1)
        while to_add:
            max_flow += to_add
            to_add = dfs([False]*n, s,INF, 2**i - 1)
    return max_flow


n,m,s,t=map(int,raw_input().split())
INF=10**15
adj=[[] for _ in range(n)]
caps=[[0]*n for _ in range(n)]
orig_caps=[[0]*n for _ in range(n)]
for edge in range(m):
    u,v,c=map(int,raw_input().split())
    adj[u].append(v)
    adj[v].append(u) # Residual
    caps[u][v] += c
    orig_caps[u][v] += c
mf=carp()
def dfs_2(vis,cur,out):
    if vis[cur]: return
    vis[cur]=True
    out.append(cur)
    for ne in adj[cur]:
        if not vis[ne] and caps[cur][ne]>0:
            dfs_2(vis,ne,out)

out=[]
dfs_2([False]*n,s,out)
print len(out)
for i in out:
    print i
