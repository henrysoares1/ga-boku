from individual import Individual
import random

class GeneticAlgorithm:

    def __init__(self):
        self.test=''

    def create_pop(self, pop_size):
        pop = []
        for i in range(pop_size):
            x = random.randint(0, board.size + 5)
            y = random.randint(0, board.size)
            pop.append(Individual(x, y))

        return pop
