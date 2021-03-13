import numpy as np;

boardSize = 3;
target = 3;

board = [["X", "", "X"],
         ["X", "Y", ""],
         ["Y", "Y", "Y"]];


# Checks if cells meet the target
def checkCells(row, target):
    
    # tracking the consecutive Xs and Ys
    xCount = 0;
    yCount = 0;
        
    for cell in row:
                  
        if cell == "":
            yCount = 0;
            xCount = 0;
            
        elif cell == "X":
            yCount = 0;
            xCount += 1;
                
            if xCount == target:
                return True;
                        
        elif cell == "Y":
            xCount = 0;
            yCount += 1;
                
            if yCount == target:
                return True;
    
    return False;


# Checks if diagonals meet the target    
def checkDiagonals(board, boardSize, target):
    
    for x in range(-boardSize + 1, boardSize):
        
        # getting the next diagonal in both directions
        diagonal = np.diag(board, x);
        reverseBoard = np.flip(board, 1)
        reverseDiag = np.diag(reverseBoard, x);
        
        # skipping unnecessary diagonals
        if len(diagonal) < target:
            continue;
        
        # returning true if a diagonal meets target 
        if checkCells(diagonal, target) | checkCells(reverseDiag, target):
            return True;
            
    return False;
    
    
# Checks if rows meet the target
def checkRows(board, target):
    for row in board:
        if checkCells(row, target):
            return True;
            
    return False;


# Checks if columns meet the target
def checkColumns(board, target):
    transposed = np.transpose(board);
    return checkRows(transposed, target);
    

# Checks for terminal states    
def isTerminal(board, target):
    return checkRows(board, target) | checkColumns(board, target) | checkDiagonals(board, boardSize, target);


print(isTerminal(board, target));
