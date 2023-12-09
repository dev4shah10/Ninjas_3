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
from Snake import Snake

class GameEngine:
    __NUMBEROFVEGGIES = 30 
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self): #author : shucheera
        self.field = []
        self.rabbits = []
        self.captain = None
        self.vegetables = []
        self.score = 0
        self.__snake = None

    def initVeggies(self): # author: dev
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

            for k in range(0,self.__NUMBEROFVEGGIES):
                # Next 2 variables are used to get a random x and y co-ordinated location on the field.
                while True:
                    tryX = random.randint(0, len(self.field) - 1)
                    tryY = random.randint(0, len(self.field[0]) - 1)
                    if self.field[tryX][tryY] is None:
                        randomveggie = random.choice(self.vegetables)
                        self.field[tryX][tryY] = randomveggie
                        break
    
    def initCaptain(self): #author: daksh
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.captain = Captain(x, y)
                self.field[x][y] = self.captain
                break

    def initRabbits(self): #author: daksh
        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self.rabbits.append(rabbit)
                    self.field[x][y] = rabbit
                    break
    
    def initSnake(self): #author: daksh
        while True:
            x = random.randint(0, len(self.field) - 1)
            y = random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.__snake = Snake(x, y)
                self.field[x][y] = self.__snake
                break

    def initializeGame(self): #author: dev
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()
    
    def remainingVeggies(self):#author: shucheera
        count = 0
        for row in self.field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self): #author: shucheera

        print("Welcome to the Vegetable Harvest Game!")
        print("Premise:")
        print("You are Captain Veggie, on a mission to harvest as many delicious vegetables as possible.")
        print("Avoid the rabbits and navigate through the field to collect veggies.")
        print("Goal:")
        print("Harvest as many vegetables as you can to maximize your score.")
        print("Symbols:")
        print(f"Captain Veggie: {self.captain.get_symbol()}")
        print(f"Rabbit: {self.rabbits[0].get_symbol()}")
        print(f"Snake: {self.__snake.get_symbol()}")
        print("Vegetables:")
        for veggie in self.vegetables:
            print(f"Symbol: {veggie.get_symbol()}, Name: {veggie._name}, Points: {veggie.getpoints()}")
    
    def printField(self): #author: Daksh
        # Calculate the width of the field dynamically
        field_width = len(self.field[0]) if self.field and len(self.field) > 0 else 0

        # Construct the boundary string
        boundary = "+" + "-" * (2 * field_width + 1) + "+"

        # Print the field
        print("Field:")
        print(boundary)
        for row in self.field:
            print("|", end=' ')
            for item in row:
                if item is not None:
                    print(item.get_symbol(), end=' ')
                else:
                    print(' ', end=' ')
            print("|")
        print(boundary)

    def getScore(self): #author: daksh
        return self.score

    def moveRabbits(self): #author: daksh
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
                # Update the field: set the previous location to None, move the rabbit
                self.field[x][y] = None
                self.field[new_x][new_y] = rabbit
                # Update the rabbit's position
                rabbit.set_x(new_x)
                rabbit.set_y(new_y)
    
    def moveCptVertical(self,vertimovement): #author: daksh

        # next 2 variables store the position of the captain before it is changed in order to set it to None later
        new_x=self.captain.get_x() + vertimovement
        new_y=self.captain.get_y()
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
      
    def moveCptHorizontal(self, movement): #author: daksh
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
 
    def moveCaptain(self): #author: daksh
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
    
    # def moveSnake(self): #author: daksh
    #     if self.__snake is not None and self.captain is not None:
    #         snake_x, snake_y = self.__snake.get_x(), self.__snake.get_y()
    #         captain_x, captain_y = self.captain.get_x(), self.captain.get_y()

    #         diff_x = abs(snake_x - captain_x)
    #         diff_y = abs(snake_y - captain_y)

    #         if diff_x > diff_y:
    #             # Move in x direction
    #             move_x = 1 if captain_x > snake_x else -1
    #             new_x = snake_x + move_x
    #             new_y = snake_y
    #         else:
    #             # Move in y direction
    #             move_y = 1 if captain_y > snake_y else -1
    #             new_y = snake_y + move_y
    #             new_x = snake_x

    #         if 0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0]) and self.field[new_x][new_y] is None:
    #             self.field[snake_x][snake_y] = None
    #             self.field[new_x][new_y] = self.__snake
    #             self.__snake.set_x(new_x)
    #             self.__snake.set_y(new_y)
    #         elif new_x == captain_x and new_y == captain_y:
    #             # Snake catches the captain, reset snake and remove veggies from captain
    #             print("Stepped on a snake, droping last 5 veggies")
    #             self.field[snake_x][snake_y] = None
    #             print("Veggies dropped: " + ', '.join(str(v) for v in self.captain._collectedVeggie[-5:]))
    #             self.captain._collectedVeggie = self.captain._collectedVeggie[:-5]
    #             self.initSnake()

    def moveSnake(self): #author: Daksh
        if self.__snake is not None and self.captain is not None:
            snake_x, snake_y = self.__snake.get_x(), self.__snake.get_y()
            captain_x, captain_y = self.captain.get_x(), self.captain.get_y()

            # Calculate differences in x and y
            diff_x = abs(snake_x - captain_x)
            diff_y = abs(snake_y - captain_y)

            # Decide the direction to move based on greater difference
            if diff_x > diff_y:
                # Move in x direction
                move_x = 1 if captain_x > snake_x else -1
                new_x = snake_x + move_x
                new_y = snake_y
            else:
                # Move in y direction
                move_y = 1 if captain_y > snake_y else -1
                new_y = snake_y + move_y
                new_x = snake_x

            # Check for field boundaries and object collisions
            if 0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0]) and self.field[new_x][new_y] is None:
                self.field[snake_x][snake_y] = None
                self.field[new_x][new_y] = self.__snake
                self.__snake.set_x(new_x)
                self.__snake.set_y(new_y)
            elif new_x == captain_x and new_y == captain_y:
                # Snake catches the captain, reset snake and remove veggies from captain
                print("Stepped on a snake, dropping last 5 veggies")
                self.field[snake_x][snake_y] = None
                
                # Calculate the total points of dropped veggies
                dropped_veggies_points = sum(int(v.getpoints()) for v in self.captain._collectedVeggie[-5:])
                print("Veggies dropped: " + ', '.join(str(v) for v in self.captain._collectedVeggie[-5:]))

                # Update captain's veggies and score
                self.captain._collectedVeggie = self.captain._collectedVeggie[:-5]
                self.score -= dropped_veggies_points
                
                # Reset snake's position
                self.field[snake_x][snake_y] = None
                self.initSnake()

    def gameOver(self): #author: dev, daksh
        print("The game is over")
        list1= self.captain.getcollectedVeggie()
        list2=[]
        for x in list1:
           list2.append(x.getname())
        print(f"The list of all the harvested vegetables are : {list2}")
        print(f"The total score is : {self.score}")

    def highscore(self): #author: dev
        listofhighs = []
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "rb") as inFile:
                listofhighs = pickle.load(inFile)
        x=input("Enter your initials")
        inital=x[:3]

        if len(listofhighs)==0:
             tuple1=(inital,self.score)
             listofhighs.append(tuple1)
        else:
            tuple1=(inital,self.score)
            listofhighs.append(tuple1)
            #descending order
            for x in range(len(listofhighs)):
                if tuple1[1]>listofhighs[x][1]:
                    listofhighs.insert(x,tuple1)
                    listofhighs.pop()
                    break

        print("The highscore are:\n")
        for x in range(len(listofhighs)):
            print(f"{listofhighs[x][0]} : {listofhighs[x][1]}")
        inFile = open("highscore.data", "wb")
        pickle.dump(listofhighs, inFile )
        inFile.close()