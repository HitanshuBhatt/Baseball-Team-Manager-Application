# db.py

# Import the csv module to read and write CSV files
import csv

# Import the os module to check if the file exists
import os


# Constant variable that stores the filename used for saving player data
FILENAME = 'players.csv'


# Function to read players from the CSV file
def read_players():
    """Reads players from CSV and returns a list of dictionaries."""
    
    # Create an empty list to store player data
    players_data = []
    
    # Check if the file exists
    if not os.path.exists(FILENAME):
        
        # Create an empty file if it doesn't exist (Professional requirement)
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as f:
            pass
        
        # Return the empty list since there is no data yet
        return players_data
        
    try:
        # Open the CSV file in read mode
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as f:
            
            # Create a CSV reader object
            reader = csv.reader(f)
            
            # Loop through each row in the CSV file
            for row in reader:
                
                # Ensure the row has exactly 4 fields
                if len(row) == 4:
                    
                    # Unpack the row values
                    name, pos, ab, hits = row
                    
                    # Split the full name into first and last name
                    parts = name.split(' ', 1)
                    
                    # First part becomes the first name
                    first = parts[0]
                    
                    # If a last name exists use it, otherwise leave it blank
                    last = parts[1] if len(parts) > 1 else ""
                    
                    # Append the player data as a dictionary
                    players_data.append({
                        "first_name": first,
                        "last_name": last,
                        "position": pos,
                        "at_bats": int(ab),
                        "hits": int(hits)
                    })
                    
    # Catch any unexpected errors during reading
    except Exception as e:
        print(f"Data file error during read: {e}")
        
    # Return the list of player dictionaries
    return players_data


# Function to write player data to the CSV file
def write_players(players_list):
    """Writes a list of player dictionaries back to the CSV."""
    
    try:
        # We use 'f' instead of 'file' to avoid potential shadowing
        
        # Open the CSV file in write mode (this overwrites the existing file)
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as f:
            
            # Create a CSV writer object
            writer = csv.writer(f)
            
            # Loop through each player dictionary
            for p in players_list:
                
                # Combine first and last name into a full name string
                full_name = f"{p['first_name']} {p['last_name']}".strip()
                
                # Write the player data as a row in the CSV file
                writer.writerow([full_name, p['position'], p['at_bats'], p['hits']])
                
    # Handle case where the file cannot be written because it is open elsewhere
    except PermissionError:
        print(f"ERROR: Could not save to {FILENAME}. Please close the file if it is open in Excel.")
    
    # Handle any other unexpected errors
    except Exception as e:
        print(f"Error saving data (write_players): {e}")