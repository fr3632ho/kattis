# Union Find problem
import sys

class Network:

    def __init__(self, N):
        self.parents = [[i, ''] for i in range(2*N)]
        self.p_indices = dict()
        self.sizes = [1]*(2*N)
        self.index = 0

    '''
    Add every person to the network iff key not present in p_indices
    '''
    def add_new(self, *args):
        for i in args:
            if i not in self.p_indices.keys():
                self.parents[self.index][1] = i
                self.p_indices[i] = self.index
                self.index += 1

    '''
    Locate root of every person by index.
    '''
    def n_find(self, v):
        v_index = self.p_indices[v]
        root = v_index
        # find root
        while root != self.parents[root][0]:
            root = self.parents[root][0]

        # [v-index, v-name], path compression
        p = self.parents[v_index]
        while p[0] != root:
            # Parent of p
            _p = self.parents[p[0]]
            # Only change the parent of each element in the parent list
            p[0] = root
            p = _p

        return root

    def n_union(self, u, v):
        u_parent, v_parent = self.n_find(u), self.n_find(v)
        connected = 0

        if u_parent == v_parent:
            connected = max(self.sizes[u_parent], self.sizes[v_parent])
        elif self.sizes[u_parent] > self.sizes[v_parent]:
            self.parents[v_parent][0] = u_parent
            self.sizes[u_parent] += self.sizes[v_parent]
            connected = self.sizes[u_parent]
        else:
            self.parents[u_parent][0] = v_parent
            self.sizes[v_parent] += self.sizes[u_parent]
            connected = self.sizes[v_parent]

        print(connected)

def main():
    # Query handling
    T = int(sys.stdin.readline().strip())
    for test in range(T):
        F = int(sys.stdin.readline().strip())
        network = Network(F)
        for i in range(F):
            a, b = sys.stdin.readline().strip().split()
            network.add_new(a, b)
            network.n_union(a, b)



if __name__ == '__main__':
    main()


# END
