from heapq import heappush, heappop
from node import *
from math import sqrt


def astar(start, end, grid):
    # gCost - distance from starting node
    # hCost - distance from target node
    #  fCost = gCost + hCost
    startNode = Node(start[0], start[1])
    endNode = Node(end[0], end[1])
    startNode.gCost, startNode.hCost = 0, 0
    endNode.gCost, endNode.hCost = 0, 0

    openSet = []
    closedSet = []

    heappush(openSet, (startNode.distance, startNode))
    while len(openSet) != 0:
        curNode = heappop(openSet)[1]
        closedSet.append(curNode)

        if curNode == endNode:
            return getPath(startNode, curNode, grid)

        neighbors = getNeighbors(curNode, grid)
        for neighbor in neighbors:
            gCost = curNode.gCost + 1

            if (neighbor.distance, neighbor) not in openSet or gCost < neighbor.gCost:
                neighbor.gCost = gCost
                neighbor.hCost = euclideanDistance(neighbor, endNode)
                neighbor.prev = curNode
                neighbor.distance = neighbor.gCost + neighbor.hCost
                heappush(openSet, (neighbor.distance, neighbor))


def euclideanDistance(startNode, endNode):
    """ Used when move in any direction """
    return sqrt((startNode.row - endNode.row) ** 2 + (startNode.col - endNode.col) ** 2)
