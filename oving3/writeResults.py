import sys

def writeResults(target, start, path, board, out, openSet, closedSet):
    node = target
    
    '''Iterating through all the parent nodes and appending them to the path...'''
    while node != start:
        path.append(node)
        node = node.parent
    path.append(start)
    
    '''Drawing the path the algorithm took by changing the value on the board to X'''
    for node in path:
        if not node.target and not node.start:
            board[node.y][node.x] = "X";

    '''Visualizing open nodes'''
    if(openSet != None):
        for node in openSet:
            if not node.target and not node.start:
                if len(board[node.y][node.x]) == 1:
                    board[node.y][node.x] = "(" + board[node.y][node.x] + ")"

    '''Visualizing closed nodes'''
    if(closedSet != None):
        for node in closedSet:
            if not node.target and not node.start:
                if len(board[node.y][node.x]) == 1:
                    board[node.y][node.x] = "[" + board[node.y][node.x] + "]"

    '''Printing the results to the terminal and writing them to the output-file'''
    for i in range(len(board)):         # Y Coordinates
        for j in range(len(board[0])):  # X Coordinates
            if len(board[i][j]) > 1:
                sys.stdout.write(board[i][j])
                out.write(board[i][j])
            else:
                sys.stdout.write(" " + board[i][j] + " ")
                out.write(" " + board[i][j] + " ")
        sys.stdout.write("\n")
        out.write("\n")
    sys.stdout.flush()
    out.write("\n")