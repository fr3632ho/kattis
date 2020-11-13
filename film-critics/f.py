def calc(switch):
    global ai, n,m
    tot = 0
    for big in range(switch):
        val,_ = ai[-1-big]
        if tot==0:
            tot+=1
            continue

        #tot*m/big is average
        if tot*m<=big*val:
            tot+=1

    for small in range(n-switch):
        val,_ = ai[small]
        if tot==0:
            tot+=1
            continue

        #tot*m/(small+switch) is average
        if tot*m<=(small+switch)*val:
            tot+=1
    return tot


n,m,k = map(int,raw_input().split())
a = list(map(int,raw_input().split()))
ai = [(a[i],i) for i in range(n)]
if k%m != 0:
    print "impossible"
    exit(0)
k = k/m
ai.sort()
loposs = calc(n)
hiposs = calc(0)
print loposs, hiposs
if loposs<=k<=hiposs:
    lo=0 #should give answer >=k
    hi=n+1 #should give answer <k
    while lo+1<hi:
        mid = (lo+hi)/2
        if calc(mid) >=k:
            lo = mid
        else:
            hi = mid
    #lo is num we should switch
    out = []
    for big in range(lo):
        _,ind = ai[-1-big]
        out.append(ind+1)
    for small in range(n-lo):
        _,ind = ai[small]
        out.append(ind+1)
    print " ".join(map(str,out))
else:
    print "impossible"
    exit(0)
