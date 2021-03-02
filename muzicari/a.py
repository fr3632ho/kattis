from collections import Counter, deque

class StopRec(Exception):
    pass

class Queue:

    def __init__(self, t):
        self.total = t
        self.used = 0
        self.queue = deque()

    def push(self, index, time):
        if self.used + time > self.total:
            return False
        self.queue.append((index, self.used))
        self.used += time
        return True

    def undo_push(self, time):
        self.time -= time
        self.queue.pop()

    def get_used(self):
        return self.used

def rec_call(rest, counter, queues, dp):
    if not rest:
        queues[0].queue += queues[1].queue
        print " ".join([str(t0) for _, t0 in sorted(queues[0].queue, \
                                                key=lambda z : z[0]) ])
        raise StopRec

    stamp = (queues[0].get_used(), queues[1].get_used(), counter[rest[-1][1]])
    if stamp in dp:
        return

    index, time = rest.pop() # largest element in rest
    for q in queues:
        if q.push(index, time):
            counter[time] -= 1
            rec_call(rest, counter, queues, dp)
            q.undo_push(time)
            counter[time] += 1
    rest.append((index, time))
    dp.add(stamp)


t,_ =map(int, raw_input().split()) # 1<= T <= 5000, 1<=N<=500
musicians = sorted(enumerate(map(int, raw_input().split())),key=lambda x : x[1])
counter = Counter(x for _,x in musicians)
Q = [Queue(t), Queue(t)]
mem = set()
try:
    rec_call(musicians, counter, Q, mem)
except Exception:
    pass
