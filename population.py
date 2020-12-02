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


    def left_diagonal(self, board, x, y, flag, player):
        middle_row = (len(board)-1)/2  # pega o indice da linha do meio
        board_size = len(board)-1 # isso retorna quantas colunas aquela linha tem - SÓ QUE NÃO
        if board_size >= x+1:
            row_size = len(board[x+1])-1
            if row_size >= y:
                if x < middle_row:
                    if board[x+1][y] == player:
                        flag += 1
                        if flag == 5:
                            return 100
                        else:
                            return self.left_diagonal(board, x+1, y, flag, player)
                else:
                    if board[x+1][y-1] == player:
                        flag += 1
                        if flag == 5:
                            return 100
                        else:
                            return self.left_diagonal(board, x+1, y-1, flag, player)
            
        return flag

    def right_diagonal(self, board, x, y, flag, player):
        middle_row = (len(board)-1)/2
        board_size = len(board)-1
        if board_size >= x+1:
            row_size = len(board[x+1])-1
            if x < middle_row:    
                if row_size >= y+1:
                    if board[x+1][y+1] == player:
                        flag += 1
                        if flag == 5:
                            return 100
                        else:
                            return self.right_diagonal(board, x+1, y+1, flag, player)
            else:
                if row_size >= y:
                    if board[x+1][y] == player:
                        flag += 1
                        if flag == 5:
                            return 100
                        else:
                            return self.right_diagonal(board, x+1, y, flag, player)
        
        return flag

    def horizontal(self, board, x, y, flag, player):
        row_size = len(board[x])-1
        if row_size >= y+1:
            if board[x][y+1] == player:
                flag += 1
                if flag == 5:
                    return 100
                else:
                    return self.horizontal(board, x, y+1, flag, player)

        return flag

    def diagonal_principal(self, board, x, y, player):
        mid_line = 

    def fitness(self, board, individual, player):
        x, y = individual.get_coordinates()
        temp_board = board.game_board[:]
        fitness = 0
        if len(board.game_board)-1 >= y and len(board.game_board[y])-1 >= x and board.game_board[y][x] == 0: #verifica se jogada é valida
            temp_board[y][x] = player
            flag = 1
            for i in range(0,len(temp_board)-1):
                for j in range(0,len(temp_board[i])):
                    if not temp_board[i][j] == 0:
                        left = self.left_diagonal(temp_board, i, j, flag, player)
                        right = self.right_diagonal(temp_board, i, j, flag, player)
                        horizontal = self.horizontal(temp_board, i, j, flag, player)
                        total = max(left, right, horizontal)
                        fitness = total if total > fitness else fitness

            return fitness

        else:
            print(x, y)
            fitness = -1 #posição inválida = fitness -1
            return fitness
        #individual.set_fitness(fitness)