from AlgoSolver import ALgoSolver
from pyamaze import maze, agent


def main():
    size = int(input("Enter size of the maze: "))
    loop_percent = int(input("Enter percent of possible loops:"))

    m = maze(size, size)
    m.CreateMaze(loopPercent=loop_percent)

    option = -1
    while option != 1 and option != 2:
        option = int(input("For A* algo pick 1,\n"
                           "For LDFS - pick 2:\n"))

    algo = ALgoSolver(m)
    if option == 1:
        algo.search_AStar()
    else:
        limit = int(input("Enter limit of depth or -1 for auto-limit: "))
        limit = limit if limit else size**2//2
        algo.search_LDFS(limit)
        print(f"Number of stops is {algo.stops}")
        if not algo.is_solvable:
            print(f"There is no solution with the {limit} depth.")

    print(f"Iterations: {algo.iterations}, unique states: {algo.amount_of_states}")

    a = agent(m, shape='arrow', filled=True, footprints=True, color=algo.color)
    m.tracePath({a: algo.path}, delay=100)

    print("Length of resulted path is", len(algo.path))

    m.run()


if __name__ == '__main__':
    main()
