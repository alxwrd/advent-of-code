
import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_cycle(self):
        bank = solutions.MemoryBanks("0\t2\t7\t0")

        bank.cycle()

        self.assertEqual(bank.banks, [2, 4, 1, 2])


    def test_redistribute(self):
        bank = solutions.MemoryBanks("0\t2\t7\t0")

        bank.redistibute()

        self.assertEqual(bank.operations, 5)


    def test_puzzle_redistibute(self):
        bank = solutions.MemoryBanks(solutions.PUZZLE_INPUT)

        bank.redistibute()

        self.assertEqual(bank.operations, 7864)


    def test_loop_szie(self):
        bank = solutions.MemoryBanks("0\t2\t7\t0")

        bank.redistibute()

        self.assertEqual(bank.loop_size(), 4)


    def test_puzzle_loop_szie(self):
        bank = solutions.MemoryBanks(solutions.PUZZLE_INPUT)

        bank.redistibute()

        self.assertEqual(bank.loop_size(), 1695)