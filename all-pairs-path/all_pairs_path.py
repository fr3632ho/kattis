import sys


INF = 1000000000
'''
Floyd-Warshall algorithm for all pairs shortest path.
Takes a matrix A with set edge relations and computes minimal distance between
each and every node.
'''
def floyd_warshall(A, n):
    # Perform Floyd warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] < INF and A[k][j] < INF:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    # Negative cycles
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][j] != -INF:
                    if A[k][k] < 0 and A[i][k] != INF and A[k][j] != INF:
                        A[i][j] = -INF


def main():
    n, m, q = map(int, sys.stdin.readline().split())
    while True:
        # Create matrix
        matrix = [[0 if i == j else INF for i in range(n)] for j in range(n)]

        for edge in range(m):
            u, v, w = map(int, sys.stdin.readline().split())

            if u == v:
                matrix[u][v] = 0
            elif matrix[u][v] > w: # Pick the edge with smallest weight
                matrix[u][v] = w

        floyd_warshall(matrix, n)

        # Queries to be answered
        for query in range(q):
            u, v = map(int, sys.stdin.readline().split())

            dist = matrix[u][v]

            if dist == -INF:
                print('-Infinity')
            elif dist == INF:
                print('Impossible')
            else:
                print(dist)

        n, m, q = map(int, sys.stdin.readline().split())

        if not (n + m + q):
            break
        print()

if __name__ == '__main__':
    main()
