
def f(_w, ribbons):
    global w, h, M

    if ribbons < 0:
        return 0
    if _w > w:
        return 1

    if dp[_w][ribbons] > 0:
        return dp[_w][ribbons]

    s = 0
    for len in range(0, h+1):
        s += f(_w + 1, ribbons - len)

    dp[_w][ribbons] = s
    return s % M


M = 10**9 + 7
n, w, h = map(int, input().split())

# Row represents width of frame
dp = [[0 for _ in range(n + 1)] for _ in range(w + 1)]
plain_scenes = min(n, w*h)//w + 1

print(((f(1, n) - plain_scenes) + M) % M)
