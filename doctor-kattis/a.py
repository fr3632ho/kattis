from heapq import heapify, heappush, heappop
'''
0 check in at clinic
1 update infection level
2 treated cat
3 print cat with highest infection level

Need to use heap structure
'''

class Cat:

    def __init__(self, name, level, order):
        self.name = name
        self.level = level
        self.order = order

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        if self.level == other.level:
            return self.order < other.order
        return self.level > other.level

    def __hash__(self):
        return hash((self.name, self.order))

    def update(self, i):
        self.level = min(100, self.level + i)


class CatHeap:

    def __init__(self):
        self.cats = []
        self.catdict = dict()

    def __len__(self):
        return len(self.cats)

    def push(self, c):
        self.catdict[c.name] = c
        heappush(self.cats, c)

    def remove(self, name):
        return self.catdict.pop(name, None)

    def update(self, name, level):
        self.catdict[name].update(level)

    def print_top(self):
        if not self.cats:
            print("The clinic is empty")
            return

        while self.cats[0].name not in self.catdict:
            heappop(self.cats)
            if not self.cats:
                print("The clinic is empty")
                return

        print(self.cats[0].name)


n = int(input())
c = CatHeap()
for i in range(n):
    q = input().split()
    if q[0] == '0':
        c.push(Cat(q[1], int(q[2]), i))
    elif q[0] == '1':
        c.update(q[1], int(q[2]))
    elif q[0] == '2':
        c.remove(q[1])
    else:
        c.print_top()
