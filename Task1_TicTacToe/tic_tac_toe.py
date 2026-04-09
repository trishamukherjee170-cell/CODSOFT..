def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i])
        print(" " + row)
        if i < 2:
            print("---|---|---")
    print("\n")


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -1000
    move = (0, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe AI")
    print("You are X, AI is O")
    print("Enter row and column (0-2)\n")

    while True:
        print_board(board)

        # User move
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move! Try again.")
                continue
        except:
            print("Invalid input!")
            continue

        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break

        if is_full(board):
            print_board(board)
            print("Draw!")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print(f"AI played at ({ai_row}, {ai_col})")

        if check_winner(board, "O"):
            print_board(board)
            print("💻 Computer wins!")
            break

        if is_full(board):
            print_board(board)
            print("Draw!")
            break


# Run the game
play_game()