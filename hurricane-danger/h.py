

def two_points_to_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y2-y1,x1-x2,x2*y1-y2*x1)

def proj_onto_line(p, line):
