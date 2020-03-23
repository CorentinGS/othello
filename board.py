import numpy as np
from termcolor import colored

board_row_top = '-------------------------------'

white_piece = colored('●', 'white')
white_legal_move = colored('●', 'white', attrs=['blink'])
black_piece = colored('●', 'blue')
black_legal_move = colored('●', 'blue', attrs=['blink'])
board_piece = {0: '   |', 1: ' ' + white_piece + ' |', 2: ' ' + black_piece + ' |'}


# Print Board
def print_board(board):
    # Scores
    score_white = len(np.where(board == 1)[0])
    score_black = len(np.where(board == 2)[0])
    # Top row
    print('  ' + colored('/' + board_row_top + '\\', 'blue'))
    for i in range(0, 8):
        row = colored('  |', 'blue')
        for j in range(0, 8):
            # Afficher les pièces
            row += board_piece[int(board[i][j])]
        row = row[:-1] + colored('|', 'blue')
        # Afficher les scores
        if i == 2:
            row += colored('	   Score | ', 'red') + 'White: ' + str(score_white)
        if i == 3:
            row += colored('	         | ', 'red') + colored('Black: ' + str(score_black), 'blue')
        print(row)
        if not i == 7:
            print(colored('  +', 'blue') + board_row_top + colored('+', 'blue'))
    # Bottom row
    print('  ' + colored("\\" + board_row_top + '/', 'blue'))
