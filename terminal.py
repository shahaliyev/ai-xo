import numpy as np;

# Checks if cells meet the target
def checkCells(row, target):
    
    # tracking the consecutive Xs and Os
    xCount = 0;
    oCount = 0;
        
    for cell in row:
                  
        if cell == "":
            oCount = 0;
            xCount = 0;
            
        elif cell == "X":
            oCount = 0;
            xCount += 1;
                
            if xCount == target:
                return True;
                        
        elif cell == "O":
            xCount = 0;
            oCount += 1;
                
            if oCount == target:
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
 
    
# Checks if diagonals meet the target    
def checkDiagonals(board, boardSize, target):
    
    # getting reversed board
    reverseBoard = np.flip(board, 1);
    
    for x in range(-boardSize + 1, boardSize):
        
        # getting the next diagonal in both directions
        diagonal = np.diag(board, x);
        reverseDiag = np.diag(reverseBoard, x);
        
        # skipping unnecessary diagonals
        if len(diagonal) < target:
            continue;
        
        # returning true if a diagonal meets target 
        if checkCells(diagonal, target) | checkCells(reverseDiag, target):
            return True;
            
    return False;
    

# Checks for terminal states    
def isTerminal(board, boardSize, target):
    return checkRows(board, target) | checkColumns(board, target) | checkDiagonals(board, boardSize, target);


# Test
boardSize = 3;
target = 3;

board = [["X", "", "O"],
         ["X", "O", ""],
         ["O", "X", "O"]];

print(isTerminal(board, boardSize, target));
