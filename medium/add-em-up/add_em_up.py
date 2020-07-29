import sys
from collections import defaultdict


fl = [0, 1, 2, -1, -1, 5, 9, -1, 8, 6]

'''
Calculates if a sum of two cards == s is possible
'''
def possible_sum(xs, s, n):
    mappings = defaultdict(set)
    num, alt = [0]*n, [0]*n

    # Construct two lists with their alternative value
    for x in range(n):
        a = xs[x]
        flipped = flip(a)
        num[x], alt[x] = a, flipped
        mappings[a].add(x)

        # Add the flipped card to the mappings
        if flipped != -1 and flipped != a:
            mappings[flipped].add(x)

    # Now we want to see if it's possible to form the sum from two cards
    for x in range(n):
        a, flipped = num[x], alt[x]
        needed = s - a

        # remove the current card from the needed number set
        if needed in mappings:
            new_set = mappings[needed]
            new_set.discard(x)
            if len(new_set) > 0: # if true there exists another card to form the sum
                print("YES")
                return

        # same as the previous conditional, just with flipped value
        if flipped > 0:
            needed = s - flipped
            if needed in mappings:
                new_set = mappings[needed]
                new_set.discard(x)
                if len(new_set) > 0:
                    print("YES")
                    return

    print("NO")

'''
Returns the flipped value of a card if possible, else -1
'''
def flip(a):
    ret = 0
    while a > 0:
        d = a % 10
        if fl[d] == -1: # Digit unflippable
            return -1
        # if the digit is flippable
        ret = fl[d] + ret * 10
        a //= 10
    return ret

def main():
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))
    possible_sum(numbers, s, n)


if __name__ == '__main__':
    main()
