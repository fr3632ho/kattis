

n = input()
while n!=0:
    adj = [[] for _ in range(n)]
    for i in range(n):
        for x in map(int, raw_input().split()):
            adj[i].append(x)
    m = input()

    dp = dict() # (room, turn) -> (min, max)
    for i in range(n):
        dp[(i, 0)] = adj[0][i]

    for turn in range(1,m):
        for room in range(n):
            if (room, turn) in dp:
                curr = dp[(room,turn)]
            else:
                curr = 0
            for r2 in range(n):
                dp[(room, turn)] = max(curr, dp[(r2, turn-1)] + adj[room][r2])

    for k, v in dp.items():
        print k, v

    n=input()
    print "new test\n"
