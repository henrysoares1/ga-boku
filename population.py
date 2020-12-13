from typing import Sequence
from individual import Individual
import random

class Population:
    
    def __init__(self, size, game_board):
        self.__size = size
        self.__game_board = game_board
        self.population = self.init_population()


    def init_population(self):
        pop = []
        for i in range(self.__size):
            y = random.randint(0, len(self.__game_board)-1)
            x = random.randint(0, len(self.__game_board[y])-1)
            pop.append(Individual(x, y))

        return pop
        

    def __horizontal(self, individual: Individual, player):
        x, y = individual.get_coordinates()

        fitness = self.__horizontal_esquerda( x, y, player) + self.__horizontal_direita( x, y, player)

        return fitness


    def __horizontal_esquerda(self, x, y, player):
        count_equal = 0
        queue = []

        queue.append((x,y))

        while queue:
            _x, _y = queue.pop(0)

            if _x-1 > 0 and self.__game_board[_y][_x-1] == player:
                queue.append((_x-1,_y))
                count_equal += 1

        return count_equal


    def __horizontal_direita(self, x, y, player):
        count_equal = 0
        queue = []

        queue.append((x,y))

        while queue:
            _x, _y = queue.pop(0)

            if _x+1 < len(self.__game_board[_y]) and self.__game_board[_y][_x+1] == player:
                queue.append((_x+1,_y))
                count_equal += 1

        return count_equal


    def __diagonal_secundaria(self, individual: Individual, player):
        x, y = individual.get_coordinates()

        fitness = self.__diagonal_secundaria_cima( x, y, player) + self.__diagonal_secundaria_baixo( x, y, player)

        return fitness


    def __diagonal_secundaria_cima(self, x, y, player):
        mid_line = (len(self.__game_board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x < len(self.__game_board[_y-1]):
                    if self.__game_board[_y-1][_x] == player:
                        diagonal_queue.append((_x,_y-1))
                        count_equal += 1
            
            else:
                if self.__game_board[_y-1][_x+1] == player:
                    diagonal_queue.append((_x+1,_y-1))
                    count_equal += 1

        return count_equal


    def __diagonal_secundaria_baixo(self, x, y, player):
        mid_line = (len(self.__game_board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y < mid_line:
                if self.__game_board[_y+1][_x] == player:
                    diagonal_queue.append((_x,_y+1))
                    count_equal += 1
            
            else:
                if _y+1 < len(self.__game_board) and _x-1 >= 0:
                    if self.__game_board[_y+1][_x-1] == player:
                        diagonal_queue.append((_x-1,_y+1))
                        count_equal += 1

        return count_equal


    def __diagonal_principal(self, individual: Individual, player):
        x, y = individual.get_coordinates()

        fitness = self.__diagonal_principal_cima( x, y, player) + self.__diagonal_principal_baixo( x, y, player)

        return fitness


    def __diagonal_principal_cima(self, x, y, player):
        mid_line = (len(self.__game_board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x - 1 >=0:
                    if self.__game_board[_y-1][_x-1] == player:
                        diagonal_queue.append((_x-1,_y-1))
                        count_equal += 1
            else:
                if self.__game_board[_y-1][_x] == player:
                    diagonal_queue.append((_x,_y-1))
                    count_equal += 1


        return count_equal


    def __diagonal_principal_baixo(self, x, y, player):
        mid_line = (len(self.__game_board)-1)/2
        count_equal = 0
        diagonal_queue = []

        diagonal_queue.append((x,y))

        while diagonal_queue:
            _x, _y = diagonal_queue.pop(0)

            if _y < mid_line:
                if self.__game_board[_y+1][_x+1] == player:
                    diagonal_queue.append((_x+1,_y+1))
                    count_equal += 1
            else:
                if _y+1 < len(self.__game_board) and _x < len(self.__game_board[_y+1]):
                    if self.__game_board[_y+1][_x] == player:
                        diagonal_queue.append((_x,_y+1))
                        count_equal += 1
            

        return count_equal


    def __sandwich_dp_cima(self, x, y, player, enemy):
        mid_line = (len(self.__game_board)-1)/2
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x-1 >= 0 and self.__game_board[_y-1][_x-1] != 0:
                    count += 1
                    sandwich_queue.append((_x-1,_y-1))
                    if self.__game_board[_y-1][_x-1] == player:
                        sequence_queue.append((player, (_x-1,_y-1)))
                    else:
                        sequence_queue.append((enemy, (_x-1,_y-1)))
            else:
                if self.__game_board[_y-1][_x] != 0:
                    count += 1
                    sandwich_queue.append((_x,_y-1))
                    if self.__game_board[_y-1][_x] == player:
                        sequence_queue.append((player, (_x,_y-1)))
                    else:
                        sequence_queue.append((enemy, (_x,_y-1)))

        return sequence_queue


    def __sandwich_dp_baixo(self, x, y, player, enemy):
        mid_line = (len(self.__game_board)-1)/2
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _y < mid_line:
                if self.__game_board[_y+1][_x+1] != 0:
                    count += 1
                    sandwich_queue.append((_x-1,_y-1))
                    if self.__game_board[_y-1][_x-1] == player:
                        sequence_queue.append((player, (_x-1,_y-1)))
                    else:
                        sequence_queue.append((enemy, (_x-1,_y-1)))
            else:
                if _y+1 < len(self.__game_board) and _x < len(self.__game_board[_y+1]) and self.__game_board[_y+1][_x] != 0:
                    count += 1
                    sandwich_queue.append((_x,_y+1))
                    if self.__game_board[_y+1][_x] == player:
                        sequence_queue.append((player, (_x,_y+1)))
                    else:
                        sequence_queue.append((enemy, (_x,_y+1)))

        return sequence_queue


    def __sandwich_ds_cima(self, x, y, player, enemy):
        mid_line = (len(self.__game_board)-1)/2
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _y <= mid_line:
                if _y-1 >= 0 and _x < len(self.__game_board[_y-1]) and self.__game_board[_y-1][_x] != 0:
                    count += 1
                    sandwich_queue.append((_x,_y-1))
                    if self.__game_board[_y-1][_x] == player:
                        sequence_queue.append((player, (_x,_y-1)))
                    else:
                        sequence_queue.append((enemy, (_x,_y-1)))
            else:
                if self.__game_board[_y-1][_x+1] != 0:
                    count += 1
                    sandwich_queue.append((_x+1,_y-1))
                    if self.__game_board[_y-1][_x+1] == player:
                        sequence_queue.append((player, (_x+1,_y-1)))
                    else:
                        sequence_queue.append((enemy, (_x+1,_y-1)))

        return sequence_queue


    def __sandwich_ds_baixo(self, x, y, player, enemy):
        mid_line = (len(self.__game_board)-1)/2
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _y < mid_line:
                if self.__game_board[_y+1][_x] != 0:
                    count += 1
                    sandwich_queue.append((_x,_y+1))
                    if self.__game_board[_y+1][_x] == player:
                        sequence_queue.append((player, (_x,_y+1)))
                    else:
                        sequence_queue.append((enemy, (_x,_y+1)))
            else:
                if _y+1 < len(self.__game_board) and _x-1 >= 0 and self.__game_board[_y+1][_x-1] != 0:
                    count += 1
                    sandwich_queue.append((_x-1,_y+1))
                    if self.__game_board[_y+1][_x-1] == player:
                        sequence_queue.append((player, (_x-1,_y+1)))
                    else:
                        sequence_queue.append((enemy, (_x-1,_y+1)))

        return sequence_queue


    def __sandwich_h_esquerda(self, x, y, player, enemy):
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _x-1 > 0 and self.__game_board[_y][_x-1] != 0:
                count += 1
                sandwich_queue.append((_x-1,_y))

                if self.__game_board[_y][_x-1] == player:
                    sequence_queue.append((player, (_x-1,_y)))
                else:
                    sequence_queue.append((enemy, (_x-1,_y)))

        return sequence_queue


    def __sandwich_h_direita(self, x, y, player, enemy):
        sandwich_queue = []
        sequence_queue = []
        count = 0

        sandwich_queue.append((x,y))

        while sandwich_queue and count < 2:
            _x, _y = sandwich_queue.pop(0)

            if _x+1 < len(self.__game_board[_y]) and self.__game_board[_y][_x+1] != 0:
                count += 1
                sandwich_queue.append((_x+1,_y))

                if self.__game_board[_y][_x+1] == player:
                    sequence_queue.append((player, (_x+1,_y)))
                else:
                    sequence_queue.append((enemy, (_x+1,_y)))

        return sequence_queue


    def __sandwich(self, individual: Individual, player, enemy):
        x, y = individual.get_coordinates()

        seq_dp_cima = self.__sandwich_dp_cima(x, y, player, enemy)
        seq_dp_baixo = self.__sandwich_dp_baixo(x, y, player, enemy)
        seq_ds_cima = self.__sandwich_ds_cima(x, y, player, enemy)
        seq_ds_baixo = self.__sandwich_ds_baixo(x, y, player, enemy)
        seq_h_esq = self.__sandwich_h_esquerda(x, y, player, enemy)
        seq_h_dir = self.__sandwich_h_direita(x, y, player, enemy)

        all_sequence = [seq_dp_cima, seq_dp_baixo, seq_ds_cima, seq_ds_baixo, seq_h_esq, seq_h_dir]
        counter = 0

        for sequence in all_sequence:
            if sequence and len(sequence) == 2:
                seq_player0, coords0 = sequence[0]
                seq_player1, _ = sequence[1]
                if seq_player0 == enemy and seq_player1 == player:
                    counter += 1
                    x, y = coords0
                    individual.add_sandwiched_enemies(x, y)

        if counter > 0:
            individual.set_is_sandwich()

        return counter


    def fitness(self, individual: Individual, player):
        x, y = individual.get_coordinates()

        if y < 0 or y > len(self.__game_board)-1 or x < 0 or x > len(self.__game_board[y])-1 or self.__game_board[y][x] != 0:
            return -1

        enemy = 2 if player == 1 else 1

        horizontal_fit = self.__horizontal(individual, player)
        dp_fit = self.__diagonal_principal(individual, player)
        ds_fit = self.__diagonal_secundaria(individual, player)

        ct_horiz_fit = self.__horizontal(individual, enemy)
        ct_dp_fit = self.__diagonal_principal(individual, enemy)
        ct_ds_fit = self.__diagonal_secundaria(individual, enemy)

        fitness = horizontal_fit + dp_fit + ds_fit
        ct_fitness = ct_dp_fit + ct_ds_fit + ct_horiz_fit
        sandwich = self.__sandwich(individual, player, enemy)

        if ct_horiz_fit >= 3 or ct_dp_fit >= 3 or ct_ds_fit >= 3:
            ct_fitness *= 10

        if horizontal_fit == 4 or dp_fit == 4 or ds_fit == 4:
            fitness *= 10

        if sandwich > 0:
            sandwich *= 3

        return fitness + ct_fitness + sandwich