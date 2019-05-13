###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the graph algorithms
###############################################

import unittest                     # unit testing ftw
import board as brd
import numpy as np
class TestMethods(unittest.TestCase):
    def test_horizontal_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [0,0,0,0],
                [0,1,1,1],
                [0,0,0,0],
                [0,0,0,0],
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_diagonal_down_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,0],
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_diagonal_up_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [0,0,0,0],
                [0,0,1,0],
                [0,1,0,0],
                [1,0,0,0],
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_vertical_win(self):
        game_play = brd.Board(4)
        game_play.set_state([
                [0,0,0,0],
                [0,0,1,0],
                [0,0,1,0],
                [0,0,1,0],
            ])
        self.assertEqual(True, game_play.someone_won(True))

    def test_diagonals(self):
            game_play = brd.Board(4)
            game_state = [
                [0,0,0,0],
                [1,1,0,1],
                [0,0,1,0],
                [0,0,1,1],
            ]
            game_play.set_state(game_state)
            self.assertEquals([0, 1, 1, 1], game_play.get_diagonal_range(0, 0, True))
            self.assertEquals([0, 0, 0], game_play.get_diagonal_range(0, 1, True))
            self.assertEquals([0, 0, 0, 0], game_play.get_diagonal_range(3, 0, False))
            self.assertEquals([0, 1, 0], game_play.get_diagonal_range(2, 0, False))

def main():
    game_play = brd.Board(4)
    game_state = [
            [0,0,0,0],
            [1,1,0,1],
            [0,0,1,0],
            [0,0,1,1],
        ]
    game_play.set_state(game_state)
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