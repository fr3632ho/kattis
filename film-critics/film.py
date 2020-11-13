# TODO

def get_score(l, k):
    global m
    tot = 0
    for big in range(k):
        if tot == 0:
            tot += 1
            continue
        c, _ = l[-1-big]
        if tot*m <= c*big: # tot*m/big is average
            tot += 1
    for small in range(len(l)-k):
        if tot == 0:
            tot += 1
        c,_ = l[small]
        if tot*m <= (small+k)*c: #tot*m/(small+k) is average
            tot += 1
    return tot


def binary(l, lo, hi):
    global p
    if lo+1>=hi:
        return lo

    mid = (lo + hi)//2
    if get_score(l, mid) >= p:
        return binary(l, mid, hi)
    else:
        return binary(l, lo, mid)

n, m, k = map(int, input().split())
critics = [(c, i) for i, c in enumerate(map(int, input().split()))]

if k%m != 0:
    print("impossible")
    exit(0)

p = k/m # Need p positive reviews
critics.sort()
low_possibility = get_score(critics, n)
high_possibility = get_score(critics, 0)

if low_possibility <= p <= high_possibility:
    low = binary(critics, 0, n)
    out = []
    for big in range(low):
        _, ind = critics[-1-big]
        out.append(ind+1)

    for small in range(n-low):
        _, ind = critics[small]
        out.append(ind+1)

    print(" ".join(map(str, out)))

else:
    print("impossible")
    exit(0)
