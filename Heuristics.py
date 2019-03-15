from math import sqrt


def diagonalDistance(position1, position2):
    dx = abs(position1[0] - position2[0])
    dy = abs(position1[1] - position2[1])
    return max(dx, dy) + (sqrt(2) - 1) * min(dx, dy)


def octile(position1, position2):
    dx = abs(position1[0] - position2[0])
    dy = abs(position1[1] - position2[1])
    f = sqrt(2) - 1
    if dx < dy:
        return f * dx + dy
    else:
        return f * dy + dx


def manhattan(position1, position2):
    dx = abs(position1[0] - position2[0])
    dy = abs(position1[1] - position2[1])
    return dx + dy


def euclidean(position1, position2):
    dx = abs(position1[0] - position2[0])
    dy = abs(position1[1] - position2[1])
    return sqrt(dx * dx + dy * dy)
