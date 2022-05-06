def calc_poly_area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]        
        area += x1*y2 - x2*y1
    return abs(area/2)

from math import cos, sin, radians

def rotate_rectangle(rectangle, v):
    out = []
    for x, y in rectangle:
        x1 = x * cos(radians(v)) - y * sin(v)
        y1 = x * sin(radians(v)) - y * cos(v)
        out.append((x1, y1))
    return out   

# test 1

rect1 = [(0,0), (2,0), (2,2), (0, 2)]
rect2 = [(0,0), (3,0), (3,3), (0, 3)]

print(rotate_rectangle(rect1, 45))
print(rotate_rectangle(rect1, 20))