
def f():
    global dp, M, w, h, n
    for i in range(min(h+1, n+1)):
        dp[1][i] = 1

    for i in range(1, w+1):
        m = i*h + h
        j = 0
        while j <= min(n, m):
            for k in range(h+1):
                if j-k<0:
                    break

                dp[i + 1][j] += dp[i][j-k] % M

            j+=1

    ans = 0
    for i in range(0, n+1):
        ans += dp[w][i] % M

    return ((ans - (min(h, n//w) + 1))) % M


M = 10**9 + 7
n, w, h = map(int, input().split())

if not n:
    print(0)
    exit(0)

if n == 1:
    print(w)
    exit(0)

dp = [[0 for _ in range(n + 1)] for _ in range(w + 2)]

print(f())
