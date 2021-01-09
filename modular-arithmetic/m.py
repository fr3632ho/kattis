
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

def bezout(a,b):
    if a < b:
        v,u = bezout(b,a)
        return (u,v)
    if b == 0: return (1,0)
    u1,v1 = bezout(b,a%b)
    return (v1,u1-a//b*v1)

while True:
    n, t = map(int, raw_input().split())
    if n==0:
        exit(0)
    for _ in range(t):
        a, op, b = raw_input().split()
        if op == '/':
            if gcd(int(b), n) != 1:
                print -1
                continue
            u, v = bezout(int(b),n)
            y = (u%n + n) %n
            print int(a)*y % n

        if op == '*':
            print ((int(a)%n)*(int(b)%n))%n
            continue

        if op == '+' or op == '-':
            print eval(a + op + b)%n
            continue
