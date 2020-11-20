

def start_board(size):

  board = []
  new_row = []
  row_elements =  5
  flag = True         # flag pra saber se ele ta antes ou depois da metade do tabuleiro
  
  while row_elements >= 5:  
    if row_elements < size and flag:
      for i in range(0,row_elements):
        new_row.append(0)
      row_elements = row_elements +1
    else:
      for i in range(0,row_elements):
        new_row.append(0)
      row_elements = row_elements -1
      flag = False
    board.append(new_row)
    new_row = []

  return board

def print_board(board):
  for i in board:
      print(i)

  return 0


tabuleiro = start_board(10)
print_board(tabuleiro)