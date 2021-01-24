def gcd(a, b):
    if b>a:
        return gcd(b, a)
    if b==0:
        return a
    return gcd(b, a%b)

n, d, m = map(int ,raw_input().split())
while n != 0:
    n = n+10
    # t inbetween 1 <= t <= 10
    moles = [[[False for i in range(n)] for j in range(n)] for k in range(11)]
    for m in range(m):
        x, y, t = map(int, raw_input().split())
        moles[t-1][x+5][y+5] = True # compensate for the +10 extension of the board

    dp = [[[0 for i in range(n)] for j in range(n)] for k in range(11)]

    for t in range(10):
        # want to compute dp[t+1][x][y]
        for x in range(n):
            for y in range(n):
                for dx in range(-d, d + 1):
                    for dy in range(-d, d + 1):
                        if (dx)**2 + (dy)**2 > d**2: #outside of range
                            continue
                        if x+dx >= n or x+dx<0 or y+dy>=n or y+dy<0:
                            continue

                        hits = 0
                        if dx==dy==0:
                            if moles[t][x][y]:
                                hits = 1
                        else:
                            g = gcd(abs(dx), abs(dy))
                            for cross in range(g+1):
                                if moles[t][x + dx/g*cross][y + dy/g*cross]:
                                    hits += 1
                        dp[t+1][x][y] = max(dp[t+1][x][y], dp[t][x+dx][y+dy] + hits)

    best = 0
    for x in range(n):
        for y in range(n):
            best = max(best, dp[10][x][y])

    print best

    n, d, m= map(int ,raw_input().split())
