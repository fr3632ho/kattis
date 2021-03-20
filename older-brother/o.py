q = input()
if q==1:
    print "no"
    exit(0)
for d in range(2, int(q**0.5) + 5):
    if q%d==0:
        while q%d == 0:
            q /= d
        if q==1:
            print "yes"
        else:
            print "no"
        exit(0)
print "yes"
