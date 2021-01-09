from math import sqrt, floor, ceil

primes = set()
def is_prime(n):
    if n in primes:
        return True

    if n <= 1: return False
    if n <= 3:
        primes.add(n)
        return True
    if not n%2 or not n%3: return False

    i = 5
    while i*i <= n:
        if n%i == 0 or n % (i + 2) == 0:
            return False
        primes.add(i+2), primes.add(i)
        i+= 6
    primes.add(n)
    return True

mx = 0
while True:
    n = input()
    if n == 0:
        exit(0)

    flag = is_prime(n)
    old = n
    n *= 2
    n +=1
    while not is_prime(n):
        n+=1
    if not flag:
        print n, "({} is not prime)".format(old)
    else:
        print n
