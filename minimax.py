import terminal as state


def evaluate(board):

    if state.isTie(board):
        return 0;
    
    elif state.winner == player:
        return 1;
    
    elif state.winner == opponent:
        return -1;


def makeMove(board):
    
    bestMove = [];
    bestVal = float('-inf');
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):   
            
            if cell == "":
          
                board[i][j] = player;
                value = minimax(board, 0, False);
                board[i][j] = "";
                
                if value > bestVal:
                    bestVal = value;
                    bestMove = [i, j];
    
    return bestMove;


def minimax(board, depth, isMax):
    
    if state.isTerminal(board, boardSize, target) == True:
        return evaluate(board);
    
    if isMax:
        
        bestVal = float('-inf');
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = player;
                    value = minimax(board, depth + 1, False);
                    board[i][j] = "";
                    
                    bestVal = max(bestVal, value);           

        return bestVal;

    else:
        
        bestVal = float('inf');
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                
                if cell == "":
                    
                    board[i][j] = opponent;
                    value = minimax(board, depth + 1, True);
                    board[i][j] = "";
                    
                    bestVal = min(bestVal, value);
            
        return bestVal;


# Test
boardSize = 3;
target = 3;

board = [["X", "", "O"],
         ["X", "X", ""],
         ["O", "", "O"]];

player = "X";
opponent = "O";

if state.isTerminal(board, boardSize, target) == False:
    print(makeMove(board));
