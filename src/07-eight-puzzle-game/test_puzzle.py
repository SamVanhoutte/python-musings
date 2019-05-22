from jigsaw import JigsawPlay
import unittest   
import puzzle as pz
import numpy as np

class TestMethods(unittest.TestCase):
    def test_constructor(self):
        puzz = pz.puzzle()
        self.assertIsNotNone(puzz.get_open_cell())

    def test_open_cell(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 0, 8]])
        self.assertEqual((2,1), puzz.get_open_cell())

    def test_available_moves_side(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 0, 8]])
        self.assertEqual(3, len(puzz.get_available_moves()))

    def test_available_moves_center(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [7, 0, 5],
                        [6, 4, 8]])
        self.assertEqual(4, len(puzz.get_available_moves()))

    def test_completed(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 0, 5],
                        [6, 7, 8]])
        self.assertEqual(True, puzz.completed())

    def test_available_moves_corner(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual(2, len(puzz.get_available_moves()))

    def test_do_move(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        puzz.move_cell(1, 2)
        self.assertEqual(puzz.board, 
                        [[1, 2, 3],
                        [4, 7, 0],
                        [6, 8, 5]])

    def test_signature(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        self.assertEqual('1-2-3-4-7-5-6-8-0-', puzz.get_signature())
        
    def test_solve_easy(self):
        puzz = pz.puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        jigsaw = JigsawPlay(puzz)
        jigsaw.solve()