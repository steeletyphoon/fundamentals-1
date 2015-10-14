"""A Bunch of Monsters """

from interfaces import HasStats
import random

class Dragon(HasStats):
    title = "Dragon of the North"
    def __init__(self):
        self.set_stats()
        self.strength += 10

class Lich(HasStats):
    title = "Lich Mage"
    def __init__(self):
        self.set_stats()
        self.intelligence += 10

monsters = [
    Dragon,
    Lich
]

def pick_random():
    Monster = random.choice(monsters)
    return Monster()

if __name__ == '__main__':
    one_lich = Lich()
    print(one_lich.title)
    one_lich.show_stats()

    a_random_monster = pick_random()
    print(a_random_monster.title)
    a_random_monster.show_stats()

