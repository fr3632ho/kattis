import sys
from collections import deque

def G2(M,R,C):
    for row in range(0,R):
        for col in range(0,C):
            if row == 0:
                continue
            if M[row][col] == 'a':
                if M[row-1][col] == '.':
                    current_row = row-1
                    while not current_row < 0 and M[current_row][col] == '.':
                        M[current_row][col],M[current_row+1][col] = 'a','.'
                        current_row -= 1

    for i in range(R):
        str = ""
        for j in range(C):
            str+=M[-i-1][j]
        print(str)


def add_some_a(M,number,row,col):
    for i in range(row-1,row-number-1,-1):
        M[i][col] = 'a'

'''
If we count the number of A:s as we traverse, we can then add them on top
of eachother if we bump into a #. Makes the solution a lot faster than the G2 one..
'''
def gravity(M,R,C):
    for i in range(R):
        str=""
        for j in range(C):
            str+=M[i][j]
        print(str)

    M.append(['#']*C)
    for col in range(0,C):
        count = 0
        for row in range(0,R+1):
            if M[row][col] == 'a':
                count += 1
                M[row][col] = '.'
            elif M[row][col] == '#' and count != 0:
                add_some_a(M,count,row,col)
                count = 0
    print('_'*C)
    for i in range(R):
        str=""
        for j in range(C):
            str+=M[i][j]
        print(str)


if __name__ == "__main__":
    data = []
    for i in sys.stdin:
        data.append(i)
    R,C = map(int,data[0].strip().split())
    matrix = []
    for i in data[1:]:
        matrix.append(list(i.strip()))

    gravity(matrix,R,C)
