For this project, we were required to implement a program that can play generalized Tic Tac Toe. It plays games with opponents via API with requests.
Our program consists of 5 files:
1) terminal.py

In this file, we check whether game is in terminal state or not. Functions ‘checkRows’, ‘checkColumns’, and ‘checkDiagonals’ look for terminal state where 1 player won the game with consecutive signs. ‘noMovesLeft’ and ‘isTie’ find if game is ended as tie.
2) minimax.py

A minimax algorithm is a recursive algorithm for choosing the next move in an adversarial games. We also implemented Tic Tac Toe agent in minimax algorithm. In order to increase performance, alpha-beta pruning and iterative deepening is also implemented. In this file, most important function is ‘makeMove’. Function returns best move in given graph via calling ‘minimax’ function.
3) heuristics.py

Our heuristic is evaluation function which minimax function uses. Simply it evaluates utilities of both player “X” and player “O” for a particular state in ‘calculate_score’ function. This function calls ‘get_Scores_for_Row’, ‘get_Scores_for_Column’, and ‘get_Scores_for_Diagonal’. These functions calculate scores of potential consecutive rows, columns, or diagonals of each player as each player tries to maximize their score and minimize other’s.
4) requestsAPI.py

This file contains python code of necessary API requests such as ‘createGame’, ‘makeMove’, ‘getMoves’, and more.
5) main.py

This is main program where games with other teams are initialized and played.
