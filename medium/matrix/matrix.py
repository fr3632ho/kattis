import sys

def inverse(a,b,c,d,case):
    det = 1/(a*d - b*c)
    a_prime,d_prime,b_prime,c_prime = int(d*det),int(a*det),int(-b*det),int(-c*det)
    print(f'Case {case}:')
    print(f'{a_prime} {b_prime}\n{c_prime} {d_prime}')

if __name__ == "__main__":

    data = []
    for i in sys.stdin:
        data.append(i)

    matrices = []
    for i in range(0,len(data),3):
        matrices.append([int(i) for i in data[i].strip('\n').split()])
        matrices.append([int(i) for i in data[i+1].strip('\n').split()])

    case = 1
    for i in range(0,len(matrices),2):
        a,b = [int(j) for j in matrices[i]]
        c,d = [int(j) for j in matrices[i+1]]
        inverse(a,b,c,d,case)
        case+=1
