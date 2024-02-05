#create a tic tac toe terminal game in python
# by utilizing prompt eningeering concepts, don't code it yourself
# to generate a series of prompts that will allow you to accomplish this task
#possibly use graphics terminal teams used for phone assignment

#Features---

#High-level features:
# human player turn
# pc turn
# human inputprint board for human to see 
# check after every move to see if:
# someone won
# or cats game

#Computer/AI
#computer ai, we can do player vs computer
#computer scripted to pick the same spots, just to start with and iteratively make it smarter(MVP first!)
#AI is random move

#User Input
#user inputs their move for each turn
#could ask user where to place their move by inputting row and column
#ask user if they want to be x or o--later, more complex part of feature

#Flow of Game
#1. who goes first? Player A
#2. Player A makes their move
#3. Now it's player B's turn
#4. Player B makes their move etc...

#Human Player
#1.Need to be able to see the board
#2.Prompt for their move
#3. Need to tell user how to enter their move

#Computer Player
#1.Randomly generates a move
#2.Needs to know spots available or if randomly generated move is valid or not

# print("|x| | |")
# print("-------")
# print("|0| | |")
# # or for another example
# print(f"|{row[0]}|{row[1]}|{row[2]}|")

#string constants or magic string that never changes in the program, assign it to a variable to make it harder for you to make a typo and enables better error check for VSCode (this also lets other programmers)

# X = "x"
# O = "o"
# EMPTY = " "
# board = [
#     [X, EMPTY, O],
#     [EMPTY, O, X],
#     [X, EMPTY, O]
# ]

#TIC TAC TOE TERMINAL GAME

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
