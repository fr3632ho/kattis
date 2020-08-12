import sys
from collections import deque

JOE = 'J'
FIRE = 'F'
WALL = '#'
SPACE = '.'

class Graph:

    def __init__(self, r, c, matrix):
        self.visited = [[False]*c for _ in range(r)]
        self.r, self.c = r, c
        self.mat = matrix
        self.joe, self.fires = self.find_initials()
        self.joe_start = (self.joe[0][0], self.joe[0][1])

    def is_exit(self, y, x):
        return x == 0 or x == self.c - 1 or y == 0 or y == self.r - 1

    def ok_move(self, y, x):
        return not self.visited[y][x] and self.mat[y][x] == SPACE

    def find_initials(self):
        '''
        Returns a fire & joe queue
        '''
        joe, fires = deque(), deque()
        for _r in range(self.r):
            for _c in range(self.c):
                curr = self.mat[_r][_c]
                if curr == JOE:
                    joe.append((_r, _c))
                    self.visited[_r][_c] = True
                if curr == FIRE:
                    fires.append((_r, _c))
                    self.visited[_r][_c] = True

        return joe, fires

    def joe_round(self):
        '''
        One round of joe moving in many directions
        '''
        tmp_queue = deque()

        while self.joe:
            y, x = self.joe.pop()
            if x > 0 and self.ok_move(y, x - 1): # left and check exit
                if x - 1 == 0:
                    return True
                self.visited[y][x - 1] = True
                tmp_queue.appendleft((y, x - 1))

            if x < self.c - 1 and self.ok_move(y, x + 1): # right and check exit
                if x + 1 == self.c - 1:
                    return True
                self.visited[y][x + 1] = True
                tmp_queue.appendleft((y, x + 1))

            if y > 0 and self.ok_move(y - 1, x): # up and check exit
                if y - 1 == 0:
                    return True
                self.visited[y - 1][x] = True
                tmp_queue.appendleft((y - 1, x))

            if y < self.r - 1 and self.ok_move(y + 1, x): # down and check exit
                if y + 1 == self.r - 1:
                    return True
                self.visited[y + 1][x] = True
                tmp_queue.appendleft((y + 1, x))

        self.joe = tmp_queue
        return False


    def fire_round(self):
        tmp_queue = deque()

        while self.fires:
            y, x = self.fires.pop()
            if x > 0 and self.ok_move(y, x - 1): # left
                self.visited[y][x - 1] = True
                tmp_queue.appendleft((y, x - 1))

            if x < self.c - 1 and self.ok_move(y, x + 1): # right
                self.visited[y][x + 1] = True
                tmp_queue.appendleft((y, x + 1))

            if y > 0 and self.ok_move(y - 1, x): # up
                self.visited[y - 1][x] = True
                tmp_queue.appendleft((y - 1, x))

            if y < self.r - 1 and self.ok_move(y + 1, x): # down
                self.visited[y + 1][x] = True
                tmp_queue.appendleft((y + 1, x))

        self.fires = tmp_queue


    def simulate(self):
        if self.is_exit(self.joe_start[0], self.joe_start[1]):
            return 1

        time = 1
        while self.joe:

            self.fire_round()
            curr = self.joe_round()
            time += 1
            if curr:
                return time # Reached an exit


        return "IMPOSSIBLE" # Impossible, didn't reach exit


def main():
    r, c = map(int, input().split())
    matrix = [input() for _ in range(r)]
    G = Graph(r, c, matrix)
    print(G.simulate())

if __name__ == "__main__":
    main()
