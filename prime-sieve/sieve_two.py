import sys

remainder_bit = [0, 0x01, 0, 0, 0, 0x02,
                 0, 0x04, 0, 0, 0, 0x08,
                 0, 0x10, 0, 0, 0, 0x20,
                 0, 0x40, 0, 0, 0, 0x80]

def is_prime(xs, a):
    if a <= 3:
        return a > 1
    index, r = divmod(a, 24) # Returns quotient and remainder, slow
    bit = remainder_bit[r]
    if not bit:
        return False
    else:
        return not (xs[index] & bit)

def adjust_composits(xs, p, c):
    count = c
    for i in range(5 * p, n + 1, p):
        index, rem = divmod(i, 24) # Bottle neck!
        bit = remainder_bit[rem]
        if bit and not (xs[index] & bit):
            xs[index] |= bit
            count -= 1
    return count

def sieve_of_eratosthenes(xs, n):
    count = (n // 3) + 1
    p = 5

    while p*p <= n:
        if is_prime(xs, p):
            count = adjust_composits(xs, p, count)

        p += 2

        if is_prime(xs, p):
            count = adjust_composits(xs, p, count)

        p += 4

    return count

def init_sieve(n):
    return bytearray((n + 23) // 24)

n = 10000000
xs = init_sieve(n)
print(sieve_of_eratosthenes(xs, n))
