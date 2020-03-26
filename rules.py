# Display Rules
def display_rules():
  print ("\033[41mRules\033[0m") # Affiche "Rules" en fluo rouge
  print ("\033[32mLe but du jeu:\033[0m")
  print ("\033[36m Avoir plus de pions de sa couleur que l’adversaire à la fin de la partie. La partie se termine lorsque aucun des deux joueurs ne peut plus jouer de coup légal ou  lorsque les 64 cases sont occupées.\033[0m")
  print ("\033[32mPosition de départ:\033[0m")  
  print ("\033[36m Au début de la partie, deux pions\033[0m")
  print("\033[40m noirs en:\033[0m")
  print("\033[30m (3;4) et (4;3)\033[0m")
  print("\033[36mEt deux pions\033[0m")
  print("\033[47m blanc en:\033[0m")
  print("\033[37m (3;3) et (4;4)\033[0m")
  print("\033[30m Les Noirs commence toujours et les deux adversaires jouent ensuite à tour de rôle. \033[0m")
  print ("\033[32mLa pose d’un pion:\033[0m")
  print ("\033[36m A son tour de jeu, le joueur doit poser son pion sur une case vide du plateau,adjacente à un pion adverse. Il doit également,en posant son pion,encadrer un ou plusieurs pions adverses entre le pion qu’il pose et un pion à sa couleur,déjà placé sur le plateau. Un coup qui encadre son adversaire peut se faire aussi bien horizontalement ou verticalement,qu’en diagonale. Les pions que le joueur vient d'encadrer deviennent les sien et prennent sa couleur. \033[0m")


