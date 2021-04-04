import sys
from itertools import permutations, combinations, product
from random import randint
sys.setrecursionlimit(1000000) # default is 1000.

def can_guess(x,y):
    return 0<=x<=10**6 and 0<=y<=10**6

def make_guess(x,y):
    global n
    print(x,y,flush=True)
    ans=int(input())
    if ans==0:
        n-=1
        if n==0:
            exit(0)
    return ans
n=int(input())
for query in range(110):
    x = randint(0,10**6 - 1)
    y = randint(0,10**6 -1)
    d1 = make_guess(x,y)
    d2 = make_guess(x+1,y)
    x1double=d1-d2 + 2*x + 1
    x1=x1double//2
    ysq = d1 - (x1-x)**2
    yroot=int(ysq**0.5)
    y11 = y+yroot
    y12 = y-yroot
    if can_guess(x1,y11):
        make_guess(x1,y11)
    if can_guess(x1,y12):
        make_guess(x1,y12)
