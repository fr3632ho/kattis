n,k=map(int,raw_input().split())
d,s=map(int,raw_input().split())
# d is the contest average, s is lottes
ans = (n*d-k*s)/(0.0+n-k)
if 0<=ans<=100:
    print "{:.8f}".format(ans)
else:
    print "impossible"
