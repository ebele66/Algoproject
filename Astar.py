from math import sqrt
from Grid import walkableNode, neighbours
from Heuristics import diagonalDistance


def astar(grid, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given map"""
    count = 0
    # Check if walkable terrain
    if not walkableNode(start, grid) or not walkableNode(end, grid):
        return [], 0
    start_node = grid[start[0]][start[1]]
    end_node = grid[end[0]][end[1]]

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        # count the number of node considerations done
        count += 1

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], count  # Return reversed path

        # Generate children
        children = neighbours(current_node, "astar", grid)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            # calculate the distance between the current node and the child
            # calculate the child's g value
            if child.position[0] - current_node.position[0] == 0 or child.position[1] - current_node.position[1] == 0:
                cg = current_node.g + 1
            else:
                cg = current_node.g + sqrt(2)

            # if the a shorter distance through this current node to the child
            if (child in open_list and cg < child.g):
                open_list.remove(child)
                # Create the f, g, and h values
                child.g = cg
                child.h = diagonalDistance(child.position, end_node.position)
                child.f = child.g + child.h
                child.parent = current_node
                # update the open_list to reflect the change in the child
                open_list.append(child)

            # if the child has not been considered to be explored
            if child not in open_list:
                # Create the f, g, and h values
                child.g = cg
                child.h = diagonalDistance(child.position, end_node.position)
                child.f = child.g + child.h
                child.parent = current_node
                # Add the child to the open_list
                open_list.append(child)
