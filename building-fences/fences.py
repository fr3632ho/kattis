from heapq import heappush, heappop

K, N = map(int, input().split())
poles = list(map(int, input().split()))
l = []
for i in poles:
    heappush(l, (-w, w, 1))

# Needs N-1 poles of equal length
# Have K poles
# Find a optimal hight for equal length of all poles
for i in range(N):
