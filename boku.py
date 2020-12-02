from board_game import GameBoard
from individual import Individual
from population import Population
from genetic_algorithm import GeneticAlgorithm

_popultaion = Population()
tabuleiro = GameBoard(14)

tabuleiro.player_move(1, 0, 0)
tabuleiro.player_move(1, 1, 0)
tabuleiro.player_move(1, 2, 0)
tabuleiro.player_move(1, 0, 1)
tabuleiro.player_move(1, 0, 16)
tabuleiro.player_move(1, 1, 16)
tabuleiro.player_move(1, 0, 15)
tabuleiro.player_move(1, 0, 14)
tabuleiro.player_move(1, 1, 15)
tabuleiro.player_move(1, 0, 17)
print(tabuleiro)

ind = Individual(0, 2)

print(_popultaion.fitness(tabuleiro, ind, 1))

#population = ga.create_pop(10)

#for ind in population:
#    x, y = ind.get_coordinates()
#    print(x, y)
#print(tabuleiro)
#tabuleiro.player_move(1, 1, 1)
#print(tabuleiro)