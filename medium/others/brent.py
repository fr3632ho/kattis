import math
"""
Implementation of Brent's 'Tortoise & Hare' based of of Floyd's but a bit faster.
The algorithm is a pointer based algorithm which detects cycles of any given length,
where the cycle begins from the starting point in the sequence and a repeated value.
The algorithm compares two pointers moving at different speeds; the tortoise and the hare.
If the hare catches up to the tortoise, thus sharing the same index again in the sequence,
a cycle exists in the sequence. Brent's algorithm searches for the smalles power of
2**i which is larger than borth lambda and mu for i = 0,1,2...
"""

sequence = [1,2,3,4,5,6,6,7,8,9,10]

def f(x):
    if sequence.index(x)+1 == len(sequence):
        return sequence[0]
    return sequence[sequence.index(x)+1]

def brent(x0):
    power,lam = 1,1
    tortoise = x0
    hare = f(x0)

    # Beginning phase
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    hare = tortoise = x0
    for i in range(lam):
        hare = f(hare)

    mu = 0

    # End phase
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam,mu,hare

x0 = 0
x1 = 4
lam,mu,value = brent(sequence[x0])
lam1,mu1,value1 = brent(sequence[x1])
print(
'''
start-index: {},
sequence: {},
cycle-length: {},
index from starting point (positive direction): {},
repeated value: {}'''.format(x0,sequence,lam,mu,value))

print(
'''
start-index: {},
sequence: {},
cycle-length: {},
index from starting point (positive direction): {},
repeated value: {}'''.format(x1,sequence,lam1,mu1,value1))
