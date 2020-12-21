'''
Problem strucutred as a memoization problem..
Iteratively walk through each and every dam, use the id of the one below to check
for current water needed to break the dam.

for index in [0, n-1]
    di, ci, ui := dam[index]
    needed rain is at dp[index]

    current needed rain is given by the maximum of the capcaity - current volume vs
    needed volume - current volume.
    With this we can append the rain value to the memoization data structure

    the best current answer is best := min(rain, previous best)
end
'''

n, w = map(int, raw_input().split())
dams = []
for _ in range(n):
    d, c, u = map(int, raw_input().split())
    dams.append((d, c, u))
# Memoization
dp = [w]
best = w
for i in range(n):
    d, c, u = dams[i]
    wneed = dp[d]
    rain = max(c - u, wneed - u) # Capacity vs. current capacity
    dp.append(rain)
    best = min(rain, best)
print best
