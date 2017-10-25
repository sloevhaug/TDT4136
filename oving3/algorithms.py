import bisect
from Node import Node

''' For all algorithms:
start: start node
target: target node
nodes: array of all nodes
openSet: the OPEN list
closedSet: the CLOSED list
'''

def astar(start, target, nodes, openSet, closedSet):
    '''Setting the H-value of the start node using manhattan distance.'''
    start.H = start.manhattan(target)
    openSet.append(start)

    while openSet:
        current = openSet.pop(0)
        closedSet.append(current)
        getNeighbours(current, nodes)

        if current.target:
            return True

        for neighbour in current.neighbours:
            estimate = neighbour.manhattan(target)
            
            temp_g = current.G + neighbour.cost()
            temp_f = temp_g + estimate

            if neighbour in closedSet and temp_f >= neighbour.F:
                continue

            if neighbour not in openSet or temp_f < neighbour.F:
                neighbour.parent = current
                neighbour.F = temp_f
                neighbour.G = temp_g
                if neighbour in openSet:
                    openSet.remove(neighbour)
                
                bisect.insort(openSet, neighbour) # insert last for first in first out

    return False

def djikstra(start, target, nodes, openSet, closedSet):
    
    start.H = start.manhattan(target)

    openSet.append(start)

    while openSet:
        current = openSet.pop(0)
        closedSet.append(current)
        getNeighbours(current, nodes)

        if current.target:
            return True

        for neighbour in current.neighbours:
            estimate = neighbour.manhattan(target)
            temp_g = current.G + neighbour.cost()
            temp_f = temp_g + estimate

            if neighbour in closedSet and temp_f >= neighbour.F:
                continue

            if neighbour not in openSet or temp_f < neighbour.F:
                neighbour.parent = current
                neighbour.F = temp_f
                neighbour.G = temp_g
                if neighbour in openSet:
                    openSet.remove(neighbour)
                
                openSet.append(neighbour)

                '''Djikstra sorts by G Score instead of estimating distance to target.'''
                openSet.sort(key = lambda x: x.G)
    
    return False

def bfs(start, target, nodes, openSet, closedSet):
    
    start.H = start.manhattan(target)

    openSet.append(start)

    while openSet:
        current = openSet.pop(0)
        closedSet.append(current)
        getNeighbours(current, nodes)

        if current.target:
            return True

        for neighbour in current.neighbours:
            estimate = neighbour.manhattan(target)
            temp_g = current.G + neighbour.cost()
            temp_f = temp_g + estimate

            if neighbour in closedSet and temp_f >= neighbour.F:
                continue

            if neighbour not in openSet or temp_f < neighbour.F:
                neighbour.parent = current
                neighbour.F = temp_f
                neighbour.G = temp_g
                if neighbour in openSet:
                    openSet.remove(neighbour)
                
                '''BFS does not sort the openSet - Nodes but instead insert for first in first out.'''
                openSet.append(neighbour)
                
    return False
    
def getNeighbours(current, nodes):
    '''Finding all the neighbours to the current node. Since
    we have individial nodes with x and y values we do
    not have to worry about choosing x or y values outside
    the board and getting "out of bound" errors. If the node
    is a wall; we ignore it as a neighbour.'''

    for node in nodes:
        if not node.wall:
            if (node.x == current.x + 1 and node.y == current.y) or \
            (node.x == current.x - 1 and node.y == current.y) or \
            (node.x == current.x and node.y == current.y + 1) or \
            (node.x == current.x and node.y == current.y - 1):
                current.neighbours.append(node)
