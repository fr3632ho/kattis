from math import pow
from collections import defaultdict
from heapq import heappush, heappop

def main():
    n = int(input())
    dim = int(pow(n, (1. / 3)) + 1)

    freq_map = defaultdict(list)
    answers = []
    for i in range(dim):
        for j in range(dim):
            q = pow(i, 3) + pow(j, 3)
            if q > n:
                continue
            if not freq_map[q]:
                freq_map[q] = [1, (i, j)]
            elif freq_map[q][1] != (i, j) and freq_map[q][1] != (j, i):
                freq_map[q].append((i, j))
                freq_map[q][0] = freq_map[q][0] + 1

            if len(freq_map[q]) > 2:
                heappush(answers, -q)

    if len(answers) > 0:
        print("{}".format(int(heappop(answers)*-1)))
    else:
        print("none")


    #print(freq_map)

if __name__ == "__main__":
    main()
