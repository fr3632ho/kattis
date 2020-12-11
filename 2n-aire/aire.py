
# f(i+1, 2*a) defines the next state
# a money in current state
# max(a, p * f(i+1,2*a)), want to maximise this
# Probability can be in range [t, 1]
# For any given question there is a porbability of p that it is right
# where p is in [t, 1]
#
# At any time we might answer atleast 1 or n right
# How many should we answer in order to maximise a?
#
# k := rounds left, n:= total rounds, c:= current winnings, p = 1-t, a:= 1
# 1/p * I [t, 1] max(2^(n-k), p * f(k-1))
# This integral needs to be splitted up into two intervals
# [t, upper] and [upper, 1]
# integrate 2^(n-k) and p*f(k-1) seperately


def f():
    global n, t
    ret = 2**n
    for i in range(n, -1, -1):
        prize = 2**i
        integration_point = prize/ret
        d = 1 / (1 - t)
        if integration_point <= t:
            ret = 0.5 * (1 - t**2) * ret * d
        else:
            ret = d * prize * (integration_point - t) + 0.5 * (1 - integration_point**2) * ret* d

    return ret

n = 1
while n>0:
    n, t = map(float, input().split())
    n = int(n)
    if not n:
        exit(0)

    if t < 10**-7:
        print(2**n)
    else:
        print('%.3f' % round(f(), 3))
