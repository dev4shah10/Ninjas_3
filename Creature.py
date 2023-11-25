# Assuming FieldInhabitant class is defined in FieldInhabitant.py
from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        # Call the constructor of the superclass (FieldInhabitant)
        super().__init__(symbol)
        
        # Assign x and y coordinate values to new member variables
        self._x = x
        self._y = y

    # Getter function for x coordinate
    def get_x(self):
        return self._x

    # Setter function for x coordinate
    def set_x(self, x):
        self._x = x

    # Getter function for y coordinate
    def get_y(self):
        return self._y

    # Setter function for y coordinate
    def set_y(self, y):
        self._y = y
