# Author: Dev Shah
# Date: 11/2/23
# Description: This file contains a class Captain. It is used to handle a
# list of the collected vegetables by the captain, also keeping the track of co-ordinate data.


from Creature import Creature

class Captain(Creature):
    def __init__(self,x,y):
        Creature.__init__(self,x,y,"V")
        self._collectedVeggie=[]

    def addVeggie(self,veggie):
        self._collectedVeggie.append(veggie)

    def getcollectedVeggie(self):
        return self._collectedVeggie

