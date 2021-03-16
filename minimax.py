import terminal as state


INFINITY = float('inf');


def evaluate(board):

    if state.isTie(board):
        return 0;
    
    elif state.winner == player:
        return 1;
    
    elif state.winner == opponent:
        return -1;


def makeMove(board):
    
    bestMove = [];
    bestVal = -INFINITY;
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):   
            
            if cell == "":
          
                board[i][j] = player;
                value = minimax(board, 0, False, -INFINITY, INFINITY);
                board[i][j] = "";
                
                if value > bestVal:
                    bestVal = value;
                    bestMove = [i, j];
    
    return bestMove;


def minimax(board, depth, isMax, alpha, beta):
    
    if state.isTerminal(board, boardSize, target):
        return evaluate(board);
    
    if isMax:
        
        bestVal = -INFINITY;
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = player;
                    value = minimax(board, depth + 1, False, alpha, beta);
                    board[i][j] = "";
                    
                    bestVal = max(bestVal, value); 
                    
                    alpha = max(alpha, bestVal);
                    
                    if beta <= alpha:
                        break;

        return bestVal;

    else:
        
        bestVal = INFINITY;
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = opponent;
                    value = minimax(board, depth + 1, True, alpha, beta);
                    board[i][j] = "";
                    
                    bestVal = min(bestVal, value);
                    
                    beta = max(beta, bestVal);
                    
                    if beta <= alpha:
                        break;
            
        return bestVal;
