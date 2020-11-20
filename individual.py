
class Individual:
    def __init__(self, size):
        self.size =  size
        self.chromosome = self.__create_board()

    def __create_board(self):

        board = []
        new_row = []
        row_elements = 5
        flag = True         # flag pra saber se ele ta antes ou depois da metade do tabuleiro

        while row_elements >= 5:
        
          for i in range(0, row_elements):
              new_row.append(0)

          if row_elements < self.size and flag:
              row_elements += 1
          else:
              row_elements -= 1
              flag = False

          board.append(new_row)
          new_row = []

        return board


    def __str__(self):
        board = ""

        for row in self.chromosome:
            word = ""
            for pos in row:
                word += "{0} ".format(pos)
            word = word.center(self.size*2)    
            word += "\n"
            board += word    

        return board


    def fitness(self):
        pass