# Author: Daksh Pruthi, Dev Shah, Shucheera Prasad
# Date: 11/25/2023
# Description: This module defines the GameEngine class, which manages the logic and functionality of the Captain Veggie game. The class handles initialization, player movements,
# vegetable harvesting, rabbit movements, scoring, game over conditions, and high score management.

import os
import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie

class GameEngine:
    __NUMBEROFVEGGIES = 30 
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.field = []
        self.rabbits = []
        self.captain = None
        self.vegetables = []
        self.score = 0

    def initVeggies(self):
        filename = input("Please enter the name of the vegetable file: ")
        while not os.path.exists(filename):
            filename = input("That file does not exist! Please enter the file name again: ")

        with open(filename, "r") as file1:
            filedata = []
            for line in file1:
                filedata.append(line.strip())

            f = filedata[0].split(",")

            for x in range(0, int(f[1])):
                col = []
                for y in range(0, int(f[2])):
                    col.append(None)
                self.field.append(col)

            for j in range(0, len(filedata)):
                if j == 0:
                    continue
                else:
                    g = filedata[j].split(",")
                    name = g[0]
                    symbol = g[1]
                    vegPoints = g[2]
                    v = Veggie(name, symbol, vegPoints)
                    self.vegetables.append(v)

            for k in range(0, self.__NUMBEROFVEGGIES):
                # randomveggie variable is used to store an index randomly from the veggie objects' list.
                randomveggie = random.randint(0, len(self.vegetables) - 1)
                # Next 2 variables are used to get a random x and y co-ordinated location on the field.
                tryX = random.randint(0, len(self.field) - 1)
                tryY = random.randint(0, len(self.field[0]) - 1)
                while self.field[tryX][tryY] != None:
                    tryX = random.randint(0, len(self.field) - 1)
                    tryY = random.randint(0, len(self.field[0]) - 1)
                self.field[tryX][tryY] = self.vegetables[randomveggie]
    
    def initCaptain(self):
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.captain = Captain(x, y)
                self.field[x][y] = self.captain
                break

    def initRabbits(self):
        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self.rabbits.append(rabbit)
                    self.field[x][y] = rabbit
                    break
    
    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
    
    def remainingVeggies(self):
        count = 0
        for row in self.field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):

        print("Welcome to the Vegetable Harvest Game!")
        print("Premise:")
        print("You are Captain Veggie, on a mission to harvest as many delicious vegetables as possible.")
        print("Avoid the rabbits and navigate through the field to collect veggies.")
        print("Goal:")
        print("Harvest as many vegetables as you can to maximize your score.")
        print("Symbols:")
        print(f"Captain Veggie: {self.captain.get_symbol()}")
        print(f"Rabbit: {self.rabbits[0].get_symbol()}")
        print("Vegetables:")
        for veggie in self.vegetables:
            print(f"Symbol: {veggie.get_symbol()}, Name: {veggie._name}, Points: {veggie.getpoints()}")
    
    def printField(self):
        print("Field:")
        print("+" + "-" * 21 + "+")
        for row in self.field:
            print("|", end=' ')
            for item in row:
                if item is not None:
                    print(item.get_symbol(), end=' ')
                else:
                    print(' ', end=' ')
            print("|")
        print("+" + "-" * 21 + "+")

    def getScore(self):
        return self.score

    def moveRabbits(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
        for rabbit in self.rabbits:
            x, y = rabbit.get_x(), rabbit.get_y()
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            # Check if new position is within the field boundaries
            if not (0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0])):
                continue  # Rabbit forfeits its move
            
            if self.field[new_x][new_y] is None:
                self.field[x][y], self.field[new_x][new_y] = None, rabbit
                rabbit.set_x(new_x)
                rabbit.set_y(new_y)

            target = self.field[new_x][new_y]

            # Check if the new position is occupied by Rabbit or Captain
            if isinstance(target, Rabbit) or isinstance(target, Captain):
                continue  # Rabbit forfeits its move

            # If the new position has a Veggie, remove the Veggie
            if isinstance(target, Veggie):
                # self.vegetables.remove(target)
                # Update the field: set the previous location to None, move the rabbit
                self.field[x][y] = None
                self.field[new_x][new_y] = rabbit
                # Update the rabbit's position
                rabbit.set_x(new_x)
                rabbit.set_y(new_y)

    def moveCptVertical(self, vertimovement):

        moved = 0
        # variable moved is a flag to know if the captain is moved to a new location
        # next 2 variables store the position of the captain before it is changed in order to set it to None later
        oldx = self.captain.get_x()
        oldy = self.captain.get_y()

        # print(oldx)

        if (self.captain.get_x()+vertimovement)==-1:
            self.captain.set_x(len(self.field))
        if (self.captain.get_x()+vertimovement)==len(self.field):
            self.captain.set_x(-1)

        # print(self.captain.get_x())

        if self.field[self.captain.get_x() + vertimovement][self.captain.get_y()] == None:


            self.field[self.captain.get_x() + vertimovement][self.captain.get_y()]=self.captain #Could have put self.captain.getsymbol(),
            # but the print function already uses it
            self.captain.set_x(self.captain.get_x() + vertimovement)
            moved = 1

        elif isinstance(self.field[self.captain.get_x() + vertimovement][self.captain.get_y()], Veggie):
            v1 = self.field[self.captain.get_x()+vertimovement][oldy]
            self.field[self.captain.get_x() + vertimovement][self.captain.get_y()] = self.captain


            print(f"Found a vegetable: {v1.getname()}!")
            self.captain.addVeggie(v1)
            self.score = int(self.score) + int(v1.getpoints())
            self.captain.set_x(self.captain.get_x() + vertimovement)

            moved = 1
        else:
            print("Please do not step on the rabbits")
        if moved == 1:
                self.field[oldx][oldy] = None

        # print("hi",self.captain.get_x())

    def moveCptHorizontal(self, movement):
        new_x=self.captain.get_x() 
        new_y=self.captain.get_y() + movement
        if(0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0])):
            if self.field[new_x][new_y]== None:
                self.field[self.captain.get_x()][self.captain.get_y()], self.field[new_x][new_y] = None, self.captain
                self.captain.set_x(new_x)
                self.captain.set_y(new_y)
            elif isinstance (self.field[new_x][new_y],Veggie):
                v1=self.field[new_x][new_y]
                self.captain.addVeggie(v1)
                self.score= self.score + int(v1.getpoints())
                print(f"Found a vegetable: {v1.getname()}! Score +{v1.getpoints()}")
                self.field[self.captain.get_x()][self.captain.get_y()] = None
                self.field[new_x][new_y] = self.captain
                self.captain.set_x(new_x)
                self.captain.set_y(new_y)
            elif isinstance(self.field[new_x][new_y], Rabbit):
                print("Please do not step on the rabbits")
        else:
            print("Invalid move. Captain cannot go outside the boundaries of the field.")
 
    def moveCaptain(self):
        direction = input("Enter the direction to move Captain (W/A/S/D): ").lower()
        if direction == 'w':
            self.moveCptVertical(-1)
        elif direction == 's':
            self.moveCptVertical(1)
        elif direction == 'a':
            self.moveCptHorizontal(-1)
        elif direction == 'd':
            self.moveCptHorizontal(1)
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    def gameOver(self):
        print("The game is over")
        list1= self.captain.getcollectedVeggie()
        list2=[]
        for x in range(len(list1)):

           list2.append(list1[x].getname())
        print(f"The list of all the harvested vegetables are : {list2}")
        print(f"The total score is : {self.score}")
    def highscore(self):

        listofhighs = []
        if os.path.exists("highscore.data"):
            inFile = open("highscore.data", "rb")
            listofhighs = pickle.load(inFile)
            inFile.close()
        x = input("Enter your initials")
        inital = x[:3]

        if len(listofhighs) == 0:
            tuple1 = (inital, self.score)
            listofhighs.append(tuple1)
        else:
            tuple1 = (inital, self.score)
            listofhighs.append(tuple1)
            # descending order
            for x in range(len(listofhighs)):
                if tuple1[1] > listofhighs[x][1]:
                    listofhighs.insert(x, tuple1)
                    listofhighs.pop()
                    break

        print("The highscore are:\n")
        for x in range(len(listofhighs)):
            print(f"{listofhighs[x][0]} : {listofhighs[x][1]}")
        inFile = open("highscore.data", "wb")
        pickle.dump(listofhighs, inFile)
        inFile.close()