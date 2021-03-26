from collections import defaultdict,deque

def connect(x,y,parents):
    x_parent,y_parent =find(x,parents), find(y,parents)
    if x_parent==y_parent:
        return False
    if size[x_parent]>size[y_parent]:
        size[x_parent]+=size[y_parent]
        parents[x_parent] = y_parent
    else:
        size[y_parent]+=size[x_parent]
        parents[y_parent] = x_parent
    return True

def find(x,parents):
    root=x
    while parents[root]!=-1: root=parents[root]
    while x != root:
        _p = parents[x]
        parents[x]=root
        x = _p
    return root

n=int(input())
nums={}
# Need to create a spanning tree using kruskals
edges=[]
d = {} # number mapped to a vertex
for i in range(n):
    _, *numbers=map(int,input().split())
    for num in numbers:
        if num not in d:
            d[num]=i
        else:
            edges.append((d[num], i, num)) # u,v,num
parents=[-1]*n
size=[1]*n
out=[]
while edges and len(out)<n-1:
    u,v,w = edges.pop()
    if not connect(u,v,parents):
        continue
    out.append((u+1,v+1,w))
if len(out)!=n-1:
    print("impossible")
else:
    for edge in out:
        print(*edge)
