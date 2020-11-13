from collections import deque

s1 = input()
s2 = input()
if s1 == s2:
    print(0)
    exit(0)
s1, s2 = deque(list(s1)), deque(list(s2))

while s1 and s2 and s1[0] == s2[0]:
    s1.popleft()
    s2.popleft()

while s1 and s2 and s1[-1] == s2[-1]:
    s1.pop()
    s2.pop()

print(len(s2))
