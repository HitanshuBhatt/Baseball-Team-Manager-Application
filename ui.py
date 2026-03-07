# ui.py

# Import the datetime class from the datetime module
# This is used to get the current date and calculate date differences
from datetime import datetime


# Function to display the title/header of the program
def display_title():
    # Prints a decorative line of '=' characters
    print("=" * 64)
    
    # Prints the program title centered with spaces
    print("                   Baseball Team Manager")
    
    # Prints another decorative line
    print("=" * 64)


# displays the date of the game and finds the number of days till game 
def display_dates():
    
    # Get the current date and time
    now = datetime.now()
    
    # Display the current date formatted as YYYY-MM-DD
    print(f"CURRENT DATE:    {now.strftime('%Y-%m-%d')}")
    
    # Start an infinite loop to repeatedly ask for input until valid
    while True:
        
        # Prompt the user to enter the game date
        date_str = input("GAME DATE:       ")
        
        # If the user presses enter without typing anything, exit the loop
        if not date_str:
            break
        
        try:
            # Convert the input string into a datetime object
            # Expected format: YYYY-MM-DD
            game_date = datetime.strptime(date_str, "%Y-%m-%d")
            
            # Calculate the difference between the game date and current date
            delta = game_date - now
            
            # Check if the game date is today or in the future
            if delta.days >= 0:
                
                # Print the number of days until the game (including today)
                print(f"DAYS UNTIL GAME: {delta.days + 1}")
            
            # Exit the loop after successful calculation
            break
        
        # If the date format is incorrect, this exception is triggered
        except ValueError:
            
            # Inform the user that the format is invalid
            print("Invalid format. Please use YYYY-MM-DD.")
    
    # Print an empty line for better formatting
    print()


# Function to display the menu options for the program
def display_menu():
    
    # Display menu heading
    print("MENU OPTIONS")
    
    # Display each available menu option
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    
    # Display available baseball positions
    print("\nPOSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    
    # Decorative separator line
    print("=" * 64)


# Function to display the lineup of players
def display_lineup(lineup):
    
    # Check if there are no players in the lineup
    if lineup.count == 0:
        
        # Inform the user that the lineup is empty
        print("There are currently no players in the lineup.")
        
        # Exit the function
        return
        
    # Print table header with formatted column spacing
    print(f"{'':3}{'Player':<30}{'POS':<6}{'AB':>6}{'H':>6}{'AVG':>8}")
    
    # Print a separator line
    print("-" * 64)
    
    # Loop through each player in the lineup with an index starting at 1
    for i, player in enumerate(lineup, start=1):
        
        # Print the player's details formatted into aligned columns
        print(f"{i:<3}{player.full_name:<30}{player.position:<6}{player.at_bats:>6}{player.hits:>6}{player.batting_average:>8.3f}")
    
    # Print an empty line after displaying the lineup
    print()


# Function to get a valid integer input from the user  for menu option and stat editing 
def get_int(prompt, min_val, max_val):
    
    # Continue asking until a valid integer is entered
    while True:
        try:
            
            # Prompt the user and convert input to integer
            value = int(input(prompt))
            
            # Check if the value is outside the allowed range
            if value < min_val or value > max_val:
                
                # Inform the user about the valid range
                print(f"Must be between {min_val} and {max_val}.")
            
            else:
                
                # Return the valid integer
                return value
        
        # Handle cases where input cannot be converted to an integer
        except ValueError:
            
            # Inform the user that the input is invalid
            print("Invalid integer. Please try again.")


# Function to get a valid baseball position from the user
def get_position(prompt, valid_positions):
    
    # Continue asking until a valid position is entered
    while True:
        
        # Get user input and convert it to uppercase
        pos = input(prompt).upper()
        
        # Check if the entered position is valid
        if pos in valid_positions:
            
            # Return the valid position
            return pos
        
        else:
            
            # Inform the user of valid position options
            print(f"Invalid position. Valid options are: {', '.join(valid_positions)}")






            