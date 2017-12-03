import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_locate_number(self):
        self.assertEqual(solutions.locate_number(1), (0, 0))
        self.assertEqual(solutions.locate_number(9), (1, 1))
        self.assertEqual(solutions.locate_number(5), (-1, -1))
        self.assertEqual(solutions.locate_number(solutions.PUZZLE_INPUT), (-185, -295))


    def test_find_manhattan_distance(self):
        self.assertEqual(solutions.find_manhattan_distance(start=(0, 0)), 0)
        self.assertEqual(solutions.find_manhattan_distance(start=(2, 1)), 3)
        self.assertEqual(solutions.find_manhattan_distance(start=(-185, -295)), 480)
