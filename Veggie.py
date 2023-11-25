# Author: Dev Shah
# Date: 11/2/23
# Description: This file contains a class Veggie to store the data and functions
# for a vegetable object and also prints its information.

from FieldInhabitant import FieldInhabitant
class Veggie(FieldInhabitant):

    def __init__(self,name,symbol,vegPoints):
        FieldInhabitant.__init__(self,symbol)
        self._name=name
        self._vegPoints=vegPoints

    def __str__(self):
        return f"The vegetable is\n{self._symbolOfInhabitant}: {self._name} - {self._vegPoints}"

    def getname(self):
        return self._name

    def getpoints(self):
        return self._vegPoints
    def setname(self,NewName):
        self._name=NewName
    def setpoints(self,NewPoints):
        self._vegPoints=NewPoints
