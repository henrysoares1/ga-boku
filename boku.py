import time

from board_game import GameBoard
from individual import Individual
from population import Population
from genetic_algorithm import GeneticAlgorithm

tabuleiro = GameBoard()

player1 = GeneticAlgorithm(30, tabuleiro, 1, 0.2, 0.05, 0.02, 50)
player2 = GeneticAlgorithm(50, tabuleiro, 2, 0.2, 0.1, 0.05, 30)


while True:
    # Player 1
    print("\nPlayer ", player1.get_player_num(), " move:\n")
    player1_move = player1.getFittest()

    player1_x, player1_y = player1_move.get_coordinates()
    tabuleiro.player_move(player1.get_player_num(), player1_x, player1_y)

    print(tabuleiro)
    time.sleep(3)

    if player1_move.get_is_sandwich():
        remove_x, remove_y = player1_move.get_sandwiched_enemy()
        tabuleiro.remove_piece_at(remove_x, remove_y)
        player2.add_invalid_pos(remove_x, remove_y)
        print("\nPlayer ", player1.get_player_num(), " sanduichou o ", player2.get_player_num(), ":\n")
        print(tabuleiro)
        time.sleep(3)

    if tabuleiro.win():
        break

    # Player 2
    print("\nPlayer ", player2.get_player_num(), " move:\n")
    player2_move = player2.getFittest()

    player2_x, player2_y = player2_move.get_coordinates()
    tabuleiro.player_move(player2.get_player_num(), player2_x, player2_y)

    print(tabuleiro)
    time.sleep(3)

    if player2_move.get_is_sandwich():
        remove_x, remove_y = player2_move.get_sandwiched_enemy()
        tabuleiro.remove_piece_at(remove_x, remove_y)
        player1.add_invalid_pos(remove_x, remove_y)
        print("\nPlayer ", player2.get_player_num(), " sanduichou o ", player1.get_player_num(), ":\n")
        print(tabuleiro)
        time.sleep(3)

    if tabuleiro.win():
        break