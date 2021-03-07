S,x,y,dx,dy = map(int, raw_input().split())
while S+x+y+dx+dy != 0:
    jumps = 0
    if x//S%2 and y//S%2:
