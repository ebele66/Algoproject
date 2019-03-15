class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, walkable=False):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.walkable = walkable

    def __eq__(self, other):
        return self.position == other.position
