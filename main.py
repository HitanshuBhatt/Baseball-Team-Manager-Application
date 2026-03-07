# main.py-main program file 
# Import the database layer which handles reading/writing player data
import db

# Import the user interface module for displaying menus and getting input
import ui

# Import the Player and Lineup classes and POSITIONS constant from objects module
from objects import Player, Lineup, POSITIONS


# Function to load the lineup from the database and convert it into Business objects
# this function serves as the bridge between the db layer and business logic and transforms raw data into usable objects

def load_lineup():
    """Loads raw data from DB layer into Business objects."""
    
    # Create a new Lineup object to store the players 
    lineup = Lineup()
    
    # Read player data from the db file  (returns list of dictionaries) 
    raw_players = db.read_players()
    
    # Loop through each player dictionary  returned from the databse
    for p in raw_players:
        
        # Convert dictionary data into a Player object using the player constructor 
        player = Player(p['first_name'], p['last_name'], p['position'], p['at_bats'], p['hits'])
        
        # Add the Player object to the lineup
        lineup.add_player(player)
    
    # Return the populated lineup
    return lineup


# Function to save the lineup back to the database
# this function converts the business objects back into data structure that the db layer can write to the file 
def save_lineup(lineup):
    """Converts Business objects back to primitive dicts for the DB layer."""
    
    # Create an empty list to store player dictionaries
    # this is passed to the write players function in db 
    players_list = []
    
    # Loop through each player in the lineup
    for player in lineup:
        
        # Convert Player object back into a dictionary
        players_list.append({
            "first_name": player.first_name,
            "last_name": player.last_name,
            "position": player.position,
            "at_bats": player.at_bats,
            "hits": player.hits
        })
    
    # Write the list of dictionaries to the database
    db.write_players(players_list)
    

#  Function to add player to lineup
def add_player(lineup):
     
    try:
        # Ask the user for the player's first name
        first = input("First name: ").strip()
        
        # Validate that the first name is not empty
        if first == "":
            raise ValueError("First name cannot be empty.") #  error if empty

        # Ask the user for the player's last name
        last = input("Last name: ").strip()
        
        # Validate that the last name is not empty
        if last == "":
            raise ValueError("Last name cannot be empty.") #  error if empty

        # Get a valid baseball position using the UI helper function
        pos = ui.get_position("Position: ", POSITIONS)
        
        # Get the number of at-bats (validated integer)
        ab = ui.get_int("At bats: ", 0, 10000)
        
        # Validation: Cannot have more hits than at-bats
        hits = ui.get_int("Hits: ", 0, ab)
        
        # Create a new Player object with the entered data
        player = Player(first, last, pos, ab, hits)
        
        # Add the player to the lineup
        lineup.add_player(player)
        
        # Save the updated lineup to the database
        save_lineup(lineup)
        
        # Confirm the player was added
        print(f"{player.full_name} was added.\n")
        
    # Handle errors such as empty name input
    except ValueError as e:
        print(f"Error: {e} Please eneter name again.") # Print the specific error message
    

# Function to remove a player from the lineup
def remove_player(lineup):
    
    # Ask the user which player number to remove
    number = ui.get_int("Number: ", 1, lineup.count)
    
    # Remove the player from the lineup
    player = lineup.remove_player(number)
    
    # Save the updated lineup
    save_lineup(lineup)
    
    # Confirm the deletion
    print(f"{player.full_name} was deleted.\n")


# Function to move a player to a new position in the lineup
def move_player(lineup):
    
    # Ask for the current lineup position of the player
    old_num = ui.get_int("Current lineup number: ", 1, lineup.count)
    
    # Get the selected player object
    player = lineup.get_player(old_num)
    
    # Display the selected player's name
    print(f"{player.full_name} was selected.")
    
    # Ask for the new lineup position
    new_num = ui.get_int("New lineup number: ", 1, lineup.count)
    
    # Move the player to the new position
    lineup.move_player(old_num, new_num)
    
    # Save the updated lineup
    save_lineup(lineup)
    
    # Confirm the move
    print(f"{player.full_name} was moved.\n")


# Function to edit a player's position
def edit_position(lineup):
    
    # Ask the user for the lineup number
    number = ui.get_int("Lineup number: ", 1, lineup.count)
    
    # Retrieve the selected player
    player = lineup.get_player(number)
    
    # Display current player and position
    print(f"You selected {player.full_name} POS={player.position}")
    
    # Get the new valid position
    new_pos = ui.get_position("New position: ", POSITIONS)
    
    # Update the player's position
    player.position = new_pos
    
    # Save the updated lineup
    save_lineup(lineup)
    
    # Confirm update
    print(f"{player.full_name} was updated.\n")


# Function to edit a player's statistics
def edit_stats(lineup):
    
    # Ask the user for the lineup number
    number = ui.get_int("Lineup number: ", 1, lineup.count)
    
    # Retrieve the selected player
    player = lineup.get_player(number)
    
    # Display the current stats
    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")
    
    # Get new at-bats value
    ab = ui.get_int("At bats: ", 0, 10000)
    
    # Get new hits value (cannot exceed at-bats)
    hits = ui.get_int("Hits: ", 0, ab)
    
    # Update the player's statistics
    player.at_bats = ab
    player.hits = hits
    
    # Save the updated lineup
    save_lineup(lineup)
    
    # Confirm update
    print(f"{player.full_name} was updated.\n")


# Main program function
def main():
    
    # Display the program title
    ui.display_title()
    
    # Display the date information
    ui.display_dates()
    
    # Display the menu options
    ui.display_menu()
    
    # Load lineup data from the database
    lineup = load_lineup()
    
    # Infinite loop to keep the program running until user exits
    while True:
        try:
            # Ask the user to choose a menu option
            option = int(input("Menu option: "))
        
        # Handle invalid integer input
        except ValueError:
            print("Invalid integer. Please try again.")
            ui.display_menu()
            continue
            
        # Option 1: Display lineup
        if option == 1:
            ui.display_lineup(lineup)
        
        # Option 2: Add a player
        elif option == 2:
            add_player(lineup)
        
        # Option 3: Remove a player
        elif option == 3:
            remove_player(lineup)
        
        # Option 4: Move a player
        elif option == 4:
            move_player(lineup)
        
        # Option 5: Edit player position
        elif option == 5:
            edit_position(lineup)
        
        # Option 6: Edit player stats
        elif option == 6:
            edit_stats(lineup)
        
        # Option 7: Exit program
        elif option == 7:
            print("Bye!")
            break
        
        # Handle invalid menu options
        else:
            print("Not a valid menu option. Please try again.\n")
            ui.display_menu()


# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()