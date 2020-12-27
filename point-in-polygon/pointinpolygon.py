def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
n = input()
while n!=0:
    polygon = []
    for i in range(n):
        x,y = map(int,raw_input().split())
        polygon.append((x,y))
    m = input()
    for t in range(m):
        x,y = map(int,raw_input().split())
        p = (x,y)
        count = 0
        bound = False
        for j in range(n):
            p1 = polygon[j-1]
            p2 = polygon[j]
            if p1[0]>p2[0]:
                p1,p2=p2,p1
            if p1[0]<=x<p2[0]:
                if ccw(p,p1,p2) == 0:
                    bound = True
                if ccw(p,p1,p2) > 0:
                    count+=1
            if p1[0]==x==p2[0]:
                if p1[1]<=y<=p2[1] or p2[1]<=y<=p1[1]:
                    bound = True
        if bound:
            print "on"
        elif count%2==0:
            print "out"
        else:
            print "in"

    n = input()
