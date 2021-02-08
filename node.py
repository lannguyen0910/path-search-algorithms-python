class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = None
        self.isVisited = False
        self.isWall = False
        self.prev = None
        self.distance = float('inf')

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance


def getNeighbors(curNode, grid):
    neighbors = []
    new_positions = [(0, -1), (0, 1), (-1, 0), (1, 0),
                     (-1, -1), (1, 1), (-1, 1), (1, -1)]

    for new_position in new_positions:
        node_position = (
            curNode.row + new_position[0], curNode.col + new_position[1])

        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] < len(grid) and node_position[1] >= 0 and grid[node_position[0]][node_position[1]] == 0:
            neighbors.append(Node(node_position[0], node_position[1]))

    return neighbors


def getPath(startNode, endNode, grid):
    path = []
    curNode = endNode
    while curNode != startNode:
        path.append((curNode.row, curNode.col))
        grid[curNode.row][curNode.col] = '*'
        curNode = curNode.prev

    return path[::-1]
