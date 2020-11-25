# THIS IS A DP problem

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [[] for _ in range(k+1)] # N by k dimensional array since we take at least k comps

for i in range(n):
    dp[nums[i]].append(i)

for r in dp:
    print(r)
