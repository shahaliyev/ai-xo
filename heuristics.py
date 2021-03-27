import numpy as np

def getScore(lines, boardSize, target, player, opponent):

    score = 0
    
    for line in lines:    
        for i in range(boardSize - target + 1):

            playerCount = 0
            opponentCount = 0

            for j in range(target):  
                cell = line[i + j]

                if cell == player:
                    playerCount += 1

                elif cell == opponent:
                    opponentCount += 1

            if opponentCount == 0:
                score += 8 ** playerCount

            elif playerCount == 0:
                score += - (10 ** opponentCount)

    return score


def get_Scores_for_Row(board, boardSize, target, player, opponent):
    return  getScore(board, boardSize, target, player, opponent)


def get_Scores_for_Column(board, boardSize, target, player, opponent):
    transposed = np.transpose(board)
    return  getScore(transposed, boardSize, target, player, opponent)


def get_Scores_for_Diagonal(board, boardSize, target, player, opponent):
    
    diag_score = 0
    a = np.array(board)
    all_diagonals = [a[::-1,:].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
    all_diagonals.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))

    for my_length in range(target, boardSize + 1):
        my_diagonals = list(filter(lambda x: len(x) == my_length, all_diagonals))
        diag_score += getScore(my_diagonals, my_length, target, player, opponent)
        
    return diag_score


def calculate_score(board, boardSize, target, player, opponent):
    total_score = 0
    score_diagonals = 0
    
    score_rows = get_Scores_for_Row(board, boardSize, target, player, opponent)
    score_columns = get_Scores_for_Column(board, boardSize, target, player, opponent)
    score_diagonals = get_Scores_for_Diagonal(board, boardSize, target, player, opponent)
    
    total_score = score_columns + score_diagonals + score_rows
    return total_score
