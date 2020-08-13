from heapq import heappush, heappop

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        totals = []
        for _ in range(n):
            tot = sum(map(int, input().split()[1:]))
            heappush(totals, tot)

        s = total_time = 0
        for i in range(n):
            s += heappop(totals)
            total_time += s

        print("{:.10f}".format(total_time/n))


if __name__ == '__main__':
    main()
