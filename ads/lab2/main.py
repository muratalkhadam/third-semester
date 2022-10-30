from AStar import search_astar
# from LDFS import search_ldfs

from pyamaze import maze, agent, COLOR


def main():
    size = int(input("Enter size of the maze: "))
    loop_percent = int(input("Enter percent of possible loops:"))

    m = maze(size, size)
    m.CreateMaze(loopPercent=loop_percent)

    option = int(input("For A* algo pick 1,\n"
                       "For LDFS - pick 2:\n"))

    iter = 0
    states = 0
    if option == 1:
        # path = search_astar(m)
        path, iter, states = search_astar(m)
        agent_color = COLOR.blue
    else:
        # path = search_ldfs(m)
        # path, iter, states = search_ldfs(m)
        # agent_color = COLOR.red

    print(f"Iterations: {iter}, unique states: {states}")

    a = agent(m, shape='arrow', filled=True, footprints=True, color=agent_color)
    m.tracePath({a: path}, delay=100)
    m.run()


if __name__ == '__main__':
    main()
