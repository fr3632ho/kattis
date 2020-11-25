from collections import deque
n = int(input())
#nbrs = map(int, input().split())
M = 10**9 + 7

tot = 0
ones = 0
p = 0
for num in input().split():
    if num == '1':
        ones += 1
    if num == '2':
        p *= 2
        p += ones
        p %= M
    if num == '3':
        tot += p
        tot %= M

print(tot)
