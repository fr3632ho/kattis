'''
ans[i] |= [current row]
'''
n = input()
ans = [0]*n
out = []
for i in range(n):
    for j in map(int, raw_input().split()):
        ans[i] |= j
    out.append(str(ans[i]))

print " ".join(out)
