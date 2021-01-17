from heapq import heappush, heappop

class MaxHeap:

    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, i):
        return self.elements[i]

    def push(self, a):
        heappush(self.elements, -a)

    def pop(self):
        return -heappop(self.elements)

    def first(self):
        return self.elements[0]

class MinHeap():

    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, i):
        return self.elements[i]

    def push(self, a):
        heappush(self.elements, a)

    def pop(self):
        if not self.elements:
            return None
        return heappop(self.elements)

    def first(self):
        return self.elements[0]

class MedianStructure:

    def __init__(self):
        self.min_heap = MinHeap() # upper half
        self.max_heap = MaxHeap() # lower half

    def add(self, i):
        if not self.max_heap:
            self.max_heap.push(i)
        else:
            if i > -self.max_heap[0]:
                self.min_heap.push(i)
                if len(self.min_heap) > len(self.max_heap):
                    self.max_heap.push(self.min_heap.pop())
            else:
                self.max_heap.push(i)
                if len(self.max_heap) - 1 > len(self.min_heap):
                    self.min_heap.push(self.max_heap.pop())


    def median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -1*self.max_heap[0] )//2
        return -1*self.max_heap[0]

t = input()
for _ in range(t):
    n = input()
    m = MedianStructure()
    vals = map(int, raw_input().split())
    sum = 0
    for i in vals:
        m.add(i)
        sum += m.median()
    print sum
