import sys
from math import sqrt

def find_factors(a):
    factors = [1]

    for i in range(2, int(sqrt(a) + 1) ):
        if a % i == 0:
            if a//i != i:
                factors.append(i), factors.append(a//i)
            else:
                factors.append(i)

    return(factors)

def main():
    for i in sys.stdin:
        query = int(i.strip())
        factors = find_factors(query)

        s = abs(sum(factors) - query)
        if s == 0:
            print(query, "perfect")
        elif s <= 2:
            print(query, "almost perfect"rt)
        else:
            print(query, "not perfect")


if __name__ == '__main__':
    main()
