class _Vegetable:
    def __init__(self, name):
        self.name = name
        
class _Rabbit:
    def __init__(self, name):
        self.name = name

class Game:
    _NUMBEROFVEGGIES = 30 
    #A private constant to store the initial number of vegetables in the game named NUMBEROFVEGGIES, initialized to 30
    _NUMBEROFRABBITS = 5
    # A private constant to store the number of rabbits in the game named NUMBEROFRABBITS,initialized to 5
    _HIGHSCOREFILE = "highscore.data"
    #A private constant to store the name of the high score file named HIGHSCOREFILE, initialized to “highscore.data”

    def __init__(self):
        # Initialize member variables

        self.field = []
        #Declare a new, member variable to store an empty List representing the field
        self.rabbits = []
        #Declare a new, member variable to store an empty List representing the rabbits in the field
        self.captain = None
        #Declare a new, member variable to store the captain object, initialized to None
        self.vegetables = []
        #Declare a new, member variable to store an empty List representing all of the possible vegetables in the game
        self.score = 0
        #Declare a new, member variable to store the score, initialized to 0

        # Populate the vegetables list with Vegetable objects
        #vegetable_names = ["Carrot", "Lettuce", "Broccoli", "Tomato", "Cucumber"]
     #uncomment the above line if required!

    # Other methods for the Game class can be added here
