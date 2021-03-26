import minimax as mm
import terminal as state
import APIrequests as req

userId = "1039"
teamId1 = "1251"
teamId2 = "1263"
boardSize = 3
target = 3
whichGames = "myOpenGames"
count = "1"

gameId = str(req.createGame(userId, teamId1, teamId2, str(boardSize), str(target)))

board = [[""]*target for i in range(target)]

player = "O";
opponent = "X";

if not state.isTerminal(board, boardSize, target):
    bestMove, bestMove_str = mm.makeMove(board)
    code, moveId = req.makeMove(userId, gameId, teamId1, bestMove_str)
    if code == "OK":
        print(bestMove)
        board[bestMove[0]][bestMove[1]] = player

if not state.isTerminal(board, boardSize, target):
    symbol, lastMove_str = req.getMoves(gameId, count)
    if symbol == opponent:
        lastMove = [int(x) for x in lastMove_str.split(",")]
        board[lastMove[0]][lastMove[1]] = opponent