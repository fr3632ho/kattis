queen = '*'
queens = []
for i in range(8):
    query = raw_input()
    for j in range(8):
        if query[j]==queen:            
            for x,y in queens:
                dx = abs(x-j)*1.0
                dy = abs(y-i)*1.0
                if dx != 0 and dy/dx==1.0:
                    print "invalid"
                    exit(0)
                elif x==j or y==i:
                    print "invalid"
                    exit(0)
            queens.append((j,i))
if len(queens)!=8:
    print "invalid"
else:
    print "valid"
