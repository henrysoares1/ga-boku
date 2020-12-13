
class Individual:
    def __init__(self, x: int, y: int):
        self.__chromosome = self.__compose_chromosome(x,y)
        self.__fitness = 0
        self.__is_sandwich = False
        self.__sandwich_coords = []

    def set_is_sandwich(self):
        self.__is_sandwich = True

    def get_is_sandwich(self):
        return self.__is_sandwich

    def add_sandwiched_enemies(self, x: int, y: int):
        self.__sandwich_coords.append((x,y))

    def get_sandwiched_enemies(self):
        return self.__sandwich_coords

    def __compose_chromosome(self, x: int, y: int):
        chromo = y
        chromo <<= 5
        chromo |= x

        return chromo

    def get_coordinates(self):
        val = 31
        x = self.__chromosome & val
        val <<= 5
        y = self.__chromosome & val
        y >>= 5

        return (x, y)

    def get_chromosome(self):
        return self.__chromosome

    def set_chromosome(self, chromo):
        self.__chromosome = chromo

    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness
