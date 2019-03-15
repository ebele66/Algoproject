import Heuristics
from Grid import *


def jump_card(cur, direction, end_pos, grid):
    cur_x, cur_y = cur.position
    dx, dy = direction

    # check if walkable terrain
    if not walkableNode(cur.position, grid):
        return None

    # check if at destination
    if cur.position == end_pos:
        return cur

    if dy == 0:  # vertical jump
        if not walkableNode((cur_x, cur_y + 1), grid) and walkableNode((cur_x + dx, cur_y + 1), grid) or (
                not walkableNode((cur_x, cur_y - 1), grid) and walkableNode((cur_x + dx, cur_y - 1), grid)):
            return cur
    else:  # horizontal jump
        if not walkableNode((cur_x + 1, cur_y), grid) and walkableNode((cur_x + 1, cur_y + dy), grid) or (
                not walkableNode((cur_x - 1, cur_y), grid) and walkableNode((cur_x - 1, cur_y + dy), grid)):
            return cur
    if walkableNode((cur_x+dx,cur_y + dy), grid):
        child = grid[cur_x + dx][cur_y + dy]
        child.parent = cur
        return jump_card(child, direction, end_pos, grid)


def jump_diag(cur, direction, end_pos, grid):
    cur_x, cur_y = cur.position
    dx, dy = direction
    jumps = []

    # check if walkable terrain
    if not walkableNode(cur.position, grid):
        return None

    # check if at destination
    if cur.position == end_pos:
        jumps.append(cur)

    if not walkableNode((cur_x - dx, cur_y), grid) and walkableNode((cur_x - dx, cur_y + dy), grid) or (
            not walkableNode((cur_x, cur_y - dy), grid) and walkableNode((cur_x + dx, cur_y - dy), grid)):
        jumps.append(cur)

    if walkableNode((cur_x + dx, cur_y + dy ), grid):
        child = grid[cur_x + dx][cur_y + dy]
        child.parent = cur
        result = jump_diag(child, direction, end_pos, grid)
        if result:
            for a in result:
                jumps.append(a)

    if walkableNode((cur_x + dx, cur_y), grid):
        child = grid[cur_x + dx][cur_y]
        child.parent = cur
        res = jump_card(child, (dx, 0), end_pos, grid)
        if res: jumps.append(res)

    if walkableNode((cur_x, cur_y + dy), grid):
        child = grid[cur_x][cur_y + dy]
        child.parent = cur
        res = jump_card(child, (0, dy), end_pos, grid)
        if res: jumps.append(res)
    return jumps


def jump(cur, direction, end_position, grid):
    dx = direction[0]
    dy = direction[1]

    # Diagonal jump
    if dx != 0 and dy != 0:
        points=[]
        result = jump_diag(cur, (dx, dy), end_position, grid)
        if result:
            for a in result:
                points.append(a)
        return points

    # Cardinal jump - horizontal or vertical
    else:
        point = jump_card(cur, (dx, dy), end_position, grid)
        if point:
            return [point]


# Find the neighbors for the given node. If the node has a parent, prune the neighbors based on the jump point search
# algorithm, otherwise return all available neighbors.
def jps_neighbors(current, direction, grid):
    # directed pruning
    children = []
    cur_x = current.position[0]
    cur_y = current.position[1]
    dx = direction[0]
    dy = direction[1]

    if dx != 0 and dy != 0:  # Diagonal movement
        if not walkableNode((cur_x - dx, cur_y), grid) and walkableNode((cur_x - dx, cur_y + dy), grid):
            child = grid[cur_x - dx][cur_y + dy]
            child.parent = current
            children.append(child)
        if not walkableNode((cur_x, cur_y - dy), grid) and walkableNode((cur_x + dx, cur_y - dy), grid):
            child = grid[cur_x + dx][cur_y - dy]
            child.parent = current
            children.append(child)
        if walkableNode((cur_x, cur_y + dy), grid):
            child = grid[cur_x][cur_y + dy]
            child.parent = current
            children.append(child)
        if walkableNode((cur_x + dx, cur_y), grid):
            child = grid[cur_x + dx][cur_y]
            child.parent = current
            children.append(child)
        if walkableNode((cur_x + dx, cur_y + dy), grid):
            child = grid[cur_x + dx][cur_y + dy]
            child.parent = current
            children.append(child)
    else:
        if dx == 0:  # Horizontal movement
            if not walkableNode((cur_x + 1, cur_y), grid) and walkableNode((cur_x + 1, cur_y + dy), grid):
                child = grid[cur_x + 1][cur_y + dy]
                child.parent = current
                children.append(child)
            if not walkableNode((cur_x - 1, cur_y), grid) and walkableNode((cur_x - 1, cur_y + dy), grid):
                child = grid[cur_x - 1][cur_y + dy]
                child.parent = current
                children.append(child)
            if walkableNode((cur_x, cur_y + dy), grid):
                child = grid[cur_x][cur_y + dy]
                child.parent = current
                children.append(child)
        else:  # Vertical movement
            if not walkableNode((cur_x, cur_y + 1), grid) and walkableNode((cur_x + dx, cur_y + 1), grid):
                child = grid[cur_x + dx][cur_y + 1]
                child.parent = current
                children.append(child)
            if not walkableNode((cur_x, cur_y - 1), grid) and walkableNode((cur_x + dx, cur_y - 1), grid):
                child = grid[cur_x + dx][cur_y - 1]
                child.parent = current
                children.append(child)
            if walkableNode((cur_x + dx, cur_y), grid):
                child = grid[cur_x + dx][cur_y]
                child.parent = current
                children.append(child)
    return children


def jps(grid, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given map"""
    count = 0
    # Create start and end node
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

        # Generate successors
        if current_node.parent:
            dx = int((current_node.position[0] - current_node.parent.position[0]) / max(
                abs(current_node.position[0] - current_node.parent.position[0]), 1))
            dy = int((current_node.position[1] - current_node.parent.position[1]) / max(
                abs(current_node.position[1] - current_node.parent.position[1]), 1))
            children = jps_neighbors(current_node, (dx, dy), grid)
        else:
            children = neighbours(current_node, "jps", grid)

        for child in children:
            dx = int(
                (child.position[0] - current_node.position[0]) / max(abs(child.position[0] - current_node.position[0]),
                                                                     1))
            dy = int(
                (child.position[1] - current_node.position[1]) / max(abs(child.position[1] - current_node.position[1]),
                                                                     1))
            jumpPoints = jump(child, (dx, dy), end_node.position, grid)
            if not jumpPoints:
                continue
            for jptnode in jumpPoints:
                if not jptnode or jptnode in closed_list:
                    continue

                d = Heuristics.diagonalDistance(jptnode.position, current_node.position)
                ng = current_node.g + d

                # if there is a shorter distance through this current node to the jump node
                if jptnode in open_list and ng < jptnode.g:
                    open_list.remove(jptnode)
                    # Create the f, g, and h values
                    jptnode.g = ng
                    jptnode.h = Heuristics.diagonalDistance(jptnode.position, end_node.position)
                    jptnode.f = jptnode.g + jptnode.h
                    # update the open_list to reflect the change in the child
                    open_list.append(jptnode)

                # if the child has not been considered to be explored
                if jptnode not in open_list:
                    # Create the f, g, and h values
                    jptnode.g = ng
                    jptnode.h = Heuristics.diagonalDistance(jptnode.position, end_node.position)
                    jptnode.f = jptnode.g + jptnode.h
                    # add the jump point to the open_list
                    open_list.append(jptnode)


