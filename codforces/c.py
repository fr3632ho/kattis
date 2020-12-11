# THIS IS A DP problem

n, k = map(int, input().split())
nums = list(map(int, input().split()))


positions = [[] for _ in range(k+1)]
for i in range(n):
    positions[nums[i]].append(i)


answers = [-1]*n
for pos in positions[-1]:
    answers[pos] = 0


for div in range(k-1, 0, -1):
    for pos in positions[div]:
        if positions[div+1][-1] < pos:
            answers[pos] = n - pos + answers[positions[div + 1][-1]] + positions[div+1][-1]
        else:
            lo, hi = -1, len(positions[div+1])-1
            while hi - lo > 1:
                mid = (lo + hi)//2
                if positions[div+1][mid] > pos:
                    hi = mid
                else:
                    lo = mid

            answers[pos] = positions[div + 1][hi] - pos + answers[positions[div + 1][hi]]

best = 10**20
for ans in positions[1]:
    best = min(best, answers[ans])
print(best+1)






#
