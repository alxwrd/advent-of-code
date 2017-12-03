import itertools
import os

import math


PUZZLE_INPUT = 347991


def locate_number(num):
    """For a given number, locate it's x, y co-ordinate in an infinite spiral

    Example:
         5   4   3
         6   1   2
         7   8   9
        >>>locate_number(2)
        (1, 0)
        >>>locate_number(9)
        (1, 1)

    NOTE: Based on answers found:
        - https://math.stackexchange.com/questions/1263541/
        - https://stackoverflow.com/questions/11550153/
    """

    if num == 1:
        return (0, 0)

    cycle = lambda num: math.floor((math.sqrt(num-1) + 1) / 2)
    first = lambda c: (2*c -1)**2 + 1
    length = lambda c: 8 * c
    sector = lambda num: math.floor(4 * (num - first(cycle(num))) / length(cycle(num)))

    def position(index):
        c = cycle(index)
        s = sector(index)
        offset = index - first(c) - s * length(c) // 4
        if s == 1: #north
            return c - offset - 1, -c
        if s == 0: #east
            return c, c - offset - 1
        if s == 3: #south
            return -c + offset + 1, c
        # else, west
        return -c, -c + offset + 1
    return position(num)


def find_manhattan_distance(start, end=(0, 0)):
    """Find the shortest distance using left, right, up, and down to `end`
    """
    return sum(abs(e - s) for e, s in zip(start, end))
