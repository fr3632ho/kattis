from collections import deque

COAST = "1"
SEA = "0"

def get_neighbours(G, y, x, m, n):
    ret = []

    if x > 0:
        ret.append((y, x - 1))
    if x  < m + 1:
        ret.append((y, x + 1))
    if y > 0:
        ret.append((y - 1, x))
    if y < n + 1:
        ret.append((y + 1, x))

    return ret


def coast_length(G, m, n):
    visited = [[False]*(m+2) for _ in range(n+2)]
    Q = deque([(0, 0)])
    total_coast = 0
    while Q:
        y, x = Q.pop()

        if visited[y][x]:
            continue

        visited[y][x] = True
        neighbours = get_neighbours(G, y, x, m, n)
        for _y, _x in neighbours:
            if G[_y][_x] == COAST:
                total_coast += 1
            elif G[_y][_x] == SEA and not visited[_y][_x]:
                Q.appendleft((_y, _x))

    return total_coast

def main():
    n, m = map(int, input().split())
    mat = deque(['0' + input() + '0' for _ in range(n)])

    mat.appendleft('0'*(m+2))
    mat.append('0'*(m+2))

    print(coast_length(mat, m, n))



if __name__ == "__main__":
    main()
