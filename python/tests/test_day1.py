"""
Test cases for day 1
"""
import pytest

from aoc2023 import day1

CALIBRATION_VALUES = (
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
)

CALIBRATION_VALUES_WITH_TRANSLATION = (
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
)


@pytest.mark.parametrize(("line", "expected"), CALIBRATION_VALUES)
def test_find_calibration_value(line: str, expected: int):
    """
    Test that the calibration value works.
    """
    assert day1.find_calibration_value(line) == expected


@pytest.mark.parametrize(("line", "expected"), CALIBRATION_VALUES_WITH_TRANSLATION)
def test_find_calibration_value_with_translation(line: str, expected: int):
    """
    Test that the calibration value and translation works.
    """
    translated = day1.translate_word_digits(line)
    assert day1.find_calibration_value(translated) == expected


def test_first_star():
    """
    Assert the correct first star solution.
    """
    assert day1.first_star() == 54081


def test_second_star():
    """
    Assert the correct second star solution.
    """
    assert day1.second_star() == 54649
