from puzzle import Puzzle
import unittest   
import puzzle as pz
import numpy as np

class TestMethods(unittest.TestCase):
    def test_constructor(self):
        puzz = Puzzle()
        self.assertIsNotNone(puzz.get_open_cell())

    def test_open_cell(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 0, 8]])
        self.assertEqual((2,1), puzz.get_open_cell())

    def test_available_moves_side(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 0, 8]])
        self.assertEqual(3, len(puzz.get_available_moves()))

    def test_available_moves_center(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [7, 0, 5],
                        [6, 4, 8]])
        self.assertEqual(4, len(puzz.get_available_moves()))

    def test_completed(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 0, 5],
                        [6, 7, 8]])
        self.assertEqual(True, puzz.completed())

    def test_available_moves_corner(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual(2, len(puzz.get_available_moves()))

    def test_do_move(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        puzz.move_cell(1, 2)
        self.assertEqual(puzz.board, 
                        [[1, 2, 3],
                        [4, 7, 0],
                        [6, 8, 5]])

    def test_signature(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual('12347568 :0', puzz.get_signature())
        
    def test_manhattan_distance(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual(2, puzz.evaluate('fair'))
        puzz = Puzzle(' 13425678')
        self.assertEqual(2, puzz.evaluate('fair'))

    
    def test_hamming_distance(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual(3, puzz.evaluate('weak'))

    def test_opposities_complete(self):
        puzz = Puzzle('1234 5678')
        self.assertEqual(0, puzz.evaluate('bad'))

    def test_opposities_incomplete(self):
        puzz = Puzzle('1234756 8')
        self.assertEqual(3, puzz.evaluate('bad'))

    def test_nilsson_sequence(self):
        puzz = Puzzle(' 13425678')
        self.assertEqual(17, puzz.evaluate('good'))

    def test_signature_constructor(self):
        puzz = Puzzle('1234 5678')
        self.assertEqual(True, puzz.completed())