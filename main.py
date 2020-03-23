import numpy as np

from board import print_board
from rules import display_rules


# Start game
def start_game():
    global player_1
    global player_2

    # Choisir de jouer ou d'afficher les règles
    choice = input("Do you want to play or to read the rules ? (play / rules): ").lower()
    while choice != "play" and choice != "rules":
        choice = input("Invalid entry. Do you want to play or to read the rules ? (play / rules): ").lower()
    if choice in ["rules", "r"]:
        display_rules()
    elif choice in ["play", 'p']:
        # Afficher le plateau
        board = np.zeros(shape=(8, 8))  # Plateau vierge
        # Position init
        board[3][3] = 2
        board[3][4] = 1
        board[4][3] = 1
        board[4][4] = 2
        print_board(board)


start_game()
