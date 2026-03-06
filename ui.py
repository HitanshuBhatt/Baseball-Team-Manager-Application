# ui.py
from datetime import datetime

def display_title():
    print("=" * 64)
    print("                   Baseball Team Manager")
    print("=" * 64)

# displays the date of the game and finds the number of days till game 
def display_dates():
    now = datetime.now()
    print(f"CURRENT DATE:    {now.strftime('%Y-%m-%d')}")
    while True:
        date_str = input("GAME DATE:       ")
        if not date_str:
            break
        try:
            game_date = datetime.strptime(date_str, "%Y-%m-%d")
            delta = game_date - now
            if delta.days >= 0:
                print(f"DAYS UNTIL GAME: {delta.days + 1}")
            break
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")
    print()

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("=" * 64)

def display_lineup(lineup):
    if lineup.count == 0:
        print("There are currently no players in the lineup.")
        return
        
    print(f"{'':3}{'Player':<30}{'POS':<6}{'AB':>6}{'H':>6}{'AVG':>8}")
    print("-" * 64)
    for i, player in enumerate(lineup, start=1):
        print(f"{i:<3}{player.full_name:<30}{player.position:<6}{player.at_bats:>6}{player.hits:>6}{player.batting_average:>8.3f}")
    print()

def get_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"Must be between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid integer. Please try again.")

def get_position(prompt, valid_positions):
    while True:
        pos = input(prompt).upper()
        if pos in valid_positions:
            return pos
        else:
            print(f"Invalid position. Valid options are: {', '.join(valid_positions)}")