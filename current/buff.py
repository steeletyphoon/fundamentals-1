"""Buffs and debuffs"""

class Buff():

    def __init__(self,affects=None,duration="turn",amount=0,percent=0):
        self.affects = affects
        self.duration = duration
        self.amount = amount
        self.percent = percent

if __name__ == "__main__":
    import colors as c
    print(c.clear)
    buffy = Buff()
    print(("affects: {s.affects}, " + 
          "duration: {s.duration}, " + 
          "amount: {s.amount}, " +
          "percent {s.percent}")
          .format(s=buffy))

