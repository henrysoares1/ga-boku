
class Individual:
    def __init__(self, x: int, y: int):
        self.chromosome = self.__compose_chromosome(x,y)
        self.fitness = 0

    def __compose_chromosome(self, x: int, y: int):
        chromo = y
        chromo <<= 5
        chromo |= x

        return chromo

    def get_coordinates(self):
        val = 31
        x = self.chromosome & val
        val <<= 5
        y = self.chromosome & val
        y >>= 5

        return (x, y)

    def get_chromosome(self):
        return self.chromosome

    def set_chromosome(self, chromo):
        self.chromosome = chromo

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, fitness):
        self.fitness = fitness


if __name__ == "__main__":
    individuo = Individual(15,1)

    print(individuo.get_chromosome())
    print(individuo.get_coordinates())