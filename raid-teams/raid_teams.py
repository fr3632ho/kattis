import sys
from heapq import heappush, heappop

def int_neg(a):
    return int(a)*-1

def main():
    N = int(input())
    s1, s2, s3 = [], [], []
    for _ in range(N):
        query = sys.stdin.readline().split()
        name = query[0]
        v1, v2, v3  = map(int_neg, query[1:])
        heappush(s1, (v1, name))
        heappush(s2, (v2, name))
        heappush(s3, (v3, name))
        #print('%s  [%d %d %d]' % (name, v1, v2, v3))

    S = [s1, s2, s3]
    taken = set()
    while s1 and s2 and s3:
        string = ""
        check = True
        indx = 0
        for player_list in S:
            while player_list:
                val, player = heappop(player_list)
                if player not in taken:
                    string += player
                    if indx < 2:
                        string += " "
                    taken.add(player)
                    break
                elif not player_list:
                    check = False
            indx += 1

        if check:
            print(string)
        if not check:
            if len(string.split()) == 3:
                print(string)


if __name__ == "__main__":
    main()
