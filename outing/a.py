from collections import defaultdict
n, k = map(int, input().split())

def create_graph(arr):
    vals = [i for i in map(int, input().split())]

    g = defaultdict(list)
    for i, v in enumerate(vals):
        g[i+1].append(i)            

