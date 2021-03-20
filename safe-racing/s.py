l, s = map(int, raw_input().split())
mod = 123456789
dp = [1]
tot = 1
for i in range(1,l):
    dp.append(tot)

    tot += dp[-1]
    tot %= mod
    if i >= s:
        tot -= dp[-s-1]
        tot %= mod
out = 0
for i in range(s):
    out += tot
    out %= mod
    tot -= dp[-i-1]
    tot %= mod
print out
