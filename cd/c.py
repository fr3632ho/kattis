
'''
Too slow, maybe try sliding window
'''

def binsearch(xs, a):
    lo, hi = 0, len(xs) -1
    #print xs, "target", a
    while lo-1<hi:
        mid = lo + (hi - lo)//2
        #print lo, hi, a, xs[mid]
        if xs[mid] == a:
            return True
        elif xs[mid] < a:
            lo = mid+1
        else: hi = mid -1

    return False



while True:
    jack, jill = map(int, raw_input().split())
    if jack == jill == 0:
        exit(0)

    js = [0]*jack
    for i in range(jack):
        q = input()
        js[i] = q

    c = 0
    last = 0
    for _ in range(jill):
        q = input()
        if q == last:
            continue
        last = q
        if binsearch(js, q): c += 1

    print c
