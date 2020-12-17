import sys

# Want to maximize
# R = ax + by
# Over
# x + y <= m
# 2x + y >= sigma
# x >= 1, y >= 1
# Can be done with simplex or just increasing/decreasing x along the boundaries
a, b = map(int, raw_input().split())
m, sigma = map(int, raw_input().split())

R = 0
if a > b:
    x, y = m-1, 1
    while 2*x + y < sigma:
        x -= 1
        y += 1
else:
    x, y = 1, m-1
    while 2*x + y < sigma:
        x += 1
        y -= 1

print a*x + b*y
