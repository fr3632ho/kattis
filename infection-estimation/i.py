'''
From our participation in NCPC 2020
'''

import math
import sys
def calc_k(x):
    #our guess is x, what k should we pick?

    return math.log(0.5)/math.log((10.0**7-x)/10.0**7)

guess = 22360

for i in range(15):
    k = int(round(calc_k(guess)))
    print "test",k
    sys.stdout.flush()
    ans = input()
    if ans == 1:
        guess*=2-i*(0.8/15)
    elif ans == 0:
        guess/=2-i*(0.8/15)
    guess = max(100,guess)
    guess = min(5000000,guess)
tot = 1
for i in range(35):
    k = int(round(calc_k(guess)))
    print "test",k
    sys.stdout.flush()
    ans = input()
    if ans == 1:
        guess*=1.3-i*(0.15/35)
    elif ans == 0:
        guess/=1.3-i*(0.15/35)
    guess = max(100,guess)
    guess = min(5000000,guess)
    tot*=guess

out = int(tot**(1/35.0))
out = max(199,out)
out = min(2500001,out)
print "estimate",out
