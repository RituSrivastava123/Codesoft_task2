def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth  # AI wins, faster is better
    elif check_winner(board, 'X'):
        return depth - 10  # Human wins, slower is better
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_available_moves(board):
            temp = board[i][j]
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = temp
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_available_moves(board):
            temp = board[i][j]
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = temp
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = float('-inf')
    move = None
    for i, j in get_available_moves(board):
        temp = board[i][j]
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = temp
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")
            continue

        row, col = divmod(move, 3)
        if board[row][col] in ['X', 'O']:
            print("Cell already filled. Try again.")
            continue

        board[row][col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'O'
        print("AI has moved:")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Start game
if __name__ == "__main__":
    play_game()
