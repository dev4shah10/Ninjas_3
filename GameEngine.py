from asyncio.windows_events import NULL
class GameEngine:
    def moveCptHorizontal(self, movement):
        current_row = self.captain.row
        current_col = self.captain.col
#A function named moveCptHorizontal(), that takes in a value representing the horizontal movement of the Captain object, returns nothing, and in which:
        new_col = current_col + movement
    
        #If the Captain object’s current position plus the movement would move them into an empty slot in field
        if 0 <= new_col < len(self.field[0]):
            if self.field[current_row][new_col] is None:
                # Move to an empty slot
                self.field[current_row][current_col] = None
                #Update their appropriate member variable
                self.captain.col = new_col
                self.field[current_row][new_col] = self.captain
                #Assign them to the new location in field

            elif isinstance(self.field[current_row][new_col], Veggie):
                #Otherwise, if the Captain object’s current position plus the movement would move them into a space occupied by a Veggie object
                veggie = self.field[current_row][new_col]
                # Update the Captain object’s appropriate member variable
                print(f"Found a delicious {veggie.name}!")
                #Output that a delicious vegetable, using the Veggie object’s name, has been found
                self.captain.veggies_harvested.append(veggie)
                #Add the Veggie object to the Captain object’s List of Veggies using the appropriate function
                self.score += veggie.point_value
                #Increment the score by the Veggie object’s point value
                # Move Captain to the new location
                self.field[current_row][current_col] = None
                self.captain.col = new_col
                #Assign the Captain object to the new location in field
                self.field[current_row][new_col] = self.captain

            elif isinstance(self.field[current_row][new_col], Rabbit):
                #Otherwise, if the Captain object’s current position plus the movement would move them into a space occupied by a Rabbit object
                # Found a Rabbit, inform the player not to step on them
                print("Oops! Don't step on the rabbits.")
                # Inform the player that they should not step on the rabbits
            else:
                # Another unexpected object at the new location
                print("Unexpected object at the new location!")
                #Do not move the Captain object

            # Set the Captain object’s previous location in field to None if it has moved
            self.field[current_row][current_col] = None
            #Make sure you set the Captain object’s previous location in field to none if it has moved to a new location

