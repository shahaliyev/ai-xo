#!/usr/bin/env python
# coding: utf-8

# In[132]:


import numpy as np


def getScore(lines, boardSize, target):

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
                score += 10 ** playerCount

            elif playerCount == 0:
                score += - (10**opponentCount)

    return score



def get_Scores_for_Row(board,boardSize,target):
    return  getScore(board, boardSize, target)

def get_Scores_for_Column(board,boardSize,target):
    transposed = np.transpose(board)
    return  getScore(transposed, boardSize, target)

def get_Scores_for_Diagonal(board,boardSize,target):
    diag_score = 0
    
    # getting reversed board
    reverseBoard = np.flip(board, 1)
    
    for x in range(-boardSize + 1, boardSize):
        
        # getting the next diagonal in both directions
        diagonal = np.diag(board, x)
        reverseDiag = np.diag(reverseBoard, x)
        
        # skipping unnecessary diagonals
        diag_length = len(diagonal)
        if diag_length < target:
            continue
            
        #score = score + ([diagonal,reverseDiag])
        
        diag_score += getScore([diagonal,reverseDiag],diag_length,target)
    return diag_score


def calculate_score(board,boardSize,target):
    total_score = 0
    
    score_rows = get_Scores_for_Row(board, boardSize, target)
    
    score_columns = get_Scores_for_Column(board, boardSize, target)
    
    score_diagonals = get_Scores_for_Diagonal(board,boardSize,target)
    
    total_score = score_columns + score_diagonals + score_rows
    return total_score


#test

boardSize = 4
target = 3



board = [["X", "", "X",''],
         ["X", "", "X",''],
         ["O", '', 'O',''],
         ["O", "", "O",'']]
    
    
    

player = "X"
opponent = "O"

calculate_score(board,boardSize,target)


# In[ ]:




