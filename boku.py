from board_game import GameBoard
from individual import Individual
from board_game import GameBoard
from genetic_algorithm import GeneticAlgorithm

ga = GeneticAlgorithm()
tabuleiro = GameBoard(14)
ga.create_pop(tabuleiro, 5)
#print(tabuleiro)
#tabuleiro.player_move(1, 1, 1)
#print(tabuleiro)