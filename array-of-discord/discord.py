n = int(input())
s = list(input().split())

for i, c in enumerate(s):
    j = (i+1)%n
    if j == 0:
        break

    a, b = s[i], s[j]
    if len(a) != len(b):
        continue

    _a, _b = int(a), int(b)
    if len(a) == 1:
        for dig in range(10):
            if _b <= 9 and _a > 0:
                b = str(0)
                s[j] = b
                print(" ".join(s))
                exit(0)
            elif dig > _b:
                a = str(dig)
                s[i] = a
                print(" ".join(s))
                exit(0)
    else:
        for k, char in enumerate(a):
            if k==0:
                for dig in range(1, 10):
                    if int(str(dig) + a[1:]) > _b:
                        a = str(dig) + a[1:]
                        s[i] = a
                        print(" ".join(s))
                        exit(0)

                    elif int(str(dig) + b[1:]) < _a:
                        b = str(dig) + b[1:]
                        s[j] = b
                        print(" ".join(s))
                        exit(0)

            else:
                for dig in range(10):
                    if int(a[:k] + str(dig) + a[k+1:]) > _b:
                        a = a[:k] + str(dig) + a[k+1:]
                        s[i] = a
                        print(" ".join(s))
                        exit(0)

                    elif int(b[:k] + str(dig) + b[k+1:]) < _a:
                        b = b[:k] + str(dig) + b[k+1:]
                        s[j] = b
                        print(" ".join(s))
                        exit(0)


print("impossible")
