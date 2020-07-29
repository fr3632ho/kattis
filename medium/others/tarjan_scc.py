import sys

dfn = 0
lowlink = [i for i in range(G.size)]

'''
Really fast implementation of tarjans from psuedo code. Don't think it works but
more for theory than anything else.
'''
def strong_connect(v,dfnum,G):
    dfnum[v], dfn = dfn, dfn + 1
    visited[v] = True
    on_stack = [False] * G.size
    on_stack[v] = True
    stack = [v]

    for n in G.graph[n]:
        if not visited[n]:
            strong_connect(n,dfnum,G)
            lowlink[v] = min(lowlink[n], lowlink[v])
        elif on_stack[n] and dfnum[n] < dfnum[v]:
            lowlink[v] = min(lowlink[n], lowlink[v])

    # SCC on stack
    if lowlink[v] == dfnum[v]:
        scc = []
        while stack:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)

    print(lowlink, '\n', dfnum, scc)
    scc = []


def search_scc(G):
    visited = [False]*G.size
    dfnum = [-1] * G.size

    for i in range(G.size):
        if not visited[i]:
            strong_connect(i,dfnum,G)

    return dfnum
