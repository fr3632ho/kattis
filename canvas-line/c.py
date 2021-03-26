n = int(input())
canvas = {}
endpoints = []
for _ in range(n):
    lo,hi = map(int,input().split())
    canvas[(lo,hi)] = []
    if endpoints:
        if endpoints[-1] != lo:
            endpoints.append(lo)
        endpoints.append(hi)
    else:
        endpoints.append(lo), endpoints.append(hi)
p = int(input())
placements = set()
if p!=0:
    for peg in map(int,input().split()):
        lo,hi = 0,len(endpoints)-1
        while lo+1<hi:
            mid = (lo+hi)//2
            if peg > endpoints[mid]:
                lo = mid
            else:
                hi = mid
        a,b = endpoints[lo],endpoints[hi]
        if a<=peg<=b and (a,b) in canvas.keys():
            canvas[(a,b)].append(peg)
        if peg==b and hi<len(endpoints)-1 and (b, endpoints[hi+1]) in canvas.keys():
            canvas[(b, endpoints[hi+1])].append(peg)
        placements.add(peg)
intervalls = sorted(canvas.items())
new = []
while intervalls:
    (a1,b1), v = intervalls.pop()
    if len(v)>2:
        print("impossible")
        exit(0)
    if len(v)<=1 and intervalls:
        (_,b2),v2=intervalls[-1]
        if a1==b2 and len(v2)<2 and a1 not in placements:
            v.append(a1),v2.append(a1)
            new.append(a1)
            placements.add(a1)
    temp =a1+1
    while len(v)<2:
        if temp not in placements:
            v.append(temp)
            new.append(temp)
            placements.add(temp)
        temp+=1
print(len(new))
if new:
    print(*new)
