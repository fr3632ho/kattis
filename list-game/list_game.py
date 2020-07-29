import sys
from math import sqrt

def prime_factors(a):
    factors = []
    p, n = 2, a
    while p <= sqrt(n):
        if not n % p:
            factors.append(p)
            n = n / p
            continue
        p += 1

    print(len(factors) + 1)


def main():
    num = int(input())
    prime_factors(num)

if __name__ == '__main__':
    main()
