import numpy as np
from board import print_board

# Display Rules
def display_rules():
  print ("\033[41mRules\033[0m") # Affiche "Rules" en fluo rouge
  print ("\033[32mThe goal of the game: \033[0m")
  print ("\033[36m Having more checkers of his color than the opponent at the end of the game. The game ends when neither player can make a legal move or when all 64 squares are occupied.\033[0m")
  print ("\033[32mStarting position:\033[0m")  
  print ("\033[36m At the beginning of the game,\033[0m")
  print("\033[34m  two black pawns in:\033[0m")
  print("\033[34m  (3;4) and (4;3)\033[0m")
  print("\033[36m AND\033[0m")
  print("\033[37m  two white pawns in:\033[0m")
  print("\033[37m  (3;3) and (4;4)\033[0m")
  print("\033[36m See the example:\033[0m")
  board = np.zeros(shape=(8, 8))  # Plateau vierge
  # Position init
  board[3][3] = 2
  board[3][4] = 1
  board[4][3] = 1
  board[4][4] = 2
  print_board(board)

  print("\033[36m Black always starts first and then the two opponents take turns. \033[0m")
  print ("\033[32mPawn laying:\033[0m")
  print ("\033[36m  On his turn, the player must place his checker on an empty square on the board, adjacent to an opponent's checker. He must also, when placing his pawn on the board, place one or more of his opponent's pawns between the pawn he is placing and a pawn of his own colour, already placed on the board. A move that frames the opponent's checkers can be made horizontally, vertically or diagonally. The checkers that the player has just framed become his own and take his colour. \033[0m")
  
  return
  
