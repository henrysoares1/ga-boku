from board_game import GameBoard
from individual import Individual
from population import Population
from genetic_algorithm import GeneticAlgorithm

tabuleiro = GameBoard()
_population = Population(tabuleiro)

""" tabuleiro.player_move(1, 0, 0)
tabuleiro.player_move(1, 1, 0)
tabuleiro.player_move(1, 2, 0)
tabuleiro.player_move(1, 0, 1)
tabuleiro.player_move(1, 0, 16)
tabuleiro.player_move(1, 1, 16)
tabuleiro.player_move(1, 0, 15)
tabuleiro.player_move(1, 0, 14)
tabuleiro.player_move(1, 1, 15)
tabuleiro.player_move(1, 0, 17) """
tabuleiro.player_move(1, 12, 8)
tabuleiro.player_move(1, 12, 9)
tabuleiro.player_move(1, 12, 10)
tabuleiro.player_move(1, 10, 12)
print(tabuleiro)

ind = Individual(11, 11)

print(_population.diagonal_secundaria(tabuleiro, ind,1))

#population = ga.create_pop(10)

#for ind in population:
#    x, y = ind.get_coordinates()
#    print(x, y)
#print(tabuleiro)
#tabuleiro.player_move(1, 1, 1)
#print(tabuleiro)