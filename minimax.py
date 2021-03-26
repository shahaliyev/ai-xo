import terminal as state
import heuristics as h


INFINITY = float('inf')


def evaluate(board):

    if state.isTie(board):
        return 0
    
    elif state.winner == player:
        return 1000000
    
    elif state.winner == opponent:
        return -1000000


# Recursively calls minimax function and returns the optimal move
def makeMove(board):
    
    bestMove = []
    bestVal = -INFINITY
    
    emptyCells = countEmptyCells(board)
    
    # iterating over board
    for i, row in enumerate(board):
        for j, cell in enumerate(row):   
            
            if cell == "":
                
                # marking board
                board[i][j] = player
                # getting minimax value
                value = minimax(board, 0, False, -INFINITY, INFINITY, emptyCells)
                # backtracking (erasing)
                board[i][j] = ""
                
                # getting best coordinates
                if value > bestVal:
                    bestVal = value
                    bestMove = [i, j]
    
    bestMove_str = str(bestMove[0]) + "," + str(bestMove[1])
    
    return bestMove, bestMove_str


def minimax(board, depth, isMax, alpha, beta, emptyCells):
    
    maxDepth = getDepth(emptyCells - depth)
    
    if depth == maxDepth:
        return h.calculate_score(board, boardSize, target)
    
    if isMax:
        
        bestVal = -INFINITY
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = player
                    value = minimax(board, depth + 1, False, alpha, beta, emptyCells)
                    board[i][j] = ""
                    
                    bestVal = max(bestVal, value)
                    
                    # alpha beta pruning
                    alpha = max(alpha, bestVal)
                    if beta <= alpha:
                        break

        return bestVal
    
    else:
        
        bestVal = INFINITY
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = opponent
                    value = minimax(board, depth + 1, True, alpha, beta, emptyCells)
                    board[i][j] = ""
                    
                    bestVal = min(bestVal, value)
                    
                    # alpha beta pruning
                    beta = min(beta, bestVal)
                    if beta <= alpha:
                        break
            
        return bestVal

    
def countEmptyCells(board):
    
    cnt = 0
    
    for row in board:
        for cell in row:
            if cell == "":
                cnt += 1
                
    return cnt


def getDepth(cnt):
    
    depth = 1
    
    if cnt > 64:
        depth = 1
    
    elif cnt > 36:
        depth = 2
    
    elif cnt > 16:
        depth = 3
    
    else:
        depth = 4

    
    return depth


# Test
boardSize = 12;
target = 6;

player = "X"
opponent = "O"

board = [ ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""],
          ["", "", "",'', "", "", "", "", "", "", "", ""]]


# board = [ ["",   "",    "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     ""]]


# board = [ ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""], 
#           ["",   "",    "",     "",     "",     "",     "",     ""]]

# board = [ ["",      "",     "",  ""], 
         
#           ["",      "",     "",  ""],  
          
#           ["",      "",     "",  ""],  
           
#           ["",      "",     "",  ""],  ]

print(makeMove(board))
