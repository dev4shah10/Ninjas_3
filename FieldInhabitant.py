# Author: Shucheera
class FieldInhabitant:
    def __init__(self, symbol):
        self._symbolOfInhabitant = symbol  # Using an underscore to indicate it's a "protected" variable

    # Getter function for symbol
    def get_symbol(self):
        return self._symbolOfInhabitant

    # Setter function for symbol
    def set_symbol(self, symbol):
        self._symbolOfInhabitant = symbol
