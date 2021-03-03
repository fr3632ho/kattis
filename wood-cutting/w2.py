t = input()
for _ in range(t):
    n = input()
    xs = []
    for _ in range(n):
        xs.append(sum(map(int,raw_input().split()[1:])))
    s, tot = 0,0
    for i in sorted(xs):
        s += i
        tot += s
    print("{:.10f}".format(tot/(n*1.0)))
