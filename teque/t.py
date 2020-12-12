from collections import deque
import sys

def balance(front, back):
    if len(back)-len(front) == 1:
        front.append(back.popleft())

    elif len(front)-len(back) == 2:
        back.appendleft(front.pop())


def mid_push(front, back, num):
    if len(front) < len(back):
        front.append(num)
    else:
        back.appendleft(num)

def get_op(front, back, i):
    if len(front) == i:
        return back[0]
    elif len(front) > i:
        return front[i]
    else:
        return back[i - (len(front))]


b = "push_back"
f = "push_front"
m = "push_middle"
get = "get"

front, back = deque([]), deque([])

N = int(input())
for line in sys.stdin:
    operation, num = line.split()
    num = int(num)
    #print(operation, num)
    if operation == b:
        back.append(num)
    elif operation == f:
        front.appendleft(num)
    elif operation == m:
        mid_push(front, back, num)
    else:
        print(get_op(front, back, num))

    balance(front, back)
