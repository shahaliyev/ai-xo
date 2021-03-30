import time
import minimax as mm
import terminal as state
import requestsAPI as req


def WeStartGame(userId, teamId1, teamId2, boardSize, target):
    
    player = "O"
    opponent = "X"
    
    gameId = str(req.createGame(userId, teamId1, teamId2, str(boardSize), str(target)))
    board = [[""]*boardSize for i in range(boardSize)]
    
    while not state.isTerminal(board, boardSize, target):
        
        bestMove, bestMove_str = mm.makeMove(board, boardSize, target, player, opponent)
        code, moveId = req.makeMove(userId, gameId, teamId1, bestMove_str)
        
        if code == "OK":
            board[bestMove[0]][bestMove[1]] = player
        
        if state.isTerminal(board, boardSize, target):
            break
        
        symbol, lastMove_str = req.getMoves(userId, gameId, "1")
        
        while symbol == player:
            time.sleep(5)
            symbol, lastMove_str = req.getMoves(userId, gameId, "1")
        
        if symbol == opponent:
            lastMove = [int(x) for x in lastMove_str.split(",")]
            board[lastMove[0]][lastMove[1]] = opponent


def OpStartGame(userId, teamId1, teamId2):
    
    player = "X"
    opponent = "O"
    
    gameId = req.getMyGames(userId, "myOpenGames")
    boardSize, target = req.getBoard(userId, 0, gameId)
    board = [[""]*boardSize for i in range(boardSize)]
    
    while not state.isTerminal(board, boardSize, target):
        
        symbol, lastMove_str = req.getMoves(userId, gameId, "1")
        
        while symbol == player or symbol == False:
            time.sleep(5)
            symbol, lastMove_str = req.getMoves(userId, gameId, "1")
        
        if symbol == opponent:
            lastMove = [int(x) for x in lastMove_str.split(",")]
            board[lastMove[0]][lastMove[1]] = opponent
        
        if state.isTerminal(board, boardSize, target):
            break
        
        bestMove, bestMove_str = mm.makeMove(board, boardSize, target, player, opponent)
        code, moveId = req.makeMove(userId, gameId, teamId2, bestMove_str)
        
        if code == "OK":
            board[bestMove[0]][bestMove[1]] = player


WeStartGame("1039", "1263", "1288", 3, 3)

OpStartGame("1039", "1288", "1263")
