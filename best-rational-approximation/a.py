import math
p = input()

for i in range(p):
    data = raw_input().split()
    k,m = map(int,data[:2])
    x = float(data[2])
    origx = x
    if x < 0.0000005:
        print k, "0/1"
        continue

    x = 1/x
    fraction = [0, int(math.floor(x))]
    x -= math.floor(x)
    values = 30
    for i in range(values):
        if x<0.0000005:
            break
        x = 1/x
        fraction.append(int(math.floor(x)))
        x -= math.floor(x)

    best = [0, 1]
    for le in range(2, len(fraction)+1):
        lastval = fraction[le-1]
        for reallast in range(max(1,lastval/2), lastval+1):
            frac = [1,reallast]
            for ind in range(le-2,0,-1):
                a,b = frac
                na = b*fraction[ind]+a
                nb = b
                frac = [nb,na]
            if frac[1] <= m and abs(origx-best[0]/float(best[1])) > abs(origx - frac[0]/float(frac[1])):
                best = frac
    print k, "/".join(map(str,best))
