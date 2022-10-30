import psutil
import os
import func_timeout

from queue import PriorityQueue
from pyamaze import maze, agent
from time import time


# manhattan distance
def h(point_a: tuple, point_b: tuple) -> int:
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def search_astar(m: maze):
    return func_timeout.func_timeout(60*30, AStar, args=[m])


def AStar(m: maze):
    start_time = time()

    iterations = 0
    states = []

    start = (m.rows, m.cols)
    goal = (1, 1)

    g_score = {
        cell: float('inf')
        for cell in m.grid
    }
    g_score[start] = 0

    f_score = {
        cell: float('inf')
        for cell in m.grid
    }
    f_score[start] = 0 + h(start, goal)

    queue = PriorityQueue()
    queue.put((f_score[start], h(start, goal), start))

    a_path = {}

    while not queue.empty():
        if psutil.Process(os.getpid()).memory_info().rss > 1024**3:
            raise MemoryError("1 Gb memory exceeded")

        iterations += 1
        current = queue.get()[2]
        if current == goal:
            break

        if current not in states:
            states.append(current)

        for dir in 'ESNW':
            if m.maze_map[current][dir] == 1:
                if dir == 'E':
                    neighbour = (current[0], current[1] + 1)
                elif dir == 'W':
                    neighbour = (current[0], current[1] - 1)
                elif dir == 'N':
                    neighbour = (current[0] - 1, current[1])
                else:  # if dir == 'S':
                    neighbour = (current[0] + 1, current[1])

                temp_g_score = g_score[current] + 1
                temp_f_score = temp_g_score + h(neighbour, start)

                if temp_f_score < f_score[neighbour]:
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_f_score
                    queue.put((temp_f_score, h(neighbour, start), neighbour))
                    a_path[neighbour] = current

    forward_path = {}
    cell = goal
    while cell != start:
        forward_path[a_path[cell]] = cell
        cell = a_path[cell]

    print(f"A* algo finised in {time() - start_time} seconds...")
    print(f"{psutil.Process(os.getpid()).memory_info().rss / 1024**2} MB used...")
    # print(f"Iterations: {a_iter}, unique states: {a_states}")

    amount_states = len(states)
    return (forward_path, iterations, amount_states)


if __name__ == '__main__':
    size1 = int(input("Enter size of the maze: "))
    size2 = int(input("Enter size of the maze: "))

    m = maze(size1, size2)
    m.CreateMaze(loopPercent=15)

    a_path, a_iter, a_states = search_astar(m)
    print(f"Iterations: {a_iter}, unique states: {a_states}")

    a = agent(m, shape='arrow', filled=True, footprints=True)
    m.tracePath({a: a_path}, delay=100)

    m.run()


