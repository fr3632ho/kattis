
t = input()
for _ in range(t):
    n = input() # length of walk
    if n==1:
        print 0
        continue

    newgrid = {}
    newgrid[(0,0)] = 1
    dir = [(-2, 0), (2, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(n+1):
        grid = newgrid
        newgrid = {}
        for r, c in grid:
            for dx, dy in dir:
                if (r+dx, c+dy) in newgrid:
                    newgrid[(r+dx, c+dy)] += grid[(r, c)]
                else:
                    newgrid[(r+dx, c+dy)] = grid[(r, c)]

    print grid[(0,0)]
