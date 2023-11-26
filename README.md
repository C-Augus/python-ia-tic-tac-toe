# Tic-Tac-Toe with Minimax AI

## Introduction
This Python code implements the classic Tic-Tac-Toe game, allowing a user to play against a simple Artificial Intelligence (AI). The AI employs the Minimax algorithm to make strategic decisions during the game. This documentation provides a theoretical overview of the code, explaining key concepts, strategies, and implemented functionalities.

## 1. Tic-Tac-Toe
Tic-Tac-Toe is a two-player board game where the objective is to form a line of three symbols (X or O) on a 3x3 board. Players take turns making moves, and the game ends when a player achieves victory or a draw occurs.

## 2. Board Representation
The board is represented by a 3x3 matrix, where each cell can contain one of the following values:

- 'X': Indicates the user's move.
- 'O': Indicates the AI's move.
- ' ': Indicates an empty cell.

## 3. Main Functions
### 3.1. `display_board(board)`
This function displays the current state of the board in the console, providing a clear view of the game situation.

### 3.2. `check_victory(board, player)`
Determines if the specified player has won the game. It checks rows, columns, and diagonals for a winning combination.

### 3.3. `board_full(board)`
Checks if the board is completely filled, indicating a draw.

### 3.4. `valid_move(board, row, col)`
Checks if a move is valid at a given position on the board.

### 3.5. `make_move(board, player, row, col)`
Registers the move on the board, updating the game state.

## 4. Minimax Algorithm
The Minimax algorithm is used by the AI to make decisions during its moves. It explores all possible moves, assigning values to each game state. The goal is to maximize the score when it's the AI's turn and minimize the score when it's the human player's turn.

### 4.1. `minimax(board, depth, maximizing)`
A recursive function that evaluates the score of a game state using the Minimax algorithm.

### 4.2. `ai_move(board)`
Determines the best move for the AI using the Minimax algorithm, choosing the move with the highest score.

## 5. Game Logic
The game logic is managed by the `play_tic_tac_toe()` function. It guides players through their moves, displays the board, checks for victories or draws, and alternates between the human player and the AI.

## Conclusion
This code provides a basic but functional implementation of Tic-Tac-Toe with an AI based on the Minimax algorithm. It serves as an educational example of integrating artificial intelligence into a simple game. There is room for expansion and improvements, such as enhancing the user interface, optimizing the Minimax algorithm, and adding additional features for a more engaging experience. Feel free to explore and build upon this project!
