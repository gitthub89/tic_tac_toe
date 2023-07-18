def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False


def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while ' ' in board:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if board[int(move) - 1] != ' ':
            print("Invalid move, try again.")
            continue
        board[int(move) - 1] = current_player
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    print("It's a draw!")


tic_tac_toe()
