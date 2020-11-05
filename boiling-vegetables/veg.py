from heapq import heappush, heappop

T, N = input().split()
T, N = float(T), int(N)

p = map(int, input().split())
Q = []
for w in p:
    heappush(Q, (-w, w, 1))

m = -max(Q)[0]
cuts = 0
while True:
    _w, w, c = heappop(Q)
    q = m/(-_w)
    if q >= T: break

    _c = -w/(c+1)
    m = min(m, -_c)
    cuts += 1
    heappush(Q, (_c, w, c+1))

print(cuts)
