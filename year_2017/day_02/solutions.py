import itertools
import os

with open(os.path.dirname(__file__) + "/input", "r") as f_:
    PUZZLE_INPUT = f_.read()


def parse_input(spreadsheet):
    """For a 'spreadsheet' of the following layout

    5 1 9 5
    7 5 3
    2 4 6 81

    return a generator of lists of ints
    """
    #Turn the sheet into a generator of lists of numbers
    sheet = ([int(cell.strip()) for cell in row.split()]
             for row in spreadsheet.splitlines())
    return sheet


def checksum_1(puzzle_input):
    """For each row, determine the difference between the largest value and
        the smallest value; the checksum is the sum of all of
        these differences.
    """
    return sum(max(row) - min(row) for row in parse_input(puzzle_input))


def checksum_2(puzzle_input):
    """For each row, find the two numbers that cleanly divide.
        The checksum is the sum of division results.
    """
    spreadsheet = parse_input(puzzle_input)

    return sum(a // b for row in spreadsheet
               for a, b in
               (sorted(combo, reverse=True)
                for combo in itertools.combinations(row, 2))
               if a % b == 0)
