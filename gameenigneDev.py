

import os
import random
from Veggie import Veggie
from Captain import Captain


class GameEngine:

    vertimovment=1
    NUMBEROFVEGGIES = 30

    def initVeggies(self):

        filename = input("Please enter the name of the vegetable file: ")
        # The following 2 lines are for getting a new file name in case the previous one does not exist
        while not os.path.exists(filename):
            filename = input("That file does not exist! Please enter the file name again: ")

        with open(filename, "r") as file1:
            # Although named region, it stores all the data from the file, as a list.
            filedata = []
            # the lines are stripped with trailing white spaces and appended to the filedata list
            for line in file1:
                filedata.append(line.rstrip())

        # f is a list storing split elements of filedata's first line in order to use it for creating a field.
        f = filedata[0].split(",")
        # The following code creates a 2D list representing the feild which will be used later.
        feild = []
        for x in range(0, int(f[1])):
            col = []
            for y in range(0, int(f[2])):
                col.append(None)
            feild.append(col)

        # The following block of code creates a list of objects for all vegetables mentioned in file
        # using the Veggie constructor.
        veggieObjectslist = []
        for j in range(0, len(filedata)):
            if j == 0:
                continue
            else:
                g = filedata[j].split(",")
                name = g[0]
                symbol = g[1]
                vegPoints = g[2]
                v = Veggie(name, symbol, vegPoints)
                veggieObjectslist.append(v)

        # The next block will add in the field random vegetables to random locations till count of 30.

        for k in range(0,NUMBEROFVEGGIES):
            # randomveggie variable is used to store an index randomly from the veggie objects' list.
            randomveggie = random.randint(0, len(veggieObjectslist) - 1)
            # The veggieSym variable gets the symbol of the selected object
            # veggieSym=veggieObjectslist[randomveggie].getsymbol()
            # Next 2 variables are used to get a random x and y co-ordinated location on the field.
            tryX = random.randint(0, len(feild) - 1)
            tryY = random.randint(0, len(feild[0]) - 1)
            while feild[tryX][tryY] != None:
                tryX = random.randint(0, len(feild) - 1)
                tryY = random.randint(0, len(feild[0]) - 1)
            feild[tryX][tryY] = veggieObjectslist[randomveggie]

        # return feild
    #     # For testing, To see the field:
    #     for x in range(len(feild)):
    #         print(feild[x])
    #     print()
    #     print("\n\n", veggieObjectslist)
    #
    # initVeggies()

    # def initializeGame():
    #     initVeggies()
    #     initCaptain()
    #     initRabbits()

    # captain object and veggie object- defining here for testing in next function
    # c1=Captain(4,3)
    # v2=Veggie()
    # def moveCptVertical(self,int(vertimovement)):
    #    #how to get field here?
    #     if feild[c1.getx()+vertimovement][c1.gety()]==None:
    #
    #         c1.setx(c1.getx()+vertimovement)
    # # Assign the Captain object to the new location in the field
    #
    #     elif isinstance (feild[c1.getx()+vertimovement][c1.gety()],Veggie)
    #       c1.setx(c1.getx()+vertimovement)
    #       v1=feild[c1.getx()][c1.gety()]
    #       print(f"Found a vegetable: {v1._name}!")
    #       c1.addVeggie(v1)
    #      score= score+ v1.getpoints(self)
    # # Assign the Captain object to the new location in the field
    #           else:
    #                 print("Do not step on the rabbits")
    # # dont change the loc in any other block
    # return

    # def gameover():
    #     print("The game is over")
    # list1= c1.getcollectedVeggie()
    #     for x in range(len(list1)):
    #
    #        print(list1[x].getname)
    #        print("the total score")

    #
    # def highscore():
    #     playerinitials=[]
    #     if os.path.exists(highscore.data):
    #         inFile = open(“highscore.data”, “rb”)
    #         object = pickle.load(inFile)
    #         inFile.close()
    #     x=input("Enter your initials")
    #     inital=x[:3]
    #
    #     if object is empty
    #          tuple1=(z,score)
    #          highscore list? =object
    #           object.append(tuple1)

    #     else
    #         tuple1=(z,score)
    #         object.append(tuple1)
    #         #descending order
    #      for x in range(len(object)):
    #           if tuple1[1]>object[x][1]:
    #               object.insert(x,tuple1)
    #               object.pop()
    #               break:
    #     print("The highscore are:\n")
    #     for x in range(len(object)):
    #         print(f"object[x][0] :  object[x][1]")
    #     inFile = open(“highscore.data”, “wb”)
    #     pickle.dump(object, inFile )
    #     inFile.close()
    #


