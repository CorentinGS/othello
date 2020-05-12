import numpy as np

from board import print_board, get_legal_move, print_legal_moves, take_player_turn


def get_player() -> (str, str):
    player_1 = str(input("Enter the first player's name:> "))
    while player_1.isspace():
        player_1 = str(input("Invalid name, Enter the first player's name:> "))
    player_2 = str(input("Enter second player's name:> "))
    while player_2.isspace():
        player_2 = str(input("Invalid name, Enter second player's name:> "))
    print("Name J1: {0} | Name J2: {1}".format(player_1, player_2))
    return player_1, player_2


# Start game
def start_game():
    player_1, player_2 = get_player()
    end = False
    # Afficher le plateau
    board = np.zeros(shape=(8, 8))  # Plateau vierge
    # Position init
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    board[4][4] = 1
    print_board(board, str(player_1), str(player_2))
    while not end:
        black_legal_moves = get_legal_move(board, 2)
        moves = print_legal_moves(board, black_legal_moves, 2)
        board = take_player_turn(board, moves, 2)
        white_legal_moves = get_legal_move(board, 1)
        moves = print_legal_moves(board, white_legal_moves, 1)
        board = take_player_turn(board, moves, 1)


start_game()
