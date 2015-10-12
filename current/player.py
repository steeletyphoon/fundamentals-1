"""A simple Player class with stats generated on creation."""

from interfaces import HasStats,Buffs
from utils import ask

class Player(HasStats,Buffs):
    def __init__(self):
        self.set_stats()

    def pick_move(self):
        self.move = ask("What move do you want to make?")

    def move(self):
        if self.move == 'harden':
            self.buff('defense','battle',percent=25)
            

       
if __name__ == '__main__':
    import colors as c
    player = Player()
    c.clear_screen()
    player.save()
    #player.load()
    player.show_stats()
    player.pick_move()
