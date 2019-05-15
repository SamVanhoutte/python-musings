###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
import board as brd
import numpy as np
import play

class TestMethods(unittest.TestCase):
    def test_horizontal_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ','O','O','O'],
                [' ',' ',' ',' '],
                [' ',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_diagonal_down_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                ['O',' ',' ',' '],
                [' ','O',' ',' '],
                [' ',' ','O',' '],
                [' ',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_diagonal_up_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ','O',' ',' '],
                ['O',' ',' ',' ']
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_vertical_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ',' ','O',' '],
                [' ',' ','O',' ']
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_empty_cells(self):
        game_play = brd.Board(2)
        game_play.set_state([
                [' ','1'],
                ['1',' ']
            ])
        self.assertEquals([[0,0],[1,1]], game_play.get_empty_cells())

    def test_game_finished_score(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [' ',' ',' ',' '],
                [' ',' ','O',' '],
                [' ','O',' ',' '],
                ['O',' ',' ',' ']
            ])
        game_over, score = game_play.check_game_finished(True)
        self.assertEqual(True, game_over)
        self.assertLess(score, 0)  

    def test_diagonals(self):
        game_play = brd.Board(4)
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

    def test_minimax_defensive(self):
        game_play = brd.Board(3)
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
        game_play = brd.Board(3)
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
        game_play = brd.Board(3)
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
        game_play = brd.Board(4)
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
        game_play = brd.Board(3)
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
        game_play = brd.Board(3)

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
        game_play = brd.Board(3)

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
        game_play = brd.Board(3)

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
        game_play = brd.Board(3)

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
        game_play = brd.Board(3)

        # third case that was incorrect
        game_play.set_state([
            ['O',' ','O'],
            ['X',' ','O'],
            [' ','X','X']
        ])
        suggested_move = play.minimax(game_play, len(game_play.get_empty_cells()), False)
        self.assertEqual(2, suggested_move[0])
        self.assertEqual(0, suggested_move[1])
        

def main():
    game_play = brd.Board(4)
    # game_state = [
    #         [0,0,0,0],
    #         [1,1,0,1],
    #         [0,0,1,0],
    #         [0,0,1,1],
    #     ]
    # game_play.set_state(game_state)
    print(game_play.get_diagonal_range(0, 0, True))
    print(game_play.get_diagonal_range(0, 1, True))
    print(game_play.get_diagonal_range(3, 0, False))
    print(game_play.get_diagonal_range(2, 0, False))
    print('test running !!!! ')
    #check_array = [1,0,1]
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    # nums = game_state[1]
    # for i in range(len(nums)-2):
    #     if nums[i]==1 and nums[i+1]==1 and nums[i+2]==1:
    #         print('Found !!!')
    #print(set(check_array) & set(game_state[1]) == set(check_array))
    print('Won??',game_play.someone_won(True))
    

if __name__ == "__main__": main()