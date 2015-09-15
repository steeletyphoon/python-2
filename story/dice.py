"""A simple dice rolling module.
"""

import random

def roll(howmany=1,sides=6):
    """Returns the result from rolling 'howmany' 'sides'-sided dice."""
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
    return total

def parse(text):
    """Parses traditional dice notation (ex: 3d6)"""
    (howmany, sides) = text.split('d')
    return (int(howmany), int(sides))

def parse_roll(text):
    """Parse traditional dice notation and then rolls (ex: 3d6)"""
    howmany, sides = parse(text)
    return roll(howmany, sides)


if __name__ == '__main__':
    print(parse_roll('2d6'))
