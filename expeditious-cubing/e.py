t1,t2,t3,t4 = sorted(map(lambda x  : float(x)*10**12, raw_input().split()))
beat=int(input()*10**12)
if (t2+t3+t4)<=3*beat:
    print "infinite"
    exit(0)
else:
    t5 = 3*beat - (t2+t3)
    m = 0
    if t1+t2+t3<=3*beat:
        m = max(m,t1)
    if t5+t2+t3<=3*beat and t5>t1:
        m = max(m,t5)
    if m==0:
        print "impossible"
        exit(0)
    print "{:.2f}".format(m/10**12)
