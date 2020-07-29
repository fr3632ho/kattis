import sys
from math import sqrt,pow


def compute_Z(z_re,z_im,x,y,iter):
    if iter < 0:
        return True
    else:
        if sqrt(pow(z_re,2) + pow(z_im,2)) > 2:
            return False
        z_next_re = pow(z_re,2) - pow(z_im,2) + x
        z_next_im = 2*z_re*z_im + y
        return compute_Z(z_next_re,z_next_im,x,y,iter-1)


if __name__ == "__main__":
    data = []
    for i in sys.stdin:
        data.append(i)
    points = [ [float(i) for i in line.rstrip('\n').split(' ')] for line in data]

    for i,point in enumerate(points):
        x,y,iterations = point
        z_re = z_im = 0
        #print('X:{}, Y:{},Iterations:{}'.format(x,y,iterations))
        str = f'Case {i+1}:'
        if compute_Z(z_re,z_im,x,y,iterations):
            str += " IN"
        else:
            str += " OUT"
        print(str)
