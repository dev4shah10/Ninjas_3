# Author: Daksh Pruthi
# Date: 11/25/2023
# Description: This module defines the Rabbit class, a subclass of Creature, representing rabbits in the Captain Veggie game.

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")