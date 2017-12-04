import os

with open(os.path.dirname(__file__) + "/input", "r") as f_:
    PUZZLE_INPUT = f_.read()



def has_no_duplicates(input_):
    """Check that a list contains no duplicates.

    For example:
        ['aa', 'bb', 'cc'] is valid.
        ['aa', 'bb', 'aa'] is not valid. The word aa appears more than once.
    """
    return len(input_) == len(set(input_))



def count(input_, condition=lambda x: True):
    """Count the number of items in an iterable for a given condition

    For example:
        >>>count("abc")
        3
        >>>count("abc", condition=lambda x: x=="a")
        1
    """
    return sum(condition(item) for item in input_)


def count_valid_passphrases(puzzle_input, anagrams=False):
    """Count valid passphrases from newline seperated string

    A valid passphrase must contain no duplicate words.

    With anagrams=True a passphrase must contain no two words that are
        anagrams of each other
    """
    lines = puzzle_input.splitlines()
    phrases = [line.split() for line in lines]
    if anagrams:
        phrases = [["".join(sorted(item)) for item in phrase]
                   for phrase in phrases]
    return count(phrases, condition=has_no_duplicates)
