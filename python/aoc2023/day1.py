"""
Day 1: Trebuchet?!
"""

import copy

from .utils import read_fixture


def translate_word_digits(line: str) -> str:
    """
    Translates occurrences of 1-9 in words to the actual digits. This performs a forward lookup that allows for certain
    overlapping letters in these words to also be parsed in their own context.

    Args:
        line (str): Line of text to search for.

    Returns:
        str: The input string with "digit" words replaced by the digits themselves.
    """
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    line_clone = copy.copy(line)
    for index, char in enumerate(line):
        for word, digit in digits.items():
            if word.startswith(char):
                look_ahead = len(word)
                if line[index : index + look_ahead] == word:
                    line_clone = line_clone[:index] + digit + line_clone[index + 1 :]
    return line_clone


def find_calibration_value(line: str) -> int:
    """
    Find the "calibration" value by taking essentially 10 x the first digit of a string plus the last digit of that
    string. If there's one digit, that one digit is considered the first *and* last.

    Args:
        line (str): Line of text to search for.

    Returns:
        int: The "calibration value" according to the rules above.
    """
    digits = list(filter(str.isdigit, line))
    first = digits[0]
    last = digits[-1]
    result = int(f"{first}{last}")
    return result


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: Solution for the first star.
    """
    total = 0
    for line in read_fixture("actual/1.txt"):
        total += find_calibration_value(line)
    return total


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: Solution for the second star.
    """
    total = 0
    for line in read_fixture("actual/1.txt"):
        total += find_calibration_value(translate_word_digits(line))
    return total


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
