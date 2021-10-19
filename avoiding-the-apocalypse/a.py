import sys
from itertools import permutations, combinations, product
sys.setrecursionlimit(1000000) # default is 1000.

def dfs(vis, cur, cmf, threshold, time_limit):
    if vis[cur] or time_limit<0:
        return 0
    vis[cur]=True
    if cur ==END:
        return cmf
    for ne,time in adj[cur]:
        if not vis[ne] and caps[cur][ne]>=threshold:
            new_flow = min(cmf, caps[cur][ne])
            ret = dfs(vis, ne, new_flow, threshold, time_limit-time)
            if ret>0:
                caps[cur][ne] -= ret
                caps[ne][cur] += ret
                return ret
    return 0


def carp():
    max_flow=0
    for i in range(30,-1,-1):
        to_add=dfs([False]*(n+1),START,INF,2**i -1, limit)
        while to_add:
            max_flow+=to_add
            to_add=dfs([False]*(n+1),START,INF,2**i -1,limit)
    return max_flow

t=input()
INF=10**15
for case in range(t):
    n=input()
    START,g,limit=map(int,raw_input().split())
    START-=1
    END=n
    # start, nr of people and time steps
    m=input()
    adj=[[] for _ in range(n+1)]
    caps=[[0]*(n+1) for _ in range(n+1) ]
    for _ in range(m):
        _m = input()-1
        #meds.add(_m)
        adj[_m].append((END,0))
        caps[_m][END]=INF
    r=input()
    for _ in range(r):
        a,b,p,t=map(int,raw_input().split())
        a,b=a-1,b-1
        adj[a].append((b,t))
        adj[b].append((a,t))
        caps[a][b]=caps[b][a]=p
    flow = carp()
    print START
    for row in adj:
        print row
    print flow
