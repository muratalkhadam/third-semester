import psutil
import os
import func_timeout

from queue import PriorityQueue
from pyamaze import COLOR
from time import time


class ALgoSolver:
    def __init__(self, m):
        self.m = m

        self.stops = 0
        self.states = []
        self.amount_of_states = 0

        self.iterations = 0
        self.start_time = time()

        self.start = (self.m.rows, self.m.cols)
        self.goal = (1, 1)

        self.is_solvable = False
        self.path = {}

        self.color = COLOR.blue
        self.name = ""

    def __del__(self):
        print(f"{self.name} algo finised in {time() - self.start_time} seconds...")
        print(f"{psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} MB used...")

    def search_AStar(self):
        return func_timeout.func_timeout(60 * 30, self.__AStar)

    def __AStar(self):
        self.name = "A*"

        g_score = {
            cell: float('inf')
            for cell in self.m.grid
        }
        g_score[self.start] = 0

        f_score = {
            cell: float('inf')
            for cell in self.m.grid
        }
        f_score[self.start] = 0 + self.h(self.start, self.goal)

        queue = PriorityQueue()
        queue.put((f_score[self.start], self.h(self.start, self.goal), self.start))

        a_path = {}
        while not queue.empty():
            if psutil.Process(os.getpid()).memory_info().rss > 1024 ** 3:
                raise MemoryError("1 Gb memory exceeded")

            self.iterations += 1
            current = queue.get()[2]
            if current == self.goal:
                self.amount_of_states = len(self.states)
                break

            if current not in self.states:
                self.states.append(current)

            for dir in 'ESNW':
                if self.m.maze_map[current][dir] == 1:
                    if dir == 'E':
                        neighbour = (current[0], current[1] + 1)
                    elif dir == 'W':
                        neighbour = (current[0], current[1] - 1)
                    elif dir == 'N':
                        neighbour = (current[0] - 1, current[1])
                    else:  # if dir == 'S':
                        neighbour = (current[0] + 1, current[1])

                    temp_g_score = g_score[current] + 1
                    temp_f_score = temp_g_score + self.h(neighbour, self.start)

                    if temp_f_score < f_score[neighbour]:
                        g_score[neighbour] = temp_g_score
                        f_score[neighbour] = temp_f_score
                        queue.put((temp_f_score, self.h(neighbour, self.start), neighbour))
                        a_path[neighbour] = current

        cell = self.goal
        while cell != self.start:
            self.path[a_path[cell]] = cell
            cell = a_path[cell]

    # manhattan distance
    @staticmethod
    def h(point_a: tuple, point_b: tuple) -> int:
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

    def search_LDFS(self, limit):
        return func_timeout.func_timeout(60 * 30, self.__LDFS, args=[limit])

    def __LDFS(self, limit):
        self.color = COLOR.red
        self.name = "LDFS"

        stack = [(self.start, [self.start])]
        while stack:
            if psutil.Process(os.getpid()).memory_info().rss > 1024 ** 3:
                raise MemoryError("1 Gb memory exceeded")

            self.iterations += 1
            curr, self.path = stack.pop()
            if curr not in self.states:
                self.states.append(curr)

            if len(self.path) - 1 == limit:
                self.stops += 1
                continue

            if curr == self.goal:
                self.amount_of_states = len(self.states)
                self.is_solvable = True
                break

            neighbours = []
            for dir in 'ESNW':
                if self.m.maze_map[curr][dir] == 1:
                    if dir == 'E':
                        neighbour = (curr[0], curr[1] + 1)
                    elif dir == 'W':
                        neighbour = (curr[0], curr[1] - 1)
                    elif dir == 'N':
                        neighbour = (curr[0] - 1, curr[1])
                    else:  # if dir == 'S':
                        neighbour = (curr[0] + 1, curr[1])

                    if neighbour not in self.path:
                        neighbours.append((neighbour, self.path + [neighbour]))

            stack += neighbours
