
    def remainingVeggies(self):
        return sum(row.count(None) for row in self.field)
#A function named remainingVeggies() that takes in no parameters, examines the field and returns the number of vegetables still in the game

    def intro(self):

        print("Welcome to the Vegetable Harvest Game!")
        print("Premise:")
        print("You are Captain Veggie, on a mission to harvest as many delicious vegetables as possible.")
        print("Avoid the rabbits and navigate through the field to collect veggies.")
        print("Goal:")
        print("Harvest as many vegetables as you can to maximize your score.")
        print("Symbols:")
        print(f"Captain Veggie: {self.captain.symbol}")
        print("Rabbit: R")
        print("Vegetables:")
        for veggie in self.vegetables:
            print(f"Symbol: {veggie.symbol}, Name: {veggie.name}, Points: {veggie.point_value}")

# The player is welcomed to the game
# The premise and goal of the game are explained
# The list of possible vegetables is output including each vegetable’s symbol, name, and point value
# Be sure to use the appropriate Veggie function for the printing
# Captain Veggie and the rabbit’s symbols are output
# Remember that you are informing the user about the game, so be sure to include appropriate messages and descriptions
