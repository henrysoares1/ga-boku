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

    
