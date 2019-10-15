###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
from board import Board
import numpy as np
import play

class TestMethods(unittest.TestCase):
    def test_horizontal_win(self):
        game_play = Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ','O','O','O'],
                [' ',' ',' ',' '],
                [' ',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.player_won())

    def test_diagonal_down_win(self):
        game_play = Board(4)
        game_play.set_state([
                ['O',' ',' ',' '],
                [' ','O',' ',' '],
                [' ',' ','O',' '],
                [' ',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.player_won())

    def test_diagonal_up_win(self):
        game_play = Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ','O',' ',' '],
                ['O',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.player_won())

    def test_vertical_win(self):
        game_play = Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ',' ','O',' '],
                [' ',' ','O',' ']
            ])
        self.assertEqual(True, game_play.player_won())

    def test_empty_cells(self):
        game_play = Board(2)
        game_play.set_state([
                [' ','1'],
                ['1',' ']
            ])
        self.assertEquals([[0,0],[1,1]], game_play.get_empty_cells())

    def test_game_finished_score(self):
        game_play = Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ','O',' ',' '],
                ['O',' ',' ',' ']
            ])
        game_over, score = game_play.check_game_finished(True)
        self.assertEqual(True, game_over)
        self.assertLess(score, 0)  

    def test_game_finished_score_case01(self):
        game_play = Board(3)
        game_play.set_state([
                ['X','O','X'],
                ['O','O','X'],
                ['O','X','X']
                ])
        game_over, score = game_play.check_game_finished(True)
        self.assertEqual(True, game_over)
        self.assertGreater(score, 0)  


    def test_diagonals(self):
        game_play = Board(4)
        game_state = [
                [' ',' ',' ',' '],
                ['O','O',' ','O'],
                [' ',' ','O',' '],
                [' ',' ','O','O']
        ]
        game_play.set_state(game_state)
        self.assertEquals([' ', 'O', 'O', 'O'], game_play.get_diagonal_range(0, 0, True))
        self.assertEquals([' ',' ',' '], game_play.get_diagonal_range(0, 1, True))
        self.assertEquals([' ',' ',' ', ' '], game_play.get_diagonal_range(3, 0, False))
        self.assertEquals([' ','O',' '], game_play.get_diagonal_range(2, 0, False))

