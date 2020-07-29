import sys

def find(p, a):
    root = a
    while root != p[root]: root = p[root]
    while a != root:
        _a = p[a]
        p[a] = root
        a = _a
    return root

def union(s, p, a, b):
    a, b = find(p, a), find(p, b)
    if a == b: return
    if s[b] > s[a]:
        temp = a
        a = b
        b = temp

    s[a] += s[b]
    p[b] = a

def int_sub(a):
    return int(a) - 1

'''
Binary has to stay inside path with zeros.
'''
def main():
    r, c = map(int, sys.stdin.readline().strip().split())
    graph = [sys.stdin.readline().strip() for _ in range(r)]

    parents = [i for i in range(r*c)]
    sizes = [1]*(r*c)

    for i in range(r):
        for j in range(c):
            if j + 1 < c and int(graph[i][j]) == int(graph[i][j+1]):
                union(sizes, parents, i*c + j, i*c + j + 1)
            if i + 1 < r and int(graph[i][j]) == int(graph[i+1][j]):
                union(sizes, parents, i*c + j, (i+1)*c + j)

    n = int(sys.stdin.readline().strip())
    for query in range(n):
        r1, c1, r2, c2 = map(int_sub, sys.stdin.readline().strip().split())
        start, end = r1*c + c1, r2*c + c2
        s_root, e_root = find(parents, start), find(parents, end)
        if find(parents, start) == find(parents, end):
            print("decimal") if int(graph[r1][c1]) else print("binary")
        else:
            print("neither")


if __name__ == "__main__":
    main()
