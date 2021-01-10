

while True:
    nx, ny, w = raw_input().split()
    if int(nx) == int(ny) == 0:
        exit(0)
    w = float(w)
    delta = w/2
    along = list(map(lambda x: (float(x) - delta, float(x) + delta), raw_input().split()))
    up = list(map(lambda x : (float(x) - delta, float(x) + delta), raw_input().split()))
    along.sort(), up.sort()
    flag1 = all([along[i-1][1] >= along[i][0] for i in range(1, int(nx))]) and (along[0][0] <= 0.0 and along[-1][1] >= 75.0)
    flag2 = all([up[i-1][1] >= up[i][0] for i in range(1, int(ny))]) and (up[0][0] <= 0.0 and up[-1][1] >= 100)
    if flag2 and flag1: print "YES"
    else: print "NO"
