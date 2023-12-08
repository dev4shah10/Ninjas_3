# Author: Daksh Pruthi
# Date: 12/08/2023
# Description: Snake class

from Creature import Creature

class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")