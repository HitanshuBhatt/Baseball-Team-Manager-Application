# db.py
import csv
import os

FILENAME = r"C:\Users\Hitanshu\Documents\Python Programming\midterm\playersii.csv"

def read_players():
    """Reads players from CSV and returns a list of dictionaries."""
    players_data = []
    if not os.path.exists(FILENAME):
        # Create an empty file if it doesn't exist (Professional requirement)
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as f:
            pass
        return players_data
        
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    name, pos, ab, hits = row
                    parts = name.split(' ', 1)
                    first = parts[0]
                    last = parts[1] if len(parts) > 1 else ""
                    
                    players_data.append({
                        "first_name": first,
                        "last_name": last,
                        "position": pos,
                        "at_bats": int(ab),
                        "hits": int(hits)
                    })
    except Exception as e:
        print(f"Data file error during read: {e}")
        
    return players_data

def write_players(players_list):
    """Writes a list of player dictionaries back to the CSV."""
    try:
        # We use 'f' instead of 'file' to avoid potential shadowing
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for p in players_list:
                full_name = f"{p['first_name']} {p['last_name']}".strip()
                writer.writerow([full_name, p['position'], p['at_bats'], p['hits']])
    except PermissionError:
        print(f"ERROR: Could not save to {FILENAME}. Please close the file if it is open in Excel.")
    except OSError as e:  # Added specific handling for OSError to catch file descriptor issues
        if e.errno == 9:  # Errno 9 is Bad file descriptor, often due to file being open in another program
            print(f"ERROR: Bad file descriptor for {FILENAME}. The file may be open in another program or locked. Please close it and try again.")
        else:
            print(f"Error saving data (write_players): {e}")
    except Exception as e:
        print(f"Error saving data (write_players): {e}")