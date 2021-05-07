def display_board(board):
    print('\n'*100)
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print("--------------")
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print("--------------")
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])

test_board = ['X', 'O']*10

def player_input():
    marker = ''
    # Asking Player 1 To Choose X or O

    while marker != 'X'and marker != 'O':
        marker = input("Player 1, Choose X or O : ").upper()

    # Assigning Player 2 the other marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

def place_marker(marker, board, position):
    board[position] = marker

place_marker(test_board,,8)
display_board(test_board)

