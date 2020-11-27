
class Individual:
    def __init__(self, x: int, y: int):
        self.chromosome = self.__compose_chromosome(x,y)

    def __compose_chromosome(self, x: int, y: int):
        chromo = y
        chromo <<= 4
        chromo |= x

        return chromo


    def fitness(self):
        pass