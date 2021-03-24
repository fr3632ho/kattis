from heapq import heappush, heappop

def union(x,y,parents):
    a, b = find(x,parents), find(y, parents)
    if a==b: return False
    if a>b: a,b=b,a
    parents[a] = b
    return True

def find(x, parents):
    root = x
    while parents[root] != -1: root = parents[root]
    _p = x
    while x != root:
        _p = parents[x]
        parents[x] = root
        x = _p
    return root
n,m=map(int,raw_input().split())
while n!= 0:
    edges = set()
    pq = []
    for i in range(m):
        x,y,w=map(int,raw_input().split())
        edges.add((min(x,y),max(x,y)))
        heappush(pq, (w,x,y))
    parents = [-1]*n
    forest = set()
    count = 0
    weight = 0
    out_pq = []
    while pq:
        w,a,b = heappop(pq)
        if union(a,b,parents):
            heappush(out_pq,(min(a,b),max(a,b)))
            weight+=w
            if a not in forest:
                forest.add(a)
                count+=1
            if b not in forest:
                forest.add(b)
                count+=1
    if count != n:
        print "Impossible"
    else:
        print weight
        while out_pq:
            a,b = heappop(out_pq)
            print a,b
    n,m=map(int,raw_input().split())
