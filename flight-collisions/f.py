from heapq import heappush, heappop
from fractions import Fraction

def collidetime(id1,id2):
    global drones
    assert id1!=id2
    if id1 > id2: id1,id2=id2,id1
    x1,v1 = drones[id1]
    x2,v2 = drones[id2]
    dx = x2-x1
    if v1<=v2:
        return None
    dv = v1-v2
    return Fraction(dx, dv)

n=int(input())
drones=[]
for i in range(n):
    xi,vi=map(int,input().split())
    drones.append((xi,vi))
if n==0:
    print(1)
    print(1)
    exit(0)

drones_forward=[i+1 for i in range(n)]
drones_forward[-1]=-1
drones_backward=[i-1 for i in range(n)]
drones_backward[0]=-1
time_heap=[]
for i in range(1,n):
    ret = collidetime(i-1,i)
    if ret:
        heappush(time_heap, (ret,i-1,i))
crashed = set()
while time_heap:
    frac, id1, id2 = heappop(time_heap)
    if id1 in crashed or id2 in crashed:
        continue
    crashed.add(id1)
    crashed.add(id2)
    id3 = drones_backward[id1]
    id4 = drones_forward[id2]
    if id3 != -1 and id4 != -1:
        drones_forward[id3]=id4
        drones_backward[id4]=id3
        ret = collidetime(id3,id4)
        if ret:
            heappush(time_heap, (ret, id3,id4))

print(n -len(crashed))
if len(crashed)!=n:
    out=[]
    for i in range(n):
        if i not in crashed:
            out.append(i+1)
    print(" ".join(map(str,out)))
