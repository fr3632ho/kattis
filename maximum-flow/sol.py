
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
out=[]
already_out=set()
for e in range(n):
    for ne in adj[e]:
        if orig_caps[e][ne] >0 and (orig_caps[e][ne] - caps[e][ne] >0) \
            and (e,ne) not in already_out:
            out.append((e,ne,orig_caps[e][ne] - caps[e][ne]))
            already_out.add((e,ne))
print n, mf, len(out)
for u,v,f in out:
    print u,v,f
