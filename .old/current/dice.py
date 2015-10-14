"""A simple dice rolling module.
"""

import random

def roll(howmany=1,sides=6):
    """Returns the result from rolling `howmany` of `sides`-sided dice"""
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
    return total

def parse(text):
    """Parses traditional dice notation (ex: 3d6)"""
    (howmany, sides) = text.split('d')
    return (int(howmany), int(sides))
    
def parse_roll(text):
    """Parses traditional dice notation and then rolls (ex: 3d6)"""
    (howmany, sides) = parse(text)
    return roll(howmany,sides)

if __name__ == '__main__':
    import colors as c

    def test_roll(sides):
        print(c.yellow + 'roll(1,{}):'.format(sides) + c.reset)
        for count in range(20):
            foo = roll(1,sides)
            print(c.random_color() + str(foo) + c.reset,end=' ')
        print()
        print()

    print(c.clear)

    test_roll(6)
    test_roll(20)
    test_roll(100)

    print(c.yellow + 'roll():' + c.reset)
    for count in range(20):
        foo = roll()
        print(c.random_color() + str(foo) + c.reset,end=' ')
    print()
    print()

    for text in ['2d6','4d6','1d20','2d100']:
        print("parse({})".format(text))
        print(parse(text))
        print("parse_roll({})".format(text))
        print(parse_roll(text))

