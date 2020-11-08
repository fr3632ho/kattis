from heapq import heappush, heappop

n = int(input())
coins = list(map(int, input().split()))

s = sum(coins)
if max(coins)*2 > s or s%2 == 1: # One stack has more coins than half available
    print("no")
    exit(0)

heap = []
for i in range(n):
    if coins[i] > 0:
        heappush(heap, (-coins[i], i))

print("yes")
while heap:
    c1, j1 = heappop(heap)
    c2, j2 = heappop(heap)
    print(j1+1, j2+1)
    c1, c2 = -c1, -c2
    if c1-1>0:
        heappush(heap, (-(c1-1), j1))
    if c2-1>0:
        heappush(heap, (-(c2-1), j2))
