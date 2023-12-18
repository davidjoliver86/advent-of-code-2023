"""
Day 2: Cube Conundrum
"""
import math
import operator
import re
from collections import namedtuple
from typing import Any

from . import utils

CubeSet = namedtuple("CubeSet", ("count", "color"))
Game = namedtuple("Game", ("id", "rounds"))

STANDARD_CONSTRAINT = {
    "red": (operator.le, 12),
    "green": (operator.le, 13),
    "blue": (operator.le, 14),
}


def satisfies_constraints(game: Game, constraints: dict[str, tuple[Any]]) -> bool:
    """
    Pass in a dictionary of constraint functions for each color. Return False if any round in the game violates these
    constraints.

    Args:
        game (Game): The game to examine.
        constraints (dict[str, tuple[Any]]): Dictionary of constraint functions per color.

    Returns:
        bool: Whether the game is "valid" or not.
    """
    for _round in game.rounds:
        for cubeset in _round:
            a = cubeset.count
            func, b = constraints[cubeset.color]
            if not func(a, b):
                return False
    return True


def summed_ids_of_valid_games(games_file: str, constraints: dict[str, tuple[Any]]) -> int:
    """
    For games that are considered valid (see satisfies_constraints above), sum up the IDs of those games and return
    the resulting sum.

    Args:
        games_file (str): Path to game descriptions.
        constraints (dict[str, tuple[Any]]): Dictionary of constraint functions per color.

    Returns:
        int: The sum of IDs of all valid games.
    """
    summed_ids = 0
    for game_text in utils.read_fixture(games_file):
        game = parse_game(game_text)
        if satisfies_constraints(game, constraints):
            summed_ids += game.id
    return summed_ids


def summed_power(games_file: str) -> int:
    """
    The "power" is defined as the product of the minimum number of cubes requires for each color to ensure that all
    rounds in the game are possible - hence, valid. Determine the minimum required number of cubes for each color,
    then multiply all those results together. That is each games' "power".

    Args:
        games_file (str): Path to game descriptions.

    Returns:
        int: The sum of the "power" of each game.
    """
    return sum((power(parse_game(game_text)) for game_text in utils.read_fixture(games_file)))


def power(game: Game) -> int:
    """
    Determine an individual games' "power" - that is, the product of the number of cubes of each color required to
    ensure that all rounds in the game are able to be played.

    Args:
        game (Game): The game to examine.

    Returns:
        int: The "power" of this game.
    """
    required_colors = {}
    for _round in game.rounds:
        for cubeset in _round:
            if cubeset.color not in required_colors:
                required_colors[cubeset.color] = cubeset.count
            else:
                existing = required_colors[cubeset.color]
                required_colors[cubeset.color] = max(existing, cubeset.count)
    return math.prod(required_colors.values())


def parse_game(game_line: str) -> Game:
    """
    From a line of raw text examining the game, return a tuple of its ID and the rounds within the game.

    Args:
        game_line (str): Line of raw text describing the game.

    Returns:
        Game: Standardized depiction of the game and its ID.
    """
    game_id, results = re.match(r"Game (\d+): (.*)", game_line).groups()
    round_text = results.split(";")
    rounds = [
        [CubeSet(count=int(count), color=color) for count, color in re.findall(r"(\d+) (\w+)", _round)]
        for _round in round_text
    ]
    return Game(id=int(game_id), rounds=rounds)


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The sum of the IDs of valid games in the puzzle input.
    """
    return summed_ids_of_valid_games("actual/2.txt", STANDARD_CONSTRAINT)


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: The sum of the powers
    """
    return summed_power("actual/2.txt")


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
