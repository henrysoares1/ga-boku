
class Individual:
    def __init__(self, x: int, y: int):
        self.chromosome = self.__compose_chromosome(x,y)

    def __compose_chromosome(self, x: int, y: int):
        chromo = y
        chromo <<= 4
        chromo |= x

        return chromo

    def get_chromosome(self):
        return self.chromosome

    def get_fitness(self):
        pass

    def set_fitness(self):
        pass


if __name__ == "__main__":
    individuo = Individual(10,8)

    print(individuo.get_chromosome())