from collections import deque

T = int(input())

for _ in range(T):
    xs, ys = input().split(), input().split()
    A, B = [], []
    dimy = dimx = 0
    for i in range(0, max(len(xs), len(ys)), 2):
        if i < len(xs):
            ai, bi = int(xs[i]), int(xs[i+1])
            A.append((ai, bi))

        if i < len(ys):
            ai, bi = int(ys[i]), int(ys[i+1])
            dimy = max(dimy, bi)
            dimx = max(dimx, ai)
            B.append((ai, bi))

    c, d = A[-1]
    A.pop()

    l = max(dimx, dimy) + 1
    dp = [[d for _ in range(l)] for _ in range(l)]

    for y in range(0, l):
        for x in range(0, l):
            if y > 0 and x > 0:
                dp[y][x] = c
                for ai, bi in A:
                    xi, yi = x-ai,y-bi
                    if xi>0 and yi>0:
                        dp[y][x] += dp[yi][xi]
                    else:
                        dp[y][x] += d


    for x, y in B:
        print(dp[y][x])
    print()
