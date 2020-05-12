from random import choice

import numpy as np
from termcolor import colored

board_row_top = '-------------------------------'

white_piece = colored('●', 'white')
white_legal_move = colored('●', 'white', attrs=['blink'])
black_piece = colored('●', 'blue')
black_legal_move = colored('●', 'blue', attrs=['blink'])
board_piece = {
    0: '   |',
    1: ' ' + white_piece + ' |',
    2: ' ' + black_piece + ' |'
}


# Print Board
def print_board(board: np.array, player_1: str, player_2: str):
    # Scores
    score_black = len(np.where(board == 2)[0])
    score_white = len(np.where(board == 1)[0])
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
            row += colored('       Score | ', 'red') + colored(
                player_1 + ': ' + str(score_black), 'blue')
        if i == 3:
            row += colored('	         | ',
                           'red') + player_2 + ': ' + str(score_white)
        print(row)
        if not i == 7:
            print(
                colored('  +', 'blue') + board_row_top + colored('+', 'blue'))
    # Bottom row
    print('  ' + colored("\\" + board_row_top + '/', 'blue'))


def get_legal_move(board: np.array, player_color: int) -> list:
    legal_moves = []
    if player_color == 1:
        opponent_color = 2
    else:
        opponent_color = 1
    player_pieces = np.where(board == player_color)

    for piece in zip(player_pieces[0], player_pieces[1]):
        row = piece[0]
        col = piece[1]
        box = get_box(board, row, col)
        opp_pieces = np.where(box == opponent_color)
        for move in zip(opp_pieces[0], opp_pieces[1]):
            y_direction = move[0] - 1
            x_direction = move[1] - 1
            new_row = row + y_direction * 2
            new_col = col + x_direction * 2
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                if board[new_row][new_col] == 0:
                    if (new_row, new_col) not in legal_moves:
                        legal_moves.append((new_row, new_col))
                        break
                    else:
                        break
                elif board[new_row][new_col] == opponent_color:
                    new_row += y_direction
                    new_col += x_direction
                else:
                    break
    return legal_moves


def print_legal_moves(board: np.array, legal_moves: list, player: int) -> dict:
    # TODO: Ajouter les scores et le joueur qui doit jouer
    moves = {}
    x = 0
    print('  ' + colored('/' + board_row_top + '\\', 'red'))
    for i in range(0, 8):
        row = colored('  |', 'red')
        for j in range(0, 8):
            if (i, j) in legal_moves:
                x += 1
                row += ' ' + str(x) + ' |'
                moves[str(x)] = (i, j)
            else:
                row += board_piece[int(board[i][j])]
        row = row[:-1] + colored('|', 'red')
        print(row)
        if not i == 7:
            print(
                colored('  +', 'red') + board_row_top + colored('+', 'red'))
    print('  ' + colored('\\' + board_row_top + '/', 'red'))
    return moves


def take_player_turn(board: np.array, moves: dict, player: int) -> np.array:
    if not moves:
        return "No moves"
    num = 0

    while num not in moves.keys():
        num = str(input("Where do you want to play ? "))
    board = update_board(board, player, moves[num])
    return board


def update_board(board: np.array, player: int, pos: (int, int)) -> np.array:
    row: int = pos[0]
    col: int = pos[1]
    if player == 1:
        opponent_color = 2
    else:
        opponent_color = 1
    box = get_box(board, row, col)
    opponent_pieces = np.where(box == opponent_color)
    for move in zip(opponent_pieces[0], opponent_pieces[1]):
        y_direction = move[0] - 1
        x_direction = move[1] - 1

        new_row = row + y_direction * 2
        new_col = col + x_direction * 2
        pieces_to_flip = [(row, col), (row + y_direction, col + x_direction)]

        #  if cell is empty, stop
        #  if piece in cell is opponent's, add to pieces_to_flip list continue
        #  if piece in cell is your own, stop and flip pieces in pieces_to_flip
        #  continue moving one step in direction until above case or end of board
        while 0 <= new_row <= 7 and 0 <= new_col <= 7:
            if board[new_row][new_col] == opponent_color:
                pieces_to_flip.append((new_row, new_col))
                new_row += y_direction
                new_col += x_direction
            elif board[new_row][new_col] == player:
                for piece in pieces_to_flip:
                    board[piece[0]][piece[1]] = player
                break
            else:
                # empty cell
                break

    return board


def get_box(board: np.array, row: int, col: int) -> np.array:
    if 0 < row < 7 and 0 < col < 7:
        box = np.reshape([
            board[i][j] for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
        ], (3, 3))
        return box
    # Bord du haut
    elif row == 0 and col not in (0, 7):
        box = np.reshape([
            board[i][j] for i in range(row, row + 2)
            for j in range(col - 1, col + 2)
        ], (2, 3))
        box = np.concatenate((np.array([[0., 0., 0.]]), box))
        return box
    # Bord du bas
    elif row == 7 and col not in (0, 7):
        box = np.reshape([
            board[i][j] for i in range(row - 1, row + 1)
            for j in range(col - 1, col + 2)
        ], (2, 3))
        box = np.concatenate((box, np.array([[0., 0., 0.]])))
        return box
    # Bord de gauche
    elif col == 0 and row not in (0, 7):
        box = np.reshape([
            board[i][j] for i in range(row - 1, row + 2)
            for j in range(col, col + 2)
        ], (3, 2))
        box = np.concatenate((np.array([[0., 0., 0.]]).T, box), axis=1)
        return box
    # Bord de droite
    elif col == 7 and row not in (0, 7):
        box = np.reshape([
            board[i][j] for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 1)
        ], (3, 2))
        box = np.concatenate((box, np.array([[0., 0., 0.]]).T), axis=1)
        return box
    else:
        if row == 0 and col == 0:
            box = np.reshape([
                board[i][j] for i in range(row, row + 2)
                for j in range(col, col + 2)
            ], (2, 2))
            box = np.pad(
                box,
                pad_width=((1, 0), (1, 0)),
                mode='constant',
                constant_values=0)
        elif row == 0 and col == 7:
            box = np.reshape([
                board[i][j] for i in range(row, row + 2)
                for j in range(col - 1, col + 1)
            ], (2, 2))
            box = np.pad(
                box,
                pad_width=((1, 0), (0, 1)),
                mode='constant',
                constant_values=0)
        elif row == 7 and col == 0:
            box = np.reshape([
                board[i][j] for i in range(row - 1, row + 1)
                for j in range(col, col + 2)
            ], (2, 2))
            box = np.pad(
                box,
                pad_width=((0, 1), (1, 0)),
                mode='constant',
                constant_values=0)
        elif row == 7 and col == 7:
            box = np.reshape([
                board[i][j] for i in range(row - 1, row + 1)
                for j in range(col - 1, col + 1)
            ], (2, 2))
            box = np.pad(
                box,
                pad_width=((0, 1), (0, 1)),
                mode='constant',
                constant_values=0)
    return box


def commentaire():
    liste = [
        "Perfect", "You are a champion", "Good job ", "Well done", "Wow ! "
    ]
    resultat = choice(liste)
    print(resultat)
