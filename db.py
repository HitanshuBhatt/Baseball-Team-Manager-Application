# db.py
import csv
import os

FILENAME = 'players.csv'

def read_players():
    """Reads players from CSV and returns a list of dictionaries."""
    players = []
    if not os.path.exists(FILENAME):
        return players # Handles missing file gracefully
        
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    name, pos, ab, hits = row
                    # Split full name into first and last for the Object requirements
                    parts = name.split(' ', 1)
                    first = parts[0]
                    last = parts[1] if len(parts) > 1 else ""
                    
                    players.append({
                        "first_name": first,
                        "last_name": last,
                        "position": pos,
                        "at_bats": int(ab),
                        "hits": int(hits)
                    })
    except Exception as e:
        print(f"Data file error: {e}")
        
    return players

def write_players(players_list):
    """Writes a list of player dictionaries back to the CSV."""
    try:
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for p in players_list:
                full_name = f"{p['first_name']} {p['last_name']}".strip()
                writer.writerow([full_name, p['position'], p['at_bats'], p['hits']])
    except Exception as e:
        print(f"Error saving data: {e}")