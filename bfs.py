from node import *


def bfs(start, end, grid):
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])

    queue = []
    queue.append(startNode)

    visitedNodes = set()
    visitedNodes.add((startNode.row, startNode.col))

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
