import sys

'''
Union-Find data structure for the kattis problem "Union-Find".
'''
class Sets:

    def __init__(self, n):
        self.sizes  = [1]*n
        self.parents = [i for i in range(n)]

    '''
    Check if u, v are connected in the same tree
    '''
    def is_connected(self, u, v):
        return self.find_parent(u) == self.find_parent(v)

    '''
    Union between u,v
    Compare on number of children
    '''
    def union(self, u, v):
        x_parent, y_parent = self.find_parent(u), self.find_parent(v)

        if x_parent == y_parent:
            return

        if self.sizes[x_parent] > self.sizes[y_parent]:
            self.parents[y_parent] = x_parent
            self.sizes[x_parent] += self.sizes[y_parent]
        else:
            self.parents[x_parent] = y_parent
            self.sizes[y_parent] += self.sizes[x_parent]


    '''
    Find parent of u and parent of v and move them up the tree structure
    '''
    def find_parent(self, v):
        root = v
        # First find the root
        while root != self.parents[root]:
            root = self.parents[root]
        # Path compression
        while v != root:
            _p = self.parents[v]
            self.parents[v] = root
            v = _p

        return root

N = int(sys.stdin.readline().strip().split()[0])
sets = Sets(N)
for i in sys.stdin:
    q = i.strip().split()
    print(q)
    if q[0] == '=':
        sets.union(int(q[1]), int(q[2]))
    else:
        if sets.is_connected(int(q[1]), int(q[2])):
            print("yes")
        else:
            print("no")
