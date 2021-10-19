from itertools import permutations
A,B = map(int, input().split())
delta = (A+B)//2
out = permutations('abcdefghijklmnopqrstuvwxyz', 4)
print(' '.join(''.join(next(out)) for _ in range((A+B)//2)))