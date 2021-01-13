'''
Ray Casting algorithm for each point of submarine, front and back
check if within polygon and if on bound
# if both on bound => partial
# if one bound one watere => partial
# if both land => land
# if both water => water
Need to check all polygons before print
'''

def cprod(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1] - p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])

def within_polygon_and_bound(p, polygon):
    bound = False
    count = 0
    n = len(polygon)
    for i in range(n):
        j = (i+1)%n
        p1, p2 = polygon[i], polygon[j]
        if p1[0] > p2[0]: p1, p2 = p2, p1
        if p1[0] <= p[0] < p2[0]:
            if cprod(p1, p2, p) == 0:
                bound = True
                #count = 1
                break
            if cprod(p1, p2, p) < 0:
                count += 1

        if p1[0] == p[0] ==p2[0]:
            if p1[1] <= p[1] <= p2[1] or p2[1] <= p[1] <= p1[1]:
                bound = True
                #count = 1
                break

    return count%2>0,bound

def two_points_to_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y2-y1,x1-x2,x2*y1-y2*x1)

def line_intersect(line1, line2):
    a1,b1,c1 = line1
    a2,b2,c2 = line2
    cp = a1*b2 - a2*b1
    if cp!=0:
        return ((b1*c2-b2*c1)/cp,(a2*c1-a1*c2)/cp)
    else:
        if a1*c2==a2*c1 and b1*c2==b2*c1:
            return line1
        return None

def weak_point_on_seg(seg,p):
    x,y = p
    x1, y1 = seg[0]
    x2, y2 = seg[1]
    return (x-x1)*(x-x2) <= 0 and (y-y1)*(y-y2) <= 0

def seg_intersect(seg1, seg2):
    line1 = two_points_to_line(*seg1)
    line2 = two_points_to_line(*seg2)
    p1, p2 = seg1
    p3, p4 = seg2
    p = line_intersect(line1, line2)
    if p == None:
        return None
    if len(p)==2:
        if weak_point_on_seg(seg1,p) and weak_point_on_seg(seg2,p):
            return p
        return None
    pts = [(p1[0],p1[1],0), (p2[0],p2[1],0),
            (p3[0],p3[1],1), (p4[0],p4[1],1)]
    pts.sort()
    if pts[1][0] == pts[2][0] and pts[1][1] == pts[2][1]\
            and pts[1][2] != pts[2][2]:
        return (pts[1][0],pts[1][1])
    if pts[0][2] != pts[1][2]:
        return (pts[1][0],pts[1][1],pts[2][0],pts[2][1])
    return None

def intersecting(seg, poly):
    n = len(poly)
    for i in range(n):
        j = (i+1)%n
        p = (poly[i], poly[j])
        if seg_intersect(seg, p) != None:
            return True
    return False


n = input()
subs = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, raw_input().split())
    subs.append(((x1, y1), (x2, y2)))

polys = []
m = input()
for _ in range(m):
    p = []
    for _ in range(input()):
        x, y = map(int, raw_input().split())
        p.append((x, y))
    polys.append(p)

i = 1
for sub in subs:
    p1, p2 = sub
    water = True
    for pol in polys:
        a, b = within_polygon_and_bound(p1, pol)
        c, d = within_polygon_and_bound(p2, pol)
        intersect = intersecting(sub, pol)
        #print i, sub, pol, "{}, {}, {}, {}".format(a, c, b, d)
        if (b or d) or (a^c) or intersect:
            print "Submarine {} is partially on land.".format(i)
            water = False
            break
        if a and c:
            print "Submarine {} is completely on land.".format(i)
            water = False
            break

    if water:
        print "Submarine {} is still in water.".format(i)
    i+=1
