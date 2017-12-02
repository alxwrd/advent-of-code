import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_day_01_puzzle_1(self):
        puzzle_input = solutions.PUZZLE_INPUT
        solution = solutions.sum_matching

        self.assertEqual(solution("1122"), 3)
        self.assertEqual(solution("1111"), 4)
        self.assertEqual(solution("1234"), 0)
        self.assertEqual(solution("91212129"), 9)
        self.assertEqual(solution(puzzle_input), 1144)


    def test_day_01_puzzle_2(self):
        puzzle_input = solutions.PUZZLE_INPUT
        solution = solutions.sum_matching

        self.assertEqual(solution("1212", step=2), 6)
        self.assertEqual(solution("1221", step=2), 0)
        self.assertEqual(solution("123425", step=3), 4)
        self.assertEqual(solution("123123", step=3), 12)
        self.assertEqual(solution("12131415", step=4), 4)

        self.assertEqual(solution(puzzle_input, step=len(puzzle_input)//2), 1194)
