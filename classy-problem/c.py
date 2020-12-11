# Have upper, middle and lower class
# Three choices, want to create an interval depending on the longest class string
# if length of longest string is 5 => interval will be 3^5, since class can be decided
# in 5 steps (log3(3^5))
# Using ternary search?
from collections import defaultdict

class Person:

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.rank = []
        for i in range(len(title)):
            if title[-1-i] == "middle": self.rank.append(2)
            elif title[-1-i] == "lower": self.rank.append(1)
            else: self.rank.append(3)
        for i in range(10 - len(self.rank)):
            self.rank.append(2)
        self.rank = tuple(self.rank)


    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank >= other.rank
        return self.name <= other.name

    def __str__(self):
        return self.name

def ternary_search(lo, hi, l):
    i = 0
    while lo < hi and i < len(l):
        left_third = lo + (hi - lo)//3
        right_third = hi - (hi - lo)//3
        if l[i] == "middle":
            lo = left_third
            hi = right_third
        elif l[i] == "upper":
            lo = right_third
        else:
            hi = left_third

        i+=1

    return (lo + hi)//2


T = int(input())
END = '=============================='
for _ in range(T):
    n = int(input())

    persons = []
    for _ in range(n):
        p, cl = [i.strip() for i in input().split(':')]
        cl = cl.split()[:-1][0].split('-')
        persons.append(Person(p,cl))

    for i in sorted(persons):
        print(i, i.rank)
    print(END)
