'''Useful for simulation problems and combinatorics'''

'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp())
def nl(): return [int(tok) for tok in inp().split()]

def simulate(node, board, dist):

    def get_neighbours(y, x, board):
                # dy, dx
                check = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

                def bounds(y, x): 
                    return (0 <= y < 10) and  (0 <= x < 10)

                for dy, dx in check:
                    if bounds(y-dy, x-dx) and board[y - dy][x - dx] == 0:
                        if bounds(y-(2*dy), x-(2*dx)) and str(board[y-(2*dy)][x-(2*dx)]) in '#.':                            
                            yield (y-(2*dy), x-(2*dx)), (y-dy, x-dx)
    
    def pretty_print(y, x, board):
        _p = board[y][x]
        board[y][x] = 'P'
        print("-"*40)
        print(y, x)        
        print('    ' + '   '.join(str(i) for i in range(10)) + '\n')
        print('\n'.join(['   '.join([str(i)] + [str(cell) for cell in row]) for i, row in enumerate(board)]))
        print("-"*40)
        board[y][x] = _p

            
    y, x = node

    #pretty_print(y, x, board)
    m = dist
    for (new_y, new_x), (r_y, r_x) in get_neighbours(*node, board):
        board[y][x] = '#'
        board[r_y][r_x] = '#'
        board[new_y][new_x] = 1
        m = max(m, simulate((new_y, new_x), board, dist + 1))
        board[y][x] = 1
        board[r_y][r_x] = 0
        board[new_y][new_x] = '#'

    return m

t = ni()
for _ in range(t):
    board = [['#' for _ in range(10)] for _ in range(10)]
    inp()
    check = []
    for i in range(10):
        for j, tok in enumerate(nl_2()):
            if tok == 'W' or tok == 'B':
                board[i][j] = (tok=='W')*1
            if tok =='W':
                check.append((i, j))    

    m = 0
    for node in check:
        m = max(m, simulate(node, board, 0))
    
    print(m)

    

