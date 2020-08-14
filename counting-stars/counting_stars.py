from collections import deque

BLACK = "#"
STAR = "-"

def get_neighbours(G, y, x, n, m):
    ret = []
    if x > 0:
        ret.append((y, x - 1))
    if x < m - 1:
        ret.append((y, x + 1))
    if y > 0:
        ret.append((y - 1, x))
    if y < n - 1:
        ret.append((y + 1, x))

    return ret


def BFS(G, start, visited, n, m):
    Q = deque([start])
    while Q:
        y, x = Q.pop()
        if visited[y][x]:
            continue

        visited[y][x] = True
        neighbours = get_neighbours(G, y, x, n, m)
        for _y, _x in neighbours:
            if G[_y][_x] != BLACK and not visited[_y][_x]:
                Q.appendleft((_y, _x))


def main():
    try:
        c = 1
        for _ in range(50):
            n, m = map(int, input().split())
            mat = [input() for _ in range(n)]
            visited = [[False]*m for _ in range(n)]
            stars = 0
            for i in range(n):
                for j in range(m):
                    if mat[i][j] == STAR and not visited[i][j]:
                        stars += 1
                        BFS(mat, (i, j), visited, n, m)

            print("Case {}: {}".format(c, stars))
            c += 1

    except EOFError:
        return

if __name__ == '__main__':
    main()
