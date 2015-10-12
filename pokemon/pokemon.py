"""Pokemon Class/Interface"""

class Pokemon():
    level = 1 
    xp = 0 
    height = 0
    weight = 0
    speed = 0
    hp = 0
    attack = 0
    special_attack = 0
    defense = 0
    special_defense = 0
    type1 = ""
    type2 = ""
    usable_moves = []
    moves = []

    def choose_move(self,move):
        if move in usable_moves:
            self.move = move

    def attack(self,target):
        """Resolve each attack exactly as done in game"""
        # TODO apply stats changes
        A = target.level
        B = self.attack
        D = target.defense
        if self.move.is_special:
            B = self.special_attack 
            D = self.special_defense 
        C = self.move.power
        X = 1
        if self.move.type in [self.type1,self.type2]:
            X = 1.5
        # TODO resolve Y
        # ((2A/5+2)*B*C)/D)/50)+2)*X)*Y)*Z)/255


class Espeon(Pokemon):
    height = 0.89
    weight = 26.5
    speed = 110
    hp = 65
    attack = 65
    special_attack = 130
    defense = 60
    special_defense = 95
    type1 = "Psychic"
    usable_moves = ["HelpingHand","TailWhip","Tackle"]

class Lucario(Pokemon):
    height = 1.19
    weight = 54
    speed = 90
    hp = 70
    attack = 110
    special_attack = 115
    defense = 70
    special_defense = 70
    type1 = "Fighting"
    type2 = "Steel"
    usable_moves = ["MetalClaw","AuraSphere","DragonPulse","ExtemeSpeed","Foresight","Detect","QuickAttack","CloseCombat"]
