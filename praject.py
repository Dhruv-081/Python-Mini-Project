import random

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the player has won
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return all([spot != ' ' for spot in board])

# Function to get a random move for the AI
def get_ai_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

# Main game function
def tic_tac_toe():
    board = [' ' for _ in range(9)]  # Initialize empty board
    current_player = 'X'  # Human player starts first
    
    while True:
        print_board(board)  # Show the current state of the board
        
        # Human player's turn
        if current_player == 'X':
            try:
                move = int(input("Player X, enter your move (1-9): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            if board[move] == ' ':  # Check if the chosen spot is empty
                board[move] = current_player  # Place the player's mark
            else:
                print("The spot is already taken. Choose another one.")
                continue
        # AI opponent's turn
        else:
            print("AI (Player O) is making a move...")
            move = get_ai_move(board)  # Get a random move for the AI
            board[move] = current_player  # AI places its mark

        # Check for win or draw
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
