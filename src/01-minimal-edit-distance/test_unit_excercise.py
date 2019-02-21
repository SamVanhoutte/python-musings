import unittest                     # unit testing ftw
from excercise import Excercise     # importing the actual code

class TestMethods(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(0, Excercise.CalculateEditDistance('', ''))
        self.assertEqual(0, Excercise.CalculateEditDistance('AB', 'AB'))

    def test_empty_strings(self):
        self.assertEqual(2, Excercise.CalculateEditDistance('AB', ''))
        self.assertEqual(2, Excercise.CalculateEditDistance('', 'AB'))

    def test_small_strings(self):
        self.assertEqual(1, Excercise.CalculateEditDistance('ME', 'MY'))
        self.assertEqual(1, Excercise.CalculateEditDistance('aunt', 'ant'))
        self.assertEqual(1, Excercise.CalculateEditDistance('cat', 'cut'))
        self.assertEqual(2, Excercise.CalculateEditDistance('cat', 'cuta'))

    def test_addition_only(self):
        self.assertEqual(3, Excercise.CalculateEditDistance('Sam', 'Samuel'))

    def test_complex_string(self):
        self.assertEqual(3, Excercise.CalculateEditDistance('Saturday', 'Sunday'))

    def test_ignore_casing(self):
        self.assertEqual(3, Excercise.CalculateEditDistance('SATURDay', 'Sunday', True))
        self.assertEqual(0, Excercise.CalculateEditDistance('ab', 'AB', True))

    def test_default_casing(self):
        self.assertNotEqual(3, Excercise.CalculateEditDistance('SATURDay', 'Sunday'))
        self.assertNotEqual(0, Excercise.CalculateEditDistance('ab', 'AB'))

