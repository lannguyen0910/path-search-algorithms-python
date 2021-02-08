from node import *


def dfs(start, end, grid):
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])

    stack = []
    stack.append(startNode)

    visitedNodes = set()
    visitedNodes.add((startNode.row, startNode.col))
    startNode.is_visited = True

    while stack:
        curNode = stack.pop()
        if curNode == endNode:
            return getPath(startNode, curNode, grid)

        for neighbor in getNeighbors(curNode, grid):
            if (neighbor.row, neighbor.col) not in visitedNodes:
                neighbor.prev = curNode
                visitedNodes.add((neighbor.row, neighbor.col))
                stack.append(neighbor)

    print(visitedNodes)
