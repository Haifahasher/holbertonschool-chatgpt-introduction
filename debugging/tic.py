#!/usr/bin/python3

def print_board(board):
    """
    Display the board in a 3×3 grid.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)  # matches width of "X | O | X"

def check_winner(board):
    """
    Return True if there is a three-in-a-row on rows, columns, or diagonals.
    """
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current = "X"

    while True:
        print_board(board)

        # --- Input with validation ---
        try:
            row = int(input(f"Player {current}, enter row (0–2): "))
            col = int(input(f"Player {current}, enter column (0–2): "))
        except ValueError:
            print("  → Please enter valid integers 0, 1, or 2.\n")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("  → Row and column must each be 0, 1, or 2.\n")
            continue

        if board[row][col] != " ":
            print("  → That spot is already taken! Try again.\n")
            continue

        # --- Place marker ---
        board[row][col] = current

        # --- Win check ---
        if check_winner(board):
            print_board(board)
            print(f"Player {current} wins!")
            break

        # --- Draw check ---
        if all(cell != " " for r in board for cell in r):
            print_board(board)
            print("It's a draw!")
            break

        # --- Switch player ---
        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

