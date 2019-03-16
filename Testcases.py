import random
import time

import Main
from Astar import astar
from Grid import populate_grid

# Populate the grids
from JPS import jps

Room_grid = populate_grid("maps/16room_000.map")
Arena_grid = populate_grid("maps/arena2.map")

# Pick test cases
Room_cases = [[313, 424, 311, 427, 3.82842712],
              [216, 287, 235, 285, 19.82842712],
              [123, 295, 166, 303, 46.31370850],
              [403, 366, 382, 431, 77.21320343],
              [509, 36, 430, 67, 126.56854248],
              [471, 184, 503, 73, 155.26702728],
              [204, 409, 201, 230, 199.29646454],
              [86, 4, 15, 211, 291.16652222]]
Arena_cases = [[159, 99, 162, 101, 3.82842712],
               [136, 165, 166, 142, 39.52691193],
               [135, 139, 93, 143, 43.65685425],
               [103, 208, 140, 168, 60.01219330],
               [94, 209, 62, 266, 90.59797974],
               [66, 262, 186, 252, 129.11269836]]


# Get results
def run_cases(cases, grid):
    results = []
    for case in cases:
        start = int(case[0]), int(case[1])
        end = int(case[2]), int(case[3])
        optimal_distance = float(case[4])
        results.append(test_results(grid, start, end, optimal_distance))
    return results


def test_results(maze, start, end, opt_dist):
    start_astar = time.time()
    (path1, dist1, count1) = astar(maze, start, end)
    end_astar = time.time()

    for row in maze:
        for cell in row:
            cell.parent = None
            cell.g = cell.h = cell.f = 0

    start_jps = time.time()
    (path2, dist2, count2) = jps(maze, start, end)
    end_jps = time.time()

    return len(path1), dist1, count1, (end_astar - start_astar) * 1000, (opt_dist - dist1), len(
        path2), dist2, count2, (end_jps - start_jps) * 1000, (opt_dist - dist2)


def main():
    for a, b in zip([Room_cases, Arena_cases], [Room_grid, Arena_grid]):
        results = run_cases(a, b)
    for line in results:
        print(line)


if __name__ == '__main__':
    main()
