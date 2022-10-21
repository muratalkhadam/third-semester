from queue import PriorityQueue
from pyamaze import maze, agent


# manhattan distance
def h(point_a: tuple, point_b: tuple) -> int:
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] + point_b[1])


def AStar(m: maze) -> dict:
    start = (m.rows, m.cols)

    g_score = {
        cell: float('inf')
        for cell in m.grid
    }
    g_score[start] = 0

    f_score = {
        cell: float('inf')
        for cell in m.grid
    }
    f_score[start] = 0 + h(start, (1, 1))

    open = PriorityQueue()
    open.put((f_score[start], h(start, (1, 1)), start))

    a_path = {}

    while not open.empty():
        current = open.get()[2]

        if current == (1, 1):
            break

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
                    open.put((temp_f_score, h(neighbour, start), neighbour))
                    a_path[neighbour] = current

    forward_path = {}
    cell = (1, 1)
    while cell != start:
        forward_path[a_path[cell]] = cell
        cell = a_path[cell]
    return forward_path


def print_dict(dict):
    for key, val in dict.items():
        print(f"{key}: {val}")


if __name__ == '__main__':
    m = maze(4, 4)
    m.CreateMaze(loopPercent=0)

    path = AStar(m)

    print("Resulted path with the A* algo is:")
    print_dict(path)

    a = agent(m, shape='arrow', filled=True, footprints=True)
    m.tracePath({a: path}, delay=100)

    m.run()
