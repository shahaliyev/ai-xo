import terminal as state
import heuristics as h


# Minimax algorithm which is mainly used in adversarial games
# Alpha-Beta Pruning is for reducing branching factor
# Evaluation fuction is also implemented as heuristic
def minimax(board, boardSize, target, depth, isMax, alpha, beta, emptyCells, player, opponent):
    
    maxDepth = getDepth(emptyCells - depth)
    
    if depth == maxDepth:
        return h.calculate_score(board, boardSize, target, player, opponent)
    
    if isMax:
        
        bestVal = -float('inf')
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = player
                    value = minimax(board, boardSize, target, depth + 1, False, alpha, beta, emptyCells, player, opponent)
                    board[i][j] = ""
                    
                    bestVal = max(bestVal, value)
                    
                    # alpha beta pruning
                    alpha = max(alpha, bestVal)
                    if beta <= alpha:
                        break

        return bestVal
    
    else:
        
        bestVal = float('inf')
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = opponent
                    value = minimax(board, boardSize, target, depth + 1, True, alpha, beta, emptyCells, player, opponent)
                    board[i][j] = ""
                    
                    bestVal = min(bestVal, value)
                    
                    # alpha beta pruning
                    beta = min(beta, bestVal)
                    if beta <= alpha:
                        break
            
        return bestVal


# Recursively calls minimax function and returns the optimal move
def makeMove(board, boardSize, target, player, opponent, turnDepth):
    
    bestMove = []
    bestVal = -float('inf')
    
    emptyCells = countEmptyCells(board)
    
    # iterating over board
    for i, row in enumerate(board):
        for j, cell in enumerate(row):   
            
            if cell == "":
                
                # marking board
                board[i][j] = player
                # getting minimax value
                if turnDepth == 0:
                    value = minimax(board, boardSize, target, 0, False, -float('inf'), float('inf'), emptyCells, player, opponent)
                if turnDepth == 1:
                    value = minimax(board, boardSize, target, 1, False, -float('inf'), float('inf'), emptyCells, player, opponent)
                # backtracking (erasing)
                board[i][j] = ""
                
                # getting best coordinates
                if value > bestVal:
                    bestVal = value
                    bestMove = [i, j]
    
    bestMove_str = str(bestMove[0]) + "," + str(bestMove[1])
    
    return bestMove, bestMove_str


# Counts the empty cells in graph
def countEmptyCells(board):
    
    cnt = 0
    
    for row in board:
        for cell in row:
            if cell == "":
                cnt += 1
                
    return cnt


# Finds the 'depth' to be used according to number of empty cells in graph
def getDepth(cnt):
    
    depth = 1
    
    if cnt > 100:
        depth = 1
    
    elif cnt > 64:
        depth = 2
    
    elif cnt > 36:
        depth = 3
    
    else:
        depth = 4
    
    return depth


# Test
# boardSize = 12
# target = 6

# player = "X"
# opponent = "O"


# 3x3
# board = [["",   "",   ""],
         
#          ["",   "",   ""],
         
#          ["",   "",   ""]]


# 4x4
# board = [["",   "",   "",   ""],
         
#          ["",   "",   "",   ""],
         
#          ["",   "",   "",   ""],
         
#          ["",   "",   "",   ""]]


# 6x6
# board = [["",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   ""]]


# 8x8
# board = [["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   ""]]


# 10x10
# board = [["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   ""]]


# 12x12
# board = [["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""],
         
#          ["",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",   ""]]


# print(makeMove(board, boardSize, target, player, opponent, turnDepth))
