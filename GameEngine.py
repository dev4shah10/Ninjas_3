# Author: Daksh Pruthi
# Date: 11/25/2023
# Description: This module defines the GameEngine class, which manages the logic and functionality of the Captain Veggie game.
# The game involves harvesting vegetables while avoiding rabbits. The class handles initialization, player movements,
# vegetable harvesting, rabbit movements, scoring, game over conditions, and high score management.

import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie

class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__veggies = []
        self.__score = 0

    def initVeggies(self):
        veggie_file = input("Enter the name of the veggie file: ")

        while not self.fileExists(veggie_file):
            print("File not found. Please enter a valid filename.")
            veggie_file = input("Enter the name of the veggie file: ")

        with open(veggie_file, 'r') as file:
            field_size = tuple(map(int, file.readline().strip().split()))
            self.__field = [[None for _ in range(field_size[1])] for _ in range(field_size[0])]

            for line in file:
                veggie_info = line.strip().split(',')
                veggie = Veggie(veggie_info[0], veggie_info[1], int(veggie_info[2]))
                self.__veggies.append(veggie)

            for _ in range(self.NUMBEROFVEGGIES):
                while True:
                    x, y = random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1)
                    if self.__field[x][y] is None:
                        self.__field[x][y] = self.__veggies[_]
                        break

    def initCaptain(self):
        while True:
            x, y = random.randint(0, len(self.__field) - 1), random.randint(0, len(self.__field[0]) - 1)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self):
        for _ in range(self.NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, len(self.__field) - 1), random.randint(0, len(self.__field[0]) - 1)
                if self.__field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self.__rabbits.append(rabbit)
                    self.__field[x][y] = rabbit
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        count = 0
        for row in self.__field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        print("Welcome to Captain Veggie!")
        print("In this game, you need to harvest as many vegetables as possible before they are consumed by rabbits.")
        print("Move Captain Veggie using W, A, S, D and collect vegetables to score points.")
        print("Be careful not to step on rabbits!")
        print("List of possible vegetables:")
        for veggie in self.__veggies:
            print(veggie)
        print(f"Captain Veggie symbol: {self.__captain.get_symbol()}")
        print(f"Rabbit symbol: {self.__rabbits[0].get_symbol()}")

    def printField(self):
        print("Field:")
        for row in self.__field:
            print(" | ".join(str(item) if item is not None else ' ' for item in row))
            print("-" * 30)

    def getScore(self):
        return self.__score

    def moveRabbits(self):
        for rabbit in self.__rabbits:
            new_x, new_y = self.calculateNewPosition(rabbit.get_x(), rabbit.get_y())
            if self.isValidMove(new_x, new_y):
                self.__field[rabbit.get_x()][rabbit.get_y()], self.__field[new_x][new_y] = None, rabbit
                rabbit.set_x(new_x)
                rabbit.set_y(new_y)
            elif isinstance(self.__field[new_x][new_y], Veggie):
                self.__veggies.remove(self.__field[new_x][new_y])
                self.__field[new_x][new_y] = rabbit


    def moveCptVertical(self, vertical_movement):
        new_x, new_y = self.__captain.get_x() + vertical_movement, self.__captain.get_y()
        self.moveCaptainLogic(new_x, new_y)

    def moveCptHorizontal(self, horizontal_movement):
        new_x, new_y = self.__captain.get_x(), self.__captain.get_y() + horizontal_movement
        self.moveCaptainLogic(new_x, new_y)

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

    def moveCaptainLogic(self, new_x, new_y):
        if self.isValidMove(new_x, new_y):
            if self.__field[new_x][new_y] is None:
                self.__field[self.__captain.get_x()][self.__captain.get_y()], self.__field[new_x][new_y] = None, self.__captain
                self.__captain.set_x(new_x)
                self.__captain.set_y(new_y)
            elif isinstance(self.__field[new_x][new_y], Veggie):
                veggie = self.__field[new_x][new_y]
                self.__veggies.remove(veggie)
                self.__captain.add_veggie(veggie)
                self.__score += veggie.get_points()
                print(f"Delicious {veggie.get_name()} found! Score +{veggie.get_points()}")
                self.__field[self.__captain.get_x()][self.__captain.get_y()], self.__field[new_x][new_y] = None, self.__captain
                self.__captain.set_x(new_x)
                self.__captain.set_y(new_y)
            elif isinstance(self.__field[new_x][new_y], Rabbit):
                print("Oops! Don't step on the rabbits.")
        else:
            print("Invalid move. Captain cannot go outside the boundaries of the field.")

    def gameOver(self):
        print("Game Over!")
        print("Vegetables harvested by Captain Veggie:")
        for veggie in self.__captain.get_veggies_collected():
            print(f"{veggie.get_name()} ({veggie.get_symbol()}) - {veggie.get_points()} points")
        print(f"Your score: {self.__score}")

    def highScore(self):
        high_scores = []

        if self.fileExists(self.HIGHSCOREFILE):
            with open(self.HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        initials = input("Enter your initials (max 3 characters): ")[:3]
        score_entry = (initials, self.__score)

        if not high_scores:
            high_scores.append(score_entry)
        else:
            for i, (initial, score) in enumerate(high_scores):
                if self.__score > score:
                    high_scores.insert(i, score_entry)
                    break
            else:
                high_scores.append(score_entry)

        print("High Scores:")
        for i, (initial, score) in enumerate(high_scores, start=1):
            print(f"{i}. {initial}: {score}")

        with open(self.HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)

    def fileExists(self, filename):
        try:
            with open(filename, 'r'):
                pass
            return True
        except FileNotFoundError:
            return False

    def isValidMove(self, x, y):
        return 0 <= x < len(self.__field) and 0 <= y < len(self.__field[0])

    def calculateNewPosition(self, x, y):
        new_x, new_y = x, y
        while True:
            direction = random.choice(['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right'])
            if direction == 'up':
                new_x -= 1
            elif direction == 'down':
                new_x += 1
            elif direction == 'left':
                new_y -= 1
            elif direction == 'right':
                new_y += 1
            elif direction == 'up-left':
                new_x -= 1
                new_y -= 1
            elif direction == 'up-right':
                new_x -= 1
                new_y += 1
            elif direction == 'down-left':
                new_x += 1
                new_y -= 1
            elif direction == 'down-right':
                new_x += 1
                new_y += 1

            if self.isValidMove(new_x, new_y):
                break

        return new_x, new_y