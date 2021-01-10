import sys

for line in sys.stdin:
    n = int(line.strip())
    if n>1:
        print 2*(n-1)
    else:
        print 1
