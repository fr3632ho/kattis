
k = int(input()) # number of taps
f = []
min_flow = max_flow = 0
defaultsum= 0
c = 0
for _ in range(k):
    ti, ai, bi = map(int, input().split())
    min_flow += ai
    max_flow += bi
    defaultsum += ai*ti
    c += ai + bi
    f.append((ti, ai, bi))

r = int(input())
f.sort()
extra = [x[2]-x[1] for x in f]
for _ in range(r):
    tau, phi = map(int, input().split())
    if phi > max_flow or phi < min_flow:
        print("no")
        continue
    denom = min_flow
    nom = defaultsum
    delta = phi - min_flow
    for i in range(len(f)):
        temp, ai, bi = f[i]
        if ai + delta <= bi:
            nom += temp*delta
            denom += delta
            break
        nom += temp*extra[i]
        denom += extra[i]
        delta -= extra[i]

    min_temp = nom/denom
    denom = min_flow
    nom = defaultsum
    delta = phi - min_flow
    for i in range(len(f)-1, -1, -1):
        temp, ai, bi = f[i]
        if ai + delta <= bi:
            nom += temp*delta
            denom += delta
            break
        nom += temp*extra[i]
        denom += extra[i]
        delta -= extra[i]

    max_temp = nom/denom

    if min_temp <= tau <= max_temp:
        print("yes")
    else:
        print("no")
