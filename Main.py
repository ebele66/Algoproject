import time

from Astar import astar
from Grid import populate_grid
from JPS import jps


def main():
    filename = input('Enter a filename: ')
    maze = populate_grid(filename)
    start = (1, 1)
    end = (8, 20)

    start_astar = time.time()
    (path, count) = astar(maze, start, end)
    end_astar = time.time()
    print("Astar")
    print("Path between start and destination ", path)
    print("length of path ", len(path))
    print("Time (ms) ", (end_astar - start_astar) * 1000)
    print("Numebr of nodes explored by the algorithm ", count)

    start_jps = time.time()
    (path, count) = jps(maze, start, end)
    end_jps = time.time()
    print("JPS")
    print("Path between start and destination ", path)
    print("length of path ", len(path))
    print("Time (ms) ", (end_jps - start_jps) * 1000)
    print("Numebr of nodes explored by the algorithm ", count)


if __name__ == '__main__':
    main()
