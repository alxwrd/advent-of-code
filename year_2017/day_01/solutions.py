import itertools
import os

with open(os.path.dirname(__file__) + "/input", "r") as f_:
    PUZZLE_INPUT = f_.read()

def sum_matching(puzzle_input, step=1):
    """For a string of numbers, sum digits if they match the digit `step` away.

    NOTE: The calculation is circular, so the digit after the last digit is
           the first digit in the list.

    Usage:
        >>>captcha("1122")
        3
        >>>captcha("1212", step=2)
        6
    """
    #Make the string circular
    puzzle_input += puzzle_input[0:step]

    #Create two iterables from the input
    first, second = itertools.tee(puzzle_input)

    #Advance one iterable forward the number of steps
    for _ in range(step):
        next(second)

    #Sum numbers if the number matches
    return sum(int(x) for x, y in zip(first, second) if x == y)
