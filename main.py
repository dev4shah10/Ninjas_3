# Author: Daksh Pruthi
# Date: 11/25/2023
# Description: main.py

from GameEngine import GameEngine

def main():
    """
    Main function to run the Captain Veggie game.
    """
    # Instantiate and store a GameEngine object
    game_engine = GameEngine()

    # Initialize the game
    game_engine.initializeGame()

    # Display the game’s introduction
    game_engine.intro()

    # Create a variable to store the number of remaining vegetables
    remaining_vegetables = game_engine.remainingVeggies()

    # While there are still vegetables left in the game
    while remaining_vegetables > 0:
        # Output the number of remaining vegetables and the player’s score
        print(f"{remaining_vegetables} veggies remaining. Current score: {game_engine.getScore()}\n")

        # Print out the field
        game_engine.printField()

        # Move the rabbits
        game_engine.moveRabbits()

        # Move the captain
        game_engine.moveCaptain()

        # Move snake
        game_engine.moveSnake()

        # Determine the new number of remaining vegetables
        remaining_vegetables = game_engine.remainingVeggies()

    # Display the Game Over information
    game_engine.gameOver()

    # Handle the High Score functionality
    game_engine.highscore()

if __name__ == "__main__":
    main()