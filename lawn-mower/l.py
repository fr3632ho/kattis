

while True:
    nx, ny, w = raw_input().split()
    if int(nx) == int(ny) == 0:
        exit(0)
    w = float(w)
    delta = w/2
    along = list(map(lambda x: (float(x) - delta, float(x) + delta), raw_input().split()))
    along.sort()
    #print along
    i = 1
    flag1 = False
    if along[0][0] <= 0.0 and along[-1][1] >= 75.0:
        flag1 = True
        while i<int(nx):
            #print i, len(along), nx
            if not along[i-1][1] >= along[i][0]:
                flag1 = False
                break
            i+=1

    up = list(map(lambda x : (float(x) - delta, float(x) + delta), raw_input().split()))

    up.sort()
    i = 1
    flag2 = False
    if up[0][0] <= 0.0 and up[-1][1] >= 100:
        flag2 = True
        while i < int(ny):
            if not up[i-1][1] >= up[i][0]:
                flag2 = False
                break
            i+=1

    if flag2 and flag1:
        print "YES"
    else:
        print "NO"
