from math import pi
m,n,r=raw_input().split()
m,n,r = int(m),int(n), float(r)
ax,ay,bx,by = map(int,raw_input().split())
dr, dx, dy = r/n, abs(ax-bx), abs(ay-by)
print(min(dr*min(ay,by)*pi/m*dx + dy*dr,ay*dr + by*dr))
