import copy

from character import *
from ability import *

#knight class
class Knight(Character):
    def __init__(self, x, y, name, max_hp, strength, abilities:list):
        super().__init__(x, y, name, max_hp, strength)
        self.abilities = copy.copy(abilities)

    def draw_abilities(self):
        for ability in self.abilities:
            ability.draw()
