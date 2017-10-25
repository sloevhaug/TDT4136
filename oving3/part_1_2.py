import collections
import bisect
import sys
from Node import Node
from algorithms import astar, djikstra, bfs
from writeResults import writeResults

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
outFile = './output_part_1_2.txt'
out = open(outFile, "w");

out.write("\n----- PART 1 AND 2 -----\n\n")

'''We create a loop that iterates through all files and writes the result to the file above'''

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
        writeResults(target, start, path, board, out, None, None)
    else:
        print("No path from start to target found.")

'''Closing the open file for writing'''
out.close() # Closing the write to the out file
