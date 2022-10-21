import random

from pyamaze import maze, agent, COLOR


def main():
    m = maze(2, 2)
    m.CreateMaze()
    # m.CreateMaze(
    #     x=random.randint(0, m.rows),
    #     y=random.randint(0, m.cols)
    # )

    a = agent(m, shape='arrow', filled=True, footprints=True)
    m.tracePath({a: m.path}, delay=1000)

    m.run()


if __name__ == '__main__':
    main()
