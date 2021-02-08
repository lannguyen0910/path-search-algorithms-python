from heapq import heappush, heappop
from node import *


def dijkstra(start, end, grid):
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])

    visitedNodes = set()
    unvisitedNodes = getAllAvailableNodes(grid)
    startNode.distance = 0

    heappush(unvisitedNodes, (startNode.distance, startNode))
    while len(unvisitedNodes) != 0:
        # closest prev node with min distance
        closestNode = heappop(unvisitedNodes)[1]
        visitedNodes.add((closestNode.row, closestNode.col))

        if closestNode == endNode:
            return getPath(startNode, closestNode, grid)

        neighbors = getNeighbors(closestNode, grid)
        for neighbor in neighbors:
            distance = closestNode.distance + 1

            if (neighbor.row, neighbor.col) not in visitedNodes and distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.prev = closestNode
                heappush(unvisitedNodes, (neighbor.distance, neighbor))


def getAllAvailableNodes(grid):
    nodes = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                node = Node(row, col)
                heappush(nodes, (node.distance, node))

    return nodes
