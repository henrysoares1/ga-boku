from individual import Individual
import random

class GeneticAlgorithm:

    def __init__(self):
        self.test=''

    def create_pop(self, pop_size):
        pop = []
        for i in range(pop_size):
            x = random.randint(0, 15)
            y = random.randint(0, 21)
            pop.append(Individual(x, y))

        return pop

    def fitness(self, board, individual, player):
        x, y = individual.get_coordinates()
        fitness = 0
        if len(board.game_board)-1 >= y and len(board.game_board[y])-1 >= x and board.game_board[y][x] == 0: #verifica se jogada é valida
            for item in board.game_board[y]: # fitness na horizontal
                if item == player:
                    fitness += 1

            #add aqui a fitness na diagonal
        else:
            fitness = -1 #posição inválida = fitness -1
        
        individual.set_fitness(fitness)

    
