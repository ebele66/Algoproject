from Node import Node


# Get data
def populate_grid(file):
    grid = []
    with open(file) as f:
        f.readline()
        height = int(f.readline().split()[1])
        width = int(f.readline().split()[1])
        f.readline()
        for i in range(0, height):
            row = []
            str = f.readline()
            for j in range(0, width):
                if str[j] in ('.', 'G'):
                    row.append(Node(None, (i, j), True))
                else:
                    row.append(Node(None, (i, j), False))
            grid.append(row)
    return grid


# Make sure within range
def insideGrid(node_position, grid):
    return 0 <= node_position[0] < len(grid) and 0 <= node_position[1] < len(grid[len(grid) - 1])


# Make sure walkable terrain
def walkableNode(node_position, grid):
    return insideGrid(node_position, grid) and grid[node_position[0]][node_position[1]].walkable


def neighbours(current_node, algo, grid):
    # Generate children
    children = []  # left    right    up     down    up left  up right  down left down right
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure within range
        if not walkableNode(node_position, grid):
            continue

        # Assign parent Only used for jps
        if algo == "jps":
            grid[node_position[0]][node_position[1]].parent = current_node

        # Append
        children.append(grid[node_position[0]][node_position[1]])
    return children
