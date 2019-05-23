###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
from board import Board
import numpy as np
import play

class TestMinimax(unittest.TestCase):

    def test_minimax_defensive(self):
        game_play = Board(3)
        game_state = [
            ['O','O',' '],
            [' ',' ','X'],
            [' ','X','O']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_minimax_for_win(self):
        game_play = Board(3)
        game_state = [
            ['X',' ',' '],
            ['X',' ','O'],
            [' ',' ','O']
        ]
        game_play.set_state(game_state)
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_minimax_for_diag_win(self):
        game_play = Board(3)
        game_state = [
            [' ',' ','O'],
            ['O','X','X'],
            [' ',' ','X']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(0, suggested_move[1])
    
    def test_minimax_for_win4(self):
        game_play = Board(4)
        game_state = [
            ['X','O',' ','X'],
            [' ','O',' ',' '],
            [' ','X',' ','O'],
            ['O',' ',' ','X']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_minimax_end_case01(self):
        game_play = Board(3)
        # one case that was incorrect
        game_play.set_state([
            ['X','O','X'],
            [' ','O',' '],
            ['O','X','X']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_minimax_end_case02(self):
        game_play = Board(3)

        # second case that was incorrect
        game_play.set_state([
            ['O','O','X'],
            ['X','X','O'],
            [' ',' ','O']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(0, suggested_move[1])

    def test_minimax_end_case03(self):
        game_play = Board(3)

        # third case that was incorrect
        game_play.set_state([
            ['O',' ','X'],
            ['X','O','O'],
            ['X',' ','X']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(1, suggested_move[1])

    def test_minimax_chose_win_over_defend02(self):
        game_play = Board(3)

        # fourth case that was incorrect - computer should go for win here !
        game_play.set_state([
            ['O',' ','O'],
            [' ','X','X'],
            [' ',' ','O']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(0, suggested_move[1])

    def test_minimax_chose_win_over_defend03(self):
        game_play = Board(3)

        # fourth case that was incorrect - computer should go for win here !
        game_play.set_state([
            ['O','X','O'],
            ['O','X','X'],
            [' ',' ','O']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(1, suggested_move[1])

    def test_minimax_chose_win_over_defend01(self):
        game_play = Board(3)

        # third case that was incorrect
        game_play.set_state([
            ['O',' ','O'],
            ['X',' ','O'],
            [' ','X','X']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(0, suggested_move[1])

class TestNegamax(unittest.TestCase):
    def test_negamax_defensive(self):
        game_play = Board(3)
        game_state = [
            ['O','O',' '],
            [' ',' ','X'],
            [' ','X','O']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_negamax_for_win(self):
        game_play = Board(3)
        game_state = [
            ['X',' ',' '],
            ['X',' ','O'],
            [' ',' ','O']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_negamax_for_diag_win(self):
        game_play = Board(3)
        game_state = [
            [' ',' ','O'],
            ['O','X','X'],
            [' ',' ','X']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(0, suggested_move[0])
        self.assertEqual(0, suggested_move[1])
    
    def test_negamax_for_win4(self):
        game_play = Board(4)
        game_state = [
            ['X','O',' ','X'],
            [' ','O',' ',' '],
            [' ','X',' ','O'],
            ['O',' ',' ','X']
        ]
        game_play.set_state(game_state)
        
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_negamax_end_case01(self):
        game_play = Board(3)
        # one case that was incorrect
        game_play.set_state([
            ['X','O','X'],
            [' ','O',' '],
            ['O','X','X']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(2, suggested_move[1])

    def test_negamax_end_case02(self):
        game_play = Board(3)

        # second case that was incorrect
        game_play.set_state([
            ['O','O','X'],
            ['X','X','O'],
            [' ',' ','O']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(0, suggested_move[1])

    def test_negamax_end_case03(self):
        game_play = Board(3)

        # third case that was incorrect
        game_play.set_state([
            ['O',' ','X'],
            ['X','O','O'],
            ['X',' ','X']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(1, suggested_move[1])

    def test_negamax_chose_win_over_defend02(self):
        game_play = Board(3)

        # fourth case that was incorrect - computer should go for win here !
        game_play.set_state([
            ['O',' ','O'],
            [' ','X','X'],
            [' ',' ','O']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(1, suggested_move[0])
        self.assertEqual(0, suggested_move[1])

    def test_negamax_chose_win_over_defend03(self):
        game_play = Board(3)

        # fourth case that was incorrect - computer should go for win here !
        game_play.set_state([
            ['O','X','O'],
            ['O','X','X'],
            [' ',' ','O']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(1, suggested_move[1])

    def test_negamax_chose_win_over_defend03(self):
        game_play = Board(3)

        # fourth case that was incorrect - computer should go for win here !
        game_play.set_state([
            ['O','X','O'],
            ['O','X','X'],
            [' ',' ','O']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(1, suggested_move[1])

    def test_negamax_chose_win_over_defend01(self):
        game_play = Board(3)

        # third case that was incorrect
        game_play.set_state([
            ['O',' ','O'],
            ['X',' ','O'],
            [' ','X','X']
        ])
        suggested_move = play.negamax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(0, suggested_move[1])
                