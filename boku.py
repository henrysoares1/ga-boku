from board_game import GameBoard
from individual import Individual
from population import Population
from genetic_algorithm import GeneticAlgorithm

tabuleiro = GameBoard()
_population = Population(tabuleiro)

tabuleiro.player_move(1, 12, 8)
tabuleiro.player_move(1, 10, 8)
tabuleiro.player_move(2, 12, 9)
tabuleiro.player_move(2, 11, 9)

tabuleiro.player_move(2, 11, 10)
tabuleiro.player_move(1, 10, 10)
tabuleiro.player_move(2, 13, 10)
tabuleiro.player_move(1, 14, 10)

tabuleiro.player_move(2, 11, 11)
tabuleiro.player_move(1, 10, 12)

tabuleiro.player_move(2, 12, 11)
tabuleiro.player_move(1, 12, 12)

print(tabuleiro)

ind = Individual(12, 10)

print(_population.sandwich(tabuleiro.game_board, ind, 1, 2))

#population = ga.create_pop(10)

#for ind in population:
#    x, y = ind.get_coordinates()
#    print(x, y)
#print(tabuleiro)
#tabuleiro.player_move(1, 1, 1)
#print(tabuleiro)