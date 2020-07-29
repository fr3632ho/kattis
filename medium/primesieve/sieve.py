import sys
from math import sqrt, floor, ceil
import os, psutil

primes = [] # List containing all primes
is_prime = set()

def sieve_of_eratosthenes(n):
    '''Simple implemenatiton with O(n) memory complexity'''
    xs = [True for i in range(n + 1)]
    p = 2
    while p < n:
        if xs[p]:
            primes.append(p), is_prime.add(p)
            for i in range(p * p, n + 1, p):
                xs[i] = False
        p += 1

def segmented_sieve(n):
    block = int(floor(sqrt(n)) + 1) # Block size
    # Attain the sieveing primes
    sieve_of_eratosthenes(block)

    # High and low bounds, initiate at second block
    low, high = block, 2 * block

    while low < n:

        if high > n: # If on the last block
            high = n + 1

        flag = [True for _ in range(block + 1)]

        for i in range(len(primes)):
            # Find the index for the composite of every prime
            # Ex, if l := 44, primes[i] = 3 => indx := 14*3 = 42
            # Then we step from there!
            indx = ceil(low/primes[i]) * primes[i]

            for j in range(indx, high, primes[i]):
                flag[j-low] = False # Mark the composites

        for k in range(low, high):
            if flag[k - low]:
                is_prime.add(k)

        # Update the range!
        low, high = low + block, high + block


def isPrime(a):
    return a in is_prime

def get_memory_usage():
    print('--------')
    pid = os.getpid()
    print(pid)
    ps = psutil.Process(pid)
    memory_used = ps.memory_info()
    print(memory_used)
    print('--------')

def main():
    n, q = map(int, sys.stdin.readline().split(' '))

    segmented_sieve(n)

    print('size of sieves',sys.getsizeof(primes))
    print('size of all', sys.getsizeof(is_prime))
    print(len(is_prime))
    for _ in range(q):
        query = int(input())
        if isPrime(query):
            print('1')
        else:
            print('0')

    get_memory_usage()


if __name__ == "__main__":
    main()
