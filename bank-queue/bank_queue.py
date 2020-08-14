from heapq import heappush, heappop

class Node:

    def __init__(self, time, cost):
        self.time = time
        self.cost = cost

    def get_attributes(self):
        return self.time, self.cost

    def __repr__(self):
        return "({}, {})".format(self.time, self.cost)

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.time < other.time
        return self.cost > other.cost

def main():
    '''
    Greedy method.

    Insert if latest possible time slot is free, otherwise iterate backwards and
    check if earlier time slots are empty. If not, then the job cannot be done, else
    assign the job to the slot. If a slot is free in any of the cases we include the profit
    of the job.
    '''
    n, t = map(int, input().split())

    heap = []
    for i in range(n):
        cost, time = map(int, input().split())
        heappush(heap, Node(time, cost))

    passed = [False]*t
    profit = 0
    while heap:
        time, p = heappop(heap).get_attributes()
        if not passed[time]:
            passed[time] = True
            profit += p
        elif passed[time]:
            i = time
            while i > -1:
                if not passed[i]:
                    passed[i] = True
                    profit += p
                    break
                i -= 1

    print(profit)


if __name__ == "__main__":
    main()
