"""
Test cases for day 2
"""
from aoc2023 import day2


def test_summed_ids_of_valid_games():
    """
    Sample test case for the summed IDs.
    """
    assert day2.summed_ids_of_valid_games("test/2.txt", day2.STANDARD_CONSTRAINT) == 8


def test_power():
    """
    Sample test case for the powers of the example games.
    """
    assert day2.summed_power("test/2.txt") == 2286


def test_first_star():
    """
    Assert the correct first star solution.
    """
    assert day2.first_star() == 2449


def test_second_star():
    """
    Assert the correct second star solution.
    """
    assert day2.second_star() == 63981
