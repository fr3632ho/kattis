import sys, math
from collections import deque

to_hex = {'0000': '0',
          '0001': '1',
          '0010': '2',
          '0011': '3',
          '0100': '4',
          '0101': '5',
          '0110': '6',
          '0111': '7',
          '1000': '8',
          '1001': '9',
          '1010': 'A',
          '1011': 'B',
          '1100': 'C',
          '1101': 'D',
          '1110': 'E',
          '1111': 'F'
          }

'''
Turn each digit into it's binary representation then concatenate to binary number.
'''
def octal_to_hexadecimal(a):
    if a == 0:
        print(a)
        return

    _a = str(a)
    binary = deque([])

    for i in _a:
        binary.append(format(int(i), '03b'))

    binary = ''.join(binary)
    length = len(binary)
    #print(binary, len(binary))

    if length % 4:
        binary = '0'*(4 - length % 4) + binary

    #print(binary, len(binary))

    H = []
    for i in range(len(binary), 0, -4):
        H.append(to_hex[binary[i-4:i]])

    if H[-1] == '0':
        print(''.join(reversed(H))[1:])
        return

    print(''.join(reversed(H)))


def main():
    num = int(input())
    octal_to_hexadecimal(num)

if __name__ =='__main__':
    main()
