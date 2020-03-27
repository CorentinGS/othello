import numpy as np
from board import print_board


# Display Rules
def display_rules():
  print ("\033[41mRules\033[0m") # Affiche "Rules" en fluo rouge
  print ("\033[32mLe but du jeu:\033[0m")
  print ("\033[36m Avoir plus de pions de sa couleur que l’adversaire à la fin de la partie. La partie se termine lorsque les 64 cases sont occupées.\033[0m")
  print ("\033[32mPosition de départ:\033[0m")  
  print ("\033[36m Au début de la partie, deux pions\033[0m")
  print("\033[34m noirs en:\033[0m")
  print("\033[34m (3;4) et (4;3)\033[0m")
  print("\033[36mEt deux pions\033[0m")
  print("\033[37m blanc en:\033[0m")
  print("\033[37m (3;3) et (4;4)\033[0m")
  print("\033[36mVoir l'exemple:\033[0m")
  board = np.zeros(shape=(8, 8))  # Plateau vierge
  # Position init
  board[3][3] = 2
  board[3][4] = 1
  board[4][3] = 1
  board[4][4] = 2
  print_board(board)

  print("\033[36m Les Noirs commencent toujours et les deux adversaires jouent ensuite à tour de rôle. \033[0m")
  print ("\033[32mLa pose d’un pion:\033[0m")
  print ("\033[36m A son tour de jeu, le joueur doit poser son pion sur une case vide du plateau, adjacente à un pion adverse. Il doit également, en posant son pion, encadrer un ou plusieurs pions adverses entre le pion qu’il pose et un pion de sa couleur, déjà placé sur le plateau. Un coup qui encadre son adversaire peut se faire aussi bien horizontalement, verticalement, ou en diagonale. Les pions que le joueur vient d'encadrer deviennent les siens et prennent sa couleur. \033[0m")


