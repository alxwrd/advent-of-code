import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_parse_input(self):
        spreadsheet_tabs = ("5\t1\t9\t5\n"
                            "7\t5\t3\n"
                            "2\t4\t6\t8")

        spreadsheet_spaces = ("5 1 9 5\n"
                              "7 5 3\n"
                              "2 4 6 8")
        self.assertEqual(
            list(solutions.parse_input(spreadsheet_tabs)),
            list(solutions.parse_input(spreadsheet_spaces))
            )


    def test_day_02_puzzle_1(self):
        spreadsheet = ("5 1 9 5\n"
                       "7 5 3\n"
                       "2 4 6 8")
        self.assertEqual(solutions.checksum_1(spreadsheet), 18)
        self.assertEqual(solutions.checksum_1(solutions.PUZZLE_INPUT), 44670)


    def test_day_02_puzzle_2(self):
        spreadsheet = ("5 9 2 8\n"
                       "9 4 7 3\n"
                       "3 8 6 5")
        self.assertEqual(solutions.checksum_2(spreadsheet), 9)
        self.assertEqual(solutions.checksum_2(solutions.PUZZLE_INPUT), 285)
