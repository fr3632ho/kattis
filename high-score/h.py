
def cost(x, y):
    return min(abs(ord(x) - ord(y)), 26-abs(ord(x) - ord(y)))


def loc_closest(xs, index, right_first):
    # Return distance to closest unchanged char
    if xs[index] != aa[index]:
        return index

    left = right = index
    for _ in range(len(xs)):
        left = left-1
        right = (right+1) % n
        if right_first:
            if xs[right] != aa[right]:
                return right
        if xs[left] != aa[left]:
            return left
        if xs[right] != aa[right]:
            return right

    return 999999


t = input()
for _ in range(t):
    name = list(raw_input())
    n = len(name)
    aa = ['A']*n
    count = [0, 0]
    for i in range(2):
        curr = name[:]
        idx = 0
        while curr != aa:
            new_index = loc_closest(curr, idx, i == 0)
            change = cost(curr[new_index], aa[new_index])
            count[i] += change + \
                min(abs(idx - new_index), abs(idx-new_index) + n)
            curr[new_index] = 'A'
            idx = new_index
    print(min(count))
