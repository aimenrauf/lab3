def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        # Check Row
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        #Check COlumn
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  
    return None 
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True 
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column): ")
        while True:
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken. Choose another cell.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            return
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!") 

tic_tac_toe()