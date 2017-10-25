'''
Value holds the "type" of the Node: road, mountaing, wall etc.
parent: the parent of the node
neighbours: array with all neighbours
H: H score
G: G score
F: F score
x: x position
y: y position
wall: True or False depending on it the node is a wall
start: True if this is the start node
target: True if this is the target node

cost(): calculating the cost of the node
manhattan(): used for calculating the manhattan distance to
the other node.
'''

class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.parent = None
        self.neighbours = []
        self.H = 0
        self.G = 0
        self.F = 0
        self.x = x
        self.y = y
        self.wall = value == '#'
        self.start = value == 'A'
        self.target = value == 'B'

    def cost(self):
        if self.value == '.':
            return 0
        elif self.value == 'r':
            return 1
        elif self.value == 'g':
            return 5
        elif self.value == 'f':
            return 10
        elif self.value == 'm':
            return 50
        elif self.value == 'w':
            return 100
        else:
            return 1

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.F  < other.F
