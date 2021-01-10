import sys

def print_iter(adj, s, root):
    stack = [root]
    while stack:
        node = stack.pop()
        sys.stdout.write(s[node])
        ls = adj[node]
        for i in reversed(adj[node]):
            stack.append(i)

    sys.stdout.flush()
    sys.stdout.close()

n = input()
strings = [""]*n
for i in range(n):
    strings[i] = raw_input()

adj = [[]for _ in range(n)]
last = -1
for _ in range(n-1):
    a, b = map(lambda x : int(x) - 1, raw_input().split())
    adj[a].append(b)
    last = a

print_iter(adj, strings, last)
