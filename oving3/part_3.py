import collections
import bisect
import sys
from Node import Node
from algorithms import astar, djikstra, bfs
from writeResults import writeResults

'''PART 3 IS IDENTICAL TO PART 1 AND 2 ONLY THAT IT RUNS 3 TIMES WITH
ALL THE ALGORITMS.'''


files = [
    './boards/board-1-1.txt',
    './boards/board-1-2.txt',
    './boards/board-1-3.txt',
    './boards/board-1-4.txt',
    './boards/board-2-1.txt',
    './boards/board-2-2.txt',
    './boards/board-2-3.txt',
    './boards/board-2-4.txt',
]

'''Creating the file where we will write the visualized path'''
outFile = './output_part_3.txt'
out = open(outFile, "w");

out.write("\n----- PART 3 -----\n\n")
out.write("(x) - Open Nodes\n[x] - Closed Nodes\nX - Chosen path");


### A STAR ###
out.write("\n----- A* ALGORITHM -----\n\n")

for file in files:
    print("File: " + file)
    out.write("File: " + file + "\n")
    
    board = []          # A 2D array that holds all the characters from the text file
    nodes = []          # Empty array for holding all individual nodes
    openSet = []        # The OPEN list
    closedSet = []      # The CLOSED list
    path = []           # The final path the algorithm will choose
    start = None        # Start Node
    target = None       # Target Node

    '''Converting the text file to individual nodes:'''
    for line in open(file):
        board.append(list(filter(lambda x: x != "\n", line)))

    for i in range(len(board)):
        for j in range(len(board[0])):
            #print("x: " + str(j) + "\ty: " + str(i) + "\t" + board[i][j])
            nodes.append(Node(j, i, board[i][j])) 

    '''Finding the Start and Target Node by iterating through the node array.'''
    for node in nodes:
        if node.start: 
            start = node;
        if node.target: 
            target = node;

    '''Using the astar algorithm for searching for the shortest path.
    The if statement is for catching errors should there be no
    path available. The algorithm will return True or False.'''
    if astar(start, target, nodes, openSet, closedSet):
        writeResults(target, start, path, board, out, openSet, closedSet)
    else:
        print("No path from start to target found.")


### DJIKSTRA ####

out.write("\n----- DJIKSTRA -----\n\n")
for file in files:
    print("File: " + file)
    out.write("File: " + file + "\n")
    
    board = []          # A 2D array that holds all the characters from the text file
    nodes = []          # Empty array for holding all individual nodes
    openSet = []        # The OPEN list
    closedSet = []      # The CLOSED list
    path = []           # The final path the algorithm will choose
    start = None        # Start Node
    target = None       # Target Node

    '''Converting the text file to individual nodes:'''
    for line in open(file):
        board.append(list(filter(lambda x: x != "\n", line)))

    for i in range(len(board)):
        for j in range(len(board[0])):
            #print("x: " + str(j) + "\ty: " + str(i) + "\t" + board[i][j])
            nodes.append(Node(j, i, board[i][j])) 

    '''Finding the Start and Target Node by iterating through the node array.'''
    for node in nodes:
        if node.start: 
            start = node;
        if node.target: 
            target = node;

    '''Using the astar algorithm for searching for the shortest path.
    The if statement is for catching errors should there be no
    path available. The algorithm will return True or False.'''
    if djikstra(start, target, nodes, openSet, closedSet):
        writeResults(target, start, path, board, out, openSet, closedSet)
    else:
        print("No path from start to target found.")

#### BFS ####
out.write("\n----- BFS -----\n\n")
for file in files:
    print("File: " + file)
    out.write("File: " + file + "\n")
    
    board = []          # A 2D array that holds all the characters from the text file
    nodes = []          # Empty array for holding all individual nodes
    openSet = []        # The OPEN list
    closedSet = []      # The CLOSED list
    path = []           # The final path the algorithm will choose
    start = None        # Start Node
    target = None       # Target Node

    '''Converting the text file to individual nodes:'''
    for line in open(file):
        board.append(list(filter(lambda x: x != "\n", line)))

    for i in range(len(board)):
        for j in range(len(board[0])):
            #print("x: " + str(j) + "\ty: " + str(i) + "\t" + board[i][j])
            nodes.append(Node(j, i, board[i][j])) 

    '''Finding the Start and Target Node by iterating through the node array.'''
    for node in nodes:
        if node.start: 
            start = node;
        if node.target: 
            target = node;

    '''Using the astar algorithm for searching for the shortest path.
    The if statement is for catching errors should there be no
    path available. The algorithm will return True or False.'''
    if bfs(start, target, nodes, openSet, closedSet):
        writeResults(target, start, path, board, out, openSet, closedSet)
    else:
        print("No path from start to target found.")

out.close() # Closing the write to the out file
