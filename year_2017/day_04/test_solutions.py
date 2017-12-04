import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_has_no_duplicates(self):
        self.assertEqual(solutions.has_no_duplicates(["aa", "bb", "cc"]), True)
        self.assertEqual(solutions.has_no_duplicates(["aa", "bb", "bb"]), False)
        self.assertEqual(solutions.has_no_duplicates(["aa", "bb", "aaa"]), True)


    def test_count(self):
        test_string = "aaabc"
        self.assertEqual(solutions.count(test_string), 5)
        self.assertEqual(solutions.count(test_string, condition=lambda x: x == "a"), 3)

        test_list = ["a", "a", "a", "b", "c"]
        self.assertEqual(solutions.count(test_list), 5)
        self.assertEqual(solutions.count(test_list, condition=lambda x: x == "a"), 3)


    def test_count_valid_passphrases(self):
        test_data = ("aa bb cc dd ee\n"
                     "aa bb cc dd aa\n"
                     "aa bb cc dd aaa\n")

        self.assertEqual(solutions.count_valid_passphrases(test_data), 2)
        self.assertEqual(solutions.count_valid_passphrases(solutions.PUZZLE_INPUT), 477)


    def test_count_valid_passphrases_including_anagrams(self):
        test_data = ("abcde fghij\n"
                     "abcde xyz ecdab\n"
                     "a ab abc abd abf abj\n")
        puzzle_input = solutions.PUZZLE_INPUT

        self.assertEqual(solutions.count_valid_passphrases(test_data, anagrams=True), 2)
        self.assertEqual(solutions.count_valid_passphrases(puzzle_input, anagrams=True), 167)
