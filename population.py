from individual import Individual
import random

class Population:
    
    def __init__(self, game_board):
        self.size = 20
        self.population = self.init_population()


    def init_population(self):
        pop = []
        for i in range(self.size):
            x = random.randint(0, 15)
            y = random.randint(0, 21)
            pop.append(Individual(x, y))

        return pop


    def horizontal(self, tabuleiro, individual, player):
        board = tabuleiro.game_board
        x, y = individual.get_coordinates()

        fitness = self.__horizontal_esquerda(board, x, y, player) + self.__horizontal_direita(board, x, y, player)

        return fitness


    def __horizontal_esquerda(self, board, x, y, player):
        count_equal = 0
        queue = []

        queue.append((x,y))

        while queue:
            _x, _y = queue.pop(0)

            if _x-1 > 0 and board[_y][_x-1] == player:
                queue.append((_x-1,_y))
                count_equal += 1

        return count_equal


    def __horizontal_direita(self, board, x, y, player):
        count_equal = 0
        queue = []

        queue.append((x,y))

        while queue:
            _x, _y = queue.pop(0)

            if _x+1 < len(board[_y]) and board[_y][_x+1] == player:
                queue.append((_x+1,_y))
                count_equal += 1

        return count_equal


    def diagonal_secundaria(self, tabuleiro, individual, player):
        board = tabuleiro.game_board
        x, y = individual.get_coordinates()

        fitness = self.__diagonal_secundaria_cima(board, x, y, player) + self.__diagonal_secundaria_baixo(board, x, y, player)

        return fitness


    def __diagonal_secundaria_cima(self, board, x, y, player):
        mid_line = (len(board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x < len(board[_y-1]):
                    if board[_y-1][_x] == player:
                        diagonal_queue.append((_x,_y-1))
                        count_equal += 1
            
            else:
                if board[_y-1][_x+1] == player:
                    diagonal_queue.append((_x+1,_y-1))
                    count_equal += 1

        return count_equal


    def __diagonal_secundaria_baixo(self, board, x, y, player):
        mid_line = (len(board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y < mid_line:
                if board[_y+1][_x] == player:
                    diagonal_queue.append((_x,_y+1))
                    count_equal += 1
            
            else:
                if _y+1 < len(board) and _x >= 0:
                    if board[_y+1][_x-1] == player:
                        diagonal_queue.append((_x+1,_y-1))
                        count_equal += 1

        return count_equal


    def diagonal_principal(self, tabuleiro, individual, player):

        board = tabuleiro.game_board
        x, y = individual.get_coordinates()

        fitness = self.__diagonal_principal_cima(board, x, y, player) + self.__diagonal_principal_baixo(board, x, y, player)

        return fitness


    def __diagonal_principal_cima(self, board, x, y, player):
        mid_line = (len(board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x - 1 >=0:
                    if board[_y-1][_x-1] == player:
                        diagonal_queue.append((_x-1,_y-1))
                        count_equal += 1
            else:
                if board[_y-1][_x] == player:
                    diagonal_queue.append((_x,_y-1))
                    count_equal += 1


        return count_equal


    def __diagonal_principal_baixo(self, board, x, y, player):
        mid_line = (len(board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y < mid_line:
                if board[_y+1][_x+1] == player:
                    diagonal_queue.append((_x+1,_y+1))
                    count_equal += 1
            else:
                if _y+1 < len(board) and _x < len(board[_y+1]):
                    if board[_y+1][_x] == player:
                        diagonal_queue.append((_x,_y+1))
                        count_equal += 1
            

        return count_equal


    def fitness(self, board, individual, player):
        _board = board.game_board
        x, y = individual.get_coordinates()

        if y < 0 or y > len(_board)-1 or x < 0 or x > len(_board[y])-1 or _board[y][x] != 0:
            return -1

        horizontal_fit = self.horizontal(board, individual, player)
        dp_fit = self.diagonal_principal(board, individual, player)
        ds_fit = self.diagonal_secundaria(board, individual, player)

        return horizontal_fit + dp_fit + ds_fit