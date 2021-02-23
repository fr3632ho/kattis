n = input()
while n!=0:
    adj = [[] for _ in range(n)]
    for i in range(n):
        for x in map(int, raw_input().split()):
            adj[i].append(x)
    m = input()
    if m == 0:
        print 0,0
        n=input()
        continue
    mindp = [[0 for room in range(n)] for turn in range(m+1)]
    maxdp = [[0 for room in range(n)] for turn in range(m+1)]
    call_min = min
    call_max = max
    for turn in range(1,m+1): # O(m*n^2), worst case => 5000*50^2 = 12 500 000 iterations. Too slow for python2
        for room in range(n):
            if turn == 1:
                mindp[turn][room] = adj[0][room]
                maxdp[turn][room] = adj[0][room]
            else:
                _min, _max = 9999999, -1
                for rnext in range(n):
                    _min = call_min(_min, mindp[turn-1][rnext] + adj[rnext][room])
                    _max = call_max(_max, maxdp[turn-1][rnext] + adj[rnext][room])
                mindp[turn][room] = _min
                maxdp[turn][room] = _max
    _min, _max = 999999,0
    for r in range(n):
        _min = call_min(_min, mindp[m][r])
        _max = call_max(_max, maxdp[m][r])
    print "{} {}".format(_max, _min)
    n = input()
