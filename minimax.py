import terminal as state


INFINITY = float('inf')


def evaluate(board):

    if state.isTie(board):
        return 0
    
    elif state.winner == player:
        return 1
    
    elif state.winner == opponent:
        return -1


# Recursively calls minimax function and returns the optimal move
def makeMove(board):
    
    bestMove = []
    bestVal = -INFINITY
    
    # iterating over board
    for i, row in enumerate(board):
        for j, cell in enumerate(row):   
            
            if cell == "":
                
                # marking board
                board[i][j] = player
                # getting minimax value
                value = minimax(board, 0, False, -INFINITY, INFINITY)
                # backtracking (erasing)
                board[i][j] = ""
                
                # getting best coordinates
                if value > bestVal:
                    bestVal = value
                    bestMove = [i, j]
    
    bestMove_str = str(bestMove[0]) + "," + str(bestMove[1])
    
    return bestMove, bestMove_str


def minimax(board, depth, isMax, alpha, beta):
    
    if state.isTerminal(board, boardSize, target):
        return evaluate(board)
    
    if isMax:
        
        bestVal = -INFINITY
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = player
                    value = minimax(board, depth + 1, False, alpha, beta)
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
                    value = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ""
                    
                    bestVal = min(bestVal, value)
                    
                    # alpha beta pruning
                    beta = min(beta, bestVal)
                    if beta <= alpha:
                        break
            
        return bestVal

    
 # Test
boardSize = 3
target = 3

board = [["X", "", ""],
         ["", "", ""],
         ["O", "", ""]]

player = "X"
opponent = "O"


if not state.isTerminal(board, boardSize, target):
    print(makeMove(board))
