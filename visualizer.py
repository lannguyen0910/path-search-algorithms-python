from dijkstra import dijkstra
from astar import astar
from node import Node
from bfs import bfs
from dfs import dfs
from termcolor import colored


def choose_algo(start, end, grid, algorithm):
    if algorithm == 'bfs':
        return bfs(start, end, grid)
    elif algorithm == 'dfs':
        return dfs(start, end, grid)
    elif algorithm == 'dijkstra':
        return dijkstra(start, end, grid)
    elif algorithm == 'astar':
        return astar(start, end, grid)


if __name__ == "__main__":
    # 20 x 20 grid
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    print('!=============== PATHFINDER =================!')
    print('\n-----------------------------------------------\n                Custom Grid')
    for row in maze:
        print(''.join('{0} '.format(num) for num in row))

    startInp = input(colored(
        '\nPlease enter a starting coordinate (ex: 2,1): ', 'cyan'))
    start = tuple(map(int, startInp.split(',')))
    endInput = input(colored(
        'Please enter an ending coordinate (ex: 9,1): ', 'cyan'))
    end = tuple(map(int, endInput.split(',')))
    algorithm = input(colored(
        'Please enter an algorithm (dfs, bfs, astar, dijkstra): ', 'yellow'))

    if algorithm not in ['bfs', 'dfs', 'dijkstra', 'astar']:
        raise Exception('Invalid algorithm input. Please input again!')

    choose_algo(start, end, maze, algorithm)
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    print('\n-----------------------------------------------')
    print(colored(
        f'Start visualizing path from ({start[0]},{start[1]}) to ({end[0]},{end[1]}) using {algorithm} algorithm\n', 'blue'))
    for row in maze:
        print(''.join(colored('{0} '.format(num), 'red') if num == '*' or num == 'S' or num == 'E' else ''.join(
            colored('{0} '.format(num), 'green')) if num == 0 else ''.join(
            colored('{0} '.format(num), 'magenta')) for num in row))
