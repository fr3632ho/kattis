import sys
from collections import defaultdict

# Valid stone states are 001, 010, 100
# 1, 2, 4

d = {0: [-1, -1, -1], 1: [-1, -1, 1], 2: [-1, 1, -1], 3: [-1, 1, 1],
     4: [1, -1, -1], 5: [1, -1, 1], 6:[1, 1, -1], 7: [1, 1, 1]}

n = input()
for _ in range(n):
    m = input()

    p = []
    for _ in range(m):
        q = map(lambda x : int(x) - 1, raw_input().split())
        sc = []
        for i in range(8):
            if q[i] != 0:
                sc.append([(8 - i) * j for j in d[q[i]]])
        p.append(sc)

    score = [0, 0, 0]
    for priest in p:
        for vote in priest:
            score = [sum(x) for x in zip(score, vote)]


    for pr in p:
        print(pr)
    print score
    print "------"
