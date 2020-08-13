
def main():
    t = int(input())
    for j in range(t):
        dim = int(input())
        v1 = list(map(int, input().split()))
        v2 = list(map(int, input().split()))
        v1.sort(), v2.sort()
        #print(v1, v2)
        res = 0
        for i in range(dim):
            res += v1[i]*v2[-(i+1)]

        print("Case #{}: {}".format(j+1, res))

if __name__ == '__main__':
    main()
