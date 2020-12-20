'''
input => a n b m
k = n*m
x = a mod n , x = b mod m
0 <= x < k
n, m are coprime since gcd(n, m) = 1
Calculate bezout identity coefficients
ax + by = gcd(a, b)
Since n,m are coprime we have nx+my = 1
this gives us x = anx + bmy by use of the extendend euclidian algorithm
'''

def mod_inv(a, b):
    b0 = b
    x, y = 1, 0

    if b == 0: return 0

    while a > 1:
        q = a // b

        t = b

        b = a % b # b is now remainder
        a = t
        t = y
        # Update x, y
        y = x - q*y
        x = t

    if x < 0:
        x += b0

    return x

n = input()
for _ in range(n):
    a, n, b, m = map(int, raw_input().split())
    k = n*m
    x = (((a*m)%k) * mod_inv(m, n))% k
    x += (((b*n)%k) * mod_inv(n, m))% k
    x %= k
    print x, k
