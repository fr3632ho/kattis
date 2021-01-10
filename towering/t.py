def create_twer(xs, t1):
    for i in xs:
        for j in xs:
            for k in xs:
                if i+j+k == t1 and i != k and j != k and i != j:
                    tw = [i, j, k]
                    tw.sort(reverse=True)
                    return tw

vals = map(int, raw_input().split())
xs = vals[:-2]
t1 = vals[-2]
xs.sort(reverse=True)
tw1 = create_twer(xs, t1)
print " ".join(str(i) for i in tw1), " ".join(str(i) for i in xs if i not in tw1)
