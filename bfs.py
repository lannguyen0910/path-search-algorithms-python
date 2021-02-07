from node import Node


def bfs(start, end, grid):
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])
    queue = []
    queue.append(startNode)
    visitedNodes = set([start])
    while len(queue) != 0:
        curNode = queue.pop(0)
        if curNode == endNode:
            return getPath(startNode, curNode, grid)

        for neighbor in getNeighbors(curNode, grid):
            if (neighbor.row, neighbor.col) not in visitedNodes:
                neighbor.prev = curNode
                visitedNodes.add((neighbor.row, neighbor.col))
                queue.append(neighbor)

    print(visitedNodes)


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
