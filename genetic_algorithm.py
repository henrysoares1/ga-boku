from individual import Individual
from population import Population
from board_game import GameBoard
import random

class GeneticAlgorithm:

    def __init__(self, size, board: GameBoard, player, retention, mutation, diversity, no_growth):
        self.__size = size
        self.__board = board
        self.__player = player
        self.__retention_rate = retention
        self.__mutation_rate = mutation
        self.__diversity_rate = diversity
        self.__no_growth_value = no_growth
        self.__invalid_pos = []

    
    def add_invalid_pos(self, x: int, y: int):
        self.__invalid_pos.append((x,y))

    
    def get_player_num(self):
        return self.__player


    def get_fittest(self):
        pop = Population(self.__size, self.__board.game_board, self.__invalid_pos)
        counter = 0
        best = pop.population[0]

        while True:
            for individual in pop.population:
                individual.set_fitness(pop.fitness(individual, self.__player))

            pop.population.sort(key=lambda x: x.get_fitness(), reverse=True)

            if pop.population[0].get_fitness() > best.get_fitness():
                best = pop.population[0]
                counter = 0
            else:
                counter += 1

            if counter > self.__no_growth_value:
                break

            index = int(len(pop.population) * self.__retention_rate)

            parents = pop.population[:index]
        
            for individual in pop.population[index:]:

                if random.random() < self.__diversity_rate:
                    parents.append(individual)

            children = []

            while len(parents)+len(children) < self.__size:
                index1 = random.randint(0, len(parents)-1)
                index2 = random.randint(0, len(parents)-1)

                if index1 != index2:
                    male = parents[index1]
                    female = parents[index2]

                    son1, son2 = self.__cross_over(male, female)

                    children.append(son1)
                    children.append(son2)

            for individual in children:
                if random.random() < self.__mutation_rate:
                    self.__mutation(individual)


            parents += children
            pop.population = parents
        
        pop.population.sort(key=lambda x: x.get_fitness(), reverse=True)

        return pop.population[0]


    def __mutation(self, individual: Individual):
        index = random.randint(0,9)
        
        chromo = individual.get_chromosome()

        chromo ^= (1 << index)

        individual.set_chromosome(chromo)


    def __cross_over(self, male, female):
        male_chromo = male.get_chromosome()
        female_chromo = female.get_chromosome()

        cut_point = random.randint(0, 8)

        tail_join = self.__gen_bit_chain(cut_point+1)

        head_join = 1023
        head_join >>= cut_point+1
        head_join <<= cut_point+1

        male_head = male_chromo & head_join
        male_tail = male_chromo & tail_join

        female_head = female_chromo & head_join
        female_tail = female_chromo & tail_join

        son1 = male_head | female_tail
        son2 = female_head | male_tail

        ind1 = Individual(0,0)
        ind1.set_chromosome(son1)

        ind2 = Individual(0,0)
        ind2.set_chromosome(son2)

        return ind1, ind2


    def __gen_bit_chain(self, size):
        bit_val = 1
        count = 1

        while count != size:
            bit_val <<= 1
            bit_val |= 1
            count += 1

        return bit_val