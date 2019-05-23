from jigsaw import JigsawPlay
from puzzle import Puzzle
import unittest   
import puzzle as pz
import numpy as np

class TestMethods(unittest.TestCase):

    def test_solve_easy(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
                        [4, 7, 5],
                        [6, 8, 0]])
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve()
        self.assertEqual(len(steps), 3)
    
    def test_solve_good_evaluator(self):
        puzz = Puzzle('12375846 ')
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve('good')
        self.assertEqual(len(steps), 7)

    def test_solve_fair_evaluator(self):
        puzz = Puzzle('12375846 ')
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve('fair')
        self.assertEqual(len(steps), 7)

    def test_solve_weak_evaluator(self):
        puzz = Puzzle('12375846 ')
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve('weak')
        self.assertEqual(len(steps), 7)

    def test_solve_bad_evaluator(self):
        puzz = Puzzle('12375846 ')
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve('bad')
        self.assertEqual(len(steps), 7)

    def test_solve_complex(self):
        puzz = Puzzle()
        puzz.set_state([[1, 2, 3],
            [7, 5, 8],
            [4, 6, 0]])
        jigsaw = JigsawPlay(puzz)
        steps = jigsaw.solve('good')
        self.assertEqual(len(steps), 7)