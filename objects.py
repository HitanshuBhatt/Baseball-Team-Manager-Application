# objects.py

# Tuple to store all valid baseball positions
# This acts as a constant list of positions that players can have
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


# Player class represents a single baseball player
class Player:
    
    # Constructor method that initializes a new player object
    # Stores the player's first name, last name, position, at-bats, and hits
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name      # Player's first name
        self.last_name = last_name        # Player's last name
        self.position = position          # Player's field position
        self.at_bats = at_bats            # Number of times the player has batted
        self.hits = hits                  # Number of successful hits


    # Property method that returns the player's full name
    # Combines first name and last name into a single string
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    # Property method that calculates the batting average
    # Batting average = hits ÷ at_bats
    @property
    def batting_average(self):
        
        # Prevent division by zero if the player has no at-bats
        if self.at_bats == 0:
            return 0.0
        
        # Return the batting average rounded to 3 decimal places
        return round(self.hits / self.at_bats, 3)


# Lineup class represents the entire baseball team lineup
class Lineup:
    
    # Constructor initializes the lineup
    def __init__(self):
        
        # Encapsulated private list that stores Player objects
        # Double underscore makes this variable private to the class
        self.__players = []


    # Method to add a new player to the lineup
    def add_player(self, player):
        
        # Append the player object to the private players list
        self.__players.append(player)


    # Method to remove a player from the lineup
    def remove_player(self, number):
        
        # Subtract 1 because UI shows 1-based index but Python lists use 0-based index
        return self.__players.pop(number - 1)


    # Method to move a player from one position in the lineup to another
    def move_player(self, old_number, new_number):
        
        # Remove the player from their current position
        player = self.__players.pop(old_number - 1)
        
        # Insert the player into the new position
        self.__players.insert(new_number - 1, player)


    # Method to retrieve a player from the lineup by their position number
    def get_player(self, number):
        
        # Return the player object (convert from 1-based index to 0-based index)
        return self.__players[number - 1]


    # Property that returns the total number of players in the lineup
    @property
    def count(self):
        
        # len() counts the number of elements in the players list
        return len(self.__players)


    # Iterator method that allows the lineup to be iterated over in a for loop 
    # like: for player in lineup  
    def __iter__(self):
        
        # Yield each player in the lineup one at a time, allowing for iteration
        for player in self.__players:
            yield player